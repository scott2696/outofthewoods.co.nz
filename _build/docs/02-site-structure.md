# Site structure — Casino Edge NZ

47 pages, all extensionless (`/path/` → `path/index.html`). Every page is
reachable within two clicks of the homepage. About and Contact appear in both
the main horizontal navigation and the footer, as specified.

---

## Sitemap

```
/                                   Best Online Casino Sites NZ          [MONEY]  prio 1.0
│
├── /online-casinos/                Best Online Casinos NZ (all 16)      [MONEY]  0.95
│   └── /casino-bonus/    Casino Bonuses NZ                    [MONEY]  0.90
│
├── /online-pokies/                 Online Pokies NZ                     [MONEY]  0.85
├── /live-casino/                  Live Casinos NZ                      [MONEY]  0.85
├── /new-casinos-nz/            New Online Casinos NZ                [MONEY]  0.85
├── /no-deposit-bonus/            No Deposit Bonus NZ                  [MONEY]  0.85
├── /fast-payout-casinos/           Fastest Payout Casinos NZ            [MONEY]  0.85
├── /casino-payout-percentages/           Highest Payout Casinos NZ            [MONEY]  0.85
├── /crypto-casinos-nz/           Best Crypto Casinos NZ               [MONEY]  0.85
│
├── /online-betting/                Online Betting NZ                    [MONEY]  0.95
│   └── /best-sports-betting-sites/ Best Sports Betting Sites NZ         [MONEY]  0.90
│
├── /casino-reviews/                Casino Reviews hub                   [TRUST]  0.85
│   ├── /casino-reviews/spinjo/            … and 18 more                          0.70
│   └── (19 operator reviews in the supplied order)
│
├── /how-we-rate-casinos/                 Methodology                          [EEAT]   0.80
├── /casino-payment-methods/               Payment Methods NZ                   [INFO]   0.80
├── /licensed-online-casinos/               NZ Gambling Law                      [EEAT]   0.85
├── /responsible-gambling/          Responsible Gambling                 [TRUST]  0.75
│
├── /about/                         About Us                             [EEAT]   0.70
├── /contact/                       Contact Us                           [EEAT]   0.60
├── /authors/                       Authors hub                          [EEAT]   0.65
│   ├── /authors/jordan-whitcombe/  Editor-in-Chief                               0.50
│   ├── /authors/aroha-tainui/      Regulation & Compliance Editor                0.50
│   ├── /authors/priya-raman/       Payments & Data Editor                        0.50
│   ├── /authors/sam-kavanagh/      Games & Live Casino Editor                    0.50
│   └── /authors/manaia-kerr/       Betting Editor                                0.50
│
├── /terms-and-conditions/          Terms and Conditions                 [LEGAL]  0.30
├── /privacy-policy/                Privacy Policy                       [LEGAL]  0.30
├── /cookie-policy/                 Cookie Policy                        [LEGAL]  0.30
│
├── /sitemap.xml
├── /robots.txt
└── /site.webmanifest
```

---

## Navigation

**Desktop (≥961px) — nested horizontal nav.** Six top-level items, each a link
to its own hub and each opening a CSS-only panel, plus Contact as a direct link:

| Trigger | Links to | Panel contains |
|---|---|---|
| **Casinos** ▾ | `/online-casinos/` | 10 — two columns, *Compare* and *Games & offers* |
| **Betting** ▾ | `/online-betting/` | 2 |
| **Reviews** ▾ | `/casino-reviews/` | 20 — hub plus all 19 operators, three columns, right-aligned |
| **Guides** ▾ | `/how-we-rate-casinos/` | 4 — methodology, payments, licensing, responsible gambling |
| **About** ▾ | `/about/` | 10 — company and all 5 author pages, plus a Legal column |
| **Contact** | `/contact/` | — |

That is all 47 pages. Panels open on `:hover` and stay open on `:focus-within`,
so they are keyboard operable without JavaScript; each trigger is itself a real
link, so the nav still works if a panel never opens. The top-level item for the
section you are in carries a gold underline, and the current page is gold inside
its panel.

**Mobile and tablet (≤960px) — hamburger.** The horizontal nav is hidden and the
`<details>` menu takes over, holding the same 47 pages grouped into Casino guides
· Betting · Trust & data · Casino reviews · Company · Legal. Handing over at
960px rather than 820px avoids a two-row wrapped nav whose wide panels ran off
the side of the screen.

The build fails if either the nav or the hamburger drifts from the site's live
URL set, so a new page cannot be left out of navigation.

**Footer, five columns:**

| Column | Links |
|---|---|
| Casino guides | Best online casinos NZ, Online pokies, New online casinos, Live casinos, High payout, Fast payout, Crypto, No deposit, Casino bonuses |
| Betting | Online betting NZ, Best sports betting sites, Casino reviews |
| Trust & data | How we review, Payment methods, NZ gambling law, Our authors |
| Company | **About us**, **Contact us**, Authors, Sitemap |
| Legal | Terms and conditions, Privacy policy, Cookie policy, Responsible gambling |

Footer also carries a trust badge row: 18+ · Gamble responsibly · Gambling
Helpline 0800 654 655 · Problem Gambling Foundation · Published methodology ·
Named authors.

---

## Page anatomy (applied consistently across all money pages)

1. **Top strip** — 18+ · commission disclosure link · Gambling Helpline number
2. **Sticky header** — brand, nav, gold CTA
3. **Hero** — eyebrow (freshness + proof point), H1, lede, two CTAs, 4-stat band
4. **Hero** carries its own **breadcrumbs** (top, with BreadcrumbList schema) and
   closes with the **byline** — writer + fact-checker + updated date + next review —
   separated by a hairline, so authorship sits inside the same band as the H1
   rather than in a strip beneath it
4b. **Hero offer** — the page's leading welcome offer sits directly under the H1:
   operator logo, a gold "Top welcome offer" label, the bonus in 33px bold, the
   brand/score/wagering/min-deposit line, a `Claim offer` button and a review
   link, with the bonus terms and 18+ notice beneath. On a desktop the operator
   table starts below the fold, so without this the bonus is not seen until the
   reader scrolls. Where an offer is present the hero's secondary anchor buttons
   are dropped so nothing competes with it.

5. **H2 + ranked leaderboard** — the operator table follows the hero and its H2
   directly, on every viewport, with nothing between the heading and the table
6. **Explanatory line and any caveat notes** — released underneath the table
7. **Disclosure box** — how we make money
8. **Direct-answer paragraph** — featured-snippet target, 40–55 words
9. **TOC / jump menu** — two-column, numbered
10. **Rest of page** — rank, logo, badge, bonus, page-specific note, chips,
   terms, score, CTA, review link, score bar
10. **Comparison table(s)** — the numbers competitors do not publish
11. **Segmented "best for" card grid**
12. **Education sections** — 4–7 H2 blocks, alternating background bands
13. **FAQ accordion** — `<details>`, 6–12 questions, FAQPage schema from the
    same source list so markup and visible content cannot drift
14. **Author box** — photo-less avatar, credentials, link to profile
15. **CTA band** — internal, to the next-best page in the silo
16. **Footer**

---

## Word counts (actual, built)

| Page | Words |
|---|---|
| / (homepage) | ~3,400 |
| /online-casinos/ | ~2,600 |
| /online-betting/ | ~3,300 |
| /casino-bonus/ | ~2,300 |
| /online-pokies/ | ~2,500 |
| /fast-payout-casinos/ | ~2,400 |
| /crypto-casinos-nz/ | ~2,600 |
| /licensed-online-casinos/ | ~2,700 |
| /responsible-gambling/ | ~2,800 |
| /how-we-rate-casinos/ | ~2,300 |
| /casino-payment-methods/ | ~2,400 |
| Each operator review | ~1,000–1,300 |
| **Site total** | **~88,400** |

---

## Internal linking model

Hub-and-spoke with deliberate cross-silo bridges:

- **Homepage** links down to every category page and to the four trust pages.
- **Category pages** link laterally to two or three sibling categories via the
  CTA band, and up to `/online-casinos/`.
- **Every operator mention** in a leaderboard links to its review (`/casino-reviews/<slug>/`).
- **Every review** links back to the category page it is strongest on, to
  `/how-we-rate-casinos/`, `/casino-bonus/`, `/responsible-gambling/`, and
  to three sibling reviews.
- **Every page** links to `/authors/<slug>/` twice (byline + author box) and to
  `/how-we-rate-casinos/` from the disclosure box — this is the EEAT link web.
- **Legal and law pages** are linked from the disclosure box, the footer and
  contextually from the law section of every money page.

Anchor text is descriptive and varied — never "click here", never the raw URL.
See `03-keyword-strategy.md` for the anchor-text plan.

---

## Technical specification

| Item | Implementation |
|---|---|
| URLs | Extensionless, trailing slash, lowercase, hyphenated |
| Canonical | Self-referencing absolute URL on every page |
| Robots meta | `index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1` |
| Language | `lang="en-NZ"`, `og:locale en_NZ` |
| Schema | Single `@graph` per page — Organization, WebSite, plus page-specific |
| Favicon | 48, 96, 144, 192, 512 px PNG + multi-res .ico + 180px apple-touch-icon |
| Manifest | `site.webmanifest` with maskable icons ≥192 |
| CSS | One 480-line stylesheet, no framework, no external font requests |
| CSS cache-busting | The stylesheet URL carries a content hash (`site.css?v=<sha>`), so a browser holding an older copy picks up a redesign immediately instead of serving stale CSS after a deploy |
| JavaScript | None. FAQ accordions use native `<details>` |
| Images | Explicit width/height, `loading="lazy"` below the fold, `decoding="async"` |
| Affiliate links | `rel="nofollow sponsored noopener" target="_blank"` |
| External links | `rel="noopener nofollow"` where appropriate |
| Accessibility | Skip link, landmark roles, `aria-current`, focus-visible outlines, WCAG AA contrast throughout, `prefers-reduced-motion` honoured |
| Author portraits | Each editor has a 192px and 64px square JPEG in `/images/authors/`, used in bylines (26px, eager — it sits in the first viewport on a phone), author boxes (56px), the authors table (34px) and a 92px portrait block on each profile page. Also emitted as `image` on the `Person` and `ProfilePage` schema. 44KB for all ten files |
| Welcome bonus emphasis | The bonus is the loudest element on every page. In the hero it is 33px bold in a gold-bordered panel; in each operator card it sits in its own labelled panel (gold-tinted on the top pick) at 21px desktop / 19px mobile. Verified visible without scrolling at 320–1440px |
| Mobile ordering | Under 820px `main` becomes a flex column and the three blocks that matter — H1, byline, operator table — are ordered above the disclosure, lede and contents. Verified: on a 402px viewport the H1 sits at 88px, the byline at 186px, the H2 at 278px and the first operator card (CTA included) is fully visible by 681px |
| Horizontal overflow | Zero across 17 pages × 320/360/402/768/1280px viewports |
| Sitemap | Auto-generated, priority + changefreq + content-hash lastmod |
| Operator card, mobile | Under 820px the three wrapper divs collapse to `display:contents` so every leaf is ordered against the card itself: rank and badge pinned to the top corners, then logo, name, note, score bar, a `Our score / X.X/10` row, the offer in its own labelled panel, a full-width CTA and the terms. One DOM serves both layouts — no duplicated markup |
| robots.txt | Sitemap URL + the seven specified SEO-crawler blocks + twelve more |

**Last-modified dates are content-hash derived.** A page that has not changed
keeps the date it already carried, so `lastmod` in the sitemap means something
rather than being reset on every build.

---

## Build system

```
NZ No 2/
├── _build/              # not deployed — blocked in robots.txt
│   ├── build.py         # orchestrator: pages, sitemap, robots, manifest, icons
│   ├── lib.py           # identity, templating, components, schema, write()
│   ├── favicon.py       # generates the icon set from code
│   ├── operators.json   # FACTS only — licence, bonus, payouts, rails
│   ├── copy_ops.py      # EDITORIAL only — scores, prose, pros/cons, verdicts
│   ├── lastmod.json     # content-hash manifest
│   ├── p_*.py           # page modules
│   └── docs/            # this strategy package
├── assets/css/site.css
├── logos/               # 19 normalised operator logos
├── favicon-*.png, favicon.ico, apple-touch-icon.png, site.webmanifest
├── robots.txt, sitemap.xml
└── <47 page directories>/index.html
```

Rebuild everything: `python3 _build/build.py`

**Facts and opinion are deliberately separated.** `operators.json` holds only
checkable facts; `copy_ops.py` holds only things a human wrote. If a bonus
changes, the JSON changes. If our view changes, the Python changes. They are
never the same edit, which makes the site auditable.

---

## Changing the domain

Edit two constants at the top of `_build/lib.py`:

```python
DOMAIN = "casinoedge.co.nz"     # ← the real domain
NAME   = "Casino Edge NZ"       # ← the brand, if it changes with the domain
```

Then run `python3 _build/build.py`. Every canonical, Open Graph URL, schema
`@id`, sitemap entry and the robots.txt sitemap directive follow. Nothing else
in the codebase hard-codes the host. `NAME_HTML`, `LEGAL`, `NZBN` and the email
addresses sit directly beneath and should be updated at the same time.
