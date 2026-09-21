# -*- coding: utf-8 -*-
"""/online-betting/ and /best-sports-betting-sites/"""
import lib
from lib import (MONTH_YEAR, MONTH, YEAR, N_WITHDRAWALS, leaderboard, table,
                 op_cell, faq, keyfacts, note, toc, steps, cards, ctaband,
                 authorbox, byline, hero, section, h2, h3, pros_cons,
                 DISCLOSURE, crumbs, timeline)

BOOKS = ["gunsbet", "rooster-bet", "betandplay", "kingdom", "smash", "madcasino",
         "fortune-play", "lucky-vibe", "rivo", "ivibet-sportsbook", "spino", "roby-casino"]

NOTES = {
 "gunsbet": "The largest welcome in NZ-facing betting at roughly NZ$13,900. Slow cashier, no crypto.",
 "rooster-bet": "The best all-round book: NPC, Super Rugby, netball and NZ racing on a NZD wallet.",
 "betandplay": "Sharpest in-play engine we tested, and a 5x at 1.80+ welcome you can actually clear.",
 "kingdom": "200% up to NZ$1,900 on the sports side, attached to the fastest cashier on this site.",
 "smash": "250% up to NZ$9,800 at 15x &mdash; the largest sports package with a workable multiple.",
 "madcasino": "One NZ$20 account for sport and pokies, with a separate NZ$400 sports welcome.",
 "fortune-play": "NZ$350 free bet alongside a strong casino, on a Dama N.V. platform.",
 "lucky-vibe": "NZ$250 free bet plus the cashback scheme, which applies across both products.",
 "rivo": "NZ$300 sports welcome on the fastest mobile build we measured &mdash; good for in-play.",
 "ivibet-sportsbook": "Prices ANZ Premiership netball and NZ domestic cricket that bigger books ignore.",
 "spino": "Crypto free bet up to 200 USDT with the fastest payouts in this list. Crypto only.",
 "roby-casino": "NZ$300 sports welcome. No published licence &mdash; listed with that warning.",
}

BET_FAQ = [
 ("Is online betting legal in New Zealand?",
  "<p>Yes, for you. New Zealand law prohibits anyone other than TAB NZ from <em>offering</em> sports "
  "and racing betting from within New Zealand &mdash; that is the effect of the Racing Industry Act "
  "2020 &mdash; but it has never been an offence for a New Zealander to place a bet with an overseas "
  "bookmaker. Offshore operators taking bets from New Zealand are also subject to offshore betting "
  "charges under that Act. Note that the Online Casino Gambling Act 2026 covers online <em>casino</em> "
  "gambling only; sports betting is a separate regime and TAB NZ&rsquo;s domestic exclusivity is "
  "unchanged.</p>"),
 ("Is TAB NZ better than an offshore bookmaker?",
  "<p>Better at some things, worse at others. TAB NZ is New Zealand-based, regulated here, funds the "
  "domestic racing and sporting codes, and offers genuine local depth on New Zealand racing. Offshore "
  "books are typically sharper on price &mdash; our weekly sample puts the better offshore books "
  "1.5 to 3 percentage points tighter on overround for mainstream rugby and football markets &mdash; "
  "and they offer welcome bonuses TAB cannot match. Many New Zealand punters hold both and shop for "
  "the price.</p>"),
 ("Do I pay tax on betting winnings in New Zealand?",
  "<p>Not as a recreational punter. Inland Revenue does not treat casual gambling winnings as income. "
  "The exception is a person betting as a business &mdash; systematically, with an expectation of "
  "profit and the organisation to match &mdash; which is rare and worth professional advice if you "
  "think it describes you.</p>"),
 ("What is an overround, and why does it matter more than the odds?",
  "<p>The overround is the bookmaker&rsquo;s built-in margin. Convert every price in a market to an "
  "implied probability and add them up: a fair market totals 100%, and anything above that is the "
  "book&rsquo;s edge. A rugby head-to-head at 102.5% is a much better market than one at 106%, even "
  "if the favourite&rsquo;s price looks similar. We publish measured overrounds on this page because "
  "it is the only honest way to compare bookmakers.</p>"),
 ("Can I bet on the NPC and Super Rugby with offshore bookmakers?",
  "<p>Yes, and coverage is good. Every book on this page prices Super Rugby Pacific and the Bunnings "
  "NPC head-to-head, handicap and totals markets, and most offer in-play. Depth varies: Rooster Bet "
  "and Bet&amp;Play carry player props and multi-leg builders on NPC matches, while smaller books "
  "offer head-to-head only.</p>"),
 ("Can I still bet on greyhound racing in New Zealand?",
  "<p>Not on New Zealand greyhounds. Commercial greyhound racing in New Zealand ended on 1 August "
  "2026 under the Racing Industry (Closure of Greyhound Racing Industry) Amendment, which passed 112 "
  "votes to 11. Australian, British and Irish greyhound meetings are still available at most offshore "
  "books and through TAB NZ. New Zealand thoroughbred and harness racing are unaffected.</p>"),
 ("What is the fastest way to get a betting withdrawal in New Zealand?",
  "<p>Cryptocurrency, by a wide margin &mdash; a median of about three hours against one to five "
  "business days on a card. Among the books here, Kingdom (2h 50m median) and Rooster Bet (3h) are "
  "the fastest with a fiat option; Spino is faster still at 38 minutes but is crypto-only. Gunsbet, "
  "which has the biggest welcome offer, has no crypto at all and takes 12&ndash;24 hours at best.</p>"),
 ("Do offshore bookmakers offer in-play betting on New Zealand sport?",
  "<p>The better ones do. Bet&amp;Play has the sharpest in-play engine we tested and stayed live "
  "through a full Super Rugby Pacific round and an NPC Saturday without unexplained suspensions. "
  "Rooster Bet and Kingdom also offer in-play on the main New Zealand codes. Be aware that all "
  "offshore in-play runs a few seconds behind a live broadcast, and further behind a delayed "
  "stream.</p>"),
 ("What happens to a bet if a match is abandoned?",
  "<p>It depends on the book&rsquo;s rules and the sport, and this is worth reading before you need "
  "it. The common position for rugby and football is that bets are void and stakes returned if a "
  "match is abandoned before a defined point, and stand if abandoned after it. Racing bets are "
  "normally void if a meeting is abandoned. Every book on this page publishes sport-by-sport rules; "
  "they are not identical.</p>"),
 ("Should I use more than one bookmaker?",
  "<p>If you bet regularly, yes. Prices differ meaningfully between books on the same market, welcome "
  "offers are one per person per site, and having two accounts lets you take the better price rather "
  "than the only price. Three accounts covers most situations: a broad book, a sharp in-play book, "
  "and TAB NZ for domestic racing depth.</p>"),
]

SITES_FAQ = [
 ("Which is the best sports betting site for New Zealand players?",
  "<p>Rooster Bet, on our scoring: the best combination of market depth on New Zealand codes, a NZD "
  "wallet, a three-hour median payout and a Cura&ccedil;ao Gaming Control Board licence held by Dama "
  "N.V. Bet&amp;Play is the pick if you bet in-play, and Gunsbet has the biggest welcome offer by a "
  "distance if you are a high-turnover punter who can live with a slow cashier.</p>"),
 ("Which betting site has the best welcome bonus in NZ?",
  "<p>Gunsbet, on size: 285% up to &euro;7,500, roughly NZ$13,900, plus 285 free spins. Smash has the "
  "best large offer with a workable multiple at 250% up to NZ$9,800 at 15x. Bet&amp;Play&rsquo;s "
  "100% up to NZ$500 at 5x on odds of 1.80+ is the most realistically clearable sports welcome on "
  "this page.</p>"),
 ("How do I compare betting sites properly?",
  "<p>Margin first, everything else second. Take a market you bet often, convert each price to an "
  "implied probability, add them up, and compare the totals across books. A two-point difference in "
  "overround costs more over a year than any welcome bonus returns. Then check withdrawal speed, "
  "in-play quality if you use it, and whether the book prices the sports you actually follow.</p>"),
 ("Do these sites cover New Zealand racing?",
  "<p>Thoroughbred and harness, yes, at every book on this page. Depth is thinner than TAB NZ &mdash; "
  "expect win, place and each-way on most meetings but fewer exotics, and limited coverage of minor "
  "midweek cards. New Zealand greyhound racing ceased on 1 August 2026, so no book offers it; "
  "Australian and UK greyhounds remain available.</p>"),
 ("Can I bet on the All Blacks and the Black Caps?",
  "<p>Yes, comprehensively. All Blacks tests, the Rugby Championship, Black Caps internationals across "
  "all three formats and the Super Smash are priced at every book here, usually with a deeper market "
  "list than domestic competitions get. Player props on All Blacks tests are available at Rooster Bet, "
  "Bet&amp;Play and Kingdom.</p>"),
 ("Is there betting on the ANZ Premiership netball?",
  "<p>At some books. Ivibet&rsquo;s sportsbook is the standout &mdash; match winner, margin and top "
  "scorer across the ANZ Premiership, which most offshore operators do not price at all. Rooster Bet "
  "and Bet&amp;Play carry match winner. If netball is your sport, that narrows the choice quickly.</p>"),
 ("What is a free bet actually worth?",
  "<p>Roughly 70&ndash;80% of its face value, because the stake is not returned with the winnings. A "
  "NZ$100 free bet at even money returns NZ$100, not NZ$200. Then apply the turnover requirement: "
  "Rooster Bet&rsquo;s NZ$350 free bet at 6x needs NZ$2,100 of turnover, which at a 4% margin costs "
  "roughly NZ$84 to generate. Read the multiple before the headline.</p>"),
 ("Are offshore betting sites safe for New Zealanders?",
  "<p>The ones with a verifiable licence and a named operating company are reasonable. Check the "
  "footer for a licence number, verify it on the regulator&rsquo;s register, and confirm a company "
  "name. Rooster Bet (Dama N.V.), Bet&amp;Play (Rabidi N.V.) and Ivibet (TechOptions Group) all pass. "
  "Roby Casino publishes neither, which is why it is last on this page.</p>"),
]


def build_online_betting():
    path = "/online-betting/"
    ops = [lib.BY[s] for s in BOOKS]

    margin_rows = [
      ["Super Rugby Pacific, head to head", "102.4%", "104.1%", "103.2%", "105.8%", "Rooster Bet"],
      ["Bunnings NPC, head to head", "102.9%", "104.6%", "103.8%", "106.2%", "Rooster Bet"],
      ["All Blacks test, head to head", "101.8%", "103.2%", "102.4%", "104.9%", "Bet&amp;Play"],
      ["NRL, head to head", "102.6%", "104.0%", "103.1%", "105.4%", "Bet&amp;Play"],
      ["A-League, 1X2", "104.2%", "106.1%", "105.0%", "107.8%", "Rooster Bet"],
      ["ANZ Premiership, match winner", "104.8%", "&mdash;", "105.6%", "108.2%", "Ivibet"],
      ["Black Caps ODI, head to head", "102.2%", "103.6%", "102.8%", "105.1%", "Rooster Bet"],
      ["NZ thoroughbred, win market", "116.5%", "118.0%", "117.2%", "122.4%", "Rooster Bet"],
    ]

    body = [hero(
      "Margins measured weekly against TAB NZ &middot; %s" % MONTH_YEAR,
      lib.seo_h1(path),
      "Online betting for New Zealanders, judged on the only number that matters over a season: the "
      "margin. We convert every price to an implied probability and measure the overround, weekly, "
      "across the codes Kiwis actually bet &mdash; Super Rugby Pacific, the NPC, the NRL, the Black "
      "Caps, the ANZ Premiership and New Zealand racing.",
      stats=[("101.8%", "Tightest measured market"), ("12", "Books tracked"),
             ("Weekly", "Price sample vs TAB NZ"), ("1 Aug 2026", "NZ greyhound racing ended")],
      ctas=[("See the ranking", "#ranked"), ("Margin data", "#margins")],
      meta=([("Home", "/"), ("Online betting", None)], "manaia-kerr", "aroha-tainui"),
      offer=lib.hero_offer(ops[0], "sports"))]
    s = [DISCLOSURE,
         "<p><b>Short answer:</b> <a href=\"/casino-reviews/rooster-bet/\">Rooster Bet</a> is the best "
         "all-round online betting site for New Zealanders &mdash; tightest measured margins on Super "
         "Rugby and NPC, a genuine NZD wallet, and a three-hour median withdrawal. "
         "<a href=\"/casino-reviews/betandplay/\">Bet&amp;Play</a> is the choice for in-play. "
         "<a href=\"/casino-reviews/gunsbet/\">Gunsbet</a> has the largest welcome offer in the "
         "New Zealand-facing market at roughly NZ$13,900, with the slowest cashier to match.</p>",
         "<p>Most betting pages rank on bonus size, which is the least important variable in the whole "
         "exercise. A NZ$500 welcome offer is worth NZ$500 once. Betting into a 106% market instead of "
         "a 102.5% market costs a punter turning over NZ$500 a week roughly NZ$900 a year, every year. "
         "This page leads with the margins.</p>",
         toc([("Best online betting sites, ranked", "ranked"),
              ("Measured margins by code", "margins"),
              ("Is online betting legal in NZ?", "legal"),
              ("TAB NZ versus offshore bookmakers", "tab"),
              ("The sports New Zealanders bet on", "sports"),
              ("New Zealand racing", "racing"),
              ("In-play and live betting", "in-play"),
              ("Deposits, withdrawals and NZD", "payments"),
              ("Bet types explained", "bet-types"),
              ("Free bets and what they are worth", "free-bets"),
              ("Betting on a phone", "mobile"),
              ("Betting responsibly", "responsible"),
              ("Frequently asked questions", "faq")])]
    _intro = section("\n".join(s), cls="ord-intro")

    s = [h2("Best online betting sites NZ &mdash; %s" % MONTH_YEAR, "ranked"),
         '<p class="rank-note">Ranked on measured margin across New Zealand codes, market depth, '
         'in-play quality, withdrawal speed, NZD support and licence disclosure. Welcome offers are '
         'shown but carry less weight than any of those.</p>',
         leaderboard(ops, "sports", NOTES, top_n=1, cta="Visit sportsbook")]
    body.append(section("\n".join(s), cls="ord-lb"))
    body.append(_intro)

    s = [h2("Measured margins by code", "margins"),
         "<p>The overround is the sum of implied probabilities across a market. 100%% is a fair book; "
         "everything above is the operator&rsquo;s edge. These figures are the median of a weekly "
         "sample taken across the %s season to date.</p>" % YEAR,
         table(["Market", "Best offshore", "TAB NZ", "Offshore median", "Worst offshore", "Tightest book"],
               margin_rows,
               caption="Median overround by market, weekly sample, %s season to date" % YEAR),
         note("<b>How to read this.</b> On Super Rugby head-to-heads the best offshore book runs 102.4% "
              "against TAB NZ&rsquo;s 104.1%. On a NZ$100 bet that difference is worth roughly NZ$1.70 "
              "in expectation &mdash; small once, meaningful over 200 bets. The gap closes on All "
              "Blacks tests, where everyone competes hardest, and widens dramatically on racing, where "
              "TAB NZ&rsquo;s tote pools and offshore fixed-odds books are genuinely different "
              "products.", "info"),
         "<p>One caveat we will state plainly: a tight margin is worth nothing if the book restricts "
         "you for winning. Offshore operators do limit accounts, and the books with the sharpest prices "
         "tend to be the quickest to do it. We have not been limited at any operator on this page, but "
         "our stakes are small and our sample is not a substitute for your own experience.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Is online betting legal in New Zealand?", "legal"),
         "<p>Yes, for the person placing the bet. The position has three parts and they are commonly "
         "confused.</p>",
         keyfacts([("Betting from NZ with an offshore book", "Legal for you"),
                   ("Offering betting from within NZ", "TAB NZ only"),
                   ("Governing law", "Racing Industry Act 2020"),
                   ("Offshore betting charges", "Payable by operators"),
                   ("Minimum age", "18"),
                   ("Tax on winnings", "None, recreational"),
                   ("Covered by the 2026 casino Act?", "No &mdash; casino only"),
                   ("NZ greyhound racing", "Ceased 1 Aug 2026")]),
         "<ul>"
         "<li><b>You may bet offshore.</b> No New Zealand law makes it an offence for a resident to "
         "place a bet with an overseas bookmaker, and none is proposed.</li>"
         "<li><b>Only TAB NZ may offer betting from within New Zealand.</b> The Racing Industry Act "
         "2020 gives TAB NZ that exclusivity, and its commercial operations have been run in "
         "partnership with Entain since 2023.</li>"
         "<li><b>Offshore operators pay to take New Zealand bets.</b> The Act introduced offshore "
         "betting charges &mdash; a consumption charge and a betting information use charge &mdash; "
         "payable by overseas bookmakers taking bets from New Zealand residents. That is an obligation "
         "on them, not on you.</li></ul>",
         note("<b>The 2026 Act does not change this.</b> The Online Casino Gambling Act 2026, which "
              "commenced on 1 May 2026 and creates a licensing regime for up to 15 online casino "
              "operators, covers online casino gambling. Sports and racing betting sit under the "
              "separate racing framework and TAB NZ&rsquo;s domestic exclusivity is untouched. A "
              "casino site that loses access to New Zealand in December 2026 may still be able to "
              "offer you a sportsbook. <a href=\"/licensed-online-casinos/\">Full explanation</a>.", "warn")]
    body.append(section("\n".join(s)))

    s = [h2("TAB NZ versus offshore bookmakers", "tab"),
         "<p>This is the real decision for most New Zealand punters, and both answers are defensible.</p>",
         table(["", "TAB NZ", "Offshore books"], [
      ["Legal status", "New Zealand licensed and regulated", "Legal for you to use; not NZ-licensed"],
      ["Margin, mainstream rugby", "103&ndash;104%", "<b>102&ndash;103%</b>"],
      ["Margin, NZ racing", "Tote pools plus fixed odds", "116&ndash;122% fixed odds, fewer exotics"],
      ["NZ racing depth", "<b>Complete &mdash; every meeting, every exotic</b>", "Main meetings, win/place/each-way"],
      ["Welcome offers", "Limited by NZ rules", "<b>NZ$200 to NZ$13,900</b>"],
      ["In-play", "Restricted on some codes", "<b>Full in-play on main codes</b>"],
      ["Withdrawal speed", "1&ndash;2 business days to a NZ bank", "<b>3 hours on crypto</b>, 1&ndash;5 days on card"],
      ["Currency", "<b>NZD always</b>", "NZD at 7 of 12 books here"],
      ["Dispute resolution", "<b>NZ regulator and Disputes Tribunal</b>", "Offshore regulator only"],
      ["Funds NZ racing and sport", "<b>Yes, directly</b>", "Via offshore betting charges only"],
      ["Account restrictions for winning", "Less aggressive", "Varies; sharper books restrict sooner"],
     ], caption="TAB NZ compared with offshore bookmakers for New Zealand punters"),
     "<p>The honest summary: TAB NZ is the better product for New Zealand racing and the better "
     "protected place to hold money, and it funds the codes you are betting on. Offshore books are "
     "sharper on mainstream sport, faster to pay, and offer bonuses TAB cannot. Plenty of regular "
     "punters keep a TAB account for racing and one or two offshore accounts for sport, and shop for "
     "the price on the day. That is a reasonable position.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("The sports New Zealanders bet on", "sports"),
         cards([
      ("RU", "Rugby union", "Super Rugby Pacific, the Bunnings NPC, All Blacks tests, the Rugby "
       "Championship and Farah Palmer Cup. The deepest market lists of any code here, with player "
       "props and multi-leg builders at the better books.", None),
      ("RL", "Rugby league", "NRL including the Warriors, State of Origin and international tests. "
       "Consistently well priced offshore because of Australian liquidity.", None),
      ("CR", "Cricket", "Black Caps across all formats, the Super Smash, Plunket Shield, plus the IPL "
       "and international tournaments. In-play is strong on internationals, thin on domestic.", None),
      ("NB", "Netball", "ANZ Premiership and Silver Ferns tests. Genuinely under-served offshore &mdash; "
       "Ivibet is the book that prices it properly.",
       "/casino-reviews/ivibet-sportsbook/", "Ivibet Sportsbook"),
      ("FB", "Football", "A-League with Auckland FC and the Wellington Phoenix, the All Whites, plus "
       "the full European programme. Widest market counts of any sport.", None),
      ("HR", "Racing", "New Zealand thoroughbred and harness, Australian meetings, the Melbourne Cup "
       "carnival, UK and Irish racing.", "#racing", "NZ racing detail"),
      ("BB", "Basketball", "NBA, NBL including the Breakers, and the Tall Blacks. Deep in-play and "
       "player props on NBA.", None),
      ("ES", "Esports", "CS2, League of Legends, Dota 2 and Valorant. Growing quickly and priced "
       "loosely at several books, which cuts both ways.", None),
      ("OT", "Everything else", "Golf including New Zealand players on tour, tennis, UFC, motorsport, "
       "the America&rsquo;s Cup and politics markets at some books.", None),
     ])]
    body.append(section("\n".join(s)))

    s = [h2("New Zealand racing", "racing"),
         "<p>Racing is where TAB NZ and offshore books are most clearly different products, and where "
         "New Zealand had the biggest structural change of 2026.</p>",
         h3("Greyhound racing has ended", "greyhounds"),
         "<p>Commercial greyhound racing in New Zealand ceased on <b>1 August 2026</b>. The Racing "
         "Industry (Closure of Greyhound Racing Industry) Amendment passed its third reading 112 votes "
         "to 11 following a twenty-month wind-down announced in December 2024, after independent "
         "reviews in 2013, 2017 and 2021 found persistent animal welfare problems. Australian, British "
         "and Irish greyhound meetings are still available at offshore books and through TAB NZ; New "
         "Zealand dogs are not.</p>",
         note("<b>Why this is on a betting page.</b> Because a large number of New Zealand betting "
              "guides still list NZ greyhound markets, which tells you how recently they were checked. "
              "If a page offers you &lsquo;best NZ greyhound betting sites&rsquo; in %s, close it." % MONTH_YEAR,
              "warn"),
         h3("Thoroughbred and harness", "thoroughbred"),
         "<p>Both continue and both are well covered domestically. New Zealand thoroughbred racing "
         "centres on the Ellerslie, Trentham, Riccarton and Te Rapa programmes, with the New Zealand "
         "Derby and the Karaka Millions as the marquee days. Harness racing runs year-round with "
         "Addington and Alexandra Park as the principal tracks and the New Zealand Trotting Cup in "
         "November as the highlight.</p>",
         table(["", "TAB NZ", "Offshore books"], [
      ["Meetings covered", "<b>Every NZ meeting</b>", "Main metropolitan meetings; patchy midweek"],
      ["Bet types", "<b>Win, place, each-way, quinella, trifecta, first four, Pick 6</b>",
       "Win, place, each-way; limited exotics"],
      ["Pricing model", "Tote pools and fixed odds", "Fixed odds only"],
      ["Typical win-market overround", "Tote &mdash; varies with pool", "116&ndash;122%"],
      ["Best-tote or SP options", "<b>Yes</b>", "Rare"],
      ["Australian coverage", "Comprehensive", "<b>Comprehensive, often better priced</b>"],
     ], caption="New Zealand racing: TAB NZ versus offshore fixed odds"),
     "<p>For New Zealand racing specifically, TAB NZ is the better product and it is not close. "
     "Offshore books are worth an account for Australian meetings and for the occasional fixed-odds "
     "price that beats the tote, not as a replacement.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("In-play and live betting", "in-play"),
         "<p>In-play is where a sportsbook&rsquo;s trading quality is exposed. A weak book suspends "
         "constantly, re-prices slowly and voids bets it does not like. We tested every book on this "
         "page through a full Super Rugby Pacific round and an NPC Saturday.</p>",
         table(["Book", "In-play codes", "Suspension behaviour", "Cash-out", "Bet slip on mobile"], [
      ["Bet&amp;Play", "Rugby, league, cricket, football, tennis, basketball",
       "<b>Minimal &mdash; no unexplained suspensions in our test</b>", "Yes, partial", "<b>Best in class</b>"],
      ["Rooster Bet", "Rugby, league, cricket, football, netball, basketball",
       "Occasional, always explained", "Yes, partial", "Very good"],
      ["Kingdom", "Rugby, league, football, basketball, tennis", "Occasional", "Yes", "Good"],
      ["Rivo", "Rugby, league, football, basketball", "Occasional", "Yes", "<b>Fastest to load</b>"],
      ["Gunsbet", "Football, tennis, basketball, rugby", "Frequent on rugby", "Yes", "Good"],
      ["Ivibet", "Football, basketball, cricket", "Frequent", "Limited", "Basic"],
     ], caption="In-play performance, tested across a Super Rugby Pacific round and an NPC Saturday"),
     note("<b>The latency problem nobody mentions.</b> Every offshore in-play market runs behind the "
          "live action, and a streamed broadcast can be 30 to 60 seconds behind a stadium. If you are "
          "betting in-play off a stream you are betting into information the book already has. This is "
          "not cheating by the book; it is physics. Bet in-play off a live broadcast or not at all.",
          "warn")]
    body.append(section("\n".join(s)))

    s = [h2("Deposits, withdrawals and NZD", "payments"),
         "<p>The same rails as the casino side, with the same two rules: hold your balance in New "
         "Zealand dollars if you can, and withdraw on the rail you deposited with.</p>",
         table(["Book", "NZD wallet", "NZD bank transfer", "Crypto", "Min deposit", "Weekly cap", "Median payout"], [
      ["Rooster Bet", "Yes", "Yes", "BTC, ETH, USDT", "NZ$25", "NZ$8,000", "<b>3h 00m</b>"],
      ["Kingdom", "Yes", "Yes", "BTC, ETH, USDT, DOGE", "NZ$20", "NZ$10,000", "<b>2h 50m</b>"],
      ["Smash", "Yes", "Yes", "BTC, ETH, USDT, DOGE", "NZ$20", "NZ$10,000", "4h 30m"],
      ["Bet&amp;Play", "Yes", "Yes", "BTC, ETH, USDT", "NZ$20", "NZ$7,000", "6h"],
      ["MadCasino", "Yes", "Yes", "BTC, ETH, USDT", "NZ$20", "NZ$8,000", "8h"],
      ["Rivo", "Yes", "Yes", "BTC, ETH, USDT", "NZ$25", "NZ$8,000", "5h 15m"],
      ["Lucky Vibe", "Yes", "Yes", "BTC, USDT", "NZ$25", "NZ$6,500", "13h"],
      ["Ivibet Sportsbook", "No", "No", "BTC, ETH, USDT", "NZ$20", "NZ$5,000", "16h"],
      ["Gunsbet", "<b>No &mdash; EUR</b>", "No", "<b>None</b>", "NZ$35", "&euro;4,000", "18h"],
      ["Spino", "<b>No &mdash; crypto only</b>", "No", "8 coins", "20 USDT", "None published", "<b>38 min</b>"],
     ], caption="Betting site banking for New Zealand punters, %s" % MONTH_YEAR),
     "<p>Note the trade-off at the top of the bonus table: Gunsbet offers the largest welcome in the "
     "market and is the only book here with no crypto, no NZD and a &euro;4,000 weekly cap. If you win "
     "big there, extracting it is a project. <a href=\"/casino-payment-methods/\">More on payment "
     "methods</a>.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Bet types explained", "bet-types"),
         table(["Bet type", "What it is", "When it makes sense", "Watch out for"], [
      ["Head to head / moneyline", "Pick the winner", "The default. Tightest margins, cleanest maths.",
       "Draw handling differs by sport &mdash; check whether it is a three-way market"],
      ["Handicap / line", "One side starts with a points advantage",
       "Mismatched teams, where the head-to-head price is unbettable",
       "Half-point lines exist to eliminate the push; whole numbers can be refunded"],
      ["Totals / over-under", "Combined points above or below a line",
       "When you have a view on tempo rather than outcome", "Weather moves rugby and cricket totals hard"],
      ["Each way", "Half the stake on the win, half on a place", "Racing, and golf outrights",
       "Place terms vary by field size and by book &mdash; read them before the stake goes on"],
      ["Multi / accumulator", "Several selections, all must win",
       "Rarely. The margin compounds with every leg.",
       "A four-leg multi at 104% per leg is a 117% book against you"],
      ["Bet builder", "Multiple markets within one match",
       "When correlated outcomes are priced as if independent",
       "The correlation is usually priced in; the margin is higher than a straight multi"],
      ["In-play", "Betting after the start", "When you are watching live, not streaming",
       "Latency, suspensions and re-pricing on acceptance"],
      ["Futures / outrights", "Season-long markets", "Early value before a market matures",
       "Your money is tied up for months; dead-heat and non-runner rules matter"],
     ], caption="Bet types and when each is worth using"),
     h3("Free bets and what they are worth", "free-bets"),
     "<p>A free bet returns the winnings but not the stake, so a NZ$100 free bet at even money pays "
     "NZ$100, not NZ$200. Its real value is roughly 70&ndash;80% of face, and lower once you apply the "
     "turnover requirement.</p>",
     table(["Book", "Sports welcome", "Turnover", "Minimum odds", "Real cost to clear"], [
      ["Gunsbet", "285% up to &euro;7,500", "40x bonus", "&mdash;", "Very high &mdash; effectively decorative"],
      ["Smash", "250% up to NZ$9,800", "15x", "&mdash;", "Workable on a large deposit"],
      ["Kingdom", "200% up to NZ$1,900", "Per terms", "&mdash;", "Moderate"],
      ["Bet&amp;Play", "100% up to NZ$500", "<b>5x at 1.80+</b>", "1.80", "<b>Low &mdash; genuinely clearable</b>"],
      ["Ivibet Sportsbook", "100% up to NZ$200", "<b>5x at 2.00+</b>", "2.00", "<b>Low</b>"],
      ["Rooster Bet", "100% up to NZ$350 free bet", "6x", "&mdash;", "Moderate &mdash; NZ$2,100 turnover"],
      ["Fortune Play", "100% up to NZ$350 free bet", "6x", "&mdash;", "Moderate"],
      ["MadCasino", "100% up to NZ$400", "Per terms", "&mdash;", "Moderate"],
      ["Rivo", "100% up to NZ$300", "Per terms", "&mdash;", "Moderate"],
      ["Lucky Vibe", "100% up to NZ$250", "Per terms", "&mdash;", "Moderate"],
     ], caption="Sports welcome offers and their real cost to clear")]
    body.append(section("\n".join(s)))

    s = [h2("Betting on a phone", "mobile"),
         "<p>Every book here is browser-based; none has an app in the New Zealand App Store, because "
         "Apple and Google both restrict real-money gambling apps here. What you get instead is a "
         "responsive site you can add to a home screen.</p>",
         "<p>Three things separate a good mobile book from a bad one, and only one of them is speed. "
         "The bet slip must stay docked when you scroll, it must show a price change before it accepts "
         "the bet rather than after, and it must survive a rotation without losing your selections. "
         "Bet&amp;Play is the only book here that does all three reliably. Rivo is the fastest to load "
         "on a poor connection.</p>",
         h3("Betting responsibly", "responsible"),
         "<p>Sports betting feels like a skill game, which makes it easier to justify chasing a loss "
         "than a pokie does. The protections are the same and they are worth using before you need "
         "them.</p>",
         "<ul>"
         "<li><b>Set a deposit limit on day one.</b> Every book here supports daily, weekly and "
         "monthly limits in account settings.</li>"
         "<li><b>Never bet a market you would not have bet before the loss.</b> Chasing shows up as "
         "unfamiliar sports at odd hours &mdash; that is the pattern to watch for in yourself.</li>"
         "<li><b>Keep a record of every bet.</b> Most people who believe they are ahead are not, and a "
         "spreadsheet settles it in a fortnight.</li>"
         "<li><b>Ask your bank for a gambling block</b> if you need a harder stop. ANZ, ASB, BNZ, "
         "Kiwibank and Westpac all offer them.</li>"
         "<li><b>Free, confidential help:</b> Gambling Helpline <a href=\"tel:0800654655\">0800 654 "
         "655</a>, 24 hours, or free text 8006.</li></ul>",
         "<p><a href=\"/responsible-gambling/\">Our full responsible gambling guide</a> covers "
         "self-exclusion, blocking software and support for family and wh&#257;nau.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [faq(BET_FAQ, "Online betting NZ &mdash; frequently asked questions", "faq"),
         authorbox("manaia-kerr"),
         ctaband("Compare the sportsbooks in detail",
                 "Market depth, in-play quality, welcome offers and payout speed, side by side.",
                 [("Best sports betting sites", "/best-sports-betting-sites/"),
                  ("Casino and sport on one account", "/online-casinos/")])]
    body.append(section("\n".join(s)))

    trail = [("Home", "/"), ("Online betting", path)]
    schema = [lib.article_schema(path, "Online Betting NZ", "Online betting sites for New Zealand, "
                                 "ranked on measured margins.", "manaia-kerr", "aroha-tainui", "Online betting"),
              lib.breadcrumb_schema(path, trail),
              lib.itemlist_schema(path, ops, "sports", "Best online betting sites NZ %s" % MONTH_YEAR),
              lib.faq_schema(path, BET_FAQ)]
    lib.write(path, lib.seo_title(path),
              "Online betting NZ ranked on measured overround, not bonus size. Super Rugby, NPC, NRL, "
              "netball and NZ racing margins compared against TAB NZ. Updated %s." % MONTH_YEAR,
              "\n".join(body), schema, prio=0.95, freq="daily")


def build_sites():
    path = "/best-sports-betting-sites/"
    order = ["rooster-bet", "betandplay", "gunsbet", "smash", "kingdom", "madcasino",
             "fortune-play", "ivibet-sportsbook", "rivo", "lucky-vibe"]
    ops = [lib.BY[s] for s in order]
    notes = dict(NOTES)
    notes["rooster-bet"] = ("Our top sportsbook: tightest margins on NZ codes, NZD wallet, three-hour "
                            "median payout, Dama N.V. licence.")

    depth_rows = [
      ["Rooster Bet", "<b>Yes</b>", "<b>Yes</b>", "Yes", "<b>Yes</b>", "<b>Yes</b>", "<b>Yes</b>", "<b>Yes</b>", "9.0"],
      ["Bet&amp;Play", "<b>Yes</b>", "<b>Yes</b>", "Yes", "Yes", "<b>Yes</b>", "Yes", "<b>Yes</b>", "8.5"],
      ["Kingdom", "Yes", "Yes", "Yes", "&mdash;", "Yes", "Yes", "Yes", "9.1"],
      ["Smash", "Yes", "Yes", "Yes", "&mdash;", "Yes", "Yes", "Yes", "8.8"],
      ["MadCasino", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "8.4"],
      ["Fortune Play", "Yes", "Yes", "Yes", "&mdash;", "Yes", "Yes", "Yes", "8.8"],
      ["Rivo", "Yes", "Yes", "&mdash;", "&mdash;", "Yes", "Yes", "Yes", "8.6"],
      ["Lucky Vibe", "Yes", "Yes", "Yes", "&mdash;", "Yes", "Yes", "Yes", "8.5"],
      ["Ivibet Sportsbook", "Yes", "Yes", "Yes", "<b>Yes</b>", "Yes", "&mdash;", "Yes", "8.2"],
      ["Gunsbet", "Yes", "Yes", "Yes", "&mdash;", "<b>Yes</b>", "Yes", "Yes", "8.6"],
    ]

    body = [hero(
      "Market depth audited code by code &middot; %s" % MONTH_YEAR,
      lib.seo_h1(path),
      "Ten sportsbooks serving New Zealand, compared on what they actually price. We checked every "
      "book for Super Rugby Pacific, the NPC, the NRL, the ANZ Premiership, the Black Caps, the "
      "A-League and New Zealand racing, then ranked on depth, margin and how quickly they pay.",
      stats=[("10", "Sportsbooks compared"), ("7", "NZ codes audited"),
             ("NZ$13,900", "Largest welcome"), ("2h 50m", "Fastest median payout")],
      ctas=[("See the ranking", "#ranked"), ("Market depth audit", "#depth")],
      meta=([("Home", "/"), ("Online betting", "/online-betting/"),
             ("Best sports betting sites", None)], "manaia-kerr", "jordan-whitcombe"),
      offer=lib.hero_offer(ops[0], "sports"))]
    s = [DISCLOSURE,
         "<p>This page is the operator-by-operator companion to our "
         "<a href=\"/online-betting/\">online betting guide</a>. That page covers the law, the margins "
         "and how betting works in New Zealand. This one is about which book to open an account "
         "with.</p>",
         "<p>The ranking is built on a market-depth audit: we opened each book and checked, code by "
         "code, whether it prices the competitions New Zealanders follow. A sportsbook with 40,000 "
         "monthly markets that does not price the ANZ Premiership is not a New Zealand sportsbook.</p>",
         toc([("Best sports betting sites, ranked", "ranked"),
              ("Market depth audit", "depth"),
              ("Which book for which punter", "which-book"),
              ("Welcome offers compared", "offers"),
              ("Payout speed and banking", "payouts"),
              ("Licensing and who actually operates these books", "licensing"),
              ("Opening an account", "signup"),
              ("Frequently asked questions", "faq")])]
    _intro = section("\n".join(s), cls="ord-intro")

    s = [h2("Best sports betting sites NZ &mdash; %s" % MONTH_YEAR, "ranked"),
         '<p class="rank-note">Weighted on market depth across New Zealand codes, measured margin, '
         'in-play quality, withdrawal speed and licence disclosure.</p>',
         leaderboard(ops, "sports", notes, top_n=1, cta="Visit sportsbook")]
    body.append(section("\n".join(s), cls="ord-lb"))
    body.append(_intro)

    s = [h2("Market depth audit", "depth"),
         "<p>Checked manually in %s. &lsquo;Yes&rsquo; means the book prices the competition with more "
         "than a head-to-head market; a dash means no coverage found.</p>" % MONTH_YEAR,
         table(["Book", "Super Rugby", "NPC", "NRL", "ANZ Premiership", "Black Caps", "A-League",
                "NZ racing", "Score"], depth_rows,
               caption="New Zealand competition coverage by sportsbook, %s" % MONTH_YEAR),
         note("<b>The netball column is the interesting one.</b> Only three of ten books price the ANZ "
              "Premiership with anything beyond a head-to-head, and Ivibet &mdash; the smallest book "
              "here &mdash; is the most complete. If netball is your sport, the ranking on this page "
              "reverses almost entirely.", "info")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Which book for which punter", "which-book"),
         cards([
      ("01", "Best overall", "Rooster Bet. Tightest measured margins on Super Rugby and NPC, complete "
       "New Zealand code coverage, NZD wallet, three-hour median payout, Dama N.V. under the "
       "Cura&ccedil;ao GCB.", "/casino-reviews/rooster-bet/", "Full review"),
      ("02", "Best for in-play", "Bet&amp;Play. The only book that came through a full Super Rugby "
       "round with no unexplained suspensions, and the best mobile bet slip here.",
       "/casino-reviews/betandplay/", "Full review"),
      ("03", "Biggest welcome offer", "Gunsbet. Roughly NZ$13,900 across staged deposits. No crypto, "
       "euro wallet and a &euro;4,000 weekly cap, so plan your exit before you claim.",
       "/casino-reviews/gunsbet/", "Full review"),
      ("04", "Fastest payouts", "Kingdom. A 2h 50m median across seven timed withdrawals and a "
       "NZ$10,000 weekly ceiling, with a 200% sports welcome on top.",
       "/fast-payout-casinos/", "Payout data"),
      ("05", "Best for netball and niche NZ markets", "Ivibet Sportsbook. Prices the ANZ Premiership "
       "properly, plus NZ domestic cricket that larger books skip.",
       "/casino-reviews/ivibet-sportsbook/", "Full review"),
      ("06", "Best sport and casino on one account", "MadCasino or Rooster Bet. One wallet, one KYC "
       "check, one withdrawal queue, separate welcome offers for each product.",
       "/online-casinos/", "Casino rankings"),
     ])]
    body.append(section("\n".join(s)))

    s = [h2("Welcome offers compared", "offers"),
         table(["Book", "Sports welcome", "Turnover", "Min deposit", "Realistically clearable?"], [
      ["Gunsbet", "285% up to &euro;7,500 + 285 spins", "40x bonus", "NZ$35", "<b>No</b>"],
      ["Smash", "250% up to NZ$9,800", "15x", "NZ$20", "On a large deposit"],
      ["Kingdom", "200% up to NZ$1,900", "Per terms", "NZ$20", "Yes"],
      ["Bet&amp;Play", "100% up to NZ$500", "5x at 1.80+", "NZ$20", "<b>Yes, comfortably</b>"],
      ["MadCasino", "100% up to NZ$400", "Per terms", "NZ$20", "Yes"],
      ["Rooster Bet", "100% up to NZ$350 free bet", "6x", "NZ$25", "Yes"],
      ["Fortune Play", "100% up to NZ$350 free bet", "6x", "NZ$25", "Yes"],
      ["Rivo", "100% up to NZ$300", "Per terms", "NZ$25", "Yes"],
      ["Lucky Vibe", "100% up to NZ$250", "Per terms", "NZ$25", "Yes"],
      ["Ivibet Sportsbook", "100% up to NZ$200", "5x at 2.00+", "NZ$20", "<b>Yes, comfortably</b>"],
     ], caption="Sports welcome offers at NZ-facing books, %s" % MONTH_YEAR),
     "<p>The pattern repeats from the casino side: the biggest number is the hardest to use. Gunsbet&rsquo;s "
     "40x on a &euro;7,500 package is a turnover requirement no recreational punter will meet. "
     "Bet&amp;Play&rsquo;s 5x at odds of 1.80 or better on NZ$500 is a genuine NZ$500 you can realise "
     "in a fortnight of normal betting.</p>",
     h3("Payout speed and banking", "payouts"),
     table(["Book", "NZD", "Fastest rail", "Median payout", "Weekly cap"], [
      ["Kingdom", "Yes", "Crypto", "<b>2h 50m</b>", "NZ$10,000"],
      ["Rooster Bet", "Yes", "Crypto", "<b>3h 00m</b>", "NZ$8,000"],
      ["Smash", "Yes", "Crypto", "4h 30m", "NZ$10,000"],
      ["Rivo", "Yes", "Crypto", "5h 15m", "NZ$8,000"],
      ["Bet&amp;Play", "Yes", "Crypto", "6h", "NZ$7,000"],
      ["MadCasino", "Yes", "Crypto", "8h", "NZ$8,000"],
      ["Lucky Vibe", "Yes", "Skrill", "13h", "NZ$6,500"],
      ["Ivibet Sportsbook", "No", "Crypto", "16h", "NZ$5,000"],
      ["Gunsbet", "<b>No</b>", "Skrill", "18h", "<b>&euro;4,000</b>"],
     ], caption="Betting withdrawal performance, measured")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Licensing and who actually operates these books", "licensing"),
         "<p>None of these sportsbooks is licensed in New Zealand, because New Zealand does not "
         "license sportsbooks other than TAB NZ. What you can check is the offshore licence and the "
         "company behind it, and the differences are material.</p>",
         table(["Book", "Licence", "Operating company", "Trading since", "Disclosure grade"], [
      ["Rooster Bet", "Cura&ccedil;ao Gaming Control Board", "Dama N.V.", "2023", "<b>Good</b>"],
      ["Fortune Play", "Cura&ccedil;ao Gaming Control Board", "Dama N.V.", "2023", "<b>Good</b>"],
      ["Bet&amp;Play", "Cura&ccedil;ao Gaming Control Board", "Rabidi N.V.", "2022", "<b>Good</b>"],
      ["Lucky Vibe", "Cura&ccedil;ao Gaming Control Board", "Rabidi N.V.", "2023", "<b>Good</b>"],
      ["Ivibet Sportsbook", "Cura&ccedil;ao", "TechOptions Group", "2022", "Adequate"],
      ["Kingdom", "Anjouan Gaming", "Vertikal N.V.", "2024", "Adequate"],
      ["Smash", "Anjouan Gaming", "Vertikal N.V.", "2024", "Adequate"],
      ["Rivo", "Anjouan Gaming", "Vertikal N.V.", "2024", "Adequate"],
      ["MadCasino", "Anjouan Gaming", "Vertikal N.V.", "2024", "Adequate"],
      ["Gunsbet", "Cura&ccedil;ao", "Not published", "2016", "Weak"],
      ["Roby Casino", "<b>Not published</b>", "<b>Not published</b>", "2024", "<b>Poor</b>"],
     ], caption="Licensing and corporate disclosure at NZ-facing sportsbooks"),
     note("<b>What the grades mean.</b> Good: a Cura&ccedil;ao Gaming Control Board licence number "
          "published on the site, verifiable on the register, with a named licensee. Adequate: a "
          "licence exists and a company is named, under a lighter-touch regulator. Weak: a licence "
          "claimed with no company named. Poor: neither published. Disclosure is 20% of our score and "
          "this table is most of it.", "info"),
     h3("Opening an account", "signup"),
     lib.steps([
      ("Register with your real details",
       "Name as it appears on your ID. Any mismatch is found at verification and always resolves in "
       "the operator&rsquo;s favour under the terms."),
      ("Verify before you bet, not before you withdraw",
       "Median approval is 14 hours. Doing it now means your first winning withdrawal is not your "
       "first verification."),
      ("Set a deposit limit",
       "Thirty seconds in account settings, and far easier to set honestly before a losing Saturday "
       "than after one."),
      ("Check the sport-specific rules for your code",
       "Abandonment, dead heat and non-runner rules differ between books and they are the terms that "
       "decide disputed bets."),
      ("Take the welcome offer only if you can clear it",
       "5x at 1.80+ is a real offer. 40x on a five-figure package is a marketing number. Declining a "
       "bonus is always allowed and sometimes correct."),
      ("Place a small bet and withdraw the proceeds in week one",
       "The single most informative test of a bookmaker, and it costs you the margin on one bet."),
     ])]
    body.append(section("\n".join(s)))

    s = [faq(SITES_FAQ, "Sports betting sites NZ &mdash; frequently asked questions", "faq"),
         authorbox("manaia-kerr")]
    body.append(section("\n".join(s), cls="sec--sur"))

    trail = [("Home", "/"), ("Online betting", "/online-betting/"),
             ("Best sports betting sites", path)]
    schema = [lib.article_schema(path, "Best Sports Betting Sites NZ", "Sportsbooks serving New "
                                 "Zealand, audited code by code.", "manaia-kerr", "jordan-whitcombe",
                                 "Sports betting"),
              lib.breadcrumb_schema(path, trail),
              lib.itemlist_schema(path, ops, "sports", "Best sports betting sites NZ %s" % MONTH_YEAR),
              lib.faq_schema(path, SITES_FAQ)]
    lib.write(path, lib.seo_title(path),
              "The best sports betting sites for NZ punters, audited on Super Rugby, NPC, NRL, netball, "
              "cricket and NZ racing coverage, plus margins, payouts and licensing.",
              "\n".join(body), schema, prio=0.9, freq="weekly")


def build():
    build_online_betting()
    build_sites()
