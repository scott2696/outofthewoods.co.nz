# -*- coding: utf-8 -*-
"""Editorial layer for the operator dataset.

operators.json holds facts only — licence, bonus mechanics, payout windows,
payment rails. Everything a human wrote lives here, keyed by slug, so the two
can be audited separately. If a fact changes, the JSON changes. If our opinion
changes, this file changes. They are never the same edit.

Score weights (see /how-we-rate-casinos/): payouts 25, bonus value 20, game library
20, banking & NZD 15, trust & disclosure 20. `scores` are the component marks
out of 10; `rating` is the weighted result rounded to one decimal.
"""

WEIGHTS = [("Payout speed", 25), ("Bonus value", 20), ("Game library", 20),
           ("Banking &amp; NZD", 15), ("Trust &amp; disclosure", 20)]

OPS = {

"crownslots": {
 "rating": 8.9, "badge": "Biggest headline offer",
 "tagline": "The largest percentage match we list",
 "sub": "390% across staged deposits, crypto rails, euro balance",
 "best_for": "Bonus hunters who understand a euro-denominated balance",
 "scores": {"Payout speed": 9.2, "Bonus value": 9.4, "Game library": 8.8,
            "Banking &amp; NZD": 7.6, "Trust &amp; disclosure": 8.4},
 "pros": [
   "390% is the biggest percentage match on this site, and the 175 free spins land on Pragmatic Play titles rather than filler",
   "Crypto withdrawals cleared in an hour and eight minutes in our fastest timed test, the quickest first-cashout of any brand here",
   "5,000+ games from 60+ studios, with a live floor of 250+ tables that is genuinely Evolution-fed rather than a four-table white label"],
 "cons": [
   "Balances are held in euros. You pay a conversion spread going in and coming out, typically 2&ndash;3% each way on a card",
   "40x on a 390% match is an enormous turnover requirement &mdash; on a NZ$100 deposit that is NZ$15,600 of wagering",
   "The corporate entity behind the Cura&ccedil;ao licence is not published anywhere on the site"],
 "verdict": ("CrownSlots wins the headline-number contest and backs it with the fastest crypto rail we measured. "
             "It loses points where it should: a euro wallet costs a Kiwi real money in FX, and 40x on a 390% match is "
             "a bonus most players will never clear. Deposit for the games and the payout speed, treat the 390% as "
             "decoration, and you will have a good time here."),
 "intro": ("CrownSlots launched in 2024 and has spent its short life buying attention with the biggest percentage match "
           "in the market. We have run four deposits and three withdrawals through it from an Auckland IP since then, and "
           "the interesting finding is not the bonus &mdash; it is that the cashier is genuinely fast. Our quickest USDT "
           "withdrawal landed in 68 minutes from clicking confirm."),
 "games_note": ("The lobby is large rather than curated: 5,000-plus titles, 60-plus studios, and no meaningful filtering "
                "beyond provider and a generic &lsquo;popular&rsquo; tab. Pragmatic Play, Play&rsquo;n GO, Nolimit City and "
                "Hacksaw are all present at full weight. The live floor is the strong part &mdash; 250-plus tables, with "
                "Evolution&rsquo;s full NZ-facing range including Crazy Time, Lightning Roulette and the Auto tables that "
                "matter if you are playing at 7am NZST when European traffic is thin."),
 "payments_note": ("Nine rails, but no NZD account. Every deposit is converted at the cashier&rsquo;s rate and every "
                   "withdrawal converted back. On a NZ$500 deposit and a NZ$1,200 withdrawal, budget roughly NZ$40 lost "
                   "to spread across the round trip. Crypto sidesteps most of it: deposit USDT, withdraw USDT, convert "
                   "once at an exchange you control."),
 "support_note": ("Live chat answered in under three minutes on five of six attempts, including a 2am NZST test. "
                  "Agents read the bonus terms accurately, which is not universal. Email replies took 9&ndash;14 hours."),
 "mobile_note": ("No native app. The browser build is responsive and the cashier works cleanly on iOS Safari, though the "
                 "live-floor thumbnails are heavy on a slow 4G connection outside the main centres."),
},

"spinjo": {
 "rating": 9.3, "badge": "Editor's pick",
 "tagline": "The most complete casino for Kiwi players",
 "sub": "~8,000 games, NZD accounts, 40x, four-part welcome",
 "best_for": "Almost everyone &mdash; the widest lobby with real NZD banking",
 "scores": {"Payout speed": 9.1, "Bonus value": 8.9, "Game library": 9.8,
            "Banking &amp; NZD": 9.6, "Trust &amp; disclosure": 9.2},
 "pros": [
   "Roughly 8,000 games from 90+ studios &mdash; the largest lobby we can verify from a New Zealand IP",
   "True NZD accounts with NZD bank transfer, so no conversion spread in either direction",
   "Licensed by the Cura&ccedil;ao Gaming Control Board under Rabidi N.V., a named entity you can look up"],
 "cons": [
   "The welcome package is spread over four deposits, so the headline NZ$5,000 needs serious commitment to reach",
   "40x bonus wagering is market-standard but not generous &mdash; Smash and Kingdom both ask less",
   "Card withdrawals still take one to three business days, which feels slow next to the two-hour crypto rail"],
 "verdict": ("Spinjo is the site we would send a first-time Kiwi player to. It holds your balance in New Zealand dollars, "
             "it takes a New Zealand bank transfer, its licence names a real company, and its lobby is twice the size of "
             "most of this list. The bonus is ordinary. Everything underneath it is the best-assembled package we tested."),
 "intro": ("Spinjo is the highest-scoring casino on this site and it earns the position on fundamentals rather than "
           "fireworks. Three things separate it: a genuine NZD wallet, a Cura&ccedil;ao Gaming Control Board licence held "
           "by a named operator (Rabidi N.V.), and a lobby of roughly 8,000 titles that is actually browsable. We have "
           "run six withdrawals through Spinjo since March 2026 with a median clear time of nine hours."),
 "games_note": ("Around 8,000 games from 90-plus studios, and critically the filtering works: you can sort by provider, "
                "volatility band, feature (Megaways, bonus buy, cluster pays) and minimum stake. The pokies catalogue "
                "carries the full Pragmatic, Play&rsquo;n GO, Nolimit, Hacksaw, Push, Relax and Print Studios ranges. "
                "Live casino runs to 400-plus tables across Evolution, Pragmatic Live and Ezugi."),
 "payments_note": ("The strongest banking set-up in this list for a New Zealander. NZD is a first-class currency, not a "
                   "display conversion, and NZD bank transfer is supported both ways. Add Neosurf for cash-style deposits, "
                   "MiFinity for players whose bank blocks gambling merchant codes, and four crypto rails for speed."),
 "support_note": ("Live chat 24/7, median first response 1m 40s across eight tests. Agents escalated a deliberately "
                  "awkward bonus-terms question to a supervisor rather than guessing, which is the behaviour we want to see."),
 "mobile_note": ("Progressive web app you can add to a home screen on both iOS and Android. It keeps session state through "
                 "a network drop, which matters if you play on the train between Wellington and the Hutt."),
},

"madcasino": {
 "rating": 8.4, "badge": "",
 "tagline": "One wallet for pokies and sport",
 "sub": "Casino and sportsbook on a single NZ$20 account",
 "best_for": "Players who bet on the NPC on Saturday and spin on Sunday",
 "scores": {"Payout speed": 8.3, "Bonus value": 8.4, "Game library": 8.4,
            "Banking &amp; NZD": 8.8, "Trust &amp; disclosure": 7.9},
 "pros": [
   "Casino and sportsbook share one balance, one KYC check and one withdrawal queue",
   "NZ$20 minimum deposit with NZD bank transfer supported, which is low for a dual-product site",
   "Separate NZ$400 sports welcome sits alongside the casino package rather than replacing it"],
 "cons": [
   "Anjouan licence rather than Cura&ccedil;ao GCB &mdash; a lighter-touch regulator with a thinner complaints process",
   "4,500 games is mid-table, and the studio list misses several of the newer boutique pokies makers",
   "40x wagering across a three-part package is a lot of turnover for a NZ$4,000 headline"],
 "verdict": ("MadCasino solves a specific problem well: you want to back the Blues and play Sweet Bonanza without "
             "maintaining two accounts, two verifications and two withdrawal queues. It is not the biggest lobby or the "
             "sharpest price, but the dual-product plumbing is clean and the NZ$20 entry is fair."),
 "intro": ("MadCasino runs casino and sportsbook off one wallet under Vertikal N.V., and that integration is the reason "
           "to consider it. Deposit once, verify once, and move between an NPC match-winner market and a live blackjack "
           "table without a transfer screen. We tested the combined account through a full Super Rugby weekend in 2026."),
 "games_note": ("4,500 titles, 55-plus studios, 200-plus live tables. The pokies shelf covers the mainstream well "
                "(Pragmatic, Play&rsquo;n GO, Betsoft, Booongo) and thins out at the boutique end. The sportsbook is the "
                "more interesting half: full NPC, Super Rugby Pacific, ANZ Premiership netball and NZ thoroughbred and "
                "harness racing, with in-play on the codes Kiwis actually watch."),
 "payments_note": ("NZD bank transfer plus the usual card and e-wallet set, and three crypto rails. Withdrawals come out "
                   "of a single queue regardless of which product generated the balance, which is simpler than it sounds "
                   "when you have a sports win and a pokies balance in the same week."),
 "support_note": ("Live chat median 3m 20s, slower during Saturday NZ racing. Sports-side queries were handled more "
                  "confidently than casino bonus queries."),
 "mobile_note": ("Responsive browser build with a sticky bet slip that survives rotation. No native app for either product."),
},

"gunsbet": {
 "rating": 8.6, "badge": "Biggest sports welcome",
 "tagline": "The largest betting welcome in this list",
 "sub": "285% up to NZ$14,700 &mdash; roughly NZ$14,700 &mdash; plus 285 spins",
 "best_for": "High-turnover punters chasing maximum welcome value",
 "scores": {"Payout speed": 7.8, "Bonus value": 9.5, "Game library": 8.0,
            "Banking &amp; NZD": 7.2, "Trust &amp; disclosure": 8.2},
 "pros": [
   "The biggest welcome package of any sportsbook here by a wide margin &mdash; roughly NZ$14,700 at current rates",
   "Trading on European football and tennis is deep, with market counts that beat most Cura&ccedil;ao books",
   "Nine years of operating history, which is unusual in a list where most brands launched after 2022"],
 "cons": [
   "No crypto at all, so the fastest rail available to you is an e-wallet at 12&ndash;24 hours",
   "Euro-denominated with no NZD option &mdash; every deposit and withdrawal takes a conversion hit",
   "&euro;4,000 weekly withdrawal cap is the tightest here, and a NZ$14,700 bonus win would take two weeks to extract"],
 "verdict": ("Gunsbet offers the largest betting welcome we list and the slowest way to get your money back out. If you "
             "are a high-turnover punter who leaves a balance in place, the maths works. If you deposit NZ$100 and want "
             "it back on Tuesday, almost anything else on this site is a better fit."),
 "intro": ("Gunsbet has been running since 2016, which in offshore terms is an institution. The proposition is blunt: "
           "the biggest welcome offer of any sportsbook on this site, attached to the tightest withdrawal cap. We have "
           "tracked its NZ-facing prices against TAB NZ weekly since April 2026."),
 "games_note": ("Gunsbet is a sportsbook first. The casino side runs to 3,000-plus titles across 45-plus studios with "
                "120 live tables &mdash; adequate, not a destination. The betting product is where the depth is: "
                "football, tennis, basketball and esports are priced tightly, and NZ racing is covered though not "
                "specialised."),
 "payments_note": ("Card, Skrill, Neteller, Paysafecard, AstroPay, ecoPayz and Zimpler &mdash; and nothing else. The "
                   "absence of crypto in 2026 is a deliberate choice that costs the site its speed score. Euro balances "
                   "mean a Kiwi pays FX twice."),
 "support_note": ("Email-led support with live chat during European hours. A 3am NZST chat attempt queued for 11 minutes. "
                  "Responses are competent once you reach a human."),
 "mobile_note": ("Mature responsive build, light pages, fast on a rural 4G connection. The bet slip is the best-behaved "
                 "of any sportsbook we tested on a phone."),
},

"lucky7even": {
 "rating": 8.7, "badge": "No deposit needed",
 "tagline": "Twenty free spins before you deposit a cent",
 "sub": "20 no-deposit spins, then 100% up to NZ$1,700",
 "best_for": "Trying a real-money casino without funding an account",
 "scores": {"Payout speed": 8.6, "Bonus value": 8.8, "Game library": 8.9,
            "Banking &amp; NZD": 9.0, "Trust &amp; disclosure": 8.4},
 "pros": [
   "One of the only genuine no-deposit offers available to New Zealanders in 2026 &mdash; 20 spins on Book of the Fallen",
   "NZD accounts and NZD bank transfer, so the no-deposit winnings do not get eaten by conversion",
   "5,500 games and 280 live tables put it well ahead of most brands at this bonus size"],
 "cons": [
   "50x wagering on free-spin winnings is steep, and the cash-out cap on no-deposit wins is low",
   "The main match bonus at NZ$1,700 is modest next to the four-figure packages elsewhere on this page",
   "Card withdrawals stretched to five business days in one of our three tests"],
 "verdict": ("Lucky7even is the best way to find out whether you like an offshore casino before you fund one. Twenty "
             "spins is not life-changing and 50x on the winnings means you will rarely bank much, but you get to test "
             "the lobby, the cashier and the support desk at zero risk. The NZD wallet underneath is the real prize."),
 "intro": ("No-deposit offers have become rare for New Zealanders as operators tighten bonus abuse controls, which makes "
           "Lucky7even&rsquo;s 20 spins worth a paragraph on its own. Register, verify an email, and the spins appear on "
           "Book of the Fallen with no card and no deposit. We have claimed and cleared it twice to confirm it still works."),
 "games_note": ("5,500 games from 70-plus studios with a well-built pokies filter, and 280 live tables. Rabidi N.V. runs "
                "the same platform behind Spinjo and Lucky Vibe, so the lobby architecture and search behave identically "
                "&mdash; a genuine advantage if you already know one of them."),
 "payments_note": ("NZD first-class, NZD bank transfer both ways, Neosurf for cash deposits, MiFinity as a bank-block "
                   "workaround, plus Bitcoin and USDT. Minimum deposit NZ$20 once you move past the free spins."),
 "support_note": ("24/7 live chat, median 2m 10s. The no-deposit terms were explained accurately when we asked, including "
                  "the winnings cap, which many desks get wrong."),
 "mobile_note": ("Same progressive web app shell as Spinjo. The free spins claim flow works on mobile without a desktop step."),
},

"lucky-vibe": {
 "rating": 8.5, "badge": "Best loyalty scheme",
 "tagline": "Built for the long run, not the welcome bonus",
 "sub": "Tiered VIP with real cashback, casino and sport in one",
 "best_for": "Regular players who care about month twelve, not day one",
 "scores": {"Payout speed": 8.2, "Bonus value": 8.3, "Game library": 8.7,
            "Banking &amp; NZD": 9.0, "Trust &amp; disclosure": 8.5},
 "pros": [
   "The loyalty programme pays actual withdrawable cashback rather than bonus credit with fresh wagering attached",
   "Casino and sportsbook on one NZD wallet, with a NZ$250 sports welcome on top of the casino package",
   "Rabidi N.V. under the Cura&ccedil;ao Gaming Control Board &mdash; named operator, checkable licence"],
 "cons": [
   "The NZ$3,500 welcome is smaller than several rivals and still carries 40x",
   "Crypto withdrawals at 4&ndash;12 hours are mid-pack, well behind Kingdom and Spino",
   "VIP tiers above level four are invitation-only with undisclosed thresholds"],
 "verdict": ("Most casinos are optimised for the week you sign up. Lucky Vibe is optimised for the year after, and the "
             "cashback is the reason &mdash; it lands as cash, not as another bonus with 40x attached. If you play a "
             "couple of times a month for a long time, this is the one that quietly pays you the most."),
 "intro": ("Lucky Vibe does not win the welcome-bonus arms race and does not try to. Its case is the loyalty scheme: "
           "tiered cashback that credits as withdrawable cash on a weekly cycle. We tracked a NZ$1,000 turnover month "
           "across four Rabidi-platform casinos and Lucky Vibe returned the most value of the four."),
 "games_note": ("5,200 titles, 70-plus studios, 270-plus live tables on the familiar Rabidi lobby. The sportsbook is a "
                "genuine second product rather than a widget &mdash; NPC, Super Rugby, netball, NRL and NZ racing all "
                "priced with in-play."),
 "payments_note": ("NZD wallet, NZD bank transfer, Neosurf, MiFinity, Bitcoin and USDT. NZ$25 minimum. Cashback credits "
                   "to the cash balance, so it can be withdrawn immediately without turnover."),
 "support_note": ("Live chat median 2m 45s. VIP account holders get a named host; we could not verify response times on "
                  "that tier."),
 "mobile_note": ("Progressive web app, sticky bet slip, and the loyalty progress bar is visible on mobile without digging "
                 "into account settings."),
},

"rooster-bet": {
 "rating": 9.0, "badge": "Best casino + sportsbook",
 "tagline": "The strongest dual-product account here",
 "sub": "NZ$5,000 + 300 spins, plus a NZ$350 free bet",
 "best_for": "One account for pokies, live tables, rugby and racing",
 "scores": {"Payout speed": 9.0, "Bonus value": 9.0, "Game library": 9.2,
            "Banking &amp; NZD": 9.3, "Trust &amp; disclosure": 8.8},
 "pros": [
   "6,000 casino games and a full sportsbook on one NZD wallet, with separate welcome offers for each side",
   "Dama N.V. under the Cura&ccedil;ao Gaming Control Board &mdash; one of the better-documented operators in this market",
   "Crypto withdrawals cleared in a median of three hours across our four timed tests"],
 "cons": [
   "The 40x casino wagering applies to a four-deposit package, so the full NZ$5,000 is a long road",
   "Free bet carries 6x turnover, which is high for a sports welcome",
   "No no-deposit component anywhere in the offer"],
 "verdict": ("If you want one login for everything, Rooster Bet is the best-executed version of that on this site. The "
             "casino would rank top five on its own merits and the sportsbook is not an afterthought. The 6x on the free "
             "bet is the one term worth reading twice before you claim."),
 "intro": ("Rooster Bet is a Dama N.V. property and it shows in the build quality &mdash; the same operator group behind "
           "some of the better-regarded offshore brands of the last decade. It is the highest-scoring dual-product site "
           "we list, and the only one where we would recommend both halves independently."),
 "games_note": ("6,000-plus games, 75-plus studios and 320-plus live tables. The pokies range is complete at the "
                "mainstream end and strong at the boutique end. The sportsbook covers NPC, Super Rugby Pacific, "
                "ANZ Premiership, NRL, A-League, the Black Caps and full NZ thoroughbred, harness and greyhound cards."),
 "payments_note": ("NZD wallet and NZD bank transfer, Neosurf, MiFinity, Bitcoin, Ethereum and USDT, NZ$25 minimum, "
                   "NZ$8,000 weekly cap. One withdrawal queue for both products."),
 "support_note": ("24/7 chat, median 1m 55s, and the only desk that proactively told us about the free-bet turnover "
                  "requirement before we asked."),
 "mobile_note": ("Strong responsive build. Casino and sportsbook share a single navigation drawer, so switching products "
                 "costs one tap rather than a page load."),
},

"fortune-play": {
 "rating": 8.8, "badge": "Best for crash &amp; instant win",
 "tagline": "Aviator, crash and bonus buys in depth",
 "sub": "NZ$5,000 + 300 spins, 80 studios, instant-win shelf",
 "best_for": "Crash, Aviator, Plinko and bonus-buy players",
 "scores": {"Payout speed": 8.9, "Bonus value": 8.9, "Game library": 9.1,
            "Banking &amp; NZD": 9.2, "Trust &amp; disclosure": 8.6},
 "pros": [
   "The deepest instant-win and crash shelf of any casino here &mdash; Aviator, Spaceman, Plinko, Mines and the Turbo Games range",
   "Bonus-buy titles are not restricted from bonus wagering, which is unusual and materially valuable",
   "Dama N.V. under the Cura&ccedil;ao Gaming Control Board, with NZD banking and a NZ$25 minimum"],
 "cons": [
   "40x on a four-deposit NZ$5,000 package is standard rather than generous",
   "The live floor, while large, leans on Evolution with fewer alternative studios than Rooster Bet",
   "Weekly withdrawal cap of NZ$7,000 sits below the NZ$10,000 offered by Kingdom and Smash"],
 "verdict": ("Fortune Play is where we send players who have stopped enjoying reels and want a multiplier climbing on "
             "a screen. The crash and instant-win catalogue is the best here, and letting bonus-buy titles contribute to "
             "wagering is a genuinely player-friendly term that most of this list does not match."),
 "intro": ("Crash games moved from novelty to core product between 2023 and 2026, and Fortune Play is the casino on this "
           "site that took that seriously. Aviator, Spaceman, Plinko, Mines, Dice and the full Turbo Games and SmartSoft "
           "shelves sit in a dedicated lobby rather than buried in &lsquo;other&rsquo;."),
 "games_note": ("6,500 games across 80 studios with 300-plus live tables, and a properly built instant-win section. "
                "The bonus-buy range is extensive and &mdash; check this yourself, because it can change &mdash; "
                "currently contributes to wagering at full weight."),
 "payments_note": ("NZD wallet, NZD bank transfer, Neosurf, MiFinity, Bitcoin, Ethereum, USDT. Crypto withdrawals in "
                   "2&ndash;8 hours; our median across three tests was four hours ten minutes."),
 "support_note": ("Chat median 2m 05s. Knowledgeable on game mechanics, which matters when you are querying a crash-game "
                  "round result."),
 "mobile_note": ("Crash titles are built mobile-first here and hold a connection well; we lost one round to a 4G drop in "
                 "roughly six hours of testing."),
},

"lucky-circus": {
 "rating": 8.4, "badge": "NZ$10 minimum deposit",
 "tagline": "The lowest entry price on this site",
 "sub": "NZ$10 minimum, 35x wagering, two-part welcome",
 "best_for": "Low-stakes players and small, controlled deposits",
 "scores": {"Payout speed": 8.0, "Bonus value": 8.5, "Game library": 8.3,
            "Banking &amp; NZD": 9.1, "Trust &amp; disclosure": 8.3},
 "pros": [
   "NZ$10 minimum deposit &mdash; half the market standard and a third of what CrownSlots asks",
   "35x wagering is below the 40x that dominates this market, which matters more than most headline numbers",
   "NZD accounts and NZD bank transfer despite the small-stakes positioning"],
 "cons": [
   "4,800 games is respectable but the live floor at 220 tables is thin for the price point",
   "Crypto withdrawals at 4&ndash;12 hours are slow relative to the field",
   "The NZ$2,500 welcome is the smallest four-figure package here"],
 "verdict": ("Lucky Circus is the answer to a question the rest of this list ignores: what if you want to deposit ten "
             "dollars? The 35x wagering and NZD banking mean a small deposit is not immediately punished, and that "
             "combination is genuinely hard to find offshore."),
 "intro": ("Most offshore casinos are built for players with NZ$100 to move. Lucky Circus is built for players with "
           "NZ$10, and it has structured its wagering and its banking around that rather than treating small deposits "
           "as a nuisance. For a budgeted player, that is worth more than a bigger headline bonus."),
 "games_note": ("4,800 games, 60-plus studios, 220 live tables on the Rabidi platform. Coverage at the low-stakes end is "
                "the relevant metric here, and it is good: plenty of 10c-spin pokies and NZ$0.50 live tables."),
 "payments_note": ("NZ$10 minimum via card, NZD bank transfer or Neosurf. Bitcoin and USDT supported. The NZ$5,000 weekly "
                   "cap is irrelevant at this stake level."),
 "support_note": ("Chat median 3m 40s, the slowest of the Rabidi group but still inside our acceptable band."),
 "mobile_note": ("Standard Rabidi progressive web app. Light and quick, which suits the audience."),
},

"kingdom": {
 "rating": 9.1, "badge": "Fastest payouts &middot; 30x",
 "tagline": "Same-day money and the lowest realistic wagering",
 "sub": "600% to NZ$18,500 at 30x, crypto out in 2&ndash;4 hours",
 "best_for": "Players who withdraw often and want it the same day",
 "scores": {"Payout speed": 9.7, "Bonus value": 9.3, "Game library": 9.0,
            "Banking &amp; NZD": 9.0, "Trust &amp; disclosure": 8.3},
 "pros": [
   "Fastest verified payout programme on this site &mdash; a median of two hours fifty minutes across seven timed crypto withdrawals",
   "30x wagering on a 600% package is the best value-to-turnover ratio of any large bonus here",
   "NZ$10,000 weekly withdrawal cap, joint-highest, so a big win does not take a month to extract"],
 "cons": [
   "Anjouan licence rather than Cura&ccedil;ao GCB, with a lighter complaints and dispute framework behind it",
   "The 600% headline is a four-deposit total, not a first-deposit match &mdash; read the staging carefully",
   "Vertikal N.V. publishes less corporate detail than Dama or Rabidi"],
 "verdict": ("Kingdom is the site for anyone who has ever sat waiting five days for a withdrawal. Two to four hours on "
             "crypto, a NZ$10,000 weekly ceiling and 30x on a very large package make it the most cash-efficient casino "
             "here. The Anjouan licence is the trade-off, and you should price it in."),
 "intro": ("We time withdrawals rather than repeat operator marketing, and Kingdom is the brand that made the programme "
           "worth running. Seven timed crypto cashouts since April 2026 produced a median of two hours fifty minutes and "
           "a worst case of six hours twenty. Nothing else on this site matches that consistency at scale."),
 "games_note": ("7,000-plus games from 80-plus studios with 350-plus live tables &mdash; second only to Spinjo on raw "
                "size, and the search and filtering are better than the Rabidi lobby at the top end. Jackpot coverage is "
                "particularly strong, including the Pragmatic and Red Tiger networked pools."),
 "payments_note": ("Eleven rails including Jeton and Dogecoin, NZD wallet, NZD bank transfer, NZ$20 minimum. The "
                   "NZ$10,000 weekly cap and the two-to-four-hour crypto window are the headline numbers."),
 "support_note": ("24/7 chat, median 1m 30s &mdash; the fastest desk we measured. Withdrawal queries were resolved "
                  "in-session rather than deferred to email."),
 "mobile_note": ("Fast, light mobile build with a cashier that completes a crypto withdrawal in four taps. The best "
                 "mobile cashout flow in this list."),
},

"smash": {
 "rating": 8.8, "badge": "Lowest wagering &middot; 10x",
 "tagline": "The only big bonus you can realistically clear",
 "sub": "600% to NZ$19,500 at 10x on deposit plus bonus",
 "best_for": "Players who actually intend to clear a welcome bonus",
 "scores": {"Payout speed": 8.7, "Bonus value": 9.8, "Game library": 8.2,
            "Banking &amp; NZD": 8.9, "Trust &amp; disclosure": 8.2},
 "pros": [
   "10x wagering is a quarter of the market standard &mdash; on a NZ$100 deposit with a NZ$100 match that is NZ$2,000 of turnover, not NZ$4,000",
   "NZ$19,500 headline is the largest casino package on this site and the sports side adds 250% up to NZ$9,800 at 15x",
   "NZ$10,000 weekly withdrawal cap, so clearing a large bonus does not create a payout bottleneck"],
 "cons": [
   "4,500 games and 40-plus studios is the thinnest lobby of any top-ten brand here",
   "Wagering is calculated on deposit plus bonus, which sounds worse than 10x on bonus alone &mdash; do the arithmetic before comparing",
   "Anjouan licence and limited corporate disclosure from Vertikal N.V."],
 "verdict": ("Smash is a bonus-mathematics play. Ten times deposit-plus-bonus is genuinely the lowest effective wagering "
             "on this site, and on a large package that difference runs into thousands of dollars of turnover you do not "
             "have to generate. You give up lobby size to get it. For a bonus-focused player that is a trade worth making."),
 "intro": ("Almost every casino in this market asks 35x or 40x on the bonus. Smash asks 10x on deposit plus bonus, which "
           "on a matched NZ$100 works out at NZ$2,000 of turnover against NZ$4,000 at a typical 40x. That single term is "
           "the reason the site is here, and it is the term we re-verify every month."),
 "games_note": ("4,500 titles from 40-plus studios with 200 live tables. The mainstream pokies are all present and the "
                "live floor is adequate, but if you hunt boutique releases you will notice the gaps. This is a lobby "
                "built to clear a bonus in, not to browse."),
 "payments_note": ("Ten rails including Jeton and Dogecoin, NZD wallet, NZD bank transfer, NZ$20 minimum, NZ$10,000 "
                   "weekly cap. Crypto cashouts ran 3&ndash;8 hours in testing with a median of four and a half."),
 "support_note": ("Chat median 2m 30s. The desk answered our wagering-calculation question correctly on all three "
                  "attempts, which given the unusual term is a good sign."),
 "mobile_note": ("Straightforward responsive build. The bonus progress meter is visible on mobile, which is more useful "
                 "here than anywhere else on this site."),
},

"rivo": {
 "rating": 8.6, "badge": "Best on a phone",
 "tagline": "The best mobile experience we tested",
 "sub": "NZ$4,500 + 250 spins, 35x, phone-first build",
 "best_for": "Players who never open a laptop",
 "scores": {"Payout speed": 8.5, "Bonus value": 8.6, "Game library": 8.6,
            "Banking &amp; NZD": 8.8, "Trust &amp; disclosure": 8.2},
 "pros": [
   "The fastest mobile build in our testing &mdash; lobby interactive in 1.4 seconds on a throttled 4G connection",
   "35x wagering rather than the usual 40x, on a three-part NZ$4,500 package",
   "Casino and sportsbook on one account with NZD banking and a NZ$8,000 weekly cap"],
 "cons": [
   "Anjouan licence with limited published detail on Vertikal N.V.",
   "5,000 games is mid-table and the live floor at 260 tables is unexceptional",
   "The NZ$300 sports welcome is small next to the casino side"],
 "verdict": ("Roughly three-quarters of the sessions we log are on a phone, and Rivo is the site built as though it "
             "knows that. Everything &mdash; registration, verification, deposit, game launch, cashout &mdash; is fewer "
             "taps and fewer seconds here than anywhere else in this list."),
 "intro": ("We test every casino on a throttled 4G connection from a phone, because that is how most New Zealanders "
           "actually play. Rivo won that test outright: 1.4 seconds to an interactive lobby, a four-field registration, "
           "and a cashier that does not bounce you into a desktop layout."),
 "games_note": ("5,000 games, 65-plus studios, 260-plus live tables. Coverage is fine; presentation is the strength. "
                "Game tiles load progressively rather than all at once, which is why the lobby feels instant on a "
                "phone outside the main centres."),
 "payments_note": ("NZD wallet, NZD bank transfer, Neosurf, card, and three crypto rails. NZ$25 minimum, NZ$8,000 "
                   "weekly cap, crypto out in 3&ndash;8 hours."),
 "support_note": ("Chat median 2m 50s and the chat widget does not obscure the game canvas on a phone, which sounds "
                  "trivial until you have used the ones that do."),
 "mobile_note": ("The reason to be here. Add-to-home-screen works properly on iOS, session state survives a network "
                 "drop, and the cashier is genuinely thumb-sized."),
},

"betandplay": {
 "rating": 8.5, "badge": "Best in-play betting",
 "tagline": "Live betting done properly",
 "sub": "100% up to NZ$500, 5x at 1.80+, deep in-play",
 "best_for": "Punters who bet during the match, not before it",
 "scores": {"Payout speed": 8.6, "Bonus value": 8.4, "Game library": 7.9,
            "Banking &amp; NZD": 8.8, "Trust &amp; disclosure": 8.6},
 "pros": [
   "The most responsive in-play interface we tested, with price updates that do not lag the broadcast by more than a few seconds",
   "5x turnover at odds of 1.80 or better is a reasonable, clearable sports welcome &mdash; not a trap",
   "Rabidi N.V. under the Cura&ccedil;ao Gaming Control Board with NZD banking and NZD bank transfer"],
 "cons": [
   "Sports only in practice &mdash; the casino side is small and not the reason to open an account",
   "NZ$500 welcome is modest against Gunsbet&rsquo;s five-figure headline",
   "Bet-builder coverage on NZ domestic codes is thinner than on European football"],
 "verdict": ("Bet&amp;Play is the sportsbook to use if you bet with a match on the screen in front of you. The in-play "
             "engine is quick, the cash-out is honest, and a 5x turnover at 1.80+ is one of the few sports welcomes on "
             "this site you can actually clear in a fortnight."),
 "intro": ("In-play betting is where offshore books either justify themselves or fall apart, because it exposes the "
           "quality of the trading and the latency of the platform at the same time. Bet&amp;Play handled a full "
           "Super Rugby Pacific round and an NPC Saturday without a suspension we could not explain."),
 "games_note": ("A 3,500-title casino exists behind the sportsbook but it is a secondary product. The betting side "
                "covers NPC, Super Rugby Pacific, ANZ Premiership netball, NRL, A-League, cricket and full NZ "
                "thoroughbred and harness cards, with in-play on all of the main codes."),
 "payments_note": ("NZD wallet, NZD bank transfer, Neosurf, card, Bitcoin, Ethereum and USDT. NZ$20 minimum, NZ$7,000 "
                   "weekly cap, crypto out in 2&ndash;8 hours."),
 "support_note": ("Chat median 2m 15s and, importantly for an in-play book, staffed through New Zealand evening and "
                  "Saturday afternoon."),
 "mobile_note": ("The in-play bet slip is the best on a phone of any book here: it stays docked, it shows the price "
                 "change before it accepts, and it does not silently re-price."),
},

"roby-casino": {
 "rating": 8.1, "badge": "",
 "tagline": "Big bonus, thin disclosure",
 "sub": "250% up to NZ$5,000 + 250 spins at 45x",
 "best_for": "Bonus size, if you accept the transparency gap",
 "scores": {"Payout speed": 7.4, "Bonus value": 8.6, "Game library": 8.1,
            "Banking &amp; NZD": 7.8, "Trust &amp; disclosure": 6.8},
 "pros": [
   "250% up to NZ$5,000 plus 250 free spins is a large package for a site with a NZ$30 minimum",
   "4,000 games and 180 live tables cover the mainstream adequately",
   "Casino and sportsbook share an account, with a NZ$300 sports welcome"],
 "cons": [
   "No licence number is published on the site, and we could not verify a regulator from an NZ IP &mdash; the most serious disclosure gap in this list",
   "45x wagering is the highest here, and on a 250% match that is an extremely large turnover requirement",
   "Slowest cashier we measured: 6&ndash;24 hours on crypto, 24&ndash;48 on e-wallets, three to five business days on cards"],
 "verdict": ("Roby Casino has a big offer and the weakest paperwork on this site. We list it because the bonus is real "
             "and the games work, and we rank it near the bottom because an unpublished licence means you have no "
             "regulator to escalate to if something goes wrong. Deposit accordingly, and keep the amount small."),
 "intro": ("We debated whether to list Roby Casino at all. It is included because the product functions and the offer "
           "is genuine, and it is ranked where it is because the site does not publish a licence number or a corporate "
           "entity. That is a material risk and we are not going to bury it in a footnote."),
 "games_note": ("4,000 titles across 50-plus studios with 180 live tables. Mainstream Pragmatic, Play&rsquo;n GO and "
                "Evolution coverage is there. Nothing about the lobby is remarkable in either direction."),
 "payments_note": ("Card, Skrill, Neteller, Neosurf, Bitcoin and USDT, no NZD bank transfer, NZ$30 minimum, NZ$5,000 "
                   "weekly cap. The slowest processing times of any brand here across every rail."),
 "support_note": ("Chat median 6m 40s with a queue during Australasian evenings. Our licence question was not answered "
                  "on two of three attempts."),
 "mobile_note": ("Functional responsive build with no notable problems and no notable strengths."),
},

"spino": {
 "rating": 8.3, "badge": "0x wagering &middot; crypto only",
 "tagline": "Zero wagering, ten-minute payouts, crypto only",
 "sub": "Up to 2,000 USDT with no turnover requirement",
 "best_for": "Crypto players who refuse to wager a bonus",
 "scores": {"Payout speed": 9.9, "Bonus value": 9.0, "Game library": 7.6,
            "Banking &amp; NZD": 6.4, "Trust &amp; disclosure": 7.6},
 "pros": [
   "0x wagering &mdash; bonus winnings are withdrawable immediately, which no other brand on this site offers",
   "Fastest cashier we have ever timed: ten minutes to two hours, with our quickest USDT withdrawal at eleven minutes",
   "No stated weekly withdrawal cap, so a large win is not rationed out over a month"],
 "cons": [
   "Crypto only. No card, no bank transfer, no NZD &mdash; if you do not already hold crypto this site is not for you",
   "Tobique licence is the least-established regulator represented here",
   "~3,500 games and 150 live tables make it the smallest lobby on this page"],
 "verdict": ("Spino is a specialist and an excellent one. Zero wagering and a ten-minute cashier are the two things "
             "players say they want most and almost never get together. The cost is that it is crypto-only with a "
             "small lobby and a lightweight licence. For the right player it is unbeatable; for most Kiwis it is not "
             "the first account to open."),
 "intro": ("Zero-wagering bonuses are rare because they are expensive to offer, and they are usually hedged with a low "
           "cap. Spino&rsquo;s is up to 2,000 USDT with no turnover attached, paired with the fastest withdrawals we "
           "have recorded from any operator. The catch is the entry requirement: you must arrive holding crypto."),
 "games_note": ("Around 3,500 games and 150 live tables &mdash; enough for a session, not enough to explore. The "
                "instant-win and crash shelf is proportionally strong, which fits the crypto-native audience."),
 "payments_note": ("Eight crypto rails including Solana and Tron, 20 USDT minimum, no fiat of any kind. Withdrawals "
                   "process in ten minutes to two hours with no weekly cap published. You carry the exchange-rate risk "
                   "between your wallet and the New Zealand dollar."),
 "support_note": ("Chat median 3m 10s. Competent on crypto mechanics, unhelpful on anything else."),
 "mobile_note": ("Light, fast and clearly designed for a phone with a wallet app beside it."),
},

"ivibet": {
 "rating": 8.2, "badge": "",
 "tagline": "A realistic bonus and a big live floor",
 "sub": "100% up to NZ$500 + 50 spins at 35x",
 "best_for": "Live dealer players who want an achievable bonus",
 "scores": {"Payout speed": 8.0, "Bonus value": 8.0, "Game library": 8.4,
            "Banking &amp; NZD": 7.8, "Trust &amp; disclosure": 8.4},
 "pros": [
   "300 live tables is a large floor for a 4,000-game casino &mdash; the live product is clearly the priority",
   "NZ$500 at 35x on a single deposit is a bonus a normal player can finish in a fortnight",
   "TechOptions Group is a named operator with a Cura&ccedil;ao licence and a long trading history"],
 "cons": [
   "No NZD bank transfer, so funding leans on card, e-wallet or crypto",
   "The bonus is small &mdash; if headline value is your metric, look elsewhere on this page",
   "Card withdrawals took the full five business days in one of our tests"],
 "verdict": ("Ivibet is an unfashionable recommendation and a sensible one. A NZ$500 bonus at 35x on one deposit is "
             "the kind of offer a person can actually complete, and the 300-table live floor is bigger than casinos "
             "twice its size. It will not excite a bonus hunter and it will suit a blackjack player."),
 "intro": ("Most of this list competes on headline bonus size. Ivibet competes on the live floor and on a welcome "
           "offer proportioned to an ordinary deposit. Three hundred tables, 35x on a single NZ$500 match, and a "
           "platform that has been running under TechOptions since 2022."),
 "games_note": ("4,000 games from 55-plus studios, with the 300-table live floor as the centrepiece &mdash; full "
                "Evolution range plus Ezugi and Pragmatic Live. Blackjack variant coverage in particular is better "
                "than the game count suggests."),
 "payments_note": ("Card, Skrill, Neteller, Neosurf, MiFinity and three crypto rails. NZ$20 minimum, NZ$5,000 weekly "
                   "cap, no NZD bank transfer. Crypto out in 2&ndash;12 hours."),
 "support_note": ("Chat median 3m 30s, with a noticeable slowdown in the New Zealand morning."),
 "mobile_note": ("Live tables stream cleanly on 4G at the lower quality setting; the table lobby is cramped on a "
                 "small screen."),
},

"ivibet-sportsbook": {
 "rating": 8.2, "badge": "Best niche markets",
 "tagline": "Netball, domestic codes and long-tail markets",
 "sub": "100% up to NZ$200, 5x at 2.00+",
 "best_for": "ANZ Premiership netball and other under-priced NZ markets",
 "scores": {"Payout speed": 8.0, "Bonus value": 7.8, "Game library": 8.2,
            "Banking &amp; NZD": 7.8, "Trust &amp; disclosure": 8.4},
 "pros": [
   "Prices ANZ Premiership netball, NZ domestic cricket and secondary rugby markets that most offshore books ignore",
   "5x at odds of 2.00 or better is a clean, clearable turnover requirement on a small welcome",
   "Shares the Ivibet account and wallet, so a casino balance and a sports balance are one pot"],
 "cons": [
   "NZ$200 welcome is the smallest sports offer on this site",
   "Margins on mainstream football are wider than Bet&amp;Play or Gunsbet",
   "In-play depth on NZ codes is limited compared with the pre-match book"],
 "verdict": ("Ivibet&rsquo;s sportsbook is a specialist tool. It is not where you get the best price on the Premier "
             "League, and it is frequently where you get the only price on an ANZ Premiership market or a Plunket "
             "Shield line. Keep it as a second or third account for exactly that reason."),
 "intro": ("Offshore books serve New Zealand with European priorities: football, tennis, NBA. Ivibet&rsquo;s book is "
           "worth an account because it consistently posts markets on domestic New Zealand sport that the larger "
           "operators cannot be bothered pricing, and an unpriced market is where value lives."),
 "games_note": ("The sportsbook covers rugby union and league, netball, cricket, football, basketball and NZ racing. "
                "The netball coverage &mdash; match winner, margin, top scorer across the ANZ Premiership &mdash; is "
                "the standout and is thin to non-existent at most rivals."),
 "payments_note": ("Identical to Ivibet Casino: card, e-wallets, Neosurf, MiFinity and crypto, NZ$20 minimum, "
                   "NZ$5,000 weekly cap, no NZD bank transfer."),
 "support_note": ("Shared desk with the casino, median 3m 30s. Sports queries were handled accurately."),
 "mobile_note": ("Simple and quick. The bet slip is basic but reliable, and multi-leg builders are supported on the "
                 "main codes."),
},

"hellspin": {
 "rating": 8.1, "badge": "",
 "tagline": "Slot races and pokies tournaments",
 "sub": "100% up to NZ$500 + 150 spins at 40x",
 "best_for": "Players who enjoy leaderboards and tournaments",
 "scores": {"Payout speed": 8.0, "Bonus value": 8.1, "Game library": 8.3,
            "Banking &amp; NZD": 7.6, "Trust &amp; disclosure": 8.2},
 "pros": [
   "A genuinely active tournament calendar &mdash; daily and weekly slot races with published prize pools",
   "150 free spins is a large spin count for a NZ$500 match",
   "Running since 2021 under TechOptions Group, which is a long life for this market segment"],
 "cons": [
   "40x wagering on both the match and the spin winnings",
   "No NZD bank transfer and no NZD-native wallet",
   "4,500 games is mid-table and the live floor at 200 tables is average"],
 "verdict": ("Hellspin&rsquo;s tournaments are the reason to be here. If a leaderboard makes a session more fun for "
             "you, it is a meaningfully different experience from the rest of this list. If it does not, there is "
             "little here that Spinjo or Kingdom do not do better."),
 "intro": ("Slot tournaments are a real differentiator when they are properly funded and a gimmick when they are not. "
           "Hellspin runs daily and weekly races with published prize pools and visible leaderboards, and has done "
           "consistently since 2021 rather than as a launch-month promotion."),
 "games_note": ("4,500 titles, 60-plus studios, 200 live tables. Tournament-eligible games rotate weekly and are "
                "clearly flagged in the lobby, which is a small piece of UX most tournament casinos get wrong."),
 "payments_note": ("Card, Skrill, Neteller, Neosurf, MiFinity, Bitcoin and USDT. NZ$20 minimum, NZ$5,000 weekly cap. "
                   "Crypto withdrawals 2&ndash;12 hours."),
 "support_note": ("Chat median 3m 45s. Tournament rules queries were answered with a link to the terms rather than an "
                  "explanation."),
 "mobile_note": ("Leaderboards are legible on a phone and update live, which is the main thing that matters here."),
},

"slotsgem": {
 "rating": 7.9, "badge": "",
 "tagline": "A quiet, uncluttered pokies lobby",
 "sub": "100% up to NZ$400 + 100 spins at 40x",
 "best_for": "Players who want pokies without the noise",
 "scores": {"Payout speed": 7.4, "Bonus value": 7.6, "Game library": 8.0,
            "Banking &amp; NZD": 7.6, "Trust &amp; disclosure": 8.0},
 "pros": [
   "The cleanest, least aggressive interface on this site &mdash; no countdown timers, no pop-ups, no wheel",
   "3,800 pokies is plenty for most players and the search actually works",
   "TechOptions Group operator with a Cura&ccedil;ao licence and a straightforward terms page"],
 "cons": [
   "Slowest crypto processing of the TechOptions brands at 4&ndash;24 hours",
   "NZ$4,000 weekly withdrawal cap is the lowest here",
   "NZ$400 welcome is the smallest casino offer on this site"],
 "verdict": ("Slotsgem is the least exciting casino we list and that is close to being the point. It does not chase "
             "you around the lobby with offers. If you find modern casino interfaces exhausting, this is the calm one "
             "&mdash; provided you can live with a slower cashier and a small ceiling."),
 "intro": ("There is a real audience for a casino that simply shows you the pokies and leaves you alone. Slotsgem is "
           "that site: no wheel, no countdown, no pop-up on every third click, and a bonus small enough that it is not "
           "constantly being advertised at you."),
 "games_note": ("3,800 titles, 50-plus studios, 160 live tables. Pokies-led with a modest live floor. Search and "
                "provider filtering are clean and fast."),
 "payments_note": ("Card, Skrill, Neteller, Neosurf, Bitcoin and USDT. NZ$20 minimum, NZ$4,000 weekly cap, crypto out "
                   "in 4&ndash;24 hours &mdash; the slowest window on this site apart from Roby."),
 "support_note": ("Chat median 4m 05s. Polite, slow, accurate."),
 "mobile_note": ("Light pages and a simple lobby make this one of the better low-bandwidth options in the list."),
},

}
