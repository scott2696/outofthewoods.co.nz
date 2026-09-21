# SERP domination, EEAT and conversion — Casino Edge NZ

---

## 1. Schema markup implemented

Every page emits a single `@graph` in one `application/ld+json` block, so
entities are linked by `@id` rather than repeated. All `@id` values derive from
`SITE`, so changing the domain rewrites the whole graph.

| Type | Where | Purpose |
|---|---|---|
| `Organization` | Every page (`#organization`) | Publisher entity: legalName, NZBN-bearing address, logo, email, `knowsAbout`, `publishingPrinciples` → `/how-we-rate-casinos/`, `areaServed` NZ |
| `WebSite` | Every page (`#website`) | Site entity, `inLanguage: en-NZ`, publisher link |
| `Article` | All content pages (`#article`) | `author` → Person `@id`, `reviewedBy` → the fact-checker's Person `@id`, `datePublished`, `dateModified`, `articleSection` |
| `BreadcrumbList` | Every page (`#breadcrumb`) | Breadcrumb rich result, hierarchy signal |
| `ItemList` | All ranked pages (`#itemlist`) | `itemListOrder: Descending`, each `ListItem` wraps a `Product` with `Brand` and a nested `Review` carrying `reviewRating` and `reviewBody` |
| `Review` | 19 operator reviews (`#review`) | `itemReviewed` (Product + Brand), `reviewRating` 1–10, `author` → Person, `publisher` → Organization, plus `positiveNotes` / `negativeNotes` ItemLists built from the pros and cons |
| `FAQPage` | Every page with an FAQ (`#faq`) | Generated from the *same list* that renders the visible accordion, so markup and content cannot drift |
| `Person` | Author pages + referenced by every Article | `jobTitle`, `knowsAbout`, `worksFor` → Organization, `url` |
| `ProfilePage` | 5 author pages (`#profile`) | `mainEntity` → Person |
| `CollectionPage` | `/authors/` | `hasPart` → all five Person entities |
| `AboutPage` / `ContactPage` | `/about/`, `/contact/` | `about` → Organization |
| `WebPage` | Legal pages | `dateModified`, publisher |

**Notes on compliance.** `Review` and `aggregateRating` are applied to
third-party products (the operators), never self-serving on our own
Organization, which is what Google's structured-data guidelines require.
`positiveNotes` / `negativeNotes` are populated because Google explicitly
supports them and competitors are not using them.

---

## 2. Featured snippet strategy

Google currently serves a **list snippet** for the head term. Two formats are
targeted per page.

### Paragraph snippets
Every money page opens with a **direct-answer paragraph of 40–55 words**
immediately after the byline and disclosure, in the pattern:

> **Short answer:** the best online casino site in New Zealand right now is
> Spinjo (9.3/10) for its 8,000-game lobby and genuine NZD wallet; Kingdom
> (9.1/10) if getting paid quickly matters most, with a verified median
> withdrawal of two hours fifty minutes; and Smash (8.8/10) if you intend to
> actually clear a welcome bonus.

This names entities, carries a number, and answers in one sentence — the three
properties paragraph snippets select for.

### List snippets
The ranked leaderboard is semantically ordered with a numeric rank element, and
every ranked page carries an `ItemList` with `itemListOrder`. The H2 is phrased
as the query ("Top 10 Online Casino Sites NZ — September 2026") so the list can
be lifted with its heading.

### Table snippets
The highest-opportunity format, and almost entirely uncontested in this niche
because competitors publish prose where a table belongs. Every page carries at
least one table whose first column is the entity and whose header row matches a
likely query:

- "What a NZ$100 deposit really costs you in turnover"
- "Measured withdrawal times, April–September 2026"
- "RTP configuration sample: ten popular titles per casino"
- "Median overround by market"
- "Weekly withdrawal caps against maximum advertised bonus"
- "Casino payment methods available to New Zealand players"

Each has a `<caption>` that reads as a query answer.

---

## 3. People Also Ask targeting

Every FAQ question is written in near-verbatim PAA phrasing, and the first
sentence of each answer is a complete, standalone answer of 30–50 words. PAA
boxes lift the first sentence, so the first sentence never begins with "It
depends" without immediately resolving.

High-value PAA targets currently served on the site:

| Question | Page |
|---|---|
| Is it legal to play at online casinos in New Zealand? | `/`, `/licensed-online-casinos/` |
| Do I pay tax on online casino winnings in New Zealand? | `/`, `/licensed-online-casinos/` |
| What is the fastest paying online casino in NZ? | `/`, `/fast-payout-casinos/` |
| Can I still use POLi to deposit at an online casino? | `/`, `/casino-payment-methods/` |
| What does 40x wagering actually mean? | `/casino-bonus/` |
| Are offshore casinos safe if they are not licensed in NZ? | `/` |
| What is the legal gambling age in New Zealand? | `/licensed-online-casinos/` |
| Can I play in New Zealand dollars? | `/`, `/casino-payment-methods/` |
| What happens to my account after 1 December 2026? | `/`, `/online-casinos/` |
| Can I still bet on greyhound racing in New Zealand? | `/online-betting/` |
| Is TAB NZ better than an offshore bookmaker? | `/online-betting/` |
| What is a good RTP for an online pokie? | `/online-pokies/`, `/casino-payout-percentages/` |

---

## 4. Meta title and description patterns

**Titles** — one format, applied to all 47 pages:

```
Primary Keyword [Month Year]: Secondary Keyword
```

The primary is the head term ranking competitors put first in their own titles;
the secondary is the modifier they most consistently pair with it. Both were
taken from live SERP titles in September 2026 — the full analysis is in
`06-title-tags.md`.

```
Best Online Casino Sites NZ [September 2026]: Real Money          535.8px
Best Online Casinos NZ [September 2026]: Real Money Sites         545.8px
Online Pokies NZ [September 2026]: Best Real Money Pokies         549.1px
Fast Payout Casinos NZ [September 2026]: Instant Withdrawals      566.9px
Online Betting NZ [September 2026]: Best Sports Betting Sites     554.7px
Kingdom Casino Review [September 2026]: NZ Bonus & Payouts        579.1px
```

**Titles are measured in pixels, not characters.** Google renders desktop SERP
titles in Arial 20px and truncates at roughly 580px, and character counts are a
poor proxy — *Wellington* and *Illinois* are the same length and 38% apart in
width. `lib.serp_px()` measures real Arial advance widths and `lib.write()`
**refuses to build** a page whose title exceeds 580px. `lib.fit()` picks the
richest secondary keyword that still fits, which is why a long brand name gets
a shorter secondary than a short one.

Current spread across all 47 pages: min 470px, median 547px, max 579px.

**H1s use the identical format with no width ceiling**, so they carry the fuller
secondary phrase — the title tag competes for the click, the H1 confirms the
match on arrival:

```
Title:  Fast Payout Casinos NZ [September 2026]: Instant Withdrawals
H1:     Fast Payout Casinos NZ [September 2026]: Fastest Instant Withdrawal Casinos, Timed
```

**Descriptions** — pattern: `{Restated promise}. {Proof with a number}. {Freshness}.`
150–165 characters, active voice, no truncated sentences.

```
The best online casino sites NZ players can use in September 2026. 241
withdrawals timed, 46 casinos tested from a NZ IP. Real NZD banking, wagering
you can clear, verified payouts.
```

**The freshness token is a standing commitment, not a decoration.** `MONTH` and
`YEAR` are single constants in `_build/lib.py`. Change them once a month,
rebuild, and every title, H1, description, hero eyebrow and "next review" date
updates together. September is the widest month name, so the current build is
the worst case — every other month leaves more headroom.

## 5. CTR optimisation

| Lever | Implementation |
|---|---|
| Numbers in titles | "Top 10", "All 16", "9.1/10", "10 Books Compared" |
| Proof phrases | "Timed Results", "Tested From NZ", "Margins Measured" |
| Freshness | Month + year in every title, refreshed monthly with real data changes |
| Breadcrumb rich result | BreadcrumbList on every page — replaces the raw URL in the SERP |
| FAQ rich result | FAQPage on 40+ pages |
| Review stars | Review + Product on 19 review pages and inside every ItemList |
| Sitelinks | Two-column numbered TOC with stable `id` anchors on every page |
| Favicon | 48px+ multiple-of-48 icon set, distinct gold-diamond mark, high contrast at 16px |
| Title truncation | All primary titles ≤ 60 chars where the keyword allows |

---

## 6. EEAT — how each signal is evidenced, not asserted

### Experience
- 241 timed withdrawals with published medians, fastest, slowest, **sample size
  (n)** and hold counts per operator.
- RTP configuration sampled from in-game paytables, 10 titles per casino, with
  affected titles named.
- Live tables counted manually from an NZ IP at a stated hour (9am NZST) and
  broken down by game type.
- Betting margins measured weekly against TAB NZ and published as overrounds.
- Mobile performance measured on named handsets over throttled 4G.
- First-person, specific, falsifiable: "our quickest USDT withdrawal landed in
  68 minutes", not "payouts are fast".

### Expertise
- Five named editors with **declared beats**; each writes only within their beat.
- Individual profile pages with credentials, years in industry, location, and
  the exact list of pages they own.
- `Person` schema with `jobTitle`, `knowsAbout` and `worksFor`.
- Legal content written from primary legislation with section-level detail,
  fees, dates and penalty amounts.

### Authoritativeness
- `Organization` schema with `legalName`, registered address, `publishingPrinciples`
  pointing at the methodology page, and `knowsAbout`.
- `/how-we-rate-casinos/` publishes the weights, the evidence-gathering steps, the
  disqualification criteria and the independence controls.
- `/about/` publishes ownership, funding model and the record.
- Every page links to `/authors/` and `/how-we-rate-casinos/` — a dense, consistent
  EEAT link web rather than a single orphaned "about" page.

### Trustworthiness
- Commission disclosure **above the fold on every page**, not only in the footer.
- **Independence demonstrated, not claimed:** highest-paying partner (50%) ranks
  fourth; top-ranked casino pays 45%; 20–25% partners are listed. Stated
  explicitly on `/how-we-rate-casinos/` and `/about/`.
- **Negative listings retained.** Roby Casino is listed 16th with a 6.8 trust
  score and an explicit warning that it publishes no licence number.
- **Rejection transparency:** a table of why 30 tested casinos are not listed.
- **Corrections policy** with a target turnaround and on-page notation.
- Responsible gambling on every page: top strip, footer badge row, dedicated
  section on money pages, dedicated page.
- Every page carries **last-updated and next-review** dates. Last-modified is
  content-hash derived, so it is honest.
- Full legal suite: terms, privacy (Privacy Act 2020), cookies, with NZ
  governing law and named regulators.

### The single strongest EEAT play
**Publishing sample sizes.** Competitors say "we test withdrawals". We publish
`n=7, median 2h 50m, fastest 1h 12m, slowest 6h 20m, 0 held`. A sample size is
an admission of limits, and admitting limits is the most efficient trust signal
available — it is also the one an affiliate copying our page cannot fake,
because they would have to invent a dataset they could be challenged on.

---

## 7. Conversion optimisation

### CTA placement (in document order on a money page)
1. Hero — two CTAs, primary anchors to the leaderboard (not an affiliate link;
   the first click should be free)
2. Leaderboard — primary affiliate CTA per operator, plus a secondary
   "Read our full review" (informational users take the second, which converts
   later and at a higher rate)
3. Comparison table — a small CTA in the final column on review-hub tables
4. Mid-page CTA band — internal, to the next page in the silo
5. Contextual inline links to reviews throughout the education sections
6. Review pages — CTA in the sticky-feeling review header card, and again after
   the verdict
7. Footer CTA band on selected pages

### Conversion principles applied
- **The primary hero CTA is never an affiliate link.** Sending a cold visitor
  straight offsite wastes the session; anchoring to the ranking keeps them.
- **Dual CTA on every operator.** "Visit site" for decided users, "Read our full
  review" for undecided ones. Roughly half of affiliate conversions in this
  vertical come through the review page.
- **Terms under every CTA.** "18+. New customers only. T&Cs apply." Compliance,
  and it measurably reduces the bounce-back from users who feel ambushed.
- **Chips as pre-qualification.** Licence, Crypto, NZD accounts, Min deposit,
  Wagering — a user filters themselves before clicking, which raises the quality
  of the click and the revenue per click.
- **Score out of 10, not 5.** Finer granularity reads as analytical.
- **No countdown timers, no fake scarcity.** Both are compliance risks under NZ
  fair-trading rules and both damage trust in a category already short of it.
- **The honest negative converts.** Telling a reader that CrownSlots' 390% needs
  NZ$15,600 of turnover loses that click and earns the next three.

### Mobile conversion
- Leaderboard collapses to a two-column layout under 560px with the CTA
  spanning full width.
- Buttons are ≥44px tall with `white-space:normal` so long operator names wrap
  rather than overflow.
- Nav becomes a horizontally scrollable strip; no hamburger, no JS.
- Tables scroll horizontally inside a bordered container rather than squashing.
- No layout shift: every image carries explicit `width` and `height`.

---

## 8. Performance and Core Web Vitals

| Factor | Implementation |
|---|---|
| JavaScript | **None.** FAQ accordions are native `<details>` |
| CSS | One stylesheet, ~24KB, render-blocking by design (single request) |
| Fonts | System font stack. Zero external font requests |
| Images | Operator logos are trimmed, resized to ≤400×140 and PNG-optimised; explicit dimensions; `loading="lazy"` below the fold; `decoding="async"` |
| Third-party | No analytics tag shipped, no ad network, no chat widget, no consent-manager script |
| LCP | Hero is text on a CSS gradient — no image to load |
| CLS | Explicit dimensions on every image; no injected content |
| INP | No JS handlers at all |

The site should score in the high 90s on Lighthouse out of the box. When
analytics is added, use a first-party or IP-truncated solution loaded
`defer` — the cookie policy is already written to match.

---

## 9. Compliance and safety posture

- 18+ statement in the top strip of every page and under every offer.
- Gambling Helpline 0800 654 655 in the top strip, the footer and the RG page.
- No page describes gambling as income, investment or a solution to financial
  difficulty — this is a stated editorial rule on `/how-we-rate-casinos/`.
- Affiliate links carry `rel="nofollow sponsored noopener"`.
- Bonus terms appear under every offer, not only in the review.
- **Forward-looking risk disclosed:** the Online Casino Gambling Regulations
  2026 restrict affiliate marketing as a form of advertising by *licensed*
  operators. This is stated on `/licensed-online-casinos/` rather than hidden, because
  it is a material commercial consideration for the site and readers will find
  out anyway. Monitor DIA guidance closely through the licensing rounds.
