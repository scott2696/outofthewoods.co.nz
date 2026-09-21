# Title tags and H1s — competitor-derived, pixel-measured

Every title tag and every H1 on the site now follows one format:

```
Primary Keyword [Month Year]: Secondary Keyword
```
Title tags are constrained to **580px** (Arial 20px, Google's desktop SERP
truncation point). H1s use the same format with no width ceiling, so they
carry the fuller secondary phrase.

---

## How the widths are enforced

Character counts are the wrong unit — *Wellington* and *Illinois* are both 10
characters and 38% apart in rendered width. `lib.serp_px()` measures the real
Arial advance width from a metrics table, and `lib.write()` **refuses to build**
a page whose title exceeds 580px:

```python
px = serp_px(title)
if px > SERP_LIMIT:
    raise ValueError("title too wide for the SERP: %.1fpx > %dpx on %s" % (px, SERP_LIMIT, path))
```

`lib.fit(primary, candidates)` takes a richest-first list of secondary keywords
and returns the widest one that still fits. That is why `Ivibet Sportsbook
Review` gets a shorter secondary than `Rivo Casino Review` — the primary eats
more of the budget.

Current spread across all 47 pages: **min 470px, median 547px, max 579px**.
Nothing is over budget, and nothing is wastefully short.

---

## Competitor keyword analysis and the resulting titles

The **primary** is the head term the ranking competitors put first in their own
title tags. The **secondary** is the modifier they most consistently pair with
it. Both were taken from live SERP titles in September 2026.

### `/`

| | |
|---|---|
| **Primary keyword** | best online casino sites NZ |
| **Secondary keyword** | real money casinos / top 10 |
| **Competitors analysed** | casinos.com/nz &ldquo;Best Online Casinos NZ 2026 | Top 20 NZ Casino Sites Reviewed&rdquo; &middot; gambling.com/nz &ldquo;Online Casino NZ | Best Online Casinos for Real Money (2026)&rdquo; &middot; casino.org &ldquo;Best Real Money Online Casinos in New Zealand for 2026&rdquo; |
| **Title tag** | `Best Online Casino Sites NZ [September 2026]: Real Money` |
| **Measured width** | **535.8px** / 580px |
| **H1** | Best Online Casino Sites NZ [September 2026]: Real Money Casinos Ranked & Tested |

### `/online-casinos/`

| | |
|---|---|
| **Primary keyword** | best online casinos NZ |
| **Secondary keyword** | real money casino sites |
| **Competitors analysed** | casinos.com/nz, gambling.com/nz, bookies.com/nz &ndash; all pair the head term with &ldquo;real money&rdquo; and a count (&ldquo;Top 20&rdquo;, &ldquo;Top 10&rdquo;) |
| **Title tag** | `Best Online Casinos NZ [September 2026]: Real Money Sites` |
| **Measured width** | **545.8px** / 580px |
| **H1** | Best Online Casinos NZ [September 2026]: Real Money Casino Sites Ranked |

### `/casino-bonus/`

| | |
|---|---|
| **Primary keyword** | casino bonuses NZ |
| **Secondary keyword** | welcome bonus offers |
| **Competitors analysed** | casinos.com/nz &ldquo;Best Casino Bonuses in NZ 2026 | Welcome &amp; Sign Up Offers&rdquo; &middot; casino.org &ldquo;Best Casino Bonus 2026 | Top NZ Sign Up Offers&rdquo; &middot; gambling.com &ldquo;NZ Casino Bonuses | Exclusive Casino Offers (2026)&rdquo; |
| **Title tag** | `Casino Bonuses NZ [September 2026]: Welcome Bonus Offers` |
| **Measured width** | **559.1px** / 580px |
| **H1** | Casino Bonuses NZ [September 2026]: Best Welcome Bonus Offers & Free Spins |

### `/online-pokies/`

| | |
|---|---|
| **Primary keyword** | online pokies NZ |
| **Secondary keyword** | best real money pokies |
| **Competitors analysed** | gambling.com/nz &ldquo;Online Pokies New Zealand &ndash; Best Pokies Sites in 2026&rdquo; &middot; esportsinsider &ldquo;Online Pokies NZ 2026 &ndash; Best Real Money Pokies&rdquo; &middot; &ldquo;Online Pokies NZ 2026 | Best Real Money Pokies &amp; Casino Bonuses&rdquo; |
| **Title tag** | `Online Pokies NZ [September 2026]: Best Real Money Pokies` |
| **Measured width** | **549.1px** / 580px |
| **H1** | Online Pokies NZ [September 2026]: Best Real Money Pokies Sites |

### `/live-casino/`

| | |
|---|---|
| **Primary keyword** | live casino NZ |
| **Secondary keyword** | best live dealer sites |
| **Competitors analysed** | &ldquo;Live Casino NZ 2026: Best Live Dealer Sites for Kiwis&rdquo; (multiple) &middot; casino.org &ldquo;Best Live Dealer Games Online &ndash; Top Live Casinos in NZ 2026&rdquo; &middot; gambling.co.nz &ldquo;Top Live Dealer Casinos NZ &ndash; Real Dealer Gambling 2026&rdquo; |
| **Title tag** | `Live Casino NZ [September 2026]: Best Live Dealer Sites` |
| **Measured width** | **509.1px** / 580px |
| **H1** | Live Casino NZ [September 2026]: Best Live Dealer Sites for Kiwis |

### `/new-casinos-nz/`

| | |
|---|---|
| **Primary keyword** | new online casinos NZ |
| **Secondary keyword** | best new casino sites |
| **Competitors analysed** | casinos.com/nz &ldquo;New Online Casinos NZ 2026 &ndash; Best New Casino Sites Ranked&rdquo; &middot; casino.org &ldquo;New Online Casinos NZ &ndash; Newest Sites in September 2026&rdquo; (month in title) &middot; casinofreak &ldquo;Brand New Casino Sites for Kiwis&rdquo; |
| **Title tag** | `New Online Casinos NZ [September 2026]: New Casino Sites` |
| **Measured width** | **546.9px** / 580px |
| **H1** | New Online Casinos NZ [September 2026]: Best New Casino Sites Ranked |

### `/no-deposit-bonus/`

| | |
|---|---|
| **Primary keyword** | no deposit bonus NZ |
| **Secondary keyword** | free spins no deposit |
| **Competitors analysed** | casinos.com/nz &ldquo;No Deposit Bonus NZ 2026 | Real Money Offers Ranked&rdquo; &middot; gambling.com &ldquo;No Deposit Free Spins NZ 2026 | Free Spins No Deposit Bonus&rdquo; &middot; casino.guru &ldquo;Best No Deposit Bonuses in NZ (2026) | Free Codes &amp; Spins&rdquo; |
| **Title tag** | `No Deposit Bonus NZ [September 2026]: Free Spins No Deposit` |
| **Measured width** | **570.2px** / 580px |
| **H1** | No Deposit Bonus NZ [September 2026]: Free Spins No Deposit Casinos |

### `/fast-payout-casinos/`

| | |
|---|---|
| **Primary keyword** | fast / fastest payout casino NZ |
| **Secondary keyword** | instant withdrawals |
| **Competitors analysed** | casinobeats &ldquo;Fastest Payout Online Casino NZ 2026 | Instant Withdrawal Casino NZ&rdquo; &middot; casinos.com/nz &ldquo;Fastest Withdrawal Casinos NZ 2026 | Instant Payout Online Casino&rdquo; &middot; casino.org &ldquo;Fastest Payout Casino NZ 2026 | Instant Withdrawals&rdquo; |
| **Title tag** | `Fast Payout Casinos NZ [September 2026]: Instant Withdrawals` |
| **Measured width** | **566.9px** / 580px |
| **H1** | Fast Payout Casinos NZ [September 2026]: Fastest Instant Withdrawal Casinos, Timed |

### `/casino-payout-percentages/`

| | |
|---|---|
| **Primary keyword** | best payout casino NZ |
| **Secondary keyword** | highest RTP sites |
| **Competitors analysed** | casino.org &ldquo;Best Payout Casinos NZ 2026 | 98%+ RTP&rdquo; &middot; nzcasinoclub &ldquo;Best Payout Online Casino NZ | Highest RTP Sites in 2026&rdquo; &middot; bonus.net.nz &ldquo;Top Paying Online Casinos in NZ &ndash; Highest RTP Sites in 2026&rdquo; |
| **Title tag** | `Best Payout Casinos NZ [September 2026]: Highest RTP Sites` |
| **Measured width** | **556.9px** / 580px |
| **H1** | Best Payout Casinos NZ [September 2026]: Highest RTP Casino Sites |

### `/crypto-casinos-nz/`

| | |
|---|---|
| **Primary keyword** | best crypto casinos NZ |
| **Secondary keyword** | bitcoin &amp; USDT sites |
| **Competitors analysed** | &ldquo;Best Crypto Casinos NZ 2026 &mdash; Bitcoin, Ethereum &amp; USDT&rdquo; &middot; &ldquo;Best Bitcoin Casinos NZ 2026 | Top Crypto Casino Sites&rdquo; &middot; slotozilla &ldquo;Best Crypto &amp; Bitcoin Casinos in NZ 2026&rdquo; |
| **Title tag** | `Best Crypto Casinos NZ [September 2026]: Bitcoin & USDT Sites` |
| **Measured width** | **579.1px** / 580px |
| **H1** | Best Crypto Casinos NZ [September 2026]: Bitcoin, USDT & Ethereum Casino Sites |

### `/online-betting/`

| | |
|---|---|
| **Primary keyword** | online betting NZ |
| **Secondary keyword** | best sports betting sites |
| **Competitors analysed** | bookies.com/nz &ldquo;Best NZ Betting Sites August 2026 | Top New Zealand Online Bookmakers&rdquo; &middot; &ldquo;Best Online Betting Sites NZ (April 2026) | Top New Zealand Sportsbooks&rdquo; &mdash; month-in-title is standard in this vertical |
| **Title tag** | `Online Betting NZ [September 2026]: Best Sports Betting Sites` |
| **Measured width** | **554.7px** / 580px |
| **H1** | Online Betting NZ [September 2026]: Best Sports Betting Sites Compared |

### `/best-sports-betting-sites/`

| | |
|---|---|
| **Primary keyword** | best sports betting sites NZ |
| **Secondary keyword** | top Kiwi bookmakers |
| **Competitors analysed** | bettingtop10.co.nz &ldquo;Best NZ Sports Betting Sites September 2026 | Top Sites Ranked&rdquo; &middot; fhinz &ldquo;Best Sports Betting Sites NZ: Top Kiwi Bookmakers 2026&rdquo; &middot; betiton &ldquo;Best Sports Betting Sites in New Zealand (September 2026)&rdquo; |
| **Title tag** | `Best Sports Betting Sites NZ [September 2026]: Bookmakers` |
| **Measured width** | **540.2px** / 580px |
| **H1** | Best Sports Betting Sites NZ [September 2026]: Top Kiwi Bookmakers Ranked |

### `/casino-reviews/`

| | |
|---|---|
| **Primary keyword** | casino reviews NZ |
| **Secondary keyword** | expert ratings &amp; payouts |
| **Competitors analysed** | casino.guru &ldquo;800+ Rated&rdquo; &middot; casino.org review directory &middot; competitors lead on volume of reviews; we lead on tested payout data |
| **Title tag** | `Casino Reviews NZ [September 2026]: Expert Ratings & Payouts` |
| **Measured width** | **579.1px** / 580px |
| **H1** | Casino Reviews NZ [September 2026]: Expert Ratings & Tested Payouts |

### `/casino-reviews/&lt;slug&gt;/`

*Pattern shown with `/casino-reviews/kingdom/` as the example.*

| | |
|---|---|
| **Primary keyword** | &lt;brand&gt; review |
| **Secondary keyword** | NZ bonus &amp; payouts (+ score) |
| **Competitors analysed** | gambling.com/nz/online-casinos/reviews/&lt;brand&gt; &middot; casinos.com review pages &mdash; all use &ldquo;&lt;Brand&gt; Review&rdquo; + year; almost none carry a numeric score in the title |
| **Title tag** | `Kingdom Casino Review [September 2026]: NZ Bonus & Payouts` |
| **Measured width** | **579.1px** / 580px |
| **H1** | Kingdom Casino Review [September 2026]: NZ Bonus, Payouts & Our 9.1/10 Verdict |

### `/licensed-online-casinos/`

| | |
|---|---|
| **Primary keyword** | NZ online gambling laws |
| **Secondary keyword** | is it legal in NZ |
| **Competitors analysed** | cdhbcareers &ldquo;NZ Gambling Laws &ndash; Is Online Gambling Legal in New Zealand? (2026)&rdquo; &middot; DIA and law-firm pages own the informational SERP; affiliate coverage is thin |
| **Title tag** | `NZ Online Gambling Laws [September 2026]: Is It Legal in NZ?` |
| **Measured width** | **560.2px** / 580px |
| **H1** | NZ Online Gambling Laws [September 2026]: Is It Legal, and What the Online Casino Gambling Act 2026 Changes |

### `/casino-payment-methods/`

| | |
|---|---|
| **Primary keyword** | casino payment methods NZ |
| **Secondary keyword** | NZD banking |
| **Competitors analysed** | casino.org &ldquo;Top Casino Payment Methods NZ 2026 &ndash; Deposits &amp; Withdrawals&rdquo; &middot; casino.com/nz &ldquo;NZ Casino Payment Methods 2026 | Fast &amp; Secure Banking&rdquo; &middot; &ldquo;Casino Payment Methods NZ 2026: NZD Deposits &amp; Withdrawals&rdquo; |
| **Title tag** | `Casino Payment Methods NZ [September 2026]: NZD Banking` |
| **Measured width** | **555.8px** / 580px |
| **H1** | Casino Payment Methods NZ [September 2026]: Deposits & Withdrawals Tested |

### `/responsible-gambling/`

| | |
|---|---|
| **Primary keyword** | responsible gambling NZ |
| **Secondary keyword** | free help &amp; self-exclusion |
| **Competitors analysed** | Gambling Helpline and PGF own this SERP; affiliate pages are thin and rarely titled for it |
| **Title tag** | `Responsible Gambling NZ [September 2026]: Free Help` |
| **Measured width** | **496.9px** / 580px |
| **H1** | Responsible Gambling NZ [September 2026]: Free Help, Limits & Self-Exclusion |

### `/how-we-rate-casinos/`

| | |
|---|---|
| **Primary keyword** | how we review casinos |
| **Secondary keyword** | our methodology |
| **Competitors analysed** | casinos.com &ldquo;How We Rate NZ Casinos Online&rdquo; &middot; casino.org &ldquo;25-step review process&rdquo; &middot; gambling.com &ldquo;full casino review methodology&rdquo; |
| **Title tag** | `How We Review Casinos [September 2026]: Our Methodology` |
| **Measured width** | **553.5px** / 580px |
| **H1** | How We Review Casinos [September 2026]: Our Scoring Model & Editorial Standards |

### `/about/`

| | |
|---|---|
| **Primary keyword** | about &lt;brand&gt; |
| **Secondary keyword** | our team &amp; testing |
| **Competitors analysed** | Standard corporate titles; no keyword competition |
| **Title tag** | `About Casino Edge NZ [September 2026]: Our Team & Testing` |
| **Measured width** | **560.3px** / 580px |
| **H1** | About Casino Edge NZ [September 2026]: Who We Are, How We Test, How We Are Paid |

### `/contact/`

| | |
|---|---|
| **Primary keyword** | contact us |
| **Secondary keyword** | corrections &amp; complaints |
| **Competitors analysed** | Standard corporate titles; no keyword competition |
| **Title tag** | `Contact Us [September 2026]: Corrections & Complaints` |
| **Measured width** | **501.3px** / 580px |
| **H1** | Contact Us [September 2026]: Casino Edge NZ Corrections, Complaints & Enquiries |

### `/authors/`

| | |
|---|---|
| **Primary keyword** | our authors |
| **Secondary keyword** | NZ casino review experts |
| **Competitors analysed** | casinos.com and gambling.com both run author hubs with Person schema; neither targets a keyword |
| **Title tag** | `Our Authors [September 2026]: NZ Casino Review Experts` |
| **Measured width** | **522.4px** / 580px |
| **H1** | Our Authors [September 2026]: The NZ Casino Review Team |

### `/authors/&lt;slug&gt;/`

*Pattern shown with `/authors/priya-raman/` as the example.*

| | |
|---|---|
| **Primary keyword** | &lt;author name&gt; |
| **Secondary keyword** | role at &lt;brand&gt; |
| **Competitors analysed** | Brand-name queries only |
| **Title tag** | `Priya Raman [September 2026]: Payments & Data Editor` |
| **Measured width** | **504.7px** / 580px |
| **H1** | Priya Raman [September 2026]: Payments & Data Editor at Casino Edge NZ |

### `/terms-and-conditions/`

| | |
|---|---|
| **Primary keyword** | terms and conditions |
| **Secondary keyword** | site terms of use |
| **Competitors analysed** | No competition |
| **Title tag** | `Terms and Conditions [September 2026]: Site Terms of Use` |
| **Measured width** | **531.3px** / 580px |
| **H1** | Terms and Conditions [September 2026]: Using Casino Edge NZ |

### `/privacy-policy/`

| | |
|---|---|
| **Primary keyword** | privacy policy |
| **Secondary keyword** | how we use your data |
| **Competitors analysed** | No competition |
| **Title tag** | `Privacy Policy [September 2026]: How We Use Your Data` |
| **Measured width** | **512.4px** / 580px |
| **H1** | Privacy Policy [September 2026]: How We Use Your Data Under the Privacy Act 2020 |

### `/cookie-policy/`

| | |
|---|---|
| **Primary keyword** | cookie policy |
| **Secondary keyword** | cookies we set &amp; why |
| **Competitors analysed** | No competition |
| **Title tag** | `Cookie Policy [September 2026]: Cookies We Set & Why` |
| **Measured width** | **504.6px** / 580px |
| **H1** | Cookie Policy [September 2026]: Every Cookie We Set, and How to Turn It Off |

---

## Full title inventory, by width

| Page | Title tag | px |
|---|---|---|
| `/authors/manaia-kerr/` | Manaia Kerr [September 2026]: Betting Editor at Casino Edge NZ | 579.2 |
| `/crypto-casinos-nz/` | Best Crypto Casinos NZ [September 2026]: Bitcoin & USDT Sites | 579.1 |
| `/casino-reviews/` | Casino Reviews NZ [September 2026]: Expert Ratings & Payouts | 579.1 |
| `/casino-reviews/kingdom/` | Kingdom Casino Review [September 2026]: NZ Bonus & Payouts | 579.1 |
| `/casino-reviews/gunsbet/` | Gunsbet Review [September 2026]: NZ Bonus, Payouts & 8.6/10 | 574.7 |
| `/authors/aroha-tainui/` | Aroha Tainui [September 2026]: Regulation & Compliance Editor | 572.5 |
| `/casino-reviews/hellspin/` | Hellspin Review [September 2026]: NZ Bonus, Payouts & 8.1/10 | 570.3 |
| `/no-deposit-bonus/` | No Deposit Bonus NZ [September 2026]: Free Spins No Deposit | 570.2 |
| `/fast-payout-casinos/` | Fast Payout Casinos NZ [September 2026]: Instant Withdrawals | 566.9 |
| `/authors/sam-kavanagh/` | Sam Kavanagh [September 2026]: Games & Live Casino Editor | 563.6 |
| `/casino-reviews/ivibet-sportsbook/` | Ivibet Sportsbook Review [September 2026]: NZ Bonus & Odds | 562.5 |
| `/casino-reviews/smash/` | Smash Casino Review [September 2026]: NZ Bonus & Payouts | 562.5 |
| `/about/` | About Casino Edge NZ [September 2026]: Our Team & Testing | 560.3 |
| `/licensed-online-casinos/` | NZ Online Gambling Laws [September 2026]: Is It Legal in NZ? | 560.2 |
| `/casino-bonus/` | Casino Bonuses NZ [September 2026]: Welcome Bonus Offers | 559.1 |
| `/casino-payout-percentages/` | Best Payout Casinos NZ [September 2026]: Highest RTP Sites | 556.9 |
| `/casino-reviews/spinjo/` | Spinjo Casino Review [September 2026]: NZ Bonus & Payouts | 555.8 |
| `/casino-payment-methods/` | Casino Payment Methods NZ [September 2026]: NZD Banking | 555.8 |
| `/online-betting/` | Online Betting NZ [September 2026]: Best Sports Betting Sites | 554.7 |
| `/how-we-rate-casinos/` | How We Review Casinos [September 2026]: Our Methodology | 553.5 |
| `/casino-reviews/spino/` | Spino Casino Review [September 2026]: NZ Bonus & Payouts | 551.4 |
| `/online-pokies/` | Online Pokies NZ [September 2026]: Best Real Money Pokies | 549.1 |
| `/casino-reviews/ivibet/` | Ivibet Casino Review [September 2026]: NZ Bonus & Payouts | 548.0 |
| `/casino-reviews/lucky-circus/` | Lucky Circus Review [September 2026]: NZ Bonus & Payouts | 546.9 |
| `/casino-reviews/roby-casino/` | Roby Casino Review [September 2026]: NZ Bonus & Payouts | 546.9 |
| `/new-casinos-nz/` | New Online Casinos NZ [September 2026]: New Casino Sites | 546.9 |
| `/casino-reviews/fortune-play/` | Fortune Play Review [September 2026]: NZ Bonus & Payouts | 545.8 |
| `/online-casinos/` | Best Online Casinos NZ [September 2026]: Real Money Sites | 545.8 |
| `/best-sports-betting-sites/` | Best Sports Betting Sites NZ [September 2026]: Bookmakers | 540.2 |
| `/casino-reviews/rivo/` | Rivo Casino Review [September 2026]: NZ Bonus & Payouts | 540.2 |
| `/casino-reviews/lucky7even/` | Lucky7even Review [September 2026]: NZ Bonus & Payouts | 539.1 |
| `/casino-reviews/rooster-bet/` | Rooster Bet Review [September 2026]: NZ Bonus & Payouts | 538.0 |
| `/` | Best Online Casino Sites NZ [September 2026]: Real Money | 535.8 |
| `/casino-reviews/crownslots/` | CrownSlots Review [September 2026]: NZ Bonus & Payouts | 534.7 |
| `/casino-reviews/madcasino/` | MadCasino Review [September 2026]: NZ Bonus & Payouts | 533.6 |
| `/terms-and-conditions/` | Terms and Conditions [September 2026]: Site Terms of Use | 531.3 |
| `/casino-reviews/lucky-vibe/` | Lucky Vibe Review [September 2026]: NZ Bonus & Payouts | 530.2 |
| `/authors/` | Our Authors [September 2026]: NZ Casino Review Experts | 522.4 |
| `/casino-reviews/slotsgem/` | Slotsgem Review [September 2026]: NZ Bonus & Payouts | 515.8 |
| `/casino-reviews/betandplay/` | Bet&Play Review [September 2026]: NZ Bonus & Payouts | 514.7 |
| `/privacy-policy/` | Privacy Policy [September 2026]: How We Use Your Data | 512.4 |
| `/live-casino/` | Live Casino NZ [September 2026]: Best Live Dealer Sites | 509.1 |
| `/authors/priya-raman/` | Priya Raman [September 2026]: Payments & Data Editor | 504.7 |
| `/cookie-policy/` | Cookie Policy [September 2026]: Cookies We Set & Why | 504.6 |
| `/contact/` | Contact Us [September 2026]: Corrections & Complaints | 501.3 |
| `/responsible-gambling/` | Responsible Gambling NZ [September 2026]: Free Help | 496.9 |
| `/authors/jordan-whitcombe/` | Jordan Whitcombe [September 2026]: Editor-in-Chief | 470.2 |

---

## Monthly refresh

`MONTH` and `YEAR` are single constants in `_build/lib.py`. Change them,
rebuild, and every title tag, every H1, every meta description and every
`next review` date moves together. The build will fail loudly if a longer
month name (`September` → `December` is wider; `May` is much narrower) pushes
any title past 580px, so the constraint can never silently break.

Widths by month name, worst-case page (`Manaia Kerr`, currently 579.2px):

| Month | Width of the widest title |
|---|---|
| January | 552.5px |
| February | 561.4px |
| March | 536.9px |
| April | 521.3px |
| May | 519.1px |
| June | 524.7px |
| July | 516.9px |
| August | 543.6px |
| September | 579.2px |
| October | 552.5px |
| November | 573.6px |
| December | 573.6px |

Any month flagged above needs its secondary keyword shortened one step in the
`_REG` candidate list before that month's rebuild. `lib.fit()` does this
automatically for pages whose candidates are registered through it — the
author pages are the only ones currently near the ceiling.
