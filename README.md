# Casino Edge NZ

A complete, static, dependency-free affiliate site targeting **"best online
casino sites NZ"** and its surrounding clusters, built for New Zealand players.

47 pages · ~109,000 words · no JavaScript · no framework · no external requests.

---

## Before you deploy: set the domain

The domain is not yet registered, so the site currently builds against a
placeholder. Edit the top of `_build/lib.py`:

```python
DOMAIN = "casinoedge.co.nz"     # ← the real domain
NAME   = "Casino Edge NZ"       # ← the brand
NAME_HTML = 'Casino<i>Edge</i>&nbsp;NZ'
LEGAL  = "Casino Edge Media Limited"
NZBN   = "9429050000000"        # ← the real NZBN
POSTAL = "PO Box 106-172, Auckland 1143, New Zealand"
```

Then rebuild:

```bash
python3 _build/build.py
```

Every canonical, Open Graph URL, schema `@id`, sitemap entry and the robots.txt
`Sitemap:` directive follows from `DOMAIN`. Nothing else hard-codes the host.

---

## Monthly refresh

1. Update `MONTH` and `YEAR` in `_build/lib.py` (and `NEXT_REVIEW`).
   Every title tag and H1 follows the format `Primary Keyword [Month Year]:
   Secondary Keyword` and is rebuilt from these two constants. Titles are
   measured in pixels (Arial 20px) and the build **fails** if any exceeds 580px,
   so the SERP constraint can never silently break.
2. Re-verify the facts in `_build/operators.json` — bonuses, licences, rails.
3. Re-measure the payout medians in `_build/p_reviews.py` (`MEASURED`).
4. `python3 _build/build.py`

Titles, descriptions, H1s, hero eyebrows and review dates all follow the two
constants. Last-modified dates are content-hash derived, so a page that did not
change keeps the date it already had.

---

## Layout

```
_build/            build system — NOT deployed (blocked in robots.txt)
  build.py         orchestrator: pages + sitemap + robots + manifest + icons
  lib.py           identity, templating, components, schema, write()
  favicon.py       generates the whole icon set from code
  keywords.py      KEYWORD MAP — which page owns which terms, plus the 301 table
  operators.json   FACTS ONLY (licence, bonus, payouts, payment rails)
  copy_ops.py      EDITORIAL ONLY (scores, prose, pros/cons, verdicts)
  lastmod.json     content-hash manifest driving sitemap lastmod
  p_*.py           page modules
  docs/            strategy package — competitor research, keywords, SERP plan
assets/css/site.css
logos/             19 normalised operator logos
images/authors/    editor portraits, 192px and 64px squares
favicon-{48,96,144,192,512}.png, favicon.ico, apple-touch-icon.png
robots.txt, sitemap.xml, site.webmanifest
<47 page directories>/index.html
```

**Facts and opinion are separated on purpose.** If a bonus changes, edit the
JSON. If our view changes, edit the Python. They are never the same edit, which
keeps the site auditable.

---

## Strategy documents

| File | Contents |
|---|---|
| `_build/docs/01-competitor-research.md` | Who ranks, what they do well, and the nine exploitable gaps |
| `_build/docs/02-site-structure.md` | Full sitemap, page anatomy, technical spec, build system |
| `_build/docs/03-keyword-strategy.md` | 11 clusters, long-tail, entities, per-page mapping, anchor text, cannibalisation controls |
| `_build/docs/04-serp-eeat-and-conversion.md` | Schema inventory, snippet and PAA targeting, meta patterns, EEAT evidence, CTA plan, CWV |
| `_build/docs/05-scalability-roadmap.md` | Six expansion phases, cross-linking model, maintenance cadence |
| `_build/docs/06-title-tags.md` | Per-page competitor title analysis, every title and H1, measured widths, month-by-month headroom |
| `_build/docs/07-money-page-serp-teardown.md` | Homepage SERP teardown: competitor heading extraction, user-question mining, 12 content gaps, sourced statistics, Google Trends, final heading structure |
| `_build/docs/08-keyword-map-and-url-migration.md` | Keyword-to-page assignment, the URL migration and its 301s, cannibalisation controls, measured coverage and the anti-stuffing guard |

---

## Preview locally

```bash
python3 -m http.server 8777
# open http://localhost:8777/
```

---

## Redirects

Nine URLs were retired during the keyword re-targeting. `build.py` emits the 301s in four formats —
`_redirects` (Netlify/Cloudflare Pages), `.htaccess` (Apache), `vercel.json` and
`nginx-redirects.conf` — and deletes the retired directories so an old URL cannot return a 200.
Upload the one your host reads. `/instant-withdrawals/` is a redirect only; no page exists there.

## Welcome bonus

The bonus is the first thing on every page: `lib.hero_offer(op, kind)` renders the
leading offer directly under the H1, and each operator card carries its bonus in
its own labelled panel. The hero offer deliberately repeats the table's number-one
row — on a desktop the table starts below the fold, so without it the bonus is
not seen until the reader scrolls. `rel="nofollow sponsored noopener"`, 18+ and
the bonus terms are on every instance, checked by the build.

## Author portraits

`/images/authors/<slug>-192.jpg` and `-64.jpg`, cropped so the head fills 85% of
the square and sits slightly above centre — loose passport framing turns to mush
at the 24px byline size.

To swap a photo: put the new file beside the others, measure three numbers off it
(top of hair, bottom of chin, horizontal centre of the face, in source pixels),
add them to `FACES` in `_build/tools/crop_portraits.py`, then:

```bash
PORTRAIT_SRC=/path/to/headshots python3 _build/tools/crop_portraits.py
```

The templates and schema reference the output by slug, so nothing else changes.

**Before launch:** the five editor names, roles, biographies and credentials in
`_build/lib.py` are placeholders written during the build. Replace them with the
real people's details so the portraits, names and stated experience match.

## Navigation

**Every page on the site appears in the header at both sizes.**

- **≥961px** — a nested horizontal nav: Casinos ▾ · Betting ▾ · Reviews ▾ ·
  Guides ▾ · About ▾ · Contact. Panels are CSS-only (`:hover` + `:focus-within`),
  so they work for a mouse and a keyboard with no JavaScript.
- **≤960px** — a `<details>` hamburger with the same 47 pages, grouped.

Both are generated from the page data, and the build fails if either drifts from
the live URL set — so a new review or author page cannot be left out of
navigation.

## Keyword audit

Every build checks the rendered HTML against `_build/keywords.py` and **fails** if a Tier 1 term
drops off its page or if any term exceeds 1.2% density. Current state: Tier 1 and Tier 2 fully
covered on all 12 mapped pages, highest head-term density 0.95%.

## Deploy

Upload everything **except `_build/`**. Any static host works (Netlify, Cloudflare
Pages, S3, nginx). The site needs no server-side processing.

The contact form at `/contact/` posts to `/contact/` and needs a handler wiring
up on your host (Netlify Forms, Cloudflare Workers, or a small serverless
endpoint). Until then, the emailed contact routes on the page are live.

---

## Compliance notes

- 18+ messaging on every page; Gambling Helpline 0800 654 655 in the top strip
  and footer of every page.
- Affiliate links carry `rel="nofollow sponsored noopener"`.
- Commission disclosure appears above the fold on every commercial page.
- The Online Casino Gambling Regulations 2026 restrict affiliate marketing as a
  form of advertising by **licensed** New Zealand operators. This is disclosed on
  `/licensed-online-casinos/`. Monitor DIA guidance through the licensing rounds — it is
  a material commercial risk to the model.
