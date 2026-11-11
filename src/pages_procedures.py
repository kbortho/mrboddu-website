# Procedure pages. Text inside [[...]] is a fact still to confirm; it shows highlighted in the preview.

NICE_157 = '<a href="https://www.nice.org.uk/guidance/ng157">NICE guideline NG157: Joint replacement (primary): hip, knee and shoulder (2020)</a>'
NICE_226 = '<a href="https://www.nice.org.uk/guidance/ng226">NICE guideline NG226: Osteoarthritis in over 16s: diagnosis and management (2022)</a>'
NJR_SITE = '<a href="https://www.njrcentre.org.uk/">National Joint Registry</a>'
EVANS_HIP = "Evans JT et al. How long does a hip replacement last? A systematic review and meta-analysis of case series and national registry reports with more than 15 years of follow-up. Lancet 2019;393:647&ndash;54."
EVANS_KNEE = "Evans JT et al. How long does a knee replacement last? A systematic review and meta-analysis of case series and national registry reports with more than 15 years of follow-up. Lancet 2019;393:655&ndash;63."
BESWICK = "Beswick AD et al. What proportion of patients report long-term pain after total hip or knee replacement for osteoarthritis? A systematic review. BMJ Open 2012;2:e000435."
TOPKAT = "Beard DJ et al. The clinical and cost-effectiveness of total versus partial knee replacement in patients with medial compartment osteoarthritis (TOPKAT): 5-year outcomes of a randomised controlled trial. Lancet 2019;394:746&ndash;56."
LIDDLE = "Liddle AD et al. Adverse outcomes after total and unicompartmental knee replacement in 101,330 matched patients: a study of data from the National Joint Registry for England and Wales. Lancet 2014;384:1437&ndash;45."
BMJ_RR = "Siemieniuk RAC et al. Arthroscopic surgery for degenerative knee arthritis and meniscal tears: a clinical practice guideline. BMJ 2017;357:j1982."
FIDELITY = "Sihvonen R et al. Arthroscopic partial meniscectomy versus sham surgery for a degenerative meniscal tear. N Engl J Med 2013;369:2515&ndash;24."
BODDU_HIP23 = '<a href="https://doi.org/10.1302/1358-992X.2023.11.039">Boddu K. Three-year and five-year revision rates of primary total hip arthroplasty are poor predictors of 15-year revision rates: a National Joint Registry analysis. Orthop Proc 2023;105-B(Supp 11):39.</a>'
CHRASTEK_BODDU23 = '<a href="https://doi.org/10.1302/1358-992X.2023.13.085">Chrastek D, Boddu K. Long-term survival rates are similar with or without patellar resurfacing after total knee arthroplasty; however, higher revision rate without patellar resurfacing can be prosthesis-specific: a National Joint Registry analysis. Orthop Proc 2023;105-B(Supp 13):85.</a>'
NJR_REPORTS = '<a href="https://reports.njrcentre.org.uk/">National Joint Registry annual reports: implant survival</a>'
WILSON = '<a href="https://doi.org/10.1136/bmj.l352">Wilson HA et al. Patient relevant outcomes of unicompartmental versus total knee replacement: systematic review and meta-analysis. BMJ 2019;364:l352.</a>'
RACER_KNEE = '<a href="https://doi.org/10.1016/S0140-6736(26)00986-4">Parsons H et al. Robotic-arm-assisted versus conventional total knee replacement (RACER-Knee): a pragmatic, multicentre, participant-masked and assessor-masked, superiority, randomised controlled trial. Lancet 2026.</a>'
RASKAL = '<a href="https://doi.org/10.1302/0301-620X.108B.BJJ-2025-1472.R2">MacDessi SJ et al. Robotic-assisted surgery and functional alignment in total knee arthroplasty: the RASKAL registry-nested 2 &times; 2 factorial randomized trial. Bone Joint J 2026;108-B:622&ndash;33.</a>'
GILL_ZUK = "Gill JR, Nicolai P. Clinical results and 12-year survivorship of the Physica ZUK unicompartmental knee replacement. Knee 2019;26:750&ndash;8."
AOANJRR_2026 = '<a href="https://registry.aoa.org.au/annual-reports-2026">Australian Orthopaedic Association National Joint Replacement Registry. Hip, Knee and Shoulder Arthroplasty Annual Report 2026: Tables KT74 and KT75 (Triathlon CR, robotically assisted vs traditional instrumentation).</a>'
NJR_ROBOTIC = '<a href="https://doi.org/10.1136/bmj-2026-100691">Mohammad HR et al. Early national comparison of robotic versus conventional knee replacements for arthritis using National Joint Registry data: target trial emulation study. BMJ 2026;394:e100691.</a>'

COSTS = """
<h2>Costs and insurance</h2>
<p>I am recognised by Bupa, AXA Health, Aviva, Vitality, WPA, Allianz and Healix. Please check your policy and ask your insurer for a pre-authorisation number before your first appointment. If you are paying for yourself, Nuffield Health Ipswich will give you a fixed-price package after your consultation. See <a href="/fees-insurance/">fees and insurance</a>.</p>
"""

REVISION_WHERE = """
<h2>Where I carry out revision surgery</h2>
<p>Revision surgery is a bigger operation, and patients may need high-dependency care afterwards. For this reason, I prefer to carry out most revision operations at the Essex and Suffolk Elective Orthopaedic Centre (ESEOC) at Colchester Hospital, which offers <a href="https://www.esneft.nhs.uk/your-visit/information-for-private-patients/">a private patient service</a> for both insured and self-paying patients. Some less complicated revision operations are done at Nuffield Health Ipswich. We will discuss which hospital is best for you at your first consultation at Nuffield Health Ipswich.</p>
"""

REVISION_COSTS = """
<h2>Costs and insurance</h2>
<p>I am recognised by Bupa, AXA Health, Aviva, Vitality, WPA, Allianz and Healix. Please check that your policy covers your treatment and the hospital where it will take place, and ask your insurer for a pre-authorisation number before your first appointment. If you are paying for yourself, you will be given a quote for your surgery once we have agreed your treatment plan and where it will take place. See <a href="/fees-insurance/">fees and insurance</a>.</p>
"""

PROCEDURES = [
{
"slug": "hip-replacement",
"nav": "Hip replacement",
"group": "treatments",
"card": "Replacing a hip worn by arthritis, to relieve pain and stiffness.",
"title": "Hip Replacement Surgery in Ipswich, Suffolk | Mr Krishna Boddu",
"description": "Private hip replacement at Nuffield Health Ipswich with Mr Krishna Boddu, consultant hip and knee surgeon. What to expect, recovery, risks and costs.",
"h1": "Hip replacement in Ipswich",
"lead": "A hip replacement can relieve the pain and stiffness of hip arthritis when other treatments are no longer enough. I perform hip replacements at Nuffield Health Ipswich Hospital for patients from across Suffolk and north Essex.",
"about": ("MedicalProcedure", "Total hip replacement"),
"glance": [
  ("Hospital stay", "Usually 1 to 2 nights"),
  ("Anaesthetic", "Usually a spinal anaesthetic, sometimes with sedation"),
  ("Walking", "With a frame or crutches, usually on the day of surgery or the next day"),
  ("Driving", "Usually after about 6 weeks"),
  ("Full recovery", "3 to 12 months"),
],
"body": """
<h2>What is a hip replacement?</h2>
<p>In a total hip replacement, the worn ball at the top of the thigh bone and the worn socket in the pelvis are replaced with artificial parts, usually made of metal and ceramic. The new joint is designed to move smoothly and without pain.</p>

<h2>Who might it help?</h2>
<p>Surgery is worth considering when hip pain or stiffness has a real effect on your daily life, such as walking, sleeping, working or caring for others, and exercise, weight management and painkillers are no longer enough. Age, weight or other health conditions do not on their own rule you out, but they affect the balance of benefits and risks, which we will discuss together.</p>

<h2>Your first appointment</h2>
<p>I will ask about your symptoms, examine your hip and review X-rays, which can usually be taken on the day. If surgery is not the right step yet, I will explain the other options. If it is, we will go through the operation, the recovery and the risks so that you can decide with confidence. There is no pressure to decide on the day.</p>

<h2>The operation</h2>
<p>The operation usually takes 1 to 2 hours. Most people have a spinal anaesthetic, which numbs the legs and helps early recovery, sometimes with sedation; a general anaesthetic is an alternative. Where suitable, I perform hip replacement through a smaller incision, combined with an accelerated rehabilitation programme, so most people are up and walking with the physiotherapists on the day of surgery or the next morning. Where it is clinically suitable, I can also perform the operation with <a href="/robotic-hip-and-knee-replacement/">Mako robotic assistance</a>.</p>

<h2>Recovery</h2>
<ul>
<li>Most people go home after 1 to 2 nights.</li>
<li>You will use crutches or sticks for the first few weeks.</li>
<li>Most people can drive after about 6 weeks, once they can safely make an emergency stop.</li>
<li>Office work is often possible after 4 to 6 weeks; heavier work may take around 3 months.</li>
<li>Improvement continues for up to a year.</li>
</ul>
<p>See the <a href="/hip-replacement-recovery/">week-by-week hip replacement recovery guide</a>, and read more about <a href="/your-operation/">preparing for and recovering from your operation</a>.</p>

<h2>How long does a hip replacement last?</h2>
<p>I use one of the best-performing implant combinations in the UK National Joint Registry, with one of the longest track records. Registry figures show that 95 in 100 of these hip replacements last more than 15 years after surgery, and many last longer. However, individual factors, such as your age and activity level, can affect this significantly. I prefer implants with a long, proven track record because my own research, using National Joint Registry data, found that good results in the first 3 to 5 years are a poor guide to how an implant will perform at 15 years.</p>

<h2>Risks</h2>
<p>Hip replacement is a common and generally successful operation, but every operation carries risks. They include infection (about 1 in 100), blood clots in the leg or lungs, dislocation of the new joint, a difference in leg length, a fracture around the implant, nerve or blood vessel injury, and wear or loosening that may need further surgery in the future. I will explain how these apply to you and the steps we take to reduce them.</p>

<h2>Alternatives to surgery</h2>
<p>Alternatives include exercise and physiotherapy, losing weight where appropriate, painkillers, a walking stick and, for some people, a steroid injection for short-term relief. These are worth trying first and may be enough. See <a href="/hip-arthritis/">hip arthritis</a>.</p>
""" + COSTS + """
<p>Already had a hip replacement that is causing problems? See <a href="/revision-hip-replacement/">revision hip replacement</a>.</p>
""",
"sources": [NICE_157, NICE_226, NJR_REPORTS, BODDU_HIP23],
"related": ["hip-arthritis", "hip-replacement-recovery", "how-long-do-hip-and-knee-replacements-last", "robotic-hip-and-knee-replacement", "revision-hip-replacement"],
},
{
"slug": "revision-hip-replacement",
"nav": "Revision hip replacement",
"group": "treatments",
"card": "Redo surgery for a hip replacement that is worn, loose or causing problems.",
"title": "Revision Hip Replacement in Suffolk | Mr Krishna Boddu",
"description": "Assessment and revision surgery for painful, worn or failed hip replacements in Suffolk and north Essex, with fellowship-trained surgeon Mr Krishna Boddu.",
"h1": "Revision hip replacement",
"lead": "Most hip replacements last many years, but some wear out, loosen or cause problems. Revision surgery replaces some or all of the original implant. I trained in revision hip and knee surgery during fellowships in Montreal and at King's College Hospital, London.",
"about": ("MedicalProcedure", "Revision hip replacement"),
"glance": [
  ("Hospital stay", "Usually 3 to 5 nights"),
  ("Tests beforehand", "Blood tests and X-rays, often a CT scan, sometimes a sample of joint fluid"),
  ("Recovery", "Slower than a first hip replacement, often 3 to 12 months"),
  ("Where", "Most revisions at the Essex and Suffolk Elective Orthopaedic Centre, Colchester Hospital"),
],
"body": """
<h2>Why a hip replacement may need revising</h2>
<ul>
<li>Loosening of the implant from the bone</li>
<li>Wear of the bearing surfaces</li>
<li>Repeated dislocation</li>
<li>Infection</li>
<li>A fracture of the bone around the implant</li>
<li>Pain with a cause that can be corrected</li>
</ul>

<h2>Finding the cause</h2>
<p>Finding the cause matters more than anything else. I will review your history, examine you and arrange X-rays and blood tests, often with a CT scan. If infection is possible, I may take a sample of fluid from the joint. I may also ask for records of your original operation, wherever it was done.</p>

<h2>The operation</h2>
<p>Revision surgery is more complex than a first hip replacement and usually takes longer. Depending on the problem, I may replace only the worn parts or the whole implant, sometimes using bone graft or specialised implants. An infected hip replacement is sometimes treated in two operations several weeks apart.</p>

<h2>Recovery and risks</h2>
<p>Recovery is usually slower than after a first hip replacement, and you may need to limit the weight you put on the leg for a time. The risks are similar to those of a first hip replacement but higher, particularly infection, dislocation and the need for further surgery. Results are generally good but less predictable, and I will give you a realistic picture for your own situation.</p>
""" + REVISION_WHERE + REVISION_COSTS,
"sources": [NJR_SITE, NICE_157],
"related": ["problem-joint-replacement", "hip-replacement", "second-opinion", "fees-insurance"],
},
{
"slug": "knee-replacement",
"nav": "Knee replacement",
"group": "treatments",
"card": "Total knee replacement for knee arthritis, including robotic-assisted surgery where suitable.",
"title": "Knee Replacement Surgery in Ipswich, Suffolk | Mr Krishna Boddu",
"description": "Private knee replacement at Nuffield Health Ipswich with Mr Krishna Boddu. Total, partial and robotic-assisted options, recovery, risks and costs explained.",
"h1": "Knee replacement in Ipswich",
"lead": "A knee replacement can relieve the pain of knee arthritis and help you walk further and sleep better. I perform total, partial and robotic-assisted knee replacements at Nuffield Health Ipswich Hospital.",
"about": ("MedicalProcedure", "Total knee replacement"),
"glance": [
  ("Hospital stay", "Usually 1 to 2 nights"),
  ("Anaesthetic", "Usually a spinal anaesthetic, sometimes with sedation"),
  ("Walking", "With a frame or crutches, usually on the day of surgery or the next day"),
  ("Driving", "Usually after about 6 weeks"),
  ("Full recovery", "Up to 12 months"),
],
"body": """
<h2>What is a knee replacement?</h2>
<p>A total knee replacement resurfaces the worn ends of the thigh bone and shin bone with metal parts, with a smooth plastic insert between them. The back of the kneecap is rarely resurfaced. My own research, using National Joint Registry data, found that at 15 years knee replacements did equally well with or without resurfacing of the kneecap, although this can depend on the implant design.</p>

<h2>Is it right for you?</h2>
<p>A knee replacement is usually considered when arthritis pain limits walking, sleep or daily life, and non-surgical treatments have stopped helping. If arthritis affects only one part of your knee, a <a href="/partial-knee-replacement/">partial knee replacement</a> may be an option, and national guidance recommends that suitable patients are offered that choice.</p>

<h2>Your first appointment</h2>
<p>I will examine your knee, review X-rays and talk through all your options, including physiotherapy, weight management, injections and partial knee replacement where suitable. If we decide together that surgery is right, I will explain the operation, recovery and risks in detail.</p>

<h2>The operation</h2>
<p>The operation usually takes 1 to 2 hours. Most people have a spinal anaesthetic, sometimes with sedation. Where it is clinically suitable, I can perform the operation with <a href="/robotic-hip-and-knee-replacement/">Mako robotic assistance</a>. You will usually be up and walking with the physiotherapists on the day of surgery or the next morning.</p>

<h2>Recovery</h2>
<ul>
<li>Most people go home after 1 to 2 nights.</li>
<li>Regular exercises to bend and straighten the knee are the key to a good result.</li>
<li>Swelling and aching are normal for several months.</li>
<li>Most people can drive after about 6 weeks, once they can safely make an emergency stop.</li>
<li>The knee continues to improve for up to a year.</li>
</ul>
<p>See the <a href="/knee-replacement-recovery/">week-by-week knee replacement recovery guide</a>, and read more about <a href="/your-operation/">preparing for and recovering from your operation</a>.</p>

<h2>What results can you expect?</h2>
<p>Most people have much less pain and can do more after a knee replacement. Around 1 in 5 people still have some pain or are not fully satisfied, so I will help you weigh this up before you decide.</p>

<h2>How long does a knee replacement last?</h2>
<p>I use one of the best-performing implant combinations in the UK National Joint Registry, with one of the longest track records. Registry figures show that 95 in 100 of these knee replacements last more than 15 years after surgery, and many last longer. However, individual factors, such as your age and activity level, can affect this significantly.</p>

<h2>Risks</h2>
<p>Risks include infection (about 1 in 100), blood clots, stiffness (occasionally needing a manipulation under anaesthetic), ongoing pain, wound problems, nerve or blood vessel injury, a fracture around the implant, and wear or loosening that may need further surgery in the future.</p>

<h2>Alternatives to surgery</h2>
<p>Exercise and physiotherapy, weight loss where appropriate, anti-inflammatory gels and painkillers, and steroid injections for short-term relief can all help. See <a href="/knee-arthritis/">knee arthritis</a>.</p>
""" + COSTS,
"sources": [NICE_157, NICE_226, NJR_REPORTS, BESWICK, CHRASTEK_BODDU23],
"related": ["partial-knee-replacement", "knee-replacement-recovery", "partial-vs-total-knee-replacement", "robotic-hip-and-knee-replacement", "knee-arthritis"],
},
{
"slug": "partial-knee-replacement",
"nav": "Partial knee replacement",
"group": "treatments",
"card": "Replacing only the worn part of the knee, keeping the healthy rest of the joint.",
"title": "Partial Knee Replacement in Ipswich, Suffolk | Mr Krishna Boddu",
"description": "Partial (unicompartmental) knee replacement at Nuffield Health Ipswich with Mr Krishna Boddu. Who is suitable, recovery, and how it compares with a total knee replacement.",
"h1": "Partial knee replacement",
"lead": "If arthritis affects only one part of your knee, a partial (unicompartmental) knee replacement resurfaces just that part. It keeps the healthy rest of the knee, including its ligaments.",
"about": ("MedicalProcedure", "Unicompartmental knee replacement"),
"glance": [
  ("Hospital stay", "Usually 0 to 1 nights"),
  ("Recovery", "Usually quicker than after a total knee replacement"),
  ("Driving", "Often after 4 to 6 weeks"),
],
"body": """
<h2>Who is suitable?</h2>
<p>A partial knee replacement can be a good option when arthritis is limited to one compartment of the knee, most often the inner (medial) side, the knee ligaments are healthy and the knee bends and straightens well. I assess this with an examination and standing X-rays, and sometimes further X-rays or an MRI scan.</p>

<h2>Partial or total knee replacement?</h2>
<p>National guidance recommends that people with arthritis in the inner part of the knee are offered the choice of a partial or a total knee replacement. A large UK trial (TOPKAT) found that patients did as well after a partial as after a total knee replacement at five years. A review of studies published in the BMJ found lower risks of complications, such as blood clots, heart attack, stroke and deep infection, after a partial than after a total knee replacement.</p>
<ul>
<li><strong>Advantages:</strong> recovery is often quicker, the knee often feels more natural, and serious complications in the first months are less common.</li>
<li><strong>Trade-off:</strong> partial replacements are more likely to need further surgery later. If needed, a partial replacement can usually be converted to a total one.</li>
</ul>
<p>See <a href="/partial-vs-total-knee-replacement/">partial or total knee replacement compared side by side</a>.</p>

<h2>How long does a partial knee replacement last?</h2>
<p>For most partial knee replacements, I use the ZUK implant, one of the best-performing partial knees in the UK National Joint Registry, with one of the longest track records. Registry figures show that 91 in 100 of these partial knee replacements last more than 15 years after surgery, and many last longer. This compares with 95 in 100 for the total knee replacements I use. However, individual factors, such as your age and activity level, can affect this significantly.</p>

<h2>Robotic assistance</h2>
<p>Where it is suitable, I can perform a partial knee replacement with <a href="/robotic-hip-and-knee-replacement/">Mako robotic assistance</a>, which helps position the implant precisely.</p>

<h2>Risks</h2>
<p>Risks are similar to those of a total knee replacement, including infection, blood clots, stiffness and ongoing pain. Arthritis can also progress in the rest of the knee, which may lead to a total knee replacement in the future.</p>
""" + COSTS,
"sources": [NICE_157, TOPKAT, WILSON, LIDDLE, NJR_REPORTS, GILL_ZUK],
"related": ["knee-replacement", "partial-vs-total-knee-replacement", "robotic-hip-and-knee-replacement", "knee-arthritis", "fees-insurance"],
},
{
"slug": "revision-knee-replacement",
"nav": "Revision knee replacement",
"group": "treatments",
"card": "Redo surgery for a knee replacement that is loose, unstable, infected or worn.",
"title": "Revision Knee Replacement in Suffolk | Mr Krishna Boddu",
"description": "Assessment and revision surgery for painful, unstable or failed knee replacements in Suffolk and north Essex, with fellowship-trained surgeon Mr Krishna Boddu.",
"h1": "Revision knee replacement",
"lead": "When a knee replacement becomes loose, unstable, infected or worn, revision surgery replaces some or all of it. I trained in revision hip and knee surgery during fellowships in Montreal and at King's College Hospital, London.",
"about": ("MedicalProcedure", "Revision knee replacement"),
"glance": [
  ("Hospital stay", "Usually 3 to 5 nights"),
  ("Tests beforehand", "Blood tests and X-rays, often a CT scan, sometimes a sample of joint fluid"),
  ("Recovery", "Slower than a first knee replacement, often 6 to 12 months"),
  ("Where", "Most revisions at the Essex and Suffolk Elective Orthopaedic Centre, Colchester Hospital"),
],
"body": """
<h2>Why a knee replacement may need revising</h2>
<ul>
<li>Loosening of the implant from the bone</li>
<li>Instability, where the knee feels wobbly or gives way</li>
<li>Infection</li>
<li>Wear of the plastic insert</li>
<li>Severe stiffness</li>
<li>A fracture around the implant</li>
<li>Arthritis progressing after a partial knee replacement</li>
</ul>

<h2>Finding the cause</h2>
<p>I will review your history and examine you, and arrange X-rays, blood tests and often a CT scan. If infection is possible, I may take a sample of fluid from the joint. Revision for pain without a clear cause rarely helps, and I will tell you honestly if I do not think surgery will improve things.</p>

<h2>The operation and recovery</h2>
<p>Revision surgery is more complex than a first knee replacement. It often uses implants designed for revision, which give extra stability and fixation. Recovery is slower, and the risks, particularly infection, stiffness and further surgery, are higher. Results are generally good when there is a clear cause to correct.</p>
""" + REVISION_WHERE + REVISION_COSTS,
"sources": [NJR_SITE, NICE_157],
"related": ["problem-joint-replacement", "knee-replacement", "second-opinion", "fees-insurance"],
},
{
"slug": "knee-arthroscopy-meniscal-surgery",
"nav": "Knee arthroscopy and meniscal surgery",
"group": "treatments",
"card": "Keyhole surgery to repair or trim a torn meniscus when it is needed.",
"title": "Knee Arthroscopy and Meniscal Surgery, Ipswich, Suffolk | Mr Krishna Boddu",
"description": "Keyhole knee surgery for meniscal tears at Nuffield Health Ipswich: meniscal repair and debridement, when surgery helps, recovery and risks.",
"h1": "Knee arthroscopy and meniscal surgery",
"lead": "Knee arthroscopy is keyhole surgery using a small camera. I use it to treat meniscal tears that cause locking or persistent symptoms, and I repair the meniscus where possible.",
"about": ("MedicalProcedure", "Knee arthroscopy"),
"glance": [
  ("Hospital stay", "Usually a day case"),
  ("Anaesthetic", "Usually a general anaesthetic"),
  ("After trimming", "Desk work after about 1 to 2 weeks"),
  ("After repair", "A brace and protected movement for about 6 weeks"),
],
"body": """
<h2>When can keyhole surgery help?</h2>
<ul>
<li>A torn piece of meniscus that makes the knee lock or catch</li>
<li>A tear from an injury that can be repaired, especially in younger and active people</li>
<li>Symptoms from a tear that continue despite a good course of physiotherapy</li>
</ul>

<h2>When it is unlikely to help</h2>
<p>Keyhole surgery does not treat knee arthritis, and national guidance advises against it for arthritis alone. For tears that come on gradually in middle age, physiotherapy is usually the first treatment, because good-quality trials show that surgery often adds little. I will tell you if I think surgery is unlikely to help you.</p>

<h2>Repair or trimming?</h2>
<p>The meniscus protects the knee, so I repair it where the tear is suitable. Repairs heal best in younger patients and in tears near the outer edge, which have a good blood supply. Where a tear cannot be repaired, I trim away the torn part (meniscal debridement) and keep as much healthy meniscus as possible.</p>

<h2>Recovery</h2>
<p>After trimming, most people walk the same day and return to desk work within 1 to 2 weeks. After a repair, recovery is longer, usually with a brace and limited bending for about 6 weeks, and a return to sport after 4 to 6 months.</p>

<h2>Risks</h2>
<p>Risks are low but include infection, blood clots, swelling, stiffness and nerve injury. Some meniscal repairs do not heal and need further surgery.</p>

""" + COSTS,
"sources": [NICE_226, BMJ_RR, FIDELITY],
"related": ["meniscal-tear", "knee-arthritis", "hip-knee-clinic", "fees-insurance"],
},
{
"slug": "robotic-hip-and-knee-replacement",
"nav": "Robotic-assisted hip and knee replacement",
"group": "treatments",
"card": "Mako robotic-assisted hip, knee and partial knee replacement, used where clinically suitable.",
"title": "Robotic Hip and Knee Replacement in Suffolk (Mako) | Mr Krishna Boddu",
"description": "Mako robotic-assisted hip, knee and partial knee replacement at Nuffield Health Ipswich. How it works, what the evidence shows and whether it suits you.",
"h1": "Robotic-assisted hip and knee replacement",
"lead": "I am trained in Mako robotic-assisted hip and knee replacement, including partial knee replacement, at Nuffield Health Ipswich Hospital. I use it where it is clinically suitable, as one of several good options.",
"about": ("MedicalProcedure", "Robotic-assisted hip and knee replacement"),
"glance": [
  ("Extra step", "A CT scan of your hip or knee before surgery"),
  ("Who operates", "I perform the operation; the robotic arm guides it within my plan"),
  ("Hospital stay and recovery", "Similar to a standard hip or knee replacement"),
],
"body": """
<h2>How it works</h2>
<p>A CT scan before surgery creates a 3D model of your hip or knee, which I use to plan the size and position of the implants. During the operation I guide a robotic arm that helps prepare the bone and position the implants within the limits of that plan. The robot does not operate on its own.</p>

<h2>What the evidence shows</h2>
<p>Studies show that robotic assistance positions hip and knee implants more precisely and closer to the plan, and some earlier, smaller studies reported less pain and a quicker recovery in the first weeks after robotic knee replacement. Recent large studies have tested whether this leads to better results for patients:</p>
<ul>
<li><strong>RACER-Knee</strong>, a UK trial of 339 patients in 10 hospitals, compared Mako robotic-assisted with conventional total knee replacement. The robotic operations were more precise, but at one year there was no significant difference in patients' outcomes, and early recovery and pain were similar (Lancet, 2026).</li>
<li><strong>RASKAL</strong>, an Australian trial of 334 patients, compared robotic-assisted with computer-navigated total knee replacement and found no significant difference in outcomes at one or two years (Bone &amp; Joint Journal, 2026).</li>
<li><strong>A National Joint Registry study</strong> of almost 700,000 knee replacements, including more than 22,000 robotic operations, found no significant difference in the risk of revision (further surgery) in the first few years between robotic and conventional total or partial knee replacements (BMJ, 2026).</li>
<li><strong>The Australian joint registry</strong> found that, of more than 67,000 Triathlon total knee replacements (the implant used with the Mako robot) performed since 2016, 1.9 in 100 robotic-assisted knees had needed revision by 5 years, compared with 2.4 in 100 done with traditional instruments. This small difference was statistically significant after the first 18 months, once patient and surgeon factors were taken into account (AOANJRR Annual Report, 2026).</li>
</ul>
<p>So when robotic assistance is used routinely, these studies found no significant difference in outcomes at one year, and standard hip and knee replacements remain excellent operations. There may, however, be a case for robotic assistance in more complex surgery, where placing the components accurately is technically challenging.</p>

<h2>Is it right for you?</h2>
<p>We will decide together at your consultation. It depends on your joint, the type of implant that suits you, and your insurance, as cover for robotic surgery varies between insurers. Read more about <a href="/hip-replacement/">hip replacement</a>, <a href="/knee-replacement/">knee replacement</a> and <a href="/partial-knee-replacement/">partial knee replacement</a>.</p>

<p class="small">Mako is a trademark of Stryker Corporation.</p>
""" + COSTS,
"sources": ["Domb BG et al. Comparison of robotic-assisted and conventional acetabular cup placement in THA: a matched-pair controlled study. Clin Orthop Relat Res 2014;472:329&ndash;36.", "Kayani B et al. Robotic-arm assisted total knee arthroplasty is associated with improved early functional recovery and reduced short-term inpatient length of stay compared with conventional jig-based total knee arthroplasty. Bone Joint J 2018;100-B:930&ndash;7.", RACER_KNEE, RASKAL, NJR_ROBOTIC, AOANJRR_2026, NICE_157],
"related": ["hip-replacement", "knee-replacement", "partial-knee-replacement", "fees-insurance"],
},
]
