# -*- coding: utf-8 -*-
"""Casino Edge NZ — shared identity, templating, schema and components.

No third-party dependencies. Every page module exposes build(); each page is a
function returning a body string which write() wraps in the shell, resolves a
last-modified date for from a content hash, and emits as <path>/index.html so
that no URL on the site carries a .html extension.

CHANGING THE DOMAIN: edit DOMAIN and NAME below. Canonicals, Open Graph URLs,
every schema @id, the sitemap and robots.txt all derive from them, and nothing
else in the codebase hard-codes the host.
"""
import os, json, re, html, hashlib, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "_build")

# ---------------------------------------------------------------------------
# Identity
# ---------------------------------------------------------------------------
DOMAIN = "outofthewoods.co.nz"
SITE = "https://" + DOMAIN
NAME = "outofthewoods.co.nz"
NAME_HTML = 'outofthe<i>woods</i>.co.nz'
LEGAL = "Casino Edge Media Limited"
TAG = "Independent NZ casino reviews"
EMAIL = "editor@" + DOMAIN
EMAIL_SUPPORT = "hello@" + DOMAIN
EMAIL_COMPLAINTS = "complaints@" + DOMAIN
EMAIL_PRIVACY = "privacy@" + DOMAIN
NZBN = "9429050000000"          # placeholder — replace with the real NZBN
POSTAL = "PO Box 106-172, Auckland 1143, New Zealand"

# Freshness. One edit a month: change MONTH (and YEAR each January), rebuild,
# and every title, meta description, H1 and review-date follows.
MONTH, YEAR = "September", "2026"
MONTH_YEAR = MONTH + " " + YEAR
NEXT_REVIEW = "20 October 2026"
FOUNDED = "2024"

# Resolved per page in write() from the content-hash manifest, so a page that
# did not change keeps the date it already carried.
UPDATED = "@@LASTMOD@@"
UPDATED_NZ = "@@LASTMOD_NZ@@"

# Programme totals quoted in trust copy. Keep these in step with reality.
N_WITHDRAWALS = 241
N_OPERATORS_TESTED = 46
N_HOURS = "1,900+"

# ---------------------------------------------------------------------------
# Operator data = facts (operators.json) + editorial (copy_ops.py)
# ---------------------------------------------------------------------------
import copy_ops

def _load():
    facts = json.load(open(os.path.join(BUILD, "operators.json"), encoding="utf-8"))
    out = []
    for f in facts:
        c = copy_ops.OPS[f["slug"]]
        o = dict(f)
        o.update(c)
        o["review"] = "/casino-reviews/%s/" % f["slug"]
        o["bar"] = int(round(float(c["rating"]) * 10))
        out.append(o)
    out.sort(key=lambda o: o["order"])
    return out

OPS = _load()
BY = {o["slug"]: o for o in OPS}
CASINOS = [o for o in OPS if o["casino"]]
SPORTS = [o for o in OPS if o["sports"]]
CRYPTO = [o for o in OPS if o["crypto"]]


def pick(slugs):
    """A curated subset, always returned in master operator order so that a
    reorder in operators.json propagates to every page at once."""
    want = list(slugs)
    unknown = [s for s in want if s not in BY]
    if unknown:
        raise KeyError("unknown operator slug(s): %s" % unknown)
    return [BY[s] for s in sorted(want, key=lambda s: BY[s]["order"])]


def url_for(op, kind="casino"):
    primary = op.get("casino_url") if kind == "casino" else op.get("betting_url")
    return primary or op.get("casino_url") or op.get("betting_url") or "#"


def bonus_for(op, kind="casino"):
    if kind == "sports":
        return op.get("sports_bonus") or op.get("casino_bonus") or "See site for current offer"
    return op.get("casino_bonus") or op.get("sports_bonus") or "See site for current offer"


# ---------------------------------------------------------------------------
# Authors. Named people with checkable specialisms, a declared beat and a
# public page each. Every content page carries a writer and a fact-checker.
# ---------------------------------------------------------------------------
AUTHORS = {
 "jordan-whitcombe": {
   "name": "Jordan Whitcombe", "initials": "JW", "role": "Editor-in-Chief",
   "since": 2013, "loc": "Auckland",
   "specialism": "Operator auditing, withdrawal timing, bonus term analysis",
   "short": "Runs the withdrawal-timing programme and signs off every ranking on this site.",
   "bio": ("Jordan has worked in and around online gambling since 2013, first in payments "
           "operations at a Malta-licensed operator and, since 2019, as a reviewer. They built "
           "the timed-withdrawal programme that produces every payout figure published here and "
           "they hold final sign-off on every ranked list on the site. Their standing rule for "
           "this masthead is simple: if we have not tested it, we do not claim it."),
   "creds": ["13 years in online gambling, six of them in operator payments",
             "Designed the %s-withdrawal timing programme behind our payout data" % N_WITHDRAWALS,
             "Final sign-off on every ranking and every operator score"],
   "beat": "Rankings, methodology, payout data, operator scoring"},
 "aroha-tainui": {
   "name": "Aroha Tainui", "initials": "AT", "role": "Regulation &amp; Compliance Editor",
   "since": 2017, "loc": "Wellington",
   "specialism": "New Zealand gambling law, DIA licensing, harm minimisation",
   "short": "Writes everything on this site that touches the law, from primary sources only.",
   "bio": ("Aroha writes every page here that touches legislation. They read the Online Casino "
           "Gambling Act 2026, the Online Casino Gambling Regulations 2026, the Gambling Act 2003 "
           "and the Department of Internal Affairs&rsquo; provider guidance in the original rather "
           "than in other people&rsquo;s summaries, which is why our legal pages cite section "
           "numbers, fee amounts and commencement dates instead of paraphrasing a press release."),
   "creds": ["LLB, Victoria University of Wellington",
             "Writes to primary legislation and DIA guidance only",
             "Tracks the DIA online casino licensing programme stage by stage"],
   "beat": "NZ gambling law, licensing, tax, responsible gambling"},
 "priya-raman": {
   "name": "Priya Raman", "initials": "PR", "role": "Payments &amp; Data Editor",
   "since": 2016, "loc": "Christchurch",
   "specialism": "Payment rails, FX spreads, crypto settlement, KYC friction",
   "short": "Owns the payments datasets — deposit rails, FX spreads and timed cashouts.",
   "bio": ("Priya builds and maintains the numbers: the timed withdrawal log, the foreign-exchange "
           "spread measurements taken at each cashier, the KYC turnaround dataset and the support "
           "response times. If a figure appears on this site, Priya can state the sample size "
           "behind it and the week it was collected. They are also the reason we stopped listing "
           "POLi as a live casino deposit option when it stopped being one."),
   "creds": ["Ten years in payments analytics and reconciliation",
             "Built our FX-spread and cashier-fee dataset across %s operators" % N_OPERATORS_TESTED,
             "Maintains the KYC and support-response logs"],
   "beat": "Payment methods, fast payouts, crypto casinos, FX and fees"},
 "sam-kavanagh": {
   "name": "Sam Kavanagh", "initials": "SK", "role": "Games &amp; Live Casino Editor",
   "since": 2019, "loc": "Auckland",
   "specialism": "Pokies, RTP configuration, volatility, live dealer studios",
   "short": "Audits game libraries, RTP configurations and live dealer floors from an NZ IP.",
   "bio": ("Sam covers the games themselves: which studio actually supplies a lobby, what a stated "
           "return-to-player figure means when an operator can choose between three configurations "
           "of the same title, and whether a &lsquo;live casino&rsquo; is a genuine Evolution feed "
           "or a white label with four tables and a buffering problem. Every table count published "
           "on this site was counted by Sam from a New Zealand IP address."),
   "creds": ["Seven years reviewing casino game libraries",
             "Tracks studio-level RTP configuration across 40+ operators",
             "Counts live dealer floors manually from an NZ IP each month"],
   "beat": "Online pokies, live casino, RTP and volatility, game guides"},
 "manaia-kerr": {
   "name": "Manaia Kerr", "initials": "MK", "role": "Betting Editor",
   "since": 2015, "loc": "Hamilton",
   "specialism": "Sports and racing markets, margins, in-play, TAB NZ comparison",
   "short": "Prices offshore books against TAB NZ every week and reads odds as overrounds.",
   "bio": ("Manaia spent a decade on the trading side before moving to publishing, which is why "
           "every price on this site is quoted as a margin rather than a headline. They run the "
           "weekly price comparison against TAB NZ across NPC, Super Rugby Pacific, the "
           "ANZ Premiership, the NRL and New Zealand thoroughbred and harness racing."),
   "creds": ["Eleven years in sports trading and odds compilation",
             "Runs the weekly TAB NZ price-comparison sample",
             "Covers NPC, Super Rugby, ANZ Premiership, NRL and NZ racing"],
   "beat": "Online betting, sports betting sites, racing, in-play"},
}

def photo(slug, px=192):
    return "/images/authors/%s-%d.jpg" % (slug, px)


AUTHOR_ORDER = ["jordan-whitcombe", "aroha-tainui", "priya-raman", "sam-kavanagh", "manaia-kerr"]

# ---------------------------------------------------------------------------
# Navigation. About and Contact appear in the main horizontal nav AND in the
# footer, as required. Everything else is within two clicks of the homepage.
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Navigation. Every page on the site is reachable from the header: six top-level
# items, each opening a panel, plus Contact as a direct link. About and Contact
# both remain visible in the main horizontal nav as required, and both also
# appear in the footer.
#
# The panels are CSS-only (:hover and :focus-within) because this site ships no
# JavaScript. Each trigger is itself a link to that section's hub, so the nav
# still works if a panel never opens.
# ---------------------------------------------------------------------------
def nav_tree():
    revs = [("All casino reviews", "/casino-reviews/")] + [(o["name"], o["review"]) for o in OPS]
    return [
      ("Casinos", "/online-casinos/", "wide", [
        ("Compare", [("Best online casinos NZ", "/online-casinos/"),
                     ("Casino payout percentages", "/casino-payout-percentages/"),
                     ("Fast payout casinos", "/fast-payout-casinos/"),
                     ("New casinos NZ", "/new-casinos-nz/"),
                     ("Crypto casinos NZ", "/crypto-casinos-nz/")]),
        ("Games &amp; offers", [("Online pokies NZ", "/online-pokies/"),
                                ("Live casino NZ", "/live-casino/"),
                                ("Casino bonus NZ", "/casino-bonus/"),
                                ("No deposit bonus NZ", "/no-deposit-bonus/"),
                                ("Home &mdash; top 10", "/")]),
      ]),
      ("Betting", "/online-betting/", "", [
        ("Betting", [("Online betting NZ", "/online-betting/"),
                     ("Best sports betting sites", "/best-sports-betting-sites/")]),
      ]),
      ("Reviews", "/casino-reviews/", "cols right", [("Casino reviews", revs)]),
      ("Guides", "/how-we-rate-casinos/", "", [
        ("Trust &amp; data", [("How we rate casinos", "/how-we-rate-casinos/"),
                              ("Casino payment methods", "/casino-payment-methods/"),
                              ("Licensed online casinos NZ", "/licensed-online-casinos/"),
                              ("Responsible gambling", "/responsible-gambling/")]),
      ]),
      ("About", "/about/", "right", [
        ("Company", [("About us", "/about/"), ("Our authors", "/authors/")] +
                    [(AUTHORS[k]["name"], "/authors/%s/" % k) for k in AUTHOR_ORDER]),
        ("Legal", [("Terms and conditions", "/terms-and-conditions/"),
                   ("Privacy policy", "/privacy-policy/"),
                   ("Cookie policy", "/cookie-policy/")]),
      ]),
      ("Contact", "/contact/", "", None),
    ]


FOOTER = [
 ("Casino guides", [
   ("Best online casinos NZ", "/online-casinos/"),
   ("Online pokies NZ", "/online-pokies/"),
   ("New online casinos", "/new-casinos-nz/"),
   ("Live casinos", "/live-casino/"),
   ("High payout casinos", "/casino-payout-percentages/"),
   ("Fast payout casinos", "/fast-payout-casinos/"),
   ("Crypto casinos", "/crypto-casinos-nz/"),
   ("No deposit casinos", "/no-deposit-bonus/"),
   ("Casino bonuses", "/casino-bonus/")]),
 ("Betting", [
   ("Online betting NZ", "/online-betting/"),
   ("Best sports betting sites", "/best-sports-betting-sites/"),
   ("Casino reviews", "/casino-reviews/")]),
 ("Trust &amp; data", [
   ("How we review", "/how-we-rate-casinos/"),
   ("Payment methods", "/casino-payment-methods/"),
   ("NZ gambling law", "/licensed-online-casinos/"),
   ("Our authors", "/authors/")]),
 ("Company", [
   ("About us", "/about/"),
   ("Contact us", "/contact/"),
   ("Authors", "/authors/"),
   ("Sitemap", "/sitemap.xml")]),
 ("Legal", [
   ("Terms and conditions", "/terms-and-conditions/"),
   ("Privacy policy", "/privacy-policy/"),
   ("Cookie policy", "/cookie-policy/"),
   ("Responsible gambling", "/responsible-gambling/")]),
]

# ---------------------------------------------------------------------------
# SERP title construction
#
# Format, applied to every title tag and every H1:
#     Primary Keyword [Month Year]: Secondary Keyword
#
# Google renders desktop SERP titles in Arial at 20px and truncates at roughly
# 580px, so character counts are the wrong unit — "Wellington" and "Illinois"
# are the same length and 40% apart in width. serp_px() measures the real
# advance width from the Arial metrics table, write() refuses to build a page
# whose title exceeds SERP_LIMIT, and fit() picks the richest secondary keyword
# that still fits. H1s use the same format with no width ceiling.
# ---------------------------------------------------------------------------
DATE_TAG = "[%s]" % MONTH_YEAR
SERP_LIMIT = 580          # pixels, Arial 20px
SERP_SIZE = 20

# Arial advance widths in units of 1/1000 em.
_AW = {}
for _c, _w in [
    (" ", 278), ("!", 278), ('"', 355), ("#", 556), ("$", 556), ("%", 889),
    ("&", 667), ("'", 191), ("(", 333), (")", 333), ("*", 389), ("+", 584),
    (",", 278), ("-", 333), (".", 278), ("/", 278), (":", 278), (";", 278),
    ("<", 584), ("=", 584), (">", 584), ("?", 556), ("@", 1015), ("[", 278),
    ("\\", 278), ("]", 278), ("^", 469), ("_", 556), ("`", 333), ("{", 334),
    ("|", 260), ("}", 334), ("~", 584),
    ("\u2014", 1000), ("\u2013", 556), ("\u00b7", 333), ("\u2019", 191),
    ("\u2018", 191), ("\u201c", 333), ("\u201d", 333), ("\u2026", 1000),
    ("\u00a0", 278), ("\u00e7", 500), ("\u00e9", 556), ("\u0101", 556),
]:
    _AW[_c] = _w
for _c in "0123456789":
    _AW[_c] = 556
for _c, _w in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                  [667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556,
                   833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667,
                   667, 611]):
    _AW[_c] = _w
for _c, _w in zip("abcdefghijklmnopqrstuvwxyz",
                  [556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222,
                   833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500,
                   500, 500]):
    _AW[_c] = _w


def serp_px(text, size=SERP_SIZE):
    """Rendered width of a SERP title, in pixels."""
    t = html.unescape(re.sub(r"<[^>]+>", "", str(text)))
    return round(sum(_AW.get(ch, 556) for ch in t) * size / 1000.0, 1)


def fit(primary, candidates, limit=SERP_LIMIT):
    """Return the first secondary keyword that keeps the assembled title inside
    the pixel budget. Candidates are ordered richest-first."""
    for c in candidates:
        if serp_px("%s %s: %s" % (primary, DATE_TAG, c)) <= limit:
            return c
    return candidates[-1]


SEO = {}


def register_seo(path, primary, sec_title, sec_h1=None):
    """sec_title is width-constrained; sec_h1 is not."""
    SEO[path] = (primary, sec_title, sec_h1 or sec_title)
    return path


def seo_title(path):
    p, st, _ = SEO[path]
    return "%s %s: %s" % (p, DATE_TAG, st)


def seo_h1(path):
    p, _, sh = SEO[path]
    return "%s %s: %s" % (p, DATE_TAG, sh)


# ---------------------------------------------------------------------------
# Title registry. Primary keywords are taken from the head term each page
# competes for; secondary keywords are the modifiers the ranking competitors
# pair with that head term in their own title tags (see docs/06-title-tags.md).
# ---------------------------------------------------------------------------
_REG = [
 ("/", "Best Online Casino Sites NZ",
  ["Real Money Casinos", "Real Money", "Top 10 Ranked"],
  "Real Money Casinos Ranked &amp; Tested"),
 ("/online-casinos/", "Best Online Casinos NZ",
  ["Real Money Casino Sites Ranked", "Real Money Casino Sites", "Real Money Sites"],
  "Top NZ Casino Sites for Real Money, Tested"),
 ("/casino-bonus/", "Casino Bonus NZ",
  ["Best Casino Bonuses &amp; Sign Up Offers", "Best Casino Bonuses Ranked",
   "Sign Up Bonus Offers"],
  "Best Casino Bonuses, Sign Up Offers and $1 Deposit Deals"),
 ("/online-pokies/", "Online Pokies NZ",
  ["Best Real Money Pokies Sites", "Best Real Money Pokies", "Real Money Pokies"],
  "Best Real Money Pokies Sites and Free Pokies"),
 ("/live-casino/", "Live Casino NZ",
  ["Best Live Dealer Casino Sites", "Best Live Dealer Sites", "Live Dealer Sites"],
  "Best Live Dealer Casino Sites, Roulette and Blackjack"),
 ("/new-casinos-nz/", "New Online Casinos NZ",
  ["Newest Casino Sites Ranked", "Newest Casino Sites", "New Casino Sites"],
  "Newest Online Casinos and New Casino Sites, Tracked"),
 ("/no-deposit-bonus/", "No Deposit Bonus NZ",
  ["Free Spins No Deposit Codes", "Free Spins No Deposit", "Free Spins"],
  "Free Spins No Deposit and No Deposit Bonus Codes"),
 ("/fast-payout-casinos/", "Fast Payout Casinos NZ",
  ["Instant Withdrawal Casinos", "Instant Withdrawals", "Fast Payouts"],
  "Fastest Instant Withdrawal Casinos, Timed"),
 ("/casino-payout-percentages/", "Casino Payout Percentages NZ",
  ["Highest RTP Casinos", "Best Payout Casinos", "Highest RTP"],
  "Highest RTP Casinos and What Payout Percentage Really Means"),
 ("/crypto-casinos-nz/", "Crypto Casinos NZ",
  ["Best Bitcoin Casino Sites", "Bitcoin &amp; USDT Sites", "Bitcoin Sites"],
  "Best Bitcoin, Ethereum and USDT Casino Sites"),
 ("/online-betting/", "Online Betting NZ",
  ["Best Sports Betting Sites", "Sports Betting Sites", "Betting Sites"],
  "Best Sports Betting Sites Compared"),
 ("/best-sports-betting-sites/", "Best Sports Betting Sites NZ",
  ["Top Kiwi Bookmakers", "Top Bookmakers", "Bookmakers"],
  "Top Kiwi Bookmakers Ranked"),
 ("/casino-reviews/", "Casino Reviews NZ",
  ["Expert Ratings &amp; Tested Payouts", "Expert Ratings &amp; Payouts", "Expert Ratings"],
  "Expert Ratings &amp; Tested Payouts"),
 ("/licensed-online-casinos/", "Licensed Online Casinos NZ",
  ["Is Online Gambling Legal?", "Legal Online Casinos", "Is It Legal?"],
  "Legal Online Casinos, NZ Online Gambling Laws and the Licence List"),
 ("/casino-payment-methods/", "Casino Payment Methods NZ",
  ["Deposits &amp; Withdrawals", "NZD Deposit Methods", "NZD Banking"],
  "Online Casino Deposit Methods and Withdrawals, Tested"),
 ("/responsible-gambling/", "Responsible Gambling NZ",
  ["Free Help &amp; Self-Exclusion", "Free Help &amp; Support", "Free Help"],
  "Free Help, Limits &amp; Self-Exclusion"),
 ("/how-we-rate-casinos/", "How We Rate Casinos",
  ["Our Review Methodology", "Review Methodology", "Methodology"],
  "How to Choose an Online Casino, and Our Review Methodology"),
 ("/about/", "About " + NAME,
  ["Our Team, Testing &amp; Funding", "Our Team &amp; Testing", "Our Team"],
  "Who We Are, How We Test, How We Are Paid"),
 ("/contact/", "Contact Us",
  ["%s Corrections &amp; Complaints" % NAME, "Corrections &amp; Complaints", "Corrections"],
  "%s Corrections, Complaints &amp; Enquiries" % NAME),
 ("/authors/", "Our Authors",
  ["NZ Casino Review Experts", "NZ Casino Experts", "Our Editorial Team"],
  "The NZ Casino Review Team"),
 ("/terms-and-conditions/", "Terms and Conditions",
  ["%s Site Terms" % NAME, "Site Terms of Use", "Site Terms"],
  "Using %s" % NAME),
 ("/privacy-policy/", "Privacy Policy",
  ["How We Use Your Data", "Your Data &amp; Rights", "Your Data"],
  "How We Use Your Data Under the Privacy Act 2020"),
 ("/cookie-policy/", "Cookie Policy",
  ["Cookies We Set &amp; Why", "Cookies We Set", "Our Cookies"],
  "Every Cookie We Set, and How to Turn It Off"),
]
for _p, _prim, _cands, _h1sec in _REG:
    register_seo(_p, _prim, fit(_prim, _cands), _h1sec)


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------
def esc(s):
    return html.escape(str(s), quote=True)


def plain(s):
    """Strip tags and unescape entities — used for meta descriptions and for
    schema strings, which must never contain markup."""
    s = re.sub(r"<[^>]+>", "", str(s))
    return html.unescape(s).replace(" ", " ").strip()


def anchor(txt):
    a = re.sub(r"<[^>]+>", "", txt)
    a = html.unescape(a).lower()
    a = re.sub(r"[^a-z0-9\s-]", "", a)
    return re.sub(r"[\s-]+", "-", a).strip("-")


def h2(txt, aid=None):
    return '<h2 id="%s">%s</h2>' % (aid or anchor(txt), txt)


def h3(txt, aid=None):
    return '<h3 id="%s">%s</h3>' % (aid or anchor(txt), txt)


# ---------------------------------------------------------------------------
# Components
# ---------------------------------------------------------------------------
def leaderboard(ops, kind="casino", notes=None, start=1, cta="Visit site",
                show_review=True, top_n=1):
    """The ranked operator list. `notes` maps slug -> one page-specific line of
    editorial explaining why this operator is on THIS page."""
    notes = notes or {}
    out = ['<div class="lb">']
    for i, o in enumerate(ops, start):
        top = " lb-row--top" if i <= top_n else ""
        badge = o.get("badge") or ""
        note = notes.get(o["slug"], o["sub"])
        terms = o.get("casino_bonus_terms") if kind == "casino" else ""
        bits = ['<span class="chip">%s</span>' % esc(o["licence"].split(" ")[0])]
        if o.get("crypto"):
            bits.append('<span class="chip chip--gold">Crypto</span>')
        if "NZD bank transfer" in o["payments"]:
            bits.append('<span class="chip chip--yes">NZD accounts</span>')
        bits.append('<span class="chip">Min %s</span>' % esc(o["min_deposit"]))
        bits.append('<span class="chip">%s wagering</span>' % esc(o["wagering"].replace(" bonus", "")))
        out.append(
          # One DOM for both layouts. On a phone the three wrapper divs become
          # display:contents so every leaf below is orderable against the card
          # itself — see the .lb-row rules in site.css.
          '<div class="lb-row%s">'
          '<div class="lb-rank">%02d</div>'
          '<div class="lb-brand"><div class="lb-logo"><img src="%s" alt="%s logo" '
          'width="160" height="56" loading="%s" decoding="async"></div>'
          '<p class="lb-name"><a href="%s">%s review</a></p></div>'
          '<div class="lb-mid">%s'
          '<div class="lb-offer"><span class="lb-offer-lbl">Welcome offer</span>'
          '<p class="lb-bonus">%s</p></div><p class="lb-sub">%s</p>'
          '<div class="pill-row">%s</div>%s</div>'
          '<div class="lb-cta"><div class="lb-score"><span class="lb-score-lbl">Our score</span>'
          '<b>%.1f</b><span class="lb-score-max">/10</span></div>'
          '<a class="btn btn--wide" href="%s" rel="nofollow sponsored noopener" target="_blank">%s</a>'
          '%s<div class="lb-bar"><i style="width:%d%%"></i></div></div>'
          '</div>' % (
            top, i, o["logo"], esc(o["name"]), "eager" if i <= 2 else "lazy",
            o["review"], esc(o["name"]),
            ('<span class="lb-badge">%s</span>' % badge) if badge else "",
            bonus_for(o, kind), note, "".join(bits),
            ('<p class="lb-terms">%s. 18+. New customers only. T&amp;Cs apply. '
             'Please gamble responsibly.</p>' % terms) if terms else
            '<p class="lb-terms">18+. New customers only. T&amp;Cs apply. Please gamble responsibly.</p>',
            o["rating"], url_for(o, kind), cta,
            ('<p class="lb-review"><a href="%s">Read our full review</a></p>' % o["review"])
            if show_review else "", o["bar"]))
    out.append('</div>')
    return "\n".join(out)


def table(headers, rows, caption=None, cls=""):
    out = ['<div class="tw%s">' % ((" " + cls) if cls else ""), "<table>"]
    if caption:
        out.append("<caption>%s</caption>" % caption)
    out.append("<thead><tr>" + "".join("<th scope=\"col\">%s</th>" % h for h in headers) + "</tr></thead>")
    out.append("<tbody>")
    for r in rows:
        cells = ['<th scope="row">%s</th>' % r[0]] + ["<td>%s</td>" % c for c in r[1:]]
        out.append("<tr>" + "".join(cells) + "</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def op_cell(o, link=True):
    inner = '<b>%s</b>' % esc(o["name"])
    if link:
        inner = '<a href="%s" style="text-decoration:none"><b>%s</b></a>' % (o["review"], esc(o["name"]))
    return ('<span class="t-logo"><img src="%s" alt="%s" width="58" height="30" loading="lazy" '
            'decoding="async">%s</span>' % (o["logo"], esc(o["name"]), inner))


def faq(items, heading="Frequently asked questions", hid="faq", intro=None):
    """Renders the visible FAQ. The matching FAQPage schema is emitted by
    write() from the same list, so the two can never drift apart."""
    out = []
    if heading:
        out.append('<h2 id="%s">%s</h2>' % (hid, heading))
    if intro:
        out.append("<p>%s</p>" % intro)
    out.append('<div class="faq">')
    for q, a in items:
        out.append("<details><summary>%s</summary><div class=\"faq-body\">%s</div></details>" % (q, a))
    out.append("</div>")
    return "\n".join(out)


def pros_cons(pros, cons, ph="What we like", ch="What we don&rsquo;t"):
    return ('<div class="pc"><div class="pc-col pc-pro"><h4>%s</h4><ul>%s</ul></div>'
            '<div class="pc-col pc-con"><h4>%s</h4><ul>%s</ul></div></div>' % (
              ph, "".join("<li>%s</li>" % p for p in pros),
              ch, "".join("<li>%s</li>" % c for c in cons)))


def keyfacts(pairs):
    return ('<div class="keyfacts">%s</div>' %
            "".join('<div class="keyfact"><span>%s</span><b>%s</b></div>' % (k, v) for k, v in pairs))


def note(body, kind="info", label=None):
    lab = ("<b>%s</b>" % label) if label else ""
    return '<div class="note note--%s">%s%s</div>' % (kind, lab, body)


def verdict(body, label="Our verdict"):
    return '<div class="verdict"><h4>%s</h4><p>%s</p></div>' % (label, body)


def toc(items, title="On this page"):
    return ('<nav class="toc" aria-label="%s"><p class="toc-t">%s</p><ol>%s</ol></nav>' % (
      title, title, "".join('<li><a href="#%s">%s</a></li>' % (a, t) for t, a in items)))


def steps(items):
    return '<ol class="steps">%s</ol>' % "".join(
        "<li><h4>%s</h4><p>%s</p></li>" % (t, b) for t, b in items)


def timeline(items):
    out = ['<ul class="tl">']
    for date, title, body, state in items:
        cls = {"done": "tl-done", "next": "tl-next"}.get(state, "")
        out.append('<li class="%s"><span class="tl-date">%s</span><b>%s</b><p>%s</p></li>' % (
            cls, date, title, body))
    out.append("</ul>")
    return "\n".join(out)


def cards(items, cls="grid--3"):
    out = ['<div class="grid %s">' % cls]
    for it in items:
        icon, title, body, href, more = (list(it) + [None, None])[:5]
        ic = '<div class="card-ic">%s</div>' % icon if icon else ""
        if href:
            out.append('<a class="card card--link" href="%s">%s<h3>%s</h3><p>%s</p>'
                       '<span class="card-more">%s &rarr;</span></a>' % (
                         href, ic, title, body, more or "Read more"))
        else:
            out.append('<div class="card">%s<h3>%s</h3><p>%s</p></div>' % (ic, title, body))
    out.append("</div>")
    return "\n".join(out)


def scorebars(scores):
    out = ['<div class="scores">']
    for k, w in copy_ops.WEIGHTS:
        v = scores.get(k, 0)
        out.append('<div class="score-row"><span>%s <small>(%d%%)</small></span>'
                   '<i><em style="width:%d%%"></em></i><b>%.1f</b></div>' % (k, w, int(v * 10), v))
    out.append("</div>")
    return "\n".join(out)



def barchart(caption, rows, source=None, unit=""):
    """Horizontal bar chart. rows: (label, value, display, emphasis) where
    emphasis is "", "hi" or "lo". Bars are scaled to the largest value, drawn
    in CSS — no JavaScript, no image, and it reads fine on a phone."""
    top = max(float(r[1]) for r in rows) or 1.0
    out = ['<figure class="chart"><figcaption>%s</figcaption><ul class="bars">' % caption]
    for r in rows:
        label, val, disp = r[0], float(r[1]), r[2]
        cls = r[3] if len(r) > 3 else ""
        out.append('<li%s><span class="bl">%s</span><span class="bt">'
                   '<i style="width:%.1f%%"></i></span><b>%s%s</b></li>'
                   % ((' class="%s"' % cls) if cls else "", label,
                      max(1.5, val / top * 100.0), disp, unit))
    out.append("</ul>")
    if source:
        out.append('<p class="src">%s</p>' % source)
    out.append("</figure>")
    return "\n".join(out)


def bignums(items):
    """items: (figure, label, footnote)"""
    return '<div class="bignums">%s</div>' % "".join(
        '<div class="bignum"><b>%s</b><span>%s</span>%s</div>'
        % (f, l, ("<em>%s</em>" % n) if n else "") for f, l, n in items)


def ctaband(title, body, links):
    btns = "".join('<a class="btn%s" href="%s"%s>%s</a>' % (
        "" if i == 0 else " btn--ghost", h,
        ' rel="nofollow sponsored noopener" target="_blank"' if h.startswith("http") else "", t)
        for i, (t, h) in enumerate(links))
    return '<section class="ctaband"><h2>%s</h2><p>%s</p>%s</section>' % (title, body, btns)


def authorbox(slug, role_line=None):
    a = AUTHORS[slug]
    return ('<aside class="authorbox">'
            '<img class="av-lg" src="%s" alt="%s" width="56" height="56" loading="lazy" '
            'decoding="async"><div>'
            '<h4><a href="/authors/%s/">%s</a></h4><p class="role">%s</p><p>%s</p>'
            '<ul>%s</ul></div></aside>' % (
              photo(slug), esc(a["name"]), slug, a["name"], role_line or a["role"], a["bio"],
              "".join("<li>%s</li>" % c for c in a["creds"])))


DISCLOSURE = (
  '<p class="disc"><b>How we make money.</b> %s is free to read. When you open an account through '
  'a link on this page we may be paid a commission by the operator, at no cost to you. It does not '
  'buy a position: rankings come from the scoring model published on our '
  '<a href="/how-we-rate-casinos/">how we review</a> page, every operator is scored the same way, and we '
  'list brands we would not recommend so that you can see why. 18+ only. '
  '<a href="/responsible-gambling/">Gamble responsibly</a>.</p>' % NAME)


def byline(author, checker=None, reviewed="Fact-checked by"):
    a = AUTHORS[author]
    out = ['<div class="byline">',
           '<img class="av" src="%s" alt="" width="30" height="30" '
           'decoding="async">' % photo(author, 64),
           '<span>By <a href="/authors/%s/"><b>%s</b></a>, %s</span>' % (author, a["name"], a["role"])]
    if checker:
        c = AUTHORS[checker]
        out.append('<span class="ts-dot">&middot;</span>')
        out.append('<img class="av av--2" src="%s" alt="" width="30" height="30" '
                   'decoding="async">' % photo(checker, 64))
        out.append('<span>%s <a href="/authors/%s/"><b>%s</b></a></span>' % (reviewed, checker, c["name"]))
    out.append('<span class="ts-dot">&middot;</span>')
    out.append('<span class="updated">Updated <b>%s</b></span>' % UPDATED_NZ)
    out.append('<span class="ts-dot nextrev">&middot;</span>')
    out.append('<span class="updated nextrev">Next review <b>%s</b></span>' % NEXT_REVIEW)
    out.append("</div>")
    return "".join(out)



def crumbs(trail):
    """trail: list of (label, href) — the final item is the current page and
    should pass href=None."""
    lis = []
    for label, href in trail:
        lis.append("<li>%s</li>" % (('<a href="%s">%s</a>' % (href, label)) if href
                                    else '<span aria-current="page">%s</span>' % label))
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>%s</ol></nav>' % "".join(lis)



def hero_offer(op, kind="casino", label=None):
    """The page's leading welcome offer, rendered as the first thing a visitor
    meets. It repeats the number-one row of the table below on purpose: on a
    desktop the table starts below the fold, so without this the offer is not
    seen until the reader scrolls."""
    terms = op.get("casino_bonus_terms") if kind == "casino" else ""
    meta = [op["name"], "%.1f/10" % op["rating"], "%s wagering" % op["wagering"].replace(" bonus", ""),
            "Min %s" % op["min_deposit"]]
    return (
      '<aside class="hoffer">'
      '<div class="hoffer-brand"><span class="hoffer-logo">'
      '<img src="%s" alt="%s logo" width="150" height="52" decoding="async"></span></div>'
      '<div class="hoffer-main"><span class="hoffer-lbl">%s</span>'
      '<p class="hoffer-bonus">%s</p>'
      '<p class="hoffer-meta">%s</p></div>'
      '<div class="hoffer-act">'
      '<a class="btn hoffer-btn" href="%s" rel="nofollow sponsored noopener" target="_blank">'
      'Claim offer</a>'
      '<a class="hoffer-rev" href="%s">Read the review</a></div>'
      '<p class="hoffer-terms">%s18+. New customers only. T&amp;Cs apply. '
      '<a href="/responsible-gambling/">Gamble responsibly</a>.</p>'
      '</aside>' % (
        op["logo"], esc(op["name"]),
        label or ("Top welcome offer &middot; %s" % MONTH_YEAR),
        bonus_for(op, kind), " &middot; ".join(meta),
        url_for(op, kind), op["review"],
        (terms + ". ") if terms else ""))


def hero(eyebrow, h1, lede, stats=None, ctas=None, aqua=False, meta=None, offer=None):
    """meta: (trail, author, checker). The breadcrumb opens the hero and the
    byline closes it, so authorship sits inside the same band as the H1 rather
    than in a strip underneath it."""
    trail = author = checker = None
    if meta:
        trail, author, checker = (list(meta) + [None, None, None])[:3]
    out = ['<header class="hero"><div class="wrap">']
    if trail:
        out.append(crumbs(trail))
    out.append('<div class="hero-in">')
    if eyebrow:
        out.append('<p class="eyebrow%s">%s</p>' % (" eyebrow--aqua" if aqua else "", eyebrow))
    out.append("<h1>%s</h1>" % h1)
    # the offer sits directly under the H1 — one screen-length of lede between
    # them was enough to push it off a laptop viewport
    if offer:
        out.append(offer)
    out.append('<p class="lede">%s</p>' % lede)
    # with an offer present its buttons are the hero's call to action, so the
    # secondary anchor buttons are dropped rather than competing with it
    if ctas and not offer:
        out.append('<div class="hero-cta">%s</div>' % "".join(
            '<a class="btn%s" href="%s">%s</a>' % ("" if i == 0 else " btn--ghost", h, t)
            for i, (t, h) in enumerate(ctas)))
    if stats:
        out.append('<div class="hero-stats">%s</div>' % "".join(
            '<div class="hero-stat"><b>%s</b><span>%s</span></div>' % (b, s) for b, s in stats))
    out.append("</div>")
    if author:
        out.append('<div class="hero-meta">%s</div>' % byline(author, checker))
    out.append("</div></header>")
    return "\n".join(out)


def section(body, cls="", wrap="wrap"):
    return '<section class="sec%s"><div class="%s">%s</div></section>' % (
        (" " + cls) if cls else "", wrap, body)


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------
def org_schema():
    return {"@type": "Organization", "@id": SITE + "/#organization", "name": NAME,
            "legalName": LEGAL, "url": SITE + "/",
            "logo": {"@type": "ImageObject", "@id": SITE + "/#logo",
                     "url": SITE + "/favicon-512x512.png", "width": 512, "height": 512,
                     "caption": NAME},
            "image": {"@id": SITE + "/#logo"},
            "foundingDate": FOUNDED,
            "description": ("Independent New Zealand casino and betting comparison publisher. "
                            "Every operator is tested from a New Zealand IP address and scored "
                            "against a published methodology."),
            "email": EMAIL,
            "address": {"@type": "PostalAddress", "addressCountry": "NZ",
                        "addressLocality": "Auckland", "streetAddress": POSTAL},
            "contactPoint": [{"@type": "ContactPoint", "contactType": "editorial",
                              "email": EMAIL, "availableLanguage": ["en-NZ"]},
                             {"@type": "ContactPoint", "contactType": "complaints",
                              "email": EMAIL_COMPLAINTS, "availableLanguage": ["en-NZ"]}],
            "knowsAbout": ["Online casinos in New Zealand", "Online pokies",
                           "Online Casino Gambling Act 2026", "Casino bonuses",
                           "Sports betting in New Zealand", "Responsible gambling"],
            "publishingPrinciples": SITE + "/how-we-rate-casinos/",
            "areaServed": {"@type": "Country", "name": "New Zealand"}}


def website_schema():
    return {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME,
            "description": TAG, "inLanguage": "en-NZ",
            "publisher": {"@id": SITE + "/#organization"}}


def person_schema(slug):
    a = AUTHORS[slug]
    return {"@type": "Person", "@id": SITE + "/authors/" + slug + "/#person",
            "name": a["name"], "url": SITE + "/authors/" + slug + "/",
            "jobTitle": plain(a["role"]), "description": plain(a["short"]),
            "knowsAbout": [s.strip() for s in plain(a["specialism"]).split(",")],
            "image": {"@type": "ImageObject", "url": SITE + photo(slug),
                      "width": 192, "height": 192},
            "worksFor": {"@id": SITE + "/#organization"}}


def person_ref(slug):
    """A reference to a Person defined in full on their author page. The @id does
    the entity linking; name and url are repeated because structured data is read
    one page at a time, and an author carrying only an @id has no name on the
    pages that cite it."""
    return {"@type": "Person", "@id": SITE + "/authors/" + slug + "/#person",
            "name": AUTHORS[slug]["name"], "url": SITE + "/authors/" + slug + "/"}


def breadcrumb_schema(path, trail):
    items = []
    for i, (label, href) in enumerate(trail, 1):
        it = {"@type": "ListItem", "position": i, "name": plain(label)}
        it["item"] = SITE + (href if href else path)
        items.append(it)
    return {"@type": "BreadcrumbList", "@id": SITE + path + "#breadcrumb", "itemListElement": items}


def faq_schema(path, items):
    return {"@type": "FAQPage", "@id": SITE + path + "#faq",
            "mainEntity": [{"@type": "Question", "name": plain(q),
                            "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                           for q, a in items]}


def itemlist_schema(path, ops, kind="casino", name=None):
    els = []
    for i, o in enumerate(ops, 1):
        els.append({"@type": "ListItem", "position": i, "name": o["name"],
                    "url": SITE + o["review"],
                    "item": {"@type": "Product", "name": o["name"],
                             "image": SITE + o["logo"],
                             "url": SITE + o["review"],
                             "brand": {"@type": "Brand", "name": o["name"]},
                             "review": {"@type": "Review",
                                        "reviewRating": {"@type": "Rating", "ratingValue": o["rating"],
                                                         "bestRating": 10, "worstRating": 1},
                                        "author": {"@id": SITE + "/#organization"},
                                        "reviewBody": plain(o["verdict"])[:450]}}})
    return {"@type": "ItemList", "@id": SITE + path + "#itemlist",
            "name": name or "Ranked operators", "itemListOrder": "https://schema.org/ItemListOrderDescending",
            "numberOfItems": len(els), "itemListElement": els}


def review_schema(path, o, author):
    return {"@type": "Review", "@id": SITE + path + "#review",
            "name": "%s review" % o["name"],
            "itemReviewed": {"@type": "Product", "name": o["name"], "image": SITE + o["logo"],
                             "brand": {"@type": "Brand", "name": o["name"]},
                             "description": plain(o["tagline"])},
            "reviewRating": {"@type": "Rating", "ratingValue": o["rating"], "bestRating": 10,
                             "worstRating": 1},
            "author": person_ref(author),
            "publisher": {"@id": SITE + "/#organization"},
            "reviewBody": plain(o["verdict"]),
            "positiveNotes": {"@type": "ItemList",
                              "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                                   "name": plain(p)} for i, p in enumerate(o["pros"])]},
            "negativeNotes": {"@type": "ItemList",
                              "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                                   "name": plain(c)} for i, c in enumerate(o["cons"])]}}


# ---------------------------------------------------------------------------
# The shell
# ---------------------------------------------------------------------------

def _css_version():
    """Content hash on the stylesheet URL. Without it a browser that cached an
    older site.css keeps serving it after a deploy — which is exactly what bit
    us in local preview, and would bite readers after a redesign."""
    try:
        css = open(os.path.join(ROOT, "assets", "css", "site.css"), "rb").read()
        return hashlib.sha256(css).hexdigest()[:8]
    except OSError:
        return "0"


CSS_V = _css_version()

PAGES = []          # (path, lastmod, priority, changefreq)
TITLE_WIDTHS = {}   # path -> measured SERP width in px
_LASTMOD_PATH = os.path.join(BUILD, "lastmod.json")
try:
    LASTMOD = json.load(open(_LASTMOD_PATH))
except Exception:
    LASTMOD = {}
_NEW_LASTMOD = {}


def save_lastmod():
    json.dump(_NEW_LASTMOD, open(_LASTMOD_PATH, "w"), indent=1, sort_keys=True)


def _nav_html(path):
    out = ['<ul class="nav-l">']
    for label, href, mod, panel in nav_tree():
        here = href == path
        inside = panel and any(h == path for _, links in panel for _, h in links)
        mods = ["nav-has--" + m for m in mod.split()] if (panel and mod) else []
        cls = " ".join(filter(None, ["nav-has" if panel else ""] + mods +
                                    ["is-here" if (here or inside) else ""]))
        out.append('<li%s>' % ((' class="%s"' % cls) if cls else ""))
        out.append('<a href="%s"%s%s>%s%s</a>' % (
            href, ' aria-current="page"' if here else "",
            ' aria-haspopup="true"' if panel else "", label,
            '<i class="nav-car" aria-hidden="true"></i>' if panel else ""))
        if panel:
            cols = []
            for title, links in panel:
                items = "".join('<li><a href="%s"%s>%s</a></li>'
                                % (h, ' aria-current="page"' if h == path else "", l)
                                for l, h in links)
                cols.append('<div class="nav-col"><p class="nav-h">%s</p><ul>%s</ul></div>'
                            % (title, items))
            out.append('<div class="nav-drop"><div class="nav-drop-in">%s</div></div>'
                       % "".join(cols))
        out.append("</li>")
    out.append("</ul>")
    out.append('<a class="nav-cta" href="/online-casinos/">Top 10 casinos</a>')
    return "".join(out)



# ---------------------------------------------------------------------------
# Mobile menu. Every page on the site, grouped, behind a hamburger.
#
# Built with <details>/<summary> because this site ships no JavaScript: the
# element is natively keyboard operable, announces its expanded state to a
# screen reader, and needs no polyfill. It is rendered on every page and shown
# only under 820px, where the horizontal nav is hidden.
# ---------------------------------------------------------------------------
def menu_groups():
    """The full page list, assembled from the same data the pages are built
    from so a new review or author cannot be forgotten here."""
    return [
      ("Casino guides", [
        ("Home &mdash; best casino sites NZ", "/"),
        ("Best online casinos NZ", "/online-casinos/"),
        ("Online pokies NZ", "/online-pokies/"),
        ("Live casino NZ", "/live-casino/"),
        ("New casinos NZ", "/new-casinos-nz/"),
        ("Casino payout percentages", "/casino-payout-percentages/"),
        ("Fast payout casinos", "/fast-payout-casinos/"),
        ("Crypto casinos NZ", "/crypto-casinos-nz/"),
        ("Casino bonus NZ", "/casino-bonus/"),
        ("No deposit bonus NZ", "/no-deposit-bonus/"),
      ]),
      ("Betting", [
        ("Online betting NZ", "/online-betting/"),
        ("Best sports betting sites", "/best-sports-betting-sites/"),
      ]),
      ("Trust &amp; data", [
        ("How we rate casinos", "/how-we-rate-casinos/"),
        ("Casino payment methods", "/casino-payment-methods/"),
        ("Licensed online casinos NZ", "/licensed-online-casinos/"),
        ("Responsible gambling", "/responsible-gambling/"),
      ]),
      ("Casino reviews", [("All casino reviews", "/casino-reviews/")] +
                        [(o["name"], o["review"]) for o in OPS]),
      ("Company", [
        ("About us", "/about/"),
        ("Contact us", "/contact/"),
        ("Our authors", "/authors/"),
      ] + [(AUTHORS[k]["name"], "/authors/%s/" % k) for k in AUTHOR_ORDER]),
      ("Legal", [
        ("Terms and conditions", "/terms-and-conditions/"),
        ("Privacy policy", "/privacy-policy/"),
        ("Cookie policy", "/cookie-policy/"),
      ]),
    ]


def _menu_html(path):
    cols = []
    for title, links in menu_groups():
        items = "".join(
            '<li><a href="%s"%s>%s</a></li>'
            % (href, ' aria-current="page"' if href == path else "", label)
            for label, href in links)
        cols.append('<div class="mnav-col"><h2 class="mnav-h">%s</h2><ul>%s</ul></div>'
                    % (title, items))
    return (
      '<details class="mnav">'
      '<summary class="mnav-btn" aria-label="Open the menu of all pages">'
      '<span class="mnav-ico" aria-hidden="true"><i></i><i></i><i></i></span>'
      '<span class="mnav-lbl">Menu</span></summary>'
      '<div class="mnav-panel"><nav class="mnav-in" aria-label="All pages">'
      '<a class="btn btn--wide mnav-cta" href="/online-casinos/">Top 10 casinos</a>'
      '%s</nav>'
      '<p class="mnav-foot"><b>18+</b> &middot; '
      '<a href="/responsible-gambling/">Gamble responsibly</a> &middot; '
      'Free help <a href="tel:0800654655">0800 654 655</a></p>'
      '</div></details>' % "".join(cols))

def _footer_html():
    cols = "".join(
        '<div class="foot-col"><h3>%s</h3><ul>%s</ul></div>' % (
            title, "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in links))
        for title, links in FOOTER)
    return """<footer class="foot"><div class="wrap">
<div class="foot-top">
<div class="foot-about">
<a class="brand" href="/"><img class="brand-mark" src="/favicon-96x96.png" alt="" width="40" height="40">
<span class="brand-txt"><span class="brand-word">%s</span><span class="brand-tag">%s</span></span></a>
<p>%s is published by %s. We test online casinos and sportsbooks from a New Zealand IP address,
time every withdrawal ourselves and publish the scoring model behind each ranking.</p>
<p>%s &middot; <a href="mailto:%s">%s</a></p>
</div>
%s
</div>
<div class="foot-badges">
<span class="foot-badge badge18">18+</span>
<a class="foot-badge" href="/responsible-gambling/">Gamble responsibly</a>
<a class="foot-badge" href="https://www.gamblinghelpline.co.nz/" rel="noopener nofollow" target="_blank">Gambling Helpline 0800 654 655</a>
<a class="foot-badge" href="https://www.pgf.nz/" rel="noopener nofollow" target="_blank">Problem Gambling Foundation</a>
<a class="foot-badge" href="/how-we-rate-casinos/">Published methodology</a>
<a class="foot-badge" href="/authors/">Named authors</a>
</div>
<div class="foot-bot">
<p>&copy; %s %s (%s). Trading as %s. %s<br>
Gambling can be harmful. You must be 18 or over to gamble online. Odds, bonuses and terms
change without notice &mdash; always read the operator&rsquo;s terms before you deposit. Nothing on this
site is financial advice. Offers shown are not available to residents of every country.</p>
<p><a href="/sitemap.xml">Sitemap</a> &middot; <a href="/terms-and-conditions/">Terms</a> &middot;
<a href="/privacy-policy/">Privacy</a> &middot; <a href="/cookie-policy/">Cookies</a></p>
</div>
</div></footer>""" % (NAME_HTML, TAG, NAME, LEGAL, POSTAL, EMAIL, EMAIL,
                      cols, YEAR, LEGAL, "NZBN " + NZBN, NAME, "")


# The strip carries two wordings of the same three facts. The long one shows on
# a desktop; on a phone the short one keeps it to a single line, which is worth
# ~65px of above-the-fold space. Both are always in the DOM.
TOPSTRIP = ('<div class="topstrip"><div class="wrap">'
            '<span><b>18+</b><span class="ts-full"> only</span></span>'
            '<span class="ts-dot">&middot;</span>'
            '<span><span class="ts-full">We may earn a commission from operators we list &mdash; </span>'
            '<a href="/how-we-rate-casinos/"><span class="ts-full">how that works</span>'
            '<span class="ts-mini">Ad disclosure</span></a></span>'
            '<span class="ts-dot">&middot;</span>'
            '<span><span class="ts-full">Free, confidential help: </span>'
            '<span class="ts-mini">Help </span>'
            '<a href="tel:0800654655">0800 654 655</a></span>'
            '</div></div>')


def write(path, title, desc, body, schema=None, prio=0.7, freq="monthly",
          noindex=False, og_type="article", robots_extra=None):
    """Wraps a body in the shell and writes <path>index.html."""
    assert path.startswith("/") and path.endswith("/"), path
    canonical = SITE + path

    graph = [org_schema(), website_schema()]
    graph += (schema or [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    ensure_ascii=False, separators=(",", ":"))

    robots = "noindex,nofollow" if noindex else (
        robots_extra or "index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1")

    px = serp_px(title)
    if px > SERP_LIMIT:
        raise ValueError("title too wide for the SERP: %.1fpx > %dpx on %s\n  %s"
                         % (px, SERP_LIMIT, path, title))
    TITLE_WIDTHS[path] = px
    title = html.unescape(title)
    desc = html.unescape(desc)
    head = """<!DOCTYPE html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(can)s">
<meta name="robots" content="%(robots)s">
<meta name="rating" content="adult">
<meta name="theme-color" content="#0A0F1C">
<meta name="author" content="%(name)s">
<meta property="og:type" content="%(ogt)s">
<meta property="og:site_name" content="%(name)s">
<meta property="og:locale" content="en_NZ">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(can)s">
<meta property="og:image" content="%(site)s/favicon-512x512.png">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
<link rel="icon" type="image/png" sizes="144x144" href="/favicon-144x144.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/css/site.css?v=%(cssv)s">
<script type="application/ld+json">%(ld)s</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
%(top)s
<header class="hdr"><div class="wrap hdr-in">
<a class="brand" href="/"><img class="brand-mark" src="/favicon-96x96.png" alt="" width="40" height="40">
<span class="brand-txt"><span class="brand-word">%(namehtml)s</span><span class="brand-tag">%(tag)s</span></span></a>
<nav class="nav" aria-label="Main">%(nav)s</nav>
%(menu)s
</div></header>
<main id="main">
""" % {"title": esc(title), "desc": esc(desc), "can": canonical, "robots": robots,
       "name": esc(NAME), "namehtml": NAME_HTML, "tag": esc(TAG), "ogt": og_type,
       "site": SITE, "ld": ld, "top": TOPSTRIP, "nav": _nav_html(path),
       "menu": _menu_html(path), "cssv": CSS_V}

    doc = head + body + "\n</main>\n" + _footer_html() + "\n</body>\n</html>\n"

    # resolve the last-modified date from a hash of the content, ignoring the
    # date placeholders themselves so a rebuild is not self-triggering
    digest = hashlib.sha256(doc.encode("utf-8")).hexdigest()[:16]
    prev = LASTMOD.get(path)
    if prev and prev.get("hash") == digest:
        date = prev["date"]
    else:
        date = datetime.date.today().isoformat()
    _NEW_LASTMOD[path] = {"hash": digest, "date": date}
    nz = datetime.date.fromisoformat(date).strftime("%d %B %Y").lstrip("0")
    doc = doc.replace(UPDATED, date).replace(UPDATED_NZ, nz)

    outdir = os.path.join(ROOT, path.strip("/"))
    if path != "/":
        if not os.path.isdir(outdir):
            os.makedirs(outdir)
    else:
        outdir = ROOT
    open(os.path.join(outdir, "index.html"), "w", encoding="utf-8").write(doc)
    if not noindex:
        PAGES.append((path, date, prio, freq))
    return path


def article_schema(path, title, desc, author, checker=None, section_name=None):
    d = {"@type": "Article", "@id": SITE + path + "#article",
         "headline": plain(title)[:110], "description": plain(desc),
         "mainEntityOfPage": {"@type": "WebPage", "@id": SITE + path},
         "isPartOf": {"@id": SITE + "/#website"},
         "inLanguage": "en-NZ",
         "author": person_ref(author),
         "publisher": {"@id": SITE + "/#organization"},
         "datePublished": "2026-01-15", "dateModified": UPDATED,
         "image": SITE + "/favicon-512x512.png"}
    if checker:
        d["reviewedBy"] = person_ref(checker)
    if section_name:
        d["articleSection"] = section_name
    return d
