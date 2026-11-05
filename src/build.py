#!/usr/bin/env python3
"""Builds the static website into ../site from the page files in this folder.

Run:  python3 src/build.py
"""
import html, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import site_config as C
from faqs import FAQS
from pages_procedures import PROCEDURES
from pages_conditions import CONDITIONS
from pages_other import OTHER
from pages_guides import GUIDES
from pages_guides2 import GUIDES2
from pages_guides3 import GUIDES3
GUIDES = GUIDES + GUIDES2 + GUIDES3

OUT = os.path.join(os.path.dirname(HERE), "site")
LASTMOD = "2026-11-01"
ALL = PROCEDURES + CONDITIONS + GUIDES + OTHER
BY_SLUG = {p["slug"]: p for p in ALL}

def tel(n):
    d = re.sub(r"\D", "", n)
    return "+44" + d[1:] if d.startswith("0") else d

TOKENS = {
    "NJR": C.NJR, "PHIN": C.PHIN, "DOCTIFY": C.DOCTIFY, "TOPDOCTORS": C.TOPDOCTORS,
    "GMC": C.GMC, "HOSPITAL": C.HOSPITAL, "HOSPITAL_PHONE": C.HOSPITAL_PHONE,
    "HOSPITAL_PHONE_TEL": tel(C.HOSPITAL_PHONE), "SEC_PHONE": C.SEC_PHONE,
    "SEC_PHONE_TEL": tel(C.SEC_PHONE), "SEC_EMAIL": C.SEC_EMAIL, "SECRETARY": C.SECRETARY,
    "BOOK_URL": C.BOOK_URL, "NUFFIELD_HOSPITAL": C.NUFFIELD_HOSPITAL, "MAPS": C.MAPS,
    "RATING_NOTE": C.RATING_NOTE, "GOOGLE_PROFILE": C.GOOGLE_PROFILE, "GOOGLE_REVIEWS": str(C.GOOGLE_REVIEWS), "CLINIC_TIMES": C.CLINIC_TIMES,
    "ADDRESS_INLINE": ", ".join(C.ADDRESS_LINES),
    "ADDRESS_HTML": "<br>".join(C.ADDRESS_LINES),
    "INSURER_LIST": "".join(f"<li>{i}</li>" for i in C.INSURERS),
    "RESEARCHGATE": C.RESEARCHGATE,
    "COOKIES": ("<p>This website uses cookies only if you agree. When you first visit, a banner asks whether you accept Google cookies. If you click Accept, Google Analytics and Google Ads set cookies that tell us how many people visit, which pages they read, whether a visit came from one of our Google adverts, and whether they then clicked to book or call. This helps us improve the website and see whether our adverts are useful. Google does not tell us who you are. If you click Reject, or ignore the banner, no cookies are set. You can change your choice at any time using the \"Cookie settings\" link at the bottom of every page. Google's use of this information is described in <a href=\"https://policies.google.com/technologies/partner-sites\">Google's policy on partner sites</a>.</p>"
                if C.GOOGLE_ADS_ID else "<p>This website does not use cookies.</p>"),
}

def fill(s):
    for k, v in TOKENS.items():
        s = s.replace(f"%{k}%", v)
    # [[...]] marks a fact still to confirm: highlighted in the preview
    s = re.sub(r"\[\[(.+?)\]\]", r'<mark class="todo">[\1]</mark>', s)
    return s

def url(slug):
    return f"{C.BASE_URL}/" if slug == "" else f"{C.BASE_URL}/{slug}/"

PHYSICIAN_ID = f"{C.BASE_URL}/#physician"
PHYSICIAN = {
    "@context": "https://schema.org",
    "@type": "Physician",
    "@id": PHYSICIAN_ID,
    "name": C.NAME,
    "description": "Consultant orthopaedic surgeon specialising in hip and knee replacement, revision surgery and knee arthroscopy, at Nuffield Health Ipswich Hospital.",
    "url": url(""),
    "image": f"{C.BASE_URL}/assets/krishna-boddu-800.jpg",
    "medicalSpecialty": ["Musculoskeletal", "Surgical"],
    "telephone": tel(C.SEC_PHONE),
    "email": C.SEC_EMAIL,
    "address": {"@type": "PostalAddress", "streetAddress": "Nuffield Health Ipswich Hospital, Foxhall Road",
                "addressLocality": "Ipswich", "addressRegion": "Suffolk", "postalCode": "IP4 5SW", "addressCountry": "GB"},
    "hospitalAffiliation": {"@type": "Hospital", "name": C.HOSPITAL, "telephone": tel(C.HOSPITAL_PHONE)},
    "areaServed": ["Ipswich", "Suffolk", "North Essex"],
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": "Monday", "opens": "08:30", "closes": "12:30"}],
    "knowsLanguage": ["en", "hi", "te", "ur"],
    "identifier": {"@type": "PropertyValue", "propertyID": "GMC", "value": C.GMC},
    "sameAs": [C.DOCTIFY, C.TOPDOCTORS, C.NUFFIELD_PROFILE, C.PHIN, C.BUPA, C.NJR, C.LINKEDIN, C.RESEARCHGATE, C.GOOGLE_PROFILE],
}

NAV = [("/#treatments", "Treatments"), ("/#conditions", "Conditions"), ("/fees-insurance/", "Fees and insurance"),
       ("/outcomes-reviews/", "Reviews"), ("/about/", "About")]

def header():
    links = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    banner = ('<div class="preview-banner">Preview for Mr Boddu\'s review. Not yet published.</div>' if C.PREVIEW else "")
    return f"""{banner}<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="/"><span class="brand-name">{C.NAME}</span><span class="brand-sub">Consultant Hip and Knee Surgeon, Ipswich</span></a>
<nav class="main-nav" aria-label="Main">{links}<a class="btn btn-small" href="/contact/">Book an appointment</a></nav>
<details class="mobile-nav"><summary>Menu</summary><nav aria-label="Main menu">{links}<a href="/contact/">Book an appointment</a></nav></details>
</div></header>"""

def footer():
    treat = "".join(f'<li><a href="/{p["slug"]}/">{p["nav"]}</a></li>' for p in PROCEDURES)
    info = "".join(f'<li><a href="/{s}/">{BY_SLUG[s]["nav"]}</a></li>' for s in
                   ["hip-knee-clinic", "fees-insurance", "outcomes-reviews", "your-operation", "gps-physiotherapists", "about", "contact"])
    info = '<li><a href="/#guides">Patient guides</a></li>' + info
    return f"""<footer class="site-footer"><div class="wrap footer-grid">
<div><p class="f-name">{C.NAME}</p><p>MBBS, MS (Orth), MRCSEd, AFRCSI, FRCS (Tr &amp; Orth)<br>Consultant Orthopaedic Surgeon<br>GMC {C.GMC}</p>
<p class="f-links"><a href="{C.DOCTIFY}">Doctify</a> · <a href="{C.TOPDOCTORS}">Top Doctors</a> · <a href="{C.GOOGLE_PROFILE}">Google</a> · <a href="{C.NJR}">NJR</a> · <a href="{C.PHIN}">PHIN</a> · <a href="{C.LINKEDIN}">LinkedIn</a> · <a href="{C.RESEARCHGATE}">ResearchGate</a></p></div>
<div><p class="f-h">Private practice</p><p>{"<br>".join(C.ADDRESS_LINES)}</p><p>Clinic: {C.CLINIC_TIMES}</p><p>Secretary: {C.SECRETARY}<br><a href="tel:{tel(C.SEC_PHONE)}">{C.SEC_PHONE}</a><br><a href="mailto:{C.SEC_EMAIL}">{C.SEC_EMAIL}</a></p></div>
<div><p class="f-h">Treatments</p><ul>{treat}</ul></div>
<div><p class="f-h">Information</p><ul>{info}</ul></div>
</div>
<div class="wrap f-small"><p>This website gives general information and does not replace a consultation. In an emergency call 999; for urgent medical advice call NHS 111.</p>
<p>&copy; 2026 {C.NAME} · <a href="/privacy/">Privacy, cookies and accessibility</a>{' · <a href="/privacy/#cookies" data-cookie-settings>Cookie settings</a>' if C.GOOGLE_ADS_ID else ""}</p></div>
</footer>"""

def cta():
    return f"""<section class="cta-band"><div class="wrap narrow">
<h2>Book a consultation</h2>
<p>I see patients at {C.HOSPITAL}. You can book online, or contact my secretary, {C.SECRETARY}, who can also help with insurance and self-pay questions.</p>
<div class="cta-row"><a class="btn btn-light" href="{C.BOOK_URL}">Book online at Nuffield Health</a><a class="btn btn-outline-light" href="tel:{tel(C.SEC_PHONE)}">Call Daniela on {C.SEC_PHONE}</a></div>
</div></section>"""

def consent_tag():
    if not C.GOOGLE_ADS_ID:
        return ""
    a = lambda v: html.escape(v, quote=True)
    return f'<script src="/consent.js" data-ads="{a(C.GOOGLE_ADS_ID)}" data-book="{a(C.ADS_LABEL_BOOK)}" data-call="{a(C.ADS_LABEL_CALL)}"></script>'

def page_shell(title, description, slug, main, jsonld):
    robots = '<meta name="robots" content="noindex, nofollow">' if C.PREVIEW else ""
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{url(slug)}">
<meta name="msvalidate.01" content="C601E889E0E15D8A85ACE487C4F1D5C2">
{robots}
<meta property="og:type" content="website">
<meta property="og:locale" content="en_GB">
<meta property="og:site_name" content="{C.NAME}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{url(slug)}">
<meta property="og:image" content="{C.BASE_URL}/assets/krishna-boddu-800.jpg">
<meta name="theme-color" content="#12304d">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/styles.css">
{ld}
</head>
<body>
{header()}
<main id="main">
{main}
</main>
{footer()}
{consent_tag()}
</body>
</html>
"""

def crumbs_ld(p):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": url("")},
        {"@type": "ListItem", "position": 2, "name": p["nav"], "item": url(p["slug"])}]}

def render_page(p):
    clinical = p["group"] in ("treatments", "conditions", "guides")
    parts = [f"""<div class="page-head"><div class="wrap narrow">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span aria-hidden="true">›</span> <span aria-current="page">{p["nav"]}</span></nav>
<h1>{p["h1"]}</h1>
<p class="lead">{fill(p["lead"])}</p>
</div></div>
<div class="wrap narrow content">"""]
    if p.get("photo"):
        parts.append('<figure class="portrait"><img src="/assets/krishna-boddu-480.jpg" srcset="/assets/krishna-boddu-480.jpg 480w, /assets/krishna-boddu-800.jpg 800w" sizes="240px" width="480" height="600" alt="Mr Krishna Boddu"></figure>')
    if p.get("glance"):
        rows = "".join(f"<div><dt>{k}</dt><dd>{fill(v)}</dd></div>" for k, v in p["glance"])
        parts.append(f'<aside class="glance" aria-label="At a glance"><p class="glance-h">At a glance</p><dl>{rows}</dl></aside>')
    parts.append(fill(p["body"]))
    if clinical:
        reviewed, reviewed_iso = p.get("reviewed", (C.REVIEWED, C.REVIEWED_ISO))
        parts.append(fill(f'<p class="reviewed">Written and reviewed by {C.NAME} FRCS (Tr &amp; Orth), consultant orthopaedic surgeon, GMC {C.GMC}. Last reviewed: {reviewed}.</p>'))
    faq = FAQS.get(p["slug"])
    if faq:
        qa = "".join(f'<h3>{q}</h3><p>{fill(a)}</p>' for q, a in faq)
        parts.append(f'<section class="faq" id="questions"><h2>Common questions</h2>{qa}</section>')
    if p.get("sources"):
        items = "".join(f"<li>{s}</li>" for s in p["sources"])
        parts.append(fill(f'<section class="sources"><h2>Sources</h2><ul>{items}</ul></section>'))
    if p.get("related"):
        items = "".join(f'<li><a href="/{s}/">{BY_SLUG[s]["nav"]}</a></li>' for s in p["related"])
        parts.append(f'<nav class="related" aria-label="Related pages"><h2>Related pages</h2><ul>{items}</ul></nav>')
    parts.append("</div>")
    if not p.get("nocta"):
        parts.append(cta())
    jsonld = [PHYSICIAN, crumbs_ld(p)]
    if clinical:
        t, name = p["about"]
        mwp = {"@context": "https://schema.org", "@type": "MedicalWebPage", "name": p["h1"], "url": url(p["slug"]),
               "about": {"@type": t, "name": name}, "author": {"@id": PHYSICIAN_ID}, "reviewedBy": {"@id": PHYSICIAN_ID},
               "inLanguage": "en-GB", "lastReviewed": reviewed_iso}
        jsonld.append(mwp)
    if faq:
        jsonld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", fill(a))}}
            for q, a in faq]})
    return page_shell(p["title"], p["description"], p["slug"], "\n".join(parts), jsonld)

def card(p):
    return f'<a class="card" href="/{p["slug"]}/"><h3>{p["nav"]}</h3><p>{p["card"]}</p><span class="more" aria-hidden="true">Read more →</span></a>'

def render_home():
    treat = "".join(card(p) for p in PROCEDURES)
    cond = "".join(card(p) for p in CONDITIONS + [BY_SLUG["hip-knee-clinic"]])
    guides = "".join(card(p) for p in GUIDES)
    insurers = "".join(f"<li>{i}</li>" for i in C.INSURERS)
    main = f"""<section class="hero"><div class="wrap hero-grid">
<div class="hero-text">
<p class="eyebrow">Private practice at {C.HOSPITAL}</p>
<h1>{C.NAME}<span>Consultant Hip and Knee Surgeon in Ipswich</span></h1>
<p class="lead">Assessment and surgery for hip and knee arthritis, meniscal tears and problem joint replacements, for patients across Suffolk and north Essex.</p>
<div class="cta-row"><a class="btn" href="{C.BOOK_URL}">Book online</a><a class="btn btn-outline" href="/contact/">Contact my secretary</a></div>
<ul class="trust">
<li><strong>More than 1,000</strong><span>hip and knee replacements, with outcomes <a href="/outcomes-reviews/#hip-results">better than expected on the National Joint Registry</a></span></li>
<li><strong>4.96 out of 5</strong><span>from 124 reviews on Doctify</span></li>
<li><strong>FRCS (Tr &amp; Orth)</strong><span>fellowship-trained in hip and knee replacement</span></li>
<li><strong>NHS consultant</strong><span>at Ipswich Hospital</span></li>
</ul>
</div>
<div class="hero-photo"><img src="/assets/krishna-boddu-800.jpg" srcset="/assets/krishna-boddu-480.jpg 480w, /assets/krishna-boddu-800.jpg 800w" sizes="(max-width: 820px) 70vw, 400px" width="800" height="1000" alt="Mr Krishna Boddu, consultant orthopaedic surgeon"></div>
</div></section>

<section class="intro"><div class="wrap narrow">
<p>I am a consultant orthopaedic surgeon at Ipswich Hospital, and I see private patients at {C.HOSPITAL}. I look after people with hip and knee problems from their first assessment through to surgery and recovery. My practice is evidence-based: many people do not need an operation, and I will tell you if that is the case for you.</p>
</div></section>

<section class="section" id="treatments"><div class="wrap">
<h2>Treatments</h2>
<div class="cards">{treat}</div>
</div></section>

<section class="section alt" id="conditions"><div class="wrap">
<h2>Conditions I treat</h2>
<div class="cards">{cond}</div>
</div></section>

<section class="section" id="guides"><div class="wrap">
<h2>Patient guides</h2>
<div class="cards">{guides}</div>
</div></section>

<section class="section alt"><div class="wrap">
<h2>What you can expect</h2>
<div class="points">
<div><h3>Honest, evidence-based advice</h3><p>I recommend surgery only when the likely benefits clearly outweigh the risks for you, and I explain both in plain language.</p></div>
<div><h3>Specialist training</h3><p>Fellowship training in primary and revision hip and knee replacement in Montreal and at King's College Hospital, London, and more than 1,000 hip and knee replacements.</p></div>
<div><h3>One consultant throughout</h3><p>I look after you from your first appointment through to your follow-up after surgery.</p></div>
<div><h3>Results you can check</h3><p>My joint replacements are recorded on the National Joint Registry, and my private practice is reported to PHIN. See <a href="/outcomes-reviews/">outcomes and reviews</a>.</p></div>
</div>
</div></section>

<section class="section"><div class="wrap">
<h2>What patients say</h2>
<div class="ratings">
<a class="rating" href="{C.DOCTIFY}"><span class="score">4.96<small>/5</small></span><span>from 124 reviews on Doctify</span></a>
<a class="rating" href="{C.TOPDOCTORS}"><span class="score">5.0<small>/5</small></span><span>from 32 reviews on Top Doctors</span></a>
<a class="rating" href="{C.PHIN}"><span class="score">96%</span><span>of 76 patients surveyed by PHIN would recommend me</span></a>
</div>
<p class="small">Ratings {C.RATING_NOTE}, collected and published independently by Doctify, Top Doctors and PHIN. You can also <a href="{C.GOOGLE_PROFILE}">read my {C.GOOGLE_REVIEWS} reviews on Google</a>.</p>
</div></section>

<section class="section alt"><div class="wrap two-col">
<div>
<h2>Fees and insurance</h2>
<p>New consultations for self-paying patients are &pound;200, and follow-ups &pound;100. For surgery, Nuffield Health Ipswich gives you a fixed-price package after your consultation.</p>
<p>I am recognised by:</p>
<ul class="insurers">{insurers}</ul>
<p><a href="/fees-insurance/">Fees and insurance in detail</a></p>
</div>
<div>
<h2>Where I see patients</h2>
<figure class="wide"><img src="/assets/nuffield-ipswich-800.jpg" srcset="/assets/nuffield-ipswich-800.jpg 800w, /assets/nuffield-ipswich-1360.jpg 1360w" sizes="(max-width: 820px) 100vw, 560px" width="800" height="398" alt="Nuffield Health Ipswich Hospital entrance on Foxhall Road" loading="lazy"></figure>
<p>{", ".join(C.ADDRESS_LINES)}. <a href="{C.MAPS}">Get directions</a></p>
</div>
</div></section>
{cta()}"""
    return page_shell("Mr Krishna Boddu | Hip and Knee Surgeon in Ipswich, Suffolk",
                      "Private hip and knee replacement, including robotic-assisted and partial knee replacement, and meniscal surgery at Nuffield Health Ipswich with consultant orthopaedic surgeon Mr Krishna Boddu.",
                      "", main, [PHYSICIAN])

def render_404():
    main = """<div class="page-head"><div class="wrap narrow"><h1>Page not found</h1>
<p class="lead">Sorry, that page does not exist. It may have moved.</p></div></div>
<div class="wrap narrow content"><p><a href="/">Go to the home page</a> or <a href="/contact/">book an appointment</a>.</p></div>"""
    return page_shell("Page not found | Mr Krishna Boddu", "Page not found.", "404", main, [])

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#12304d"/><text x="32" y="42" font-family="Georgia, serif" font-size="28" fill="#fff" text-anchor="middle">KB</text></svg>"""

G = "https://*.google-analytics.com https://*.analytics.google.com https://www.googletagmanager.com https://*.googletagmanager.com https://www.googleadservices.com https://googleads.g.doubleclick.net https://*.doubleclick.net https://www.google.com https://www.google.co.uk"
CSP = ("default-src 'self'; img-src 'self' data:" + (" " + G if C.GOOGLE_ADS_ID else "") +
       "; style-src 'self'; script-src 'self'" + (" https://www.googletagmanager.com https://www.googleadservices.com https://googleads.g.doubleclick.net" if C.GOOGLE_ADS_ID else "") +
       ("; connect-src 'self' " + G + "; frame-src https://td.doubleclick.net https://www.googletagmanager.com" if C.GOOGLE_ADS_ID else "") +
       "; frame-ancestors 'none'; base-uri 'self'; form-action 'none'")
NETLIFY = """[build]
  publish = "site"

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "DENY"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "camera=(), microphone=(), geolocation=(), interest-cohort=()"
    Content-Security-Policy = "{CSP}"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
"""

def main():
    os.makedirs(OUT, exist_ok=True)
    for p in ALL:
        d = os.path.join(OUT, p["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w") as f:
            f.write(render_page(p))
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(render_home())
    with open(os.path.join(OUT, "404.html"), "w") as f:
        f.write(render_404())
    shutil.copy(os.path.join(HERE, "styles.css"), os.path.join(OUT, "styles.css"))
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)
    js = os.path.join(OUT, "consent.js")
    if C.GOOGLE_ADS_ID:
        shutil.copy(os.path.join(HERE, "consent.js"), js)
    elif os.path.exists(js):
        os.remove(js)
    with open(os.path.join(OUT, "favicon.svg"), "w") as f:
        f.write(FAVICON)
    with open(os.path.join(os.path.dirname(OUT), "netlify.toml"), "w") as f:
        f.write(NETLIFY.replace("{CSP}", CSP))  # repo root: Netlify publishes the site/ folder
    urls = [(url(""), LASTMOD)] + [(url(p["slug"]), p.get("reviewed", (None, LASTMOD))[1]) for p in ALL]
    sm = "".join(f"<url><loc>{u}</loc><lastmod>{m}</lastmod></url>" for u, m in urls)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {C.BASE_URL}/sitemap.xml\n")
    print(f"Built {len(urls)} pages into {OUT}")

if __name__ == "__main__":
    main()
