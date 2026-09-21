# -*- coding: utf-8 -*-
"""Company and legal pages: about, contact, authors, terms, privacy, cookies."""
import lib
from lib import (MONTH_YEAR, MONTH, YEAR, NAME, LEGAL, DOMAIN, SITE, EMAIL,
                 EMAIL_SUPPORT, EMAIL_COMPLAINTS, EMAIL_PRIVACY, POSTAL, NZBN,
                 FOUNDED, N_WITHDRAWALS, N_OPERATORS_TESTED, N_HOURS,
                 AUTHORS, AUTHOR_ORDER, table, faq, keyfacts, note, toc, steps,
                 cards, ctaband, authorbox, byline, hero, section, h2, h3,
                 pros_cons, crumbs, timeline)

LEGAL_UPDATED = "20 September 2026"


# ===========================================================================
def build_about():
    path = "/about/"
    faqs = [
     ("Who owns %s?" % NAME,
      "<p>%s is published by %s, a New Zealand registered company (NZBN %s). It is independently "
      "owned and is not part of an operator group, a casino network or an operator-owned media "
      "business. No gambling operator holds any equity in the company.</p>" % (NAME, LEGAL, NZBN)),
     ("How do you make money?",
      "<p>Revenue share from operators when a reader opens an account through one of our links. "
      "There is no display advertising and no paid placement. The commercial arrangement is "
      "disclosed at the top of every page that contains such a link, and our "
      "<a href=\"/how-we-rate-casinos/\">methodology page</a> sets out the controls that keep it away from "
      "the rankings.</p>"),
     ("Are your reviewers real people?",
      "<p>Yes. Five named editors, each with a declared beat, a published biography and a profile "
      "page: <a href=\"/authors/\">our authors</a>. Every content page names the writer and a "
      "separate fact-checker. We do not publish under house bylines or invented personas.</p>"),
     ("Do you accept guest posts or paid links?",
      "<p>No. We do not accept guest contributions, sponsored posts, paid links or link insertions, "
      "and we do not respond to outreach offering them. Every page on this site is written by a named "
      "member of the editorial team.</p>"),
     ("Can an operator pay to be listed or removed?",
      "<p>No to both. Listing follows from testing and scoring. An operator that meets the standard "
      "is listed at the position its score produces; one that fails a disqualifying test is not "
      "listed at any price. We have declined both kinds of request.</p>"),
     ("How can I contact the editorial team?",
      "<p>Email <a href=\"mailto:%s\">%s</a> for anything editorial, including corrections. Use "
      "<a href=\"mailto:%s\">%s</a> for operator complaints and "
      "<a href=\"/contact/\">our contact page</a> for everything else.</p>"
      % (EMAIL, EMAIL, EMAIL_COMPLAINTS, EMAIL_COMPLAINTS)),
    ]

    body = [hero(
      "Independent since %s" % FOUNDED,
      lib.seo_h1(path),
      "We are a small New Zealand editorial team that tests online casinos and sportsbooks the "
      "tedious way: real accounts, real deposits, real withdrawals, timed to the minute. This page "
      "explains who we are, how we work, how we are paid, and what we will not do.",
      stats=[("%d" % N_OPERATORS_TESTED, "Operators tested"),
             ("%d" % N_WITHDRAWALS, "Withdrawals timed"),
             ("5", "Named editors"), ("%s" % N_HOURS, "Hours of testing")],
      ctas=[("Meet the team", "/authors/"), ("Our methodology", "/how-we-rate-casinos/")], aqua=True)]

    s = [crumbs([("Home", "/"), ("About", None)]),
         byline("jordan-whitcombe", "aroha-tainui"),
         "<p>%s exists because most New Zealand casino comparison content is written by people who "
         "have never opened an account at the sites they recommend. Feeds get reprinted, bonus "
         "numbers get copied, payout claims get repeated, and payment methods that stopped working "
         "eighteen months ago stay on the page. We started this site to do the boring version "
         "properly.</p>" % NAME,
         "<p>The boring version means opening an account from an Auckland or Christchurch IP address, "
         "putting our own money through it, reading every clause of the bonus terms, timing the "
         "withdrawal with a stopwatch and asking the support desk something awkward at three in the "
         "morning. It takes about six hours per operator and we do it again every month.</p>",
         toc([("What we do", "what"), ("What makes us different", "different"),
              ("The team", "team"), ("How we are funded", "funding"),
              ("What we will not do", "wont"), ("Our record", "record"),
              ("Corrections policy", "corrections"), ("Contact", "contact"),
              ("Frequently asked questions", "faq")])]
    body.append(section("\n".join(s)))

    s = [h2("What we do", "what"),
         cards([
      ("01", "Test operators properly", "Real accounts, real deposits, real withdrawals from a New "
       "Zealand IP address. Six hours of active testing per operator, repeated monthly.",
       "/how-we-rate-casinos/", "Our methodology"),
      ("02", "Time every withdrawal", "A log of %d withdrawals and counting, recording confirmation "
       "time, funds-available time, holds and what was asked for." % N_WITHDRAWALS,
       "/fast-payout-casinos/", "The payout data"),
      ("03", "Read the terms so you do not have to", "Every bonus, clause by clause: what the "
       "multiple applies to, game weighting, maximum bet, expiry, cash-out caps.",
       "/casino-bonus/", "Bonus analysis"),
      ("04", "Track the law", "Written from the Online Casino Gambling Act 2026 and the regulations "
       "themselves, with section-level detail and dates.", "/licensed-online-casinos/", "NZ gambling law"),
      ("05", "Publish the negatives", "We list operators we would not use, with reasons. A comparison "
       "site that only recommends is an advertisement.", "/casino-reviews/", "All reviews"),
      ("06", "Say when we are wrong", "Corrections are logged on the page. If a figure here is "
       "stale, we would rather hear about it than have you rely on it.", "#corrections", "Corrections"),
     ])]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("What makes us different", "different"),
         table(["What most comparison sites do", "What we do"], [
      ["Quote the operator&rsquo;s stated payout window",
       "<b>Publish a measured median with the sample size attached</b>"],
      ["Rank on headline bonus size",
       "<b>Rank on turnover required, game weighting, maximum bet and expiry</b>"],
      ["Quote lobby size from a press release",
       "<b>Audit studio coverage against a fixed nine-studio list and sample RTP configurations</b>"],
      ["Show a licence badge",
       "<b>Publish the licence number, the operating company, and say when there is neither</b>"],
      ["List POLi because the template does",
       "<b>Re-test every payment rail monthly and remove the ones that stopped working</b>"],
      ["Use house bylines or stock-photo personas",
       "<b>Name a writer and a separate fact-checker on every page, each with a profile</b>"],
      ["Recommend everything they are paid for",
       "<b>List operators we would not use, ranked where their scores put them</b>"],
      ["Update the year in the title",
       "<b>Re-measure the underlying data monthly and log what changed</b>"],
     ], caption="Our approach against the industry norm"),
     note("<b>The POLi example is the clearest test.</b> POLi has not been available as a casino "
          "deposit method in New Zealand for some time. It still appears on a large number of New "
          "Zealand casino comparison pages, including some very well-known ones, because those pages "
          "were built from a template and never re-checked. That single fact tells you most of what "
          "you need to know about how current a page is.", "ok")]
    body.append(section("\n".join(s)))

    s = [h2("The team", "team"),
         "<p>Five editors, each with a declared beat. Every page names its writer and its "
         "fact-checker, and both link to a full profile.</p>",
         cards([('<img class="card-av" src="%s" alt="" width="46" height="46" loading="lazy" '
                 'decoding="async">' % lib.photo(k, 64),
                 AUTHORS[k]["name"], "<b>%s</b> &mdash; %s" % (AUTHORS[k]["role"], AUTHORS[k]["short"]),
                 "/authors/%s/" % k, "Profile") for k in AUTHOR_ORDER], cls="grid--3"),
         "<p>Between them: thirteen years in online gambling including six in operator payments, an "
         "LLB and a practice of reading primary legislation rather than summaries, ten years in "
         "payments analytics, seven years auditing casino game libraries, and eleven years in sports "
         "trading. <a href=\"/authors/\">Full biographies and credentials</a>.</p>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("How we are funded", "funding"),
         "<p>Revenue share. When a reader opens an account with an operator through a link on this "
         "site, that operator pays us a percentage of its net revenue from that account. There is no "
         "display advertising, no subscription and no paid placement.</p>",
         "<p>We think that model is defensible provided two things are true: that it is disclosed "
         "plainly, and that it demonstrably does not set the rankings. On the first, there is a "
         "disclosure at the top of every page that carries a commercial link. On the second, here is "
         "the evidence:</p>",
         "<ul>"
         "<li>Our highest-paying partner pays 50% and ranks fourth on the homepage.</li>"
         "<li>Our top-ranked casino pays 45%.</li>"
         "<li>We list operators paying 20% and 25% alongside those paying 45&ndash;50%.</li>"
         "<li>We list an operator we explicitly advise readers to be cautious about, at position "
         "sixteen, with the reasons stated.</li></ul>",
         "<p>If commission set the order, none of that would be the case. The "
         "<a href=\"/how-we-rate-casinos/\">methodology page</a> sets out the full set of controls, and we "
         "will tell you the commission rate for any specific operator if you email and ask.</p>",
         h3("What we will not do", "wont"),
         pros_cons(
      ["Test every operator from a New Zealand IP with our own money",
       "Publish the scoring weights and every component score",
       "Publish sample sizes beside every measured figure",
       "Name a writer and a fact-checker on every page",
       "List operators we would not personally use, with reasons",
       "Correct errors quickly and log material corrections on the page"],
      ["Accept payment for placement or for a higher position",
       "Let an operator review a draft before publication",
       "Remove a negative finding in exchange for commercial terms",
       "Publish guest posts, sponsored content or paid links",
       "Describe gambling as a way to make money or solve a financial problem",
       "Reprint an operator&rsquo;s claim as though we had verified it"],
      "What we commit to", "What we refuse")]
    body.append(section("\n".join(s)))

    s = [h2("Our record", "record"),
         keyfacts([("Founded", FOUNDED), ("Operators tested", str(N_OPERATORS_TESTED)),
                   ("Operators listed", "19"), ("Withdrawals timed", str(N_WITHDRAWALS)),
                   ("Hours of testing", N_HOURS), ("Editors", "5"),
                   ("Pages fact-checked", "Every one"), ("Review cycle", "Monthly")]),
         h3("Corrections policy", "corrections"),
         "<p>We publish numbers, and numbers go stale or turn out to be wrong. When that happens we "
         "want to fix it quickly and visibly.</p>",
         "<ul>"
         "<li>Email <a href=\"mailto:%s\">%s</a> with the URL and the problem.</li>" % (EMAIL, EMAIL) +
         "<li>We aim to acknowledge within two working days and correct within five.</li>"
         "<li>Material corrections &mdash; anything that would change a reader&rsquo;s decision "
         "&mdash; are noted on the page itself, not silently edited.</li>"
         "<li>Every page carries the date it was last updated and the date of its next scheduled "
         "review. If the next review date has passed, treat the figures with caution and tell "
         "us.</li></ul>",
         h3("Contact", "contact"),
         "<p>Editorial and corrections: <a href=\"mailto:%s\">%s</a>. Operator complaints: "
         "<a href=\"mailto:%s\">%s</a>. Privacy: <a href=\"mailto:%s\">%s</a>. General: "
         "<a href=\"mailto:%s\">%s</a>. Post: %s. Full detail on our "
         "<a href=\"/contact/\">contact page</a>.</p>"
         % (EMAIL, EMAIL, EMAIL_COMPLAINTS, EMAIL_COMPLAINTS, EMAIL_PRIVACY, EMAIL_PRIVACY,
            EMAIL_SUPPORT, EMAIL_SUPPORT, POSTAL),
         faq(faqs, "About us &mdash; frequently asked questions", "faq"),
         ctaband("Start with the rankings",
                 "Nineteen operators tested, scored and explained, with the component marks published.",
                 [("Best online casinos NZ", "/online-casinos/"),
                  ("How we review", "/how-we-rate-casinos/")])]
    body.append(section("\n".join(s), cls="sec--sur"))

    trail = [("Home", "/"), ("About", path)]
    schema = [{"@type": "AboutPage", "@id": SITE + path + "#about",
               "name": "About " + NAME, "url": SITE + path,
               "isPartOf": {"@id": SITE + "/#website"},
               "about": {"@id": SITE + "/#organization"},
               "inLanguage": "en-NZ"},
              lib.breadcrumb_schema(path, trail), lib.faq_schema(path, faqs)]
    lib.write(path, lib.seo_title(path),
              "%s is an independent New Zealand casino review publisher. Five named editors, %d "
              "operators tested, %d withdrawals timed, and a published scoring model."
              % (NAME, N_OPERATORS_TESTED, N_WITHDRAWALS),
              "\n".join(body), schema, prio=0.7, freq="monthly", og_type="website")


# ===========================================================================
def build_contact():
    path = "/contact/"
    faqs = [
     ("How quickly will you reply?",
      "<p>Two working days for most enquiries, and usually faster for corrections. We are a small "
      "team in New Zealand, so replies arrive during NZ business hours.</p>"),
     ("I have a dispute with a casino. Can you help?",
      "<p>We cannot adjudicate &mdash; we are a publisher, not a regulator or an alternative dispute "
      "resolution body. What we can do is tell you which regulator the operator is licensed by and "
      "how to escalate, log the complaint against that operator&rsquo;s trust score, and follow up "
      "with the operator ourselves where it is one we list. Email "
      "<a href=\"mailto:%s\">%s</a> with the operator name, dates, amounts and what the operator has "
      "told you.</p>" % (EMAIL_COMPLAINTS, EMAIL_COMPLAINTS)),
     ("I think a figure on your site is wrong.",
      "<p>Please tell us. Email <a href=\"mailto:%s\">%s</a> with the URL and what is wrong. We aim "
      "to correct within five working days and we note material corrections on the page.</p>"
      % (EMAIL, EMAIL)),
     ("I represent an operator and want to be listed.",
      "<p>Email <a href=\"mailto:%s\">%s</a>. Listing follows testing and scoring, not commercial "
      "discussion: we will open an account, deposit, play, withdraw and score you against the same "
      "published model as everyone else. We do not sell placement, we do not send drafts for "
      "approval, and we do not remove findings.</p>" % (EMAIL, EMAIL)),
     ("Do you accept guest posts or link placements?",
      "<p>No. We do not publish guest contributions, sponsored posts, paid links or link insertions, "
      "and we do not reply to outreach offering them.</p>"),
     ("How do I request my personal data or ask for it to be deleted?",
      "<p>Email <a href=\"mailto:%s\">%s</a>. Under the Privacy Act 2020 you have the right to "
      "access and correct personal information we hold about you, and we will respond within 20 "
      "working days. See our <a href=\"/privacy-policy/\">privacy policy</a>.</p>"
      % (EMAIL_PRIVACY, EMAIL_PRIVACY)),
    ]

    body = [hero(
      "We read everything",
      lib.seo_h1(path),
      "Corrections, complaints, privacy requests and editorial enquiries all reach a person. We are a "
      "small team based in New Zealand and we aim to reply within two working days.",
      stats=[("2 days", "Target reply time"), ("NZ", "Where we are"),
             ("5", "Editors"), ("Always", "Corrections welcome")],
      ctas=[("Email the editor", "mailto:" + EMAIL), ("About us", "/about/")], aqua=True)]

    s = [crumbs([("Home", "/"), ("Contact", None)]),
         h2("Who to contact about what", "who"),
         table(["Reason", "Email", "What to include"], [
      ["<b>Correction or factual error</b>", '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL),
       "The page URL, the figure or statement that is wrong, and the correct position if you know it"],
      ["<b>Complaint about an operator</b>",
       '<a href="mailto:%s">%s</a>' % (EMAIL_COMPLAINTS, EMAIL_COMPLAINTS),
       "Operator name, your account registration date, dates and amounts, and what the operator has "
       "said to you"],
      ["<b>Privacy request</b>", '<a href="mailto:%s">%s</a>' % (EMAIL_PRIVACY, EMAIL_PRIVACY),
       "What you are asking for &mdash; access, correction or deletion &mdash; and enough detail to "
       "identify the records"],
      ["<b>Editorial enquiry or feedback</b>", '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL),
       "Whatever is on your mind. We read all of it."],
      ["<b>Operator or commercial enquiry</b>", '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL),
       "Brand, licence details and markets. Note that listing follows testing, not commercial terms."],
      ["<b>Everything else</b>", '<a href="mailto:%s">%s</a>' % (EMAIL_SUPPORT, EMAIL_SUPPORT),
       "General enquiries"],
     ], caption="Contact routes")]
    body.append(section("\n".join(s)))

    form = ('<form class="form" method="post" action="/contact/" '
            'aria-label="Contact form">'
            '<div class="field"><label for="cf-name">Your name</label>'
            '<input id="cf-name" name="name" type="text" autocomplete="name" required></div>'
            '<div class="field"><label for="cf-email">Email address</label>'
            '<input id="cf-email" name="email" type="email" autocomplete="email" required>'
            '<span class="hint">We use it to reply and nothing else.</span></div>'
            '<div class="field"><label for="cf-topic">What is this about?</label>'
            '<select id="cf-topic" name="topic">'
            '<option>Correction or factual error</option>'
            '<option>Complaint about an operator</option>'
            '<option>Privacy request</option>'
            '<option>Editorial feedback</option>'
            '<option>Operator or commercial enquiry</option>'
            '<option>Something else</option></select></div>'
            '<div class="field"><label for="cf-url">Page URL, if relevant</label>'
            '<input id="cf-url" name="url" type="url" placeholder="https://%s/..."></div>'
            '<div class="field"><label for="cf-msg">Message</label>'
            '<textarea id="cf-msg" name="message" required></textarea>'
            '<span class="hint">Dates, amounts and operator names help us act faster.</span></div>'
            '<button class="btn btn--wide" type="submit">Send message</button>'
            '<p style="margin:.9rem 0 0;font-size:.79rem;color:var(--faint)">By sending this you agree '
            'to our <a href="/privacy-policy/">privacy policy</a>. We do not add you to a mailing list '
            'and we do not pass your details to operators.</p>'
            '</form>' % DOMAIN)

    s = ['<div class="grid grid--2">',
         '<div>' + h2("Send us a message", "form") +
         "<p>The form goes to the editorial inbox. If your enquiry is a complaint about an operator, "
         "emailing <a href=\"mailto:%s\">%s</a> directly is faster.</p>" % (EMAIL_COMPLAINTS, EMAIL_COMPLAINTS) +
         form + "</div>",
         '<div>' + h2("Company details", "company") +
         lib.keyfacts([("Publisher", LEGAL), ("Trading as", NAME), ("NZBN", NZBN),
                       ("Registered", "New Zealand"), ("Founded", FOUNDED),
                       ("Postal address", POSTAL)]) +
         h3("Postal", "postal") +
         "<p>%s<br>%s</p>" % (LEGAL, POSTAL) +
         h3("Response times", "times") +
         "<p>We aim to acknowledge every email within two working days and to resolve corrections "
         "within five. Complaints involving an operator can take longer because we contact the "
         "operator as part of the process, and we will keep you updated.</p>" +
         h3("What we cannot do", "cannot") +
         "<ul><li>Adjudicate a dispute between you and an operator &mdash; we are a publisher, not a "
         "regulator</li><li>Recover funds, unlock an account or intervene in a KYC check</li>"
         "<li>Give legal, tax or financial advice</li>"
         "<li>Offer gambling counselling &mdash; for that, call the Gambling Helpline free on "
         "<a href=\"tel:0800654655\">0800 654 655</a>, 24 hours</li></ul>" +
         "</div>", "</div>"]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [faq(faqs, "Contact &mdash; frequently asked questions", "faq"),
         note("<b>If you need gambling support, not us.</b> Gambling Helpline Aotearoa is free, "
              "confidential and available 24 hours on <a href=\"tel:0800654655\">0800 654 655</a>, "
              "or free text 8006. See our <a href=\"/responsible-gambling/\">responsible gambling "
              "page</a> for the full list of New Zealand services.", "no")]
    body.append(section("\n".join(s)))

    trail = [("Home", "/"), ("Contact", path)]
    schema = [{"@type": "ContactPage", "@id": SITE + path + "#contact",
               "name": "Contact " + NAME, "url": SITE + path,
               "isPartOf": {"@id": SITE + "/#website"},
               "about": {"@id": SITE + "/#organization"}, "inLanguage": "en-NZ"},
              lib.breadcrumb_schema(path, trail), lib.faq_schema(path, faqs)]
    lib.write(path, lib.seo_title(path),
              "Contact the %s editorial team. Corrections, operator complaints, privacy requests and "
              "general enquiries, answered within two working days." % NAME,
              "\n".join(body), schema, prio=0.6, freq="yearly", og_type="website")


# ===========================================================================
def build_authors():
    path = "/authors/"
    body = [hero(
      "Named, credentialed, accountable",
      lib.seo_h1(path),
      "Every page on this site names the person who wrote it and a second person who checked it. "
      "This page is who they are, what they are qualified to write about, and which parts of the "
      "site each of them owns.",
      stats=[("5", "Editors"), ("51", "Combined years in the industry"),
             ("2", "Names on every page"), ("Monthly", "Re-review cycle")],
      ctas=[("How we review", "/how-we-rate-casinos/"), ("About us", "/about/")], aqua=True)]

    s = [crumbs([("Home", "/"), ("Authors", None)]),
         "<p>Gambling is a subject where the reader has a right to know who is talking. A house byline "
         "on a page recommending where to put your money is not good enough, and neither is a stock "
         "photograph attached to a name that does not exist anywhere else.</p>",
         "<p>Everyone below is a real member of the editorial team with a declared beat. They write "
         "only within it: our regulation editor does not write pokies reviews, and our games editor "
         "does not write about the Online Casino Gambling Act. Every page names a writer and a "
         "separate fact-checker, and both link here.</p>"]
    body.append(section("\n".join(s)))

    rows = []
    for k in AUTHOR_ORDER:
        a = AUTHORS[k]
        rows.append(['<span class="t-author"><img src="%s" alt="" width="34" height="34" '
                     'loading="lazy" decoding="async">'
                     '<a href="/authors/%s/"><b>%s</b></a></span>'
                     % (lib.photo(k, 64), k, a["name"]), a["role"],
                     str(YEAR and (2026 - a["since"])) + " years", a["loc"], a["beat"]])
    s = [h2("The editorial team", "team"),
         table(["Editor", "Role", "In the industry", "Based", "Beat"], rows,
               caption="Who writes what on %s" % NAME)]
    body.append(section("\n".join(s), cls="sec--sur"))

    s = [h2("Full profiles", "profiles")]
    for k in AUTHOR_ORDER:
        s.append('<div id="%s">%s</div>' % (k, lib.authorbox(k)))
    s.append("<p>Each editor has a full profile page with their credentials, beat and the pages they "
             "own: " + ", ".join('<a href="/authors/%s/">%s</a>' % (k, AUTHORS[k]["name"])
                                 for k in AUTHOR_ORDER) + ".</p>")
    body.append(section("\n".join(s)))

    s = [h2("How bylines work on this site", "bylines"),
         "<ul>"
         "<li><b>Writer.</b> The named editor who researched and wrote the page, drawn from the beat "
         "it falls in.</li>"
         "<li><b>Fact-checker.</b> A second editor who independently verifies every figure, date, "
         "licence and claim before publication. Never the same person as the writer.</li>"
         "<li><b>Data owner.</b> Payout figures come from the withdrawal timing programme regardless "
         "of who wrote the page, and Priya Raman owns that dataset.</li>"
         "<li><b>Final sign-off.</b> Jordan Whitcombe approves every ranked list on the site.</li>"
         "<li><b>Updated and next review dates.</b> Every page carries both. If the next review date "
         "has passed, the figures have not been re-verified and you should treat them accordingly "
         "&mdash; and tell us.</li></ul>",
         ctaband("Want to know how the scoring works?",
                 "The weights, the evidence behind each component, and how we are paid.",
                 [("How we review", "/how-we-rate-casinos/"), ("About us", "/about/")])]
    body.append(section("\n".join(s), cls="sec--sur"))

    trail = [("Home", "/"), ("Authors", path)]
    schema = [{"@type": "CollectionPage", "@id": SITE + path + "#collection",
               "name": "Authors", "url": SITE + path, "inLanguage": "en-NZ",
               "isPartOf": {"@id": SITE + "/#website"},
               "hasPart": [lib.person_schema(k) for k in AUTHOR_ORDER]},
              lib.breadcrumb_schema(path, trail)]
    lib.write(path, lib.seo_title(path),
              "The five named editors behind %s, their credentials and beats. Every page on this "
              "site names a writer and a separate fact-checker." % NAME,
              "\n".join(body), schema, prio=0.65, freq="monthly", og_type="website")

    for k in AUTHOR_ORDER:
        build_author(k)


def build_author(slug):
    a = AUTHORS[slug]
    path = "/authors/%s/" % slug
    lib.register_seo(path, a["name"],
                     lib.fit(a["name"], ["%s at %s" % (lib.plain(a["role"]), NAME),
                                         lib.plain(a["role"]),
                                         "%s Editor" % NAME]),
                     "%s at %s" % (a["role"], NAME))
    others = [x for x in AUTHOR_ORDER if x != slug]

    pages = {
     "jordan-whitcombe": [("Best online casino sites NZ", "/"),
                          ("Best online casinos NZ", "/online-casinos/"),
                          ("Casino bonuses NZ", "/casino-bonus/"),
                          ("New online casinos NZ", "/new-casinos-nz/"),
                          ("No deposit bonuses NZ", "/no-deposit-bonus/"),
                          ("How we review", "/how-we-rate-casinos/"),
                          ("Casino reviews", "/casino-reviews/")],
     "aroha-tainui": [("New Zealand gambling law", "/licensed-online-casinos/"),
                      ("Responsible gambling", "/responsible-gambling/")],
     "priya-raman": [("Casino payment methods NZ", "/casino-payment-methods/"),
                     ("Fastest payout casinos NZ", "/fast-payout-casinos/"),
                     ("Best crypto casinos NZ", "/crypto-casinos-nz/")],
     "sam-kavanagh": [("Online pokies NZ", "/online-pokies/"),
                      ("Best live casinos NZ", "/live-casino/"),
                      ("Highest payout casinos NZ", "/casino-payout-percentages/")],
     "manaia-kerr": [("Online betting NZ", "/online-betting/"),
                     ("Best sports betting sites NZ", "/best-sports-betting-sites/")],
    }[slug]

    body = [hero("Author profile &middot; %d years in the industry" % (2026 - a["since"]),
                 lib.seo_h1(path), a["short"],
      stats=[("%d" % (2026 - a["since"]), "Years in the industry"), (a["loc"], "Based"),
             ("%d" % len(pages), "Pages owned"), ("Named", "On every page they write")],
      ctas=[("All authors", "/authors/"), ("How we review", "/how-we-rate-casinos/")], aqua=True)]

    s = [crumbs([("Home", "/"), ("Authors", "/authors/"), (a["name"], None)]),
         '<div class="authorhead">'
         '<img src="%s" alt="%s" width="92" height="92" decoding="async">'
         '<div><p class="role">%s</p>'
         '<p class="authorhead-meta">In the industry since <b>%d</b> &middot; '
         'Based in <b>%s</b> &middot; %d years&rsquo; experience</p>'
         '<p class="authorhead-beat">%s</p></div></div>'
         % (lib.photo(slug), lib.esc(a["name"]), a["role"], a["since"], a["loc"],
            2026 - a["since"], a["specialism"]),
         h2("Biography", "bio"), "<p>%s</p>" % a["bio"],
         h2("Credentials", "credentials"),
         "<ul>%s</ul>" % "".join("<li>%s</li>" % c for c in a["creds"]),
         h2("Areas of expertise", "expertise"),
         "<p>%s</p>" % a["specialism"],
         '<div class="pill-row">%s</div>' % "".join(
             '<span class="chip chip--aqua">%s</span>' % t.strip()
             for t in a["specialism"].split(",")),
         h2("Pages %s owns" % a["name"].split(" ")[0], "pages"),
         "<p>%s writes and maintains the following pages. Each one is re-checked monthly and carries "
         "both the last-updated date and the date of the next scheduled review.</p>" % a["name"],
         "<ul>%s</ul>" % "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in pages),
         h2("Editorial approach", "approach"),
         "<p>%s works to the standards set out on our <a href=\"/how-we-rate-casinos/\">methodology "
         "page</a>: published weights, evidence collected first-hand, sample sizes attached to every "
         "measured figure, and a second editor fact-checking before publication. %s does not accept "
         "operator input on drafts and does not write outside the beat above.</p>"
         % (a["name"], a["name"].split(" ")[0]),
         h2("The rest of the team", "team"),
         cards([("", AUTHORS[k]["name"], "<b>%s</b> &mdash; %s" % (AUTHORS[k]["role"], AUTHORS[k]["short"]),
                 "/authors/%s/" % k, "Profile") for k in others], cls="grid--2"),
         '<p><small>Contact %s through the editorial inbox: <a href="mailto:%s">%s</a>.</small></p>'
         % (a["name"], EMAIL, EMAIL)]
    body.append(section("\n".join(s), wrap="wrap wrap--narrow"))

    trail = [("Home", "/"), ("Authors", "/authors/"), (a["name"], path)]
    schema = [{"@type": "ProfilePage", "@id": SITE + path + "#profile",
               "name": a["name"], "url": SITE + path, "inLanguage": "en-NZ",
               "isPartOf": {"@id": SITE + "/#website"},
               "mainEntity": lib.person_schema(slug)},
              lib.breadcrumb_schema(path, trail)]
    lib.write(path, lib.seo_title(path),
              "%s is %s at %s. %s" % (a["name"], lib.plain(a["role"]).lower(), NAME,
                                      lib.plain(a["short"])),
              "\n".join(body), schema, prio=0.5, freq="yearly", og_type="profile")

# ===========================================================================
def _legal_page(path, title, h1, lede, desc, sections, toc_items, author="aroha-tainui"):
    label = h1                      # short form, for breadcrumbs and schema
    h1 = lib.seo_h1(path)           # "Primary [Month Year]: Secondary"
    title = lib.seo_title(path)
    body = [hero("Last updated %s" % LEGAL_UPDATED, h1, lede,
                 stats=None, ctas=[("Contact us", "/contact/"), ("About us", "/about/")], aqua=True)]
    s = [crumbs([("Home", "/"), (label, None)]),
         lib.byline(author, "jordan-whitcombe"),
         lib.toc(toc_items)]
    body.append(section("\n".join(s), wrap="wrap wrap--narrow"))
    body.append(section('<div class="prose">%s</div>' % "\n".join(sections),
                        wrap="wrap wrap--narrow"))
    trail = [("Home", "/"), (label, path)]
    schema = [{"@type": "WebPage", "@id": SITE + path + "#webpage", "name": label,
               "url": SITE + path, "inLanguage": "en-NZ",
               "isPartOf": {"@id": SITE + "/#website"},
               "dateModified": lib.UPDATED,
               "publisher": {"@id": SITE + "/#organization"}},
              lib.breadcrumb_schema(path, trail)]
    lib.write(path, title, desc, "\n".join(body), schema, prio=0.3, freq="yearly")


def build_terms():
    path = "/terms-and-conditions/"
    secs = [
     h2("1. Who we are", "who"),
     "<p>This website at <b>%s</b> is operated by %s (&ldquo;we&rdquo;, &ldquo;us&rdquo;, "
     "&ldquo;our&rdquo;), a company registered in New Zealand, NZBN %s, trading as %s. Our postal "
     "address is %s and our contact address for legal notices is "
     "<a href=\"mailto:%s\">%s</a>.</p>" % (DOMAIN, LEGAL, NZBN, NAME, POSTAL, EMAIL, EMAIL),
     "<p>By accessing or using this website you agree to these terms. If you do not agree to them, "
     "please do not use the site.</p>",

     h2("2. Age restriction", "age"),
     "<p>This website is intended solely for people aged <b>18 years or over</b> who are legally "
     "permitted to gamble in their jurisdiction. By using the site you confirm that you are 18 or "
     "over. If you are under 18 you must leave the site immediately. We take reasonable steps to "
     "prevent under-age access and we do not knowingly direct any content at people under 18.</p>",

     h2("3. Nature of the service", "nature"),
     "<p>We are an <b>independent information and comparison publisher</b>. We do not operate any "
     "gambling service, we do not accept bets or deposits, we do not hold customer funds and we are "
     "not an agent of any gambling operator. Any gambling you undertake is a contract between you and "
     "the operator concerned, governed by that operator&rsquo;s own terms and its own licence.</p>",
     "<p>Nothing on this site is an offer or inducement to gamble in any jurisdiction where doing so "
     "would be unlawful. It is your responsibility to know and comply with the law that applies to "
     "you.</p>",

     h2("4. Affiliate relationships and how we are paid", "affiliate"),
     "<p>We are paid a commission by gambling operators when a reader opens an account through a link "
     "on this site. This is disclosed on every page carrying such a link. It costs you nothing and it "
     "does not change any offer available to you.</p>",
     "<p>Commercial arrangements do not determine our rankings. Our scoring model is published in "
     "full on our <a href=\"/how-we-rate-casinos/\">how we review</a> page and applied identically to every "
     "operator. We list operators we do not recommend, and our highest-paying partner is not our "
     "highest-ranked operator.</p>",

     h2("5. Accuracy of information", "accuracy"),
     "<p>We take substantial care with the information published here. Every operator is tested from "
     "a New Zealand IP address, every figure carries a source or a sample size, and every page is "
     "fact-checked by a second editor and re-reviewed monthly.</p>",
     "<p>Despite that, <b>bonuses, terms, odds, payment methods, licences and availability change "
     "without notice</b>, sometimes daily. Information on this site may be out of date by the time "
     "you read it. You must read the operator&rsquo;s own current terms before depositing. Where a "
     "conflict exists between this site and an operator&rsquo;s terms, the operator&rsquo;s terms "
     "govern your relationship with them.</p>",
     "<p>If you find an error, please tell us at <a href=\"mailto:%s\">%s</a>. We aim to correct "
     "material errors within five working days.</p>" % (EMAIL, EMAIL),

     h2("6. No advice", "no-advice"),
     "<p>Nothing on this website constitutes legal, financial, tax, investment or professional "
     "advice, and nothing here should be relied on as such. Gambling is not an investment and should "
     "never be treated as a source of income or as a way to resolve financial difficulty. Information "
     "about New Zealand law is general information only; if you need advice about your own position, "
     "consult a New Zealand lawyer or a chartered accountant.</p>",

     h2("7. Third-party sites", "third-party"),
     "<p>This site links to third-party websites, including gambling operators and support services. "
     "We do not control those sites and we are not responsible for their content, their terms, their "
     "privacy practices or their conduct. A link is not an endorsement of everything on the linked "
     "site, and your use of any third-party site is at your own risk and subject to that site&rsquo;s "
     "terms.</p>",

     h2("8. Disputes with operators", "disputes"),
     "<p>We are a publisher, not a regulator or a dispute resolution body. We cannot adjudicate a "
     "dispute between you and an operator, recover funds, unlock an account or intervene in an "
     "identity verification process.</p>",
     "<p>What we will do, if you email <a href=\"mailto:%s\">%s</a>: tell you which regulator the "
     "operator is licensed by and how to escalate, record the complaint against that "
     "operator&rsquo;s trust score, and raise it with the operator ourselves where it is one we "
     "list.</p>" % (EMAIL_COMPLAINTS, EMAIL_COMPLAINTS),

     h2("9. Intellectual property", "ip"),
     "<p>All content on this site &mdash; text, data, scoring models, tables, layout, design and code "
     "&mdash; is owned by %s or used under licence, and is protected by copyright. Operator logos and "
     "trade marks remain the property of their respective owners and are used for identification "
     "purposes only.</p>" % LEGAL,
     "<p>You may quote short extracts for the purposes of review, criticism or news reporting with "
     "clear attribution and a link. You may not reproduce substantial parts of this site, scrape it "
     "systematically, or republish our datasets without written permission.</p>",

     h2("10. Acceptable use", "acceptable-use"),
     "<p>You must not use this site to break the law, to attempt to gain unauthorised access to any "
     "system, to introduce malicious code, to scrape content at a rate that degrades service for "
     "others, or to impersonate any person. We reserve the right to block access where we reasonably "
     "believe any of these is occurring.</p>",

     h2("11. Liability", "liability"),
     "<p>To the maximum extent permitted by law, we exclude liability for any loss &mdash; including "
     "gambling losses, lost profits, lost data or consequential loss &mdash; arising from your use of "
     "this site or from reliance on information published here. You gamble entirely at your own "
     "risk.</p>",
     "<p>Nothing in these terms limits or excludes any right you have under the <b>Consumer "
     "Guarantees Act 1993</b> or the <b>Fair Trading Act 1986</b> that cannot lawfully be limited or "
     "excluded. Where you acquire services from us for business purposes, the Consumer Guarantees Act "
     "does not apply.</p>",

     h2("12. Responsible gambling", "rg"),
     "<p>Gambling carries a risk of harm. If your gambling is causing difficulty for you or for "
     "someone close to you, free and confidential help is available in New Zealand 24 hours a day "
     "from the <b>Gambling Helpline on <a href=\"tel:0800654655\">0800 654 655</a></b> or by free "
     "text to <b>8006</b>. See our <a href=\"/responsible-gambling/\">responsible gambling page</a> "
     "for the full list of services, self-exclusion guidance and blocking tools.</p>",

     h2("13. Changes to these terms", "changes"),
     "<p>We may update these terms from time to time. The current version always appears on this "
     "page with the date it was last updated at the top. Continuing to use the site after a change "
     "means you accept the revised terms.</p>",

     h2("14. Governing law", "law"),
     "<p>These terms are governed by the law of <b>New Zealand</b>, and you and we submit to the "
     "non-exclusive jurisdiction of the New Zealand courts.</p>",

     h2("15. Contact", "contact"),
     "<p>%s<br>%s<br>General: <a href=\"mailto:%s\">%s</a><br>Editorial and corrections: "
     "<a href=\"mailto:%s\">%s</a><br>Complaints: <a href=\"mailto:%s\">%s</a><br>Privacy: "
     "<a href=\"mailto:%s\">%s</a></p>"
     % (LEGAL, POSTAL, EMAIL_SUPPORT, EMAIL_SUPPORT, EMAIL, EMAIL,
        EMAIL_COMPLAINTS, EMAIL_COMPLAINTS, EMAIL_PRIVACY, EMAIL_PRIVACY),
     "<p><small>Last updated %s.</small></p>" % LEGAL_UPDATED,
    ]
    toc_items = [("Who we are", "who"), ("Age restriction", "age"),
                 ("Nature of the service", "nature"), ("Affiliate relationships", "affiliate"),
                 ("Accuracy of information", "accuracy"), ("No advice", "no-advice"),
                 ("Third-party sites", "third-party"), ("Disputes with operators", "disputes"),
                 ("Intellectual property", "ip"), ("Acceptable use", "acceptable-use"),
                 ("Liability", "liability"), ("Responsible gambling", "rg"),
                 ("Changes to these terms", "changes"), ("Governing law", "law"),
                 ("Contact", "contact")]
    _legal_page(path, "Terms and Conditions &mdash; %s" % NAME, "Terms and Conditions",
                "The terms on which you may use this website, who we are, how we are paid, and the "
                "limits of what we can be relied on for.",
                "Terms and conditions for %s: age restriction, affiliate disclosure, accuracy, "
                "liability and New Zealand governing law." % NAME,
                secs, toc_items)


def build_privacy():
    path = "/privacy-policy/"
    secs = [
     h2("1. Introduction", "intro"),
     "<p>%s (&ldquo;we&rdquo;) operates %s. This policy explains what personal information we "
     "collect, why, what we do with it and what rights you have. We handle personal information in "
     "accordance with the <b>Privacy Act 2020</b> and the thirteen Information Privacy Principles.</p>"
     % (LEGAL, DOMAIN),
     "<p>Our privacy contact is <a href=\"mailto:%s\">%s</a>." % (EMAIL_PRIVACY, EMAIL_PRIVACY) +
     " Postal enquiries to %s.</p>" % POSTAL,

     h2("2. What we collect", "collect"),
     "<p>We collect as little as we can. Specifically:</p>",
     lib.table(["Category", "What it is", "How it is collected", "Why"], [
      ["Contact details", "Name, email address and the content of your message",
       "Only when you email us or submit the contact form",
       "To reply to you and to process corrections, complaints and privacy requests"],
      ["Technical data", "IP address, browser type and version, device type, operating system, "
       "screen size, referring URL",
       "Automatically, in server logs and analytics", "Security, fraud prevention, and understanding "
       "which pages are useful"],
      ["Usage data", "Pages viewed, time on page, links clicked, approximate region",
       "Analytics cookies, only with your consent", "To improve the site"],
      ["Affiliate click data", "That a click occurred on an operator link, with a campaign identifier",
       "A tracking parameter or cookie set when you click an operator link",
       "So the operator can attribute the referral and pay us"],
     ], caption="Personal information we collect"),
     "<p>We do <b>not</b> collect or store payment details, gambling account credentials, deposit or "
     "withdrawal amounts, or any information about your gambling activity. We never see your casino "
     "account.</p>",

     h2("3. Legal basis and purpose", "purpose"),
     "<p>Under the Privacy Act 2020 we collect personal information only for a lawful purpose "
     "connected with our function as a publisher, and only where collection is necessary for that "
     "purpose. We use it to respond to you, to operate and secure the website, to measure which "
     "content is useful, and to receive attribution for referrals.</p>",
     "<p>We do not use your information to make automated decisions with legal or similarly "
     "significant effects, and we do not profile individuals.</p>",

     h2("4. Cookies and similar technologies", "cookies"),
     "<p>We use a small number of cookies. Strictly necessary cookies are set without consent because "
     "the site cannot work without them; analytics and affiliate attribution cookies are set only "
     "where you have consented or where you have clicked an operator link. Full detail, including "
     "names, purposes and durations, is in our <a href=\"/cookie-policy/\">cookie policy</a>, where "
     "you can also change your choices.</p>",

     h2("5. Who we share information with", "sharing"),
     "<p>We do not sell personal information, and we do not share your contact details with gambling "
     "operators. Limited sharing occurs with:</p>",
     "<ul>"
     "<li><b>Our hosting and infrastructure providers</b>, who process server logs on our behalf "
     "under contract.</li>"
     "<li><b>Our analytics provider</b>, where you have consented to analytics cookies, in a "
     "configuration that does not identify you by name.</li>"
     "<li><b>Affiliate networks and operators</b>, but only the fact of a click and a campaign "
     "identifier &mdash; never your name, email address or message.</li>"
     "<li><b>Law enforcement or regulators</b>, where we are legally required to disclose.</li>"
     "</ul>",
     "<p>Some of these providers are located outside New Zealand. Where personal information is "
     "transferred overseas we take reasonable steps to ensure it is subject to comparable safeguards, "
     "as required by Information Privacy Principle 12.</p>",

     h2("6. How long we keep it", "retention"),
     "<ul>"
     "<li><b>Email correspondence:</b> 24 months from the last contact, then deleted, unless it "
     "relates to an unresolved complaint.</li>"
     "<li><b>Server logs:</b> 90 days.</li>"
     "<li><b>Analytics data:</b> 14 months, in aggregated form.</li>"
     "<li><b>Affiliate attribution cookies:</b> up to 30 days on your device, depending on the "
     "operator&rsquo;s programme.</li></ul>",

     h2("7. Security", "security"),
     "<p>The site is served over HTTPS. Access to the email inbox and to analytics is restricted to "
     "members of the editorial team and protected by multi-factor authentication. We keep no "
     "database of user accounts because the site has no user accounts. If we become aware of a "
     "privacy breach that has caused or is likely to cause serious harm, we will notify the Office "
     "of the Privacy Commissioner and affected individuals as required by the Privacy Act 2020.</p>",

     h2("8. Your rights", "rights"),
     "<p>Under the Privacy Act 2020 you have the right to:</p>",
     "<ul>"
     "<li><b>Access</b> the personal information we hold about you.</li>"
     "<li><b>Correct</b> information that is wrong, and to have a statement of correction attached "
     "if we disagree.</li>"
     "<li><b>Request deletion</b> of information we no longer need.</li>"
     "<li><b>Withdraw consent</b> to analytics cookies at any time through our "
     "<a href=\"/cookie-policy/\">cookie policy</a>.</li>"
     "<li><b>Complain</b> to us and, if you are not satisfied, to the Office of the Privacy "
     "Commissioner.</li></ul>",
     "<p>To exercise any of these, email <a href=\"mailto:%s\">%s</a>. We will respond within "
     "<b>20 working days</b>, which is the period the Privacy Act allows.</p>"
     % (EMAIL_PRIVACY, EMAIL_PRIVACY),

     h2("9. Complaints", "complaints"),
     "<p>If you are unhappy with how we have handled your personal information, contact us first at "
     "<a href=\"mailto:%s\">%s</a> so we can try to resolve it. If you remain dissatisfied you may "
     "complain to the <b>Office of the Privacy Commissioner</b>: "
     "<a href=\"https://www.privacy.org.nz/\" rel=\"noopener nofollow\" target=\"_blank\">privacy.org.nz</a>, "
     "0800 803 909.</p>" % (EMAIL_PRIVACY, EMAIL_PRIVACY),

     h2("10. Children", "children"),
     "<p>This site is for adults aged 18 and over. We do not knowingly collect personal information "
     "from anyone under 18. If you believe we hold information about a person under 18, contact "
     "<a href=\"mailto:%s\">%s</a> and we will delete it.</p>" % (EMAIL_PRIVACY, EMAIL_PRIVACY),

     h2("11. Changes to this policy", "changes"),
     "<p>We may update this policy. The current version is always on this page with the date it was "
     "last updated. Material changes will be noted at the top of the page for at least 30 days.</p>",
     "<p><small>Last updated %s.</small></p>" % LEGAL_UPDATED,
    ]
    toc_items = [("Introduction", "intro"), ("What we collect", "collect"),
                 ("Legal basis and purpose", "purpose"), ("Cookies", "cookies"),
                 ("Who we share with", "sharing"), ("How long we keep it", "retention"),
                 ("Security", "security"), ("Your rights", "rights"),
                 ("Complaints", "complaints"), ("Children", "children"),
                 ("Changes", "changes")]
    _legal_page(path, "Privacy Policy &mdash; %s" % NAME, "Privacy Policy",
                "What personal information we collect, why, who we share it with, and the rights you "
                "have under the New Zealand Privacy Act 2020.",
                "%s privacy policy: what we collect, how we use it, overseas transfers, retention "
                "periods and your rights under the Privacy Act 2020." % NAME,
                secs, toc_items)


def build_cookies():
    path = "/cookie-policy/"
    secs = [
     h2("1. What cookies are", "what"),
     "<p>A cookie is a small text file a website stores on your device. It lets the site remember "
     "things between page loads &mdash; that you dismissed a banner, for example &mdash; and lets us "
     "count visits without identifying you by name. Similar technologies such as local storage and "
     "pixels work the same way and are covered by this policy.</p>",

     h2("2. The cookies we use", "which"),
     "<p>We use as few as we can get away with. The site has no user accounts and no advertising "
     "network, so the list is short.</p>",
     lib.table(["Cookie / technology", "Type", "Purpose", "Duration", "Consent needed?"], [
      ["<code>ce_consent</code>", "Strictly necessary",
       "Remembers your cookie choices so we do not ask again", "12 months", "No"],
      ["<code>ce_session</code>", "Strictly necessary",
       "Maintains page state during a single visit", "Session", "No"],
      ["Analytics (first-party, IP-truncated)", "Analytics",
       "Counts page views and measures which content is useful. Configured so that individuals are "
       "not identified.", "14 months", "<b>Yes</b>"],
      ["Affiliate attribution parameter", "Functional / commercial",
       "Records that you reached an operator through this site so the referral can be attributed. "
       "Set only when you click an operator link.", "Up to 30 days", "<b>Yes</b> &mdash; by clicking the link"],
     ], caption="Cookies used on %s" % DOMAIN),

     h2("3. Cookies set by gambling operators", "operators"),
     "<p>When you click a link to an operator you leave this site and enter theirs. From that point "
     "the operator&rsquo;s own cookies and privacy policy apply, and we have no control over and no "
     "visibility of them. Operators typically set cookies for session management, marketing "
     "attribution and fraud prevention. Read the privacy policy of any operator before you register "
     "with it.</p>",

     h2("4. What we do not do", "not"),
     "<ul>"
     "<li>We do not run display advertising, so there are no advertising network cookies on this "
     "site.</li>"
     "<li>We do not use cross-site tracking pixels from social networks.</li>"
     "<li>We do not build advertising profiles or sell data to data brokers.</li>"
     "<li>We do not use cookies to identify you personally.</li></ul>",

     h2("5. Managing your choices", "manage"),
     "<p>You can change your mind at any time:</p>",
     "<ul>"
     "<li><b>On this site:</b> clear the <code>ce_consent</code> cookie in your browser and the "
     "choice banner will appear again on your next visit.</li>"
     "<li><b>In your browser:</b> every major browser lets you block or delete cookies. In Chrome, "
     "Settings &rarr; Privacy and security &rarr; Third-party cookies. In Safari, Preferences &rarr; "
     "Privacy. In Firefox, Settings &rarr; Privacy &amp; Security. In Edge, Settings &rarr; Cookies "
     "and site permissions.</li>"
     "<li><b>Private browsing</b> discards cookies at the end of the session.</li></ul>",
     "<p>Blocking strictly necessary cookies may stop parts of the site working correctly. Blocking "
     "analytics cookies has no effect on anything you can see.</p>",

     h2("6. Do Not Track and Global Privacy Control", "dnt"),
     "<p>We honour the Global Privacy Control signal. If your browser sends GPC, we treat that as a "
     "withdrawal of consent to analytics cookies and do not set them.</p>",

     h2("7. Legal basis", "legal"),
     "<p>We set strictly necessary cookies on the basis that they are required to deliver the service "
     "you have asked for. All other cookies are set only with your consent, which you may withdraw at "
     "any time. Personal information collected via cookies is handled in accordance with the Privacy "
     "Act 2020 and our <a href=\"/privacy-policy/\">privacy policy</a>.</p>",

     h2("8. Changes", "changes"),
     "<p>If we add or remove a cookie, this page is updated and the date at the top changes. Where a "
     "new cookie requires consent, we will ask again rather than relying on a previous choice.</p>",

     h2("9. Contact", "contact"),
     "<p>Questions about cookies or anything else privacy-related: "
     "<a href=\"mailto:%s\">%s</a>, or write to %s, %s.</p>"
     % (EMAIL_PRIVACY, EMAIL_PRIVACY, LEGAL, POSTAL),
     "<p><small>Last updated %s.</small></p>" % LEGAL_UPDATED,
    ]
    toc_items = [("What cookies are", "what"), ("The cookies we use", "which"),
                 ("Operator cookies", "operators"), ("What we do not do", "not"),
                 ("Managing your choices", "manage"), ("Do Not Track and GPC", "dnt"),
                 ("Legal basis", "legal"), ("Changes", "changes"), ("Contact", "contact")]
    _legal_page(path, "Cookie Policy &mdash; %s" % NAME, "Cookie Policy",
                "Every cookie this site sets, what it does, how long it lasts and how to turn it "
                "off. There are four, and two of them are optional.",
                "%s cookie policy: the four cookies we set, their purpose and duration, operator "
                "cookies, and how to manage your choices." % NAME,
                secs, toc_items, author="aroha-tainui")


def build():
    build_about()
    build_contact()
    build_authors()
    build_terms()
    build_privacy()
    build_cookies()
