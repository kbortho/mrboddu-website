# Patient guides: pages that answer the questions patients type into Google.
# Clinical pages: they carry the "written and reviewed by" line and MedicalWebPage markup.
from pages_procedures import (NICE_157, NICE_226, NJR_REPORTS, EVANS_HIP, EVANS_KNEE, BESWICK,
                              TOPKAT, LIDDLE, WILSON, GILL_ZUK)

REVIEWED_GUIDES = "3 November 2026"
REVIEWED_GUIDES_ISO = "2026-11-03"

WARNING_SIGNS = """
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
"""

NHS_KNEE_REC = '<a href="https://www.nhs.uk/conditions/knee-replacement/recovery/">NHS: Knee replacement recovery</a>'
NHS_HIP_REC = '<a href="https://www.nhs.uk/conditions/hip-replacement/recovery/">NHS: Hip replacement recovery</a>'
KORFITSEN = '<a href="https://doi.org/10.2340/17453674.2023.11958">Korfitsen CB et al. Hip precautions after posterior-approach total hip arthroplasty among patients with primary hip osteoarthritis do not influence early recovery: a systematic review and meta-analysis of randomized and non-randomized studies with 8,835 patients. Acta Orthop 2023;94:141&ndash;51.</a>'
NUFFIELD_PRICES = '<a href="%NUFFIELD_HOSPITAL%">Nuffield Health Ipswich Hospital: treatments and prices</a>'

GUIDES = [
{
"slug": "knee-replacement-recovery",
"nav": "Knee replacement recovery",
"group": "guides",
"card": "What to expect week by week, from the hospital to a year after surgery.",
"title": "Knee Replacement Recovery Week by Week | Mr Krishna Boddu, Ipswich",
"description": "A week-by-week guide to recovery after knee replacement: walking, exercises, swelling, sleep, driving, work and sport. From consultant knee surgeon Mr Krishna Boddu.",
"h1": "Knee replacement recovery: week by week",
"lead": "Recovery from a knee replacement takes time, and the hard work you put into your exercises makes a real difference. This guide shows what most people can expect. Everyone recovers at their own pace, and I will tailor the advice to you.",
"about": ("MedicalProcedure", "Total knee replacement"),
"reviewed": (REVIEWED_GUIDES, REVIEWED_GUIDES_ISO),
"body": """
<h2>In hospital: the first 1 to 2 days</h2>
<ul>
<li>The physiotherapists will help you stand and walk with a frame or crutches, usually on the day of surgery or the next morning.</li>
<li>They will teach you exercises to bend and straighten the knee, and how to manage stairs.</li>
<li>Most people go home after 1 to 2 nights, once they are comfortable and walking safely.</li>
</ul>

<h2>Weeks 1 to 2</h2>
<ul>
<li>Do your exercises several times a day. Getting the knee fully straight, and bending it a little more each day, is the most important part of recovery.</li>
<li>Take your painkillers regularly, especially before exercises, so that you can do them properly.</li>
<li>Swelling and bruising are normal. Rest with your leg raised and use a cold pack wrapped in a towel for 15 to 20 minutes at a time.</li>
<li>Walk short distances around the house, and a little further each day.</li>
<li>At about 2 weeks, your wound will be checked and your clips removed, usually by a nurse at the hospital.</li>
</ul>

<h2>Weeks 2 to 6</h2>
<ul>
<li>Most people walk further and more confidently, and may move from crutches to one stick.</li>
<li>Night-time aching and poor sleep are common in these weeks. They usually improve.</li>
<li>Keep working on bending the knee. Your physiotherapist will check your progress.</li>
<li>At about 6 weeks, I will see you for a follow-up appointment.</li>
</ul>

<h2>Weeks 6 to 12</h2>
<ul>
<li>Many people walk without crutches or sticks.</li>
<li>Most people can drive after about 6 weeks, once they can safely make an emergency stop. Tell your insurer that you have had surgery.</li>
<li>Office work is often possible from about 6 weeks. Heavier or physical work may take around 3 months.</li>
<li>Gentle swimming, an exercise bike and walking are good ways to build strength.</li>
</ul>

<h2>3 to 12 months</h2>
<ul>
<li>Most people are back to most daily activities and many hobbies by about 3 months, such as golf, cycling, bowls and dancing.</li>
<li>Some swelling, warmth and stiffness can last for several months. This is normal.</li>
<li>The knee keeps improving for up to a year. Kneeling will not damage your new knee, but many people find it uncomfortable at first.</li>
</ul>

<h2>Tips for a good recovery</h2>
<ul>
<li><strong>Exercises:</strong> little and often is better than a long session once a day. See the <a href="/knee-replacement-exercises/">knee exercises, with diagrams</a>.</li>
<li><strong>Stairs:</strong> go up with your good leg first and down with your operated leg first.</li>
<li><strong>Pain:</strong> some discomfort during exercises is expected, but tell us if pain is getting worse rather than better.</li>
<li><strong>Before surgery:</strong> getting fitter, strengthening your thigh muscles and preparing your home all help. See <a href="/your-operation/">your operation</a>.</li>
</ul>
""" + WARNING_SIGNS,
"sources": [NICE_157, NHS_KNEE_REC],
"related": ["knee-replacement-exercises", "pain-after-knee-replacement", "swelling-after-knee-replacement", "sleeping-after-hip-or-knee-replacement", "clicking-or-numbness-after-knee-replacement"],
},
{
"slug": "hip-replacement-recovery",
"nav": "Hip replacement recovery",
"group": "guides",
"card": "What to expect week by week, from the hospital to a year after surgery.",
"title": "Hip Replacement Recovery Week by Week | Mr Krishna Boddu, Ipswich",
"description": "A week-by-week guide to recovery after hip replacement: walking, exercises, sleeping, driving, work and sport. From consultant hip surgeon Mr Krishna Boddu in Ipswich.",
"h1": "Hip replacement recovery: week by week",
"lead": "Most people recover well from a hip replacement and notice a big improvement within weeks. This guide shows what most people can expect. Everyone recovers at their own pace, and I will tailor the advice to you.",
"about": ("MedicalProcedure", "Total hip replacement"),
"reviewed": (REVIEWED_GUIDES, REVIEWED_GUIDES_ISO),
"body": """
<h2>In hospital: the first 1 to 2 days</h2>
<ul>
<li>The physiotherapists will help you stand and walk with a frame or crutches, usually on the day of surgery or the next morning.</li>
<li>They will teach you your exercises, how to get in and out of bed and a chair, and how to manage stairs.</li>
<li>Most people go home after 1 to 2 nights, once they are comfortable and walking safely.</li>
</ul>

<h2>Weeks 1 to 2</h2>
<ul>
<li>Walk little and often around the house, using your crutches.</li>
<li>Do your exercises several times a day to strengthen the muscles around the hip.</li>
<li>Take your painkillers regularly so that you can walk and exercise comfortably.</li>
<li>I do not routinely ask patients to follow "hip precautions", the traditional restrictions on bending, crossing the legs and sitting in low chairs. Research has found that these restrictions make little or no difference to the risk of dislocation, and moving freely helps an accelerated recovery. If your operation needs any particular precautions, I will explain them to you.</li>
<li>Your wound will be checked at about 2 weeks, usually by a nurse at the hospital.</li>
</ul>

<h2>Weeks 2 to 6</h2>
<ul>
<li>Most people walk further each week, and many move from two crutches to one or to a stick.</li>
<li>Thigh swelling and bruising settle gradually.</li>
<li>At about 6 weeks, I will see you for a follow-up appointment.</li>
</ul>

<h2>Weeks 6 to 12</h2>
<ul>
<li>Many people walk without crutches or sticks.</li>
<li>Most people can drive after about 6 weeks, once they can safely make an emergency stop. Tell your insurer that you have had surgery.</li>
<li>Office work is often possible after 4 to 6 weeks. Heavier work may take around 3 months.</li>
<li>Swimming (once your wound has healed), an exercise bike and walking are good ways to build strength.</li>
</ul>

<h2>3 to 12 months</h2>
<ul>
<li>Most people are back to most daily activities and many hobbies by about 3 months, such as golf, cycling, bowls and dancing.</li>
<li>Some tiredness and aching after activity is normal, and keeps improving for up to a year.</li>
</ul>

<h2>Tips for a good recovery</h2>
<ul>
<li><strong>Walking:</strong> regular short walks are better than one long one.</li>
<li><strong>Stairs:</strong> go up with your good leg first and down with your operated leg first.</li>
<li><strong>Sleeping:</strong> many people find it most comfortable on their back at first. Ask your physiotherapist when you can sleep on your side.</li>
<li><strong>Before surgery:</strong> getting fitter, stopping smoking and preparing your home all help. See <a href="/your-operation/">your operation</a>.</li>
</ul>
""" + WARNING_SIGNS,
"sources": [NICE_157, KORFITSEN, NHS_HIP_REC],
"related": ["hip-replacement", "sleeping-after-hip-or-knee-replacement", "blood-clots-after-joint-replacement", "life-after-a-joint-replacement", "your-operation"],
},
{
"slug": "partial-vs-total-knee-replacement",
"nav": "Partial or total knee replacement?",
"group": "guides",
"card": "How the two operations compare, and who is suitable for a partial knee.",
"title": "Partial vs Total Knee Replacement: Which Is Right for You? | Mr Krishna Boddu",
"description": "Partial (unicompartmental) or total knee replacement? Who is suitable, recovery, risks and how long each lasts, compared side by side by knee surgeon Mr Krishna Boddu.",
"h1": "Partial or total knee replacement?",
"lead": "If arthritis affects only one part of your knee, you may be able to choose between a partial and a total knee replacement. Both are good operations. This page compares them so that you can think about which suits you before we talk.",
"about": ("MedicalProcedure", "Unicompartmental knee replacement"),
"reviewed": (REVIEWED_GUIDES, REVIEWED_GUIDES_ISO),
"body": """
<h2>The difference</h2>
<p>A <a href="/knee-replacement/">total knee replacement</a> resurfaces the whole joint. A <a href="/partial-knee-replacement/">partial knee replacement</a> replaces only the worn part, most often the inner (medial) side, and keeps the healthy rest of the knee and its ligaments.</p>

<figure class="diagram"><img src="/assets/knee-total-vs-partial.svg" width="560" height="440" alt="Line diagram of a knee from the front. In a total knee replacement, metal covers the whole end of the thigh bone and the top of the shin bone, with a plastic insert between them. In a partial knee replacement, only the worn inner side is replaced and the rest of the knee is kept." loading="lazy"><figcaption>A total knee replacement resurfaces the whole joint. A partial knee replacement resurfaces only the worn side.</figcaption></figure>

<h2>Side by side</h2>
<table>
<thead><tr><th scope="col"></th><th scope="col">Partial knee</th><th scope="col">Total knee</th></tr></thead>
<tbody>
<tr><td>Who is suitable</td><td>Arthritis in one part of the knee, healthy ligaments, good movement</td><td>Most people with knee arthritis</td></tr>
<tr><td>Hospital stay</td><td>Usually 0 to 1 nights</td><td>Usually 1 to 2 nights</td></tr>
<tr><td>Recovery</td><td>Often quicker</td><td>Full recovery up to 12 months</td></tr>
<tr><td>Driving</td><td>Often after 4 to 6 weeks</td><td>Usually after about 6 weeks</td></tr>
<tr><td>How it feels</td><td>Often feels more like a natural knee</td><td>Most people are very satisfied</td></tr>
<tr><td>Serious complications in the first months</td><td>Less common</td><td>Uncommon</td></tr>
<tr><td>Lasting more than 15 years (implants I use)</td><td>91 in 100</td><td>95 in 100</td></tr>
</tbody>
</table>

<h2>What the research shows</h2>
<ul>
<li>A large UK trial (TOPKAT) found that patients did as well after a partial as after a total knee replacement at five years.</li>
<li>National Joint Registry studies and a review published in the BMJ found lower risks of complications, such as blood clots, heart attack, stroke and deep infection, after a partial knee replacement.</li>
<li>Partial knee replacements are more likely to need further surgery later. If that happens, a partial knee can usually be converted to a total knee replacement.</li>
</ul>
<p>National guidance (NICE) recommends that people with arthritis in the inner part of the knee are offered the choice of either operation.</p>

<h2>How I help you decide</h2>
<p>I will examine your knee and review standing X-rays, and sometimes further X-rays, to see whether a partial knee replacement is possible for you. Where both are suitable, we will weigh up the quicker recovery of a partial knee against the slightly higher chance of further surgery, in the light of your age, activity and preferences. Either operation can be done with <a href="/robotic-hip-and-knee-replacement/">Mako robotic assistance</a>, but I use it only where it is appropriate for you.</p>
""",
"sources": [NICE_157, TOPKAT, WILSON, LIDDLE, NJR_REPORTS, GILL_ZUK],
"related": ["partial-knee-replacement", "knee-replacement", "knee-arthritis", "knee-replacement-recovery"],
},
{
"slug": "how-long-do-hip-and-knee-replacements-last",
"nav": "How long do replacements last?",
"group": "guides",
"card": "What the evidence and the National Joint Registry say, and what affects it.",
"title": "How Long Do Hip and Knee Replacements Last? | Mr Krishna Boddu",
"description": "How long hip, knee and partial knee replacements last, from large studies and the UK National Joint Registry, what affects it, and signs that a joint may be wearing out.",
"h1": "How long do hip and knee replacements last?",
"lead": "Most hip and knee replacements last for many years, and for many people they last a lifetime. Here is what the evidence shows, and what affects how long yours may last.",
"about": ("MedicalProcedure", "Joint replacement"),
"reviewed": (REVIEWED_GUIDES, REVIEWED_GUIDES_ISO),
"body": """
<h2>What large studies show</h2>
<p>Two large reviews published in the Lancet in 2019 pooled national joint registry data for hundreds of thousands of patients with more than 15 years of follow-up.</p>
<ul>
<li><strong>Hip replacements:</strong> about 58 in 100 were still working 25 years after surgery.</li>
<li><strong>Total knee replacements:</strong> about 82 in 100 were still working 25 years after surgery.</li>
<li><strong>Partial knee replacements:</strong> about 70 in 100 were still working 25 years after surgery.</li>
</ul>
<p>These figures include implants that are no longer used, so modern joint replacements may do better.</p>

<h2>The implants I use</h2>
<p>I use implants with some of the best results and longest track records in the UK National Joint Registry. For these implants, the Registry shows that:</p>
<table>
<thead><tr><th scope="col">Operation</th><th scope="col">Lasting more than 15 years</th></tr></thead>
<tbody>
<tr><td><a href="/hip-replacement/">Hip replacement</a></td><td>95 in 100</td></tr>
<tr><td><a href="/knee-replacement/">Total knee replacement</a></td><td>95 in 100</td></tr>
<tr><td><a href="/partial-knee-replacement/">Partial knee replacement</a></td><td>91 in 100</td></tr>
</tbody>
</table>
<p>See my <a href="/outcomes-reviews/">outcomes and reviews</a>.</p>

<h2>What affects how long a joint replacement lasts</h2>
<ul>
<li><strong>Age:</strong> younger people are more active and live longer with their joint, so they are more likely to need further surgery at some point.</li>
<li><strong>Activity:</strong> walking, swimming, cycling and golf are encouraged. High-impact sports such as running put more strain on the joint.</li>
<li><strong>Weight:</strong> being overweight increases the load on the joint replacement, so keeping to a healthy weight helps it last.</li>
<li><strong>Bone strength:</strong> bones can weaken with age, for example from osteoporosis. A fall can then cause a fracture around the joint replacement, which sometimes needs revision surgery. Treating osteoporosis and reducing the risk of falls both help.</li>
<li><strong>Infection:</strong> uncommon, but it can affect a joint replacement at any time, so get any infection elsewhere in the body treated promptly.</li>
<li><strong>The implant and how it is positioned:</strong> this is why I use implants with proven long-term results.</li>
</ul>

<h2>Signs that a joint replacement may need checking</h2>
<p>New or worsening pain, swelling, a feeling of instability, or clicking and grinding can be signs of wear or loosening. If you notice these, see <a href="/problem-joint-replacement/">painful or worn joint replacements</a>. Not every problem needs further surgery, and when it does, I perform <a href="/revision-hip-replacement/">revision hip</a> and <a href="/revision-knee-replacement/">revision knee</a> replacement.</p>
""",
"sources": [EVANS_HIP, EVANS_KNEE, NJR_REPORTS, GILL_ZUK],
"related": ["why-do-joint-replacements-fail", "am-i-too-young-for-a-joint-replacement", "partial-vs-total-knee-replacement", "problem-joint-replacement"],
},
{
"slug": "when-to-have-a-hip-or-knee-replacement",
"nav": "When is it time for a replacement?",
"group": "guides",
"card": "Signs it may be time to consider surgery, and why there is no need to wait for the pain to be unbearable.",
"title": "When Is It Time for a Hip or Knee Replacement? | Mr Krishna Boddu",
"description": "How to tell when it may be time for a hip or knee replacement: the signs, what to try first, and how the decision is made. Consultant surgeon Mr Krishna Boddu, Ipswich.",
"h1": "When is it time for a hip or knee replacement?",
"lead": "There is no single X-ray finding or pain score that decides when you need a joint replacement. The right time is when arthritis is having a real effect on your life and other treatments are no longer enough. This page explains how to think about it.",
"about": ("MedicalCondition", "Osteoarthritis"),
"reviewed": (REVIEWED_GUIDES, REVIEWED_GUIDES_ISO),
"body": """
<h2>Signs it may be time to talk about surgery</h2>
<ul>
<li>Pain that limits how far you can walk, or stops you doing things you enjoy</li>
<li>Pain that wakes you at night or stops you getting to sleep</li>
<li>Difficulty with stairs, getting out of a chair or a car, or putting on shoes and socks</li>
<li>Pain that affects your work, or your ability to care for others</li>
<li>Exercise, weight loss and painkillers no longer helping enough</li>
<li>Relying on painkillers more than you would like</li>
</ul>

<h2>Try these first</h2>
<p>For most people, the first treatments are exercise and physiotherapy, losing weight if you are overweight, and painkillers or anti-inflammatory gels. A steroid injection can give short-term relief for some people. These help many people, and they also make recovery easier if you do have surgery later. See <a href="/hip-arthritis/">hip arthritis</a> and <a href="/knee-arthritis/">knee arthritis</a>.</p>

<h2>You do not have to wait until the pain is unbearable</h2>
<p>National guidance (NICE) says that people should be referred for a joint replacement assessment when their symptoms have a substantial effect on their quality of life and non-surgical treatments have not helped. It also says that age, weight, smoking or other health conditions should not on their own stop someone being referred. They do affect the balance of benefits and risks, which we will discuss together.</p>

<h2>Is there a risk in waiting?</h2>
<p>For most people, waiting does not make the operation less successful, and it is reasonable to wait until you feel ready. However, very severe stiffness, deformity or muscle weakness can make recovery slower, so it is worth being assessed if your joint is getting steadily worse.</p>

<h2>How we decide together</h2>
<p>At your consultation, I will examine your joint, review X-rays and ask how arthritis affects your daily life. I will explain the likely benefits and risks of surgery for you. Most people have much less pain after a joint replacement, but some still have pain or are not fully satisfied, and I will help you weigh this up. If surgery is not the right step yet, I will tell you. There is no pressure to decide on the day. See <a href="/hip-knee-clinic/">my hip and knee clinic</a>.</p>
""",
"sources": [NICE_226, NICE_157, BESWICK],
"related": ["am-i-too-young-for-a-joint-replacement", "steroid-injections-for-hip-and-knee-arthritis", "hip-pain-or-back-pain", "hip-knee-clinic"],
},
{
"slug": "private-hip-and-knee-replacement-cost",
"nav": "Private replacement costs",
"group": "guides",
"card": "What you pay for, how fixed-price packages work, and using insurance.",
"title": "Private Hip and Knee Replacement Cost in Ipswich | Mr Krishna Boddu",
"description": "How much a private hip or knee replacement costs at Nuffield Health Ipswich, what a fixed-price package includes, consultation fees, insurance and finance options.",
"h1": "How much does a private hip or knee replacement cost?",
"lead": "If you are paying for yourself, you will know the full cost of your surgery before you decide. Here is how the costs work at Nuffield Health Ipswich Hospital, and what to do if you have health insurance.",
"about": ("MedicalProcedure", "Joint replacement"),
"reviewed": (REVIEWED_GUIDES, REVIEWED_GUIDES_ISO),
"body": """
<h2>The steps and what each costs</h2>
<table>
<thead><tr><th scope="col">Step</th><th scope="col">Cost if you are paying for yourself</th></tr></thead>
<tbody>
<tr><td>New consultation with me</td><td>&pound;200</td></tr>
<tr><td>X-rays or scans</td><td>Charged separately by Nuffield Health Ipswich</td></tr>
<tr><td>Follow-up consultation, if needed before you decide</td><td>&pound;100</td></tr>
<tr><td>Surgery</td><td>A fixed-price package from Nuffield Health Ipswich, quoted after your consultation</td></tr>
</tbody>
</table>

<h2>Fixed-price surgery packages</h2>
<p>Once we have agreed that surgery is right for you, Nuffield Health Ipswich will give you a fixed-price quote. Packages usually include the hospital stay, the surgeon's and anaesthetist's fees and follow-up care, and your quote will set out exactly what is included. Nuffield Health publishes guide prices for each operation at Ipswich on its website: see <a href="%NUFFIELD_HOSPITAL%">Nuffield Health Ipswich Hospital</a>. Your own quote depends on your operation and your health.</p>
<p>Nuffield Health also offers finance options, so that you can spread the cost.</p>

<h2>If you have health insurance</h2>
<p>I am recognised by:</p>
<ul class="insurers">%INSURER_LIST%</ul>
<ol>
<li>Check that your policy covers outpatient consultations and the treatment you may need.</li>
<li>Ask your GP for a referral letter if your insurer needs one.</li>
<li>Call your insurer for a pre-authorisation number, and give it to Daniela when you book.</li>
</ol>
<p>I am a Bupa fee-assured consultant, so Bupa members pay no shortfall on my fees for eligible treatment (your policy excess may still apply).</p>

<h2>Questions about fees</h2>
<p>My secretary, %SECRETARY%, handles my billing and can answer questions about fees and insurance on <a href="tel:%SEC_PHONE_TEL%">%SEC_PHONE%</a>. See also <a href="/fees-insurance/">fees and insurance</a>.</p>
""",
"sources": [NUFFIELD_PRICES],
"related": ["fees-insurance", "hip-replacement", "knee-replacement", "contact"],
},
]
