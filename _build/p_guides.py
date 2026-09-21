# -*- coding: utf-8 -*-
"""Trust and guide pages: methodology, payments, NZ law, responsible gambling."""
import lib, copy_ops
from lib import (MONTH_YEAR, MONTH, YEAR, NAME, LEGAL, EMAIL, EMAIL_COMPLAINTS,
                 N_WITHDRAWALS, N_OPERATORS_TESTED, N_HOURS, table, faq, keyfacts,
                 note, toc, steps, cards, ctaband, authorbox, byline, hero,
                 section, h2, h3, pros_cons, crumbs, timeline, AUTHORS, AUTHOR_ORDER)


# ===========================================================================
def build_methodology():
    path = "/how-we-rate-casinos/"
    faqs = [
     ("Do operators pay for a better ranking?",
      "<p>No, and the data shows it. Our highest commission partner, CrownSlots at 50%, ranks fourth. "
      "Our lowest, Ivibet and Slotsgem at 20%, are not excluded &mdash; they are ranked where their "
      "scores put them. Kingdom pays us 45% and outranks CrownSlots at 50%. If commission drove the "
      "order, none of that would be true.</p>"),
     ("Do you let operators see reviews before publication?",
      "<p>No. Operators see a review when readers do. We will correct a factual error at any time and "
      "we log the correction, but we do not send drafts for approval and we do not accept edits to "
      "opinion. Two operators have asked; both requests are recorded in the relevant reviews.</p>"),
     ("How often is the data refreshed?",
      "<p>Monthly, on a fixed cycle. Payout medians are re-measured, licence numbers and corporate "
      "entities are re-verified, bonus terms are re-read in full, and live table counts are "
      "re-counted from a New Zealand IP. Pages carry a &lsquo;next review&rsquo; date so you can see "
      "when the current figures expire.</p>"),
     ("How can I tell if an online casino is legit myself?",
      "<p>Knowing how to tell if an online casino is legit comes down to six checks, all at the top "
      "of this page. In order of how much they tell you: a "
      "licence number that verifies on the regulator&rsquo;s register, a named operating "
      "company, independent game testing by eCOGRA, iTech Labs or GLI, a weekly withdrawal "
      "cap above the maximum bonus, working responsible gambling tools, and a NZ$50 test "
      "deposit followed by a NZ$30 withdrawal in week one. The last one settles it.</p>"),
     ("What makes you qualified to review casinos?",
      "<p>Five named editors with declared beats and checkable backgrounds, listed on our "
      "<a href=\"/authors/\">authors page</a>. Between them: thirteen years in online gambling "
      "including six in operator payments, an LLB and a practice of reading primary legislation, ten "
      "years in payments analytics, seven years auditing game libraries, and eleven years in sports "
      "trading. Every page names the writer and a separate fact-checker.</p>"),
     ("Why do you list casinos you would not use?",
      "<p>Because a list that contains only recommendations is an advertisement. Roby Casino is on "
      "this site with a 6.8 trust score and an explicit warning that it publishes no licence number. "
      "Readers deserve to know it exists, that it has a large bonus, and exactly why we rank it "
      "sixteenth.</p>"),
     ("Can I see the raw data?",
      "<p>The measured medians, sample sizes, RTP configuration samples and market depth audits are "
      "published in the relevant pages rather than held back. If you want the detail behind a "
      "specific figure, email <a href=\"mailto:%s\">%s</a> and we will send it.</p>" % (EMAIL, EMAIL)),
    ]

    body = [hero(
      "Our scoring model, published in full",
      lib.seo_h1(path),
      "Every score on this site comes from the same weighted model, applied to evidence we collected "
      "ourselves. This page sets out the weights, what each component measures, how the evidence is "
      "gathered, and what would make us change a score. If a ranking on this site ever looks odd, "
      "this page is where you check our working.",
      stats=[("5", "Scored components"), ("%d" % N_OPERATORS_TESTED, "Operators tested"),
             ("%d" % N_WITHDRAWALS, "Withdrawals timed"), ("%s" % N_HOURS, "Hours of testing")],
      ctas=[("See the weights", "#weights"), ("Our editors", "/authors/")], aqua=True)]

    s = [crumbs([("Home", "/"), ("How we review", None)]),
         byline("jordan-whitcombe", "aroha-tainui"),
         "<p>Most gambling comparison sites publish a ranking and ask you to trust it. We would rather "
         "publish the model. Below is our full online casino review methodology: the exact weights, "
         "the evidence behind each component, the things we refuse to do, and how we are paid. If you "
         "only want the practical version &mdash; how to choose an online casino NZ side without "
         "relying on us at all &mdash; start with the six checks immediately below.</p>",
         toc([("The weighting", "weights"), ("What each component measures", "components"),
              ("How the evidence is gathered", "evidence"),
              ("The withdrawal timing programme", "timing"),
              ("What disqualifies an operator entirely", "disqualify"),
              ("How we are paid, and what it does not buy", "money"),
              ("Corrections and complaints", "corrections"),
              ("Editorial standards", "standards"),
              ("Frequently asked questions", "faq")])]
    body.append(section("\n".join(s)))

    s = [h2("The weighting", "weights"),
         "<p>Five components, weighted as below. The overall score is the weighted mean, rounded to "
         "one decimal place. Component marks appear at the top of every review so you can re-weight "
         "them for your own priorities.</p>",
         table(["Component", "Weight", "What it measures", "Primary evidence"], [
      ["Payout speed", "<b>25%</b>", "Time from confirming a withdrawal to funds being available, "
       "plus weekly caps and how often requests are held", "Our timed withdrawal log"],
      ["Bonus value", "<b>20%</b>", "Turnover required relative to bonus granted, game weighting, "
       "maximum bet and expiry &mdash; not headline size", "Full reading of the bonus terms"],
      ["Game library", "<b>20%</b>", "Studio coverage against a fixed nine-studio list, verified RTP "
       "configuration, live table count, filtering quality", "Manual audit from an NZ IP"],
      ["Banking &amp; NZD", "<b>15%</b>", "NZD wallet and NZD bank transfer, rail breadth, minimum "
       "deposit, FX spread on non-NZD sites", "Cashier testing with real deposits"],
      ["Trust &amp; disclosure", "<b>20%</b>", "Licence verifiability, named operating company, "
       "independent game testing, complaints path, responsible gambling tools, trading history",
       "Regulator registers and the operator&rsquo;s own footer"],
     ], caption="Scoring weights, applied identically to every operator"),
     note("<b>Why payout speed carries the most weight.</b> Every other quality is theoretical if the "
          "money does not come back. It is also the component operators most often let slip after "
          "launch, which is why we re-measure it monthly rather than annually.", "info")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("What each component measures", "components"),
         h3("Payout speed &mdash; 25%", "c-payout"),
         "<p>Measured, not claimed. We request withdrawals on real balances and record the time from "
         "clicking confirm to funds being available &mdash; not to the operator marking the request "
         "approved, which is the number operators quote. A site scores well by being fast <em>and</em> "
         "consistent: a 40-minute best result alongside a four-day worst result scores below a steady "
         "three hours. Weekly caps are folded in, because a cap below the maximum bonus is a delay "
         "mechanism.</p>",
         h3("Bonus value &mdash; 20%", "c-bonus"),
         "<p>Scored on the turnover contract, never on the headline. We compute the turnover required "
         "on a standard NZ$100 deposit, apply the game weighting to the games a typical player would "
         "use, and check the maximum bet and the expiry. A 600% package at 40x scores below a 100% "
         "package at 10x, which is why Smash outscores CrownSlots on this component despite a smaller "
         "effective match.</p>",
         h3("Game library &mdash; 20%", "c-games"),
         "<p>Counted, not quoted. Studio coverage is checked against a fixed list of nine studios. "
         "RTP configuration is sampled across ten popular titles by opening each game&rsquo;s paytable "
         "&mdash; a casino running reduced builds loses marks here regardless of lobby size. Live "
         "tables are counted manually at 9am NZST, which is when thin floors show up.</p>",
         h3("Banking and NZD &mdash; 15%", "c-banking"),
         "<p>A true New Zealand dollar wallet with NZD bank transfer scores highest, because a "
         "euro-denominated site costs a Kiwi roughly 2&ndash;3% on each conversion. We measure the "
         "actual amount credited against the amount sent to calculate the real spread rather than "
         "taking the cashier&rsquo;s stated rate.</p>",
         h3("Trust and disclosure &mdash; 20%", "c-trust"),
         "<p>The component that separates otherwise similar sites. Full marks require a licence number "
         "published on the site that verifies on the regulator&rsquo;s register, a named operating "
         "company, stated independent game testing, a reachable complaints path, and responsible "
         "gambling tools usable within three clicks. Trading history matters: an operator under two "
         "years old cannot reach the top of this component regardless of everything else.</p>"]
    body.append(section("\n".join(s)))

    s = [h2("How to choose an online casino, and tell if an online casino is legit", "how-to-choose"),
         "<p>Most readers arrive at this page for one of two reasons: to audit our working, or because "
         "they want to know how to choose an online casino NZ players can rely on without taking "
         "anybody&rsquo;s word for it. This section is for the second group. It is the short version of "
         "the model below, and you can run all six checks in about five minutes.</p>",
         steps([
      ("Find the licence number, not the badge",
       "Scroll to the footer. A logo is worth nothing; a number is worth checking. This is how to "
       "check if a casino is licensed in NZ terms &mdash; there is no New Zealand register yet, so you "
       "verify against the regulator that issued it: the Cura&ccedil;ao Gaming Control Board, Anjouan "
       "or Tobique. If there is no number at all, stop here."),
      ("Find the company behind the licence",
       "A named entity &mdash; Rabidi N.V., Dama N.V., Vertikal N.V., TechOptions Group &mdash; means "
       "there is a counterparty. &lsquo;Not published&rsquo; means you have nobody to escalate to "
       "beyond the regulator, which is most of how to tell if an online casino is legit."),
      ("Check who tests the games",
       "eCOGRA, iTech Labs or GLI should be named somewhere. That certification covers the random "
       "number generator and the stated return to player, and it is what makes the games themselves "
       "trustworthy independent of the operator."),
      ("Read the withdrawal terms before the bonus terms",
       "Weekly cap, stated processing window, and whether identity verification happens at "
       "registration or at first cashout. What makes an online casino safe in practice is mostly "
       "whether it pays, and these three numbers predict that better than anything else on the site."),
      ("Open the responsible gambling tools",
       "Deposit limit, cooling-off, self-exclusion &mdash; reachable from account settings within "
       "three clicks, and working. An operator that hides them, or requires an email to support to "
       "activate them, has told you something."),
      ("Deposit NZ$50 and withdraw NZ$30 in week one",
       "The only test that settles it. Time it. What makes an online casino safe for you specifically "
       "is that it gave your money back when you asked, on the schedule it promised."),
     ]),
         h3("Casino licensing explained", "licensing-explained"),
         "<p>Casino licensing explained in one paragraph: a licence is a jurisdiction agreeing to "
         "supervise an operator in exchange for fees and compliance, and its value to you is entirely "
         "a function of how seriously that jurisdiction takes the job. The Malta Gaming Authority and "
         "the UK Gambling Commission sit at the strict end, with segregated player funds and mandatory "
         "dispute resolution. The Cura&ccedil;ao Gaming Control Board, which replaced the old "
         "master-licence system in 2024, is a genuine improvement on what came before and a step below "
         "those two. Anjouan and Tobique are lighter still. None of them protects your balance if the "
         "operator fails.</p>",
         "<p>New Zealand will have its own register from 2027 under the Online Casino Gambling Act "
         "2026, at which point how to check if a casino is licensed in NZ becomes a single lookup "
         "rather than a judgement call. <a href=\"/licensed-online-casinos/\">We track that here</a>.</p>",
         note("<b>What this is not.</b> This page is our online casino review methodology, published "
              "so you can check our working &mdash; not a guarantee about any operator. We test, we "
              "publish what we found and the sample size behind it, and we re-test monthly. Where we "
              "have not tested something we say so rather than filling the gap.", "info")]
    body.append(section("\n".join(s)))

    s = [h2("How the evidence is gathered", "evidence"),
         steps([
      ("Register from a New Zealand IP address",
       "Auckland or Christchurch, on a residential connection. Not a VPN, and not an office in another "
       "country &mdash; geo-behaviour is part of what we are testing."),
      ("Complete identity verification and time it",
       "Real documents, real turnaround. The median across the current cohort is 14 hours and the "
       "worst was four days."),
      ("Deposit on at least two rails",
       "One fiat and one fast rail, recording the exact amount credited so the foreign-exchange "
       "spread can be calculated on non-NZD sites."),
      ("Play a fixed two-hour session",
       "Across pokies, a live table and, where offered, a crash game. Ten titles are opened "
       "specifically to read their RTP configuration from the paytable."),
      ("Read every bonus term in full",
       "Multiple, what it applies to, game weighting, maximum bet, excluded titles, expiry, maximum "
       "cash-out. This takes longer than the session does."),
      ("Withdraw, and start a stopwatch",
       "Recorded to the minute. Repeated monthly thereafter, which is how the medians accumulate."),
      ("Test support three times at different hours",
       "Including one attempt between 2am and 4am NZST. Each asks something the terms page answers "
       "ambiguously, so we are testing accuracy as well as speed."),
      ("Verify the paperwork independently",
       "Licence number against the regulator&rsquo;s register, corporate entity against public "
       "records, game testing certificates, responsible gambling tools opened and actually used."),
     ]),
     h3("The withdrawal timing programme", "timing"),
     "<p>Every payout figure on this site comes from one log. It records the operator, the rail, the "
     "amount, the timestamp at confirmation, the timestamp at funds availability, whether the request "
     "was held for review and what was asked for. It currently holds %d withdrawals across %d "
     "operators, and it is the reason we publish sample sizes beside every median. A median with no n "
     "is marketing.</p>" % (N_WITHDRAWALS, N_OPERATORS_TESTED)]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("What disqualifies an operator entirely", "disqualify"),
         "<p>Some findings end the assessment rather than reducing a score. An operator that hits any "
         "of these is not listed at any position.</p>",
         "<ul>"
         "<li><b>A withdrawal not paid within seven days with no explanation given.</b> This is the "
         "line. Eleven of the operators we tested failed here.</li>"
         "<li><b>Bonus terms that differ between the promotion page and the account terms.</b> Four "
         "failed here.</li>"
         "<li><b>No contactable support across three attempts at different hours.</b> Four failed.</li>"
         "<li><b>Accepting a New Zealand registration and then blocking deposits or game launch from "
         "an NZ IP.</b> Three failed.</li>"
         "<li><b>Any request that we alter a factual finding in exchange for commercial terms.</b> "
         "No operator has been delisted for this, but two have asked and it is recorded in their "
         "reviews.</li></ul>",
         note("<b>What does not disqualify an operator.</b> A weak licence, a bad bonus, a small "
              "lobby or a slow cashier. Those reduce the score and are described plainly, because a "
              "reader deciding between a big bonus and a strong licence deserves to see both options "
              "with the trade-off explained &mdash; not to have one hidden from them.", "info")]
    body.append(section("\n".join(s)))

    s = [h2("How we are paid, and what it does not buy", "money"),
         "<p>%s is free to read and carries no display advertising. We are paid a revenue share by "
         "operators when a reader opens an account through one of our links. That is the entire "
         "business model and it is disclosed at the top of every page that contains such a link.</p>"
         % NAME,
         "<p>The conflict is real and we are not going to pretend otherwise. Here is how it is "
         "managed, and how you can check that it is.</p>",
         table(["Control", "How it works", "How you can verify it"], [
      ["Scores precede commercial terms", "Operators are scored before rates are discussed, and a "
       "rate change does not trigger a re-score", "Compare our published rates against our rankings "
       "&mdash; they do not correlate"],
      ["Published weights", "The model on this page is applied identically to every operator",
       "Component scores are on every review; recompute the weighted mean yourself"],
      ["Negative listings retained", "We list operators we would not use, with reasons",
       "Roby Casino, ranked 16th with a 6.8 trust score and an explicit warning"],
      ["No pre-publication review", "Operators do not see reviews before readers",
       "Requests to the contrary are logged in the review concerned"],
      ["Commission disclosed", "Revenue share rates are a matter we will state on request",
       "Email <a href=\"mailto:%s\">%s</a> and ask about any operator" % (EMAIL, EMAIL)],
     ], caption="Editorial independence controls"),
     "<p>The clearest test available: our top-ranked casino, Spinjo, pays us 45%. CrownSlots pays 50% "
     "and ranks fourth. Spino pays 25% and Ivibet pays 20%, and both are listed. If commission set "
     "the order, the page would look completely different.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Corrections and complaints", "corrections"),
         "<p>We get things wrong. When we do, we want to know quickly.</p>",
         "<ul>"
         "<li><b>Factual error on a page:</b> email <a href=\"mailto:%s\">%s</a> with the URL and what "
         "is wrong. We aim to respond within two working days and to correct within five. Material "
         "corrections are noted on the page.</li>" % (EMAIL, EMAIL) +
         "<li><b>Complaint about an operator:</b> email <a href=\"mailto:%s\">%s</a>. We cannot "
         "adjudicate a dispute &mdash; we are a publisher, not a regulator &mdash; but we log every "
         "complaint against the operator&rsquo;s trust score, we will tell you which regulator to "
         "escalate to, and a pattern of complaints affects the ranking.</li>" % (EMAIL_COMPLAINTS, EMAIL_COMPLAINTS) +
         "<li><b>Complaint about us:</b> same address. If you believe a page is misleading, say so "
         "and we will review it against this methodology.</li></ul>",
         h3("Editorial standards", "standards"),
         "<p>The standing rules this masthead operates under:</p>",
         "<ul>"
         "<li>If we have not tested it, we do not claim it. Where a figure comes from an operator "
         "rather than from us, the page says so.</li>"
         "<li>Every number carries its sample size or its source.</li>"
         "<li>Every content page names a writer and a separate fact-checker, both with public "
         "profiles.</li>"
         "<li>Legal content is written from primary legislation and regulator guidance, never from "
         "another publisher&rsquo;s summary.</li>"
         "<li>Negatives appear in the listing, not buried in the review.</li>"
         "<li>No page on this site will ever describe gambling as a way to make money, solve a "
         "financial problem or generate income.</li>"
         "<li>Responsible gambling information appears on every page, not only on the responsible "
         "gambling NZ page dedicated to it. The Gambling Helpline NZ number sits in the strip at the "
         "top of every page and in every footer.</li></ul>",
         faq(faqs, "Questions about our methodology", "faq"),
         authorbox("jordan-whitcombe")]
    body.append(section("\n".join(s)))

    trail = [("Home", "/"), ("How we review", path)]
    schema = [lib.article_schema(path, "How We Review", "Our published scoring model and editorial "
                                 "standards.", "jordan-whitcombe", "aroha-tainui", "Methodology"),
              lib.breadcrumb_schema(path, trail), lib.faq_schema(path, faqs)]
    lib.write(path, lib.seo_title(path),
              "The full scoring model behind every ranking on this site: five weighted components, "
              "how the evidence is gathered, and how we are paid.",
              "\n".join(body), schema, prio=0.8, freq="monthly")


# ===========================================================================
def build_payments():
    path = "/casino-payment-methods/"
    faqs = [
     ("What is the best payment method for NZ online casinos?",
      "<p>NZD bank transfer at a casino that holds a New Zealand dollar balance, if speed is not "
      "critical. USDT on the Tron network if it is. Those two cover almost every situation: the first "
      "has no conversion cost and no crypto learning curve, the second clears in hours instead of "
      "days.</p>"),
     ("Can I still use POLi at an online casino?",
      "<p>No. This is the most out-of-date claim on competing New Zealand casino pages. POLi itself is "
      "operating normally &mdash; it was acquired by Merco, it connects through bank-approved open "
      "banking APIs following the December 2025 rules, and eight New Zealand banks partner with it "
      "&mdash; but it is not available as a deposit method at online casinos serving New Zealand in "
      "2026. Any page showing you a POLi logo for casino deposits has not been checked.</p>"),
     ("Why did my bank decline a casino deposit?",
      "<p>New Zealand banks can decline transactions coded to gambling merchant categories, and "
      "several do so on credit cards as a matter of policy. Debit usually works where credit does "
      "not. If your bank blocks both, the practical workarounds are Neosurf (a prepaid voucher bought "
      "at a dairy or service station), MiFinity, or crypto. Note that credit cards are banned outright "
      "for licensed operators under the Online Casino Gambling Regulations 2026.</p>"),
     ("Can I use PayPal at an online casino in New Zealand?",
      "<p>No. PayPal does not process gambling transactions for New Zealand users at any offshore "
      "casino we have tested. Apple Pay and Google Pay appear at a small number of sites as a card "
      "wrapper, which means they inherit the same bank decline behaviour as the underlying card.</p>"),
     ("How long does a withdrawal take?",
      "<p>Crypto: 30 minutes to 8 hours, median about 3 hours across the operators we track. "
      "E-wallets: 4 to 24 hours. NZD bank transfer: 1 to 3 business days. Cards: 2 to 5 business "
      "days. Almost all of the variance is the operator&rsquo;s approval queue rather than the "
      "payment network. Our <a href=\"/fast-payout-casinos/\">timed data</a> has the detail.</p>"),
     ("Do I have to withdraw to the same method I deposited with?",
      "<p>Usually yes, up to the amount you deposited. Anti-money-laundering rules require operators "
      "to reverse the original rail first. Beyond that amount you can normally nominate another "
      "verified method, but doing so triggers a manual review and adds a day or two. Plan your exit "
      "rail before you deposit &mdash; particularly if you are using a voucher, which cannot pay "
      "out.</p>"),
     ("What does a currency conversion actually cost me?",
      "<p>Typically 2&ndash;3% per conversion at the cashier&rsquo;s rate, and you pay it twice "
      "&mdash; once going in, once coming out. On a NZ$500 deposit and a NZ$1,200 withdrawal that is "
      "roughly NZ$40 gone for nothing. Over a year of regular play at a euro-denominated site it "
      "exceeds the value of most welcome bonuses.</p>"),
     ("Are there fees on casino deposits or withdrawals?",
      "<p>The operators we list do not charge a direct fee on standard transactions. The costs are "
      "indirect: the currency spread above, a blockchain network fee on crypto (about NZ$1.50 on "
      "Tron, more on Ethereum), and your e-wallet&rsquo;s own fee for moving money to a New Zealand "
      "bank account. Skrill and Neteller both charge for that and it is easy to overlook.</p>"),
    ]

    body = [hero(
      "Checked and corrected for %s" % MONTH_YEAR,
      lib.seo_h1(path),
      "Which deposit and withdrawal methods actually work at online casinos from New Zealand right "
      "now &mdash; including the ones that used to and no longer do. Every rail below was tested with "
      "a real deposit and, where possible, a real withdrawal.",
      stats=[("11", "Rails tested"), ("3 h", "Median crypto payout"),
             ("2&ndash;3%", "Typical FX cost each way"), ("POLi", "No longer at casinos")],
      ctas=[("The full table", "#table"), ("Fastest payouts", "/fast-payout-casinos/")], aqua=True)]

    s = [crumbs([("Home", "/"), ("Payment methods", None)]),
         byline("priya-raman", "jordan-whitcombe"),
         "<p>Payment pages age badly, and most New Zealand casino payment pages are wrong in at least "
         "one important respect. This one is re-tested monthly and it says plainly where the market "
         "has moved.</p>",
         note("<b>The correction most pages have not made.</b> POLi is no longer available as a "
              "deposit method at online casinos serving New Zealand. POLi the company is fine and "
              "operating &mdash; Merco-owned, bank-API connected since the December 2025 open banking "
              "rules, eight New Zealand bank partners &mdash; but the casino channel has gone. If a "
              "comparison site is still showing you POLi logos on casino cards, treat everything else "
              "on that page as equally current.", "warn"),
         toc([("Every method, compared", "table"), ("NZD accounts and why they matter", "nzd"),
              ("Bank transfers and card deposits", "bank"),
              ("Prepaid vouchers: Neosurf and Paysafecard", "vouchers"),
              ("E-wallets", "ewallets"), ("Cryptocurrency", "crypto"),
              ("Which casinos support what", "by-casino"),
              ("Verification and why it delays your first payout", "kyc"),
              ("Frequently asked questions", "faq")])]
    body.append(section("\n".join(s)))

    s = [h2("Every method, compared", "table"),
         table(["Method", "Deposit", "Withdraw", "Speed out", "Real cost", "Verdict for Kiwis"], [
      ["NZD bank transfer", "Yes", "Yes", "1&ndash;3 business days", "Usually free",
       "<b>Best fiat option.</b> Only at casinos with a true NZD wallet."],
      ["Visa / Mastercard debit", "Yes", "Usually", "2&ndash;5 business days", "FX if non-NZD site",
       "Reliable enough. Some banks decline gambling codes."],
      ["Credit card", "Often declined", "Rarely", "&mdash;", "Cash advance fees",
       "<b>Avoid.</b> Banned for licensed operators under the 2026 regulations."],
      ["Neosurf", "Yes", "<b>No</b>", "&mdash;", "Voucher purchase price",
       "Good for control. You need a second method to cash out."],
      ["Paysafecard", "Yes", "<b>No</b>", "&mdash;", "Voucher purchase price",
       "Same as Neosurf. Deposit only."],
      ["Skrill", "Yes", "Yes", "4&ndash;24 hours", "Wallet fee to NZ bank",
       "Fastest reliable fiat cashout."],
      ["Neteller", "Yes", "Yes", "4&ndash;24 hours", "Wallet fee to NZ bank", "As Skrill."],
      ["MiFinity", "Yes", "Yes", "8&ndash;24 hours", "Wallet fee",
       "Useful when your bank blocks gambling codes."],
      ["Jeton", "Yes", "Yes", "8&ndash;24 hours", "Wallet fee", "Kingdom and Smash only."],
      ["Bitcoin", "Yes", "Yes", "30 min &ndash; 8 hours", "Network fee + volatility",
       "Fast, but the price moves while you wait."],
      ["USDT (Tron)", "Yes", "Yes", "<b>30 min &ndash; 4 hours</b>", "&asymp;NZ$1.50 network fee",
       "<b>Fastest overall.</b> Stable value, cheap, widely supported."],
      ["POLi", "<b>No longer offered</b>", "No", "&mdash;", "&mdash;",
       "Withdrawn from the casino channel. Still operates elsewhere in NZ."],
      ["PayPal", "<b>No</b>", "No", "&mdash;", "&mdash;", "Not available at any offshore casino here."],
      ["Apple Pay / Google Pay", "At some sites", "No", "&mdash;", "As underlying card",
       "A card wrapper. Inherits the same decline behaviour."],
     ], caption="Casino payment methods for New Zealand players, tested %s" % MONTH_YEAR)]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("NZD accounts and why they matter more than the bonus", "nzd"),
         "<p>This is the most under-appreciated variable in choosing a casino, and it is worth more "
         "than most welcome offers.</p>",
         "<p>A casino that holds your balance in euros or US dollars converts every deposit and every "
         "withdrawal. The spread is typically 2&ndash;3% each way at the cashier&rsquo;s rate, which "
         "is not the mid-market rate. Run a year of ordinary play through that &mdash; say NZ$4,000 "
         "deposited and NZ$3,000 withdrawn &mdash; and you have paid roughly NZ$175 for nothing.</p>",
         table(["Casino", "Wallet currency", "NZD bank transfer", "Cost of a NZ$500 in / NZ$1,200 out"], [
      ["Spinjo", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["Kingdom", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["Rooster Bet", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["Fortune Play", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["Smash", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["Rivo", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["Lucky Vibe", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["Lucky7even", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["Lucky Circus", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["MadCasino", "<b>NZD</b>", "Yes", "<b>NZ$0</b>"],
      ["Ivibet", "EUR", "No", "&asymp;NZ$42"],
      ["Hellspin", "EUR", "No", "&asymp;NZ$42"],
      ["Slotsgem", "EUR", "No", "&asymp;NZ$42"],
      ["CrownSlots", "EUR", "No", "&asymp;NZ$42"],
      ["Gunsbet", "EUR", "No", "&asymp;NZ$42"],
      ["Roby Casino", "EUR", "No", "&asymp;NZ$42"],
      ["Spino", "Crypto only", "No", "Exchange fees + volatility"],
     ], caption="Wallet currency and the real cost of one deposit and one withdrawal"),
     note("<b>The workaround if you want a euro site.</b> Use a stablecoin. Deposit USDT, withdraw "
          "USDT, and convert once at a New Zealand exchange where you control the rate. You still pay "
          "an exchange spread, but once rather than twice, and at a better rate than a casino "
          "cashier.", "ok")]
    body.append(section("\n".join(s)))

    s = [h2("Online casino deposit methods NZ players can use", "methods"),
         "<p>Every one of the online casino deposit methods NZ players actually reach for is below, "
         "each funded and &mdash; where the rail allows it &mdash; cashed out from a New Zealand "
         "account this month. They are ordered roughly by how often Kiwis use them.</p>",

         h3("Visa and Mastercard casino NZ deposits", "cards"),
         "<p>The default, and the one most likely to be declined. New Zealand banks can refuse "
         "transactions coded to gambling merchant categories, and several apply that as standing "
         "policy on credit. Debit succeeds far more often than credit. A declined card is your "
         "bank&rsquo;s decision rather than the casino refusing you, and the cashier usually cannot "
         "tell you which it was. A Visa casino NZ deposit credits instantly; the return journey takes "
         "two to five business days after the operator approves it. Mastercard casino NZ behaviour is "
         "identical &mdash; the difference that matters is debit versus credit, not the scheme.</p>",

         h3("NZD bank transfer casinos", "bank-transfer"),
         "<p>The cleanest fiat option available, and the reason a bank transfer casino NZ players can "
         "actually use is worth hunting for. Money moves in New Zealand dollars both ways, so there is "
         "no conversion spread at either end. Deposits normally credit within the hour during banking "
         "hours; a casino withdrawal to a bank account in NZ takes one to three business days once "
         "approved. Ten of the sixteen casinos we list support it.</p>",

         h3("Neosurf casinos NZ", "neosurf"),
         "<p>A prepaid voucher bought for cash at dairies, service stations and supermarkets, redeemed "
         "with a ten-digit code at the cashier. A Neosurf casino NZ deposit is instant and carries no "
         "fee at the operator&rsquo;s end. The real advantage is control: a NZ$50 voucher is a hard "
         "ceiling rather than a good intention, and no gambling transaction appears on your bank "
         "statement. This is the online casino that accepts prepaid card NZ players usually mean. The "
         "drawback is that vouchers cannot pay out.</p>",

         h3("Paysafecard casino NZ deposits", "paysafecard"),
         "<p>The same prepaid model with wider international acceptance and slightly thinner New "
         "Zealand retail distribution. A Paysafecard casino NZ player funds an account with a 16-digit "
         "PIN and passes no card or bank details to the operator at all. Like Neosurf it is "
         "deposit-only, so set up a withdrawal method before you need one rather than while a payout "
         "is waiting.</p>",

         h3("Skrill and Neteller casinos NZ", "ewallets"),
         "<p>A Skrill casino NZ account and a Neteller casino NZ account behave identically: instant "
         "deposits and the fastest non-crypto cashout available, at four to twenty-four hours. Two "
         "costs get missed. The wallet charges you to move money out to a New Zealand bank, and many "
         "operators exclude e-wallet deposits from welcome bonus eligibility &mdash; check that before "
         "you fund if you intend to claim.</p>",

         h3("MiFinity, Jeton and the bank-block workarounds", "mifinity"),
         "<p>MiFinity is the one to know if your bank blocks gambling merchant codes outright, because "
         "it settles through a different rail and its New Zealand coverage has grown steadily. Jeton "
         "is supported at Kingdom and Smash. Both clear in eight to twenty-four hours and both charge "
         "their own fee to reach a New Zealand bank.</p>",

         h3("Apple Pay casino NZ and Google Pay", "apple-pay"),
         "<p>Available at a small number of sites, and worth understanding before you rely on it. An "
         "Apple Pay casino NZ deposit is a card transaction wearing a different coat: it settles "
         "through the card underneath, so it inherits exactly the same decline behaviour. It is faster "
         "to authorise and it is deposit-only. If your Visa is being declined, Apple Pay on that same "
         "Visa will be declined too. Which casinos accept Apple Pay in NZ changes often, so check the "
         "cashier rather than a badge on a landing page. Pay by phone bill is not offered by any "
         "offshore operator serving New Zealand.</p>",

         h3("PayPal casino NZ &mdash; why there are none", "paypal"),
         "<p>Can you use PayPal at online casinos in NZ? No, and any page telling you otherwise is "
         "wrong. There is no PayPal casino NZ players can fund: PayPal does not process gambling "
         "transactions for New Zealand users at any offshore operator we have tested, and has not for "
         "years. It works with licensed operators in a handful of regulated markets, which is where "
         "the confusion comes from. If PayPal is a requirement for you, the honest answer is to wait "
         "and see which operators the New Zealand licensed regime signs.</p>",

         h3("Casinos that accept POLi in NZ &mdash; the current position", "poli"),
         "<p>This is the claim we most often have to correct. POLi Payments is alive and operating in "
         "New Zealand: it was acquired by Merco, it now connects through bank-approved open banking "
         "APIs following the December 2025 rules, and eight banks &mdash; ANZ, ASB, BNZ, Kiwibank, "
         "TSB, Westpac, Bank Direct and The Co-operative Bank &mdash; partner with it for ordinary "
         "retail payments.</p>",
         "<p>What no longer exists is the gambling channel. There are effectively no casinos that "
         "accept POLi in NZ in 2026, and the POLi payments casino NZ listings you still see on "
         "comparison sites are residue from templates written years ago. We re-check this every month "
         "and will rewrite the section the day it changes. Until then, NZD bank transfer is the "
         "closest equivalent.</p>",
         note("<b>Use a POLi listing as a freshness test.</b> If a comparison page still shows POLi "
              "logos on casino cards, it has not been re-checked recently &mdash; which tells you how "
              "much to trust its payout times, bonus terms and licence claims as well.", "warn"),

         h3("Cryptocurrency", "crypto"),
         "<p>The fastest rail in both directions and the one we use for most of our own withdrawal "
         "testing. USDT on the Tron network is the practical recommendation: value pegged to the US "
         "dollar so nothing moves while a withdrawal processes, network fees around NZ$1.50, "
         "confirmation in a couple of minutes, and the widest support across the casinos here. "
         "<a href=\"/crypto-casinos-nz/\">Full detail on crypto casinos, including the tax "
         "position</a>.</p>",
         table(["Coin", "Confirmation", "Network fee", "Volatility while in flight", "Best for"], [
      ["USDT (Tron)", "1&ndash;3 min", "&asymp;NZ$1.50", "None", "<b>Everyone. The default.</b>"],
      ["USDT (Ethereum)", "2&ndash;5 min", "NZ$4&ndash;25", "None", "When Tron is not offered"],
      ["Bitcoin", "10&ndash;60 min", "NZ$2&ndash;15", "Real", "Universal acceptance"],
      ["Litecoin", "3&ndash;10 min", "&asymp;NZ$0.10", "Real", "Cheap transfers"],
      ["Dogecoin", "2&ndash;10 min", "&asymp;NZ$0.20", "High", "Novelty, low fees"],
      ["Solana", "&lt;1 min", "&asymp;NZ$0.02", "Real", "Speed, where supported"],
     ], caption="Crypto rails from a New Zealand perspective")]
    body.append(section("\n".join(s)))

    s = [h2("Casinos that accept NZD, and what the others cost you", "nzd-casinos"),
         "<p>Holding your balance in New Zealand dollars is worth more than most welcome bonuses and "
         "it is the most useful single filter when choosing where to play. Casinos that accept NZD "
         "convert nothing; the rest convert twice, at a rate the cashier sets.</p>",
         table(["Casino", "Wallet currency", "NZD bank transfer", "Min deposit",
                "Cost of NZ$500 in / NZ$1,200 out"], [
      ["Spinjo", "<b>NZD</b>", "Yes", "NZ$30", "<b>NZ$0</b>"],
      ["Kingdom", "<b>NZD</b>", "Yes", "NZ$20", "<b>NZ$0</b>"],
      ["Rooster Bet", "<b>NZD</b>", "Yes", "NZ$25", "<b>NZ$0</b>"],
      ["Fortune Play", "<b>NZD</b>", "Yes", "NZ$25", "<b>NZ$0</b>"],
      ["Smash", "<b>NZD</b>", "Yes", "NZ$20", "<b>NZ$0</b>"],
      ["Rivo", "<b>NZD</b>", "Yes", "NZ$25", "<b>NZ$0</b>"],
      ["Lucky Vibe", "<b>NZD</b>", "Yes", "NZ$25", "<b>NZ$0</b>"],
      ["Lucky7even", "<b>NZD</b>", "Yes", "NZ$20", "<b>NZ$0</b>"],
      ["Lucky Circus", "<b>NZD</b>", "Yes", "<b>NZ$10</b>", "<b>NZ$0</b>"],
      ["MadCasino", "<b>NZD</b>", "Yes", "NZ$20", "<b>NZ$0</b>"],
      ["Ivibet / Hellspin / Slotsgem", "EUR", "No", "NZ$20", "&asymp;NZ$42"],
      ["CrownSlots / Gunsbet / Roby", "EUR", "No", "NZ$30&ndash;35", "&asymp;NZ$42"],
      ["Spino", "Crypto only", "No", "20 USDT", "Exchange fees + volatility"],
     ], caption="Casinos that accept NZD, and the real cost of the ones that do not"),
         "<p>The minimum deposit online casino NZ players face sits at NZ$20 across most of this list, "
         "with Lucky Circus at NZ$10 and the euro-denominated sites asking NZ$30&ndash;35. If you want "
         "NZD deposits with no conversion fee, the first ten rows are the shortlist. Casino deposits "
         "carry no fee at any operator here; the costs are the conversion spread, the blockchain "
         "network fee on crypto and your e-wallet&rsquo;s own charge to reach a New Zealand bank.</p>",
         note("<b>The workaround if you want a euro site anyway.</b> Use a stablecoin. Deposit USDT, "
              "withdraw USDT, and convert once at a New Zealand exchange where you control the rate. "
              "You still pay a spread, but once rather than twice, and at a better rate than a casino "
              "cashier offers.", "ok")]
    body.append(section("\n".join(s), cls="sec--sur"))

    rows = []
    for o in lib.OPS:
        pays = o["payments"]
        def y(x):
            return "Yes" if x in pays else "&mdash;"
        rows.append([o["name"], y("NZD bank transfer"), y("Visa"), y("Neosurf"), y("Skrill"),
                     y("MiFinity"), y("Jeton"), "Yes" if o["crypto"] else "&mdash;", o["min_deposit"]])
    s = [h2("Which casinos support what", "by-casino"),
         table(["Operator", "NZD transfer", "Card", "Neosurf", "Skrill", "MiFinity", "Jeton",
                "Crypto", "Min deposit"], rows,
               caption="Payment support by operator, %s" % MONTH_YEAR),
         h3("Verification, and why it delays your first payout", "kyc"),
         "<p>Every licensed operator must verify your identity before releasing funds. Most do it at "
         "first withdrawal, which is the worst possible moment. Do it the day you register instead.</p>",
         "<p>You will need photo ID (a New Zealand passport or driver licence), proof of address dated "
         "within three months (a rates bill, bank statement or power bill &mdash; a mobile phone bill "
         "is often rejected), and, if you deposited by card, a photo of the card with the middle "
         "digits covered. Median approval across our testing was 14 hours; the worst was four days. "
         "Above roughly NZ$5,000 in withdrawals, expect a source-of-funds request as well.</p>",
         faq(faqs, "Payment questions", "faq"),
         authorbox("priya-raman")]
    body.append(section("\n".join(s), cls="sec--sur"))

    trail = [("Home", "/"), ("Payment methods", path)]
    schema = [lib.article_schema(path, "Casino Payment Methods NZ", "Deposit and withdrawal methods "
                                 "that work from New Zealand.", "priya-raman", "jordan-whitcombe",
                                 "Payments"),
              lib.breadcrumb_schema(path, trail), lib.faq_schema(path, faqs)]
    lib.write(path, lib.seo_title(path),
              "NZ casino deposits and withdrawals tested: NZD bank transfer, Neosurf, Skrill, "
              "MiFinity, crypto. Real speeds, real costs, and why POLi is no longer an option.",
              "\n".join(body), schema, prio=0.8, freq="monthly")

# ===========================================================================
def build_law():
    path = "/licensed-online-casinos/"
    faqs = [
     ("Is online gambling legal in New Zealand?",
      "<p>Playing is legal. It has never been an offence for a person in New Zealand to gamble at an "
      "overseas online casino or with an overseas bookmaker, and the Online Casino Gambling Act 2026 "
      "does not change that. What the Act regulates is <em>supply</em>: from 1 December 2026, a "
      "provider that has not applied for a New Zealand licence must stop conducting online casino "
      "gambling in New Zealand.</p>"),
     ("When does the new licensing regime start?",
      "<p>The Act commenced on 1 May 2026 and the Online Casino Gambling Regulations 2026 commenced "
      "on 3 July 2026. Expressions of interest opened from late July 2026, the auction was scheduled "
      "from September 2026, and full applications from October 2026. Successful applicants have 90 "
      "days from licence grant to go live. The Department of Internal Affairs does not expect the "
      "regime to be fully operational until 2027.</p>"),
     ("How many online casino licences will there be?",
      "<p>Up to 15, and the DIA is not obliged to issue them all. No person with significant "
      "influence &mdash; defined as 20% or more of ownership or voting rights &mdash; may hold more "
      "than three. Licences run for three years with one renewal available for a further five, and "
      "they are personal and non-transferable.</p>"),
     ("What does the Act change for players?",
      "<p>At licensed sites, several things. Credit cards and credit-linked payment methods are "
      "banned. Autoplay and multi-slot play are prohibited. Any request to remove or increase a "
      "deposit limit carries a mandatory 24-hour cooling-off period. Operators must verify age "
      "digitally, with a minimum age of 18, and one account per customer per platform.</p>"),
     ("Do I pay tax on gambling winnings in New Zealand?",
      "<p>Not as a recreational player. Inland Revenue does not treat casual gambling winnings as "
      "assessable income, so there is nothing to declare. The exception is gambling carried on as a "
      "business, which is rare. Note that cryptoassets are treated separately as property, so "
      "converting crypto can have tax consequences even when the gambling itself does not.</p>"),
     ("What happens to my account and my balance on 1 December 2026?",
      "<p>It depends on whether your operator applied for a licence. An operator that did <b>not</b> "
      "apply must cease offering online casino gambling to New Zealanders. An operator that "
      "<b>did</b> apply may keep serving New Zealand players &mdash; though not advertise into New "
      "Zealand &mdash; until its application is decided or until mid-2027. In practice expect a mix of "
      "geo-blocking, closed registrations with withdrawals still honoured, and some operators "
      "continuing and being dealt with by the DIA. Do not hold a large balance offshore through the "
      "transition &mdash; withdraw regularly.</p>"),
     ("Does the Act cover sports betting?",
      "<p>No. The Online Casino Gambling Act 2026 covers online casino gambling. Sports and racing "
      "betting remain under the Racing Industry Act 2020, which gives TAB NZ exclusivity to offer "
      "betting from within New Zealand and imposes offshore betting charges on overseas operators "
      "taking New Zealand bets. Betting with an offshore bookmaker remains legal for you.</p>"),
     ("What are the penalties for operators that breach the Act?",
      "<p>Civil penalties reach $5 million for a body corporate and $300,000 for an individual. "
      "Licensed operators also pay offshore gambling duty &mdash; rising from 12% to 16% of gross "
      "gambling revenue on 1 January 2027, with the extra four percentage points ring-fenced for "
      "community funding &mdash; plus a 1.24% problem gambling levy, and must keep a platform "
      "available for at least 270 days in any 12-month period.</p>"),
     ("Will advertising change?",
      "<p>Substantially, for licensed operators. The regulations prohibit sponsorships, personal "
      "endorsements and affiliate marketing, bar portraying gambling as an investment or a solution "
      "to financial problems, prohibit targeting under-18s, and ban advertising within 30 minutes "
      "before or after a live broadcast. Expect the New Zealand online gambling advertising landscape "
      "to look very different in 2027.</p>"),
    ]

    body = [hero(
      "Written from the legislation, not from summaries",
      lib.seo_h1(path),
      "There are no licensed online casinos NZ players can join yet &mdash; the Department of "
      "Internal Affairs is still running the auction. This page tracks what the Online Casino "
      "Gambling Act 2026 actually says, when legal online casinos NZ side will exist, and what "
      "changes on 1 December 2026. Written from the primary sources, with dates and figures.",
      stats=[("1 May 2026", "Act commenced"), ("Up to 15", "Licences available"),
             ("1 Dec 2026", "Unlicensed cut-off"), ("2027", "Regime fully operational")],
      ctas=[("The timeline", "#timeline"), ("What it means for you", "#for-players")], aqua=True)]

    s = [crumbs([("Home", "/"), ("NZ gambling law", None)]),
         byline("aroha-tainui", "jordan-whitcombe"),
         "<p>New Zealand spent two decades with online gambling laws New Zealand regulators could not "
         "apply to the thing most people actually did. The Gambling Act 2003 prohibited offering "
         "unlicensed gambling from within New Zealand but said almost nothing about offshore online "
         "casinos, which is why hundreds of them have served New Zealanders legally for years while "
         "paying nothing here.</p>",
         "<p>The Online Casino Gambling Act 2026 closes that gap. This page sets out what it does, "
         "with the dates and figures, and separates clearly what applies to operators from what "
         "applies to you.</p>",
         toc([("Are online casinos legal in New Zealand?", "legal-status"),
              ("The position in one table", "summary"),
              ("The Online Casino Gambling Act 2026", "the-act"),
              ("The licensing process and timeline", "timeline"),
              ("What the regulations require", "regulations"),
              ("What it means for players", "for-players"),
              ("Sports betting is a separate regime", "betting"),
              ("Tax on gambling winnings", "tax"),
              ("Greyhound racing closure", "greyhounds"),
              ("The old framework: Gambling Act 2003", "gambling-act"),
              ("Frequently asked questions", "faq")])]
    body.append(section("\n".join(s)))

    s = [h2("Are online casinos legal in New Zealand?", "legal-status"),
         "<p>Short answer: yes for you, and it always has been. Long answer below, because the question "
         "people are really asking in 2026 is not about their own position but about which sites will "
         "still be there next year.</p>",
         table(["The question people ask", "The actual position"], [
      ["Is online gambling legal in NZ for me as a player?",
       "<b>Yes.</b> No New Zealand law has ever made it an offence for a resident to gamble at an "
       "overseas online casino, and none is proposed."],
      ["Are online casinos legal in New Zealand to operate?",
       "Only under a licence, from 2027. The Gambling Act 2003 barred offering unlicensed gambling "
       "from inside New Zealand; the Online Casino Gambling Act 2026 now licenses the offshore supply "
       "side as well."],
      ["Is it legal to gamble online in New Zealand right now, at an offshore site?",
       "<b>Yes.</b> Offshore operators are still serving New Zealand legally from your side of the "
       "transaction during the transition."],
      ["What is the offshore casinos NZ legal status after December?",
       "An operator that did not apply must stop. One that applied may continue, without advertising, "
       "until its application is decided."],
      ["Do I pay tax on casino winnings in NZ?",
       "<b>No</b>, as a recreational player. Gambling is tax free in New Zealand for casual players; "
       "Inland Revenue does not treat casual winnings as income."],
     ], caption="Online gambling laws New Zealand players actually need to know"),
         "<p>That last row is worth expanding, because it is the single most searched question in this "
         "area. Is gambling tax free in New Zealand? For a recreational player, yes &mdash; there is "
         "nothing to declare and nothing to pay, whether you win at a casino, a sportsbook or Lotto. "
         "The exception is a person gambling as a business, which is rare and fact-specific. "
         "Cryptoassets are treated separately as property, so converting crypto back to New Zealand "
         "dollars can have its own consequences even though the gambling does not.</p>",
         h3("Which online casinos are licensed in NZ?", "which-licensed"),
         "<p>None yet, and any page publishing a New Zealand online casino licence list today has "
         "invented it. The Department of Internal Affairs opened expressions of interest in late July "
         "2026 and closed them on 14 August with roughly 50 received; the auction stage was scheduled "
         "for the end of September. Until the DIA announces outcomes there are no DIA licensed online "
         "casino brands to name.</p>",
         "<p>When they exist, the NZ online casino licence holders list will be published by the DIA "
         "and we will mirror it here with launch dates. Regulated online casinos in New Zealand will "
         "be identifiable by a New Zealand licence number in the footer, and by what they are no "
         "longer allowed to do: no credit cards, no autoplay, no advertising within 30 minutes of a "
         "live broadcast, and a mandatory 24-hour wait on any deposit-limit increase.</p>",
         note("<b>How many online casino licences will NZ issue?</b> Up to 15, and the DIA is not "
              "obliged to issue them all. No operator with significant influence &mdash; 20% or more "
              "of ownership or voting rights &mdash; may hold more than three. When do online casinos "
              "become legal in NZ in the licensed sense? The first licences are expected around the "
              "turn of the year, with a legal online casino NZ 2027 market fully operational during "
              "that year rather than at a single switch-on date.", "info")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("The position in one table", "summary"),
         keyfacts([("Act commenced", "1 May 2026"), ("Regulations commenced", "3 July 2026"),
                   ("Regulator", "Dept of Internal Affairs"), ("Licences available", "Up to 15"),
                   ("Max per operator", "3"), ("Licence term", "3 years + 5 renewal"),
                   ("EOI fee", "$19,000 + GST"), ("Auction format", "Multi-round ascending"),
                   ("Time to launch", "90 days from grant"), ("Min platform availability", "270 days / year"),
                   ("Offshore duty", "12% &rarr; 16% on 1 Jan 2027"),
                   ("Problem gambling levy", "1.24% of profits"),
                   ("Minimum age", "18"), ("Credit cards", "Banned at licensed sites"),
                   ("Unlicensed cut-off", "1 December 2026"), ("Fully operational", "Expected 2027")]),
         note("<b>Player position, stated plainly.</b> It is legal for you to gamble online at an "
              "overseas casino from New Zealand today, and nothing in this Act makes it illegal for "
              "you. The obligations and the penalties fall on operators. What will change for you is "
              "<em>which</em> operators you can reach.", "ok")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("The Online Casino Gambling Act 2026 and the NZ online casino licence", "the-act"),
         "<p>The Act commenced on 1 May 2026 and creates New Zealand&rsquo;s first licensing regime "
         "for online casino gambling, administered by the Department of Internal Affairs. Its core "
         "features:</p>",
         "<ul>"
         "<li><b>A capped licence pool.</b> Up to 15 licences. The DIA is not required to issue all "
         "15 and has indicated it will issue only as many as meet the standard.</li>"
         "<li><b>A concentration limit.</b> No person with significant influence &mdash; 20% or more "
         "of ownership or voting rights &mdash; may hold more than three licences.</li>"
         "<li><b>A three-year term</b>, with one renewal for a further five years. Licences are "
         "personal and non-transferable, so a licence cannot be sold with a business.</li>"
         "<li><b>An auction mechanism.</b> Licences are allocated by multi-round ascending auction "
         "conducted through the Government Electronic Tenders Service, following an expression of "
         "interest stage.</li>"
         "<li><b>Financial obligations.</b> Offshore gambling duty rises from <b>12% to 16%</b> of "
         "gross gambling revenue on <b>1 January 2027</b>, with the additional four percentage points "
         "ring-fenced for community funding, plus a <b>1.24%</b> problem gambling levy on operator "
         "profits that funds harm-minimisation services. A separate DIA regulatory levy recovers the "
         "cost of running the regime; published sources differ on its rate, so we have not quoted a "
         "figure we cannot verify.</li>"
         "<li><b>Enforcement.</b> Civil penalties of up to $5 million for a body corporate and "
         "$300,000 for an individual.</li>"
         "<li><b>The continuation rule.</b> An operator that <em>applies</em> for a licence before "
         "1 December 2026 may keep serving New Zealand players &mdash; though not advertise into New "
         "Zealand &mdash; until its application is decided or until mid-2027, whichever is earlier. "
         "Published sources differ on whether that backstop is 1 June or 1 July 2027. Only operators "
         "that do not apply at all must stop on 1 December.</li>"
         "<li><b>Operating obligations.</b> A licensed platform must go live within 90 days of grant "
         "and must be available for at least 270 days in any 12-month period.</li></ul>"]
    body.append(section("\n".join(s)))

    s = [h2("The licensing process and timeline", "timeline"),
         timeline([
      ("1 May 2026", "Act commences", "The Online Casino Gambling Act 2026 comes into force, "
       "establishing the regime and the DIA&rsquo;s role as regulator.", "done"),
      ("3 July 2026", "Regulations commence", "The Online Casino Gambling Regulations 2026 take "
       "effect, adding the operational detail on harm minimisation, consumer protection, advertising "
       "and operator obligations.", "done"),
      ("Late July 2026", "Stage one &mdash; expressions of interest",
       "Applicants pay a $19,000 (excluding GST) EOI fee and submit detail on themselves, their key "
       "officers, ownership structure, platform, branding and available capital.", "done"),
      ("September 2026", "Stage two &mdash; auction",
       "A multi-round ascending auction run through GETS allocates the licences among qualified "
       "applicants.", "next"),
      ("October 2026", "Stage three &mdash; full applications",
       "Successful bidders pay the auction price and submit full licence applications for assessment "
       "by the DIA.", ""),
      ("1 December 2026", "Unlicensed operators must cease",
       "Providers that have not applied for a licence must stop conducting online casino gambling in "
       "New Zealand. This is the date that matters for players.", ""),
      ("From late 2026", "Licensed platforms go live",
       "Licensees have 90 days from grant to launch a compliant platform. The first licensed New "
       "Zealand online casinos are expected around the turn of the year.", ""),
      ("2027", "Regime fully operational",
       "The DIA does not expect the full licensed regime to be operational before 2027.", ""),
     ]),
     note("<b>Why this timeline is unusually uncertain.</b> An auction with a capped pool means "
          "nobody &mdash; including the operators &mdash; knows in advance who will be serving New "
          "Zealand in 2027. A brand with a modest New Zealand book has a genuine commercial question "
          "about whether to pay a $19,000 EOI fee plus an auction price for one of fifteen licences. "
          "Some will exit rather than bid.", "warn")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("What the regulations require", "regulations"),
         "<p>The Online Casino Gambling Regulations 2026, in force from 3 July 2026, contain the "
         "provisions players will actually notice at licensed sites.</p>",
         table(["Area", "Requirement", "Effect on players"], [
      ["Age", "Minimum 18, with robust digital identity verification",
       "Verification at registration rather than at first withdrawal"],
      ["Credit", "Credit cards and credit-linked payment methods banned",
       "You will not be able to fund a licensed NZ account with credit"],
      ["Limits", "Mandatory 24-hour cooling-off before a deposit limit is removed or increased",
       "You can tighten a limit instantly; loosening it takes a day"],
      ["Autoplay", "Autoplay and multi-slot play prohibited",
       "Each spin requires an action; no running several games at once"],
      ["Accounts", "One account per customer per platform",
       "Duplicate accounts are a regulatory breach, not just a terms breach"],
      ["Advertising", "No sponsorships, personal endorsements or affiliate marketing; no "
       "advertising within 30 minutes either side of a live broadcast",
       "Far less gambling advertising around New Zealand sport"],
      ["Framing", "Gambling may not be portrayed as an investment or a solution to financial problems",
       "An end to &lsquo;make money&rsquo; marketing at licensed operators"],
      ["Under-18s", "No targeting of under-18s in any advertising", "Content and placement restrictions"],
     ], caption="Key provisions of the Online Casino Gambling Regulations 2026"),
     note("<b>A disclosure about this site.</b> The regulations restrict affiliate marketing as a "
          "form of advertising by <em>licensed</em> operators. %s is an affiliate publisher. When the "
          "licensed regime is operational we expect the way New Zealand-licensed operators may work "
          "with sites like this one to change materially, and we will say so on this page when the "
          "position is settled. We would rather tell you that now than have you discover it "
          "later." % NAME, "info")]
    body.append(section("\n".join(s)))

    s = [h2("What it means for players", "for-players"),
         cards([
      ("01", "Playing offshore is still legal", "Nothing in the Act makes it an offence for a New "
       "Zealander to gamble at an overseas site. The obligations fall on operators.", None),
      ("02", "Your choice of operator will narrow", "Up to 15 licensed operators, against hundreds "
       "currently accepting New Zealand registrations.", None),
      ("03", "Licensed sites will be safer and more restricted", "Digital age verification, no credit "
       "cards, no autoplay, cooling-off on limit increases &mdash; real protections with real friction.",
       "/responsible-gambling/", "Responsible gambling"),
      ("04", "Withdraw regularly through the transition", "Do not accumulate a large balance offshore "
       "between now and December. An operator exiting New Zealand is not a disaster if your money is "
       "already in your bank account.", "/fast-payout-casinos/", "Fastest payouts"),
      ("05", "Complete KYC now", "Verification takes a median of 14 hours. Doing it before December "
       "removes a delay at exactly the wrong moment.", "/casino-payment-methods/", "Verification detail"),
      ("06", "Sports betting is unaffected", "The Act covers casino only. TAB NZ&rsquo;s domestic "
       "exclusivity and your right to bet offshore are unchanged.", "/online-betting/", "Online betting"),
     ])]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Sports betting is a separate regime", "betting"),
         "<p>This causes constant confusion, so to be explicit: the Online Casino Gambling Act 2026 "
         "does not cover sports or racing betting. Those sit under the <b>Racing Industry Act 2020</b>, "
         "which gives TAB NZ the exclusive right to offer betting from within New Zealand and which "
         "introduced offshore betting charges &mdash; a consumption charge and a betting information "
         "use charge &mdash; payable by overseas bookmakers taking bets from New Zealand residents.</p>",
         "<p>TAB NZ&rsquo;s commercial operations have been run in partnership with Entain since 2023 "
         "under a long-term arrangement. None of that changes in December 2026. A casino brand that "
         "loses access to New Zealand under the casino Act may still be able to offer you a "
         "sportsbook. <a href=\"/online-betting/\">Our online betting guide</a> covers this in "
         "detail.</p>",
         h3("Tax on gambling winnings", "tax"),
         "<p>New Zealand does not tax recreational gambling winnings. Inland Revenue does not treat "
         "casual winnings as assessable income, so there is nothing to declare and nothing to pay, "
         "whether you win at a casino, a sportsbook or the TAB.</p>",
         "<p>Two qualifications. First, a person whose gambling constitutes a business &mdash; "
         "systematic, organised, with an expectation of profit &mdash; can have winnings treated as "
         "income. This is rare and fact-specific. Second, cryptoassets are treated as property by "
         "Inland Revenue: disposing of crypto, including converting it back to New Zealand dollars, "
         "can create a taxable gain or loss independently of the gambling. Keep records.</p>",
         h3("Greyhound racing closure", "greyhounds"),
         "<p>Commercial greyhound racing in New Zealand ended on <b>1 August 2026</b>. The Racing "
         "Industry (Closure of Greyhound Racing Industry) Amendment passed its third reading 112 votes "
         "to 11, following a twenty-month wind-down announced in December 2024. Independent reviews in "
         "2013, 2017 and 2021 had found persistent animal welfare problems, with more than 2,500 "
         "injuries and 262 deaths recorded between 2021 and mid-2024.</p>",
         "<p>New Zealand greyhound markets no longer exist at any bookmaker. Australian, British and "
         "Irish greyhound racing is unaffected and remains available. New Zealand thoroughbred and "
         "harness racing continue.</p>"]
    body.append(section("\n".join(s)))

    s = [h2("The old framework: Gambling Act 2003", "gambling-act"),
         "<p>The Gambling Act 2003 remains in force for everything the 2026 Act does not cover: "
         "class 4 gaming machines in pubs and clubs, Lotto NZ, casino venues, and community gambling. "
         "Its key features, for context:</p>",
         "<ul>"
         "<li><b>Remote interactive gambling</b> offered from within New Zealand was prohibited except "
         "by Lotto NZ and TAB NZ. Gambling offered from overseas was outside its reach, which is the "
         "gap the 2026 Act fills.</li>"
         "<li><b>Class 4 gaming machines</b> &mdash; pub and club pokies &mdash; operate under "
         "prescribed minimum return-to-player rules, with a substantial share of turnover directed to "
         "community funding, duty and venue costs. This is why online pokies at 94&ndash;97% return "
         "and pub pokies at around 78% are very different products.</li>"
         "<li><b>Land-based casinos</b> operate under a closed set of venue licences with a minimum "
         "entry age of 20, against 18 for online gambling under the new Act.</li>"
         "<li><b>Harm minimisation</b> obligations, including multi-venue exclusion, run through the "
         "Act and are administered by the DIA with the Ministry of Health funding treatment "
         "services.</li></ul>",
         faq(faqs, "New Zealand gambling law &mdash; frequently asked questions", "faq"),
         authorbox("aroha-tainui"),
         note("<b>This page is information, not legal advice.</b> It was written from the Online "
              "Casino Gambling Act 2026, the Online Casino Gambling Regulations 2026, the Racing "
              "Industry Act 2020, the Gambling Act 2003 and Department of Internal Affairs guidance. "
              "If you need advice about your own position, consult a New Zealand lawyer. If you spot "
              "an error, email <a href=\"mailto:%s\">%s</a> and we will correct it." % (EMAIL, EMAIL),
              "info")]
    body.append(section("\n".join(s), cls="sec--sur"))

    trail = [("Home", "/"), ("NZ gambling law", path)]
    schema = [lib.article_schema(path, "New Zealand Gambling Law", "The Online Casino Gambling Act "
                                 "2026 explained.", "aroha-tainui", "jordan-whitcombe", "Regulation"),
              lib.breadcrumb_schema(path, trail), lib.faq_schema(path, faqs)]
    lib.write(path, lib.seo_title(path),
              "The Online Casino Gambling Act 2026 explained: licensing timeline, the 1 December 2026 "
              "cut-off, what changes for players, tax, and how sports betting differs.",
              "\n".join(body), schema, prio=0.85, freq="weekly")


# ===========================================================================
def build_rg():
    path = "/responsible-gambling/"
    faqs = [
     ("Where can I get free help for gambling harm in New Zealand?",
      "<p>The Gambling Helpline is free, confidential and available 24 hours a day on "
      "<a href=\"tel:0800654655\">0800 654 655</a>, or free text 8006. The Problem Gambling "
      "Foundation offers free face-to-face and online counselling nationwide, including for family "
      "and wh&#257;nau. Salvation Army Oasis and Mapu Maia (for Pasifika communities) also provide "
      "free services. None of these costs anything and none requires a referral.</p>"),
     ("How do I self-exclude from an online casino?",
      "<p>Every operator on this site offers self-exclusion in account settings, usually under "
      "&lsquo;responsible gambling&rsquo; or &lsquo;account limits&rsquo;. You choose a period &mdash; "
      "commonly 6 months, 1 year, 5 years or permanent &mdash; and the account is closed to you for "
      "that time and cannot be reopened early. Do it from account settings rather than by emailing "
      "support, which is slower and sometimes resisted.</p>"),
     ("Can I block gambling sites on my devices?",
      "<p>Yes. BetBlocker is free, works on Windows, Mac, Android and iOS, and blocks tens of "
      "thousands of gambling sites at the device level. Gamban is paid and harder to remove. Both "
      "work in New Zealand. Install on every device, including the one you think you would not use.</p>"),
     ("Can my bank block gambling transactions?",
      "<p>Yes, and it is one of the more effective steps available. ANZ, ASB, BNZ, Kiwibank and "
      "Westpac all offer card-level gambling blocks on request, and some can be toggled in the "
      "banking app. A block that takes 48 hours to lift is a genuine circuit breaker.</p>"),
     ("What is multi-venue exclusion?",
      "<p>A New Zealand mechanism under the Gambling Act 2003 that lets you exclude yourself from "
      "multiple pub and club gaming venues in an area with a single request, rather than venue by "
      "venue. It is administered through the Department of Internal Affairs and gambling harm "
      "services can help you arrange it. It applies to land-based venues, not offshore online "
      "sites.</p>"),
     ("How do I know if my gambling is a problem?",
      "<p>The reliable signals are behavioural rather than financial. Gambling more than you planned. "
      "Chasing losses. Hiding it, or lying about how much. Borrowing to gamble, or gambling with money "
      "meant for something else. Feeling irritable when you try to stop. Gambling to escape rather "
      "than for entertainment. Any one of these is worth a free, anonymous conversation with the "
      "Helpline &mdash; you do not have to be in crisis to call.</p>"),
     ("Can I get money back that I lost while self-excluded?",
      "<p>Sometimes, if the operator let you play after you had self-excluded with them. Licensed "
      "operators have obligations to honour exclusions and a breach is grounds for complaint to their "
      "regulator. Contact the operator in writing first, then escalate to the licensing authority. "
      "We can point you to the right regulator &mdash; email "
      "<a href=\"mailto:%s\">%s</a>.</p>" % (EMAIL_COMPLAINTS, EMAIL_COMPLAINTS)),
     ("What support is there for family and wh&#257;nau?",
      "<p>Substantial, and it is free and separate from the gambler&rsquo;s own treatment. The "
      "Problem Gambling Foundation, Salvation Army Oasis and Mapu Maia all provide counselling "
      "specifically for family members, and the Gambling Helpline takes calls from people worried "
      "about someone else. You do not need the person who is gambling to agree, or even to know.</p>"),
    ]

    body = [hero(
      "Free, confidential help &middot; 0800 654 655",
      lib.seo_h1(path),
      "Gambling is entertainment with a negative expected return. That is the honest description, and "
      "everything on this page follows from it. Here are the tools that limit exposure, the signals "
      "worth taking seriously, and where to get free help in New Zealand &mdash; for yourself or for "
      "someone else.",
      stats=[("0800 654 655", "Gambling Helpline, 24/7"), ("8006", "Free text"),
             ("Free", "All NZ support services"), ("18+", "Minimum age online")],
      ctas=[("Get help now", "#help"), ("Self-exclusion", "#exclude")], aqua=True)]

    s = [crumbs([("Home", "/"), ("Responsible gambling", None)]),
         byline("aroha-tainui", "jordan-whitcombe"),
         note("<b>If you need help right now.</b> Gambling Helpline Aotearoa, free and confidential, "
              "24 hours: <a href=\"tel:0800654655\"><b>0800 654 655</b></a>. Free text <b>8006</b>. "
              "Web chat at <a href=\"https://www.gamblinghelpline.co.nz/\" rel=\"noopener nofollow\" "
              "target=\"_blank\">gamblinghelpline.co.nz</a>. You do not need to be in crisis and you "
              "do not have to give your name.", "no"),
         "<p>This site exists because people gamble online, and we would rather they did it with "
         "accurate information than without. That obliges us to be equally accurate about the other "
         "side: every operator listed here makes money because players lose more than they win, over "
         "time and in aggregate. That is not a criticism of the operators. It is the product.</p>",
         toc([("Where to get help in New Zealand", "help"),
              ("The tools that actually work", "tools"),
              ("Setting limits before you need them", "limits"),
              ("Self-exclusion", "exclude"),
              ("Blocking software and bank blocks", "blocking"),
              ("Warning signs", "signs"),
              ("Myths worth discarding", "myths"),
              ("Support for family and wh&#257;nau", "family"),
              ("What the 2026 regulations require", "regulations"),
              ("Frequently asked questions", "faq")])]
    body.append(section("\n".join(s)))

    s = [h2("Where to get help in New Zealand", "help"),
         "<p>Every service below is free and confidential. None requires a doctor&rsquo;s referral. "
         "All of them take calls from family members as well as from gamblers.</p>",
         table(["Service", "Contact", "What they offer"], [
      ["<b>Gambling Helpline Aotearoa</b>", "<a href=\"tel:0800654655\">0800 654 655</a> &middot; "
       "free text 8006 &middot; <a href=\"https://www.gamblinghelpline.co.nz/\" rel=\"noopener nofollow\" "
       "target=\"_blank\">gamblinghelpline.co.nz</a>",
       "24/7 phone, text and web chat. Immediate support, brief intervention and referral. Also "
       "operates M&#257;ori, Pasifika and youth lines."],
      ["<b>Problem Gambling Foundation</b>", "<a href=\"https://www.pgf.nz/\" rel=\"noopener nofollow\" "
       "target=\"_blank\">pgf.nz</a> &middot; 0800 664 262",
       "Free face-to-face and online counselling nationwide, for gamblers and for family and "
       "wh&#257;nau. No cost, no referral."],
      ["<b>Salvation Army Oasis</b>", "<a href=\"https://www.salvationarmy.org.nz/oasis\" "
       "rel=\"noopener nofollow\" target=\"_blank\">salvationarmy.org.nz/oasis</a>",
       "Free counselling and support across New Zealand, including financial mentoring alongside "
       "gambling treatment."],
      ["<b>Mapu Maia</b>", "<a href=\"https://mapumaia.nz/\" rel=\"noopener nofollow\" "
       "target=\"_blank\">mapumaia.nz</a> &middot; 0800 21 21 22",
       "Free Pasifika-led gambling harm services for individuals, families and communities."],
      ["<b>Gamblers Anonymous NZ</b>", "<a href=\"https://gaaustralia.org.au/new-zealand/\" "
       "rel=\"noopener nofollow\" target=\"_blank\">Meetings list</a>",
       "Peer support meetings in the main centres and online."],
      ["<b>Safer Gambling Aotearoa</b>", "<a href=\"https://safergambling.org.nz/\" "
       "rel=\"noopener nofollow\" target=\"_blank\">safergambling.org.nz</a>",
       "Self-assessment tools, information and links to local services."],
      ["<b>Need to Talk</b>", "Call or text <b>1737</b>",
       "Free 24/7 mental health and addiction support line. Useful when gambling sits alongside "
       "anxiety, depression or alcohol."],
     ], caption="Free gambling harm services in New Zealand")]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("The tools that actually work", "tools"),
         "<p>Ranked roughly by how hard they are to undo, which is the only measure that matters at "
         "the moment you want to undo them.</p>",
         table(["Tool", "Where", "How hard to reverse", "Effectiveness"], [
      ["Bank gambling block", "Your banking app or by phone", "<b>24&ndash;48 hours in most banks</b>",
       "<b>High</b> &mdash; stops the money at source across every site"],
      ["Device blocking software", "BetBlocker (free) or Gamban (paid)", "Deliberately difficult",
       "<b>High</b> &mdash; but install it on every device"],
      ["Operator self-exclusion", "Account settings at each casino", "Cannot be lifted early",
       "High for that site; does nothing about the next one"],
      ["Deposit limit", "Account settings", "24-hour cooling-off at licensed sites",
       "Moderate &mdash; the single best habit to start with"],
      ["Loss limit", "Account settings where offered", "Same cooling-off",
       "Moderate, and more honest than a deposit limit"],
      ["Session time limit", "Account settings", "Immediate", "Low alone, useful combined"],
      ["Reality check pop-ups", "Account settings", "Immediate", "Low &mdash; easy to ignore"],
      ["Multi-venue exclusion", "Via DIA or a harm service", "Formal process",
       "High for land-based venues; does not cover online"],
     ], caption="Harm-reduction tools available to New Zealanders"),
     note("<b>The most effective single step.</b> A bank-level gambling block, because it works "
          "across every site at once and takes a day or two to lift. Operator self-exclusion is "
          "valuable but it is site-by-site, and the next casino is one search away.", "ok")]
    body.append(section("\n".join(s)))

    s = [h2("Setting limits before you need them", "limits"),
         "<p>A limit set on the day you register is a decision made by a person who has not yet won "
         "or lost anything. A limit set after a bad night is a negotiation with yourself. Set them "
         "first.</p>",
         steps([
      ("Decide the number away from the site",
       "What could you lose this month without it affecting anything &mdash; not your rent, not your "
       "savings, not your mood on Wednesday? That is the number."),
      ("Set a monthly deposit limit to that figure",
       "Account settings, under responsible gambling or account limits. Every operator here supports "
       "daily, weekly and monthly."),
      ("Set a session time limit as well",
       "Most harm happens in long sessions, not large single bets. Ninety minutes is a reasonable "
       "default."),
      ("Turn on reality checks",
       "An hourly pop-up showing elapsed time and net position. Easy to dismiss, but it interrupts "
       "the trance."),
      ("Never increase a limit on the day you want to",
       "At licensed New Zealand operators from 2027 a 24-hour cooling-off will be mandatory. Apply "
       "that rule to yourself now, offshore, where it is not."),
      ("Review the numbers every three months",
       "Down is fine. Up should require the same thought as the original decision."),
     ]),
     h3("Self-exclusion", "exclude"),
     "<p>Self-exclusion closes your account for a fixed period and cannot be reversed early. It is "
     "the right tool when limits have stopped working.</p>",
     "<ul>"
     "<li><b>Do it from account settings</b>, under responsible gambling. It is faster than emailing "
     "support and it does not involve a retention conversation.</li>"
     "<li><b>Choose the longest period you are willing to choose.</b> Six months is the usual minimum; "
     "permanent is available everywhere.</li>"
     "<li><b>Withdraw your balance first</b> &mdash; some operators return it automatically, others "
     "make you ask, and asking after exclusion is more difficult.</li>"
     "<li><b>Exclude everywhere at once.</b> Excluding from one site and opening an account at "
     "another is the most common failure pattern, which is why a bank block or blocking software "
     "should go alongside it.</li>"
     "<li><b>Expect marketing to stop.</b> If a site you have excluded from keeps emailing you, that "
     "is a breach and grounds for complaint to its regulator.</li></ul>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Blocking software and bank blocks", "blocking"),
         table(["Tool", "Cost", "Platforms", "Notes"], [
      ["BetBlocker", "<b>Free</b>", "Windows, Mac, Android, iOS",
       "Registered charity. Blocks tens of thousands of gambling sites. Can be set for a fixed period "
       "that cannot be shortened."],
      ["Gamban", "Paid subscription", "Windows, Mac, Android, iOS",
       "Harder to remove than BetBlocker. Often funded free through treatment services &mdash; ask."],
      ["Bank gambling block", "Free", "Card level, all NZ major banks",
       "ANZ, ASB, BNZ, Kiwibank and Westpac. Ask in-app or by phone. Usually a 48-hour delay to lift."],
      ["Router-level DNS filtering", "Free options exist", "Whole household",
       "Blocks on the home network. Does not cover mobile data."],
     ], caption="Blocking tools that work in New Zealand"),
     h3("Warning signs", "signs"),
     "<p>These are the behavioural patterns that gambling harm services see most often. They are "
     "written as statements rather than questions because that is how they usually present.</p>",
     pros_cons(
      ["You gamble for entertainment and stop when the session budget is gone",
       "You know roughly what you are up or down over a year, because you track it",
       "You never gamble with money that is committed to something else",
       "You would be comfortable telling anyone in your life exactly how much you gamble",
       "A limit or a block feels sensible rather than threatening"],
      ["You deposit more than you planned, most times you play",
       "You gamble to win back what you lost &mdash; and the amounts escalate",
       "You hide it, delete history, or understate the figures when asked",
       "You have borrowed, used credit, or dipped into money meant for bills",
       "You feel irritable or restless when you try to cut down",
       "You gamble to escape stress, boredom, grief or conflict rather than for fun",
       "You have missed work, study or family commitments because of it"],
      "Signs things are in proportion", "Signs worth acting on"),
     note("<b>One of those on the right is enough.</b> You do not need to tick several, and you do "
          "not need to be in crisis to call <a href=\"tel:0800654655\">0800 654 655</a>. It is free, "
          "it is confidential, and a first call is usually a conversation rather than a "
          "commitment.", "no")]
    body.append(section("\n".join(s)))

    s = [h2("Myths worth discarding", "myths"),
         table(["The belief", "Why it is wrong"], [
      ["&ldquo;I&rsquo;m due a win.&rdquo;",
       "Every spin and every hand is independent. A pokie has no memory of the last two hundred "
       "spins and no obligation to correct."],
      ["&ldquo;This machine is hot / cold.&rdquo;",
       "Outcomes come from a certified random number generator. Streaks are how randomness looks, "
       "not evidence of a pattern."],
      ["&ldquo;I can win it back.&rdquo;",
       "Chasing increases stake size at the exact moment judgement is worst. It is the single "
       "strongest predictor of serious harm."],
      ["&ldquo;A system beats roulette.&rdquo;",
       "No staking system changes the house edge. Martingale converts many small wins into one "
       "catastrophic loss and requires an infinite bankroll to work."],
      ["&ldquo;I&rsquo;m good at this.&rdquo;",
       "Skill exists in poker and, marginally, in sports betting. It does not exist in pokies, "
       "roulette or crash games. Confusing the two is expensive."],
      ["&ldquo;A bigger bonus means better odds.&rdquo;",
       "A bonus is a turnover contract. A 40x requirement typically costs more in expected losses "
       "than the bonus is worth."],
      ["&ldquo;I&rsquo;m ahead overall.&rdquo;",
       "Most people who believe this have not counted. Track every deposit and withdrawal for a "
       "month and the question settles itself."],
     ], caption="Common beliefs and what is actually true"),
     h3("Support for family and wh&#257;nau", "family"),
     "<p>Gambling harm is rarely contained to the person gambling. Every service listed on this page "
     "provides free support to family members, and you do not need the person who is gambling to "
     "agree or to know.</p>",
     "<ul>"
     "<li><b>You can call the Helpline yourself.</b> 0800 654 655 takes calls from people worried "
     "about someone else, and the conversation is about you as much as them.</li>"
     "<li><b>Protect the household finances first.</b> Separate accounts, remove joint access to "
     "credit, and speak to the bank &mdash; New Zealand banks deal with this regularly and "
     "sympathetically.</li>"
     "<li><b>Financial mentoring is free.</b> MoneyTalks on 0800 345 123 offers free, confidential "
     "budgeting support, and Salvation Army Oasis combines it with gambling counselling.</li>"
     "<li><b>Do not cover the debts silently.</b> Services consistently advise that repaying gambling "
     "debts without conditions tends to extend the problem.</li>"
     "<li><b>Look after yourself.</b> Counselling for family members is free and is not contingent on "
     "the gambler seeking help.</li></ul>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("What the 2026 regulations require", "regulations"),
         "<p>The Online Casino Gambling Regulations 2026 impose harm-minimisation obligations on "
         "operators licensed in New Zealand. These are real improvements and they are worth knowing "
         "about, because they will not apply at the offshore sites you can use today.</p>",
         "<ul>"
         "<li><b>Credit cards and credit-linked payment methods banned.</b> Removing the single most "
         "harmful funding route.</li>"
         "<li><b>Mandatory 24-hour cooling-off</b> before a deposit limit can be removed or "
         "increased. Tightening a limit stays instant.</li>"
         "<li><b>Autoplay and multi-slot play prohibited.</b> Both are associated with dissociative "
         "play and loss of time awareness.</li>"
         "<li><b>One account per customer per platform</b>, with robust digital age verification and "
         "a minimum age of 18.</li>"
         "<li><b>Advertising restrictions</b>, including no sponsorships, no personal endorsements, "
         "no affiliate marketing, no portrayal of gambling as an investment or a solution to "
         "financial problems, and nothing within 30 minutes either side of a live broadcast.</li>"
         "</ul>",
         "<p>Until licensed platforms are operating &mdash; not expected before 2027 &mdash; none of "
         "this protects you at an offshore site. The tools on this page do. "
         "<a href=\"/licensed-online-casinos/\">Full detail on the Act and the timeline</a>.</p>",
         faq(faqs, "Responsible gambling &mdash; frequently asked questions", "faq"),
         authorbox("aroha-tainui"),
         note("<b>Gambling Helpline Aotearoa: <a href=\"tel:0800654655\">0800 654 655</a>, free, "
              "confidential, 24 hours. Free text 8006.</b> If you are worried about your gambling or "
              "someone else&rsquo;s, that call is the shortest route to help and it costs "
              "nothing.", "no")]
    body.append(section("\n".join(s)))

    trail = [("Home", "/"), ("Responsible gambling", path)]
    schema = [lib.article_schema(path, "Responsible Gambling", "Free help and harm-reduction tools "
                                 "for New Zealanders.", "aroha-tainui", "jordan-whitcombe",
                                 "Responsible gambling"),
              lib.breadcrumb_schema(path, trail), lib.faq_schema(path, faqs)]
    lib.write(path, lib.seo_title(path),
              "Free, confidential gambling help in New Zealand: Gambling Helpline 0800 654 655, "
              "self-exclusion, bank blocks, blocking software and support for family and wh&#257;nau.",
              "\n".join(body), schema, prio=0.75, freq="monthly")


def build():
    build_methodology()
    build_payments()
    build_law()
    build_rg()
