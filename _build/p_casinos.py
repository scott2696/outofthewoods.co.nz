# -*- coding: utf-8 -*-
"""/online-casinos/ and /casino-bonus/"""
import lib
from lib import (MONTH_YEAR, MONTH, YEAR, NAME, N_WITHDRAWALS, N_OPERATORS_TESTED,
                 pick, leaderboard, table, op_cell, faq, keyfacts, note, verdict,
                 toc, steps, cards, ctaband, authorbox, byline, hero, section,
                 h2, h3, pros_cons, DISCLOSURE, crumbs, timeline)

ORDER = ["spinjo", "kingdom", "rooster-bet", "crownslots", "fortune-play", "smash",
         "lucky7even", "rivo", "lucky-vibe", "madcasino", "lucky-circus", "spino",
         "ivibet", "hellspin", "roby-casino", "slotsgem"]

NOTES = {
 "spinjo": "Best overall. ~8,000 games, true NZD wallet, Cura&ccedil;ao GCB licence under Rabidi N.V.",
 "kingdom": "Fastest verified payouts on this site and 30x on a 600% staged package.",
 "rooster-bet": "Dama N.V. build quality, 6,000 games and a full sportsbook on one NZD balance.",
 "crownslots": "Biggest percentage match here. Euro wallet, so price in the FX on both legs.",
 "fortune-play": "The crash, Aviator and bonus-buy specialist, with bonus buys eligible for wagering.",
 "smash": "10x on deposit plus bonus &mdash; the lowest effective turnover in New Zealand-facing casinos.",
 "lucky7even": "Twenty no-deposit spins up front, then a modest but clean NZ$1,700 match at 40x.",
 "rivo": "Fastest mobile build we measured: interactive lobby in 1.4 seconds on throttled 4G.",
 "lucky-vibe": "Weekly cashback paid as withdrawable cash. Built for month twelve, not day one.",
 "madcasino": "One NZ$20 account for pokies and sport, with a separate NZ$400 sports welcome.",
 "lucky-circus": "NZ$10 minimum and 35x wagering &mdash; the friendliest terms for a small deposit.",
 "spino": "0x wagering and an eleven-minute fastest cashout. Crypto only, no fiat at all.",
 "ivibet": "300 live tables and a NZ$500 bonus at 35x that an ordinary player can finish.",
 "hellspin": "Daily and weekly slot races with published prize pools, running since 2021.",
 "roby-casino": "Large bonus, no published licence number. Listed with that warning attached.",
 "slotsgem": "The calm one. No pop-ups, no wheel, no countdown &mdash; and a slower cashier.",
}

FAQ = [
 ("How many online casinos accept New Zealand players?",
  "<p>Several hundred offshore sites will take a New Zealand registration. That number is not useful. "
  "The number that matters is how many hold a verifiable licence, publish a corporate entity, support "
  "New Zealand dollars and pay out inside a stated window. We tested %d and list 16 &mdash; the rest "
  "failed on payout time, disclosure or support quality.</p>" % N_OPERATORS_TESTED),
 ("What should I look at first when choosing an online casino?",
  "<p>Withdrawal terms, before anything else. Specifically: the weekly withdrawal cap, the stated "
  "processing window for the rail you will actually use, and whether identity verification happens at "
  "registration or at first cashout. A casino with a brilliant bonus and a NZ$4,000 weekly cap will "
  "ration a good win back to you over a month. The bonus is the last thing to compare, not the first.</p>"),
 ("Are online casinos with a Cura&ccedil;ao licence safe?",
  "<p>It depends entirely on the operator, and it is checkable rather than a matter of faith &mdash; "
  "the six-row table above is how. On licensing specifically: Cura&ccedil;ao replaced its old "
  "master-licence system with direct "
  "licensing by the Cura&ccedil;ao Gaming Control Board, which means a named licensee, published "
  "conditions and a complaints process that exists. It is still lighter-touch than the Malta Gaming "
  "Authority or the UK Gambling Commission. Treat a Cura&ccedil;ao GCB licence held by a named company "
  "as a reasonable baseline, an Anjouan or Tobique licence as thinner, and no published licence at all "
  "as a reason to keep your deposit small.</p>"),
 ("Which online casinos pay out the fastest in New Zealand?",
  "<p>On our timed data: Spino (11 minutes to 2 hours, crypto only), Kingdom (median 2h 50m across "
  "seven crypto withdrawals), CrownSlots (fastest single result at 68 minutes) and Rooster Bet (median "
  "3 hours). For fiat, Skrill and Neteller clear in 4&ndash;24 hours at most of these sites, and NZD "
  "bank transfers take one to three business days. Full data on our "
  "<a href=\"/fast-payout-casinos/\">fast payout casinos</a> page.</p>"),
 ("Can I open accounts at more than one casino?",
  "<p>Yes, and most regular players should. Different sites are better at different things and welcome "
  "offers are one-per-person-per-site, not one-per-person. What you must not do is open two accounts at "
  "the <em>same</em> casino &mdash; that breaches the terms at every operator here and is the most "
  "common reason a withdrawal gets voided.</p>"),
 ("Do online casinos let you play for free?",
  "<p>Most offer demo play on pokies without registering, which is genuinely useful for learning a "
  "game&rsquo;s volatility before betting real money. Live dealer tables and jackpot titles never have "
  "a demo mode, and neither do bonus-buy features. Demo results are not predictive &mdash; a demo "
  "session runs on the same RNG but a short sample tells you nothing about the long run.</p>"),
 ("What happens to my account after 1 December 2026?",
  "<p>Operators that have not applied for a New Zealand licence must stop offering online casino "
  "gambling to New Zealanders from that date. Practically, expect some sites to geo-block New Zealand "
  "IPs, some to close registrations but honour withdrawals, and some to continue and be dealt with by "
  "the Department of Internal Affairs. Do not hold a large balance offshore through the changeover. "
  "<a href=\"/licensed-online-casinos/\">Full detail here</a>.</p>"),
 ("What is the best online casino for Kiwis, and for beginners?",
  "<p>Spinjo, on both counts. It is the best rated online casino New Zealand players can open on our "
  "scoring at 9.3/10, and it is also the one we would hand to someone opening their first account: a "
  "New Zealand dollar wallet so nothing is lost to conversion, a licence held by a named company you "
  "can look up, and a lobby that is actually navigable. The best online casino NZ has for beginners is "
  "rarely the one with the biggest bonus &mdash; a 390% match at 40x is a worse first experience than "
  "a 100% match you can finish.</p>"),
 ("Which online casino pays out the most in NZ?",
  "<p>Two different questions hide in that one. If you mean which pays out fastest, Kingdom, at a "
  "verified two hour fifty minute median across seven timed withdrawals. If you mean which returns "
  "the most of what you stake, Spinjo and Rooster Bet were the only casinos where all ten titles we "
  "sampled ran at the studio&rsquo;s default RTP. "
  "<a href=\"/casino-payout-percentages/\">The payout data is here</a>.</p>"),
 ("What is the most trusted online casino NZ readers ask about?",
  "<p>By our trust and disclosure component &mdash; licence verifiability, named operator, "
  "independent testing, complaints route &mdash; Spinjo scores highest at 9.2, followed by Rooster Bet "
  "and Fortune Play, all three Cura&ccedil;ao Gaming Control Board licensees under named companies. "
  "Be wary of the phrase itself: &lsquo;most trusted&rsquo; is the easiest claim in this industry to "
  "make and the hardest to evidence, which is why we publish the component scores rather than the "
  "adjective.</p>"),
 ("Is there a best online casino NZ Reddit consensus?",
  "<p>Not a reliable one. Threads on New Zealand gambling turn over quickly, are thin on verifiable "
  "detail, and are a known target for undisclosed promotion. What Reddit is genuinely useful for is "
  "payout complaints: if several unrelated accounts describe the same withdrawal problem at the same "
  "operator over months, that is a signal worth acting on. We read them for exactly that and nothing "
  "else. Our own complaint categorisation is on the <a href=\"/\">homepage</a>.</p>"),
 ("What is the best online casino NZ low deposit players should pick?",
  "<p>Lucky Circus, at a NZ$10 minimum with 35x wagering &mdash; the only site here below NZ$20. "
  "Smash is the better value if you can reach NZ$20, because 10x on deposit plus bonus is a quarter "
  "of the market-standard turnover. For an online casino NZ real money no deposit start, Lucky7even "
  "gives you 20 spins before you fund anything at all.</p>"),
 ("How do you decide the order of this list?",
  "<p>A weighted score out of ten: payout speed 25%, bonus value 20%, game library 20%, banking and "
  "NZD support 15%, trust and disclosure 20%. Each component is marked from evidence we collected "
  "ourselves, and the component marks are published in every review so you can re-weight them for "
  "your own priorities. Commission rates play no part &mdash; our highest-paying partner is not our "
  "top-ranked casino. <a href=\"/how-we-rate-casinos/\">Full methodology</a>.</p>"),
]

BONUS_FAQ = [
 ("What is the best casino bonus in NZ right now?",
  "<p>It depends entirely on whether you intend to clear it. On raw headline value, Smash leads at "
  "600% up to NZ$19,500 and Kingdom follows at 600% up to NZ$18,500. On <em>clearable</em> value, "
  "Smash is the clear winner because 10x on deposit plus bonus is roughly a quarter of the turnover "
  "any 40x offer demands. If you want the winnings without any turnover at all, Spino&rsquo;s crypto "
  "offer is 0x.</p>"),
 ("What does 40x wagering actually mean?",
  "<p>It means you must place bets totalling 40 times the bonus amount before the bonus balance and "
  "anything won from it can be withdrawn. A NZ$200 bonus at 40x is NZ$8,000 of turnover. That is not "
  "NZ$8,000 of losses &mdash; you are recycling the same balance &mdash; but at a typical 4% house "
  "edge on pokies you would expect to lose around NZ$320 generating it.</p>"),
 ("Is 40x on bonus the same as 40x on deposit plus bonus?",
  "<p>No, and this is the most expensive misreading in online gambling. On a 100% match of a NZ$100 "
  "deposit, 40x bonus is NZ$4,000 of turnover. 40x deposit plus bonus is NZ$8,000. Always check which "
  "the terms specify. Smash uses deposit plus bonus but at 10x, which still works out far lower than "
  "any 40x offer here.</p>"),
 ("Do free spins have their own wagering requirement?",
  "<p"
  ">Usually yes, and often a higher one. Lucky7even, for example, applies 40x to the match bonus but "
  "50x to winnings from its no-deposit free spins. Free spin winnings also frequently carry a separate "
  "maximum cash-out &mdash; commonly NZ$100 to NZ$200 &mdash; regardless of how much you win.</p>"),
 ("Which games count towards wagering?",
  "<p>Pokies almost always contribute 100%. Live blackjack and roulette typically contribute 10% or "
  "nothing. Video poker, craps and anything with a very low house edge is usually excluded entirely, "
  "and most operators exclude a named list of high-RTP pokies too. If table games are what you play, "
  "check the weighting before you accept a bonus &mdash; at 10% contribution a 40x requirement becomes "
  "an effective 400x.</p>"),
 ("Is there a maximum bet while I am wagering a bonus?",
  "<p>Yes, typically NZ$5 to NZ$8 per spin or hand. Exceeding it even once gives the operator grounds "
  "to void the bonus and every dollar won from it, and this is enforced. If you are used to NZ$20 "
  "spins, either decline the bonus or change your stake for the duration.</p>"),
 ("Are casino bonuses worth it in NZ?",
  "<p>A deposited bonus is worth taking when the turnover it demands costs less than the bonus is "
  "worth, and not otherwise. At 10x on deposit plus bonus &mdash; Smash &mdash; that is clearly true. "
  "At 45x on a 250% match &mdash; Roby Casino &mdash; it clearly is not. The honest test is the "
  "turnover table above, not the headline. If you mainly play live dealer or table games, the answer "
  "is usually no, because those contribute 10% or less towards wagering. No deposit offers work on "
  "entirely different terms and live on our "
  "<a href=\"/no-deposit-bonus/\">no deposit bonus NZ page</a>.</p>"),
 ("Can I withdraw my deposit if I change my mind about a bonus?",
  "<p>Usually yes, but only if you have not started wagering. Most terms here let you forfeit an "
  "unused bonus from account settings and withdraw the cash balance. Once you have placed a single "
  "bet with bonus funds active, forfeiting typically means losing the bonus and any winnings from it, "
  "keeping only your original deposit less what you have lost.</p>"),
 ("Do reload bonuses and cashback have wagering too?",
  "<p>Reload bonuses do, normally at the same multiple as the welcome offer. Cashback varies and this "
  "is where real value hides: Lucky Vibe credits cashback as withdrawable cash with no turnover, while "
  "most operators credit it as bonus funds carrying a fresh 30&ndash;40x. Identical headline "
  "percentages, completely different products.</p>"),
]


def build_hub():
    path = "/online-casinos/"
    ops = [lib.BY[s] for s in ORDER]

    fee_rows = []
    for o in ops[:12]:
        fee_rows.append([op_cell(o),
                         o["withdrawal_limit"],
                         o["payout_ewallet"],
                         o["payout_card"],
                         o["licence"],
                         o["operator_co"]])

    body = []
    body.append(hero(
      "All 16 ranked &middot; updated %s" % MONTH_YEAR,
      lib.seo_h1(path),
      "The complete ranked list of NZ casino sites accepting New Zealand players &mdash; all sixteen "
      "we are prepared to list, including the ones we would not use ourselves and why. Every real "
      "money casino NZ readers ask about is scored on verified "
      "payout times, clearable bonus value, NZD banking, library depth and what each operator discloses "
      "about itself.",
      stats=[("16", "Casinos listed"), ("%d" % N_OPERATORS_TESTED, "Casinos tested"),
             ("%d" % N_WITHDRAWALS, "Withdrawals timed"), ("25%", "Weight on payout speed")],
      ctas=[("See the ranking", "#ranked"), ("Compare the terms", "#terms")],
      meta=([("Home", "/"), ("Online casinos", None)], "jordan-whitcombe", "priya-raman"),
      offer=lib.hero_offer(ops[0], "casino")))

    s = [DISCLOSURE]
    s.append("<p>This is the full list. The <a href=\"/\">homepage top ten</a> is the shortlist; this "
             "page ranks every online casino we have tested and cleared for New Zealand players, "
             "including four we score below 8.3 and would not personally deposit at. They are here "
             "because a list that only contains recommendations is an advertisement, not a comparison.</p>")
    s.append("<p>Every casino below was opened from a New Zealand IP address, funded with real money and "
             "cashed out at least once. Where a site has a structural problem for a Kiwi &mdash; a euro "
             "wallet, a missing licence number, a NZ$4,000 weekly cap &mdash; it is in the listing, not "
             "hidden in the review.</p>")
    s.append(toc([("Every online casino real money NZ list", "ranked"),
                  ("Safe and trusted casinos", "safe-trusted"),
                  ("Withdrawal terms compared", "terms"),
                  ("How to choose, in the right order", "how-to-choose"),
                  ("What an online casino actually offers", "what-you-get"),
                  ("Casinos we tested and left out", "rejected"),
                  ("Opening an account, step by step", "sign-up"),
                  ("Frequently asked questions", "faq")]))
    _intro = section("\n".join(s), cls="ord-intro")

    s = [h2("Best casino sites NZ, ranked 1 to 16", "ranked"),
         '<p class="rank-note">The top online casinos NZ players can open, scored out of ten. '
         'Component marks are published in each review so you can re-weight them for how you '
         'play.</p>',
         leaderboard(ops, "casino", NOTES, top_n=3)]
    body.append(section("\n".join(s), cls="ord-lb"))
    body.append(_intro)

    s = [h2("Withdrawal terms at NZ online casinos, compared", "terms"),
         "<p>The numbers that decide whether a win reaches your bank account this week or next month. "
         "Weekly caps are the term players notice last and regret first.</p>",
         table(["Casino", "Weekly cap", "E-wallet out", "Card out", "Licence", "Operating company"],
               fee_rows, caption="Withdrawal limits and disclosure, top 12 casinos, %s" % MONTH_YEAR),
         note("<b>Read the weekly cap against the bonus.</b> Roby Casino advertises up to NZ$5,000 in "
              "bonus funds against a NZ$5,000 weekly withdrawal cap and a three-to-five-day card "
              "window. If you cleared the maximum, extracting it would take most of a month. Kingdom "
              "and Smash both cap at NZ$10,000 a week with crypto out in hours &mdash; a structurally "
              "different proposition.", "warn")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Safe and trusted online casinos NZ players can actually verify", "safe-trusted"),
         "<p>&lsquo;Safe&rsquo; and &lsquo;trusted&rsquo; are the two words this industry uses most "
         "and evidences least. The safe online casinos NZ players should shortlist are the ones where "
         "you can check the claim yourself in about five minutes, and the trusted online casinos NZ "
         "readers ask us about are usually trusted because somebody said so in an advert.</p>",
         table(["What to check", "Where to look", "What good looks like", "How many of our 16 pass"], [
      ["A licence number, not a badge", "Site footer",
       "A number that returns a result on the regulator&rsquo;s public register", "15 of 16"],
      ["A named operating company", "Footer or terms",
       "Rabidi N.V., Dama N.V., Vertikal N.V., TechOptions Group", "13 of 16"],
      ["Independent game testing", "Footer or help pages", "eCOGRA, iTech Labs or GLI named", "14 of 16"],
      ["A published complaints route", "Terms or help centre",
       "Names the regulator you can escalate to", "13 of 16"],
      ["Responsible gambling tools", "Account settings",
       "Deposit limit, cooling-off and self-exclusion inside three clicks", "16 of 16"],
      ["A withdrawal you can actually make", "Cashier",
       "A stated window and a weekly cap above the maximum bonus", "12 of 16"],
     ], caption="How to separate safe online casinos NZ can rely on from sites that only say so"),
         "<p>Roby Casino fails the first two rows, which is why it is last. That single fact matters "
         "more than its bonus, and it is the reason we list the casino sites New Zealand players "
         "should be careful with alongside the ones we recommend.</p>",
         h3("Online casinos that accept NZD", "nzd"),
         "<p>The most useful practical filter, and one almost no ranking applies. An NZD online casino "
         "holds your balance in New Zealand dollars, so nothing is converted on the way in or the way "
         "out. The rest convert twice at a rate the cashier sets, typically costing 2&ndash;3% each "
         "way &mdash; roughly NZ$42 on a NZ$500 deposit and a NZ$1,200 withdrawal.</p>",
         "<p>Ten of the sixteen online casinos that accept NZD are on this page: Spinjo, Kingdom, "
         "Rooster Bet, Fortune Play, Smash, Rivo, Lucky Vibe, Lucky7even, Lucky Circus and MadCasino. "
         "CrownSlots, Gunsbet, Ivibet, Hellspin, Slotsgem and Roby Casino do not. "
         "<a href=\"/casino-payment-methods/\">Full banking comparison</a>.</p>",
         h3("Where online gambling NZ is heading", "heading"),
         "<p>Online gambling in NZ is about to change shape. The Online Casino Gambling Act 2026 "
         "commenced on 1 May 2026 and the Department of Internal Affairs will issue up to 15 licences, "
         "with unlicensed operators that have not applied required to stop serving New Zealanders from "
         "1 December 2026. That will narrow the field of best online gambling sites NZ players can "
         "reach, and it will add real protections at the ones that survive &mdash; no credit cards, no "
         "autoplay, and a mandatory cooling-off on deposit-limit increases. "
         "<a href=\"/licensed-online-casinos/\">Our licensing page tracks it</a>.</p>",
         note("<b>New online casinos NZ players are considering during the transition.</b> A 2024 or "
              "2025 launch is not inherently riskier, but it has no payment record through a bad "
              "quarter and a real commercial question about whether to bid for a licence. Keep "
              "balances small and withdraw regularly until the licence list is published. "
              "<a href=\"/new-casinos-nz/\">The launch tracker is here</a>.", "info")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("How to choose an online casino, in the right order", "how-to-choose"),
         "<p>Most guides start with the bonus. That is the wrong end. Work down this list and you will "
         "rarely pick badly.</p>",
         steps([
      ("1. Can you get your money out, and how fast?",
       "Check the weekly withdrawal cap, the stated window for the rail you will use, and whether "
       "there is a minimum withdrawal. This single check eliminates more bad choices than everything "
       "else combined."),
      ("2. Does it hold your balance in New Zealand dollars?",
       "A euro or USD wallet costs roughly 2&ndash;3% each way. On a year of ordinary play that is "
       "more than any bonus is worth. Ten of the sixteen casinos here support NZD properly."),
      ("3. Who is the licensee, and can you verify it?",
       "Footer, licence number, regulator register. Cura&ccedil;ao Gaming Control Board with a named "
       "company is a reasonable floor. No number at all is a reason to cap your deposit at what you "
       "can afford to write off."),
      ("4. Are the games you actually play well covered?",
       "If you play Hacksaw and Nolimit pokies, lobby size is irrelevant &mdash; studio coverage is "
       "everything. If you play live blackjack, count the tables at 9am NZST, not at 9pm in Europe."),
      ("5. Only now, look at the bonus.",
       "And look at the wagering multiple, what it applies to, the game weighting and the maximum bet "
       "before you look at the headline number."),
    ])]
    body.append(section("\n".join(s)))

    s = [h2("What a real money casino NZ account actually gives you", "what-you-get"),
         cards([
      ("PK", "Online pokies", "Between 3,000 and 8,000 titles depending on the site. Pragmatic Play, "
       "Play&rsquo;n GO, Nolimit City, Hacksaw and Push are the studios worth checking for by name.",
       "/online-pokies/", "Online pokies NZ"),
      ("LV", "Live dealer", "Real dealers streamed from studios in Latvia, Malta and the Philippines. "
       "Blackjack, roulette, baccarat, plus game shows like Crazy Time and Lightning Roulette.",
       "/live-casino/", "Live casinos"),
      ("TB", "Table games", "RNG blackjack, roulette, baccarat, casino hold&rsquo;em and video poker. "
       "Lower house edge than pokies, and usually weighted at 10% or less towards bonus wagering.", None),
      ("CR", "Crash and instant win", "Aviator, Spaceman, Plinko, Mines and dice. The fastest-growing "
       "category since 2023, and Fortune Play carries the deepest range of it.",
       "/casino-reviews/fortune-play/", "Fortune Play review"),
      ("JP", "Jackpots", "Networked progressive pools from Pragmatic, Red Tiger and Microgaming. "
       "Kingdom has the widest jackpot coverage of the sites here.",
       "/casino-payout-percentages/", "High payout casinos"),
      ("SP", "Sports betting", "Seven of these sixteen run a sportsbook on the same wallet, covering "
       "NPC, Super Rugby, the ANZ Premiership, NRL and New Zealand racing.",
       "/online-betting/", "Online betting NZ"),
    ])]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Online casino real money NZ sites we tested and left out", "rejected"),
         "<p>We tested %d and list 16. Transparency about the other %d matters more than another "
         "recommendation, so here is what disqualified them. We do not name them individually because "
         "we are not in the business of publishing a blacklist we cannot defend legally &mdash; but the "
         "failure categories are worth knowing.</p>" % (N_OPERATORS_TESTED, N_OPERATORS_TESTED - 16),
         table(["Reason for exclusion", "Casinos affected", "What we saw"], [
      ["Withdrawal exceeded 7 days with no explanation", "11",
       "Requests sat in &lsquo;pending&rsquo; past the operator&rsquo;s own stated window with support "
       "unable to give a reason."],
      ["No verifiable licence", "8",
       "Licence badge present, no number, or a number that returned nothing on the regulator&rsquo;s register."],
      ["Bonus terms changed mid-claim", "4",
       "Wagering multiple or excluded-games list differed between the promotion page and the account terms."],
      ["Support unreachable", "4",
       "No response to three chat attempts across different time zones, or chat replaced by a ticket form."],
      ["Geo-blocked New Zealand during testing", "3",
       "Accepted registration, then blocked deposits or game launch from an NZ IP."],
    ], caption="Why %d tested casinos are not listed" % (N_OPERATORS_TESTED - 16))]
    body.append(section("\n".join(s)))

    s = [h2("Opening a top online casinos NZ account, step by step", "sign-up"),
         steps([
      ("Register with your real details",
       "Name exactly as it appears on your ID, real date of birth, real address. A mismatch found at "
       "verification is the most common cause of a frozen withdrawal, and it is always the player&rsquo;s "
       "fault in the terms."),
      ("Verify immediately &mdash; do not wait",
       "Upload passport or NZ driver licence, and a proof of address dated within three months. Median "
       "approval in our tests was 14 hours. Doing this on day one removes the delay from day thirty."),
      ("Set a deposit limit before your first deposit",
       "Account settings, daily or weekly, a number you would be comfortable losing. It takes 30 seconds "
       "and it is much harder to set honestly after a loss than before one."),
      ("Deposit on a rail you can also withdraw to",
       "Neosurf and Paysafecard are deposit-only. If you fund with a voucher you will need a second "
       "verified method to cash out, and setting that up mid-withdrawal adds days."),
      ("Read the bonus terms, then decide",
       "Wagering multiple, what it applies to, game weighting, maximum bet, expiry. If any of the five "
       "does not suit how you play, decline the bonus &mdash; you can always claim a reload later."),
      ("Withdraw something small early",
       "A NZ$50 test withdrawal in your first week tells you more about a casino than any review, "
       "including ours."),
    ])]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [faq(FAQ, "Online casinos NZ &mdash; frequently asked questions", "faq"),
         authorbox("jordan-whitcombe"),
         ctaband("Looking for something more specific?",
                 "We maintain separate ranked lists for pokies, live dealer, fast payouts, crypto, "
                 "no-deposit offers and new arrivals.",
                 [("Online pokies", "/online-pokies/"), ("Fast payouts", "/fast-payout-casinos/"),
                  ("Crypto casinos", "/crypto-casinos-nz/"), ("New casinos", "/new-casinos-nz/")])]
    body.append(section("\n".join(s)))

    trail = [("Home", "/"), ("Online casinos", path)]
    schema = [lib.article_schema(path, "Best Online Casinos NZ", "Every online casino tested for New "
                                "Zealand players, ranked.", "jordan-whitcombe", "priya-raman", "Online casinos"),
              lib.breadcrumb_schema(path, trail),
              lib.itemlist_schema(path, ops, "casino", "Best online casinos NZ %s" % MONTH_YEAR),
              lib.faq_schema(path, FAQ)]
    lib.write(path, lib.seo_title(path),
              "Every online casino we tested for NZ players, ranked 1 to 16 on verified payout speed, "
              "NZD banking, clearable bonuses and licence disclosure. Updated %s." % MONTH_YEAR,
              "\n".join(body), schema, prio=0.95, freq="daily")


def build_bonuses():
    path = "/casino-bonus/"
    order = ["smash", "kingdom", "crownslots", "spinjo", "rooster-bet", "fortune-play",
             "rivo", "lucky-circus", "lucky7even", "spino", "roby-casino", "ivibet"]
    ops = [lib.BY[s] for s in order]
    notes = {
     "smash": "600% to NZ$19,500 at 10x deposit + bonus &mdash; the lowest real turnover of any large offer.",
     "kingdom": "600% to NZ$18,500 at 30x, staged over four deposits, with a NZ$10,000 weekly cap behind it.",
     "crownslots": "390% &mdash; the biggest percentage &mdash; but 40x makes it a NZ$15,600 turnover on NZ$100.",
     "spinjo": "NZ$5,000 + 300 spins at 40x over four deposits, on the best all-round casino here.",
     "rooster-bet": "NZ$5,000 + 300 spins at 40x, plus a separate NZ$350 sports free bet at 6x.",
     "fortune-play": "NZ$5,000 + 300 spins at 40x, and bonus-buy titles count towards wagering.",
     "rivo": "NZ$4,500 + 250 spins at 35x &mdash; below-market wagering on a mid-size package.",
     "lucky-circus": "NZ$2,500 + 150 spins at 35x with a NZ$10 minimum deposit. Best small-stakes offer.",
     "lucky7even": "20 no-deposit spins first, then 100% to NZ$1,700. 50x applies to spin winnings.",
     "spino": "Up to 2,000 USDT at <b>0x wagering</b>. Withdraw winnings immediately. Crypto only.",
     "roby-casino": "250% to NZ$5,000 at 45x &mdash; the highest multiple here, on an unlicensed-looking site.",
     "ivibet": "100% to NZ$500 at 35x on one deposit. Small, honest, finishable in a fortnight.",
    }

    turn_rows = []
    for o in ops:
        w = o["wagering"]
        dep = o["min_deposit"]
        turn_rows.append([op_cell(o), lib.bonus_for(o), w, dep,
                          o.get("casino_bonus_terms") or "&mdash;"])

    body = []
    body.append(hero(
      "Every welcome offer, with the real turnover &middot; %s" % MONTH_YEAR,
      lib.seo_h1(path),
      "Twelve welcome offers, ranked by what they are actually worth rather than by the number on the "
      "banner. Every entry shows the wagering multiple, what that multiple applies to, and the turnover "
      "a NZ$100 deposit really generates.",
      stats=[("10x", "Lowest wagering: Smash"), ("0x", "Spino, crypto only"),
             ("NZ$19,500", "Largest headline"), ("20", "No-deposit spins available")],
      ctas=[("See the offers", "#ranked"), ("Turnover calculator", "#turnover")],
      meta=([("Home", "/"), ("Online casinos", "/online-casinos/"),
             ("Bonuses", None)], "jordan-whitcombe", "priya-raman"),
      offer=lib.hero_offer(ops[0], "casino",
                           "Biggest clearable bonus &middot; %s" % MONTH_YEAR)))

    s = [DISCLOSURE]
    s.append("<p>An online casino bonus New Zealand players are offered is a turnover contract. The "
             "operator advances you balance; you agree to recycle it a set number of times before any "
             "of it is yours. Every other detail &mdash; the "
             "percentage, the free spin count, the tier structure &mdash; is presentation. This page "
             "ranks New Zealand casino bonuses on the contract, not the banner.</p>")
    s.append(toc([("Best casino bonuses NZ, ranked", "ranked"),
                  ("What NZ$100 really costs you in turnover", "turnover"),
                  ("Bonus types explained", "types"),
                  ("The five terms that decide everything", "terms"),
                  ("Every offer and its conditions", "all-offers"),
                  ("Mistakes that void a bonus", "mistakes"),
                  ("Frequently asked questions", "faq")]))
    _intro = section("\n".join(s), cls="ord-intro")

    s = [h2("Best casino bonuses NZ &mdash; %s" % MONTH_YEAR, "ranked"),
         '<p class="rank-note">Every welcome bonus casino NZ players can claim here, ranked on '
         'clearable value: the headline amount discounted by the turnover needed to release it, the '
         'game weighting, the maximum bet and the expiry window.</p>',
         leaderboard(ops, "casino", notes, top_n=1, cta="Claim offer")]
    body.append(section("\n".join(s), cls="ord-lb"))
    body.append(_intro)

    s = [h2("What a NZ$100 deposit really costs you in turnover", "turnover"),
         "<p>Same deposit, seven different contracts. The turnover column is what you must bet before "
         "the balance is withdrawable; the expected-cost column is roughly what generating that "
         "turnover costs at a typical 4% pokies house edge.</p>",
         table(["Offer", "Rule", "Bonus on NZ$100", "Turnover required", "Expected cost to clear", "Verdict"], [
      ["Spino (crypto)", "0x", "&asymp;NZ$100", "<b>Nil</b>", "NZ$0", "Withdraw immediately"],
      ["Smash", "10x deposit + bonus", "NZ$100", "<b>NZ$2,000</b>", "&asymp;NZ$80", "Genuinely clearable"],
      ["Rivo", "35x bonus", "NZ$100", "<b>NZ$3,500</b>", "&asymp;NZ$140", "Reasonable"],
      ["Lucky Circus", "35x bonus", "NZ$100", "<b>NZ$3,500</b>", "&asymp;NZ$140", "Reasonable, NZ$10 entry"],
      ["Spinjo", "40x bonus", "NZ$100", "<b>NZ$4,000</b>", "&asymp;NZ$160", "Market standard"],
      ["Kingdom", "30x bonus", "NZ$100", "<b>NZ$9,000</b>", "&asymp;NZ$360", "Large match, large turnover"],
      ["Roby Casino", "45x bonus", "NZ$100", "<b>NZ$11,250</b>", "&asymp;NZ$450", "Avoid"],
      ["CrownSlots", "40x bonus", "NZ$100", "<b>NZ$15,600</b>", "&asymp;NZ$624", "Decorative, not clearable"],
    ], caption="Turnover required to release a welcome bonus on a NZ$100 deposit"),
      note("<b>This is the whole argument in one table.</b> CrownSlots gives you NZ$390 of bonus and "
           "asks NZ$15,600 of turnover. Smash gives you NZ$100 and asks NZ$2,000. The second offer is "
           "worth more to almost every real player, and it is advertised with a smaller number.", "ok")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Casino sign up bonus NZ offers, by deposit size", "by-deposit"),
         "<p>Most welcome offers quote a maximum almost nobody reaches. The more useful question is "
         "what an ordinary first deposit actually buys, so here is every casino sign up bonus NZ "
         "players can claim on this page, sized to real deposits.</p>",
         table(["Your deposit", "Best offer at that level", "What you get", "Turnover to clear",
                "Where it sits"], [
      ["<b>NZ$10</b>", "Lucky Circus", "100% match + spins at 35x", "NZ$350",
       "The closest thing to a $1 deposit casino NZ players will find &mdash; see the note below"],
      ["<b>NZ$20</b>", "Smash", "100% match at 10x deposit + bonus", "<b>NZ$400</b>",
       "Best value per dollar risked on this site"],
      ["<b>NZ$20</b>", "Ivibet", "100% up to NZ$500 at 35x", "NZ$700", "Best if you want live tables"],
      ["<b>NZ$25</b>", "Rivo", "Part one of NZ$4,500 at 35x", "NZ$875", "Below-market wagering"],
      ["<b>NZ$30</b>", "Spinjo", "Part one of NZ$5,000 at 40x", "NZ$1,200", "Best all-round casino"],
      ["<b>NZ$50</b>", "Kingdom", "Part one of 600% at 30x", "NZ$4,500", "Fastest payouts behind it"],
      ["<b>NZ$100+</b>", "Smash", "600% staged to NZ$19,500 at 10x", "NZ$2,000 on the first part",
       "Only large package designed to be finished"],
     ], caption="Casino sign up bonus NZ offers sized to a realistic first deposit"),
         note("<b>On $1, $5 and $10 deposit casinos.</b> A $1 deposit casino NZ players can genuinely "
              "use does not exist in this market, and neither does a $5 deposit casino NZ offer &mdash; "
              "the 1 dollar deposit casino NZ pages you will find are almost all recycled from other "
              "markets or from operators that no longer accept New Zealand registrations. A $10 deposit "
              "casino NZ offer is real: Lucky Circus takes NZ$10 at 35x. Everything else here starts at "
              "NZ$20. We would rather tell you the floor than pretend it is lower. If you want a $1 "
              "deposit casino NZ free spins equivalent at zero cost, the "
              "<a href=\"/no-deposit-bonus/\">no deposit offer</a> is the honest answer.", "warn"),
         h3("What does 35x wagering mean, and how do casino wagering requirements work?", "wagering-meaning"),
         "<p>Multiply the bonus by the number. What does 35x wagering mean on a NZ$100 bonus? NZ$3,500 "
         "of bets placed before the balance is withdrawable. How casino wagering requirements work in "
         "practice adds three wrinkles that change the answer: whether the multiple applies to the "
         "bonus alone or to deposit plus bonus, how each game is weighted, and how long you have.</p>",
         table(["Term on the page", "What it means in money", "On a NZ$100 bonus"], [
      ["35x bonus", "Bet 35 &times; the bonus", "NZ$3,500 of turnover"],
      ["35x deposit + bonus", "Bet 35 &times; both", "<b>NZ$7,000</b> of turnover"],
      ["10x deposit + bonus", "Bet 10 &times; both", "<b>NZ$2,000</b> of turnover"],
      ["Pokies 100%, live 10%", "Live bets count a tenth", "35x becomes an effective 350x on live"],
      ["Max bet NZ$5 while wagering", "One larger spin voids it", "Bonus and winnings forfeited"],
      ["7-day expiry", "Unmet turnover is lost", "Forces a stake size that burns the balance"],
     ], caption="Reading a wagering requirement, translated"),
         h3("Low wagering, no wagering, reload and cashback", "other-types"),
         "<p>Beyond the welcome offer, four recurring promotions are worth knowing, because two of them "
         "are where the real long-run value hides.</p>",
         "<ul>"
         "<li><b>A no wagering casino bonus NZ side is almost always crypto.</b> Spino&rsquo;s offer is "
         "0x &mdash; winnings withdrawable immediately &mdash; and it is the only genuine example on "
         "this site. Check the maximum cash-out, which is where the limit moves to instead.</li>"
         "<li><b>A low wagering bonus NZ players can actually finish</b> means 35x or below, or 10x on "
         "deposit plus bonus. Smash, Rivo and Lucky Circus are the three here.</li>"
         "<li><b>A reload bonus casino NZ operators run</b> is a smaller match on later deposits, "
         "usually on a fixed weekday and usually at the same multiple as the welcome offer.</li>"
         "<li><b>Cashback casino bonus NZ terms vary enormously</b>, and this is the one worth reading "
         "closely: Lucky Vibe credits cashback as withdrawable cash with no turnover, while most "
         "operators credit it as bonus funds carrying a fresh 30&ndash;40x. Identical headline "
         "percentage, completely different product.</li></ul>",
         "<p>Casino bonus codes NZ players need are rare at these operators &mdash; almost every offer "
         "on this page credits automatically on deposit, and where a code is required it is shown in "
         "the listing. Treat any page advertising a long list of codes with suspicion; most are "
         "expired or were never valid for New Zealand.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Bonus types explained", "types"),
         cards([
      ("01", "Match bonus", "The operator matches a percentage of your deposit in bonus funds. The "
       "headline product. Judge it by the multiple, not the percentage.", None),
      ("02", "Free spins", "A fixed number of spins on named titles at a fixed stake. Watch for a "
       "separate, higher wagering multiple on the winnings and a maximum cash-out.", None),
      ("03", "No deposit bonus", "Credited for registering, with no funding required. We keep this "
       "one on its own page because the terms work differently &mdash; higher wagering, a cash-out "
       "cap and a fixed stake.", "/no-deposit-bonus/", "No deposit bonus NZ"),
      ("04", "Cashback", "A percentage of net losses returned, weekly or monthly. The critical "
       "question is whether it credits as cash (Lucky Vibe) or as bonus with fresh wagering (most).", None),
      ("05", "Reload bonus", "A smaller match on subsequent deposits, usually on a fixed weekday. "
       "Normally carries the same multiple as the welcome offer.", None),
      ("06", "Zero-wagering offer", "Winnings are withdrawable immediately. Almost always crypto-only "
       "and capped. Spino is the one on this site.",
       "/crypto-casinos-nz/", "Crypto casinos"),
    ])]
    body.append(section("\n".join(s)))

    s = [h2("The five terms that decide whether a bonus is worth taking", "terms"),
         pros_cons(
      ["A multiple of 35x or less applied to the bonus only",
       "Pokies weighted at 100% and a published list of excluded titles",
       "A maximum bet of NZ$8 or more while wagering",
       "At least 30 days to complete the requirement",
       "A weekly withdrawal cap comfortably above the maximum bonus"],
      ["A multiple applied to deposit plus bonus at 35x or higher",
       "Live and table games weighted at 0&ndash;10% when those are what you play",
       "A maximum bet of NZ$5 with automatic forfeiture for a single breach",
       "A seven-day expiry on a four-figure requirement",
       "A maximum cash-out on winnings from a deposited bonus, not just a free-spin bonus"],
      "Terms worth accepting", "Terms to walk away from"),
      h3("Where the money actually leaks", "leaks"),
      "<p>Three places, in order of size. First, game weighting &mdash; a 40x requirement at 10% "
      "contribution is an effective 400x, which no one clears. Second, maximum-bet breaches, which void "
      "the whole bonus and are enforced by automated systems that do not care that it was accidental. "
      "Third, expiry, because a 40x requirement on a seven-day clock forces a stake size that burns the "
      "balance before the turnover is met.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Every welcome offer and its conditions", "all-offers"),
         table(["Casino", "Welcome offer", "Wagering", "Min deposit", "Structure"], turn_rows,
               caption="Casino welcome bonuses available to New Zealand players, %s" % MONTH_YEAR)]
    body.append(section("\n".join(s)))

    s = [h2("Mistakes that void a bonus", "mistakes"),
         "<ul>"
         "<li><b>Betting above the maximum stake once.</b> The most common cause by a distance. Set your "
         "stake below the cap and leave it there for the whole wagering period.</li>"
         "<li><b>Withdrawing while a bonus is active.</b> At most operators this forfeits the bonus and "
         "everything won from it, even if your cash balance is separate.</li>"
         "<li><b>Playing an excluded game.</b> Excluded lists are long and change. Check the list on the "
         "day you claim, not the day you read a review.</li>"
         "<li><b>Opening a second account.</b> Instant forfeiture everywhere, plus likely closure of "
         "both accounts and confiscation of the balance.</li>"
         "<li><b>Depositing with a method in someone else&rsquo;s name.</b> A partner&rsquo;s card is "
         "third-party payment and will fail verification.</li>"
         "<li><b>Letting it expire.</b> Bonus funds and free spins both expire, usually separately and "
         "on different clocks.</li></ul>",
         faq(BONUS_FAQ, "Casino bonus questions", "faq"),
         authorbox("jordan-whitcombe")]
    body.append(section("\n".join(s), cls="sec--sur"))

    trail = [("Home", "/"), ("Online casinos", "/online-casinos/"), ("Bonuses", path)]
    schema = [lib.article_schema(path, "Online Casino Bonuses NZ", "Casino welcome bonuses for NZ "
                                 "players, ranked by clearable value.", "jordan-whitcombe", "priya-raman",
                                 "Casino bonuses"),
              lib.breadcrumb_schema(path, trail),
              lib.itemlist_schema(path, ops, "casino", "Best casino bonuses NZ %s" % MONTH_YEAR),
              lib.faq_schema(path, BONUS_FAQ)]
    lib.write(path, lib.seo_title(path),
              "NZ casino bonuses ranked by real value, not headline size. Wagering multiples, turnover "
              "on a NZ$100 deposit, game weighting and the terms that void an offer.",
              "\n".join(body), schema, prio=0.9, freq="weekly")


def build():
    build_hub()
    build_bonuses()
