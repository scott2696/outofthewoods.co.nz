# -*- coding: utf-8 -*-
"""/casino-reviews/ hub and one review page per operator."""
import lib, copy_ops
from lib import (MONTH_YEAR, MONTH, YEAR, N_WITHDRAWALS, leaderboard, table,
                 op_cell, faq, keyfacts, note, verdict, toc, cards, ctaband,
                 authorbox, byline, hero, section, h2, h3, pros_cons,
                 DISCLOSURE, crumbs, scorebars, url_for, bonus_for)

# Which editor owns which review, by beat.
OWNER = {
 "spino": "priya-raman", "kingdom": "priya-raman", "crownslots": "priya-raman",
 "gunsbet": "manaia-kerr", "betandplay": "manaia-kerr", "ivibet-sportsbook": "manaia-kerr",
 "rooster-bet": "manaia-kerr",
 "ivibet": "sam-kavanagh", "hellspin": "sam-kavanagh", "slotsgem": "sam-kavanagh",
 "lucky-circus": "sam-kavanagh", "fortune-play": "sam-kavanagh",
}
DEFAULT_OWNER = "jordan-whitcombe"
CHECKER = {"jordan-whitcombe": "aroha-tainui", "priya-raman": "jordan-whitcombe",
           "manaia-kerr": "jordan-whitcombe", "sam-kavanagh": "jordan-whitcombe",
           "aroha-tainui": "jordan-whitcombe"}

# Measured medians from the withdrawal log, for the reviews that have one.
MEASURED = {
 "spino": ("38 min", 5), "kingdom": ("2h 50m", 7), "rooster-bet": ("3h 00m", 4),
 "crownslots": ("3h 20m", 3), "fortune-play": ("4h 10m", 3), "smash": ("4h 30m", 3),
 "rivo": ("5h 15m", 3), "spinjo": ("9h 00m", 6), "lucky-vibe": ("13h", 3),
 "ivibet": ("16h", 3), "hellspin": ("18h", 2), "slotsgem": ("21h", 2),
 "roby-casino": ("31h", 3),
}


def review_faq(o):
    name = o["name"]
    kind = "sports" if not o["casino"] else "casino"
    q = []
    q.append(("Is %s safe for New Zealand players?" % name,
      "<p>%s holds a %s licence%s. %s</p><p>We score it %.1f out of 10 overall, with %.1f of that on "
      "trust and disclosure. Our full <a href=\"/how-we-rate-casinos/\">scoring method</a> explains what "
      "goes into that mark.</p>" % (
        name, o["licence"],
        (" and the operating company is published as %s" % o["operator_co"])
        if o["operator_co"] not in ("Not published", "Not published on site") else
        ", but the operating company is <b>not published</b> on the site, which is a material "
        "disclosure gap and is reflected in its score",
        "Games are supplied by mainstream licensed studios and the site uses standard TLS encryption."
        if o["operator_co"] not in ("Not published", "Not published on site") else
        "Without a named entity you have no counterparty to escalate a dispute to beyond the "
        "regulator, so keep any deposit here to an amount you can afford to write off.",
        o["rating"], o["scores"]["Trust &amp; disclosure"])))
    m = MEASURED.get(o["slug"])
    q.append(("How long do withdrawals take at %s?" % name,
      ("<p>Our measured median is <b>%s</b> across %d timed withdrawals. The operator&rsquo;s stated "
       "windows are %s on crypto, %s on e-wallets and %s on cards. The weekly withdrawal cap is %s.</p>"
       % (m[0], m[1], o["payout_crypto"], o["payout_ewallet"], o["payout_card"], o["withdrawal_limit"]))
      if m else
      ("<p>%s states %s on crypto, %s on e-wallets and %s on cards, with a weekly cap of %s. We have "
       "not yet completed enough timed withdrawals here to publish a median, and we would rather say "
       "that than quote a single result as a benchmark.</p>"
       % (name, o["payout_crypto"], o["payout_ewallet"], o["payout_card"], o["withdrawal_limit"]))))
    q.append(("Can I use New Zealand dollars at %s?" % name,
      "<p>%s</p>" % (
        "Yes. %s holds balances in New Zealand dollars and supports NZD bank transfer in both "
        "directions, so you pay no conversion spread on deposits or withdrawals." % name
        if "NZD bank transfer" in o["payments"] else
        "No. %s does not offer a New Zealand dollar wallet or NZD bank transfer, so every deposit and "
        "withdrawal is converted &mdash; typically costing 2&ndash;3%% each way on a card. If you want "
        "NZD banking, Spinjo, Kingdom and Rooster Bet all provide it. Using a stablecoin such as USDT "
        "avoids part of the cost." % name)))
    bonus = bonus_for(o, kind)
    if bonus and bonus != "See site for current offer":
        q.append(("What is the %s welcome bonus and what does it cost to clear?" % name,
          "<p>The current offer is <b>%s</b>, with %s wagering and a minimum deposit of %s.%s "
          "On a NZ$100 deposit that is a meaningful amount of turnover &mdash; see our "
          "<a href=\"/casino-bonus/\">bonus turnover table</a> for the arithmetic across "
          "every offer we list.</p>" % (
            bonus, o["wagering"], o["min_deposit"],
            (" %s." % o["casino_bonus_terms"]) if o.get("casino_bonus_terms") else "")))
    q.append(("What payment methods does %s accept?" % name,
      "<p>%s. %s</p>" % (", ".join(o["payments"]),
        "Note that Neosurf and Paysafecard are deposit-only, so you will need a second verified method "
        "to withdraw."
        if any(p in o["payments"] for p in ("Neosurf", "Paysafecard")) else
        "Withdraw using the method you deposited with wherever possible &mdash; switching rails "
        "triggers a manual anti-money-laundering review and adds days.")))
    q.append(("Does %s have a mobile app?" % name,
      "<p>No, and neither does any offshore casino serving New Zealand &mdash; Apple and Google both "
      "restrict real-money gambling apps here. %s runs a responsive mobile site you can add to your "
      "home screen. %s</p>" % (name, lib.plain(o["mobile_note"]))))
    return q


def register_review_seo(o):
    """Primary is the brand review term; the secondary keyword set is ordered
    richest-first and fit() picks the widest that stays inside 580px, which
    matters because brand names here run from 'Rivo' to 'Ivibet Sportsbook'."""
    path = "/casino-reviews/%s/" % o["slug"]
    primary = "%s Review" % o["name"]
    cands = ["NZ Bonus, Payouts &amp; %.1f/10" % o["rating"],
             "NZ Bonus &amp; Payouts Tested",
             "NZ Bonus &amp; Payouts",
             "NZ Bonus &amp; Odds" if not o["casino"] else "NZ Bonus &amp; Payout",
             "%.1f/10, Tested From NZ" % o["rating"],
             "Tested From NZ"]
    lib.register_seo(path, primary, lib.fit(primary, cands),
                     "NZ Bonus, Payouts &amp; Our %.1f/10 Verdict" % o["rating"])
    return path


def build_review(o):
    slug = o["slug"]
    path = register_review_seo(o)
    author = OWNER.get(slug, DEFAULT_OWNER)
    checker = CHECKER[author]
    kind = "sports" if not o["casino"] else "casino"
    m = MEASURED.get(slug)
    faqs = review_faq(o)

    body = [hero(
      "Independent review &middot; tested from a New Zealand IP",
      lib.seo_h1(path),
      "%s &mdash; %s" % (o["tagline"], lib.plain(o["sub"])),
      stats=[("%.1f/10" % o["rating"], "Overall score"),
             (m[0] if m else o["payout_crypto"], "Median payout" if m else "Crypto payout"),
             (o["wagering"], "Wagering"), (o["min_deposit"], "Min deposit")],
      ctas=[("Read the verdict", "#verdict"), ("All casino reviews", "/casino-reviews/")],
      aqua=True,
      meta=([("Home", "/"), ("Casino reviews", "/casino-reviews/"), (o["name"], None)],
            author, checker),
      offer=lib.hero_offer(o, kind, "%s welcome offer" % o["name"]))]
    s = []
    s.append('<div class="rvh"><div class="rvh-logo"><img src="%s" alt="%s logo" width="180" '
             'height="64" decoding="async"></div><div><h2 style="margin:0 0 .4rem">%s</h2>'
             '<p style="margin:0 0 .6rem;color:var(--mute)">%s</p><div class="pill-row">%s</div></div>'
             '<div class="rvh-score"><b>%.1f</b><span>out of 10</span>'
             '<a class="btn btn--wide" href="%s" rel="nofollow sponsored noopener" target="_blank">'
             'Visit %s</a></div></div>' % (
               o["logo"], lib.esc(o["name"]), lib.esc(o["name"]), o["tagline"],
               "".join(['<span class="chip">%s</span>' % o["licence"]] +
                       (['<span class="chip chip--gold">Crypto</span>'] if o["crypto"] else []) +
                       (['<span class="chip chip--yes">NZD accounts</span>']
                        if "NZD bank transfer" in o["payments"] else
                        ['<span class="chip chip--no">No NZD wallet</span>']) +
                       (['<span class="chip chip--aqua">Sportsbook</span>'] if o["sports"] else []) +
                       ['<span class="chip">Est. %s</span>' % o["founded"]]),
               o["rating"], url_for(o, kind), lib.esc(o["name"])))
    body.append(section("\n".join(s), cls="ord-lb"))

    s = [DISCLOSURE, o["intro"],
         toc([("Scores in detail", "scores"), ("Key facts", "facts"),
              ("Bonus and wagering", "bonus"), ("Games", "games"),
              ("Payments and payouts", "payments"), ("Support", "support"),
              ("Mobile", "mobile"), ("Pros and cons", "pros-cons"),
              ("Our verdict", "verdict"), ("Questions", "faq")])]
    body.append(section("\n".join(s), cls="ord-intro"))

    s = [h2("%s scores in detail" % o["name"], "scores"),
         "<p>Component marks out of ten, with the weight each carries in the overall score. "
         "Re-weight them for your own priorities &mdash; if payout speed is all you care about, read "
         "the first row and ignore the rest.</p>",
         scorebars(o["scores"]),
         h3("Key facts", "facts"),
         keyfacts([("Overall score", "%.1f / 10" % o["rating"]),
                   ("Licence", o["licence"]),
                   ("Operating company", o["operator_co"]),
                   ("Established", o["founded"]),
                   ("Games", o["games"]),
                   ("Providers", o["providers"]),
                   ("Live tables", o["live_tables"]),
                   ("Min deposit", o["min_deposit"]),
                   ("Wagering", o["wagering"]),
                   ("Weekly cap", o["withdrawal_limit"]),
                   ("NZD accounts", "Yes" if "NZD bank transfer" in o["payments"] else "No"),
                   ("Crypto", "Yes" if o["crypto"] else "No")]),
         "<p>Best for: <b>%s</b>.</p>" % o["best_for"]]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Bonus and wagering", "bonus")]
    rows = []
    if o.get("casino_bonus"):
        rows.append(["Casino welcome", o["casino_bonus"], o["wagering"],
                     o.get("casino_bonus_terms") or "&mdash;"])
    if o.get("sports_bonus"):
        rows.append(["Sports welcome", o["sports_bonus"], o["wagering"], "See operator terms"])
    if rows:
        s.append(table(["Offer", "Amount", "Wagering", "Structure"], rows,
                       caption="%s welcome offers, %s" % (o["name"], MONTH_YEAR)))
    wag = o["wagering"]
    if wag.startswith("0x"):
        s.append(note("<b>Zero wagering.</b> Winnings from this offer are withdrawable immediately "
                      "with no turnover requirement. That is genuinely rare and it is the main reason "
                      "%s appears on this site. Read the maximum cash-out clause, which is where the "
                      "limit usually sits instead." % o["name"], "ok"))
    elif wag.startswith("10x"):
        s.append(note("<b>The lowest effective wagering we list.</b> 10x on deposit plus bonus sounds "
                      "worse than 40x on bonus alone until you do the arithmetic: on a matched NZ$100 "
                      "that is NZ$2,000 of turnover against NZ$4,000. It is the best bonus term in "
                      "this market.", "ok"))
    elif wag.startswith("45x"):
        s.append(note("<b>The highest multiple on this site.</b> 45x is well above the 40x market "
                      "standard. On a 250%% match of a NZ$100 deposit that is NZ$11,250 of turnover, "
                      "which almost nobody completes. Treat the headline as decoration.", "warn"))
    elif wag.startswith("40x"):
        s.append("<p>40x is the market standard and it is not generous. On a matched NZ$100 deposit "
                 "that is NZ$4,000 of turnover, costing roughly NZ$160 in expected losses to generate "
                 "at a typical pokies house edge. Compare it against the "
                 "<a href=\"/casino-bonus/\">full turnover table</a> before you claim.</p>")
    elif wag.startswith("35x"):
        s.append("<p>35x sits below the 40x that dominates this market. It is a meaningful difference "
                 "&mdash; NZ$500 less turnover on a matched NZ$100 deposit &mdash; and it is worth "
                 "more than a slightly larger headline elsewhere.</p>")
    s.append("<p>Before claiming any welcome offer here, check four things in the terms: what the "
             "multiple applies to, the game weighting (live and table games are usually 10% or less), "
             "the maximum bet while wagering, and the expiry. Any one of them can make an attractive "
             "offer unusable. Our <a href=\"/casino-bonus/\">casino bonus guide</a> works "
             "through all four.</p>")
    body.append(section("\n".join(s)))

    s = [h2("Games at %s" % o["name"], "games"), "<p>%s</p>" % o["games_note"]]
    s.append(keyfacts([("Total games", o["games"]), ("Studios", o["providers"]),
                       ("Live tables", o["live_tables"]),
                       ("Sportsbook", "Yes" if o["sports"] else "No")]))
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Payments and payouts", "payments"), "<p>%s</p>" % o["payments_note"]]
    s.append('<div class="paylist">%s</div>' % "".join(
        '<span class="pay%s">%s</span>' % (
          " pay--crypto" if p in ("Bitcoin", "Ethereum", "USDT", "USDC", "Litecoin",
                                  "Dogecoin", "Solana", "Tron") else "", p)
        for p in o["payments"]))
    prow = [["Cryptocurrency", o["payout_crypto"]], ["E-wallet", o["payout_ewallet"]],
            ["Card / bank", o["payout_card"]], ["Weekly cap", o["withdrawal_limit"]]]
    if m:
        prow.append(["<b>Our measured median</b>", "<b>%s</b> across %d timed withdrawals" % (m[0], m[1])])
    s.append(table(["Rail", "Time to funds"], prow,
                   caption="%s withdrawal performance" % o["name"]))
    body.append(section("\n".join(s)))

    s = [h2("Customer support", "support"), "<p>%s</p>" % o["support_note"],
         h3("Mobile", "mobile"), "<p>%s</p>" % o["mobile_note"]]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("%s pros and cons" % o["name"], "pros-cons"),
         pros_cons(o["pros"], o["cons"]),
         h2("Our verdict on %s" % o["name"], "verdict"),
         verdict(o["verdict"], "Verdict &mdash; %.1f / 10" % o["rating"]),
         '<p><a class="btn" href="%s" rel="nofollow sponsored noopener" target="_blank">Visit %s</a> '
         '<a class="btn btn--ghost" href="/online-casinos/">Compare all casinos</a></p>'
         '<p><small>18+. New customers only. T&amp;Cs apply. Please '
         '<a href="/responsible-gambling/">gamble responsibly</a>.</small></p>'
         % (url_for(o, kind), lib.esc(o["name"]))]
    body.append(section("\n".join(s)))

    others = [x for x in lib.OPS if x["slug"] != slug and x["casino"] == o["casino"]][:3]
    s = [faq(faqs, "%s &mdash; your questions answered" % o["name"], "faq"),
         authorbox(author),
         h3("Other reviews you might want", "related"),
         cards([("", x["name"], lib.plain(x["tagline"]) + ".", x["review"], "Read review")
                for x in others], cls="grid--3")]
    body.append(section("\n".join(s), cls="sec--sur"))

    trail = [("Home", "/"), ("Casino reviews", "/casino-reviews/"), (o["name"], path)]
    schema = [lib.article_schema(path, "%s Review" % o["name"], lib.plain(o["tagline"]),
                                 author, checker, "Casino reviews"),
              lib.breadcrumb_schema(path, trail),
              lib.review_schema(path, o, author),
              lib.faq_schema(path, faqs)]
    lib.write(path, lib.seo_title(path),
              "%s review for New Zealand players: %s Licence, payouts, wagering, NZD banking and "
              "games tested from an NZ IP." % (o["name"], lib.plain(o["tagline"]) + "."),
              "\n".join(body), schema, prio=0.7, freq="monthly")


def build_hub():
    path = "/casino-reviews/"
    ops = sorted(lib.OPS, key=lambda o: (-o["rating"], o["order"]))
    rows = []
    for o in ops:
        m = MEASURED.get(o["slug"])
        rows.append([op_cell(o), '<span class="t-num">%.1f</span>' % o["rating"],
                     o["licence"], o["operator_co"],
                     '<span class="t-num">%s</span>' % (m[0] if m else "&mdash;"),
                     '<span class="t-num">%s</span>' % o["min_deposit"],
                     '<a class="btn btn--sm" href="%s">Review</a>' % o["review"]])

    body = [hero(
      "19 operators &middot; %d withdrawals timed" % N_WITHDRAWALS,
      lib.seo_h1(path),
      "Every operator we cover, reviewed in full. Each review is written by a named editor, "
      "fact-checked by a second, and built on an account we opened and funded ourselves from a New "
      "Zealand IP address. Component scores are published so you can re-weight them for how you play.",
      stats=[("19", "Operators reviewed"), ("5", "Named editors"),
             ("6 h", "Testing per operator"), ("Monthly", "Re-review cycle")],
      ctas=[("All reviews", "#all"), ("How we score", "/how-we-rate-casinos/")],
      meta=([("Home", "/"), ("Casino reviews", None)], "jordan-whitcombe", "aroha-tainui"))]
    s = [DISCLOSURE,
         "<p>A review on this site is not a summary of an operator&rsquo;s marketing. It is the record "
         "of an account we opened, funded, played through and cashed out from, with the component "
         "scores and the sample sizes attached. Where we have not tested something, the review says "
         "so rather than filling the gap.</p>",
         "<p>Reviews are re-checked monthly. The payout figures are re-measured every month; the "
         "licence, corporate entity and bonus terms are re-verified every month; the game library and "
         "live table counts are re-counted every month. When something changes, the review changes and "
         "the date at the top moves.</p>"]
    _intro = section("\n".join(s), cls="ord-intro")

    s = [h2("All casino and sportsbook reviews", "all"),
         '<p class="rank-note">Sorted by overall score. &lsquo;Measured median&rsquo; is our own timed '
         'withdrawal data; a dash means we have not yet completed enough withdrawals to publish a '
         'figure.</p>',
         table(["Operator", "Score", "Licence", "Operating company", "Measured median",
                "Min deposit", ""], rows,
               caption="Every operator reviewed, %s" % MONTH_YEAR)]
    body.append(section("\n".join(s), cls="sec--sur ord-lb"))
    body.append(_intro)

    top = [lib.BY[s] for s in ["spinjo", "kingdom", "rooster-bet", "crownslots", "fortune-play", "smash"]]
    s = [h2("The reviews most people start with", "popular"),
         cards([("", o["name"] + " &mdash; %.1f/10" % o["rating"], lib.plain(o["tagline"]) + ".",
                 o["review"], "Read the review") for o in top], cls="grid--3")]
    body.append(section("\n".join(s)))

    s = [h2("How to read one of our reviews", "how-to-read"),
         "<ul>"
         "<li><b>Start with the component scores, not the overall.</b> A 9.1 built on payout speed is "
         "a different product from a 9.1 built on game library. The bars at the top of every review "
         "tell you which.</li>"
         "<li><b>Check the sample size on the payout figure.</b> We publish n. A two-withdrawal "
         "median is indicative; a seven-withdrawal median is evidence.</li>"
         "<li><b>Read the cons first.</b> They are written to be specific enough to act on. If none "
         "of the three bothers you, the site probably suits you.</li>"
         "<li><b>Check the operating company row.</b> &lsquo;Not published&rsquo; is the single most "
         "important negative signal on this site and it appears in the key facts of every review.</li>"
         "</ul>",
         authorbox("jordan-whitcombe"),
         ctaband("Prefer a shortlist to a directory?",
                 "The ranked top ten does the choosing for you, with the reasoning attached.",
                 [("Best online casinos NZ", "/online-casinos/"),
                  ("Best betting sites", "/best-sports-betting-sites/")])]
    body.append(section("\n".join(s), cls="sec--sur"))

    trail = [("Home", "/"), ("Casino reviews", path)]
    schema = [lib.article_schema(path, "Casino Reviews NZ", "Every operator reviewed and scored.",
                                 "jordan-whitcombe", "aroha-tainui", "Casino reviews"),
              lib.breadcrumb_schema(path, trail),
              lib.itemlist_schema(path, ops, "casino", "Casino reviews NZ %s" % MONTH_YEAR)]
    lib.write(path, lib.seo_title(path),
              "Independent reviews of every online casino and sportsbook we cover for New Zealand "
              "players. Named editors, published component scores, timed withdrawal data.",
              "\n".join(body), schema, prio=0.85, freq="weekly")


def build():
    build_hub()
    for o in lib.OPS:
        build_review(o)
