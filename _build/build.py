#!/usr/bin/env python3
"""Orchestrator. Regenerates every page, sitemap.xml, robots.txt, the web
manifest and the icon set. Output is written in place — the parent directory
is the deployable site.

Usage:  python3 _build/build.py
"""
import os, re, sys, json, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from lib import ROOT, SITE, DOMAIN, NAME, PAGES, save_lastmod
import favicon
import keywords

MODULES = ["p_home", "p_casinos", "p_categories", "p_betting",
           "p_reviews", "p_guides", "p_site"]

# SEO-tool crawlers are blocked at the user-agent level, as specified. They burn
# crawl budget and hand competitors a free map of the site in return for nothing.
# Search engines and the AI crawlers we want indexing us are left alone.
BLOCKED = ["AhrefsBot", "SemrushBot", "MJ12bot", "DotBot", "Rogerbot",
           "serpstatbot", "SistrixBot", "BLEXBot", "DataForSeoBot",
           "Barkrowler", "ZoominfoBot", "SEOkicks", "LinkpadBot", "spbot",
           "Screaming Frog SEO Spider", "PetalBot", "Seekport Crawler",
           "MegaIndex", "Cliqzbot"]


def sitemap():
    rows = []
    for path, date, pri, freq in sorted(PAGES, key=lambda p: (-p[2], p[0])):
        rows.append("  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n"
                    "    <changefreq>%s</changefreq>\n    <priority>%.1f</priority>\n  </url>"
                    % (SITE, path, date, freq, pri))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(xml)
    return len(rows)


def robots():
    out = ["# robots.txt for %s" % SITE,
           "# %s — regenerated %s" % (NAME, datetime.date.today().isoformat()), ""]
    for ua in BLOCKED:
        out += ["User-agent: %s" % ua, "Disallow: /", ""]
    out += ["# Everything else is welcome.",
            "User-agent: *",
            "Allow: /",
            "Disallow: /_build/",
            "Disallow: /docs/",
            "Disallow: /*?",
            "",
            "Sitemap: %s/sitemap.xml" % SITE,
            ""]
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write("\n".join(out))


def manifest():
    m = {"name": NAME, "short_name": "CasinoEdge", "start_url": "/",
         "scope": "/", "display": "standalone", "lang": "en-NZ", "dir": "ltr",
         "background_color": "#0A0F1C", "theme_color": "#0A0F1C",
         "description": "Independent New Zealand casino and betting reviews.",
         "categories": ["news", "reference"],
         "icons": [{"src": "/favicon-%dx%d.png" % (s, s), "sizes": "%dx%d" % (s, s),
                    "type": "image/png",
                    "purpose": "any maskable" if s >= 192 else "any"}
                   for s in (48, 96, 144, 192, 512)]}
    json.dump(m, open(os.path.join(ROOT, "site.webmanifest"), "w"), indent=1)



def prune():
    """Delete pages left behind by a URL change. Without this a rename leaves the
    old URL live, which is a duplicate of the new one and splits its signals."""
    live = set(p for p, _, _, _ in PAGES)
    removed = []
    for dirpath, dirnames, files in os.walk(ROOT, topdown=False):
        dirnames[:] = [d for d in dirnames if d not in ("_build", "assets", "logos", "images")]
        if "index.html" not in files:
            continue
        rel = os.path.relpath(dirpath, ROOT)
        url = "/" if rel == "." else "/" + rel.replace(os.sep, "/") + "/"
        if url in live:
            continue
        os.remove(os.path.join(dirpath, "index.html"))
        removed.append(url)
        try:
            os.rmdir(dirpath)
        except OSError:
            pass
    return removed


def redirects():
    """301s for every retired URL, in the formats the usual static hosts read.
    All permanent; none of them is a meta-refresh or a JavaScript hop."""
    rs = sorted(keywords.REDIRECTS.items())

    # Netlify / Cloudflare Pages
    out = ["# 301 redirects for retired URLs — %s" % NAME, "# <old>  <new>  <status>", ""]
    out += ["%-34s %-32s 301!" % (a, b) for a, b in rs]
    open(os.path.join(ROOT, "_redirects"), "w").write("\n".join(out) + "\n")

    # Apache
    ht = ["# %s — 301 redirects for retired URLs" % NAME,
          "<IfModule mod_rewrite.c>", "  RewriteEngine On"]
    ht += ["  RewriteRule ^%s$ %s [R=301,L]" % (a.lstrip("/"), b) for a, b in rs]
    ht += ["</IfModule>", "",
           "# extensionless URLs are directories with an index.html; no rewrite needed"]
    open(os.path.join(ROOT, ".htaccess"), "w").write("\n".join(ht) + "\n")

    # Vercel
    json.dump({"redirects": [{"source": a.rstrip("/"), "destination": b, "permanent": True}
                             for a, b in rs]},
              open(os.path.join(ROOT, "vercel.json"), "w"), indent=1)

    # nginx
    ng = ["# %s — include inside the server block" % NAME]
    ng += ["rewrite ^%s$ %s permanent;" % (a, b) for a, b in rs]
    open(os.path.join(ROOT, "nginx-redirects.conf"), "w").write("\n".join(ng) + "\n")
    return len(rs)


def _rx(term):
    """A term matches in its natural forms, not just verbatim.

    "paysafecard casino nz" is credited by "Paysafecard casinos in NZ" and by
    "Paysafecard casino deposits in New Zealand". Tokens must stay in order,
    nouns may be plural, "nz" and "new zealand" are interchangeable, and up to
    two filler words may sit between tokens. This is what lets the copy read
    like English instead of like a keyword list."""
    parts = []
    for tok in term.lower().split():
        if tok == "nz":
            parts.append(r"(?:nz|new zealand)")
        elif tok.startswith("$"):
            parts.append(r"\$?\s?" + re.escape(tok[1:]))
        elif tok[0].isalpha():
            parts.append(re.escape(tok) + r"(?:s|es)?")
        else:
            parts.append(re.escape(tok))
    return re.compile(r"(?:\b|^)" + r"\W+(?:\w+\W+){0,2}?".join(parts) + r"\b")


def audit_keywords():
    """Two counts per term: exact (what looks spammy when repeated) and loose
    (what actually demonstrates coverage). Tier 1 needs both."""
    import html as _h
    text = {}
    for path, _, _, _ in PAGES:
        d = ROOT if path == "/" else os.path.join(ROOT, path.strip("/"))
        raw = open(os.path.join(d, "index.html"), encoding="utf-8").read()
        raw = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
        raw = re.sub(r"<style.*?</style>", " ", raw, flags=re.S)
        body = _h.unescape(re.sub(r"<[^>]+>", " ", raw)).lower()
        body = body.replace("\u2019", "'").replace("\u2014", " ").replace("\u2013", " ")
        body = re.sub(r"\s+", " ", body)
        text[path] = (body, len(body.split()))

    problems, report = [], []
    for path, spec in sorted(keywords.PAGES.items()):
        if path not in text:
            problems.append("%s: page missing" % path)
            continue
        body, words = text[path]
        loose_total = 0
        for term in spec["t1"]:
            exact = body.count(term.lower())
            loose = len(_rx(term).findall(body))
            loose_total += loose
            if loose < keywords.MIN_T1_HITS:
                problems.append("%s: tier-1 %r %dx loose (need %d)"
                                % (path, term, loose, keywords.MIN_T1_HITS))
            elif exact == 0 and term == spec["t1"][0]:
                # the head term should read naturally enough to appear as written
                problems.append("%s: head term %r never appears verbatim" % (path, term))
            if exact * len(term.split()) / max(words, 1) > keywords.MAX_DENSITY:
                problems.append("%s: tier-1 %r over-used verbatim (%dx in %d words)"
                                % (path, term, exact, words))
        t2 = [t for t in spec["t2"] if _rx(t).search(body)]
        for t in spec["t2"]:
            if t not in t2:
                problems.append("%s: tier-2 %r not covered" % (path, t))
        tail = [t for t in spec["tail"] if _rx(t).search(body)]
        report.append((path, words, loose_total, len(spec["t1"]),
                       len(t2), len(spec["t2"]), len(tail), len(spec["tail"])))
    return report, problems


def main():
    n_icons = favicon.build(ROOT)
    print("  ok icons (%d files)" % n_icons)
    for name in MODULES:
        try:
            mod = __import__(name)
        except ImportError as e:
            print("  .. %s not present (%s), skipping" % (name, e))
            continue
        mod.build()
        print("  ok %s" % name)
    gone = prune()
    if gone:
        print("  .. pruned %d retired URL(s): %s" % (len(gone), ", ".join(gone)))
    n = sitemap()
    robots()
    manifest()
    nr = redirects()
    save_lastmod()
    report, problems = audit_keywords()
    print("\n  keyword coverage")
    print("  %-30s %6s %8s %8s %8s" % ("page", "words", "tier1", "tier2", "long-tail"))
    for path, w, h1, n1, t2, n2, tl, nl in report:
        print("  %-30s %6d %8s %8s %8s"
              % (path, w, "%d hits/%d" % (h1, n1), "%d/%d" % (t2, n2), "%d/%d" % (tl, nl)))
    if problems:
        print("\n  !! %d keyword problem(s):" % len(problems))
        for p_ in problems[:40]:
            print("     -", p_)
    else:
        print("\n  keyword audit clean")
    print("\n%d pages written. sitemap.xml, robots.txt, site.webmanifest and %d redirects updated." % (n, nr))
    print("Domain is set to %s — change DOMAIN in _build/lib.py and rebuild to swap it." % DOMAIN)


if __name__ == "__main__":
    main()
