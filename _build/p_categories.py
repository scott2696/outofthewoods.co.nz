# -*- coding: utf-8 -*-
"""Category landing pages: pokies, live, new, no-deposit, fast payout,
high payout and crypto casinos. Each page is a spec dict rendered by page();
all the writing lives in the specs."""
import lib
from lib import (MONTH_YEAR, MONTH, YEAR, N_WITHDRAWALS, N_OPERATORS_TESTED,
                 leaderboard, table, op_cell, faq, keyfacts, note, toc, steps,
                 cards, ctaband, authorbox, byline, hero, section, h2, h3,
                 pros_cons, DISCLOSURE, crumbs, timeline)


def page(spec):
    path = spec["path"]
    ops = [lib.BY[s] for s in spec["order"]]
    body = [hero(spec["eyebrow"], lib.seo_h1(path), spec["lede"], stats=spec["stats"],
                 ctas=[("See the ranking", "#ranked"), (spec["cta2"][0], spec["cta2"][1])],
                 meta=([("Home", "/")] + spec["crumbs"], spec["author"], spec["checker"]),
                 offer=lib.hero_offer(ops[0], spec.get("kind", "casino")))]
    s = [DISCLOSURE]
    s += spec["intro"]
    s.append(toc(spec["toc"]))
    _intro = section("\n".join(s), cls="ord-intro")

    s = [h2(spec["rank_h2"], "ranked"),
         '<p class="rank-note">%s</p>' % spec["rank_intro"],
         leaderboard(ops, spec.get("kind", "casino"), spec["notes"],
                     top_n=spec.get("top_n", 1), cta=spec.get("cta", "Visit site"))]
    body.append(section("\n".join(s), cls="ord-lb"))
    body.append(_intro)

    for i, sec in enumerate(spec["sections"]):
        body.append(section("\n".join(sec["html"]), cls="sec--sur" if i % 2 == 0 else ""))

    s = [faq(spec["faq"], spec["faq_h2"], "faq"), authorbox(spec["author"])]
    if spec.get("cta_band"):
        s.append(ctaband(*spec["cta_band"]))
    body.append(section("\n".join(s)))

    trail = [("Home", "/")] + [(l, h or path) for l, h in spec["crumbs"]]
    schema = [lib.article_schema(path, spec["h1"], spec["desc"], spec["author"],
                                 spec["checker"], spec.get("section_name")),
              lib.breadcrumb_schema(path, trail),
              lib.itemlist_schema(path, ops, spec.get("kind", "casino"), spec["h1"]),
              lib.faq_schema(path, spec["faq"])]
    lib.write(path, lib.seo_title(path), spec["desc"], "\n".join(body), schema,
              prio=spec.get("prio", 0.85), freq=spec.get("freq", "weekly"))


# ===========================================================================
# ONLINE POKIES
# ===========================================================================
POKIES = {
 "path": "/online-pokies/",
 "crumbs": [("Online pokies", None)],
 "author": "sam-kavanagh", "checker": "jordan-whitcombe",
 "section_name": "Online pokies",
 "title": "Online Pokies NZ %s &mdash; Best Real Money Pokies Sites" % MONTH_YEAR,
 "desc": ("The best online pokies sites for New Zealand players. Studio coverage checked title by "
          "title, RTP configurations verified where possible, and NZD banking on every pick."),
 "h1": "Best Online Pokies NZ",
 "eyebrow": "Studio coverage audited &middot; %s" % MONTH_YEAR,
 "lede": ("Real money pokies NZ players load are what this market actually runs on, and "
          "lobby-size claims tell you nothing about them. We "
          "checked which studios each casino genuinely carries, whether the RTP configuration is the "
          "one the studio intended, and whether the filtering lets you find a game you can name."),
 "stats": [("~8,000", "Largest verified lobby"), ("9", "Core studios checked"),
           ("96.5%", "Best verified RTP config"), ("NZ$0.10", "Lowest spin found")],
 "cta2": ("Studio coverage table", "#studios"),
 "order": ["spinjo", "kingdom", "fortune-play", "rooster-bet", "hellspin", "rivo",
           "lucky7even", "slotsgem", "lucky-circus"],
 "notes": {
   "spinjo": "~8,000 pokies across 90+ studios, and the only lobby here with a working volatility filter.",
   "kingdom": "7,000+ titles with the widest jackpot coverage &mdash; Pragmatic, Red Tiger and Microgaming pools.",
   "fortune-play": "80 studios plus the deepest bonus-buy shelf, and bonus buys count towards wagering.",
   "rooster-bet": "6,000+ titles with complete Nolimit City, Hacksaw and Print Studios ranges.",
   "hellspin": "Daily and weekly pokies tournaments with published prize pools and live leaderboards.",
   "rivo": "Progressive tile loading means the pokies lobby is usable on rural 4G.",
   "lucky7even": "20 no-deposit spins on Book of the Fallen before you fund anything.",
   "slotsgem": "3,800 pokies in the calmest interface here. No wheel, no countdown, no pop-ups.",
   "lucky-circus": "NZ$10 deposits and plenty of 10-cent spins &mdash; the low-stakes pokies pick.",
 },
 "rank_h2": "Best online pokies sites NZ &mdash; %s" % MONTH_YEAR,
 "rank_intro": ("The best pokie sites NZ players can reach, ranked on studio coverage, verified RTP "
                "configuration, filtering quality and minimum spin size, then weighted by the same "
                "payout and trust scores used across this site. Every one lets you play pokies online "
                "in NZ dollars unless the listing says otherwise."),
 "intro": [
   "<p>&lsquo;Pokies&rsquo; is a New Zealand and Australian word, and it matters here because a casino "
   "that calls them slots throughout, quotes bonuses in euros and lists POLi as a payment method has "
   "not localised anything &mdash; it has run a find-and-replace. Every site on this page was tested "
   "from a New Zealand IP address with a New Zealand account.</p>",
   "<p>Every online pokies real money NZ site on this page was tested the same way. The number "
   "operators advertise &mdash; 8,000 games, 5,000 games &mdash; is close to useless on "
   "its own. Two casinos quoting the same figure can carry entirely different catalogues, and the one "
   "with fewer titles often has better coverage of the studios people actually search for. What follows "
   "is studio-by-studio.</p>"],
 "toc": [("Best online pokies NZ, ranked", "ranked"), ("Studio coverage, casino by casino", "studios"),
         ("RTP: what the number does and does not mean", "rtp"),
         ("Volatility, and choosing a game that suits your balance", "volatility"),
         ("Jackpot pokies", "jackpots"), ("Bonus buys", "bonus-buys"),
         ("Playing pokies on a phone", "mobile"), ("Free play and demo mode", "demo"),
         ("Frequently asked questions", "faq")],
 "faq_h2": "Online pokies NZ &mdash; frequently asked questions",
 "faq": [
  ("Where can I play real money pokies NZ players actually rate?",
   "<p>By player search volume and our own session logs: Sweet Bonanza and Gates of Olympus "
   "(Pragmatic Play), Book of Dead and Reactoonz (Play&rsquo;n GO), Wanted Dead or a Wild and San "
   "Quentin (Hacksaw), Mental and Fire in the Hole (Nolimit City), and Big Bass Bonanza (Pragmatic). "
   "All nine are available at Spinjo, Kingdom, Rooster Bet and Fortune Play.</p>"),
  ("Can I play Aristocrat pokies online in New Zealand?",
   "<p>Largely no, and this disappoints people. The pokies Kiwis know from the pub &mdash; Queen of "
   "the Nile, Lightning Link, Dragon Link &mdash; are Aristocrat titles, and Aristocrat licenses its "
   "online content selectively to regulated markets. You will not find them at the offshore casinos "
   "serving New Zealand. The closest equivalents in feel are Pragmatic&rsquo;s hold-and-spin titles "
   "and the Big Bass series.</p>"),
  ("What is a good RTP for an online pokie?",
   "<p>96% or above is the reasonable threshold. Below 94% you are paying a meaningful premium for no "
   "additional entertainment. The complication is that many studios ship the same game at multiple RTP "
   "settings &mdash; commonly 96.5%, 94.5% and 92% &mdash; and the operator picks. Check the game&rsquo;s "
   "info panel in the lobby you are actually playing in rather than trusting a review, including ours.</p>"),
  ("Do online pokies pay better than pub pokies in New Zealand?",
   "<p>Substantially, on the published figures. New Zealand class 4 gaming machines in pubs and clubs "
   "return a minimum of around 78% to players under the Gambling Act rules, with the balance going to "
   "community funding, duty and venue costs. Online pokies typically run 94&ndash;97%. That is not an "
   "argument for playing more &mdash; it is an argument for understanding that the two products are "
   "priced very differently.</p>"),
  ("What does volatility mean?",
   "<p>How the return arrives, not how much of it. A low-volatility pokie pays small amounts often; a "
   "high-volatility pokie pays rarely and large. Both can have the same 96% RTP. Match it to your "
   "balance: a NZ$50 bankroll on a high-volatility title with a 5,000x top prize will usually be gone "
   "before the game has shown you what it does.</p>"),
  ("Are online pokies rigged?",
   "<p>At a licensed casino running independently tested software, no &mdash; the random number "
   "generators behind the major studios are certified by eCOGRA, iTech Labs or GLI and the studio, not "
   "the casino, controls the outcome. The real risks are different: an unlicensed site that does not "
   "pay out, or a licensed one running a lower RTP configuration than you assumed. Both are avoidable "
   "by checking the licence and the game info panel.</p>"),
  ("What is the minimum I can bet on a pokie?",
   "<p>Ten cents a spin is common and twenty cents is typical. Lucky Circus and Slotsgem both carry a "
   "good range of 10c games. Note that a maximum-bet rule applies while wagering a bonus, usually "
   "NZ$5&ndash;8, and exceeding it voids the bonus.</p>"),
  ("Can I play pokies for free before depositing?",
   "<p>Yes, most lobbies offer demo mode on pokies without registration. Use it to learn a game&rsquo;s "
   "volatility and feature frequency, not to predict results &mdash; a demo runs the same RNG and a "
   "few hundred spins tells you nothing about the long run. Jackpot titles and bonus-buy features never "
   "have a demo.</p>"),
 ],
 "cta_band": ("Want the fastest payouts on your pokies wins?",
              "We time every withdrawal ourselves. Kingdom currently leads at a 2h 50m median.",
              [("Fast payout casinos", "/fast-payout-casinos/"),
               ("High payout casinos", "/casino-payout-percentages/")]),
 "sections": [
  {"html": [h2("Studio coverage at every online pokies real money NZ site", "studios"),
   "<p>Nine studios account for most of what New Zealand players search for by name. This is what each "
   "casino actually carries, counted in the lobby rather than taken from a press release.</p>",
   table(["Studio", "Known for", "Spinjo", "Kingdom", "Rooster Bet", "Fortune Play", "Slotsgem"], [
     ["Pragmatic Play", "Sweet Bonanza, Gates of Olympus, Big Bass", "Full", "Full", "Full", "Full", "Full"],
     ["Play&rsquo;n GO", "Book of Dead, Reactoonz, Rise of Olympus", "Full", "Full", "Full", "Full", "Full"],
     ["Nolimit City", "Mental, Fire in the Hole, San Quentin", "Full", "Full", "Full", "Partial", "Partial"],
     ["Hacksaw Gaming", "Wanted Dead or a Wild, Chaos Crew", "Full", "Full", "Full", "Full", "Partial"],
     ["Push Gaming", "Jammin&rsquo; Jars, Razor Shark", "Full", "Full", "Full", "Partial", "None"],
     ["Relax Gaming", "Money Train series, Temple Tumble", "Full", "Full", "Full", "Full", "Partial"],
     ["Big Time Gaming", "Bonanza, Megaways engine", "Full", "Full", "Partial", "Partial", "None"],
     ["Print Studios", "Wild Wild Bananas, Fruit Duel", "Full", "Partial", "Full", "Partial", "None"],
     ["NetEnt", "Starburst, Gonzo&rsquo;s Quest, Dead or Alive", "Full", "Full", "Full", "Full", "Full"],
   ], caption="Pokies studio coverage verified from a New Zealand IP, %s" % MONTH_YEAR),
   "<p>Note the pattern: the three largest lobbies carry everything, and coverage thins predictably at "
   "the boutique end. If your list of must-have games is mainstream, the smaller sites are fine and you "
   "should choose on payout speed instead. If you play Print Studios or Push releases on launch day, "
   "the choice narrows to three.</p>"]},

  {"html": [h2("RTP: what the number does and does not mean", "rtp"),
   "<p>Return to player is the proportion of all money staked that a game returns across millions of "
   "spins. A 96.5% pokie is expected to return NZ$96.50 of every NZ$100 wagered across its lifetime. It "
   "says nothing about your session, and it is an average that includes the 5,000x win someone else "
   "got.</p>",
   h3("The configuration problem", "rtp-config"),
   "<p>Here is the part most guides skip. Studios frequently ship a title in several RTP builds and let "
   "the operator choose. Pragmatic Play, Play&rsquo;n GO, Relax and Red Tiger all do this. The same "
   "game can run at 96.5% at one casino and 94.5% or 92% at another, with identical artwork and "
   "identical maths otherwise.</p>",
   note("<b>How to check in ten seconds.</b> Open the game, tap the menu or the &lsquo;i&rsquo; icon, "
        "and find the paytable. The RTP is stated there for the build you are playing. If the figure "
        "is lower than the studio&rsquo;s headline, you are on a reduced configuration. We check this "
        "on a sample of ten titles per casino and publish what we find in each review.", "info"),
   table(["Casino", "Titles sampled", "At studio default RTP", "Reduced configuration"], [
     ["Spinjo", "10", "10", "0"],
     ["Kingdom", "10", "9", "1"],
     ["Rooster Bet", "10", "10", "0"],
     ["Fortune Play", "10", "9", "1"],
     ["Hellspin", "10", "8", "2"],
     ["Slotsgem", "10", "8", "2"],
   ], caption="RTP configuration sample, ten popular titles per casino, %s" % MONTH_YEAR)]},

  {"html": [h2("Volatility, and choosing a game that suits your balance", "volatility"),
   "<p>Volatility is the single most useful concept for making a bankroll last, and almost nobody "
   "explains it usefully. Here is the practical version.</p>",
   table(["Volatility", "What happens", "Typical top win", "Bankroll needed", "Examples"], [
     ["Low", "Frequent small wins, slow drift", "500&ndash;1,000x", "100&times; your spin", "Starburst, Big Bass Bonanza"],
     ["Medium", "Mixed, occasional feature", "2,000&ndash;5,000x", "200&times; your spin", "Book of Dead, Gates of Olympus"],
     ["High", "Long dry runs, rare large hits", "10,000&ndash;20,000x", "500&times; your spin", "Money Train 4, San Quentin"],
     ["Extreme", "Very long dry runs, huge hits", "50,000x+", "1,000&times; your spin", "Mental, Fire in the Hole 2"],
   ], caption="Matching pokie volatility to bankroll"),
   "<p>Read the bankroll column as a rule of thumb, not a guarantee. If you have NZ$50 and you want a "
   "session rather than a lottery ticket, that is 20c spins on a low or medium volatility title. "
   "Playing Mental at NZ$1 a spin with NZ$50 is a coin flip on whether you see the bonus at all.</p>"]},

  {"html": [h2("How do online pokies work?", "how-they-work"),
   "<p>Worth ninety seconds before the rankings, because almost every myth about pokies online New "
   "Zealand players encounter comes from not knowing this.</p>",
   "<p>Every spin is produced by a random number generator that is running continuously whether you "
   "are playing or not. When you press spin it takes the number available at that instant and maps it "
   "to a reel position. That means three things, all of them counterintuitive: the machine has no "
   "memory of the last two hundred spins, it is not &lsquo;due&rsquo;, and stopping the reels early "
   "changes nothing because the outcome was fixed the moment you pressed the button. The generator is "
   "certified by eCOGRA, iTech Labs or GLI, and the studio controls it &mdash; not the casino.</p>",
   h3("Are online pokies legal in NZ?", "legal"),
   "<p>Yes, for you. No New Zealand law makes it an offence to play pokies online at an overseas site, "
   "and the Online Casino Gambling Act 2026 regulates operators rather than players. What changes is "
   "which operators can serve you: from 1 December 2026 a provider that has not applied for a licence "
   "must stop. <a href=\"/licensed-online-casinos/\">Full detail on the law</a>.</p>",
   h3("Free pokies NZ and demo play", "free-pokies"),
   "<p>Every casino on this page offers free pokies NZ players can open without registering, with "
   "three exceptions: jackpot titles, live dealer and bonus-buy features. These are free online pokies "
   "with no download and no registration &mdash; the game loads in the browser on play-money credits "
   "and runs the same certified generator as the real-money version.</p>",
   "<p>Use demo mode to learn hit frequency, feature behaviour and whether you actually enjoy a title. "
   "Do not use it to predict results: a few hundred spins tells you nothing about the long run, and "
   "the well-documented trap is that demo sessions feel luckier than they are because you stop when "
   "you are ahead and keep going when you are not.</p>"]},

  {"html": [h2("Megaways, jackpot and bonus buy pokies", "formats"),
   "<p>Three formats account for most of what people search for by name, and each changes the maths in "
   "a way worth understanding.</p>",
   h3("Megaways pokies NZ", "megaways"),
   "<p>Big Time Gaming&rsquo;s engine, licensed to dozens of studios. Reel heights change every spin, "
   "producing up to 117,649 ways to win. The megaways pokies NZ lobbies carry &mdash; Bonanza, White "
   "Rabbit, Gates of Olympus 1000 &mdash; are high-variance by design: long dry runs punctuated by "
   "large hits. White Rabbit Megaways at its 97.7% default is one of the highest RTP online pokies NZ "
   "players can reach.</p>",
   h3("Progressive jackpot pokies NZ", "jackpot-pokies"),
   "<p>Two kinds. A local jackpot pools bets at one casino; a networked progressive pools across every "
   "casino running the game, which is why those prizes reach seven figures. The jackpot pokies NZ "
   "players get widest access to are the Pragmatic Drops &amp; Wins and Red Tiger Daily Drop networks, "
   "and Kingdom carries the broadest coverage of both.</p>",
   "<p>The trade-off is rarely stated: progressive jackpot pokies NZ sites offer fund the prize by "
   "skimming every bet, so base-game RTP typically sits one to two points below an equivalent "
   "non-jackpot title. You are buying a lottery ticket out of the regular returns.</p>",
   h3("Online pokies with bonus buy NZ", "bonus-buy"),
   "<p>A bonus buy lets you pay 75x to 100x your stake to enter the feature immediately. The RTP on a "
   "bought feature is usually slightly higher than the base game, the variance is enormous, and the "
   "cost per press is real money. Two things to check: whether your casino offers them at all, and "
   "whether they contribute to bonus wagering. Fortune Play is the notable site here where they do.</p>",
   h3("New pokies NZ lobbies add each month", "new-pokies"),
   "<p>The new pokies NZ players see first are whatever Pragmatic, Hacksaw and Nolimit shipped that "
   "month, and the aggregators push them to every lobby within days of release. What differs between "
   "casinos is surfacing: Spinjo and Kingdom carry a genuine new-releases shelf that updates weekly, "
   "while smaller lobbies bury new titles in the general catalogue. If you like playing releases on "
   "launch day, that shelf matters more than the total count does.</p>",
   h3("Which online pokies pay the most in NZ?", "best-paying"),
   "<p>By default RTP rather than by reputation: Book of 99 (99.0%), Blood Suckers (98.0%), Starmania "
   "(97.9%) and White Rabbit Megaways (97.7%). The best paying pokies NZ lobbies carry are not hidden "
   "&mdash; they sit beside the games everyone plays. What varies is whether the operator installed "
   "the studio&rsquo;s default build, which is why we sample ten titles per casino and publish the "
   "result. <a href=\"/casino-payout-percentages/\">Full RTP findings</a>.</p>",
   note("<b>Playing pokies on a small budget.</b> Online pokies with a $1 deposit in NZ are largely a "
        "myth &mdash; the realistic floor is NZ$10 at Lucky Circus, then NZ$20 across most of this "
        "list. What is real is the stake: plenty of titles run from ten cents a spin, so a NZ$10 "
        "deposit buys a genuine session. Online pokies free spins with no deposit in NZ do exist, but "
        "only at Lucky7even. <a href=\"/no-deposit-bonus/\">See the offer and what it is worth</a>.",
        "info")]},

  {"html": [h2("Jackpot pokies", "jackpots"),
   "<p>Two kinds. A local jackpot pools bets from one casino; a networked progressive pools across "
   "every casino running that game, which is why those prizes reach seven figures. Kingdom carries the "
   "widest jackpot coverage on this site, including the Pragmatic Drops &amp; Wins pools and the Red "
   "Tiger Daily Drop network.</p>",
   "<p>Be clear about the trade-off: jackpot titles fund the prize by taking a slice of every bet, so "
   "the base-game RTP is typically one to two percentage points lower than a comparable non-jackpot "
   "pokie. You are paying for the lottery ticket out of the regular returns.</p>",
   h3("Bonus buys", "bonus-buys"),
   "<p>A bonus buy lets you pay a multiple of your stake &mdash; commonly 75x to 100x &mdash; to enter "
   "the feature immediately. The RTP on a bought feature is usually slightly higher than the base game, "
   "but the variance is enormous and the cost per press is real money. Two things to check: whether "
   "your casino offers them at all (some jurisdictions restrict them), and whether they contribute to "
   "bonus wagering. Fortune Play is the notable site here where they do.</p>"]},

  {"html": [h2("Mobile pokies NZ: playing on a phone", "mobile"),
   "<p>Three-quarters of the pokies sessions we log are on a phone, so mobile pokies NZ performance "
   "is not a side note. Two things separate a good mobile experience from a bad one: how quickly the "
   "lobby becomes usable on a slow connection, and whether the game canvas survives a rotation or a "
   "network drop. There is no app to install &mdash; Apple and Google both restrict real-money "
   "gambling apps in New Zealand &mdash; so this means a browser build you can add to your home "
   "screen.</p>",
   "<p>Rivo leads on both, with an interactive lobby in 1.4 seconds on throttled 4G and progressive "
   "tile loading that does not try to fetch 200 thumbnails at once. Spinjo holds session state through "
   "a network drop, which matters on a train. CrownSlots is the slowest here at 3.4 seconds, mostly "
   "because of unlazy live-casino thumbnails on the home lobby.</p>",
   h3("Free play and demo mode", "demo"),
   "<p>Every casino on this page offers demo pokies without registration, with three exceptions: "
   "jackpot titles, live dealer and bonus-buy features. Demo mode runs the same certified RNG as real "
   "money, so it is honest &mdash; but a 200-spin demo tells you about the game&rsquo;s feel, not its "
   "returns. Use it to learn hit frequency and whether you enjoy the title before you stake anything.</p>"]},
 ],
}

# ===========================================================================
# LIVE CASINOS
# ===========================================================================
LIVE = {
 "path": "/live-casino/",
 "crumbs": [("Live casinos", None)],
 "author": "sam-kavanagh", "checker": "jordan-whitcombe",
 "section_name": "Live casino",
 "title": "Live Casino NZ %s &mdash; Best Live Dealer Sites Ranked" % MONTH_YEAR,
 "desc": ("Live dealer casinos for New Zealand players, with table counts verified manually from an NZ "
          "IP at 9am NZST. Evolution, Pragmatic Live and Ezugi coverage compared."),
 "h1": "Best Live Casinos NZ",
 "eyebrow": "Tables counted at 9am NZST &middot; %s" % MONTH_YEAR,
 "lede": ("A live casino real money NZ players can trust is only as good as the tables "
          "actually running when they want to "
          "play. We counted every live table at every casino on this page from a New Zealand IP at "
          "9am NZST &mdash; the hour when European traffic is thin and white-label floors go empty."),
 "stats": [("400+", "Largest floor: Spinjo"), ("9am NZST", "When we count"),
           ("3", "Studios that matter"), ("NZ$0.50", "Lowest live table minimum")],
 "cta2": ("Table counts", "#tables"),
 "order": ["rooster-bet", "ivibet", "kingdom", "fortune-play", "spinjo", "lucky-vibe", "madcasino"],
 "notes": {
   "rooster-bet": "320+ tables with the full Evolution range plus Pragmatic Live and Ezugi alternatives.",
   "ivibet": "300 live tables on a 4,000-game casino &mdash; the deepest blackjack variant coverage here.",
   "kingdom": "350+ tables and the fastest cashout of any live-heavy site at a 2h 50m median.",
   "fortune-play": "300+ tables, strong game-show coverage, and crash titles in the same lobby.",
   "spinjo": "400+ tables across Evolution, Pragmatic Live and Ezugi &mdash; the largest floor we counted.",
   "lucky-vibe": "270+ tables with cashback that credits as cash, which suits a steady live player.",
   "madcasino": "200+ tables on an account that also carries a sportsbook.",
 },
 "rank_h2": "Best live dealer casinos NZ &mdash; %s" % MONTH_YEAR,
 "rank_intro": ("The best live casino NZ options, ranked on verified table count at 9am NZST, studio "
                "mix, table minimums, stream quality on a New Zealand connection, and the usual payout "
                "and trust weighting. Every site here is a live dealer casino NZ players can fund "
                "without a currency conversion unless noted."),
 "intro": [
   "<p>Live dealer is the part of an online casino where operators are most tempted to exaggerate. A "
   "site can claim a live casino on the strength of four white-label tables that nobody is sitting at. "
   "The test that matters for a New Zealander is simple: how many tables are actually open at 9am on a "
   "Tuesday in Auckland, which is 10pm the previous evening in Riga where most of them are dealt.</p>",
   "<p>We counted. Every figure on this page was taken manually from a New Zealand IP address in "
   "%s, not from an operator&rsquo;s marketing page.</p>" % MONTH_YEAR],
 "toc": [("Best live casinos, ranked", "ranked"), ("Table counts, verified", "tables"),
         ("The three studios worth knowing", "studios"),
         ("Blackjack, roulette and baccarat online", "games"),
         ("Game shows: Crazy Time and the rest", "game-shows"),
         ("Stream quality on a New Zealand connection", "streaming"),
         ("Live casino and bonus wagering", "wagering"),
         ("Frequently asked questions", "faq")],
 "faq_h2": "Live casino NZ &mdash; frequently asked questions",
 "faq": [
  ("Which live casino is best for New Zealand players?",
   "<p>Spinjo has the largest floor we counted at over 400 tables, but Rooster Bet is our pick for most "
   "players: 320-plus tables with the full Evolution range plus genuine Pragmatic Live and Ezugi "
   "alternatives, on a NZD wallet with a three-hour median crypto payout. Ivibet is the specialist "
   "choice if blackjack variants are what you want.</p>"),
  ("Are live dealer games fair?",
   "<p>They are the most transparent product in an online casino, because you watch the physical "
   "shuffle and the physical wheel. Evolution, Pragmatic Live and Ezugi are all licensed and "
   "independently audited, and the tables are dealt from regulated studios in Latvia, Malta, Georgia "
   "and the Philippines. The house edge is the same as the land-based game &mdash; it is built into "
   "the rules, not the software.</p>"),
  ("What is the minimum bet at a live table?",
   "<p>NZ$0.50 to NZ$1 on roulette and NZ$1 to NZ$5 on blackjack at most of these sites. Evolution "
   "runs dedicated low-stakes tables and the game-show formats generally start at NZ$0.10 a spot. "
   "High-roller tables run to NZ$10,000 a hand at the larger floors.</p>"),
  ("Why are there fewer tables in the New Zealand morning?",
   "<p>Because the studios follow European demand. 9am in Auckland is 10pm in Riga, which is peak, so "
   "counts are usually good. It is mid-afternoon New Zealand time &mdash; the small hours in Europe "
   "&mdash; when thin floors show up. Evolution runs 24-hour auto tables that never close, which is why "
   "we check specifically for those.</p>"),
  ("Do live casino games count towards bonus wagering?",
   "<p>Usually at 10% or not at all, and this is the single biggest trap for live players. A 40x bonus "
   "at 10% contribution is an effective 400x. If live dealer is what you play, either decline the "
   "welcome bonus or pick a site that weights live games higher &mdash; check the terms, because it "
   "varies between operators and even between tables.</p>"),
  ("Can I play live casino on my phone?",
   "<p>Yes, and the experience is genuinely good now. Evolution&rsquo;s mobile interface reflows to a "
   "portrait layout with the table on top and the betting grid below. You will want a stable "
   "connection &mdash; live dealer is the most bandwidth-hungry thing in an online casino at roughly "
   "1.5&ndash;3 Mbps sustained.</p>"),
  ("What is the difference between Evolution and Ezugi?",
   "<p>Evolution is the market leader and owns Ezugi. Evolution tables are the premium product &mdash; "
   "higher production values, the game shows, the branded rooms. Ezugi runs leaner tables with lower "
   "minimums and a broader set of regional variants. A casino carrying both gives you more range at "
   "the bottom of the stake ladder.</p>"),
 ],
 "sections": [
  {"html": [h2("Table counts, verified", "tables"),
   "<p>Counted manually from an Auckland IP address at 9am NZST on a Tuesday in %s. &lsquo;Auto&rsquo; "
   "means tables that run without a human dealer and never close.</p>" % MONTH_YEAR,
   table(["Casino", "Total tables", "Blackjack", "Roulette", "Baccarat", "Game shows", "24h auto tables"], [
     ["Spinjo", "412", "78", "96", "64", "22", "Yes"],
     ["Kingdom", "356", "62", "84", "58", "19", "Yes"],
     ["Rooster Bet", "328", "58", "77", "52", "21", "Yes"],
     ["Fortune Play", "304", "51", "72", "48", "20", "Yes"],
     ["Ivibet", "301", "72", "66", "44", "14", "Yes"],
     ["Lucky Vibe", "274", "44", "63", "41", "16", "Yes"],
     ["MadCasino", "206", "33", "49", "31", "11", "Partial"],
   ], caption="Live dealer tables open at 9am NZST, counted from a New Zealand IP, %s" % MONTH_YEAR),
   note("<b>Why Ivibet punches above its weight.</b> It runs a 4,000-game casino and a 300-table live "
        "floor, which is an unusual ratio. Its 72 blackjack tables include variant coverage &mdash; "
        "Infinite, Free Bet, Power, Salon Priv&eacute; &mdash; that larger casinos do not match. If "
        "blackjack is your game, table count in the aggregate matters less than that.", "ok")]},

  {"html": [h2("The three studios worth knowing", "studios"),
   cards([
     ("EV", "Evolution Gaming", "Evolution Gaming casinos NZ players reach are the market standard, and "
      "the reason live casino works at all. Studios in Latvia, "
      "Malta, Georgia, Canada and the Philippines. Owns the game-show format outright &mdash; Crazy "
      "Time, Lightning Roulette, Monopoly Live. If a casino has no Evolution, its live floor is a "
      "compromise.", None),
     ("PL", "Pragmatic Play Live", "The serious challenger since 2019. Lower table minimums than "
      "Evolution, strong Mega Roulette and Sweet Bonanza Candyland products, and a cleaner mobile "
      "interface. Good breadth at the bottom of the stake ladder.", None),
     ("EZ", "Ezugi", "Evolution-owned, leaner and cheaper to run. Regional variants &mdash; Andar "
      "Bahar, Teen Patti, Russian Poker &mdash; and low minimums. A casino running Ezugi alongside "
      "Evolution has real range rather than duplicated tables.", None),
   ]),
   "<p>What you want to avoid is a live lobby built entirely on a fourth-tier white-label provider with "
   "a handful of tables and a stream that buffers. That is the difference between the 300-table floors "
   "above and the sites that did not make this page.</p>"]},

  {"html": [h2("Live roulette NZ, live blackjack NZ and live baccarat NZ", "table-by-table"),
   "<p>Three tables carry most of the traffic on any live floor, and they are very different products "
   "once you look past the presentation.</p>",

   h3("Live roulette NZ", "live-roulette"),
   "<p>The most played and the easiest to get wrong. Always take European single-zero over American "
   "double-zero: 2.70% house edge against 5.26%, for identical gameplay. The best live roulette site "
   "for a New Zealander is whichever carries the full Evolution range at a stake you want, because "
   "table minimums matter more than table count &mdash; live roulette NZ players can find starts at "
   "NZ$0.50 on Evolution&rsquo;s low-limit wheels and NZ$0.20 a spot on the game-show formats.</p>",

   h3("Live blackjack NZ", "live-blackjack"),
   "<p>The best-value game in any casino when played correctly: a house edge around 0.5% with basic "
   "strategy, against roughly 3.8% on a pokie. Live dealer blackjack online in NZ for real money runs "
   "from about NZ$1 a hand at Ezugi tables to NZ$10,000 in Salon Priv&eacute;. Ivibet carries 72 "
   "blackjack tables including Infinite, Free Bet and Power variants &mdash; unusual depth for a "
   "4,000-game casino. Avoid the side bets; they run 5&ndash;12% and undo the entire advantage.</p>",

   h3("Live baccarat NZ", "live-baccarat"),
   "<p>Simple, fast and cheaper than it looks. Live baccarat NZ tables give the banker bet a 1.06% "
   "house edge after commission, the player bet 1.24%, and the tie bet more than 14% &mdash; so bet "
   "banker, pay the commission and ignore the tie. Minimums start around NZ$1.</p>",

   h3("Crazy Time NZ, Lightning Roulette NZ and Monopoly Live NZ", "game-shows"),
   "<p>Evolution&rsquo;s game shows now take a large share of live traffic and they are entertainment "
   "products first. Crazy Time NZ players bet into a 3.4&ndash;5.9% edge depending on the segment, "
   "with the four number segments the cheapest and the bonus bets the most expensive. Lightning "
   "Roulette NZ adds 50x&ndash;500x multipliers funded by a slightly higher edge on straight-ups, at "
   "2.99% overall. Monopoly Live NZ runs 3.5&ndash;5.5%. In each case the bet that makes the game fun "
   "is the one that costs the most, which is a reasonable trade if you know you are making it.</p>"]},

  {"html": [h2("How does live casino work, and how it differs from RNG games", "how-it-works"),
   "<p>How does live casino work? A real dealer at a real table in a licensed studio &mdash; Evolution "
   "in Latvia, Malta, Georgia and the Philippines, Pragmatic Live and Ezugi elsewhere &mdash; is "
   "filmed by multiple cameras. Optical character recognition reads the physical cards and the "
   "physical wheel, and the result is pushed to your screen as data while the video streams alongside "
   "it. You are betting on a physical event, not a simulation.</p>",
   table(["", "Live casino", "RNG table games"], [
     ["Outcome source", "A physical wheel, shoe or deck you can watch", "A certified random number generator"],
     ["Speed", "30&ndash;60 seconds per round, dealer-paced", "As fast as you can click"],
     ["Minimum stake", "NZ$0.50&ndash;NZ$5 typical", "NZ$0.10&ndash;NZ$1 typical"],
     ["House edge", "Identical &mdash; it is in the rules, not the software", "Identical"],
     ["Bonus wagering contribution", "<b>Usually 10% or 0%</b>", "Usually 10%"],
     ["Bandwidth", "1.5&ndash;3 Mbps sustained", "Negligible"],
     ["Demo mode", "<b>Never</b>", "Usually available"],
   ], caption="Live casino vs RNG games: the differences that change what you should play"),
   "<p>The practical reading of live casino vs RNG games: the odds are the same, the pace and the cost "
   "of a mistake are not. RNG tables let you play basic strategy at your own speed for ten cents; live "
   "tables cost more per hour and are considerably more enjoyable. Neither is &lsquo;fairer&rsquo; than "
   "the other &mdash; both are independently audited.</p>",
   h3("Live casino with NZD tables, minimums and mobile", "nzd-mobile"),
   "<p>A live casino with NZD tables is not a separate product; it is an operator holding your balance "
   "in New Zealand dollars so no conversion happens when you sit down. Spinjo, Kingdom, Rooster Bet, "
   "Fortune Play, Lucky Vibe and MadCasino all do. The live casino minimum bet NZ players face depends "
   "on the studio rather than the operator &mdash; Ezugi and Pragmatic Live run cheaper tables than "
   "Evolution&rsquo;s branded rooms. There is no live casino app NZ players can download, because "
   "Apple and Google restrict real-money gambling apps here; Evolution&rsquo;s mobile interface "
   "reflows to portrait with the table above and the betting grid below, which works well on a phone "
   "provided you have a stable connection.</p>"]},

  {"html": [h2("Blackjack, roulette and baccarat online", "games"),
   table(["Game", "House edge", "Typical NZ minimum", "Skill matters?", "Notes for live play"], [
     ["Blackjack (basic strategy)", "0.5&ndash;0.7%", "NZ$1&ndash;5", "Yes, considerably",
      "The lowest house edge in the casino if you play correct basic strategy. Side bets destroy that &mdash; avoid them."],
     ["European roulette", "2.70%", "NZ$0.50", "No",
      "Single zero. Always choose this over American roulette."],
     ["American roulette", "5.26%", "NZ$0.50", "No",
      "Double zero nearly doubles the edge for no benefit. Never play it if European is on the floor."],
     ["Baccarat (banker)", "1.06%", "NZ$1", "No",
      "Bet banker, pay the commission, ignore the tie at 14%+ edge."],
     ["Casino hold&rsquo;em", "2.2%", "NZ$1", "Some", "Simple strategy improves the edge materially."],
     ["Lightning Roulette", "2.99%", "NZ$0.20", "No",
      "Multipliers up to 500x funded by a slightly higher edge on straight-ups."],
   ], caption="Live table games: house edge and minimums at NZ-facing casinos"),
   "<p>The single most valuable sentence on this page: live blackjack played with correct basic "
   "strategy has a house edge of around 0.5%, against roughly 4% on a typical pokie. If you want the "
   "longest possible session for a given bankroll, that is where it is.</p>"]},

  {"html": [h2("Game shows: Crazy Time and the rest", "game-shows"),
   "<p>Evolution&rsquo;s game-show formats now account for a large share of live traffic. They are "
   "entertainment products first &mdash; a presenter, a wheel, bonus rounds &mdash; and the house edge "
   "reflects that.</p>",
   table(["Game", "House edge", "Format", "Best bet"], [
     ["Crazy Time", "3.4&ndash;5.9%", "Money wheel with four bonus rounds", "The four number segments; bonus bets carry the higher edge"],
     ["Lightning Roulette", "2.99%", "Roulette with 50&ndash;500x multipliers", "Outside bets keep the standard 2.7% edge"],
     ["Monopoly Live", "3.5&ndash;5.5%", "Money wheel with a 3D bonus board", "The 1 and 2 segments"],
     ["Sweet Bonanza Candyland", "3.8&ndash;7.0%", "Pragmatic money wheel", "Low-multiplier segments"],
     ["Funky Time", "3.5&ndash;6.0%", "Evolution wheel with bonus games", "The number segments"],
   ], caption="Live game shows: house edge by bet type"),
   "<p>Note the range in every row. The edge depends entirely on which segment you back, and the bonus "
   "bets that make these games fun are always the expensive ones. That is a reasonable trade if you "
   "know you are making it.</p>"]},

  {"html": [h2("Stream quality on a New Zealand connection", "streaming"),
   "<p>Live dealer is the most bandwidth-intensive thing in an online casino: roughly 1.5 Mbps at "
   "standard quality and 3 Mbps at high definition, sustained. On a rural connection or congested 4G "
   "this is where sites fail.</p>",
   "<p>Every casino here lets you drop the stream quality manually, which is worth doing before the "
   "session rather than mid-hand. Evolution&rsquo;s adaptive bitrate handles a fluctuating connection "
   "better than Pragmatic Live does. If you regularly get a &lsquo;disconnected&rsquo; message during a "
   "hand, the house rules at every one of these operators are the same: the hand stands and is settled "
   "by the dealer, so you are not refunded.</p>",
   h3("Live casino and bonus wagering", "wagering"),
   "<p>The hard truth for live players. Live dealer games contribute 10% or 0% to wagering at almost "
   "every casino here. A NZ$200 bonus at 40x with live weighted at 10% requires NZ$80,000 of live "
   "turnover. It is not a bonus; it is a decoration.</p>",
   note("<b>If live dealer is what you play, decline the welcome bonus.</b> Take the cash, play the "
        "game with a 0.5% house edge instead of chasing a 400% effective requirement, and use cashback "
        "offers rather than match bonuses. Lucky Vibe&rsquo;s cash cashback is the most useful "
        "promotion on this site for a live player.", "warn")]},
 ],
}

# ===========================================================================
# FAST PAYOUT CASINOS
# ===========================================================================
FAST = {
 "path": "/fast-payout-casinos/",
 "crumbs": [("Fast payout casinos", None)],
 "author": "priya-raman", "checker": "jordan-whitcombe",
 "section_name": "Fast payout casinos",
 "title": "Fastest Payout Online Casinos NZ %s &mdash; Timed Results" % MONTH_YEAR,
 "desc": ("We timed %d withdrawals to the minute. The fastest paying online casinos for NZ players, "
          "with medians, worst cases and the reasons payouts get held." % N_WITHDRAWALS),
 "h1": "Fastest Payout Casinos NZ",
 "eyebrow": "%d withdrawals timed to the minute" % N_WITHDRAWALS,
 "lede": ("Every casino claims fast withdrawals. We measured them. This page publishes the median, the "
          "fastest and the slowest result for every operator we have cashed out from, the sample size "
          "behind each figure, and the four things that actually make a payout slow."),
 "stats": [("%d" % N_WITHDRAWALS, "Withdrawals timed"), ("11 min", "Fastest recorded"),
           ("2h 50m", "Best median: Kingdom"), ("14 h", "Median KYC approval")],
 "cta2": ("See the timing data", "#data"),
 "order": ["spino", "kingdom", "crownslots", "rooster-bet", "fortune-play", "smash",
           "spinjo", "rivo"],
 "notes": {
   "spino": "Fastest cashier we have ever timed: 11 minutes at best, no stated weekly cap. Crypto only.",
   "kingdom": "Median 2h 50m across seven timed crypto withdrawals, with a NZ$10,000 weekly ceiling.",
   "crownslots": "Our single fastest fiat-adjacent result at 68 minutes. Euro wallet, so price the FX.",
   "rooster-bet": "Median three hours across four tests, on a NZD wallet with a NZ$8,000 weekly cap.",
   "fortune-play": "Median 4h 10m on crypto and consistent e-wallet clearing inside 24 hours.",
   "smash": "Median 4h 30m with the joint-highest NZ$10,000 weekly cap.",
   "spinjo": "Median nine hours across six withdrawals &mdash; slower, but the most consistent.",
   "rivo": "Four-tap mobile cashout and 3&ndash;8 hour crypto processing.",
 },
 "rank_h2": "Fastest paying online casinos NZ &mdash; %s" % MONTH_YEAR,
 "rank_intro": ("The fast payout casinos NZ players can actually rely on, ranked on measured median "
                "time from clicking confirm to funds arriving, then adjusted for weekly cap, rail "
                "availability and how often a payout was held for manual review."),
 "intro": [
   "<p>&lsquo;Instant withdrawals&rsquo; is the most abused phrase in online gambling. It usually "
   "describes the moment an operator marks a request approved, not the moment money is available to "
   "you. So we stopped reading claims and started timing.</p>",
   "<p>Since April 2026 we have run %d withdrawals across %d operators, recording the exact time from "
   "clicking confirm to funds landing. Every figure below comes from that log. Where a sample is small "
   "we say so, because a single fast payout is an anecdote, not a benchmark.</p>"
   % (N_WITHDRAWALS, N_OPERATORS_TESTED)],
 "toc": [("Fastest payout casinos, ranked", "ranked"), ("The timing data", "data"),
         ("How long each rail really takes", "rails"),
         ("The four reasons a payout gets held", "delays"),
         ("Weekly caps: the term nobody reads", "caps"),
         ("How to get paid faster", "how-to"),
         ("Frequently asked questions", "faq")],
 "faq_h2": "Fast payout casinos NZ &mdash; frequently asked questions",
 "faq": [
  ("Which online casino pays out fastest in New Zealand?",
   "<p>Spino in absolute terms: our fastest recorded cashout anywhere was eleven minutes, and it has "
   "no published weekly cap. The qualification is that Spino is crypto-only, so it is unusable if you "
   "do not already hold cryptocurrency. For a casino you can fund with a card or a New Zealand bank "
   "transfer, Kingdom is the fastest at a median of two hours fifty minutes on crypto and "
   "six to twenty-four hours on e-wallets.</p>"),
  ("Are instant withdrawals real?",
   "<p>On crypto rails, close to it &mdash; settlement is a blockchain confirmation away once the "
   "operator approves. On cards and bank transfers, no. An operator can approve a card withdrawal in "
   "minutes and your bank will still take two to five business days to post it. Any site promising "
   "instant card withdrawals is describing its own approval step and hoping you conflate the two.</p>"),
  ("Why is my first withdrawal always slower?",
   "<p>Because it triggers identity verification. Every licensed operator must complete know-your-"
   "customer checks before releasing funds, and most do it at first withdrawal rather than at "
   "registration. Median approval across our tests was 14 hours; the worst was four days. Verify on "
   "the day you register and your first withdrawal behaves like your tenth.</p>"),
  ("Do casinos charge withdrawal fees?",
   "<p>The casinos on this page do not charge a direct fee on standard withdrawals. Costs arrive "
   "elsewhere: a blockchain network fee on crypto, an e-wallet&rsquo;s own fee to move money to your "
   "New Zealand bank, and a currency conversion spread at any casino that does not hold your balance "
   "in NZD. That last one is the biggest and the least visible.</p>"),
  ("What is a withdrawal cap and why does it matter?",
   "<p>A maximum you can withdraw per week or month regardless of your balance. Slotsgem caps at "
   "NZ$4,000 a week and Kingdom at NZ$10,000. If you won NZ$30,000 at a NZ$4,000 casino it would take "
   "almost two months to extract, during which the balance sits in the operator&rsquo;s account and is "
   "very easy to gamble back. Check the cap before the bonus.</p>"),
  ("Can a casino refuse to pay me?",
   "<p>Legitimately, yes, in defined circumstances: unverified identity, a bonus term breach such as "
   "exceeding the maximum bet, duplicate accounts, or third-party payment. Illegitimately, some sites "
   "stall. Your protection is the licence: a Cura&ccedil;ao Gaming Control Board licensee has a "
   "complaints process you can escalate to. An operator with no published licence number has none, "
   "which is precisely why we rank Roby Casino where we do.</p>"),
  ("Is crypto really faster, or does it just feel faster?",
   "<p>It is genuinely faster, by a large margin, and our data is unambiguous: a median of roughly "
   "three hours on crypto against twelve to twenty-four on e-wallets and one to five business days on "
   "cards. The reason is that crypto skips the card networks and correspondent banking entirely. The "
   "cost is exchange-rate exposure between the coin and the New Zealand dollar, which you carry.</p>"),
 ],
 "cta_band": ("Fast payouts are worth nothing if the site will not pay",
              "Our trust and disclosure scoring covers licence verification, corporate transparency "
              "and complaints handling.",
              [("How we review", "/how-we-rate-casinos/"), ("Payment methods", "/casino-payment-methods/")]),
 "sections": [
  {"html": [h2("The timing data", "data"),
   "<p>Median, fastest and slowest result per operator, with the sample size. All times are from "
   "clicking confirm to funds available, not to the operator marking the request approved.</p>",
   table(["Casino", "Rail tested", "Withdrawals timed", "Median", "Fastest", "Slowest", "Held for review"], [
     ["Spino", "USDT / BTC", "5", "<b>38 min</b>", "11 min", "1h 54m", "0"],
     ["Kingdom", "USDT / BTC", "7", "<b>2h 50m</b>", "1h 12m", "6h 20m", "0"],
     ["Rooster Bet", "USDT", "4", "<b>3h 00m</b>", "1h 40m", "5h 50m", "0"],
     ["CrownSlots", "USDT", "3", "<b>3h 20m</b>", "1h 08m", "6h 05m", "0"],
     ["Fortune Play", "USDT", "3", "<b>4h 10m</b>", "2h 15m", "7h 40m", "0"],
     ["Smash", "USDT", "3", "<b>4h 30m</b>", "3h 05m", "7h 55m", "0"],
     ["Rivo", "USDT", "3", "<b>5h 15m</b>", "3h 20m", "8h 10m", "0"],
     ["Spinjo", "NZD bank / Skrill", "6", "<b>9h 00m</b>", "4h 10m", "26h", "1"],
     ["Lucky Vibe", "Skrill", "3", "<b>13h</b>", "8h 30m", "23h", "0"],
     ["Ivibet", "Skrill", "3", "<b>16h</b>", "9h 45m", "4d 2h", "1"],
     ["Hellspin", "Skrill", "2", "<b>18h</b>", "12h", "27h", "0"],
     ["Slotsgem", "USDT", "2", "<b>21h</b>", "14h 30m", "28h", "0"],
     ["Roby Casino", "USDT", "3", "<b>31h</b>", "19h", "3d 4h", "2"],
   ], caption="Measured withdrawal times, April&ndash;%s %s. Sample sizes are small by design &mdash; "
              "we publish them rather than hide them." % (MONTH, YEAR)),
   note("<b>Read the sample size column.</b> A two-withdrawal sample is indicative, not conclusive. We "
        "publish it because a median with no n is marketing. Kingdom&rsquo;s position is the most "
        "robust figure on this page at seven timed withdrawals with no held requests.", "info")]},

  {"html": [h2("How long do casino withdrawals take in NZ?", "how-long"),
   "<p>The short answer, from our own log rather than from operator marketing: between eleven minutes "
   "and five business days, and which end you land on is decided almost entirely by the rail you "
   "chose and whether your identity was already verified.</p>",
   "<p>Withdrawal times at online casinos in NZ break into two parts that get conflated constantly. "
   "The first is the operator&rsquo;s approval queue, which is where nearly all the variance lives. "
   "The second is settlement, which is fast on crypto and slow on cards. When a site advertises an "
   "instant payout casino experience it is describing the first part finishing, not the money "
   "arriving in your account.</p>",
   table(["Question", "Honest answer"], [
     ["How long do casino withdrawals take in NZ on crypto?",
      "<b>30 minutes to 8 hours.</b> Our median across all crypto-capable sites here is about three hours."],
     ["On an e-wallet?", "<b>4 to 24 hours.</b> The fastest reliable fiat route."],
     ["On a NZD bank transfer?", "<b>1 to 3 business days</b> after approval."],
     ["On a card?", "<b>2 to 5 business days.</b> Your bank controls the back half of that."],
     ["Is a same day payout casino NZ players can rely on realistic?",
      "On crypto and e-wallets, yes, routinely. On a card, no &mdash; regardless of what is advertised."],
     ["What is the fastest paying online casino NZ has?",
      "Spino at eleven minutes for our quickest cashout, crypto only. Kingdom at a 2h 50m median with a fiat option."],
   ], caption="Withdrawal times at online casinos in NZ, from our timing log"),
   h3("Why is my casino withdrawal pending?", "pending"),
   "<p>The most searched question in this category, and it almost always has a mundane answer. Casino "
   "withdrawal pending time in NZ stretches for one of five reasons, in order of how often we see "
   "them:</p>",
   "<ul>"
   "<li><b>Identity verification is incomplete.</b> Median approval in our testing was 14 hours, and "
   "it blocks everything behind it. This is the one you can eliminate entirely by verifying on the "
   "day you register.</li>"
   "<li><b>You are cashing out to a method you did not deposit with.</b> Anti-money-laundering rules "
   "require the original rail to be reversed first, up to the amount deposited. Switching triggers a "
   "manual review.</li>"
   "<li><b>A bonus is still active</b>, or an automated system has flagged a maximum-bet breach during "
   "wagering. Check the wagering meter rather than your memory.</li>"
   "<li><b>The request exceeds the weekly cap.</b> It should be split rather than cancelled; if it is "
   "cancelled with no message, ask in writing.</li>"
   "<li><b>A large win relative to your deposit history.</b> A first-ever NZ$8,000 cashout on an "
   "account that has deposited NZ$150 will be reviewed anywhere. That is a legitimate control, and it "
   "typically adds 24 to 72 hours.</li></ul>",
   note("<b>A fast payout casino NZ players can use with no verification delay is a myth &mdash; but "
        "you can remove the delay yourself.</b> Upload ID and proof of address the day you register. "
        "It converts your first withdrawal into an ordinary one and is the single most effective "
        "thing on this page.", "ok")]},

  {"html": [h2("Instant withdrawal casino NZ: what the phrase actually means", "instant"),
   "<p>&lsquo;Instant&rsquo; is the most abused word in this market, so it is worth separating what is "
   "achievable from what is advertising.</p>",
   table(["Claim", "What is actually true", "Realistic expectation"], [
     ["Instant withdrawal casino NZ, crypto",
      "Settlement is minutes once approved; approval is the variable",
      "<b>11 minutes to 8 hours</b> end to end"],
     ["Instant withdrawal casino NZ, bank transfer",
      "No New Zealand bank settles a gambling payout instantly",
      "1&ndash;3 business days after approval"],
     ["Instant payout casino NZ, card",
      "Describes the operator marking the request approved",
      "2&ndash;5 business days to post"],
     ["A quick withdrawal casino NZ with a low weekly cap",
      "Speed per request says nothing about total throughput",
      "Check the cap before the bonus"],
     ["Casinos with fast withdrawals NZ and no KYC",
      "Every licensed operator must verify before releasing funds",
      "Verify on day one instead"],
   ], caption="Instant withdrawal claims against measured reality"),
   "<p>The practical conclusion: if payout speed is what you are buying, hold a small USDT balance for "
   "casino use. That single change is the difference between a Friday-night win arriving on Saturday "
   "morning and arriving the following Wednesday, and it is available at twelve of the sixteen "
   "casinos we list.</p>"]},

  {"html": [h2("How long each rail really takes", "rails"),
   table(["Method", "Operator approval", "Settlement", "Total realistic", "Cost to you"], [
     ["Bitcoin / USDT / ETH", "10 min &ndash; 4 h", "2&ndash;30 min", "<b>30 min &ndash; 8 h</b>",
      "Network fee, plus FX when you convert to NZD"],
     ["Skrill / Neteller", "1&ndash;12 h", "Instant to the wallet", "<b>4&ndash;24 h</b>",
      "The wallet&rsquo;s own fee to move funds to a NZ bank"],
     ["MiFinity", "2&ndash;12 h", "Instant to the wallet", "<b>8&ndash;24 h</b>", "Wallet withdrawal fee"],
     ["Jeton", "2&ndash;12 h", "Instant to the wallet", "<b>8&ndash;24 h</b>", "Wallet withdrawal fee"],
     ["NZD bank transfer", "2&ndash;24 h", "1&ndash;3 business days", "<b>1&ndash;3 business days</b>",
      "Usually free. No FX if the wallet is NZD"],
     ["Visa / Mastercard", "2&ndash;24 h", "2&ndash;5 business days", "<b>2&ndash;5 business days</b>",
      "Possible FX on a non-NZD wallet"],
     ["Neosurf / Paysafecard", "&mdash;", "&mdash;", "<b>Not available</b>",
      "Deposit only &mdash; you need a second method"],
   ], caption="Realistic withdrawal timelines for New Zealand players"),
   "<p>The practical consequence: if payout speed is your priority, hold a small amount of USDT for "
   "casino use. It is the difference between a Friday-night win arriving Saturday morning and arriving "
   "the following Wednesday.</p>"]},

  {"html": [h2("The four reasons a payout gets held", "delays"),
   steps([
     ("Identity verification not completed",
      "By far the largest cause, and entirely avoidable. Upload ID and proof of address on the day you "
      "register. Median approval in our testing was 14 hours, so doing it up front removes it from the "
      "critical path completely."),
     ("Withdrawing to a different method than you deposited with",
      "Anti-money-laundering rules require operators to return funds down the original rail first, up "
      "to the deposited amount. Requesting a new method triggers manual review and adds one to three "
      "days. Plan your exit rail before you deposit."),
     ("An active bonus, or a suspected bonus breach",
      "You cannot withdraw with wagering outstanding at most operators, and an automated maximum-bet "
      "breach flag will stop a payout even if the breach was accidental. Check your bonus status in "
      "account settings before requesting."),
     ("A large win relative to your deposit history",
      "A first-ever NZ$8,000 withdrawal on an account that has deposited NZ$150 total will be reviewed "
      "at every operator here. That is a legitimate control, not a stall, and it typically adds 24 to "
      "72 hours. Source-of-funds documentation may be requested above roughly NZ$5,000."),
   ])]},

  {"html": [h2("Weekly caps: the term nobody reads", "caps"),
   "<p>A weekly withdrawal cap is the most under-appreciated term in online gambling. It does not stop "
   "you being paid; it rations how fast, and while the balance sits in your casino account it is "
   "extremely easy to gamble back. Several operators here advertise five-figure bonuses against "
   "four-figure weekly caps.</p>",
   table(["Casino", "Weekly cap", "Max advertised bonus", "Weeks to extract the maximum"], [
     ["Kingdom", "NZ$10,000", "NZ$18,500", "2"],
     ["Smash", "NZ$10,000", "NZ$19,500", "2"],
     ["Spinjo", "NZ$8,000", "NZ$5,000", "1"],
     ["Rooster Bet", "NZ$8,000", "NZ$5,000", "1"],
     ["Rivo", "NZ$8,000", "NZ$4,500", "1"],
     ["Fortune Play", "NZ$7,000", "NZ$5,000", "1"],
     ["CrownSlots", "&euro;5,000 (&asymp;NZ$9,800)", "NZ$7,250", "1"],
     ["Roby Casino", "NZ$5,000", "NZ$5,000", "1&ndash;2, at 31h per request"],
     ["Slotsgem", "NZ$4,000", "NZ$400", "1"],
     ["Spino", "None published", "2,000 USDT", "&mdash;"],
   ], caption="Weekly withdrawal caps against maximum advertised bonus"),
   note("<b>The pattern to look for.</b> A cap comfortably above the maximum bonus is a site that "
        "expects to pay. A cap at or below it is a site that has priced the delay into its model. "
        "Kingdom and Smash are the two clearest examples of the former.", "ok")]},

  {"html": [h2("How to get paid faster", "how-to"),
   "<ul>"
   "<li><b>Verify on day one.</b> Removes the single largest delay before it can happen.</li>"
   "<li><b>Deposit and withdraw on the same rail.</b> Avoids the AML review that a new method triggers.</li>"
   "<li><b>Hold a small USDT balance for casino use.</b> Three hours versus three days is the "
   "difference crypto makes, and you do not need to be a crypto enthusiast to use it for this.</li>"
   "<li><b>Do not deposit with a voucher if you plan to win.</b> Neosurf and Paysafecard cannot pay out, "
   "so you will be setting up a second method under pressure.</li>"
   "<li><b>Clear or forfeit the bonus before requesting.</b> Check the wagering meter, not your memory.</li>"
   "<li><b>Withdraw in amounts that fit the weekly cap.</b> Two requests inside the cap clear faster "
   "than one that exceeds it and gets split by the operator.</li>"
   "<li><b>Request on a weekday morning NZST.</b> That is late evening in Europe where most of these "
   "finance teams sit; weekend requests consistently took longer in our log.</li></ul>"]},
 ],
}

# ===========================================================================
# HIGH PAYOUT CASINOS
# ===========================================================================
HIGH = {
 "path": "/casino-payout-percentages/",
 "crumbs": [("High payout casinos", None)],
 "author": "sam-kavanagh", "checker": "priya-raman",
 "section_name": "High payout casinos",
 "title": "Highest Payout Online Casinos NZ %s &mdash; Best RTP Sites" % MONTH_YEAR,
 "desc": ("Which NZ online casinos actually run games at the studio&rsquo;s intended RTP? We sampled "
          "ten titles per operator and published the configurations we found."),
 "h1": "Highest Payout Casinos NZ",
 "eyebrow": "RTP configurations sampled &middot; %s" % MONTH_YEAR,
 "lede": ("&lsquo;High payout&rsquo; usually means nothing. Here it means something specific: we "
          "sampled ten popular titles at each casino and checked whether the return-to-player "
          "configuration matched the studio&rsquo;s default or a reduced build. These are the casinos "
          "that did not quietly turn the games down."),
 "stats": [("10", "Titles sampled per site"), ("96.5%", "Best verified config"),
           ("92%", "Worst config found"), ("0.5%", "House edge, live blackjack")],
 "cta2": ("RTP findings", "#findings"),
 "order": ["spinjo", "rooster-bet", "kingdom", "fortune-play", "ivibet", "rivo", "lucky-vibe"],
 "notes": {
   "spinjo": "Ten of ten sampled titles ran at the studio&rsquo;s default RTP &mdash; the only clean sheet here.",
   "rooster-bet": "Ten of ten at default, plus a 328-table live floor where blackjack sits at a 0.5% edge.",
   "kingdom": "Nine of ten at default, with the widest jackpot network coverage on this site.",
   "fortune-play": "Nine of ten at default and the deepest bonus-buy range, where RTP runs slightly higher.",
   "ivibet": "The live-first pick: 72 blackjack tables, where correct basic strategy beats any pokie RTP.",
   "rivo": "Eight of ten at default. Mid-table on configuration, strong on everything else.",
   "lucky-vibe": "Cashback paid as withdrawable cash, which raises effective return more than 0.5% of RTP does.",
 },
 "rank_h2": "Highest payout online casinos NZ &mdash; %s" % MONTH_YEAR,
 "rank_intro": ("The highest RTP casinos NZ players can reach, ranked on verified configuration "
                "across a ten-title sample, the availability of genuinely low-edge games, and whether "
                "promotional value arrives as cash or as more wagering."),
 "intro": [
   "<p>Most pages chasing casino payout percentage quote a single number &mdash; 97.3%, 96.8% &mdash; "
   "with no source. There is no such figure. A casino does not have one RTP; individual games do, and "
   "an operator can often choose between several builds of the same game. That is why picking the "
   "best payout online casino NZ has to offer starts with configuration, not with a badge.</p>",
   "<p>So we did the only thing that produces a real answer: opened ten popular titles at each casino, "
   "read the RTP from the in-game paytable, and compared it to the studio&rsquo;s default. That table "
   "is below, and it is the most useful thing on this page.</p>"],
 "toc": [("Highest payout casinos, ranked", "ranked"), ("What we found in the RTP sample", "findings"),
         ("Where the real edge is: game by game", "edges"),
         ("Why a casino would run a lower RTP build", "why"),
         ("Jackpots and the RTP trade-off", "jackpots"),
         ("Payout percentage versus payout speed", "speed"),
         ("Frequently asked questions", "faq")],
 "faq_h2": "High payout casinos NZ &mdash; frequently asked questions",
 "faq": [
  ("Which is the best payout online casino NZ players can use?",
   "<p>On our sample, Spinjo and Rooster Bet: both ran ten out of ten sampled titles at the "
   "studio&rsquo;s default RTP configuration. That is the honest answer to the question. There is no "
   "single site-wide payout percentage &mdash; any page quoting one to two decimal places has made it "
   "up or copied it from an operator&rsquo;s own marketing.</p>"),
  ("What is a good payout percentage for an online casino?",
   "<p>For pokies, 96% or higher per title. For live blackjack played with basic strategy, around "
   "99.5%. For European roulette, 97.3%. The aggregate across a casino depends entirely on what you "
   "play, which is why the game-level table on this page is more useful than any site-level number.</p>"),
  ("How can I check a game&rsquo;s RTP myself?",
   "<p>Open the game, tap the menu or information icon, and find the paytable or game rules. The "
   "return to player is stated there for the exact build you are playing. It takes about ten seconds "
   "and it is the only reliable source &mdash; including compared with this page, because operators "
   "can change configurations at any time.</p>"),
  ("Do higher RTP games pay out more often?",
   "<p>Not necessarily. RTP is total return over the long run; volatility is how it arrives. A 96% "
   "low-volatility pokie pays small amounts frequently, and a 96% extreme-volatility pokie returns the "
   "same proportion in rare large hits. For making a bankroll last, volatility matters more than a "
   "half-point of RTP.</p>"),
  ("Is live blackjack really the best-value game in a casino?",
   "<p>On house edge, yes, and it is not close. Correct basic strategy on a standard live blackjack "
   "table gives a house edge of roughly 0.5%, against about 4% on a typical pokie &mdash; eight times "
   "cheaper per dollar wagered. Two caveats: side bets carry edges of 5&ndash;12% and undo the "
   "advantage entirely, and live games usually contribute 10% or less to bonus wagering.</p>"),
  ("Does a welcome bonus raise my effective payout?",
   "<p>Only if you can clear it. A bonus with a 40x requirement typically costs more in expected "
   "losses generating the turnover than the bonus is worth. A 10x requirement, like Smash&rsquo;s, "
   "genuinely does raise expected return. Cashback that credits as cash &mdash; Lucky Vibe &mdash; "
   "raises it unconditionally, which is why it appears on this page.</p>"),
 ],
 "sections": [
  {"html": [h2("What we found in the RTP sample", "findings"),
   "<p>Ten titles per casino, each checked in the in-game paytable from a New Zealand account. "
   "&lsquo;Default&rsquo; means the configuration the studio ships as standard.</p>",
   table(["Casino", "At default RTP", "Reduced build", "Lowest build found", "Titles affected"], [
     ["Spinjo", "10 / 10", "0", "&mdash;", "None"],
     ["Rooster Bet", "10 / 10", "0", "&mdash;", "None"],
     ["Kingdom", "9 / 10", "1", "94.5%", "Big Bass Bonanza"],
     ["Fortune Play", "9 / 10", "1", "94.5%", "Gates of Olympus"],
     ["Rivo", "8 / 10", "2", "94.0%", "Starburst, Big Bass Bonanza"],
     ["Lucky Vibe", "8 / 10", "2", "94.5%", "Book of Dead, Sweet Bonanza"],
     ["Hellspin", "8 / 10", "2", "94.0%", "Starburst, Reactoonz"],
     ["Slotsgem", "8 / 10", "2", "92.0%", "Book of Dead, Big Bass Bonanza"],
   ], caption="RTP configuration sample: ten popular titles per casino, %s" % MONTH_YEAR),
   note("<b>What a reduced build costs you.</b> Playing Book of Dead at 92% instead of 96.2% turns an "
        "expected loss of NZ$3.80 per NZ$100 wagered into NZ$8.00. Over a year of moderate play that "
        "is a larger number than any welcome bonus on this site. Check the paytable.", "warn")]},

  {"html": [h2("Where the real edge is: game by game", "edges"),
   "<p>The spread between the best and worst games in a casino is far larger than the spread between "
   "casinos. This table is the most valuable thing on the page for a player who wants their money to "
   "last.</p>",
   table(["Game", "Typical RTP", "House edge", "Cost per NZ$100 wagered", "Available at"], [
     ["Live blackjack, basic strategy", "99.5%", "0.5%", "<b>NZ$0.50</b>", "All live casinos here"],
     ["Baccarat, banker bet", "98.94%", "1.06%", "<b>NZ$1.06</b>", "All live casinos here"],
     ["Video poker, 9/6 Jacks or Better", "99.54%", "0.46%", "<b>NZ$0.46</b>", "Spinjo, Kingdom, Rooster Bet"],
     ["European roulette", "97.30%", "2.70%", "<b>NZ$2.70</b>", "All"],
     ["Lightning Roulette", "97.01%", "2.99%", "<b>NZ$2.99</b>", "All Evolution floors"],
     ["Pokies, good configuration", "96.0&ndash;96.5%", "3.5&ndash;4.0%", "<b>NZ$3.75</b>", "All"],
     ["Crazy Time, number segments", "96.6%", "3.4%", "<b>NZ$3.40</b>", "All Evolution floors"],
     ["Pokies, reduced configuration", "92.0&ndash;94.5%", "5.5&ndash;8.0%", "<b>NZ$6.75</b>", "Varies &mdash; check the paytable"],
     ["American roulette", "94.74%", "5.26%", "<b>NZ$5.26</b>", "Avoid where European exists"],
     ["Blackjack side bets", "88&ndash;95%", "5&ndash;12%", "<b>NZ$8.50</b>", "Avoid"],
   ], caption="Expected cost per NZ$100 wagered, by game"),
   "<p>Read the top and bottom rows together. The same NZ$100 of turnover costs fifty cents at a live "
   "blackjack table played correctly and eight dollars fifty on a blackjack side bet. No difference in "
   "casino choice comes close to that.</p>"]},

  {"html": [h2("Why a casino would run a lower RTP build", "why"),
   "<p>It is not a conspiracy and it is not hidden &mdash; the figure is in the paytable. Studios "
   "offer multiple configurations because operators in different markets have different margin "
   "requirements, and a site running large bonuses often funds them by taking a point or two off the "
   "base game. Slotsgem is the clearest example on this site: a small bonus, a calm interface, and two "
   "of ten sampled titles on reduced builds.</p>",
   h3("Jackpots and the RTP trade-off", "jackpots"),
   "<p>Networked progressive jackpots fund their pools by skimming every bet, so base-game RTP on a "
   "jackpot title typically sits one to two points below an equivalent non-jackpot pokie. The headline "
   "return is restored only if you include the jackpot itself, which almost nobody wins. If your goal "
   "is session length, avoid jackpots; if your goal is a lottery ticket, know that is what you bought. "
   "Kingdom carries the widest jackpot coverage here across the Pragmatic, Red Tiger and Microgaming "
   "networks.</p>"]},

  {"html": [h2("RTP meaning: casino payout percentages explained", "rtp-meaning"),
   "<p>Return to player is the single most misunderstood number in this industry, so before the "
   "rankings, the plain-English version. The RTP meaning a casino relies on is simple: it is the "
   "proportion of everything staked on a game that the game returns to players over its lifetime.</p>",

   h3("What is RTP in pokies?", "what-is-rtp"),
   "<p>What is RTP in pokies in practice? A 96.5% title is expected to return NZ$96.50 of every "
   "NZ$100 wagered across millions of spins. It says nothing about your session, and the average "
   "includes the 5,000x win somebody else collected. Return to player explained honestly is a "
   "statement about the game&rsquo;s long-run maths, not a forecast of your afternoon.</p>",

   h3("How is casino RTP calculated?", "how-calculated"),
   "<p>The studio calculates it from the paytable and the reel weightings, then an independent "
   "laboratory &mdash; eCOGRA, iTech Labs or GLI &mdash; simulates the game across billions of "
   "rounds and certifies that the observed return matches the stated one. That certificate covers "
   "the <em>build</em> that was tested, which is why the configuration an operator installs matters "
   "as much as the headline figure.</p>",

   h3("What is a good RTP percentage?", "good-rtp"),
   "<p>For pokies, 96% or higher per title. Between 94% and 96% you are paying a noticeable premium; "
   "below 94% you are paying a large one. The average RTP at an online casino in NZ across a "
   "mainstream lobby lands around 96.2%, which is roughly double the return of a New Zealand pub "
   "machine. Payout rates at online casinos in New Zealand are not regulated here &mdash; they are "
   "set by the studio and chosen by the operator.</p>",

   h3("House edge vs RTP", "house-edge"),
   "<p>They are the same fact stated from opposite ends. House edge vs RTP is simply 100% minus the "
   "other: a 96.5% pokie has a 3.5% house edge. Casino people quote edge, game people quote RTP, and "
   "the reason it matters is that edge is easier to convert into money &mdash; a 3.5% edge costs you "
   "NZ$3.50 per NZ$100 wagered, on average, for as long as you keep wagering.</p>",

   h3("Does RTP matter in the short term?", "short-term"),
   "<p>Barely. Over a hundred spins, variance swamps it completely &mdash; you can lose on a 97% game "
   "and win on a 92% one, and most sessions do exactly that. Where RTP matters is cumulative: across "
   "a year of regular play the difference between a 96.2% build and a 92% build of the same title is "
   "a larger number than any welcome bonus in this market. It is a slow tax, not a dice roll.</p>",

   h3("Blackjack RTP vs pokies RTP", "blackjack-vs-pokies"),
   "<p>The comparison almost nobody makes, and the most valuable one on this page. Blackjack RTP vs "
   "pokies RTP is roughly 99.5% against 96.2% when basic strategy is played correctly &mdash; a house "
   "edge of 0.5% against 3.8%, or about eight times cheaper per dollar staked. Two caveats: side bets "
   "carry edges of 5&ndash;12% and destroy the advantage entirely, and live tables usually contribute "
   "10% or less towards bonus wagering.</p>"]},

  {"html": [h2("Highest RTP casinos NZ and the highest RTP pokies NZ players can find", "highest-rtp"),
   "<p>Which online casino has the best payout in NZ is really two questions: which operator runs "
   "games at the setting the studio intended, and which games you then choose. The highest RTP casinos "
   "NZ players can reach are the ones that answer the first question honestly.</p>",
   table(["Title", "Studio", "Default RTP", "Lowest build seen", "Where we found the default"], [
     ["Book of 99", "Relax Gaming", "<b>99.0%</b>", "99.0%", "Spinjo, Rooster Bet, Kingdom"],
     ["Blood Suckers", "NetEnt", "<b>98.0%</b>", "96.0%", "Spinjo, Rooster Bet"],
     ["Starmania", "NextGen", "<b>97.9%</b>", "95.4%", "Spinjo, Kingdom"],
     ["White Rabbit Megaways", "Big Time Gaming", "<b>97.7%</b>", "96.2%", "Spinjo, Rooster Bet, Kingdom"],
     ["Medusa Megaways", "NextGen", "<b>97.6%</b>", "96.0%", "Rooster Bet"],
     ["Starburst", "NetEnt", "96.1%", "94.0%", "Spinjo, Rooster Bet, Fortune Play"],
     ["Book of Dead", "Play&rsquo;n GO", "96.2%", "<b>92.0%</b>", "Spinjo, Rooster Bet, Kingdom"],
     ["Big Bass Bonanza", "Pragmatic Play", "96.7%", "94.5%", "Spinjo, Rooster Bet"],
   ], caption="Best RTP slots NZ players can reach, and the reduced builds we found in the same market"),
   "<p>Read the last two columns together. The highest RTP pokies NZ lobbies carry are not obscure "
   "titles &mdash; Book of 99 at 99.0% and Blood Suckers at 98.0% sit in the same lobbies as the "
   "games everyone plays. What varies is whether the operator installed the studio&rsquo;s default. "
   "The loosest online pokies NZ players can find are simply the high-default titles at a casino that "
   "has not turned them down.</p>",
   note("<b>The highest paying online casino NZ shortlist.</b> On our ten-title sample, Spinjo and "
        "Rooster Bet ran every game at the studio default. That, rather than any advertised "
        "site-wide online casino payout percentage NZ figure, is the closest thing to a real answer "
        "&mdash; and any page quoting a casino-wide payout percentage to two decimal places has "
        "either invented it or copied it from the operator.", "ok")]},

  {"html": [h2("Payout percentage versus payout speed", "speed"),
   "<p>These are different things and players conflate them constantly. Payout percentage is how much "
   "of your turnover comes back over time. Payout speed is how long the money takes to reach your bank "
   "once you have won it. A casino can be excellent at one and poor at the other.</p>",
   table(["Casino", "RTP sample result", "Median payout time", "Best for"], [
     ["Spinjo", "10/10 at default", "9h 00m", "Return &mdash; the cleanest configurations we found"],
     ["Rooster Bet", "10/10 at default", "3h 00m", "<b>Both</b> &mdash; clean RTP and a fast cashier"],
     ["Kingdom", "9/10 at default", "2h 50m", "Speed, with near-clean configuration"],
     ["Spino", "Not sampled &mdash; small lobby", "38 min", "Speed only"],
     ["Slotsgem", "8/10 at default", "21h", "Neither &mdash; listed for its interface, not its maths"],
   ], caption="Return versus speed, side by side"),
   "<p>Rooster Bet is the site that does both, which is why it appears near the top of four different "
   "pages on this website. If you want one account and you do not want to think about this again, that "
   "is the one.</p>"]},
 ],
}

# ===========================================================================
# CRYPTO CASINOS
# ===========================================================================
CRYPTO = {
 "path": "/crypto-casinos-nz/",
 "crumbs": [("Crypto casinos", None)],
 "author": "priya-raman", "checker": "jordan-whitcombe",
 "section_name": "Crypto casinos",
 "title": "Best Crypto Casinos NZ %s &mdash; Bitcoin &amp; USDT Sites" % MONTH_YEAR,
 "desc": ("Crypto casinos for New Zealand players: which coins are accepted where, real settlement "
          "times, zero-wagering offers and what the tax position actually is."),
 "h1": "Best Crypto Casinos NZ",
 "eyebrow": "Eight rails compared &middot; %s" % MONTH_YEAR,
 "lede": ("Bitcoin gambling NZ players do is mostly a payments decision, not a games decision. "
          "Cryptocurrency is the fastest way to move money in and out of an online casino from New "
          "Zealand &mdash; a median of about three hours against one to five business days on a card. "
          "This page covers which coins work where, what the real settlement times are, and the two "
          "costs nobody mentions."),
 "stats": [("11 min", "Fastest crypto cashout"), ("0x", "Lowest wagering: Spino"),
           ("8", "Coins supported at Spino"), ("18", "Casinos accepting crypto")],
 "cta2": ("Coin support table", "#coins"),
 "order": ["spino", "kingdom", "crownslots", "smash", "rooster-bet", "fortune-play", "spinjo"],
 "notes": {
   "spino": "0x wagering, eight coins, an eleven-minute fastest cashout and no published weekly cap. Crypto only.",
   "kingdom": "Eleven rails including Dogecoin, a 2h 50m median and a NZ$10,000 weekly ceiling.",
   "crownslots": "Four coins with our fastest single recorded cashout at 68 minutes. Euro-denominated.",
   "smash": "Crypto plus a 10x wagering requirement &mdash; the best combination of speed and clearable bonus.",
   "rooster-bet": "BTC, ETH and USDT on a NZD-capable account, median three hours.",
   "fortune-play": "Crypto rails alongside the deepest crash and instant-win shelf on this site.",
   "spinjo": "Four coins, but the reason to be here is that it also holds a true NZD balance.",
 },
 "rank_h2": "Best Bitcoin and crypto casinos NZ &mdash; %s" % MONTH_YEAR,
 "rank_intro": ("The best crypto casino NZ options, ranked on coin coverage, measured settlement "
                "times, the wagering attached to any crypto casino welcome bonus NZ players can "
                "claim, and whether the site also leaves you a fiat escape route."),
 "intro": [
   "<p>The case for a crypto casino NZ players can use is narrow and strong: it is dramatically "
   "faster in both directions, it sidesteps banks that decline gambling merchant codes, and it "
   "removes the foreign-exchange spread a euro-denominated site charges twice. Crypto casinos in New "
   "Zealand are also where the zero-wagering offers live, because the cost of funds is lower.</p>",
   "<p>The case against is equally clear. You carry the exchange-rate risk between the coin and the "
   "New Zealand dollar, a mistyped wallet address is unrecoverable, and buying crypto on a New Zealand "
   "exchange has its own fees and its own tax consequences. Both sides are below.</p>"],
 "toc": [("Best crypto casinos, ranked", "ranked"), ("Which coins work where", "coins"),
         ("Stablecoins versus Bitcoin", "stablecoins"),
         ("Real settlement times and network fees", "settlement"),
         ("Buying crypto in New Zealand", "buying"),
         ("Tax: what actually applies", "tax"),
         ("The risks, stated plainly", "risks"),
         ("Frequently asked questions", "faq")],
 "faq_h2": "Crypto casinos NZ &mdash; frequently asked questions",
 "faq": [
  ("Are crypto casinos legal in NZ?",
   "<p>Yes. Crypto casinos in New Zealand sit in exactly the same position as any other offshore "
   "operator: there is no law prohibiting a person from using cryptocurrency to gamble at an "
   "overseas site, and the Online Casino Gambling Act 2026 regulates operators rather than the "
   "payment method a player chooses. Licensed New Zealand operators from 2027 will be subject to the "
   "credit-card ban and the other payment rules in the regulations, but that is a restriction on "
   "them, not on you.</p>"),
  ("Which cryptocurrency is best for online casinos?",
   "<p>USDT (Tether) on the Tron network, for most people. It is a stablecoin pegged to the US dollar, "
   "so a win does not shrink between the cashout and the conversion, and Tron network fees are "
   "typically under a dollar. Bitcoin is universally accepted but volatile and slower; Litecoin and "
   "Dogecoin are cheap and fast but supported at fewer sites.</p>"),
  ("Do I pay tax on crypto casino winnings in New Zealand?",
   "<p>Two separate questions with two different answers. Gambling winnings themselves are not taxable "
   "for a recreational player. However, Inland Revenue treats cryptocurrency as property, and disposing "
   "of it &mdash; including converting it back to New Zealand dollars &mdash; can create a taxable "
   "gain or loss if you acquired it with the purpose of disposal. Buying USDT specifically to fund a "
   "casino and converting the proceeds back is a transaction IRD may look at. Keep records of every "
   "purchase and conversion, and take advice if the amounts are meaningful.</p>"),
  ("Which is the fastest instant withdrawal crypto casino NZ players can use?",
   "<p>Spino, on our timing &mdash; it is the closest thing to an instant withdrawal crypto casino NZ "
   "players can open, at eleven minutes for our quickest cashout. The measured median across all the "
   "crypto-capable casinos on this site is about three hours from clicking confirm to funds in the "
   "wallet, with a typical worst case of eight hours. Almost all of that time is operator approval, not blockchain "
   "settlement &mdash; the chain itself confirms in minutes.</p>"),
  ("What is a zero-wagering crypto bonus?",
   "<p>A bonus whose winnings can be withdrawn immediately with no turnover requirement. Spino offers "
   "one up to 2,000 USDT, and it is the only genuine example on this site. They are almost exclusively "
   "crypto offers because the operator&rsquo;s cost of funds is lower and the audience is more "
   "price-sensitive. Read the maximum cash-out clause, which is where the limit usually sits instead.</p>"),
  ("What happens if I send crypto to the wrong address?",
   "<p>It is gone. There is no reversal, no chargeback and no support desk that can retrieve it. Always "
   "copy and paste the address, always check the network matches (USDT on Tron sent to an Ethereum "
   "address is lost), and always send a small test transaction first when depositing to a new casino.</p>"),
  ("Can I use crypto and still hold a NZD balance?",
   "<p>At some casinos, yes. Spinjo, Kingdom, Rooster Bet and Fortune Play all hold NZD balances and "
   "accept crypto deposits, converting at the cashier. That is the best of both arrangements: fast "
   "money movement with no ongoing exchange-rate exposure on the balance itself. Spino does not &mdash; "
   "it is crypto end to end.</p>"),
 ],
 "sections": [
  {"html": [h2("Which coins work where", "coins"),
   table(["Casino", "BTC", "ETH", "USDT", "USDC", "LTC", "DOGE", "SOL", "TRX", "Fiat too?"], [
     ["Spino", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "<b>No</b>"],
     ["Kingdom", "Yes", "Yes", "Yes", "&mdash;", "&mdash;", "Yes", "&mdash;", "&mdash;", "Yes, NZD"],
     ["Smash", "Yes", "Yes", "Yes", "&mdash;", "&mdash;", "Yes", "&mdash;", "&mdash;", "Yes, NZD"],
     ["CrownSlots", "Yes", "Yes", "Yes", "&mdash;", "Yes", "&mdash;", "&mdash;", "&mdash;", "Yes, EUR"],
     ["Rooster Bet", "Yes", "Yes", "Yes", "&mdash;", "&mdash;", "&mdash;", "&mdash;", "&mdash;", "Yes, NZD"],
     ["Fortune Play", "Yes", "Yes", "Yes", "&mdash;", "&mdash;", "&mdash;", "&mdash;", "&mdash;", "Yes, NZD"],
     ["Spinjo", "Yes", "Yes", "Yes", "&mdash;", "Yes", "&mdash;", "&mdash;", "&mdash;", "Yes, NZD"],
     ["Rivo", "Yes", "Yes", "Yes", "&mdash;", "&mdash;", "&mdash;", "&mdash;", "&mdash;", "Yes, NZD"],
   ], caption="Cryptocurrency support at NZ-facing casinos, %s" % MONTH_YEAR),
   h3("Stablecoins versus Bitcoin", "stablecoins"),
   "<p>This is the decision that matters most and it is rarely explained. Bitcoin can move five percent "
   "while your withdrawal is processing. A NZ$2,000 win can become NZ$1,900 for reasons that have "
   "nothing to do with the casino. USDT and USDC are pegged to the US dollar, so the only currency "
   "exposure you carry is USD to NZD, which is a far smaller and slower-moving risk.</p>",
   note("<b>Practical recommendation.</b> Use USDT on the Tron network for casino deposits and "
        "withdrawals. Fees under a dollar, settlement in a couple of minutes, no volatility while the "
        "transaction is in flight, and it is the most widely supported rail across the sites on this "
        "page. Convert to NZD once, at an exchange you control.", "ok")]},

  {"html": [h2("Real settlement times and network fees", "settlement"),
   table(["Coin / network", "Blockchain confirmation", "Typical network fee", "Volatility risk in flight", "Support here"], [
     ["USDT (Tron)", "1&ndash;3 min", "&asymp;NZ$1.50", "Negligible", "All crypto casinos"],
     ["USDT (Ethereum)", "2&ndash;5 min", "NZ$4&ndash;25, varies", "Negligible", "All crypto casinos"],
     ["USDC", "2&ndash;5 min", "NZ$4&ndash;25", "Negligible", "Spino only"],
     ["Bitcoin", "10&ndash;60 min", "NZ$2&ndash;15", "Real &mdash; can move 3&ndash;5% in an hour", "All crypto casinos"],
     ["Ethereum", "2&ndash;5 min", "NZ$4&ndash;25", "Real", "Most"],
     ["Litecoin", "3&ndash;10 min", "&asymp;NZ$0.10", "Real", "Spino, CrownSlots, Spinjo"],
     ["Dogecoin", "2&ndash;10 min", "&asymp;NZ$0.20", "High", "Spino, Kingdom, Smash"],
     ["Solana", "&lt;1 min", "&asymp;NZ$0.02", "Real", "Spino"],
   ], caption="Crypto settlement and cost, from a New Zealand perspective"),
   "<p>Note how small the blockchain component is. When a crypto withdrawal takes three hours, roughly "
   "two hours fifty-five minutes of that is the operator&rsquo;s approval queue. That is why our "
   "ranking is built on measured end-to-end times rather than on which chains a casino supports.</p>"]},

  {"html": [h2("Coin by coin: which crypto casino NZ players should use for what", "coin-by-coin"),
   "<p>&lsquo;Crypto&rsquo; is not one payment method, it is eight, and they behave very differently. "
   "Picking the right one is most of the decision.</p>",

   h3("Bitcoin casino NZ", "bitcoin"),
   "<p>Universally accepted and the slowest of the major rails. Every bitcoin casino NZ players can "
   "reach takes BTC, confirmation runs ten to sixty minutes, and the price can move three to five "
   "percent while your withdrawal is in flight &mdash; a NZ$2,000 win can become NZ$1,900 for reasons "
   "that have nothing to do with the operator. Use it when nothing else is offered. If you want the "
   "best bitcoin casino NZ has in 2026 on our data, that is Kingdom for speed and Spino for wagering "
   "terms.</p>",

   h3("USDT casino NZ &mdash; the one we actually recommend", "usdt"),
   "<p>A USDT casino NZ account on the Tron network is the practical default: value pegged to the US "
   "dollar so nothing moves while a cashout processes, fees under NZ$1.50, confirmation in two "
   "minutes, and the widest support of any coin across the sites here. It is the rail we use for most "
   "of our own withdrawal timing.</p>",

   h3("Ethereum, Litecoin and Dogecoin", "eth-ltc-doge"),
   "<p>An Ethereum casino NZ deposit is fast but the network fee swings between NZ$4 and NZ$25, so it "
   "is poor value on small amounts. A Litecoin casino NZ transfer costs about ten cents and confirms "
   "in minutes, which makes it the cheapest fiat-free option where it is supported &mdash; Spino, "
   "CrownSlots and Spinjo. A Dogecoin casino NZ deposit works at Spino, Kingdom and Smash, is "
   "similarly cheap, and is the most volatile thing on this page.</p>",

   h3("Crypto pokies NZ and bitcoin pokies", "crypto-pokies"),
   "<p>There is no separate catalogue. The crypto pokies NZ players get are the same Pragmatic, "
   "Play&rsquo;n GO and Hacksaw titles served in a wallet denominated in coin rather than dollars. "
   "What is genuinely different at crypto-first sites is the instant-win and crash shelf, which is "
   "proportionally much larger, and the presence of provably fair in-house games.</p>",

   h3("Provably fair casino games, explained", "provably-fair"),
   "<p>A provably fair casino publishes a cryptographic seed before each round and the result "
   "afterwards, so you can verify that the outcome was fixed before you bet and was not altered. It "
   "applies only to a casino&rsquo;s own in-house games &mdash; dice, crash, plinko &mdash; never to "
   "third-party pokies, which are certified by laboratories instead. It is a real guarantee about a "
   "narrow set of games, not a site-wide seal of honesty, and it is often sold as the latter.</p>",

   h3("Anonymous casino NZ &mdash; what is and is not true", "anonymous"),
   "<p>An anonymous casino NZ players can register at with an email address and a wallet does exist, "
   "and crypto-only sites are where you find them. The limit is the cashier: any operator with a real "
   "licence still has anti-money-laundering obligations, and large or unusual withdrawals trigger "
   "identity checks regardless of how you funded the account. Treat &lsquo;no KYC&rsquo; as &lsquo;no "
   "KYC until it matters&rsquo;, and be aware that the sites promising otherwise are the ones with "
   "the thinnest regulators behind them.</p>"]},

  {"html": [h2("How to deposit and withdraw at a bitcoin casino NZ side", "how-to"),
   "<p>Bitcoin gambling NZ players do for the first time usually goes wrong in the same two places: "
   "the network and the test transaction. Here is the sequence that avoids both.</p>",
   steps([
     ("Buy on a New Zealand exchange",
      "Easy Crypto, Independent Reserve, Swyftx NZ and Binance all take NZD bank transfers. Compare "
      "the all-in cost including spread, not the headline trading fee."),
     ("Buy USDT rather than BTC if this is for gambling",
      "You want the value stable between purchase and play. Buying Bitcoin to fund a casino stacks a "
      "second speculative position on top of the gambling."),
     ("Copy the deposit address and check the network",
      "How to deposit bitcoin at an online casino NZ side: open the cashier, choose the coin, copy "
      "the address, and confirm the network matches. USDT on Tron sent to an Ethereum address is "
      "gone permanently &mdash; there is no reversal and no support desk that can retrieve it."),
     ("Send NZ$10 first",
      "Confirm it arrives and is credited before you send the real amount. This single habit prevents "
      "the most expensive mistake in crypto gambling. The crypto casino minimum deposit NZ sites ask "
      "is typically 20 USDT or the coin equivalent."),
     ("Withdraw the same way",
      "How to withdraw crypto from an online casino NZ side is the mirror image: paste your wallet "
      "address, match the network, and expect the operator&rsquo;s approval queue to be most of the "
      "wait. The fastest crypto withdrawal casino NZ we have timed is Spino at eleven minutes; "
      "Kingdom is the fastest with a fiat option at a 2h 50m median."),
     ("Keep a record of every purchase and conversion",
      "Date, amount, NZD value, fee. You may need it for Inland Revenue and reconstructing it later "
      "is painful."),
   ]),
   note("<b>Crypto vs bank transfer casino withdrawals, in one line.</b> Crypto: median about three "
        "hours, a network fee of a dollar or two, and exchange-rate exposure you carry. NZD bank "
        "transfer: one to three business days, usually free, no exposure at all. If speed is what you "
        "are buying, crypto wins clearly. If it is not, a casino with a New Zealand dollar wallet is "
        "the simpler answer.", "info")]},

  {"html": [h2("Buying crypto in New Zealand", "buying"),
   steps([
     ("Choose a New Zealand exchange",
      "Easy Crypto, Independent Reserve, Swyftx NZ and Binance all serve New Zealand and accept NZD "
      "bank transfers. Fees vary from roughly 0.1% to 1% plus a spread &mdash; compare the all-in cost, "
      "not the headline trading fee."),
     ("Verify your identity there too",
      "New Zealand exchanges are subject to the AML/CFT Act, so expect the same ID and proof-of-address "
      "process you will go through at the casino. Do it once, up front."),
     ("Buy USDT, not Bitcoin, if this is for gambling",
      "You want the value stable between purchase and play. Buying BTC to fund a casino adds a second "
      "speculative position on top of the gambling."),
     ("Withdraw to your own wallet, or send directly",
      "Sending straight from the exchange to the casino works and is simpler. Holding your own wallet "
      "gives you control but adds a step and a way to lose the funds."),
     ("Send a small test transaction first",
      "Ten dollars. Confirm it arrives and is credited before you send the real amount. This single "
      "habit prevents the most expensive mistake in crypto gambling."),
     ("Keep a record of every purchase and conversion",
      "Date, amount, NZD value, fee. You may need it for IRD, and reconstructing it later is painful."),
   ])]},

  {"html": [h2("Tax: what actually applies", "tax"),
   "<p>This trips up more New Zealanders than any other aspect of crypto gambling, because there are "
   "two separate tax questions and the answers differ.</p>",
   table(["Question", "Position", "Why"], [
     ["Are my casino winnings taxable?", "<b>No, for a recreational player</b>",
      "Inland Revenue does not treat casual gambling winnings as income. A person gambling as a "
      "business is the rare exception."],
     ["Is buying and selling crypto taxable?", "<b>Potentially yes</b>",
      "IRD treats cryptoassets as property. A gain on disposal is taxable if you acquired the asset "
      "with the purpose of disposing of it &mdash; which buying USDT to fund a casino arguably is."],
     ["What counts as a disposal?", "Converting to NZD, to another coin, or spending it",
      "Not just cashing out to your bank. Swapping USDT for BTC is a disposal."],
     ["What records should I keep?", "Every purchase, conversion and transfer with NZD values",
      "IRD expects contemporaneous records. Exchanges provide statements &mdash; download them "
      "annually."],
   ], caption="Crypto and tax for New Zealand casino players"),
   note("<b>This is general information, not tax advice.</b> If you are moving meaningful sums, talk "
        "to a New Zealand accountant who has handled cryptoassets. Inland Revenue publishes specific "
        "guidance on cryptoassets and it is worth reading in the original.", "info")]},

  {"html": [h2("The risks, stated plainly", "risks"),
   pros_cons(
     ["Withdrawals in hours rather than business days &mdash; the single biggest practical advantage",
      "No bank declining a gambling merchant code, which still happens on New Zealand cards",
      "No currency conversion spread if you deposit and withdraw in the same stablecoin",
      "Access to zero-wagering offers that fiat players cannot claim",
      "Higher weekly withdrawal ceilings, or none at all in Spino&rsquo;s case"],
     ["A mistyped or wrong-network address means the funds are permanently gone",
      "Bitcoin and Ethereum can lose value while a withdrawal is processing",
      "Converting back to NZD may create an IRD-reportable disposal",
      "Crypto-only casinos give you no fiat escape route if you want out quickly",
      "The crypto-only end of the market skews towards lighter-touch licences &mdash; Spino is "
      "Tobique-licensed, the thinnest regulator represented on this site"],
     "What crypto genuinely gives you", "What it costs you"),
   "<p>The balanced position: use crypto as a payment rail at a casino that also holds NZD and has a "
   "verifiable licence &mdash; Kingdom, Rooster Bet, Spinjo or Smash. Use a crypto-only site like Spino "
   "for the specific things it does better than anyone, with money you have consciously decided to "
   "expose to a lighter regulatory framework.</p>"]},
 ],
}

# ===========================================================================
# NEW ONLINE CASINOS
# ===========================================================================
NEW = {
 "path": "/new-casinos-nz/",
 "crumbs": [("New online casinos", None)],
 "author": "jordan-whitcombe", "checker": "aroha-tainui",
 "section_name": "New online casinos",
 "title": "New Online Casinos NZ %s &mdash; 2024&ndash;2026 Launches Tested" % MONTH_YEAR,
 "desc": ("New online casinos accepting New Zealand players, launched 2023&ndash;2026. What a new site "
          "does better, what it cannot yet prove, and how to test one safely."),
 "h1": "New Online Casinos NZ",
 "eyebrow": "Launched 2023&ndash;2026 &middot; tested %s" % MONTH_YEAR,
 "lede": ("New casinos NZ players can open compete on the two things they can change quickly: bonus "
          "size and payout speed. "
          "What they cannot offer is a track record. This page ranks the recent launches serving New "
          "Zealand, explains exactly what the missing history means for you, and sets out how to test "
          "a new site without exposing much."),
 "stats": [("2024", "Newest cohort here"), ("600%", "Largest new-site bonus"),
           ("2h 50m", "Fastest new-site payout"), ("NZ$50", "Sensible first deposit")],
 "cta2": ("How to test a new casino", "#testing"),
 "order": ["kingdom", "smash", "rivo", "madcasino", "crownslots", "spino", "roby-casino"],
 "notes": {
   "kingdom": "Launched 2024 and already the fastest payer we track. The strongest new arrival by a distance.",
   "smash": "2024 launch competing purely on bonus mathematics &mdash; 10x where the market asks 40x.",
   "rivo": "2024 launch built mobile-first, and it shows: 1.4 seconds to an interactive lobby on 4G.",
   "madcasino": "2024 launch with casino and sportsbook integrated from day one on a NZ$20 account.",
   "crownslots": "2024 launch buying attention with a 390% match. Fast crypto, euro wallet.",
   "spino": "2024 crypto-only launch with 0x wagering and the fastest cashier we have measured.",
   "roby-casino": "2024 launch with a big bonus and no published licence. Listed with that warning.",
 },
 "rank_h2": "New online casinos NZ &mdash; %s" % MONTH_YEAR,
 "rank_intro": ("The newest online casinos NZ players can currently open, ranked among recent "
                "launches only. A new casino starts with a trust-score penalty it can only remove "
                "with time, so scores here are not directly comparable with long-established sites."),
 "intro": [
   "<p>Every casino on this page opened in 2023 or 2024. That is recent enough that none of them has a "
   "multi-year payment record, and old enough that we have been able to test them properly rather than "
   "repeat a launch press release.</p>",
   "<p>The honest framing is this: a new casino usually offers a better bonus and often a faster "
   "cashier, because those are the levers available to a challenger. What it cannot offer is evidence "
   "that it will still be paying promptly in two years. That is not a reason to avoid new sites. It is "
   "a reason to size your exposure accordingly.</p>"],
 "toc": [("New casino sites NZ, ranked", "ranked"), ("Launch tracker", "tracker"),
         ("What to check before joining", "checklist"),
         ("Launch dates and platform groups", "groups"),
         ("What a new casino does better", "better"),
         ("What a new casino cannot prove yet", "risk"),
         ("How to test a new casino safely", "testing"),
         ("New casinos and the December 2026 deadline", "deadline"),
         ("Frequently asked questions", "faq")],
 "faq_h2": "New online casinos NZ &mdash; frequently asked questions",
 "faq": [
  ("Are new online casinos safe?",
   "<p>A new casino is not inherently less safe than an old one &mdash; what it lacks is evidence. "
   "Apply the same tests you would anywhere: a published licence number that verifies on the "
   "regulator&rsquo;s register, a named corporate entity, independently tested games, and a support "
   "desk that answers. Kingdom and Smash both pass those tests despite launching in 2024. Roby Casino, "
   "which launched the same year, does not publish a licence number at all.</p>"),
  ("Is a new online casino NZ real money players open any less safe?",
   "<p>Not inherently &mdash; a new online casino NZ real money players fund is missing evidence, not "
   "safeguards. It is also why the bonuses are bigger: it is the only lever a challenger has. An "
   "established site competes on reputation; a new one "
   "has none, so it buys attention with a headline number. This is genuinely good for players who read "
   "terms &mdash; Smash&rsquo;s 10x wagering exists because a 2024 launch had to differentiate "
   "somehow, and it is the best bonus term in this market.</p>"),
  ("What is a white label casino?",
   "<p>A casino running on someone else&rsquo;s platform and licence, with its own branding. Many new "
   "sites are white labels or sister brands. It is not a bad thing in itself &mdash; the underlying "
   "platform may be well-run and battle-tested &mdash; but it means the brand you are dealing with may "
   "have less substance than it appears. Knowing the platform group behind a new site tells you more "
   "than its launch date does.</p>"),
  ("How much should I deposit at a new casino?",
   "<p>Enough to test the cashier and no more, for the first month. NZ$50 is a sensible figure: large "
   "enough to trigger a real withdrawal and the verification process, small enough that being wrong "
   "about the site costs you a takeaway dinner. Withdraw something in week one before depositing "
   "anything larger.</p>"),
  ("Do new casinos have fewer games?",
   "<p>Not any more. Aggregated content platforms mean a 2024 launch can carry 7,000 titles from day "
   "one &mdash; Kingdom does. What new sites often lack is depth in the boutique studios and a "
   "properly built live floor, both of which need commercial relationships rather than an API.</p>"),
  ("Will new offshore casinos survive the New Zealand licensing regime?",
   "<p>Some will not. Up to 15 licences will be issued and the expression-of-interest fee alone is "
   "$19,000 excluding GST, before an auction price. A 2024 launch with a small New Zealand book may "
   "simply exit the market rather than bid. Treat any offshore balance as short-term money through the "
   "1 December 2026 transition. <a href=\"/licensed-online-casinos/\">Full timeline here</a>.</p>"),
 ],
 "sections": [
  {"html": [h2("Launch tracker: the newest online casinos NZ players can reach", "tracker"),
   "<p>From 1 December 2026 the licensed operators start going live, and this table becomes the "
   "running record of who has actually launched. It is re-checked and re-dated every month, and the "
   "date at the top of this page is the last time we did it.</p>",
   table(["Brand", "Launched", "Licence", "NZD", "Welcome offer", "Status for NZ"], [
     ["Kingdom", "2024", "Anjouan", "Yes", "600% to NZ$18,500 at 30x", "Accepting NZ registrations"],
     ["Smash", "2024", "Anjouan", "Yes", "600% to NZ$19,500 at 10x", "Accepting NZ registrations"],
     ["Rivo", "2024", "Anjouan", "Yes", "NZ$4,500 + 250 spins at 35x", "Accepting NZ registrations"],
     ["MadCasino", "2024", "Anjouan", "Yes", "NZ$4,000 + 200 spins at 40x", "Accepting NZ registrations"],
     ["CrownSlots", "2024", "Cura&ccedil;ao", "No, EUR", "390% to NZ$7,250 + 175 spins", "Accepting NZ registrations"],
     ["Spino", "2024", "Tobique", "No, crypto", "2,000 USDT at <b>0x</b>", "Crypto only"],
     ["Roby Casino", "2024", "<b>Not published</b>", "No, EUR", "250% to NZ$5,000 at 45x", "Listed with a warning"],
     ["Spinjo", "2023", "Cura&ccedil;ao GCB", "Yes", "NZ$5,000 + 300 spins at 40x", "Accepting NZ registrations"],
     ["Rooster Bet", "2023", "Cura&ccedil;ao GCB", "Yes", "NZ$5,000 + 300 spins at 40x", "Accepting NZ registrations"],
     ["Fortune Play", "2023", "Cura&ccedil;ao GCB", "Yes", "NZ$5,000 + 300 spins at 40x", "Accepting NZ registrations"],
     ["<em>DIA licence holders</em>", "<em>from Dec 2026</em>", "<em>NZ licence</em>", "<em>Required</em>",
      "<em>Advertising restricted</em>", "<em>Auction stage &mdash; list pending</em>"],
   ], caption="New casino sites NZ players can currently open, with launch year and licence"),
   "<p>The last row is the one to watch. Newly licensed online casinos in NZ will begin appearing "
   "once the Department of Internal Affairs completes its auction and issues the first of up to 15 "
   "licences, and we will add each brand here as it launches rather than announcing it in advance. "
   "New licensed casinos in NZ from December 2026 will look different from everything above: no "
   "credit cards, no autoplay, and a 24-hour cooling-off on any deposit-limit increase.</p>",
   note("<b>Upcoming online casinos NZ &mdash; why we will not speculate.</b> Several sites are "
        "already publishing lists of &lsquo;brand new online casinos NZ 2026&rsquo; that name "
        "operators as licence winners before the auction has concluded. Nobody knows the outcome yet, "
        "including the operators. We will name licence holders when the DIA does.", "warn")]},

  {"html": [h2("What to check before joining a new casino", "checklist"),
   "<p>The latest online casinos NZ players find are not inherently riskier than established ones "
   "&mdash; what they lack is evidence. Five minutes of checking replaces most of it.</p>",
   pros_cons(
     ["A licence number published in the footer that returns a result on the regulator&rsquo;s register",
      "A named operating company, and ideally a platform group you can recognise",
      "A welcome offer whose wagering multiple is stated plainly on the promotion page itself",
      "A cashier that lists a withdrawal method before you deposit, not after",
      "Published responsible gambling tools you can open and use immediately"],
     ["A licence badge that is an image with no number behind it",
      "Terms that differ between the promotion page and the account terms",
      "&lsquo;Instant withdrawals&rsquo; with no stated processing window",
      "A weekly withdrawal cap lower than the maximum advertised bonus",
      "Pressure to deposit again before the first withdrawal has cleared"],
     "Signs a new casino is worth a NZ$50 test", "Signs to close the tab"),
   "<p>Are new online casinos safe in NZ? The ones that pass the left-hand column generally are. Every "
   "new online casino NZ real money players can open on this page cleared a NZ$50 deposit and a test "
   "withdrawal before we listed it &mdash; that is the whole basis for its position.</p>",
   h3("New pokie sites NZ and what actually changes", "new-pokie-sites"),
   "<p>The newest pokie sites in New Zealand rarely differ on catalogue &mdash; content aggregation "
   "means a 2024 launch can carry 7,000 titles on day one. What does change is the shelf: newer "
   "lobbies put crash and instant-win games front and centre rather than burying them, and their "
   "filtering is usually better. New casino sites with free spins in NZ are common at launch because "
   "spins are cheaper for an operator to fund than a match bonus; a new online casino free spins no "
   "deposit NZ offer is much rarer, and Lucky7even remains the only one we can verify.</p>",
   "<p>New crypto casinos NZ players can reach are the fastest-growing part of this cohort, and they "
   "are also where the lightest-touch licences cluster. <a href=\"/crypto-casinos-nz/\">Our crypto "
   "page</a> covers what that trade-off actually costs.</p>"]},

  {"html": [h2("Launch dates and platform groups", "groups"),
   "<p>The platform group behind a brand tells you more than its launch year. Four groups account for "
   "almost every new site serving New Zealand.</p>",
   table(["Casino", "Launched", "Operating company", "Licence", "Sister brands here"], [
     ["Kingdom", "2024", "Vertikal N.V.", "Anjouan", "Smash, Rivo, MadCasino"],
     ["Smash", "2024", "Vertikal N.V.", "Anjouan", "Kingdom, Rivo, MadCasino"],
     ["Rivo", "2024", "Vertikal N.V.", "Anjouan", "Kingdom, Smash, MadCasino"],
     ["MadCasino", "2024", "Vertikal N.V.", "Anjouan", "Kingdom, Smash, Rivo"],
     ["CrownSlots", "2024", "Not published", "Cura&ccedil;ao", "&mdash;"],
     ["Spino", "2024", "Not published", "Tobique", "&mdash;"],
     ["Roby Casino", "2024", "<b>Not published</b>", "<b>Not published</b>", "&mdash;"],
     ["Spinjo", "2023", "Rabidi N.V.", "Cura&ccedil;ao GCB", "Lucky7even, Lucky Vibe, Lucky Circus"],
     ["Rooster Bet", "2023", "Dama N.V.", "Cura&ccedil;ao GCB", "Fortune Play"],
     ["Fortune Play", "2023", "Dama N.V.", "Cura&ccedil;ao GCB", "Rooster Bet"],
   ], caption="New casino launches serving New Zealand, with platform groups"),
   note("<b>Why sister brands matter.</b> Four of the sites on this page run on the same Vertikal "
        "platform. If you have verified at Kingdom you already know how Smash&rsquo;s cashier, support "
        "desk and KYC process behave, because they are the same. It also means a problem at one is "
        "likely to be a problem at all four &mdash; do not treat them as four independent "
        "diversification options.", "info")]},

  {"html": [h2("What a new casino does better", "better"),
   cards([
     ("01", "Bigger, better-structured bonuses", "A challenger has to buy attention. Smash&rsquo;s 10x "
      "wagering and Kingdom&rsquo;s 30x on a 600% package both exist because 2024 launches could not "
      "win on reputation.", "/casino-bonus/", "Compare bonuses"),
     ("02", "Faster cashiers", "New platforms are built on modern payment infrastructure with crypto "
      "integrated from the start rather than bolted on. Kingdom&rsquo;s 2h 50m median is a 2024 site "
      "beating every established brand here.", "/fast-payout-casinos/", "Payout data"),
     ("03", "Better mobile builds", "A 2024 launch designed for a phone first. Rivo reaches an "
      "interactive lobby in 1.4 seconds on throttled 4G; a 2016-era site takes three times that.", None),
     ("04", "Modern game coverage from day one", "Content aggregation means a new casino can carry "
      "7,000 titles at launch, including studios that took older sites years to add.", None),
     ("05", "Cleaner interfaces", "Fewer legacy promotional layers. Whether that lasts past the "
      "growth phase is a different question.", None),
     ("06", "Responsive support", "A small book means a short queue. Kingdom&rsquo;s 1m 30s median "
      "chat response is the fastest we measured, and partly a function of scale.", None),
   ])]},

  {"html": [h2("What a new casino cannot prove yet", "risk"),
   "<p>Four things, and none of them is solvable by a good bonus.</p>",
   "<ul>"
   "<li><b>A payment record through a bad quarter.</b> Any casino pays promptly while it is growing. "
   "The question is what happens when the book turns against it, and a 2024 launch has not been "
   "through that cycle.</li>"
   "<li><b>Complaints handling at volume.</b> Support is fast when there are few customers. The test "
   "is a disputed withdrawal eighteen months in.</li>"
   "<li><b>Bonus term stability.</b> Launch terms are promotional. Several new sites have quietly "
   "raised wagering multiples in their second year, and terms can change for new claims at any time.</li>"
   "<li><b>Regulatory durability.</b> Anjouan and Tobique licences &mdash; which four of the seven "
   "sites here hold &mdash; are newer and lighter than Cura&ccedil;ao GCB. The complaints escalation "
   "path behind them is correspondingly thinner.</li></ul>",
   note("<b>How we handle this in scoring.</b> Trust and disclosure carries 20% of our weighted score, "
        "and a site with under two years of trading cannot reach the top of that component regardless "
        "of how good everything else is. That is why Kingdom scores 9.1 with the best payout data on "
        "the site while Spinjo, a year older with a stronger licence, scores 9.3.", "warn")]},

  {"html": [h2("How to test a new casino safely", "testing"),
   steps([
     ("Verify the licence before you register",
      "Find the licence number in the footer and check it on the regulator&rsquo;s register. If there "
      "is no number, stop. This takes two minutes and eliminates the worst outcomes."),
     ("Deposit NZ$50, no more, in month one",
      "Enough to trigger a real withdrawal and the full verification process. Small enough that being "
      "wrong is inconsequential."),
     ("Complete KYC immediately",
      "A new site&rsquo;s verification process is where corner-cutting shows. If it is slow or "
      "disorganised now, it will be worse under load."),
     ("Decline the welcome bonus on the first deposit",
      "You want a clean test of the withdrawal process without a wagering requirement in the way. "
      "Claim the bonus on deposit two, once you know the money comes back."),
     ("Withdraw NZ$30 in the first week",
      "The single most informative thing you can do. Time it. Note whether it was held, what was asked "
      "for, and how support behaved."),
     ("Only then decide whether it deserves real money",
      "If the test withdrawal cleared inside the stated window with no surprises, the site has earned "
      "a normal deposit. If it did not, you learned that for NZ$50."),
   ]),
   h3("New casinos and the December 2026 deadline", "deadline"),
   "<p>One further consideration specific to this moment. From 1 December 2026, operators that have "
   "not applied for a New Zealand licence must stop offering online casino gambling here. A 2024 "
   "launch with a modest New Zealand book has a genuine commercial question about whether to pay a "
   "$19,000 expression-of-interest fee plus an auction price for one of fifteen licences.</p>",
   "<p>Some of these brands will exit New Zealand rather than bid. That does not mean your balance "
   "disappears &mdash; an orderly exit means withdrawals are honoured and registrations close &mdash; "
   "but it does mean you should not be accumulating a large balance offshore right now. Withdraw "
   "regularly through the transition.</p>"]},
 ],
}

# ===========================================================================
# NO DEPOSIT CASINOS
# ===========================================================================
NODEP = {
 "path": "/no-deposit-bonus/",
 "crumbs": [("No deposit casinos", None)],
 "author": "jordan-whitcombe", "checker": "sam-kavanagh",
 "section_name": "No deposit bonuses",
 "title": "No Deposit Bonus NZ %s &mdash; Free Spins, No Deposit Needed" % MONTH_YEAR,
 "desc": ("Genuine no-deposit casino bonuses for New Zealand players. What you can realistically "
          "withdraw, the wagering and cap that applies, and why these offers are now rare."),
 "h1": "No Deposit Bonus Casinos NZ",
 "eyebrow": "Verified claimable from NZ &middot; %s" % MONTH_YEAR,
 "lede": ("A no-deposit bonus lets you play for real money without funding an account. There is "
          "exactly one genuine offer available to New Zealanders on the sites we cover, and this page "
          "explains what it is actually worth, what the terms do to it, and how to use it as a free "
          "test of a casino rather than as a way to make money."),
 "stats": [("20", "Free spins, no deposit"), ("50x", "Wagering on winnings"),
           ("1", "Genuine NZ offer we found"), ("NZ$0", "What it costs you")],
 "cta2": ("What it is really worth", "#worth"),
 "order": ["lucky7even", "lucky-circus", "spino", "smash", "ivibet"],
 "notes": {
   "lucky7even": "<b>The genuine no-deposit offer:</b> 20 free spins on Book of the Fallen, before any deposit. 50x on winnings.",
   "lucky-circus": "No no-deposit offer, but NZ$10 is the lowest real deposit on this site &mdash; the next best thing.",
   "spino": "No no-deposit offer, but 0x wagering means the deposited bonus behaves like free money.",
   "smash": "No no-deposit offer. 10x wagering on a deposited bonus is the best clearable value here.",
   "ivibet": "No no-deposit offer. NZ$500 at 35x on one deposit is the most finishable standard bonus.",
 },
 "rank_h2": "No deposit and near-no-deposit offers for NZ players",
 "rank_intro": ("Only one genuine no deposit bonus NZ players can claim exists at the casinos we "
                "cover. The rest of this list is the honest alternative: the lowest-commitment offers "
                "available, ranked by how little you have to risk."),
 "intro": [
   "<p>Let us be direct, because most pages on this topic are not. No-deposit bonuses have become rare "
   "for New Zealand players. Operators tightened them as bonus-abuse controls improved, and many of "
   "the &lsquo;NZ no deposit bonus&rsquo; pages you will find list offers that are geo-blocked, "
   "expired, or were never claimable from New Zealand in the first place.</p>",
   "<p>We found one genuine, currently claimable no-deposit offer across the casinos we cover: "
   "Lucky7even&rsquo;s 20 free spins. We claimed it twice to confirm. Everything else on this page is "
   "presented as what it is &mdash; a low-commitment alternative, not a no-deposit bonus.</p>"],
 "toc": [("Offers ranked by commitment", "ranked"),
         ("What a no deposit bonus is actually worth", "worth"),
         ("How to claim, step by step", "claim"),
         ("The terms that limit it", "terms"),
         ("Why these offers are disappearing", "why-rare"),
         ("Better alternatives if you have NZ$10&ndash;20", "alternatives"),
         ("Frequently asked questions", "faq")],
 "faq_h2": "No deposit bonuses NZ &mdash; frequently asked questions",
 "faq": [
  ("Is there a genuine casino no deposit bonus New Zealand players can claim?",
   "<p>One, and we can verify it. A casino no deposit bonus New Zealand accounts can actually claim is rare; Lucky7even offers 20 free spins on Book of the Fallen with no "
   "deposit required, claimable from a New Zealand account after email verification. We have claimed "
   "it twice to confirm it still works. If you see other NZ no-deposit offers advertised, check "
   "whether they are geo-blocked before you register &mdash; most that we tested were.</p>"),
  ("How much can I actually win from 20 free spins?",
   "<p>Realistically, very little. At the typical fixed stake of NZ$0.20 per spin, 20 spins is NZ$4 of "
   "turnover. At Book of the Fallen&rsquo;s RTP you would expect to finish with around NZ$3.80, and "
   "then face 50x wagering on it plus a maximum cash-out. Treat it as a free look at the casino, not "
   "as a way to win money. Anyone telling you otherwise is selling something.</p>"),
  ("What is the wagering on a no deposit bonus?",
   "<p>Higher than on a deposited bonus, almost always. Lucky7even applies 40x to its match bonus and "
   "50x to winnings from the no-deposit spins. There is also normally a maximum cash-out &mdash; "
   "typically NZ$100 to NZ$200 &mdash; so even an exceptional result is capped.</p>"),
  ("Do I need to enter card details to claim a no deposit bonus?",
   "<p>Not at Lucky7even &mdash; email verification is sufficient. Be cautious of any &lsquo;no "
   "deposit&rsquo; offer that requires card details up front; that is a deposit flow with different "
   "branding. You will need to verify identity fully before withdrawing anything you win, which is "
   "normal and required by the operator&rsquo;s licence.</p>"),
  ("Can I claim a no deposit bonus more than once?",
   "<p>No. One per person, per household, per device, per payment method. Operators check IP, device "
   "fingerprint and identity documents, and attempting a second claim typically means both accounts "
   "are closed and any balance forfeited. It is not worth it for NZ$4 of spins.</p>"),
  ("Are no deposit bonuses a scam?",
   "<p>Not at the licensed sites here &mdash; the spins are real and the winnings are payable if you "
   "clear the terms. The dishonesty is usually in how they are marketed: pages that headline "
   "&lsquo;NZ$50 free&rsquo; and bury a 60x requirement and a NZ$50 cash-out cap. The offer is real; "
   "the implied value is not.</p>"),
  ("What is better than a no deposit bonus?",
   "<p>A low minimum deposit with reasonable wagering. Lucky Circus takes NZ$10 at 35x, which gives "
   "you a genuine bankroll and a realistic requirement. Smash takes NZ$20 at 10x on deposit plus "
   "bonus. Either is worth far more than 20 free spins with 50x attached, and NZ$10 is a smaller "
   "commitment than most people imagine.</p>"),
 ],
 "sections": [
  {"html": [h2("What a no deposit bonus is actually worth", "worth"),
   "<p>Here is the arithmetic that no-deposit pages leave out. This is Lucky7even&rsquo;s offer, run "
   "through honestly.</p>",
   table(["Step", "Figure", "Explanation"], [
     ["Free spins granted", "20", "On Book of the Fallen, at a fixed stake"],
     ["Fixed stake per spin", "NZ$0.20", "Set by the operator, not chosen by you"],
     ["Total turnover granted", "NZ$4.00", "20 &times; NZ$0.20"],
     ["Expected return at ~96% RTP", "&asymp;NZ$3.84", "The statistically expected outcome"],
     ["Wagering on winnings", "50x", "Applied to whatever the spins return"],
     ["Turnover needed on a NZ$4 win", "<b>NZ$200</b>", "50 &times; NZ$4"],
     ["Expected cost of generating it", "&asymp;NZ$8", "At a 4% house edge on NZ$200 turnover"],
     ["Maximum cash-out", "Typically NZ$100", "Caps any exceptional result"],
     ["Realistic expected value", "<b>Close to zero</b>", "But it costs you nothing"],
   ], caption="Lucky7even 20 free spins, worked through"),
   note("<b>So why claim it at all?</b> Because the expected value is zero and the cost is zero, and "
        "what you get in exchange is a complete look at the casino: the lobby, the cashier, the "
        "verification process and the support desk, before you have exposed a dollar. That is the "
        "entire case for a no-deposit bonus and it is a good one. It is just not the case the "
        "advertising makes.", "ok")]},

  {"html": [h2("No deposit bonus codes NZ: how they work and why most are dead", "codes"),
   "<p>Search results are full of no deposit bonus codes NZ pages listing dozens of strings to paste "
   "into a cashier. Almost none of them work, and it is worth understanding why before you spend an "
   "evening trying them.</p>",
   table(["Offer type", "Needs a code?", "How it is credited", "Typical shelf life"], [
     ["Lucky7even, 20 no-deposit spins", "<b>No</b>", "Automatically on email verification", "Ongoing"],
     ["Exclusive no deposit bonus codes NZ affiliates advertise", "Usually",
      "Entered at registration or in the cashier", "Weeks &mdash; they expire quietly"],
     ["A new no deposit bonus NZ sites launch with", "Usually", "Promotions tab, time-boxed", "Days"],
     ["Seasonal free chip no deposit casino NZ offers", "Usually", "Promotions tab, time-boxed", "Days"],
     ["Reload and loyalty codes", "Sometimes", "Emailed to existing players", "Days"],
     ["Codes copied from AU, CA or UK pages", "&mdash;", "<b>Geo-blocked for NZ</b>", "Never worked here"],
   ], caption="No deposit bonus codes NZ players encounter, and which actually credit"),
   "<p>That last row is most of the problem. A large share of the no deposit sign up bonus NZ listings "
   "you will find were scraped from another market, and the offer either never applied to New Zealand "
   "or was withdrawn a year ago. We list one genuine offer because it is the one we could claim twice "
   "from a New Zealand account and verify.</p>",
   h3("Free spins no deposit NZ 2026: what the amounts really mean", "amounts"),
   "<p>The headline counts are the most misleading part of this category. A free spins no deposit NZ "
   "2026 promotion advertising a big number is usually attaching a small stake and a hard cash-out "
   "cap to it.</p>",
   table(["Advertised offer", "Fixed stake", "Turnover it grants", "Typical cash-out cap", "Real value"], [
     ["20 free spins no deposit NZ", "NZ$0.20", "NZ$4", "NZ$100", "<b>&asymp;NZ$4 of play</b>"],
     ["25 free spins no deposit NZ", "NZ$0.10&ndash;0.20", "NZ$2.50&ndash;5", "NZ$100", "&asymp;NZ$4 of play"],
     ["50 free spins no deposit NZ", "NZ$0.10", "NZ$5", "NZ$50&ndash;100", "&asymp;NZ$5 of play"],
     ["100 free spins no deposit NZ", "NZ$0.10", "NZ$10", "NZ$50&ndash;100", "&asymp;NZ$10 of play"],
     ["$5 no deposit bonus NZ", "Your choice", "NZ$5", "NZ$50&ndash;100", "&asymp;NZ$5 of play"],
     ["$10 no deposit bonus NZ", "Your choice", "NZ$10", "NZ$100", "&asymp;NZ$10 of play"],
   ], caption="What each free spins no deposit offer is actually worth once the stake is fixed"),
   "<p>Note how little separates 20 spins from 100 spins once the stake is included: the operator "
   "scales the stake down as the count goes up. A real money no deposit bonus NZ offer is worth its "
   "granted turnover, not its spin count &mdash; and in every case a small deposit at sensible "
   "wagering is worth more.</p>",
   h3("Can you withdraw no deposit bonus winnings in NZ?", "withdraw"),
   "<p>Yes, if you clear the terms &mdash; and the terms are where the value goes. Three clauses apply "
   "to essentially every no deposit casino NZ offer: wagering on the winnings (50x at Lucky7even, "
   "higher than the 40x on its deposited bonus), a maximum cash-out that caps an exceptional result at "
   "NZ$100&ndash;200, and full identity verification before anything is released.</p>",
   "<p>So a no deposit bonus keep what you win NZ promise is almost always qualified. Where you see it "
   "stated without qualification, the cap has simply been moved into the terms page. No deposit free "
   "spins on registration in NZ are a free look at a casino, and that is a genuinely useful thing "
   "&mdash; it is just not a bankroll.</p>",
   note("<b>Are no deposit bonuses legit?</b> At the licensed sites here, yes: the spins are real and "
        "winnings are payable. The dishonesty is in the marketing, not the mechanism &mdash; pages "
        "that headline &lsquo;NZ$50 free&rsquo; and bury a 60x requirement with a NZ$50 cap. Free "
        "spins with no deposit and no card details in NZ do exist at Lucky7even; anything asking for "
        "card details up front is a deposit flow wearing different branding.", "info")]},

  {"html": [h2("How to claim, step by step", "claim"),
   steps([
     ("Register a Lucky7even account from a New Zealand IP",
      "Use your real name and date of birth &mdash; exactly as they appear on your ID. A mismatch "
      "found later voids any winnings."),
     ("Verify your email address",
      "The spins are credited after email confirmation. No card details are required at this stage."),
     ("Open Book of the Fallen from the lobby",
      "The spins are title-locked. They will not work on another game and they expire, usually within "
      "seven days of being credited."),
     ("Play all 20 spins",
      "The stake is fixed. Any winnings land in a bonus balance carrying 50x wagering."),
     ("Decide whether to pursue the wagering",
      "On a typical NZ$4 return that is NZ$200 of turnover. Often the honest answer is no &mdash; and "
      "that is fine, because you have already got what the offer was worth."),
     ("Use the visit to judge the casino",
      "Open the cashier. Check the withdrawal page. Start a chat and ask something awkward. This is "
      "the real value of the twenty spins."),
   ])]},

  {"html": [h2("The terms that limit it", "terms"),
   pros_cons(
     ["No deposit and no card details required",
      "Real money winnings, genuinely payable if you clear the terms",
      "A complete test of the casino at zero cost",
      "Credited automatically on email verification, with no code to hunt for"],
     ["50x wagering on winnings &mdash; higher than the 40x on deposited bonuses",
      "A maximum cash-out, typically NZ$100&ndash;200, regardless of what you win",
      "Locked to one title at a stake you do not choose",
      "Expires quickly, usually seven days",
      "Full identity verification still required before any withdrawal"],
     "What the offer gives you", "What the terms take back"),
   h3("Why these offers are disappearing", "why-rare"),
   "<p>Three reasons, and they are all structural rather than temporary. Bonus abuse got "
   "industrialised: device fingerprinting exists because multi-accounting at scale made no-deposit "
   "offers unprofitable. Payment-provider rules tightened, making the customer-acquisition cost of a "
   "non-depositing registration harder to justify. And regulators in several markets now treat "
   "no-deposit offers as high-risk for harm, which pushes compliance teams away from them.</p>",
   "<p>The New Zealand regime reinforces that direction. The Online Casino Gambling Regulations 2026 "
   "restrict how licensed operators may advertise and promote, and affiliate marketing is among the "
   "restricted categories for licensed operators. Expect no-deposit offers to become rarer still in "
   "the New Zealand market rather than more common.</p>"]},

  {"html": [h2("Better alternatives if you have NZ$10&ndash;20", "alternatives"),
   "<p>This is the honest recommendation. If your goal is to try a casino with minimal exposure, a "
   "small deposit at a site with sensible wagering beats a no-deposit bonus comfortably.</p>",
   table(["Option", "Cost to you", "What you get", "Turnover to withdraw", "Verdict"], [
     ["Lucky7even, 20 no-deposit spins", "NZ$0", "NZ$4 of turnover", "50x on winnings, capped",
      "Free look at the casino. Not a bankroll."],
     ["Lucky Circus, NZ$10 deposit", "NZ$10", "NZ$10 + NZ$10 bonus at 35x", "NZ$350",
      "<b>Best low-commitment start.</b> A real session with real choice of game."],
     ["Smash, NZ$20 deposit", "NZ$20", "NZ$20 + NZ$20 bonus at 10x deposit+bonus", "NZ$400",
      "<b>Best value per dollar risked</b> of any offer on this site."],
     ["Ivibet, NZ$20 deposit", "NZ$20", "NZ$20 + NZ$20 bonus at 35x", "NZ$700",
      "Good if live dealer is what you want to test."],
     ["Any site, deposit and decline the bonus", "NZ$10&ndash;20", "Your own money, no strings",
      "None", "The cleanest test of a cashier. Underrated."],
   ], caption="Low-commitment ways to test an online casino"),
   note("<b>The most underrated option on that table is the last one.</b> Deposit NZ$20, decline the "
        "bonus, play a bit, withdraw whatever is left. No wagering, no maximum bet rule, no excluded "
        "games, and you find out the only thing that actually matters: whether this casino gives money "
        "back promptly. We do this at every site before we write about it.", "ok")]},
 ],
}


def build():
    page(POKIES)
    page(LIVE)
    page(FAST)
    page(HIGH)
    page(CRYPTO)
    page(NEW)
    page(NODEP)
