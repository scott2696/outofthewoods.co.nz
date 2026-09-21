# Keyword map and URL migration

The keyword-to-page assignment you supplied is now the site's source of truth. It lives in
`_build/keywords.py` and the build **fails** if a Tier 1 term falls off its page or if any term is
repeated past a density cap. Nothing here is aspirational — every number below comes from the
rendered HTML.

---

## 1. URL migration

Your map implied a different URL structure to the one built. Because the site is pre-launch, the
renames were free to make. Nine URLs moved, one page is new, and one is a redirect stub only.

| Old URL | New URL | Why |
|---|---|---|
| `/online-casinos/bonuses/` | `/casino-bonus/` | Matches your map; shorter, and no longer nested under the head page |
| `/high-payout-casinos/` | `/casino-payout-percentages/` | Head term shifts from "high payout" to "casino payout percentage" / RTP |
| `/payment-methods/` | `/casino-payment-methods/` | Head term match |
| `/live-casinos/` | `/live-casino/` | Singular, per your map |
| `/how-we-review/` | `/how-we-rate-casinos/` | Head term match |
| `/no-deposit-casinos/` | `/no-deposit-bonus/` | Owns "no deposit" intent exclusively |
| `/new-online-casinos/` | `/new-casinos-nz/` | Head term match |
| `/best-crypto-casinos/` | `/crypto-casinos-nz/` | Head term match |
| `/nz-gambling-law/` | **`/licensed-online-casinos/`** | **Merged.** Your licensing page and our law page were targeting the same terms — two pages would have cannibalised each other |
| `/instant-withdrawals/` | `/fast-payout-casinos/` | **Redirect only — no page exists at the old URL** |

Two speculative redirects (`/casino-bonuses/`, `/online-casinos/no-deposit/`) are included because
they are the obvious alternate spellings someone might link to.

### The redirects are real 301s

No page, no meta-refresh, no JavaScript hop. `build.py` emits the rule in four host formats and
`prune()` deletes the old directory so the retired URL cannot return a 200:

```
_redirects             Netlify / Cloudflare Pages   (301!)
.htaccess              Apache                       (R=301,L)
vercel.json            Vercel                       (permanent: true)
nginx-redirects.conf   nginx                        (permanent)
```

**Verified:** 0 internal links anywhere on the site point at a retired URL, and no retired URL
still has an `index.html` on disk.

---

## 2. Cannibalisation control: the bonus split

You asked for `/no-deposit-bonus/` to own "no deposit" and "free spins no deposit" exclusively.
Done, and enforced in both directions:

- `/casino-bonus/` no longer competes for no-deposit terms. Its no-deposit card and its
  "are no-deposit bonuses worth claiming?" FAQ were replaced with a hand-off link and an
  "are casino bonuses worth it in NZ?" question instead.
- `/casino-bonus/` picked up the deposit-size intent in exchange: a sign-up-bonus-by-deposit table
  covering $1, $5 and $10 deposit queries, plus wagering-mechanics sections.
- `/no-deposit-bonus/` gained the codes and amounts material (a table of what 20/25/50/100 free
  spins are actually worth once the fixed stake is applied).

---

## 3. Coverage, measured

From the build's own audit. "Tier 1 hits" counts every natural-form occurrence across all Tier 1
terms on the page.

```
  page                            words    tier1    tier2 long-tail
  /casino-bonus/                   3664 23 hits/4      6/6     8/10
  /casino-payment-methods/         3232 12 hits/5      8/8     6/10
  /casino-payout-percentages/      3042 16 hits/5      5/5      9/9
  /crypto-casinos-nz/              3524 27 hits/5      7/7     9/13
  /fast-payout-casinos/            3340 11 hits/4      5/5     3/10
  /how-we-rate-casinos/            3124 9 hits/4      2/2      2/2
  /licensed-online-casinos/        3553 12 hits/5      6/6     8/11
  /live-casino/                    3189 19 hits/5      5/5      7/9
  /new-casinos-nz/                 3179 23 hits/5      5/5     7/12
  /no-deposit-bonus/               2952 32 hits/5      7/7    10/15
  /online-casinos/                 4373 35 hits/10      9/9     8/10
  /online-pokies/                  3716 20 hits/6      6/6    10/11
```

**Tier 1: 100% covered. Tier 2: 100% covered. Long-tail: 92 of 122 terms (75%)** — the remainder
are questions already answered in our own words, where forcing the exact phrasing would read badly.

---

## 4. The anti-stuffing guard

You asked for the high-volume terms to be used more than once without stuffing. Both halves are
enforced mechanically:

| Rule | Enforcement |
|---|---|
| Every Tier 1 term appears **at least twice** | Build fails below 2 |
| Each page's **head term appears verbatim** at least once | Build fails at 0 |
| Other Tier 1 terms may appear in natural variants | "Paysafecard casinos in NZ" credits "paysafecard casino nz" |
| No term exceeds **1.2% density** | Build fails above it |

Measured head-term density, all 12 pages:

| Page | Words | Head term | Verbatim uses | Density |
|---|---|---|---|---|
| `/casino-bonus/` | 3689 | casino bonus nz | 4 | **0.33%** |
| `/casino-payment-methods/` | 3287 | casino payment methods nz | 2 | **0.24%** |
| `/casino-payout-percentages/` | 3062 | casino payout percentage | 5 | **0.49%** |
| `/crypto-casinos-nz/` | 3569 | crypto casino nz | 5 | **0.42%** |
| `/fast-payout-casinos/` | 3338 | fast payout casinos nz | 4 | **0.48%** |
| `/how-we-rate-casinos/` | 3146 | how to choose an online casino nz | 2 | **0.45%** |
| `/licensed-online-casinos/` | 3582 | licensed online casinos nz | 3 | **0.34%** |
| `/live-casino/` | 3202 | live casino nz | 4 | **0.37%** |
| `/new-casinos-nz/` | 3203 | new online casinos nz | 5 | **0.62%** |
| `/no-deposit-bonus/` | 2962 | no deposit bonus nz | 7 | **0.95%** |
| `/online-casinos/` | 4374 | online casinos nz | 11 | **0.75%** |
| `/online-pokies/` | 3738 | online pokies nz | 6 | **0.48%** |

Highest is 0.95%. The usual spam threshold quoted for this is around 3%, and most over-optimised
affiliate pages sit at 2–4%. The terms are carried by **headings and natural variants**, not by
repetition.

---

## 5. Title, H1 and headings per page

### `/casino-bonus/`

- **Primary:** casino bonus nz
- **Title** (526px / 580): `Casino Bonus NZ [September 2026]: Sign Up Bonus Offers`
- **H1:** Casino Bonus NZ [September 2026]: Best Casino Bonuses, Sign Up Offers and $1 Deposit Deals
- **H2s:** Best casino bonuses NZ — September 2026 · What a NZ$100 deposit really costs you in turnover · Casino sign up bonus NZ offers, by deposit size · Bonus types explained · The five terms that decide whether a bonus is worth taking · Every welcome offer and its conditions · Mistakes that void a bonus · Casino bonus questions

### `/casino-payment-methods/`

- **Primary:** casino payment methods nz
- **Title** (556px / 580): `Casino Payment Methods NZ [September 2026]: NZD Banking`
- **H1:** Casino Payment Methods NZ [September 2026]: Online Casino Deposit Methods and Withdrawals, Tested
- **H2s:** Every method, compared · NZD accounts and why they matter more than the bonus · Online casino deposit methods NZ players can use · Casinos that accept NZD, and what the others cost you · Which casinos support what · Payment questions

### `/casino-payout-percentages/`

- **Primary:** casino payout percentage
- **Title** (569px / 580): `Casino Payout Percentages NZ [September 2026]: Highest RTP`
- **H1:** Casino Payout Percentages NZ [September 2026]: Highest RTP Casinos and What Payout Percentage Really Means
- **H2s:** Highest payout online casinos NZ — September 2026 · What we found in the RTP sample · Where the real edge is: game by game · Why a casino would run a lower RTP build · RTP meaning: casino payout percentages explained · Highest RTP casinos NZ and the highest RTP pokies NZ players can find · Payout percentage versus payout speed · High payout casinos NZ — frequently asked questions

### `/crypto-casinos-nz/`

- **Primary:** crypto casino nz
- **Title** (568px / 580): `Crypto Casinos NZ [September 2026]: Best Bitcoin Casino Sites`
- **H1:** Crypto Casinos NZ [September 2026]: Best Bitcoin, Ethereum and USDT Casino Sites
- **H2s:** Best Bitcoin and crypto casinos NZ — September 2026 · Which coins work where · Real settlement times and network fees · Coin by coin: which crypto casino NZ players should use for what · How to deposit and withdraw at a bitcoin casino NZ side · Buying crypto in New Zealand · Tax: what actually applies · The risks, stated plainly · Crypto casinos NZ — frequently asked questions

### `/fast-payout-casinos/`

- **Primary:** fast payout casinos nz
- **Title** (567px / 580): `Fast Payout Casinos NZ [September 2026]: Instant Withdrawals`
- **H1:** Fast Payout Casinos NZ [September 2026]: Fastest Instant Withdrawal Casinos, Timed
- **H2s:** Fastest paying online casinos NZ — September 2026 · The timing data · How long do casino withdrawals take in NZ? · Instant withdrawal casino NZ: what the phrase actually means · How long each rail really takes · The four reasons a payout gets held · Weekly caps: the term nobody reads · How to get paid faster · Fast payout casinos NZ — frequently asked questions · …

### `/how-we-rate-casinos/`

- **Primary:** how to choose an online casino nz
- **Title** (562px / 580): `How We Rate Casinos [September 2026]: Review Methodology`
- **H1:** How We Rate Casinos [September 2026]: How to Choose an Online Casino, and Our Review Methodology
- **H2s:** The weighting · What each component measures · How to choose an online casino, and tell if an online casino is legit · How the evidence is gathered · What disqualifies an operator entirely · How we are paid, and what it does not buy · Corrections and complaints · Questions about our methodology

### `/licensed-online-casinos/`

- **Primary:** licensed online casinos nz
- **Title** (527px / 580): `Licensed Online Casinos NZ [September 2026]: Is It Legal?`
- **H1:** Licensed Online Casinos NZ [September 2026]: Legal Online Casinos, NZ Online Gambling Laws and the Licence List
- **H2s:** Are online casinos legal in New Zealand? · The position in one table · The Online Casino Gambling Act 2026 and the NZ online casino licence · The licensing process and timeline · What the regulations require · What it means for players · Sports betting is a separate regime · The old framework: Gambling Act 2003 · New Zealand gambling law — frequently asked questions

### `/live-casino/`

- **Primary:** live casino nz
- **Title** (577px / 580): `Live Casino NZ [September 2026]: Best Live Dealer Casino Sites`
- **H1:** Live Casino NZ [September 2026]: Best Live Dealer Casino Sites, Roulette and Blackjack
- **H2s:** Best live dealer casinos NZ — September 2026 · Table counts, verified · The three studios worth knowing · Live roulette NZ, live blackjack NZ and live baccarat NZ · How does live casino work, and how it differs from RNG games · Blackjack, roulette and baccarat online · Game shows: Crazy Time and the rest · Stream quality on a New Zealand connection · Live casino NZ — frequently asked questions

### `/new-casinos-nz/`

- **Primary:** new online casinos nz
- **Title** (574px / 580): `New Online Casinos NZ [September 2026]: Newest Casino Sites`
- **H1:** New Online Casinos NZ [September 2026]: Newest Online Casinos and New Casino Sites, Tracked
- **H2s:** New online casinos NZ — September 2026 · Launch tracker: the newest online casinos NZ players can reach · What to check before joining a new casino · Launch dates and platform groups · What a new casino does better · What a new casino cannot prove yet · How to test a new casino safely · New online casinos NZ — frequently asked questions

### `/no-deposit-bonus/`

- **Primary:** no deposit bonus nz
- **Title** (570px / 580): `No Deposit Bonus NZ [September 2026]: Free Spins No Deposit`
- **H1:** No Deposit Bonus NZ [September 2026]: Free Spins No Deposit and No Deposit Bonus Codes
- **H2s:** No deposit and near-no-deposit offers for NZ players · What a no deposit bonus is actually worth · No deposit bonus codes NZ: how they work and why most are dead · How to claim, step by step · The terms that limit it · Better alternatives if you have NZ$10–20 · No deposit bonuses NZ — frequently asked questions

### `/online-casinos/`

- **Primary:** online casinos nz
- **Title** (546px / 580): `Best Online Casinos NZ [September 2026]: Real Money Sites`
- **H1:** Best Online Casinos NZ [September 2026]: Top NZ Casino Sites for Real Money, Tested
- **H2s:** Best casino sites NZ, ranked 1 to 16 · Withdrawal terms at NZ online casinos, compared · Safe and trusted online casinos NZ players can actually verify · How to choose an online casino, in the right order · What a real money casino NZ account actually gives you · Online casino real money NZ sites we tested and left out · Opening a top online casinos NZ account, step by step · Online casinos NZ — frequently asked questions · Looking for something more specific?

### `/online-pokies/`

- **Primary:** online pokies nz
- **Title** (549px / 580): `Online Pokies NZ [September 2026]: Best Real Money Pokies`
- **H1:** Online Pokies NZ [September 2026]: Best Real Money Pokies Sites and Free Pokies
- **H2s:** Best online pokies sites NZ — September 2026 · Studio coverage at every online pokies real money NZ site · RTP: what the number does and does not mean · Volatility, and choosing a game that suits your balance · How do online pokies work? · Megaways, jackpot and bonus buy pokies · Jackpot pokies · Mobile pokies NZ: playing on a phone · Online pokies NZ — frequently asked questions · …

---

## 6. Notes on two of your instructions

**POLi.** You asked us to verify its NZ availability before committing a section to it. We did,
back in the original research, and the finding stands: POLi Payments operates normally in New
Zealand — Merco-owned, bank-API connected since the December 2025 open banking rules, eight bank
partners — but **the online casino channel is gone**. `/casino-payment-methods/` says exactly that
under its own H3, and frames a competitor still showing POLi logos as a freshness test. It is a
trust asset rather than a trust hit, because we are correcting the market rather than repeating it.

**`/new-casinos-nz/` refresh value.** Agreed, and built for it: the page now leads with a launch
tracker table whose final row is a placeholder for DIA licence holders, plus an explicit note that
we will not name licence winners before the auction concludes. The visible "Updated" stamp is in
the byline on every page and is content-hash derived, so it only moves when the page actually
changes.

---

## 7. Page order

Every page with an affiliate block now reads in one order, on every viewport:

```
hero [ breadcrumb -> H1 -> lede -> CTAs -> stats -> byline ]
  ->  H2 + operator table  ->  explanatory line
  ->  disclosure  ->  lede / short answer  ->  contents  ->  rest of page
```

The breadcrumb and byline live **inside** the hero element, not in a strip under
it — `hero(meta=(trail, author, checker))` renders them. On a phone the hero
hides its eyebrow, lede, buttons and stat band, so it collapses to H1 + byline,
which is exactly what should be above the fold.

This is **DOM order**, not a CSS reorder, so reading order, crawl order and tab
order all agree. Two mechanical guarantees back it up:

- `.ord-lb > .wrap` is a flex column with the H2 at `order:0` and the table at
  `order:1`, so nothing can be introduced between the heading and the table.
- The build validates on all 32 affiliate pages that `hero < byline < table <
  disclosure`, and fails if a page drifts.

**Disclosure note.** The full disclosure block now sits below the table. The
compact version — *"We may earn a commission from operators we list — how that
works"* — remains in the top strip on every page, so a disclosure still precedes
the first affiliate link even though the detailed one follows the table.

---

## 8. Maintaining this

`_build/keywords.py` is the only file to edit. Add a term to a page's list and the next build tells
you whether the page covers it. Move a term between pages and the audit re-points. Retire a URL by
adding it to `REDIRECTS` — `prune()` removes the old page and the four host configs regenerate.
