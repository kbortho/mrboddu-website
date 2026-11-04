# Patient guides, third batch (drafted 4 November 2026).
from pages_procedures import NICE_157, NICE_226, BESWICK, BMJ_RR, FIDELITY

REVIEWED3 = ("4 November 2026", "2026-11-04")

NICE_89 = '<a href="https://www.nice.org.uk/guidance/ng89">NICE guideline NG89: Venous thromboembolism in over 16s: reducing the risk of hospital-acquired deep vein thrombosis or pulmonary embolism (2018, updated 2019)</a>'
NHS_DVT = '<a href="https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/">NHS: Deep vein thrombosis (DVT)</a>'
NHS_KNEE_REC = '<a href="https://www.nhs.uk/conditions/knee-replacement/recovery/">NHS: Knee replacement recovery</a>'
NHS_HIP_REC = '<a href="https://www.nhs.uk/conditions/hip-replacement/recovery/">NHS: Hip replacement recovery</a>'
ENGLUND = '<a href="https://doi.org/10.1056/NEJMoa0800694">Englund M et al. Incidental meniscal findings on knee MRI in middle-aged and elderly persons. N Engl J Med 2008;359:1108&ndash;15.</a>'
MESSIER = '<a href="https://doi.org/10.1002/art.21187">Messier SP et al. Weight loss reduces knee-joint loads in overweight and obese older adults with knee osteoarthritis. Arthritis Rheum 2005;52:2026&ndash;32.</a>'
KERKHOFFS = '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3489068/">Kerkhoffs GM et al. The influence of obesity on the complication rate and outcome of total knee arthroplasty: a meta-analysis and systematic literature review. J Bone Joint Surg Am 2012;94:1839&ndash;44.</a>'
ALIPOURIAN = '<a href="https://doi.org/10.1186/s13018-021-02493-4">Alipourian A et al. Improvement of sleep quality 6 months after total knee arthroplasty: a systematic review and meta-analysis. J Orthop Surg Res 2021;16:342.</a>'
SUBRAMANIAN = '<a href="https://www.actaorthopaedica.be/archive/volume-75/issue-5/original-studies/cutaneous-sensory-loss-following-primary-total-knee-arthroplasty-a-two-years-follow-up-study/">Subramanian S et al. Cutaneous sensory loss following primary total knee arthroplasty: a two years follow-up study. Acta Orthop Belg 2009;75(5).</a>'
CRISTAL = '<a href="https://doi.org/10.1001/jama.2022.13416">CRISTAL Study Group (Sidhu VS et al). Effect of aspirin vs enoxaparin on symptomatic venous thromboembolism in patients undergoing hip or knee arthroplasty: the CRISTAL randomized trial. JAMA 2022;328:719&ndash;27.</a>'
HOLM = '<a href="https://doi.org/10.1016/j.apmr.2010.07.229">Holm B et al. Loss of knee-extension strength is related to knee swelling after total knee arthroplasty. Arch Phys Med Rehabil 2010;91:1770&ndash;6.</a>'

GUIDES3 = [
{
"slug": "knee-arthritis-or-meniscal-tear",
"nav": "Arthritis or a meniscal tear?",
"group": "guides",
"card": "How to tell wear-and-tear arthritis from a torn cartilage, and why it matters.",
"title": "Knee Pain: Arthritis or a Meniscal Tear? | Mr Krishna Boddu, Ipswich",
"description": "Is your knee pain from arthritis or a torn meniscus? The typical symptoms, how scans can mislead, and why the treatments differ. Consultant knee surgeon Mr Krishna Boddu, Ipswich.",
"h1": "Knee pain: arthritis or a meniscal tear?",
"lead": "Knee arthritis and meniscal tears are the two commonest causes of knee pain in middle age, and they often occur together. Telling them apart matters, because the treatments are different.",
"about": ("MedicalCondition", "Knee pain"),
"reviewed": REVIEWED3,
"body": """
<h2>Typical features</h2>
<table>
<thead><tr><th scope="col"></th><th scope="col">Meniscal tear</th><th scope="col">Knee arthritis</th></tr></thead>
<tbody>
<tr><td>How it starts</td><td>Often after a twist, or gradually with age</td><td>Gradually, over months or years</td></tr>
<tr><td>Pain</td><td>Usually on one side of the knee, often sharp with twisting or squatting</td><td>An aching pain, often worse with walking, stairs and getting up</td></tr>
<tr><td>Other symptoms</td><td>Catching, or the knee locking so it will not fully straighten</td><td>Stiffness after rest, swelling, grinding, and the knee becoming less straight over time</td></tr>
<tr><td>Best first test</td><td>Examination, and an MRI scan where it would change treatment</td><td>Examination and standing X-rays</td></tr>
</tbody>
</table>

<h2>Why scans can mislead</h2>
<p>Meniscal tears become very common with age, and many cause no symptoms at all. A large study of MRI scans in people over 50 found that many of those with a tear had no knee pain. So a tear on a scan is not always the cause of the pain, especially when there is arthritis as well.</p>

<h2>Why the difference matters</h2>
<ul>
<li><strong>A tear after an injury,</strong> especially in a younger person or a knee that locks, may benefit from <a href="/knee-arthroscopy-meniscal-surgery/">keyhole surgery</a>, and some tears can be repaired.</li>
<li><strong>A tear that has come on gradually</strong> usually does best with physiotherapy. Good-quality trials have found that keyhole surgery often adds little for these tears.</li>
<li><strong>Arthritis</strong> is treated with exercise, weight management, painkillers and sometimes an injection, and with a <a href="/knee-replacement/">knee replacement</a> when these no longer help. Keyhole surgery does not treat arthritis, and national guidance advises against it.</li>
</ul>

<h2>Getting it right</h2>
<p>At your consultation, I will ask how your symptoms started, examine your knee and look at the right scans, so that we can agree the treatment most likely to help. See <a href="/meniscal-tear/">meniscal tear</a> and <a href="/knee-arthritis/">knee arthritis</a>.</p>
""",
"sources": [NICE_226, BMJ_RR, FIDELITY, ENGLUND],
"related": ["meniscal-tear", "knee-arthritis", "knee-arthroscopy-meniscal-surgery", "hip-knee-clinic"],
},
{
"slug": "joint-replacement-if-overweight",
"nav": "Joint replacement if you are overweight",
"group": "guides",
"card": "Why weight alone should not stop you being assessed, and how losing weight can help.",
"title": "Can I Have a Hip or Knee Replacement If I Am Overweight? | Mr Krishna Boddu",
"description": "Can you have a hip or knee replacement if you are overweight? What national guidance says, how weight affects risks and results, and how losing weight helps. Mr Krishna Boddu, Ipswich.",
"h1": "Can I have a joint replacement if I am overweight?",
"lead": "Many people with hip or knee arthritis are overweight, and arthritis pain makes it harder to be active. Being overweight should not on its own stop you being assessed for a joint replacement. This page explains how weight affects the decision.",
"about": ("MedicalProcedure", "Joint replacement"),
"reviewed": REVIEWED3,
"body": """
<h2>What national guidance says</h2>
<p>National guidance (NICE) says that people should not be excluded from referral for joint replacement because they are overweight. The decision depends on your symptoms, how they affect your life, and the balance of benefits and risks for you.</p>

<h2>How weight affects surgery</h2>
<ul>
<li><strong>The benefits are still large.</strong> People who are overweight usually get a big improvement in pain and function after a joint replacement.</li>
<li><strong>Some risks are higher.</strong> Studies have found higher rates of wound problems and deep infection after joint replacement in people who are obese, and a higher chance of further surgery.</li>
<li><strong>The anaesthetic</strong> can be more complex, and the anaesthetist will assess this before your operation.</li>
</ul>
<p>As a guide, a body mass index (BMI) under 35 is generally considered desirable before a joint replacement, because the risks of surgery rise above this. If your BMI is higher, we will talk about whether losing some weight first would make your operation safer.</p>

<h2>How losing weight helps</h2>
<ul>
<li>Even modest weight loss can ease arthritis pain. A study found that each kilogram of weight lost reduced the load on the knee by about 4 kilograms with every step.</li>
<li>Losing weight before surgery can reduce the risks of the operation.</li>
<li>Keeping to a healthy weight afterwards helps your joint replacement last.</li>
</ul>
<p>Your GP can refer you to local or NHS weight management support, which may include the NHS Digital Weight Management Programme. Exercise that is gentle on the joints, such as swimming, water exercise and cycling, can help.</p>

<h2>How we decide together</h2>
<p>I will not judge you on your weight. I will explain your options, the likely benefits and the risks for you, and whether any steps before surgery would make the operation safer. See <a href="/when-to-have-a-hip-or-knee-replacement/">when is it time for a replacement?</a></p>
""",
"sources": [NICE_226, NICE_157, KERKHOFFS, MESSIER],
"related": ["when-to-have-a-hip-or-knee-replacement", "knee-arthritis", "hip-arthritis", "how-long-do-hip-and-knee-replacements-last"],
},
{
"slug": "pain-after-knee-replacement",
"nav": "Pain after knee replacement",
"group": "guides",
"card": "How painful it is, how pain is controlled, and how long it lasts.",
"title": "How Painful Is a Knee Replacement? Pain Relief and Recovery | Mr Krishna Boddu",
"description": "How painful is a knee replacement, how pain is controlled in hospital and at home, how long it lasts, and when to seek advice. Consultant knee surgeon Mr Krishna Boddu, Ipswich.",
"h1": "How painful is a knee replacement?",
"lead": "A knee replacement is a big operation, and some pain afterwards is expected. Modern pain relief keeps most people comfortable enough to walk and exercise from the first day. Here is what to expect.",
"about": ("MedicalProcedure", "Total knee replacement"),
"reviewed": REVIEWED3,
"body": """
<h2>In hospital</h2>
<ul>
<li>Most people have a spinal anaesthetic, which numbs the legs for several hours after the operation.</li>
<li>I usually inject local anaesthetic around the knee during the operation, in line with national guidance, to ease pain for the first day.</li>
<li>You will be given regular painkillers by mouth, so that you can walk and do your exercises.</li>
</ul>

<h2>At home</h2>
<ul>
<li>Pain is usually worst in the first 1 to 2 weeks, and improves steadily over the next 6 to 12 weeks.</li>
<li>Take your painkillers regularly at first, rather than waiting for pain to build. Taking them about 30 minutes before exercise helps.</li>
<li>If you are given opioid painkillers, such as codeine, tramadol or morphine, it is essential to take a laxative with them, because they commonly cause constipation.</li>
<li>Reduce your stronger painkillers as the pain eases. Most people need only simple painkillers after a few weeks.</li>
<li>A cold pack wrapped in a towel, for 15 to 20 minutes at a time, and resting with your leg raised can ease pain and swelling.</li>
<li>Aching at night is common for a few weeks. See <a href="/sleeping-after-hip-or-knee-replacement/">sleeping after a joint replacement</a>.</li>
</ul>

<h2>Longer term</h2>
<p>Most people have much less pain than before their operation. Around 1 in 5 people still have some pain or are not fully satisfied a year after a knee replacement, so I will help you weigh this up before you decide. The knee keeps improving for up to a year.</p>

<div class="callout warn">
<p><strong>Get medical advice straight away</strong> if pain is getting worse rather than better, or comes with a red, hot or leaking wound, a fever, or pain and swelling in your calf. In an emergency, call 999.</p>
</div>
""",
"sources": [NICE_157, BESWICK, NHS_KNEE_REC],
"related": ["knee-replacement-recovery", "swelling-after-knee-replacement", "knee-replacement-exercises", "knee-replacement"],
},
{
"slug": "swelling-after-knee-replacement",
"nav": "Swelling after knee replacement",
"group": "guides",
"card": "How long swelling and warmth last, what helps, and when to seek advice.",
"title": "Swelling After Knee Replacement: What Is Normal? | Mr Krishna Boddu",
"description": "How long swelling, bruising and warmth last after a knee replacement, what helps, and the warning signs that need checking. Consultant knee surgeon Mr Krishna Boddu, Ipswich.",
"h1": "Swelling after a knee replacement: what is normal?",
"lead": "Swelling, bruising and warmth around the knee are a normal part of healing after a knee replacement. They can last longer than many people expect. Here is what is normal and what helps.",
"about": ("MedicalProcedure", "Total knee replacement"),
"reviewed": REVIEWED3,
"body": """
<h2>What is normal</h2>
<ul>
<li><strong>First 2 weeks:</strong> swelling and bruising are usually at their most noticeable. Bruising may spread down the leg to the ankle.</li>
<li><strong>Up to 3 to 6 months:</strong> some swelling is common, especially at the end of the day or after more activity.</li>
<li><strong>Up to a year:</strong> the knee may feel warmer than the other one. This is normal and settles gradually.</li>
</ul>

<h2>Why it matters</h2>
<p>Swelling can make the knee feel stiff and tight, and is linked to weakness of the thigh muscles in the first weeks. Keeping swelling under control makes your exercises easier.</p>

<h2>What helps</h2>
<ul>
<li>Rest with your leg raised, with your foot higher than your hip, a few times a day</li>
<li>Use a cold pack wrapped in a towel for 15 to 20 minutes at a time</li>
<li>Keep doing your exercises, and walk little and often</li>
<li>Pace your activity: a lot more swelling the next day usually means you did too much</li>
</ul>

<div class="callout warn">
<p><strong>Get medical advice straight away if you notice:</strong></p>
<ul>
<li>Pain, swelling or tenderness in your calf, which can be a sign of a blood clot</li>
<li>A wound that becomes red, hot or swollen, or leaks fluid</li>
<li>A fever or feeling unwell</li>
<li>Chest pain or breathlessness</li>
</ul>
<p>In an emergency, call 999.</p>
</div>
""",
"sources": [NICE_157, HOLM, NHS_KNEE_REC],
"related": ["knee-replacement-recovery", "pain-after-knee-replacement", "blood-clots-after-joint-replacement", "knee-replacement-exercises"],
},
{
"slug": "sleeping-after-hip-or-knee-replacement",
"nav": "Sleeping after a joint replacement",
"group": "guides",
"card": "Why sleep is often poor at first, comfortable positions, and tips that help.",
"title": "Sleeping After Hip or Knee Replacement: Positions and Tips | Mr Krishna Boddu",
"description": "Why sleep is often disturbed after a hip or knee replacement, how long it lasts, comfortable sleeping positions and practical tips. Consultant surgeon Mr Krishna Boddu, Ipswich.",
"h1": "Sleeping after a hip or knee replacement",
"lead": "Poor sleep is very common in the first weeks after a joint replacement, and it can be one of the most tiring parts of recovery. It usually improves, and for many people sleep ends up better than before the operation.",
"about": ("MedicalProcedure", "Joint replacement"),
"reviewed": REVIEWED3,
"body": """
<h2>Why sleep is disturbed</h2>
<ul>
<li>Aching and stiffness, which are often worse at night</li>
<li>Difficulty finding a comfortable position</li>
<li>Some painkillers, and being less active during the day</li>
</ul>
<p>Studies of knee replacement show that sleep is often disrupted for the first weeks, and has usually improved compared with before surgery by 3 to 6 months.</p>

<h2>Comfortable positions</h2>
<ul>
<li><strong>After a knee replacement:</strong> lie on your back with your leg straight. If you use a pillow, put it under your calf or heel, not under the knee, so the knee does not stiffen in a bent position. Lying on your side with a pillow between your knees is fine once it is comfortable.</li>
<li><strong>After a hip replacement:</strong> many people find lying on their back most comfortable at first. Lying on your side with a pillow between your knees is usually fine once it is comfortable. However, avoid lying on your operated side for the first 2 weeks, until the wound has healed.</li>
</ul>

<h2>Tips that help</h2>
<ul>
<li>Take your painkillers about 30 to 60 minutes before bed</li>
<li>Use a cold pack on the joint before you settle down</li>
<li>Keep active during the day, and avoid long daytime naps</li>
<li>Keep to a regular bedtime and limit caffeine in the afternoon and evening</li>
<li>If poor sleep goes on for more than a few weeks, talk to your GP or to me</li>
</ul>
""",
"sources": [ALIPOURIAN, NHS_KNEE_REC, NHS_HIP_REC],
"related": ["knee-replacement-recovery", "hip-replacement-recovery", "pain-after-knee-replacement", "life-after-a-joint-replacement"],
},
{
"slug": "clicking-or-numbness-after-knee-replacement",
"nav": "Clicking or numbness after knee replacement",
"group": "guides",
"card": "Why a new knee can click, why the skin beside the scar can feel numb, and when to worry.",
"title": "Clicking or Numbness After Knee Replacement: Should I Worry? | Mr Krishna Boddu",
"description": "Why a knee replacement can click, why skin beside the scar often feels numb, how long numbness lasts, and the signs that need checking. Consultant knee surgeon Mr Krishna Boddu.",
"h1": "Clicking or numbness after a knee replacement: should I worry?",
"lead": "Two of the commonest questions after a knee replacement are about clicking and about a numb patch of skin beside the scar. Both are usually harmless. This page explains why they happen and when to get them checked.",
"about": ("MedicalProcedure", "Total knee replacement"),
"reviewed": REVIEWED3,
"body": """
<h2>Clicking</h2>
<p>A knee replacement has metal and plastic surfaces, and these can sometimes click or clunk as they move, especially when the muscles are still weak after surgery. If the click is painless and the knee feels stable, it is usually harmless, and it often becomes less noticeable as your muscles get stronger.</p>

<h2>Numbness beside the scar</h2>
<p>Small skin nerves cross the front of the knee, and some are inevitably cut when the incision is made. This leaves a numb or tingling patch, usually on the outer side of the scar. It is very common: in one study, about 8 in 10 patients had some numbness after a knee replacement.</p>
<ul>
<li>The numb area often shrinks over the first year or two, and about half of people in that study recovered fully by two years.</li>
<li>It does not affect how the knee works.</li>
<li>Kneeling can feel strange because of the numbness, but it will not damage the knee.</li>
</ul>

<h2>When to get it checked</h2>
<ul>
<li>Clicking that comes with pain, swelling, or the knee giving way</li>
<li>A knee that feels unstable or wobbly</li>
<li>Numbness or weakness in the foot or lower leg, rather than just around the scar</li>
</ul>
<p>See <a href="/problem-joint-replacement/">painful or worn joint replacements</a>.</p>
""",
"sources": [SUBRAMANIAN, NHS_KNEE_REC],
"related": ["knee-replacement-recovery", "life-after-a-joint-replacement", "problem-joint-replacement", "knee-replacement"],
},
{
"slug": "blood-clots-after-joint-replacement",
"nav": "Blood clots after joint replacement",
"group": "guides",
"card": "The risk, how clots are prevented, and the warning signs.",
"title": "Blood Clots After Hip or Knee Replacement: Risk and Prevention | Mr Krishna Boddu",
"description": "The risk of blood clots (DVT and pulmonary embolism) after hip or knee replacement, how they are prevented in line with NICE guidance, and the warning signs to look out for.",
"h1": "Blood clots after a hip or knee replacement",
"lead": "Blood clots in the leg (deep vein thrombosis) or lungs (pulmonary embolism) are an important risk after any major leg operation. With modern prevention they are uncommon. Here is how the risk is reduced, and the signs to look out for.",
"about": ("MedicalCondition", "Venous thromboembolism"),
"reviewed": REVIEWED3,
"body": """
<h2>How clots are prevented</h2>
<p>Your prevention plan follows national guidance (NICE) and is tailored to you after your pre-operative assessment.</p>
<ul>
<li><strong>Getting moving early:</strong> walking on the day of surgery or the next day is one of the best ways to prevent clots.</li>
<li><strong>Blood-thinning medicine:</strong> based on the best available evidence, most people have 2 weeks of injections after a knee replacement. After a hip replacement, most people have 10 days of injections followed by 28 days of tablets. Individual factors are also taken into account, so your own plan may differ.</li>
<li><strong>Drinking plenty</strong> and doing your ankle and leg exercises.</li>
</ul>
<p>A large Australian trial (CRISTAL) of more than 9,000 patients found fewer symptomatic blood clots with injections than with aspirin alone after hip and knee replacement. Please complete the full course of blood-thinning medicine, even when you feel well.</p>

<h2>Who is at higher risk?</h2>
<p>The risk is higher if you have had a clot before, have a family history of clots, take hormone medicines such as some contraceptive pills or HRT, have cancer, or are less mobile. Tell us at your pre-operative assessment if any of these apply.</p>

<div class="callout warn">
<p><strong>Get medical advice straight away</strong> if you notice pain, swelling, warmth or tenderness in your calf or thigh.</p>
<p><strong>Call 999</strong> if you have sudden breathlessness, chest pain, or cough up blood.</p>
</div>

<h2>Travel</h2>
<p>Long journeys increase the risk of clots. For long-haul flights, it is usually best to wait about 3 months after surgery. See <a href="/life-after-a-joint-replacement/">life after a joint replacement</a>.</p>
""",
"sources": [NICE_89, CRISTAL, NICE_157, NHS_DVT],
"related": ["your-operation", "knee-replacement-recovery", "hip-replacement-recovery", "swelling-after-knee-replacement"],
},
]
