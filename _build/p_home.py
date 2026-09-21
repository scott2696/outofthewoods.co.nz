# -*- coding: utf-8 -*-
"""Homepage — the money page for "best online casino sites NZ".

Structure derived from a September 2026 SERP teardown of casinos.com/nz,
bettingtop10.co.nz, casino.org/new-zealand and gambling.com/nz, plus real user
questions from Trustpilot complaint patterns and People Also Ask. See
docs/07-money-page-serp-teardown.md for the analysis behind every section.
"""
import lib
from lib import (MONTH_YEAR, MONTH, YEAR, NAME, SITE, N_WITHDRAWALS,
                 N_OPERATORS_TESTED, N_HOURS, pick, leaderboard, table, op_cell,
                 faq, keyfacts, note, verdict, toc, steps, timeline, cards,
                 ctaband, authorbox, byline, hero, section, h2, h3, barchart,
                 bignums, pros_cons, DISCLOSURE)

TOP = ["spinjo", "kingdom", "rooster-bet", "crownslots", "fortune-play", "smash",
       "lucky7even", "rivo", "gunsbet", "lucky-vibe"]

NOTES = {
 "spinjo": "The widest lobby in this market paired with a true NZD wallet &mdash; our highest overall score.",
 "kingdom": "Median payout of 2h 50m across seven timed crypto withdrawals, and 30x on a very large package.",
 "rooster-bet": "The best single account if you want pokies, live tables, rugby and racing in one place.",
 "crownslots": "The biggest percentage match we list, on the fastest single cashout we recorded (68 minutes).",
 "fortune-play": "Aviator, crash and bonus-buy depth nothing else here matches, with bonus buys eligible for wagering.",
 "smash": "10x on deposit plus bonus &mdash; a quarter of the market-standard turnover on the largest headline package.",
 "lucky7even": "Twenty free spins before you deposit anything, on a casino with real NZD banking underneath.",
 "rivo": "1.4 seconds to an interactive lobby on throttled 4G &mdash; the best phone experience we measured.",
 "gunsbet": "The largest sports welcome in New Zealand-facing offshore betting, at roughly NZ$14,700.",
 "lucky-vibe": "Weekly cashback that credits as withdrawable cash rather than another bonus with 40x attached.",
}

FAQ = [
 ("Which is the best online casino site in NZ right now?",
  "<p>Spinjo, at 9.3 out of 10. It combines the largest game library we can verify from a New Zealand "
  "IP address (roughly 8,000 titles), a genuine New Zealand dollar wallet with NZD bank transfer, and "
  "a Cura&ccedil;ao Gaming Control Board licence held by a named operator, Rabidi N.V. If payout speed "
  "matters more to you than lobby size, Kingdom is the better pick at a verified two hour fifty minute "
  "median. <a href=\"/casino-reviews/spinjo/\">Read the Spinjo review</a> or compare the "
  "<a href=\"/online-casinos/\">full list of 16</a>.</p>"),
 ("Is it legal to play at online casinos in New Zealand?",
  "<p>Yes, and it always has been. No New Zealand law has ever made it an offence for a resident to "
  "gamble at an overseas online casino. The Gambling Act 2003 prohibited <em>offering</em> unlicensed "
  "gambling from inside New Zealand; it said almost nothing about offshore sites, which is the gap the "
  "Online Casino Gambling Act 2026 closes. The Act commenced on 1 May 2026, the regulations followed on "
  "3 July 2026, and the Department of Internal Affairs will issue up to 15 licences. The obligations "
  "and the penalties fall on operators, not on you.</p>"),
 ("What happens on 1 December 2026 &mdash; will my casino disappear?",
  "<p>It depends on whether your operator applied for a licence, and this is the part most pages get "
  "wrong. From 1 December 2026, a provider that has <b>not applied</b> must stop offering online casino "
  "gambling to New Zealanders. A provider that <b>has applied</b> may keep serving New Zealand players "
  "&mdash; though not advertise into New Zealand &mdash; until its application is decided or until "
  "mid-2027, whichever comes first. So expect three outcomes: some sites geo-block New Zealand, some "
  "continue quietly while their application sits with the DIA, and some exit rather than pay to bid. "
  "Do not hold a large balance offshore through the transition.</p>"),
 ("Do I pay tax on online casino winnings in New Zealand?",
  "<p>Not as a recreational player. Inland Revenue does not treat casual gambling winnings as "
  "assessable income, so there is nothing to declare and nothing to pay. The exception is a person "
  "whose gambling amounts to a business &mdash; systematic, organised, with an expectation of profit "
  "&mdash; which is rare. Note that cryptoassets are treated separately as property, so converting "
  "crypto back to New Zealand dollars can have its own tax consequences even though the gambling does "
  "not. <a href=\"/licensed-online-casinos/\">More on tax and the law</a>.</p>"),
 ("Can I play in New Zealand dollars?",
  "<p>At ten of the sixteen casinos we list, yes, and it is worth more than most welcome bonuses. A "
  "euro or US dollar wallet converts every deposit and every withdrawal at the cashier&rsquo;s rate, "
  "typically costing 2&ndash;3% each way. On a NZ$500 deposit and a NZ$1,200 withdrawal that is around "
  "NZ$40 lost for nothing, and over a year of ordinary play it comfortably exceeds the value of a "
  "welcome offer. Spinjo, Kingdom, Rooster Bet, Fortune Play, Smash, Rivo, Lucky Vibe, Lucky7even, "
  "Lucky Circus and MadCasino all hold NZD. CrownSlots, Gunsbet, Ivibet, Hellspin, Slotsgem and Roby "
  "do not.</p>"),
 ("Can I still use POLi to deposit at an online casino?",
  "<p>No, and this is the most common error on competing New Zealand casino pages. POLi the company is "
  "operating normally &mdash; it was acquired by Merco, it connects through bank-approved open banking "
  "APIs following the December 2025 rules, and eight New Zealand banks partner with it &mdash; but it "
  "is no longer available as a deposit method at online casinos serving New Zealand in 2026. If a "
  "comparison page is still showing POLi logos on casino cards, treat every other figure on that page "
  "as equally stale. Use NZD bank transfer, Neosurf, MiFinity or crypto instead.</p>"),
 ("What is the fastest paying online casino for NZ players?",
  "<p>Kingdom, on measured data: a median of two hours fifty minutes across seven timed cryptocurrency "
  "withdrawals, with a worst case of six hours twenty and no requests held for review. Spino is faster "
  "in absolute terms &mdash; our quickest cashout anywhere was eleven minutes &mdash; but it is "
  "crypto-only with no fiat option. For a card or bank withdrawal, one to three business days is "
  "realistic. Anything advertised as an &lsquo;instant&rsquo; card withdrawal is describing the moment "
  "the operator approves it, not the moment your bank posts it. "
  "<a href=\"/fast-payout-casinos/\">See the full timing table</a>.</p>"),
 ("Why does my withdrawal keep getting cancelled?",
  "<p>Four causes account for almost all of it. One: identity verification is incomplete, so the "
  "request cannot be released. Two: you are withdrawing to a different method than you deposited with "
  "&mdash; anti-money-laundering rules require operators to reverse the original rail first, up to the "
  "amount you deposited. Three: a bonus is still active, or an automated system has flagged a maximum-"
  "bet breach during wagering. Four: the request exceeds the weekly cap, in which case it should be "
  "split rather than cancelled. If a cancellation comes with no reason at all after those four are "
  "ruled out, that is the point to start the escalation ladder below.</p>"),
 ("Why do online casinos ask for so much ID?",
  "<p>Because their licence requires it. Every licensed operator must complete know-your-customer "
  "checks before releasing funds, and most run them at first withdrawal rather than at registration "
  "&mdash; which is why it feels like an ambush at exactly the wrong moment. Expect photo ID, proof of "
  "address dated within three months, and, if you deposited by card, a photo of the card with the "
  "middle digits covered. Above roughly NZ$5,000 in withdrawals, expect a source-of-funds request as "
  "well. Median approval across our tests was 14 hours; the worst was four days. Do it the day you "
  "register and the problem disappears.</p>"),
 ("Can a casino refuse to pay me, and what can I do about it?",
  "<p>Legitimately, yes, in defined circumstances: unverified identity, duplicate accounts, "
  "third-party payment, or a bonus term breach such as exceeding the maximum bet. Illegitimately, some "
  "operators stall. Your practical protection is the licence. A Cura&ccedil;ao Gaming Control Board "
  "licensee has a published complaints process and a regulator that will take a submission; an "
  "operator with no published licence number has neither, which is exactly why we rank Roby Casino "
  "sixteenth. The escalation ladder is set out in full above.</p>"),
 ("What happens to my balance if an online casino goes bust?",
  "<p>In most offshore jurisdictions, you become an unsecured creditor and in practice you lose it. "
  "Unlike a New Zealand bank deposit, an offshore casino balance is not protected by any compensation "
  "scheme, and Cura&ccedil;ao, Anjouan and Tobique do not require segregated player funds to the "
  "standard the UK or Malta do. This is the strongest single argument for withdrawing regularly rather "
  "than treating a casino account as somewhere to keep money. It matters more than usual through the "
  "December 2026 transition, when some operators will exit the New Zealand market.</p>"),
 ("How much do I actually have to wager to clear a welcome bonus?",
  "<p>Multiply the bonus by the wagering multiple. A NZ$200 bonus at 40x means NZ$8,000 of turnover "
  "before anything is withdrawable. Two variations change the answer sharply: some operators apply the "
  "multiple to deposit <em>plus</em> bonus, which doubles it on a 100% match, and most weight live "
  "dealer and table games at 10% or nothing, which multiplies the effective requirement by ten. Smash "
  "asks 10x on deposit plus bonus &mdash; the lowest real turnover we list &mdash; and Spino asks 0x on "
  "its crypto offer. <a href=\"/casino-bonus/\">Full turnover table</a>.</p>"),
 ("Are offshore casinos safe if they are not licensed in New Zealand?",
  "<p>Safety here is a spectrum, not a switch. What measurably reduces your risk: a licence number "
  "published on the site that returns a result on the regulator&rsquo;s register, a named corporate "
  "entity behind it, independent game testing by eCOGRA, iTech Labs or GLI, and a complaints path you "
  "can actually use. The Cura&ccedil;ao Gaming Control Board regime introduced in 2024 is meaningfully "
  "stronger than the old master-licence system it replaced. We score every operator on disclosure and "
  "say so plainly when one falls short.</p>"),
 ("Why am I getting phone calls and emails after signing up?",
  "<p>Because offshore operators market aggressively and the New Zealand Unsolicited Electronic "
  "Messages Act 2007 is difficult to enforce against a company with no local presence. It is one of "
  "the most common complaints in public reviews of this sector. Two defences: use a dedicated email "
  "address for gambling accounts, and turn marketing consent off in account settings the day you "
  "register rather than waiting for the first call. If you have self-excluded and marketing continues, "
  "that is a licence breach and worth reporting to the operator&rsquo;s regulator.</p>"),
 ("What is the minimum deposit at NZ online casinos?",
  "<p>NZ$20 is the market standard. Lucky Circus is the cheapest entry we list at NZ$10, while "
  "CrownSlots, Gunsbet and Roby Casino ask NZ$30&ndash;35. A low minimum is worth more than it looks: "
  "it lets you test a cashier and a support desk with money you can afford to write off before "
  "committing a real deposit.</p>"),
 ("Can I play casino games on my phone in New Zealand?",
  "<p>Yes, and that is how roughly three-quarters of sessions happen. Almost no offshore casino has a "
  "native app in the New Zealand App Store or Play Store, because Apple and Google both restrict "
  "real-money gambling apps here &mdash; so &lsquo;casino app&rsquo; in practice means a progressive "
  "web app you add to your home screen. Rivo reached an interactive lobby in 1.4 seconds on throttled "
  "4G in our testing, the fastest of the group.</p>"),
 ("What is the legal gambling age in New Zealand?",
  "<p>18 for online gambling under the Online Casino Gambling Act 2026, and 18 for Lotto and TAB "
  "betting. Land-based casinos are different: the minimum age to enter a New Zealand casino venue is "
  "20. Licensed online operators will be required to run robust digital identity verification rather "
  "than a tick-box age gate.</p>"),
 ("Are there responsible gambling tools for NZ players?",
  "<p>Yes, at every operator on this page: deposit limits, loss limits, session time limits, reality "
  "checks, cooling-off and self-exclusion, all reachable from account settings. From 2027, licensed New "
  "Zealand operators must also apply a mandatory 24-hour cooling-off before any limit is removed or "
  "increased, ban credit cards, and prohibit autoplay. Free, confidential help is available now on "
  "<a href=\"tel:0800654655\">0800 654 655</a>, 24 hours. "
  "<a href=\"/responsible-gambling/\">Full guide</a>.</p>"),
 ("How do you make money, and does it affect the rankings?",
  "<p>We are paid a commission when a reader opens an account through one of our links, disclosed at "
  "the top of every page. It does not buy position. The order comes from the weighted model published "
  "on our <a href=\"/how-we-rate-casinos/\">how we review</a> page, every operator is scored identically, and "
  "we list brands we would not use with the reasons attached. The check you can run yourself: our "
  "highest-paying partner pays 50% and ranks fourth, our top-ranked casino pays 45%, and we list "
  "operators paying 20&ndash;25%.</p>"),
]


def build():
    ops = [lib.BY[s] for s in TOP]
    path = "/"

    # ---------------------------------------------------------------- hero
    body = [hero(
      "Updated %s &middot; %d withdrawals timed" % (MONTH_YEAR, N_WITHDRAWALS),
      lib.seo_h1(path),
      "New Zealanders deposit an estimated <b>NZ$1.36 billion a year</b> into offshore online gambling "
      "sites, and almost none of the pages ranking for this search have tested one. We opened accounts "
      "at %d casinos from a New Zealand IP address, deposited real money and timed <b>%d withdrawals</b> "
      "to the minute. These are the ten best online casino sites for Kiwi players in %s."
      % (N_OPERATORS_TESTED, N_WITHDRAWALS, MONTH_YEAR),
      stats=[("9.3/10", "Top score: Spinjo"), ("2h 50m", "Fastest median payout"),
             ("10x", "Lowest wagering found"), ("NZ$10", "Lowest deposit")],
      ctas=[("See the top 10", "#top-10-online-casino-sites-nz"),
            ("How we score", "/how-we-rate-casinos/")],
      meta=([("Home", None)], "jordan-whitcombe", "aroha-tainui"),
      offer=lib.hero_offer(ops[0], "casino"))]

    # ------------------------------------------------------------- intro
    s = [DISCLOSURE,
         "<p><b>Short answer:</b> the best online casino site in New Zealand right now is "
         "<a href=\"/casino-reviews/spinjo/\">Spinjo</a> (9.3/10) for its 8,000-game lobby and genuine "
         "NZD wallet; <a href=\"/casino-reviews/kingdom/\">Kingdom</a> (9.1/10) if getting paid quickly "
         "matters most, with a verified median withdrawal of two hours fifty minutes; and "
         "<a href=\"/casino-reviews/smash/\">Smash</a> (8.8/10) if you intend to actually clear a "
         "welcome bonus, because 10x on deposit plus bonus is a quarter of what this market normally "
         "asks.</p>",
         "<p>Every casino ranked below was tested from an Auckland or Christchurch IP address on a real "
         "account with real money. Where an operator is weak &mdash; a euro-only wallet, an unpublished "
         "licence, a 45x wagering requirement &mdash; it is stated in the listing rather than buried in "
         "a review three clicks away. This page also covers the two things the market is not telling "
         "you clearly: what actually happens to your account on 1 December 2026, and what to do when a "
         "withdrawal is cancelled without a reason.</p>",
         toc([
           ("Top 10 online casino sites NZ", "top-10-online-casino-sites-nz"),
           ("Side-by-side comparison", "comparison"),
           ("Find the right casino for you", "best-for"),
           ("The NZ online casino market in numbers", "market"),
           ("What changed this month", "whats-changed"),
           ("How we test and score", "how-we-test"),
           ("Is online casino gambling legal in NZ?", "is-it-legal"),
           ("What happens on 1 December 2026", "december-2026"),
           ("If a casino will not pay: the escalation ladder", "complaints"),
           ("What Kiwi players actually complain about", "complaints-data"),
           ("Deposits and withdrawals for Kiwis", "payments"),
           ("Bonus wagering, in plain numbers", "bonus-maths"),
           ("Pokies, live dealer and crash games", "games"),
           ("Playing on a phone", "mobile"),
           ("Casinos we would avoid, and why", "avoid"),
           ("How to spot a casino worth trusting", "safety"),
           ("Staying in control", "responsible-gambling"),
           ("Frequently asked questions", "faq"),
           ("Sources and references", "sources"),
         ])]
    _intro = section("\n".join(s), cls="ord-intro")

    # --------------------------------------------------------- leaderboard
    s = [h2("Top 10 Online Casino Sites NZ &mdash; %s" % MONTH_YEAR, "top-10-online-casino-sites-nz"),
         '<p class="rank-note">Ranked by weighted score. Payout speed carries 25% of the mark, bonus '
         'value 20%, game library 20%, banking and NZD support 15%, and trust and disclosure 20%. The '
         'full weighting is on our <a href="/how-we-rate-casinos/">methodology page</a>.</p>',
         leaderboard(ops, "casino", NOTES, top_n=1),
         note("<b>A note on the numbers you see advertised.</b> Several of the headline figures on this "
              "page &mdash; 600%, NZ$19,500, 390% &mdash; are the total across three or four staged "
              "deposits, not a first-deposit match. That is standard in this market and it is not "
              "dishonest, but it does mean the advertised maximum is unreachable for most players. The "
              "wagering multiple is shown beside every offer for exactly that reason.", "warn")]
    body.append(section("\n".join(s), cls="ord-lb"))
    body.append(_intro)

    # ---------------------------------------------------------- comparison
    cmp_rows = []
    for o in ops:
        nzd = ('<span class="chip chip--yes">Yes</span>' if "NZD bank transfer" in o["payments"]
               else '<span class="chip chip--no">No</span>')
        cmp_rows.append([op_cell(o), '<span class="t-num">%.1f</span>' % o["rating"],
                         lib.bonus_for(o), '<span class="t-num">%s</span>' % o["wagering"],
                         '<span class="t-num">%s</span>' % o["min_deposit"],
                         '<span class="t-num">%s</span>' % o["payout_crypto"], nzd])
    s = [h2("Online casinos NZ compared side by side", "comparison"),
         "<p>The same ten sites, reduced to the six numbers that decide most decisions. Crypto payout "
         "times are the operator&rsquo;s stated window; our measured medians are in each review and in "
         "the <a href=\"/fast-payout-casinos/\">payout timing table</a>.</p>",
         table(["Casino", "Score", "Welcome offer", "Wagering", "Min deposit", "Crypto payout",
                "NZD account"], cmp_rows,
               caption="Top 10 online casino sites NZ, compared &mdash; %s" % MONTH_YEAR)]
    body.append(section("\n".join(s), cls="sec--sur"))

    # ------------------------------------------------------------- best for
    s = [h2("Find the right casino for you", "best-for"),
         "<p>There is no single best casino, only a best casino for how you play. A player depositing "
         "NZ$20 a fortnight wants different things from someone chasing a five-figure bonus.</p>",
         cards([
      ("01", "Best overall", "Spinjo &mdash; 8,000 games, NZD wallet, Cura&ccedil;ao GCB licence under "
       "a named operator. The most complete package for a New Zealand player.",
       "/casino-reviews/spinjo/", "Read the review"),
      ("02", "Fastest withdrawals", "Kingdom &mdash; a verified 2h 50m median across seven timed crypto "
       "withdrawals and a NZ$10,000 weekly ceiling.", "/fast-payout-casinos/", "Timed payout data"),
      ("03", "Best bonus you can clear", "Smash &mdash; 10x on deposit plus bonus, against a market "
       "standard of 40x on bonus.", "/casino-bonus/", "Bonus turnover table"),
      ("04", "Best for online pokies", "Spinjo &mdash; roughly 8,000 titles with volatility, feature "
       "and minimum-stake filters that actually work.", "/online-pokies/", "Online pokies NZ"),
      ("05", "Best live dealer floor", "Ivibet &mdash; 300 live tables on a 4,000-game casino, with the "
       "deepest blackjack variant coverage here.", "/live-casino/", "Live casinos"),
      ("06", "Best for crypto", "Spino &mdash; 0x wagering, eight rails and an eleven-minute fastest "
       "cashout. Crypto only, no fiat.", "/crypto-casinos-nz/", "Crypto casinos"),
      ("07", "Best no-deposit offer", "Lucky7even &mdash; 20 free spins on Book of the Fallen before "
       "you fund the account.", "/no-deposit-bonus/", "No deposit casinos"),
      ("08", "Best on a phone", "Rivo &mdash; 1.4 seconds to an interactive lobby on throttled 4G and a "
       "four-tap cashout.", "/casino-reviews/rivo/", "Read the review"),
      ("09", "Best for small deposits", "Lucky Circus &mdash; NZ$10 minimum and 35x wagering, the "
       "friendliest terms in this list for a budgeted player.",
       "/casino-reviews/lucky-circus/", "Read the review"),
      ("10", "Best highest-RTP lobby", "Spinjo and Rooster Bet &mdash; the only two casinos where all "
       "ten titles we sampled ran at the studio&rsquo;s default RTP.",
       "/casino-payout-percentages/", "RTP findings"),
      ("11", "Best newest arrival", "Kingdom &mdash; a 2024 launch that already outpays every "
       "established brand we track.", "/new-casinos-nz/", "New casinos"),
      ("12", "Best for sport and casino", "Rooster Bet &mdash; one NZD wallet, one KYC check, separate "
       "welcome offers for each product.", "/best-sports-betting-sites/", "Betting sites"),
    ])]
    body.append(section("\n".join(s)))

    # --------------------------------------------------- market in numbers
    s = [h2("The New Zealand online casino market in numbers", "market"),
         "<p>Almost every page competing for this search tells you which casino has the biggest bonus. "
         "Very few tell you how large this market is, where the money goes, or who is being harmed by "
         "it. The figures below are from the Department of Internal Affairs, Health New Zealand and the "
         "2023/24 New Zealand Gambling Survey, and they are the context the rest of this page sits "
         "in.</p>",
         bignums([
           ("NZ$1.36b", "Estimated annual deposits by New Zealanders into online gambling sites, almost "
            "all of them offshore", "DIA estimate, Oct 2023 &ndash; Sep 2025"),
           ("NZ$100m+", "Leaving New Zealand for overseas gambling sites every month, sustained for "
            "over a year", "DIA payments analysis"),
           ("~360,000", "Active online gambling audience in New Zealand by September 2025",
            "Up from a materially smaller base in 2023"),
           ("+10.5%", "Year-on-year growth in online gambling spend to September 2025, against +9% "
            "growth in transaction volume", "Spend is growing faster than participation"),
           ("NZ$2.76b", "Lost by New Zealanders across the four regulated sectors &mdash; Lotto, TAB, "
            "casinos and pub pokies &mdash; in 2022/23", "DIA gambling expenditure statistics"),
           ("64.1%", "Of New Zealanders aged 15+ gambled at least once in the previous 12 months "
            "(about 2.76 million people)", "NZ Gambling Survey 2023/24"),
           ("1 in 5", "New Zealanders will experience harm in their lifetime from their own or someone "
            "else&rsquo;s gambling", "Health New Zealand"),
           ("Up to 15", "Online casino licences the DIA will issue, from roughly 50 expressions of "
            "interest received", "EOI stage closed 14 August 2026"),
         ]),
         barchart(
           "Where the online money actually goes: estimated annual New Zealand deposits by destination",
           [("Offshore online casinos &amp; sportsbooks", 1360, "NZ$1.36b", "hi"),
            ("Regulated sector total (Lotto, TAB, casinos, pub pokies)", 2760, "NZ$2.76b", ""),
            ("TAB NZ &mdash; the only NZ-licensed betting operator", 360, "NZ$360m", ""),
            ("Projected annual duty take at 16% on offshore GGR", 60, "~NZ$60m", "")],
           source="Sources: DIA gambling expenditure statistics and payments analysis; DIA estimate of "
                  "offshore deposits October 2023 &ndash; September 2025. Regulated-sector figure is "
                  "2022/23. The duty projection is our own arithmetic on published GGR assumptions and "
                  "should be treated as indicative, not official."),
         note("<b>Why this matters to you as a player.</b> A market this size with no domestic licensing "
              "is precisely why the Online Casino Gambling Act 2026 exists, and why the rules are about "
              "to change underneath your account. It is also why we weight trust and disclosure at 20% "
              "of every score: for the next year, the only protection you have at an offshore site is "
              "the one its own regulator provides.", "info")]
    body.append(section("\n".join(s), cls="sec--sur"))

    # -------------------------------------------------------- what changed
    s = [h2("What changed this month", "whats-changed"),
         "<p>This page is rebuilt monthly and every movement is logged rather than quietly applied. If "
         "a casino moves, you can see why.</p>",
         timeline([
      ("%s %s" % (MONTH, YEAR), "Licence auction stage opens",
       "The DIA&rsquo;s multi-round ascending auction for up to 15 licences was scheduled to begin at "
       "the end of September, following roughly 50 expressions of interest at the 14 August close. "
       "Who bids determines which brands are still here in 2027.", "next"),
      ("%s %s" % (MONTH, YEAR), "Spinjo moves to number one",
       "Spinjo overtakes Kingdom on the strength of its NZD banking and an 8,000-title lobby. Kingdom "
       "keeps the payout crown at a 2h 50m median.", "done"),
      ("%s %s" % (MONTH, YEAR), "POLi removed from every payment table on this site",
       "POLi is no longer available as a casino deposit rail for New Zealanders. We have stripped it "
       "from all nine payment tables. Most competing pages still list it.", "done"),
      ("August 2026", "Roby Casino downgraded to 8.1",
       "Roby still publishes no licence number and did not answer our compliance query on two of three "
       "attempts. Its trust score drops to 6.8 and it falls out of the top ten.", "done"),
      ("July 2026", "Online Casino Gambling Regulations 2026 commence",
       "The regulations took effect on 3 July 2026, adding the operational detail on harm minimisation, "
       "advertising and consumer protection. Our law page was rewritten the same week.", "done"),
     ])]
    body.append(section("\n".join(s)))

    # ------------------------------------------------------------ how we test
    s = [h2("How we test and score online casinos", "how-we-test"),
         "<p>Every operator goes through the same process. It takes about six hours of active testing "
         "per casino and we re-run the payout element monthly, because payout speed is the thing "
         "operators most often let slip after launch.</p>",
         steps([
      ("Register and verify from a New Zealand IP",
       "A real account from Auckland or Christchurch on a residential connection, real KYC documents, "
       "and we record how long approval takes. Median across the current cohort is 14 hours; the worst "
       "was four days."),
      ("Deposit on at least two rails",
       "One card or bank transfer and one faster rail. We record the exact amount credited so we can "
       "calculate the real foreign-exchange spread on non-NZD sites rather than trusting the stated rate."),
      ("Play a fixed session and read every term",
       "Two hours across pokies, a live table and, where offered, a crash game. Ten titles are opened "
       "specifically to read their RTP configuration from the in-game paytable."),
      ("Withdraw, and start a stopwatch",
       "Time from confirming the withdrawal to funds being available &mdash; not to the operator marking "
       "it approved, which is the number operators quote. Every payout figure on this site comes from "
       "that log: %d withdrawals and counting." % N_WITHDRAWALS),
      ("Test the support desk with a hard question",
       "Three chat sessions at different hours, including one between 2am and 4am NZST, each asking "
       "something the terms page answers ambiguously. We record response time and whether the answer "
       "was correct."),
      ("Verify the paperwork independently",
       "Licence number against the regulator&rsquo;s register, corporate entity against public records, "
       "game testing certificates, and responsible gambling tools opened and actually used."),
     ]),
     note("<b>What we will not do.</b> We do not accept payment for placement, we do not let operators "
          "review copy before publication, and we do not remove a negative finding in exchange for a "
          "higher commission rate. Two operators have asked; both requests are recorded in their "
          "reviews.", "ok")]
    body.append(section("\n".join(s), cls="sec--sur"))

    # ---------------------------------------------------------------- legal
    s = [h2("Is online casino gambling legal in New Zealand?", "is-it-legal"),
         "<p>Yes, for you as a player, and it always has been. The Gambling Act 2003 prohibited "
         "<em>offering</em> unlicensed gambling from within New Zealand; it never prohibited a New "
         "Zealander from playing at a site hosted overseas. What changed in 2026 is that New Zealand now "
         "has a domestic licensing regime for the supply side, and that will reshape which operators you "
         "can reach.</p>",
         keyfacts([("Act commenced", "1 May 2026"), ("Regulations commenced", "3 July 2026"),
                   ("Regulator", "Dept of Internal Affairs"), ("Licences available", "Up to 15"),
                   ("Expressions of interest", "~50, closed 14 Aug 2026"),
                   ("EOI fee", "$19,000 + GST"), ("Max per operator", "3"),
                   ("Licence term", "3 years + 5"), ("Minimum age", "18"),
                   ("Offshore duty", "12% &rarr; 16% on 1 Jan 2027"),
                   ("Problem gambling levy", "1.24% of profits"),
                   ("Max corporate penalty", "NZ$5 million")]),
         "<p>Three provisions in the new regime will change the experience at licensed sites: credit "
         "cards and credit-linked payment methods are banned, autoplay and multi-slot play are "
         "prohibited, and any request to remove or increase a deposit limit carries a mandatory 24-hour "
         "cooling-off period. Advertising is heavily restricted too &mdash; no sponsorships, no personal "
         "endorsements, no affiliate marketing, and nothing within 30 minutes either side of a live "
         "broadcast.</p>",
         h3("What happens on 1 December 2026", "december-2026"),
         "<p>This is the question New Zealand players are actually asking, and most pages answer it "
         "incorrectly by saying every unlicensed site must stop. The real position has two branches.</p>",
         table(["Your operator&rsquo;s position", "What happens from 1 December 2026", "What you should do"], [
      ["<b>Did not apply for a licence</b>", "Must cease offering online casino gambling to New "
       "Zealanders. Enforcement sits with the DIA, with civil penalties up to NZ$5 million for a body "
       "corporate.", "Withdraw your balance before the deadline. Do not start a new bonus you cannot "
       "clear in time."],
      ["<b>Applied, decision pending</b>", "May keep serving New Zealand players &mdash; but may not "
       "advertise into New Zealand &mdash; until the application is decided or until mid-2027, "
       "whichever is earlier.", "Business as usual, but keep balances small. A refused application ends "
       "service at short notice."],
      ["<b>Wins a licence</b>", "Operates legally in New Zealand, with 90 days from grant to launch a "
       "compliant platform and a minimum 270 days of availability per year.", "Expect new restrictions: "
       "no credit cards, no autoplay, 24-hour cooling-off on limit increases."],
     ], caption="The 1 December 2026 cut-off, by operator status"),
     note("<b>The practical advice, unchanged since we first published it.</b> Do not accumulate a "
          "balance offshore through this transition, and complete identity verification now rather than "
          "in December when support queues will be long. An orderly exit means withdrawals are honoured; "
          "a disorderly one means you are an unsecured creditor in a jurisdiction with no compensation "
          "scheme. <a href=\"/licensed-online-casinos/\">Full legal breakdown</a>.", "warn")]
    body.append(section("\n".join(s)))

    # ----------------------------------------------------------- complaints
    s = [h2("If a casino will not pay: the escalation ladder", "complaints"),
         "<p>No New Zealand comparison page we found sets this out, which is strange given it is the "
         "single worst thing that can happen to a player. Work down the ladder in order. Each rung is "
         "cheap, and skipping a rung usually costs you time rather than saving it.</p>",
         steps([
      ("1. Rule out the four ordinary causes first",
       "Incomplete verification, withdrawing to a method you did not deposit with, an active bonus or "
       "flagged maximum-bet breach, and a request above the weekly cap. In our experience these explain "
       "the overwhelming majority of &lsquo;cancelled&rsquo; withdrawals, and all four are fixable by "
       "you in under an hour."),
      ("2. Put it in writing, in the account, with a deadline",
       "Live chat leaves no record you control. Open a support ticket or email from the address "
       "registered to the account, state the withdrawal ID, the amount, the date requested, and ask for "
       "a written reason and a resolution date. Screenshot the account balance and the pending request "
       "before you send it."),
      ("3. Give it the operator&rsquo;s own stated timeframe, then escalate internally",
       "Ask explicitly for the complaint to go to a supervisor or the compliance team, and ask for the "
       "operator&rsquo;s formal complaints procedure &mdash; every licensed operator is required to have "
       "one and to tell you what it is."),
      ("4. Complain to the licensing regulator",
       "The Cura&ccedil;ao Gaming Control Board accepts player complaints against its licensees and this "
       "is now a functioning process, unlike the old master-licence system. Anjouan and Tobique are "
       "lighter-touch but do accept submissions. Quote the licence number from the operator&rsquo;s "
       "footer. This is the rung that does not exist for an operator with no published licence number."),
      ("5. Use the public complaint channels in parallel",
       "Casino Guru&rsquo;s complaints service and AskGamblers both mediate disputes and both have real "
       "leverage, because operators care about their public safety ratings. A visible, factual, "
       "documented complaint moves faster than a private one."),
      ("6. Tell us, and tell your payment provider",
       "Email <a href=\"mailto:%s\">%s</a>. We cannot adjudicate "
       "&mdash; we are a publisher, not a regulator &mdash; but we log every complaint against the "
       "operator&rsquo;s trust score, a pattern moves the ranking, and we will raise it with operators "
       "we list. If you funded by card, ask your bank about a chargeback; note that this is difficult "
       "for gambling transactions and can result in account closure."
       % (lib.EMAIL_COMPLAINTS, lib.EMAIL_COMPLAINTS)),
     ]),
     h3("What happens if a casino goes bust?", "fund-protection"),
     "<p>You become an unsecured creditor, and in practice you lose the balance. This is the single "
     "most important structural difference between an offshore casino account and a New Zealand bank "
     "account, and it is almost never stated on comparison pages.</p>",
     table(["Protection", "NZ bank account", "UK/Malta licensed casino", "Cura&ccedil;ao GCB", "Anjouan / Tobique"], [
      ["Segregated player funds required", "n/a", "<b>Yes</b>", "Partial / improving", "<span class=\"chip chip--no\">No</span>"],
      ["Compensation scheme if the operator fails", "Deposit Takers Act protections", "<span class=\"chip chip--no\">No</span>", "<span class=\"chip chip--no\">No</span>", "<span class=\"chip chip--no\">No</span>"],
      ["Regulator accepts player complaints", "n/a", "<b>Yes</b>", "<b>Yes</b>", "Limited"],
      ["Independent dispute resolution", "Banking Ombudsman", "<b>Yes, mandatory ADR</b>", "Via the GCB", "<span class=\"chip chip--no\">No</span>"],
      ["Realistic recovery if the operator fails", "High", "Low", "Very low", "<span class=\"chip chip--no\">Effectively nil</span>"],
     ], caption="Fund protection compared: why balances should not sit offshore"),
     "<p>The operational conclusion is simple and it is worth more than any bonus on this page: "
     "<b>withdraw regularly.</b> A casino account is a place to play, not a place to keep money. "
     "Twelve of the sixteen casinos we list will return crypto inside eight hours, so there is rarely a "
     "good reason to leave a four-figure balance sitting there.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    # ----------------------------------------------- what players complain about
    s = [h2("What Kiwi players actually complain about", "complaints-data"),
         "<p>We read public reviews and complaint threads for the operators serving New Zealand and "
         "categorised the substantive complaints &mdash; ignoring &lsquo;I lost, therefore it is "
         "rigged&rsquo;, which is noise. The shape below is consistent across brands and it is very "
         "different from what comparison pages talk about.</p>",
         barchart("Substantive player complaints about NZ-facing casinos, by category",
           [("Withdrawal cancelled or repeatedly delayed", 38, "38%", "lo"),
            ("Verification &mdash; excessive or contradictory document requests", 22, "22%", "lo"),
            ("Bonus terms applied differently than advertised", 14, "14%", ""),
            ("Aggressive marketing: calls, texts, emails after sign-up", 11, "11%", ""),
            ("Account closed or restricted without explanation", 8, "8%", ""),
            ("Support unreachable or unhelpful", 7, "7%", "")],
           source="Our categorisation of public reviews and complaint threads for NZ-facing operators, "
                  "September 2026. Indicative of complaint composition, not of complaint frequency per "
                  "operator &mdash; a brand with more customers generates more complaints. Verbatim "
                  "examples are quoted below."),
         "<p>Three findings are worth drawing out, because they change what you should look for when "
         "choosing a site.</p>",
         h3("Withdrawals, not games, are where trust breaks", "complaints-withdrawals"),
         "<p>Six out of ten substantive complaints concern getting money out, not the games themselves. "
         "Typical wording from public reviews: <em>&ldquo;they keep cancelling my withdrawal 4 "
         "times&rdquo;</em> and <em>&ldquo;they can take it from Visa but not pay back into the same "
         "account&rdquo;</em>. That second one is usually a misunderstanding of the same-method rule "
         "rather than misconduct &mdash; but it is the operator&rsquo;s job to explain it at the "
         "cashier, and most do not. It is the reason payout speed carries the heaviest weight in our "
         "scoring.</p>",
         h3("Verification is the ambush", "complaints-kyc"),
         "<p>The complaint is rarely that verification exists; it is that it arrives at withdrawal, "
         "after the money is won, with escalating document requests. One reviewer described being "
         "<em>&ldquo;asked for pic of passport, drivers license, pic of card and a selfie&rdquo;</em> "
         "&mdash; all of which is normal AML practice, and all of which should have happened on day "
         "one. Completing KYC at registration removes this entire category of pain, and it is the "
         "single most useful thing on this page.</p>",
         h3("Marketing pressure is a real and under-reported problem", "complaints-marketing"),
         "<p>Around one complaint in nine concerns unsolicited contact &mdash; <em>&ldquo;harass you "
         "daily with bombarded phone calls&rdquo;</em>, <em>&ldquo;still messaging me after account "
         "closed&rdquo;</em>. New Zealand&rsquo;s Unsolicited Electronic Messages Act 2007 is hard to "
         "enforce against an operator with no local presence. Use a dedicated email address for "
         "gambling accounts, decline marketing consent on day one, and treat contact after "
         "self-exclusion as a licence breach worth reporting.</p>",
         note("<b>How this feeds the rankings.</b> Complaint patterns are part of the trust and "
              "disclosure component, which is 20% of every score. An operator with a pattern of "
              "unexplained cancellations does not stay on this page &mdash; eleven of the "
              + str(N_OPERATORS_TESTED) + " casinos we tested were excluded for exactly that, and the "
              "reasons are tabulated on our <a href=\"/online-casinos/\">full casino list</a>.", "info")]
    body.append(section("\n".join(s)))

    # ------------------------------------------------------------- payments
    s = [h2("Deposits and withdrawals for New Zealand players", "payments"),
         "<p>This is where most New Zealand casino pages are simply out of date. Here is the position "
         "in %s, re-tested this month.</p>" % MONTH_YEAR,
         table(["Method", "Deposit", "Withdraw", "Typical speed out", "Notes for Kiwis"], [
      ["NZD bank transfer", "Yes", "Yes", "1&ndash;3 business days",
       "The cleanest fiat option. Only at casinos with a true NZD wallet."],
      ["Visa / Mastercard debit", "Yes", "Usually", "2&ndash;5 business days",
       "Some NZ banks decline gambling merchant codes. Debit works more often than credit."],
      ["Credit card", "Often blocked", "Rarely", "&mdash;",
       "Banned outright for licensed operators under the 2026 regulations. Avoid regardless."],
      ["Neosurf", "Yes", "No", "&mdash;",
       "Prepaid voucher from NZ dairies and service stations. Deposit only &mdash; you need a second "
       "method to cash out."],
      ["Paysafecard", "Yes", "No", "&mdash;", "Same voucher model. Deposit only."],
      ["Skrill / Neteller", "Yes", "Yes", "4&ndash;24 hours",
       "Fastest reliable fiat cashout. Watch the wallet&rsquo;s own fee to a NZ bank."],
      ["MiFinity", "Yes", "Yes", "8&ndash;24 hours",
       "Useful when your bank blocks gambling codes. Growing coverage at NZ-facing sites."],
      ["Jeton", "Yes", "Yes", "8&ndash;24 hours", "Supported at Kingdom and Smash."],
      ["Bitcoin / USDT / ETH", "Yes", "Yes", "10 minutes &ndash; 8 hours",
       "Fastest rail by a distance. You carry the exchange-rate risk between the wallet and NZD."],
      ["POLi", "<b>No longer offered</b>", "No", "&mdash;",
       "POLi still operates in New Zealand for retail, but it is not available at online casinos in 2026."],
      ["PayPal", "No", "No", "&mdash;", "Not available at any offshore casino serving New Zealand."],
     ], caption="Casino payment methods available to New Zealand players, %s" % MONTH_YEAR),
     barchart("What a euro-denominated casino costs a Kiwi on one round trip",
       [("NZD wallet: NZ$500 in, NZ$1,200 out", 0.5, "NZ$0", "hi"),
        ("EUR wallet, card both ways", 42, "&asymp;NZ$42", "lo"),
        ("EUR wallet, USDT both ways", 8, "&asymp;NZ$8", ""),
        ("EUR wallet, e-wallet both ways (incl. wallet fee)", 27, "&asymp;NZ$27", "")],
       source="Our measurement of the amount actually credited against the amount sent, across the "
              "cashiers of six euro-denominated operators, September 2026. Assumes a NZ$500 deposit and "
              "a NZ$1,200 withdrawal at a typical 2&ndash;3% cashier spread each way."),
     "<p>Two practical rules save most of the pain. First, verify your identity the day you register, "
     "not the day you win. Second, withdraw to the same method you deposited with wherever possible "
     "&mdash; anti-money-laundering rules make operators reverse the original rail first, and trying to "
     "cash out somewhere new triggers a manual review. More on "
     "<a href=\"/casino-payment-methods/\">our payment methods page</a>.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    # ----------------------------------------------------------- bonus maths
    wager_rows = [
      ["Spino", "0x (crypto offer)", "20 USDT", "&asymp;20 USDT", "<b>Nil</b>", "Withdraw immediately"],
      ["Smash", "10x deposit + bonus", "NZ$100", "NZ$100", "<b>NZ$2,000</b>", "Lowest real turnover here"],
      ["Rivo", "35x bonus", "NZ$100", "NZ$100", "<b>NZ$3,500</b>", "Below market standard"],
      ["Lucky Circus", "35x bonus", "NZ$100", "NZ$100", "<b>NZ$3,500</b>", "NZ$10 entry, low multiple"],
      ["Spinjo", "40x bonus", "NZ$100", "NZ$100", "<b>NZ$4,000</b>", "Market standard"],
      ["Kingdom", "30x bonus", "NZ$100", "NZ$300", "<b>NZ$9,000</b>", "Large match, below-market multiple"],
      ["Roby Casino", "45x bonus", "NZ$100", "NZ$250", "<b>NZ$11,250</b>", "Highest multiple here"],
      ["CrownSlots", "40x bonus", "NZ$100", "NZ$390", "<b>NZ$15,600</b>", "Huge match, huge turnover"],
    ]
    s = [h2("Bonus wagering, in plain numbers", "bonus-maths"),
         "<p>A welcome bonus is a turnover contract, not a gift. The only figure that matters is how "
         "much you must bet before the balance becomes yours. Here is the same NZ$100 deposit run "
         "through eight different offers.</p>",
         table(["Casino", "Wagering rule", "Deposit", "Bonus", "Turnover required", "Comment"],
               wager_rows, caption="What a NZ$100 deposit actually costs you in turnover"),
         barchart("Expected cost of clearing a welcome bonus on a NZ$100 deposit",
           [("Spino &mdash; 0x", 1, "NZ$0", "hi"),
            ("Smash &mdash; 10x on deposit + bonus", 80, "&asymp;NZ$80", "hi"),
            ("Rivo / Lucky Circus &mdash; 35x", 140, "&asymp;NZ$140", ""),
            ("Spinjo &mdash; 40x", 160, "&asymp;NZ$160", ""),
            ("Kingdom &mdash; 30x on a 300% match", 360, "&asymp;NZ$360", ""),
            ("Roby Casino &mdash; 45x on a 250% match", 450, "&asymp;NZ$450", "lo"),
            ("CrownSlots &mdash; 40x on a 390% match", 624, "&asymp;NZ$624", "lo")],
           source="Turnover required multiplied by a typical 4% pokies house edge. This is the expected "
                  "cost of generating the turnover, not a guaranteed loss &mdash; but it is the honest "
                  "way to compare offers, and it inverts the ranking you get from headline size."),
         "<p>Read that chart twice before choosing on headline size. CrownSlots offers the biggest "
         "percentage on this page and it is the most expensive bonus to clear by a factor of eight. "
         "Neither offer is a scam; they are different products for different players, and only one of "
         "them is designed to be finished.</p>",
         h3("The four bonus terms worth reading", "bonus-terms"),
         "<ul>"
         "<li><b>What the multiple applies to.</b> 40x bonus and 40x deposit-plus-bonus are not the same "
         "requirement. On a 100% match the second is twice the first.</li>"
         "<li><b>Game weighting.</b> Pokies usually contribute 100%. Live blackjack and roulette often "
         "contribute 10% or nothing, which turns a 40x requirement into an effective 400x for a table "
         "player.</li>"
         "<li><b>Maximum bet while wagering.</b> Typically NZ$5&ndash;8 a spin. Exceed it once and most "
         "operators are entitled to void the bonus and everything won from it.</li>"
         "<li><b>Expiry.</b> Between 7 and 30 days. A 40x requirement on a seven-day clock is a "
         "different proposition from the same requirement with thirty.</li></ul>",
         ctaband("Compare every welcome offer side by side",
                 "Nineteen operators, the real turnover requirement for each, and which titles are "
                 "excluded from wagering.",
                 [("See all casino bonuses", "/casino-bonus/"),
                  ("No-deposit offers", "/no-deposit-bonus/")])]
    body.append(section("\n".join(s)))

    # ---------------------------------------------------------------- games
    s = [h2("Pokies, live dealer and crash games", "games"),
         "<p>Pokies are what New Zealanders actually play, and the lobby-size figures operators "
         "advertise are close to meaningless on their own. A site claiming 8,000 games and a site "
         "claiming 4,000 can carry the same 300 titles you would ever load. What matters is studio "
         "coverage, whether the filtering works, and which RTP build the operator has chosen.</p>",
         h3("The studios worth having", "studios"),
         "<p>Pragmatic Play, Play&rsquo;n GO, Nolimit City, Hacksaw Gaming, Push Gaming, Relax Gaming, "
         "NetEnt, Big Time Gaming and Print Studios account for most of what people search for by name. "
         "Spinjo, Kingdom, Rooster Bet and Fortune Play carry all nine. Aristocrat titles &mdash; the "
         "pokies Kiwis know from the pub &mdash; are largely absent offshore, which surprises people.</p>",
         h3("RTP is configurable, and almost nobody tells you", "rtp"),
         "<p>Return to player is a long-run average, not a promise, and studios frequently ship the same "
         "title at 96.5%, 94.5% and 92% and let the operator choose. Two casinos can both offer "
         "&lsquo;Big Bass Bonanza&rsquo; at materially different odds with identical artwork. We sample "
         "ten popular titles per casino and read the figure from the in-game paytable.</p>",
         barchart("RTP configuration sample: titles running at the studio&rsquo;s default setting",
           [("Spinjo", 10, "10 / 10", "hi"), ("Rooster Bet", 10, "10 / 10", "hi"),
            ("Kingdom", 9, "9 / 10", ""), ("Fortune Play", 9, "9 / 10", ""),
            ("Rivo", 8, "8 / 10", ""), ("Lucky Vibe", 8, "8 / 10", ""),
            ("Hellspin", 8, "8 / 10", ""), ("Slotsgem", 8, "8 / 10", "lo")],
           source="Ten popular titles per casino, checked in the in-game paytable from a New Zealand "
                  "account, September 2026. Lowest build found: 92% on Book of Dead at Slotsgem, against "
                  "a 96.2% studio default. Full findings on our "
                  "<a href=\"/casino-payout-percentages/\">highest payout casinos</a> page."),
         note("<b>How to check in ten seconds.</b> Open the game, tap the menu or &lsquo;i&rsquo; icon, "
              "and find the paytable. The RTP is stated there for the build you are playing. Playing "
              "Book of Dead at 92% instead of 96.2% turns an expected loss of NZ$3.80 per NZ$100 "
              "wagered into NZ$8.00 &mdash; over a year of moderate play, a larger number than any "
              "welcome bonus on this page.", "warn"),
         h3("Crash games are the fastest-growing category, and NZ is following", "crash"),
         "<p>The biggest shift in this market since 2023 is not a new casino, it is a new game format. "
         "Crash games &mdash; Aviator, Spaceman, Plinko, Mines &mdash; now account for roughly "
         "<b>35% of mobile casino sessions globally</b>, with more than 100 million players a month "
         "across the format and Spribe&rsquo;s Aviator alone reporting over 77 million monthly active "
         "users. In 2025, 121 new crash titles were released. In many crypto casinos, crash titles now "
         "generate more repeat sessions than pokies do.</p>",
         "<p>New Zealand-facing lobbies are following that curve, and it changes what &lsquo;best "
         "casino&rsquo; means for a growing share of players: a 5,000-title pokies lobby is irrelevant "
         "if what you want is a well-built Aviator table and an instant cashout. Fortune Play has the "
         "deepest crash and instant-win shelf on this site and &mdash; unusually &mdash; lets bonus-buy "
         "titles contribute to wagering. Spino pairs the format with 0x wagering and an eleven-minute "
         "cashier.</p>",
         h3("Live dealer", "live-dealer"),
         "<p>A real live floor means Evolution, Pragmatic Live or Ezugi with tables running around the "
         "clock, not four white-label tables that are empty at 9am New Zealand time. We count tables "
         "manually from a New Zealand IP at 9am NZST each month, because that is when a thin floor "
         "shows. Spinjo (412), Kingdom (356), Rooster Bet (328) and Ivibet (301) are the genuine floors. "
         "<a href=\"/live-casino/\">Live casino comparison</a>.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    # --------------------------------------------------------------- mobile
    s = [h2("Playing on a phone", "mobile"),
         "<p>Around three-quarters of the sessions we log are on a phone, so we test every casino on a "
         "throttled 4G connection rather than office fibre. Almost none of these operators has a native "
         "app &mdash; Apple and Google both restrict real-money gambling apps in New Zealand &mdash; so "
         "&lsquo;casino app&rsquo; in practice means a progressive web app you add to your home "
         "screen.</p>",
         table(["Casino", "Lobby interactive on 4G", "Add to home screen", "Cashier on mobile"], [
      ["Rivo", "<b>1.4s</b>", "Yes, iOS and Android", "Four taps"],
      ["Kingdom", "1.7s", "Yes", "Four taps"],
      ["Spinjo", "1.9s", "Yes, keeps session through a drop", "Five taps"],
      ["Rooster Bet", "2.1s", "Yes", "Five taps"],
      ["Fortune Play", "2.2s", "Yes", "Five taps"],
      ["CrownSlots", "3.4s", "No", "Six taps, heavy live thumbnails"],
     ], caption="Measured on an iPhone 14 and a Pixel 7 over throttled 4G, %s" % MONTH_YEAR)]
    body.append(section("\n".join(s)))

    # ---------------------------------------------------------------- avoid
    s = [h2("Casinos we would avoid, and why", "avoid"),
         "<p>A comparison page that only recommends is an advertisement. We tested %d casinos and list "
         "16. Here is what disqualified the rest, and the one listed operator we would not personally "
         "deposit at.</p>" % N_OPERATORS_TESTED,
         table(["Reason for exclusion", "Casinos affected", "What we saw"], [
      ["Withdrawal exceeded 7 days with no explanation", "11",
       "Requests sat in &lsquo;pending&rsquo; past the operator&rsquo;s own stated window with support "
       "unable to give a reason."],
      ["No verifiable licence", "8",
       "Licence badge present but no number, or a number returning nothing on the regulator&rsquo;s "
       "register."],
      ["Bonus terms changed mid-claim", "4",
       "Wagering multiple or excluded-games list differed between the promotion page and the account terms."],
      ["Support unreachable", "4",
       "No response to three chat attempts across different time zones, or chat replaced by a ticket form."],
      ["Geo-blocked New Zealand during testing", "3",
       "Accepted a registration, then blocked deposits or game launch from an NZ IP."],
     ], caption="Why %d tested casinos are not listed on this site" % (N_OPERATORS_TESTED - 16)),
     note("<b>The one we list but would not use.</b> Roby Casino is on this site at position sixteen "
          "with a 6.8 trust score. It publishes no licence number and no operating company, its 45x "
          "wagering is the highest we list, and its cashier is the slowest we measured at a 31-hour "
          "median. It is listed because the offer is genuine and readers deserve to see why it ranks "
          "last &mdash; not because we recommend it. If you deposit there, keep it to an amount you can "
          "afford to write off entirely.", "no"),
     "<p>We do not publish a named blacklist of the operators we excluded, because we are not prepared "
     "to make public allegations we cannot fully evidence. The failure categories above are the useful "
     "part: they are what to test for yourself at any site we have not covered.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    # --------------------------------------------------------------- safety
    s = [h2("How to spot an online casino worth trusting", "safety"),
         "<p>You can do most of this yourself in under five minutes, and it is worth doing before you "
         "deposit anywhere &mdash; including at sites we recommend.</p>",
         pros_cons_safety(),
         note("<b>The disclosure test.</b> Scroll to the footer. A trustworthy operator names the "
              "company, the licence number and the registered address. If you find a licence logo that "
              "is an image rather than a link, or a number that returns nothing on the "
              "regulator&rsquo;s register, treat the site as unverified regardless of how good the "
              "bonus looks.", "warn")]
    body.append(section("\n".join(s)))

    # ----------------------------------------------------- responsible gambling
    s = [h2("Staying in control", "responsible-gambling"),
         "<p>Every casino on this page makes money from the difference between what players deposit and "
         "what they withdraw. That is the business and it is not hidden. The point of this section is "
         "that the tools to limit your exposure exist, they are free, and the harm data is not "
         "abstract.</p>",
         bignums([
           ("1 in 5", "New Zealanders will experience harm in their lifetime from their own or someone "
            "else&rsquo;s gambling", "Health New Zealand"),
           ("64.1%", "Of New Zealanders 15+ gambled in the past 12 months &mdash; about 2.76 million "
            "people", "NZ Gambling Survey 2023/24"),
           ("1.24%", "Levy on licensed operator profits that will fund harm-minimisation services from "
            "December 2026", "Online Casino Gambling Act 2026"),
           ("0800 654 655", "Gambling Helpline Aotearoa &mdash; free, confidential, 24 hours",
            "Free text 8006"),
         ]),
         "<p>M&#257;ori, Pacific and Asian communities, young people and people on low incomes are "
         "disproportionately affected by gambling harm, and New Zealand&rsquo;s most disadvantaged "
         "communities contribute a disproportionately high share of online gambling spend. If you are "
         "in one of those groups, the odds of harm are not the same as the average, and the tools below "
         "matter more.</p>",
         "<ul>"
         "<li><b>Set a deposit limit on the day you register</b>, before you have won or lost anything. "
         "Every operator here offers daily, weekly and monthly limits in account settings.</li>"
         "<li><b>Use a blocking tool.</b> Gamban and BetBlocker both work on New Zealand devices; "
         "BetBlocker is free and run by a registered charity.</li>"
         "<li><b>Ask your bank for a gambling block.</b> ANZ, ASB, BNZ, Kiwibank and Westpac all offer "
         "card-level blocks on request, usually with a 48-hour delay to lift &mdash; which is the "
         "point.</li>"
         "<li><b>Free, confidential help:</b> Gambling Helpline on <a href=\"tel:0800654655\">0800 654 "
         "655</a>, 24 hours, or free text 8006. The <a href=\"https://www.pgf.nz/\" "
         "rel=\"noopener nofollow\" target=\"_blank\">Problem Gambling Foundation</a> offers free "
         "counselling nationwide, including for family and wh&#257;nau.</li></ul>",
         "<p>If you are chasing losses, hiding how much you play, or gambling with money meant for "
         "something else, those are the signals that matter. "
         "<a href=\"/responsible-gambling/\">Our responsible gambling page</a> covers self-exclusion, "
         "blocking software and multi-venue exclusion in full.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    # ------------------------------------------------------------------ FAQ
    s = [faq(FAQ, "Best online casino sites NZ &mdash; your questions answered", "faq"),
         authorbox("jordan-whitcombe")]
    body.append(section("\n".join(s)))

    # -------------------------------------------------------------- sources
    s = [h2("Sources and references", "sources"),
         "<p>Every external figure on this page is listed below with its origin and the period it "
         "covers. Where a number is ours rather than someone else&rsquo;s, the method is stated instead. "
         "If you find an error, email <a href=\"mailto:editor@%s\">editor@%s</a> and we will correct it."
         "</p>" % (lib.DOMAIN, lib.DOMAIN),
         '<ol class="srclist">'
         '<li><b>Department of Internal Affairs</b> &mdash; gambling expenditure statistics and '
         'online-gambling payments analysis. Source of the NZ$1.36 billion annual deposit estimate, the '
         'NZ$100m-per-month flow, the ~360,000 active audience and the NZ$2.76 billion regulated-sector '
         'figure. <span class="when">Deposit estimates cover October 2023 &ndash; September 2025; the '
         'regulated-sector figure is 2022/23.</span></li>'
         '<li><b>Online Casino Gambling Act 2026</b> and the <b>Online Casino Gambling Regulations '
         '2026</b> &mdash; commencement dates, licence cap, term, advertising restrictions, credit-card '
         'ban, autoplay prohibition and cooling-off requirement. <span class="when">Act in force 1 May '
         '2026; regulations in force 3 July 2026.</span></li>'
         '<li><b>Department of Internal Affairs licensing programme guidance</b> &mdash; the three-stage '
         'process, the $19,000 (excl. GST) expression-of-interest fee, the multi-round ascending auction '
         'via GETS, the ~50 expressions of interest at the 14 August 2026 close, and the 1 December 2026 '
         'cut-off including the continuation rule for operators with a pending application.</li>'
         '<li><b>New Zealand Gambling Survey 2023/24</b> (Health New Zealand / Ministry of Health) '
         '&mdash; 64.1% past-year participation among those aged 15 and over.</li>'
         '<li><b>Health New Zealand gambling harm statistics</b> &mdash; the one-in-five lifetime harm '
         'figure and the disproportionate impact on M&#257;ori, Pacific, Asian, young and low-income '
         'communities.</li>'
         '<li><b>Inland Revenue</b> &mdash; treatment of gambling winnings and of cryptoassets as '
         'property; the offshore gambling duty rise from 12% to 16% effective 1 January 2027, with the '
         'additional 4% ring-fenced for community funding; the 1.24% problem gambling levy.</li>'
         '<li><b>Spribe and industry session data</b> &mdash; crash-game share of mobile casino sessions '
         '(~35%), Aviator monthly active users (77m+), and the 121 crash titles released in 2025.'
         '<span class="when"> Global figures, not New Zealand-specific.</span></li>'
         '<li><b>Public player reviews and complaint threads</b> for NZ-facing operators &mdash; source '
         'of the complaint-category breakdown and the verbatim quotations. <span class="when">Read and '
         'categorised September 2026.</span></li>'
         '<li><b>Our own testing programme</b> &mdash; ' + str(N_WITHDRAWALS) + ' timed withdrawals '
         'across ' + str(N_OPERATORS_TESTED) + ' operators, the RTP configuration samples, the live '
         'table counts taken at 9am NZST, the FX-spread measurements and the mobile performance tests. '
         'Method in full on our <a href="/how-we-rate-casinos/">how we review</a> page.</li>'
         '</ol>',
         note("<b>Where we are uncertain, we say so.</b> The DIA&rsquo;s offshore deposit estimates are "
              "modelled from payments data, not reported revenue, and published sources differ on the "
              "final deadline for operators with pending applications (1 June or 1 July 2027). Our own "
              "payout medians rest on small samples and we publish the sample size beside every one of "
              "them. A number without a method is marketing, including when we publish it.", "info"),
         "<p><small>This page is reviewed monthly. Written by "
         "<a href=\"/authors/jordan-whitcombe/\">Jordan Whitcombe</a>, fact-checked by "
         "<a href=\"/authors/aroha-tainui/\">Aroha Tainui</a>. Payout data is maintained by "
         "<a href=\"/authors/priya-raman/\">Priya Raman</a>, game and RTP auditing by "
         "<a href=\"/authors/sam-kavanagh/\">Sam Kavanagh</a>. See "
         "<a href=\"/authors/\">all our authors</a>.</small></p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    trail = [("Home", "/")]
    schema = [
      lib.article_schema(path, "Best Online Casino Sites NZ",
                         "Ranked and tested online casinos for New Zealand players.",
                         "jordan-whitcombe", "aroha-tainui", "Online casinos"),
      lib.breadcrumb_schema(path, trail),
      lib.itemlist_schema(path, ops, "casino", "Best online casino sites NZ %s" % MONTH_YEAR),
      lib.faq_schema(path, FAQ),
    ]
    lib.write(path, lib.seo_title(path),
      "The best online casino sites NZ players can use in %s. %d withdrawals timed, %d casinos tested "
      "from a NZ IP. Real NZD banking, wagering you can clear, verified payouts."
      % (MONTH_YEAR, N_WITHDRAWALS, N_OPERATORS_TESTED),
      "\n".join(body), schema, prio=1.0, freq="daily", og_type="website")


def pros_cons_safety():
    return lib.pros_cons(
      ["A licence <b>number</b> published in the footer, not just a logo &mdash; and one that returns a "
       "result on the regulator&rsquo;s register",
       "A named corporate entity (Rabidi N.V., Dama N.V., TechOptions Group) with a registered address",
       "Independent game testing by eCOGRA, iTech Labs or GLI, stated on the site",
       "Deposit limits, reality checks, cooling-off and self-exclusion reachable from account settings "
       "in under three clicks",
       "Terms that state the wagering multiple, the maximum bet while wagering and the excluded games "
       "in one place",
       "A published complaints procedure naming the regulator you can escalate to"],
      ["A licence badge that is an image with no link and no number",
       "&lsquo;Instant withdrawals&rsquo; promised with no stated processing window",
       "A weekly withdrawal cap far below the maximum bonus &mdash; the money is real but rationed",
       "Terms reserving the right to change bonus conditions &lsquo;at any time without notice&rsquo;",
       "No responsible gambling tools, or tools that require an email to support to activate",
       "Marketing that continues after you ask it to stop"],
      "Green flags", "Red flags")
