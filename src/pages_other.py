# Non-clinical and practice pages. %TOKENS% are filled from site_config.py at build time.

OTHER = [
{
"slug": "about",
"nav": "About",
"group": "practice",
"title": "About Mr Krishna Boddu, Consultant Hip and Knee Surgeon | Ipswich",
"description": "Mr Krishna Boddu FRCS (Tr & Orth): consultant orthopaedic surgeon at Ipswich Hospital and Nuffield Health Ipswich, fellowship-trained in primary and revision hip and knee replacement.",
"h1": "About Mr Krishna Boddu",
"lead": "I am a consultant orthopaedic surgeon specialising in hip and knee replacement, including complex and revision surgery. I work at Ipswich Hospital in the NHS and see private patients at Nuffield Health Ipswich Hospital.",
"photo": True,
"body": """
<h2>My approach</h2>
<p>My practice is evidence-based. I recommend surgery only when the likely benefits clearly outweigh the risks for you, and I explain both in plain language. Many people with hip and knee problems do well without an operation, and I will tell you if that is the case for you. If you do have surgery with me, I will look after you from your first appointment through to your follow-up after the operation.</p>

<h2>Training and experience</h2>
<ul>
<li>Postgraduate orthopaedic training at PGIMER, Chandigarh, India</li>
<li>Research in orthopaedic biomechanics at Imperial College London</li>
<li>Registrar training in trauma and orthopaedic surgery in South East London</li>
<li>Fellowships in primary and revision hip and knee replacement at Maisonneuve-Rosemont Hospital, Montreal, and King's College Hospital, London</li>
<li>NHS consultant orthopaedic surgeon since 2015</li>
<li>Consultant at King's College Hospital NHS Foundation Trust, London, before moving to Ipswich Hospital (East Suffolk and North Essex NHS Foundation Trust) in 2022</li>
<li>More than 1,000 hip and knee replacements, with my operations recorded on the <a href="%NJR%">National Joint Registry</a></li>
<li>Trained in Mako robotic-assisted hip and knee replacement</li>
</ul>

<h2>Qualifications</h2>
<p>MBBS, MS (Orth), MRCSEd, AFRCSI, FRCS (Tr &amp; Orth), EBOT (Fellow of the European Board of Orthopaedics and Traumatology). GMC registration number %GMC%.</p>

<h2>Research, artificial intelligence and teaching</h2>
<ul>
<li>Co-founder of IMERA.AI, a company developing artificial intelligence for medical imaging, with a research interest in using AI to improve orthopaedic care</li>
<li>Trainer of orthopaedic registrars in the East of England</li>
<li>Faculty member on FRCS (Tr &amp; Orth) courses at King's College Hospital</li>
<li>25 research publications (<a href="%RESEARCHGATE%">see them on ResearchGate</a>)</li>
<li>Reviewer for the Bone &amp; Joint Journal</li>
<li>Research grants from ARC and Hammersmith Hospitals</li>
</ul>

<h2>Professional memberships</h2>
<ul>
<li>Fellow of the Royal College of Surgeons of Edinburgh</li>
<li>British Orthopaedic Association</li>
<li>British Hip Society</li>
<li>British Medical Association</li>
</ul>

<h2>Languages</h2>
<p>English, Hindi, Telugu and Urdu.</p>

<h2>Declaration of interests</h2>
<p>I have no shares or financial interest in Nuffield Health, its hospitals or the equipment used in them, and no paid advisory role with them. I am a co-founder of IMERA.AI, a company developing artificial intelligence for medical imaging.</p>
""",
"related": ["outcomes-reviews", "hip-knee-clinic", "fees-insurance", "contact"],
},
{
"slug": "hip-knee-clinic",
"nav": "Hip and knee clinic",
"group": "practice",
"card": "Assessment, scans and a clear plan, with or without surgery.",
"title": "Hip and Knee Pain Clinic in Ipswich | Mr Krishna Boddu",
"description": "Private hip and knee clinic at Nuffield Health Ipswich Hospital: assessment, X-rays and scans, and a clear treatment plan with consultant surgeon Mr Krishna Boddu.",
"h1": "Hip and knee clinic",
"lead": "My clinic at Nuffield Health Ipswich Hospital is for adults with hip or knee pain, stiffness, swelling or injury, and for anyone with a problem with an existing hip or knee replacement.",
"about": ("MedicalClinic", "Hip and knee clinic"),
"body": """
<h2>Who I see</h2>
<ul>
<li>Hip and knee arthritis</li>
<li>Meniscal tears and knee locking</li>
<li>Painful, unstable or worn hip and knee replacements</li>
<li>Second opinions about hip and knee surgery</li>
</ul>

<h2>Before your appointment</h2>
<ul>
<li>If you are paying for yourself, you can book directly; a letter from your GP is helpful but not essential.</li>
<li>If you are insured, most insurers need a GP referral and a pre-authorisation number. Please give the number to Daniela when you book.</li>
<li>Bring a list of your medicines, any scan reports and letters, and wear or bring shorts so that I can examine you properly.</li>
</ul>

<h2>At your appointment</h2>
<p>I will ask about your symptoms and how they affect your life, examine you and review any scans. X-rays are taken at the hospital, often on the same day. If you need an MRI or CT scan, I will arrange it. We will agree a plan together, and I will write to you and your GP afterwards.</p>

<h2>Treatments I may recommend</h2>
<ul>
<li>Exercise and physiotherapy, with a local physiotherapist</li>
<li>Advice on weight, activity and pain relief</li>
<li>Joint injections, where they are likely to help</li>
<li>Surgery, when the benefits clearly outweigh the risks</li>
</ul>

<h2>Clinic times</h2>
<p>My clinic at %HOSPITAL% runs every %CLINIC_TIMES%. Daniela will offer you the next available appointment.</p>
""",
"sources": ['<a href="https://www.nice.org.uk/guidance/ng226">NICE guideline NG226: Osteoarthritis in over 16s: diagnosis and management (2022)</a>'],
"related": ["fees-insurance", "contact", "second-opinion", "your-operation"],
},
{
"slug": "fees-insurance",
"nav": "Fees and insurance",
"group": "practice",
"title": "Fees and Insurance | Mr Krishna Boddu, Ipswich",
"description": "Consultation fees, recognised insurers (Bupa, AXA Health, Aviva, Vitality, WPA, Allianz, Healix) and self-pay surgery packages at Nuffield Health Ipswich.",
"h1": "Fees and insurance",
"lead": "My fees are below. If you are paying for yourself, Nuffield Health Ipswich gives you a fixed-price package for surgery after your consultation, so you know the cost before you decide.",
"body": """
<h2>Fees for self-paying patients</h2>
<table>
<thead><tr><th scope="col">Appointment</th><th scope="col">Fee</th></tr></thead>
<tbody>
<tr><td>New consultation</td><td>&pound;200</td></tr>
<tr><td>Follow-up consultation</td><td>&pound;100</td></tr>
<tr><td>Injections given in clinic</td><td>&pound;100, in addition to the consultation fee, plus hospital fees charged separately by Nuffield Health Ipswich</td></tr>
<tr><td>X-rays and scans</td><td>Charged separately by Nuffield Health Ipswich</td></tr>
<tr><td>Surgery</td><td>A fixed-price package from Nuffield Health Ipswich, quoted after your consultation</td></tr>
</tbody>
</table>
<p>Daniela handles my billing and can answer any questions about fees.</p>

<h2>Insurance</h2>
<p>I am recognised by:</p>
<ul class="insurers">%INSURER_LIST%</ul>
<p>I am a <strong>Bupa fee-assured</strong> consultant, so Bupa members pay no shortfall on my fees for eligible treatment (your policy excess may still apply). If your insurer is not listed, please ask Daniela.</p>
<ol>
<li>Check that your policy covers outpatient consultations and the treatment you may need.</li>
<li>Ask your GP for a referral letter if your insurer needs one.</li>
<li>Call your insurer for a pre-authorisation number, and give it to Daniela when you book.</li>
</ol>

<h2>Paying for yourself</h2>
<p>Nuffield Health Ipswich offers fixed-price packages for surgery, which usually include the hospital stay, the surgeon's and anaesthetist's fees and follow-up care; your quote will set out exactly what is included. Finance options are also available through Nuffield Health. See <a href="%NUFFIELD_HOSPITAL%">Nuffield Health Ipswich Hospital</a>.</p>
""",
"related": ["private-hip-and-knee-replacement-cost", "hip-knee-clinic", "contact", "knee-replacement", "hip-replacement"],
},
{
"slug": "outcomes-reviews",
"nav": "Outcomes and reviews",
"group": "practice",
"title": "Outcomes and Patient Reviews | Mr Krishna Boddu, Ipswich",
"description": "Independent outcome data from the National Joint Registry and PHIN, and verified patient reviews on Doctify and Top Doctors, for Mr Krishna Boddu.",
"h1": "Outcomes and patient reviews",
"lead": "You can check my results and what patients say through independent organisations that collect and publish them.",
"body": """
<h2>National Joint Registry</h2>
<p>Every hip and knee replacement I perform is recorded on the National Joint Registry, which publishes data for each surgeon, including whether their results are within the expected range. <a href="%NJR%">See my National Joint Registry profile</a>.</p>

<h3 id="hip-results">My hip replacement results</h3>
<figure><img src="/assets/njr-hip-funnel-2026.png" width="830" height="835" alt="National Joint Registry funnel plot of revision rates for hip replacements over the last ten years. Mr Boddu's result, a black dot, sits at a standardised revision ratio of about 0.3, well below the expected level of 1." loading="lazy"><figcaption>National Joint Registry data for my hip replacements over the last ten years (2026 report). The black dot is my result.</figcaption></figure>
<p>This chart compares how often hip replacements need to be redone (a "revision") for every surgeon in the registry:</p>
<ul>
<li>Each light blue dot is another surgeon.</li>
<li>The green line at 1 is the expected number of revisions, after allowing for patients' age and health. A dot above the line means more revisions than expected, and below it means fewer.</li>
<li>My black dot is at about 0.3, which means my patients have needed fewer than a third of the revisions expected.</li>
</ul>
<p>In other words, the survival of my hip replacements is better than expected in the National Joint Registry.</p>

<h2>Private Healthcare Information Network (PHIN)</h2>
<p>PHIN publishes information about consultants in private practice. On PHIN, 96% of 76 patients surveyed said they were extremely or very likely to recommend me (profile updated October 2026). <a href="%PHIN%">See my PHIN profile</a>.</p>

<h2>Patient reviews</h2>
<div class="ratings">
<a class="rating" href="%DOCTIFY%"><span class="score">4.96<small>/5</small></span><span>from 124 reviews on Doctify</span></a>
<a class="rating" href="%TOPDOCTORS%"><span class="score">5.0<small>/5</small></span><span>from 32 reviews on Top Doctors</span></a>
<a class="rating" href="%GOOGLE_PROFILE%"><span class="score">%GOOGLE_REVIEWS%</span><span>reviews on Google</span></a>
</div>
<p class="small">Ratings %RATING_NOTE%. Reviews are collected and published independently by Doctify, Top Doctors and Google.</p>
""",
"related": ["about", "hip-replacement", "knee-replacement", "contact"],
},
{
"slug": "your-operation",
"nav": "Your operation",
"group": "practice",
"title": "Preparing for and Recovering from Hip or Knee Surgery | Mr Krishna Boddu",
"description": "What to expect before, during and after hip or knee replacement at Nuffield Health Ipswich: preparation, your hospital stay, recovery milestones and warning signs.",
"h1": "Your operation: before, during and after",
"lead": "Knowing what to expect makes surgery easier. This page covers the usual steps for hip and knee replacement at Nuffield Health Ipswich Hospital. I will tailor the advice to you.",
"body": """
<h2>Before your operation</h2>
<ul>
<li><strong>Pre-operative assessment:</strong> a nurse at the hospital checks your health, takes blood tests and swabs, and reviews your medicines, including any blood thinners.</li>
<li><strong>Get fit for surgery:</strong> keep active, do the exercises your physiotherapist gives you, and stop smoking if you smoke. Both help you recover faster.</li>
<li><strong>Prepare your home:</strong> clear trip hazards, put everyday items within easy reach and arrange help for the first week or two.</li>
</ul>

<h2>In hospital</h2>
<p>Most people have a spinal anaesthetic, sometimes with sedation. Physiotherapists will help you walk on the day of surgery or the next morning, and teach you your exercises. You can go home when you are comfortable, walking safely with crutches or sticks, and managing stairs if you need to.</p>

<h2>Recovery milestones</h2>
<table>
<thead><tr><th scope="col">When</th><th scope="col">What to expect</th></tr></thead>
<tbody>
<tr><td>First 2 weeks</td><td>Walking with crutches, doing your exercises several times a day, wound check by a nurse at the hospital, and removal of clips after a knee replacement</td></tr>
<tr><td>About 6 weeks</td><td>Follow-up with me; many people walk without crutches and can start driving</td></tr>
<tr><td>About 3 months</td><td>Most daily activities and many hobbies; heavier work may be possible</td></tr>
<tr><td>Up to 1 year</td><td>Continued improvement, especially after a knee replacement</td></tr>
</tbody>
</table>

<div class="callout warn">
<p><strong>Get medical advice straight away if you notice:</strong></p>
<ul>
<li>A wound that becomes red, hot or swollen, or leaks fluid</li>
<li>A fever or feeling unwell</li>
<li>Pain or swelling in your calf</li>
<li>Chest pain or breathlessness</li>
</ul>
<p>In an emergency, call 999.</p>
</div>

<h2>Common questions</h2>
<details><summary>When can I drive?</summary><p>Usually after about 6 weeks, once you can safely make an emergency stop. Tell your insurer that you have had surgery.</p></details>
<details><summary>When can I fly?</summary><p>Short flights are usually fine after about 6 weeks. For long-haul flights, it is usually best to wait about 3 months because of the risk of blood clots. Please ask me about your own plans.</p></details>
<details><summary>Will I be able to kneel after a knee replacement?</summary><p>Kneeling will not damage your new knee, but many people find it uncomfortable. It often gets easier with time.</p></details>
<details><summary>Will my joint replacement set off airport scanners?</summary><p>It may. You do not need a card or letter; tell the security staff that you have a joint replacement.</p></details>
""",
"sources": ['<a href="https://www.nice.org.uk/guidance/ng157">NICE guideline NG157: Joint replacement (primary): hip, knee and shoulder (2020)</a>'],
"related": ["hip-replacement-recovery", "knee-replacement-recovery", "hip-replacement", "knee-replacement", "contact"],
},
{
"slug": "gps-physiotherapists",
"nav": "For GPs and physiotherapists",
"group": "practice",
"title": "For GPs and Physiotherapists | Mr Krishna Boddu, Ipswich",
"description": "How to refer patients privately to Mr Krishna Boddu, consultant hip and knee surgeon at Nuffield Health Ipswich: conditions treated, referral details and contacts.",
"h1": "For GPs and physiotherapists",
"lead": "Thank you for considering a referral. I see adults with hip and knee problems privately at Nuffield Health Ipswich Hospital, and I write back after every consultation.",
"body": """
<h2>Who I see</h2>
<ul>
<li>Hip and knee osteoarthritis, including assessment for partial knee replacement</li>
<li>Painful, unstable, stiff or worn hip and knee replacements, wherever the original surgery was done</li>
<li>Meniscal tears, including repair in suitable patients</li>
<li>Second opinions about hip and knee surgery</li>
</ul>

<h2>How to refer</h2>
<p>Please send a referral letter to my secretary, %SECRETARY%, by email at <a href="mailto:%SEC_EMAIL%">%SEC_EMAIL%</a> or by post to %ADDRESS_INLINE%. It helps to include:</p>
<ul>
<li>A short history and examination findings</li>
<li>Current medicines and relevant conditions</li>
<li>Any X-ray or scan reports</li>
<li>The patient's insurer, if they are insured</li>
</ul>
<p>To refer a patient or book an appointment, call Nuffield Health Ipswich on <a href="tel:%HOSPITAL_PHONE_TEL%">%HOSPITAL_PHONE%</a>, or book online through <a href="%BOOK_URL%">my Nuffield Health profile</a>.</p>

<h2>Urgent problems</h2>
<p>Patients with a suspected infected joint replacement, a locked knee or a suspected fracture should be referred through the usual urgent routes.</p>

<h2>Education evenings</h2>
<p>I am planning education evenings on hip and knee problems for GPs and physiotherapists in Suffolk. If you would like to be invited, please ask Daniela to add you to the list.</p>
""",
"related": ["hip-knee-clinic", "knee-arthritis", "problem-joint-replacement", "contact"],
},
{
"slug": "contact",
"nav": "Contact",
"group": "practice",
"title": "Book an Appointment | Mr Krishna Boddu, Nuffield Health Ipswich",
"description": "Book a private hip or knee consultation with Mr Krishna Boddu at Nuffield Health Ipswich Hospital: online booking, phone and email.",
"h1": "Book an appointment",
"lead": "I see patients at Nuffield Health Ipswich Hospital. You can book online, or contact my secretary, Daniela Capaldo, who can also help with insurance and self-pay questions.",
"nocta": True,
"body": """
<div class="choices">
<div class="choice">
<h2>Book online</h2>
<p>Choose an appointment through Nuffield Health's booking page.</p>
<p><a class="btn" href="%BOOK_URL%">Book online at Nuffield Health</a></p>
</div>
<div class="choice">
<h2>Call or email Daniela</h2>
<p>%SECRETARY%, my secretary</p>
<p><a href="tel:%SEC_PHONE_TEL%">%SEC_PHONE%</a><br><a href="mailto:%SEC_EMAIL%">%SEC_EMAIL%</a></p>
</div>
</div>

<h2>Where I see patients</h2>
<figure class="wide"><img src="/assets/nuffield-ipswich-800.jpg" srcset="/assets/nuffield-ipswich-800.jpg 800w, /assets/nuffield-ipswich-1360.jpg 1360w" sizes="(max-width: 820px) 100vw, 760px" width="800" height="398" alt="Nuffield Health Ipswich Hospital entrance on Foxhall Road" loading="lazy"></figure>
<p><strong>Clinic:</strong> %CLINIC_TIMES%</p>
<p>%ADDRESS_HTML%<br>Nuffield Health Ipswich bookings: <a href="tel:%HOSPITAL_PHONE_TEL%">%HOSPITAL_PHONE%</a><br><a href="%MAPS%">Get directions</a></p>

<h2>Before you book</h2>
<ul>
<li>If you are insured, please have your policy number and pre-authorisation number ready. See <a href="/fees-insurance/">fees and insurance</a>.</li>
<li>If you are paying for yourself, a letter from your GP is helpful but not essential.</li>
</ul>

<div class="callout"><p>This service is not for emergencies. If you need urgent medical help, call NHS 111, or 999 in an emergency.</p></div>
""",
"related": ["fees-insurance", "hip-knee-clinic", "your-operation", "about"],
},
{
"slug": "privacy",
"nav": "Privacy, cookies and accessibility",
"group": "legal",
"title": "Privacy, Cookies and Accessibility | Mr Krishna Boddu",
"description": "How this website handles your information, its use of cookies, and its accessibility.",
"h1": "Privacy, cookies and accessibility",
"lead": "This website is designed to collect as little information about you as possible.",
"nocta": True,
"body": """
<h2>Privacy</h2>
<p>This website is run by Mr Krishna Boddu, who is the data controller for it. The website has no forms and does not ask for your personal or medical details.</p>
<ul>
<li><strong>Hosting:</strong> our hosting provider, Netlify, records technical information such as IP addresses in server logs to keep the site secure. We do not use this information to identify you.</li>
<li><strong>Contacting us:</strong> if you call or email Daniela, we use your details only to arrange and provide your care.</li>
</ul>
<p>You have the right to ask what information we hold about you, and to have it corrected or deleted. Please contact Daniela on %SEC_PHONE% or at <a href="mailto:%SEC_EMAIL%">%SEC_EMAIL%</a>. If you are unhappy with how we handle your information, you can complain to the <a href="https://ico.org.uk/">Information Commissioner's Office</a>.</p>

<h2 id="cookies">Cookies</h2>
%COOKIES%
<p>Links to other websites, such as Nuffield Health's booking page, Doctify and Top Doctors, are covered by those websites' own privacy and cookie policies.</p>

<h2>Accessibility</h2>
<p>This website aims to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at level AA. You should be able to zoom to 200% without losing content, navigate using a keyboard or screen reader, and read all text clearly. If you have difficulty using any part of the site, or need information in another format, please contact Daniela.</p>

<h2>Medical information</h2>
<p>The information on this website is general and does not replace a consultation. It is written and reviewed by Mr Krishna Boddu.</p>
""",
"related": ["contact", "about"],
},
]
