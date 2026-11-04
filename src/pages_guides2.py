# Patient guides, second batch (drafted 3 November 2026), plus the north Essex page.
from pages_procedures import NICE_157, NICE_226, NJR_REPORTS

REVIEWED2 = ("4 November 2026", "2026-11-04")

NHS_KNEE_EX = '<a href="https://www.nhs.uk/conditions/knee-replacement/recovery/">NHS: Knee replacement recovery</a>'
VA_EX = '<a href="https://www.versusarthritis.org/about-arthritis/exercising-with-arthritis/exercises-for-healthy-joints/knee-pain-exercises/">Versus Arthritis: Exercises for knee pain</a>'
NHS_SCIATICA = '<a href="https://www.nhs.uk/conditions/sciatica/">NHS: Sciatica</a>'
NHS_CES = '<a href="https://www.nhs.uk/conditions/cauda-equina-syndrome/">NHS: Cauda equina syndrome</a>'
BAYLISS = '<a href="https://doi.org/10.1016/S0140-6736(17)30059-4">Bayliss LE et al. The effect of patient age at intervention on risk of implant revision after total replacement of the hip or knee: a population-based cohort study. Lancet 2017;389:1424&ndash;30.</a>'
NJR_REASONS = '<a href="https://reports.njrcentre.org.uk/">National Joint Registry annual report: reasons for revision</a>'

GUIDES2 = [
{
"slug": "knee-replacement-exercises",
"nav": "Knee exercises before and after surgery",
"group": "guides",
"card": "Simple exercises, with diagrams, to prepare for and recover from a knee replacement.",
"title": "Exercises Before and After Knee Replacement | Mr Krishna Boddu, Ipswich",
"description": "Simple exercises with diagrams to strengthen your knee before a knee replacement and recover well afterwards, from consultant knee surgeon Mr Krishna Boddu in Ipswich.",
"h1": "Exercises before and after a knee replacement",
"lead": "Exercise is the most important thing you can do to get a good result from a knee replacement. Starting before your operation makes recovery easier. These are the exercises most people are given. Your physiotherapist will tailor them to you.",
"about": ("MedicalProcedure", "Total knee replacement"),
"reviewed": REVIEWED2,
"body": """
<figure class="diagram"><img src="/assets/knee-exercises.svg" width="560" height="470" alt="Line drawings of four knee exercises: a straight leg raise lying on a bed, a heel slide lying on a bed, a seated knee bend on a chair, and knee straightening with the heel on a rolled towel." loading="lazy"><figcaption>Four key exercises. Do them slowly and smoothly.</figcaption></figure>

<h2>The four key exercises</h2>
<ol>
<li><strong>Straight leg raise.</strong> Lie on your back with your other knee bent. Tighten the thigh muscle of your straight leg, then lift it about 20 centimetres off the bed. Hold for 5 seconds and lower slowly. Repeat 10 times.</li>
<li><strong>Heel slide.</strong> Lie on your back with your legs straight. Slide the heel of your operated leg towards your bottom, bending the knee as far as is comfortable. Hold for 5 seconds, then slide it back. Repeat 10 times.</li>
<li><strong>Seated knee bend.</strong> Sit on a firm chair with your foot on the floor. Slide your foot back under the chair as far as you can, hold for 5 seconds, then relax. Repeat 10 times.</li>
<li><strong>Knee straightening.</strong> Sit with your leg out straight and your heel resting on a rolled-up towel. Let the knee sag towards the bed, or press it gently down, and hold for up to a minute. Repeat 3 times. Do not put a pillow under the knee itself, because the knee can stiffen in a bent position.</li>
</ol>

<h2>Before your operation</h2>
<p>Stronger thigh muscles before surgery help you get moving sooner afterwards. As well as the exercises above, try to:</p>
<ul>
<li>Practise standing up from a chair without using your hands, 10 times, a few times a day</li>
<li>Use an exercise bike or swim, if your knee allows</li>
<li>Keep walking as much as is comfortable</li>
</ul>

<h2>After your operation</h2>
<ul>
<li>Start the exercises the day after surgery, or as soon as the physiotherapists show you.</li>
<li>Do them 3 or 4 times a day. Little and often works better than one long session.</li>
<li>Take your painkillers about 30 minutes before you exercise.</li>
<li>Aim to get the knee fully straight, and bend it a little further each week.</li>
<li>An exercise bike is a good way to improve the bend from about 4 to 6 weeks.</li>
</ul>

<div class="callout"><p>Some discomfort during exercise is normal. Stop and seek advice if you have sharp pain, or if pain or swelling is getting steadily worse rather than better.</p></div>

<p>See the <a href="/knee-replacement-recovery/">week-by-week recovery guide</a>.</p>
""",
"sources": [NICE_157, NHS_KNEE_EX, VA_EX],
"related": ["knee-replacement-recovery", "knee-replacement", "your-operation", "knee-arthritis"],
},
{
"slug": "hip-pain-or-back-pain",
"nav": "Hip pain or back pain?",
"group": "guides",
"card": "Where the pain is felt, and how to tell a hip problem from one coming from the back.",
"title": "Is It Hip Pain or Back Pain? | Mr Krishna Boddu, Hip Surgeon, Ipswich",
"description": "Groin, buttock, thigh or knee pain: how to tell whether it comes from your hip, your back or the tendons on the side of the hip. Consultant hip surgeon Mr Krishna Boddu, Ipswich.",
"h1": "Is it hip pain or back pain?",
"lead": "Pain around the hip can come from the hip joint itself, from the lower back, or from the tendons on the side of the hip. They need different treatments, so finding the cause is the first step.",
"about": ("MedicalCondition", "Hip pain"),
"reviewed": REVIEWED2,
"body": """
<h2>Where you feel the pain</h2>
<table>
<thead><tr><th scope="col">Likely cause</th><th scope="col">Typical features</th></tr></thead>
<tbody>
<tr><td>The hip joint, for example arthritis</td><td>Pain in the groin or the front of the thigh, sometimes spreading to the knee. Stiffness, difficulty putting on shoes and socks, and a limp.</td></tr>
<tr><td>The lower back</td><td>Pain in the buttock or lower back, sometimes spreading down the back of the leg below the knee. Pins and needles or numbness. Pain made worse by bending or sitting for long.</td></tr>
<tr><td>The tendons on the side of the hip</td><td>Pain on the outside of the hip, often worse lying on that side at night, after climbing stairs, or after crossing the legs.</td></tr>
</tbody>
</table>
<p>Hip arthritis can cause pain only in the knee, which sometimes delays the diagnosis. Many people have more than one cause at the same time.</p>

<h2>How the cause is found</h2>
<p>At your consultation, I will ask where and when you feel the pain, and examine your hip, back and knee. Pain when the hip is gently rotated points to the hip joint. An X-ray of the hip is usually enough to show arthritis. Sometimes a scan of the back helps, and occasionally an injection into the hip is used as a test: if the pain goes away for a while, the hip is the likely cause.</p>

<h2>Treatment</h2>
<ul>
<li><strong>Hip arthritis:</strong> exercise and physiotherapy first, then a <a href="/hip-replacement/">hip replacement</a> if pain still has a real effect on your life. See <a href="/hip-arthritis/">hip arthritis</a>.</li>
<li><strong>Back-related pain:</strong> usually physiotherapy and staying active. If your pain comes from your back, I will explain this and advise on the right next step, which may include seeing a spinal specialist.</li>
<li><strong>Tendon pain on the side of the hip:</strong> usually a specific exercise programme with a physiotherapist, and sometimes an injection.</li>
</ul>

<div class="callout warn">
<p><strong>Go to A&amp;E or call 999 straight away</strong> if back pain or leg pain comes with any of these:</p>
<ul>
<li>Numbness around your bottom or genitals</li>
<li>New problems passing urine or controlling your bladder or bowels</li>
<li>Weakness in both legs</li>
</ul>
<p>These can be signs of cauda equina syndrome, which needs urgent treatment.</p>
</div>
""",
"sources": [NICE_226, NHS_SCIATICA, NHS_CES],
"related": ["hip-arthritis", "hip-replacement", "hip-knee-clinic", "when-to-have-a-hip-or-knee-replacement"],
},
{
"slug": "am-i-too-young-for-a-joint-replacement",
"nav": "Am I too young for a replacement?",
"group": "guides",
"card": "Why there is no lower age limit, and how age affects the decision.",
"title": "Am I Too Young for a Hip or Knee Replacement? | Mr Krishna Boddu",
"description": "Is there a minimum age for a hip or knee replacement? How age affects the benefits, how long the joint lasts and the chance of further surgery. Mr Krishna Boddu, Ipswich.",
"h1": "Am I too young for a hip or knee replacement?",
"lead": "There is no lower age limit for a hip or knee replacement. What matters is how much arthritis affects your life, and whether other treatments have helped. Age does affect the decision, and this page explains how.",
"about": ("MedicalProcedure", "Joint replacement"),
"reviewed": REVIEWED2,
"body": """
<h2>What national guidance says</h2>
<p>National guidance (NICE) says that age on its own should not stop someone being referred for joint replacement surgery. The decision depends on your symptoms, how they affect your daily life and work, and the balance of benefits and risks for you.</p>

<h2>How age makes a difference</h2>
<ul>
<li><strong>Younger people get many years of benefit.</strong> Living with severe arthritis pain in your 40s or 50s can affect work, family life, sleep and fitness for many years.</li>
<li><strong>Younger people are more likely to need further surgery in their lifetime.</strong> They are more active and will live longer with their joint. A large UK study found that the lifetime chance of needing a revision was about 1 in 20 for people having surgery at 70 or over, but up to about 1 in 3 for men having it in their early 50s.</li>
<li><strong>Revision surgery is usually possible.</strong> If a joint replacement wears out, it can usually be replaced, although a revision is a bigger operation. See <a href="/revision-hip-replacement/">revision hip</a> and <a href="/revision-knee-replacement/">revision knee replacement</a>.</li>
</ul>

<h2>Making the most of other treatments first</h2>
<p>For younger people, it is especially worth trying exercise and physiotherapy, weight loss if needed, changes to activities and painkillers before surgery. A steroid injection can give short-term relief. See <a href="/steroid-injections-for-hip-and-knee-arthritis/">steroid injections</a>.</p>

<h2>Options that may suit younger people</h2>
<ul>
<li>A <a href="/partial-knee-replacement/">partial knee replacement</a>, if arthritis affects only one part of the knee</li>
<li>Implants with long, proven track records in the National Joint Registry, which I use for my hip and knee replacements</li>
</ul>

<h2>How we decide together</h2>
<p>I will explain the likely benefits and risks for you, including the chance of needing further surgery in the future, so that you can make an informed choice. There is no pressure to decide on the day. See <a href="/when-to-have-a-hip-or-knee-replacement/">when is it time for a replacement?</a></p>
""",
"sources": [NICE_226, NICE_157, BAYLISS, NJR_REPORTS],
"related": ["when-to-have-a-hip-or-knee-replacement", "how-long-do-hip-and-knee-replacements-last", "partial-knee-replacement", "hip-knee-clinic"],
},
{
"slug": "steroid-injections-for-hip-and-knee-arthritis",
"nav": "Steroid injections for arthritis",
"group": "guides",
"card": "How well they work, how long they last, the risks and the cost.",
"title": "Steroid Injections for Hip and Knee Arthritis | Mr Krishna Boddu, Ipswich",
"description": "Do steroid injections work for knee and hip arthritis? How long they last, risks, how often you can have them, timing before surgery and cost at Nuffield Health Ipswich.",
"h1": "Steroid injections for hip and knee arthritis",
"lead": "A steroid injection into the joint can ease arthritis pain for a while, and can help you exercise and get on with life. It does not cure arthritis or slow it down, so it works best alongside exercise and other treatments.",
"about": ("MedicalProcedure", "Intra-articular corticosteroid injection"),
"reviewed": REVIEWED2,
"body": """
<h2>How well do they work?</h2>
<p>National guidance (NICE) recommends considering a steroid injection for short-term relief when other treatments have not helped enough, to support exercise. Many people find that pain improves within a few days. Relief usually lasts a few weeks to a few months, and varies from person to person. Some people get little benefit.</p>

<h2>Having the injection</h2>
<ul>
<li><strong>Knee:</strong> usually given in clinic. It takes a few minutes.</li>
<li><strong>Hip:</strong> the hip is deep, so the injection is given under X-ray or ultrasound guidance to make sure it reaches the joint.</li>
<li>A local anaesthetic is often included, so the joint may feel numb for a few hours.</li>
<li>Rest the joint for a day or two, then return to normal activities.</li>
</ul>

<h2>Risks</h2>
<ul>
<li>A flare of pain for a day or two, which usually settles</li>
<li>A temporary rise in blood sugar if you have diabetes</li>
<li>Facial flushing for a day or two</li>
<li>Infection in the joint, which is rare but serious</li>
</ul>
<div class="callout warn"><p><strong>Get medical advice the same day</strong> if the joint becomes hot, red and very swollen, or you feel feverish and unwell after an injection. In an emergency, call 999.</p></div>

<h2>How often can I have one?</h2>
<p>Injections are usually spaced at least 3 months apart, and most people have no more than a few in a year. If injections stop helping, or are needed more and more often, it is worth talking about other options, including surgery.</p>

<h2>Injections and joint replacement surgery</h2>
<p>If you are planning a joint replacement, it is usually best to avoid a steroid injection into that joint in the 3 months before surgery, because it may increase the risk of infection.</p>

<h2>Other injections</h2>
<p>In line with national guidance, I do not recommend hyaluronic acid injections for knee arthritis, because good evidence shows they do not help most people.</p>

<h2>Cost</h2>
<p>If you are paying for yourself, my fee for an injection given in clinic is &pound;100, in addition to the consultation fee. Hospital fees are charged separately by Nuffield Health Ipswich. If you are insured, please check that your policy covers injections. See <a href="/fees-insurance/">fees and insurance</a>.</p>
""",
"sources": [NICE_226],
"related": ["knee-arthritis", "hip-arthritis", "hip-knee-clinic", "fees-insurance"],
},
{
"slug": "life-after-a-joint-replacement",
"nav": "Life after a joint replacement",
"group": "guides",
"card": "Sport, kneeling, gardening, travel and looking after your new joint.",
"title": "Life After a Hip or Knee Replacement: Sport, Travel and More | Mr Krishna Boddu",
"description": "What you can do after a hip or knee replacement: walking, golf, swimming, cycling, gardening, kneeling, flying, airport scanners and keeping your new joint healthy.",
"h1": "Life after a hip or knee replacement",
"lead": "Most people get back to the activities they enjoy after a hip or knee replacement, often doing more than before. Here is what to expect, and how to look after your new joint.",
"about": ("MedicalProcedure", "Joint replacement"),
"reviewed": REVIEWED2,
"body": """
<h2>Sport and exercise</h2>
<p>What you can do after your operation depends partly on your health before it, including your muscle strength, balance and general fitness. The advice below assumes these are normal for your age. I will tailor it to you.</p>
<table>
<thead><tr><th scope="col">Activity</th><th scope="col">Usual advice</th></tr></thead>
<tbody>
<tr><td>Walking, swimming, cycling</td><td>Encouraged. Swim once your wound has healed, and cycle on an exercise bike from a few weeks.</td></tr>
<tr><td>Golf, bowls, dancing</td><td>Usually from about 3 months</td></tr>
<tr><td>Doubles tennis, hiking</td><td>Often possible once you are strong and confident</td></tr>
<tr><td>Running, jumping and contact sports</td><td>Put more strain on the joint and may wear it faster. Please discuss these with me.</td></tr>
</tbody>
</table>
<p>Keeping active and at a healthy weight helps your joint last. See <a href="/how-long-do-hip-and-knee-replacements-last/">how long replacements last</a>.</p>

<h2>Everyday life</h2>
<ul>
<li><strong>Gardening:</strong> light gardening from about 6 weeks. A kneeling pad or low stool helps.</li>
<li><strong>Kneeling after a knee replacement:</strong> it will not damage the knee, but many people find it uncomfortable. It often gets easier with time.</li>
<li><strong>Driving:</strong> usually after about 6 weeks, once you can safely make an emergency stop.</li>
<li><strong>Work:</strong> office work often after 4 to 6 weeks, heavier work after about 3 months.</li>
</ul>

<h2>Travel</h2>
<ul>
<li><strong>Flying:</strong> short flights are usually fine after about 6 weeks. For long-haul flights, it is usually best to wait about 3 months because of the risk of blood clots.</li>
<li><strong>Airport scanners:</strong> your joint may set them off. You do not need a card or letter. Tell the security staff that you have a joint replacement.</li>
</ul>

<h2>Looking after your new joint</h2>
<ul>
<li>Get infections, such as chest, urine or skin infections, treated promptly, because bacteria can occasionally spread to a joint replacement.</li>
<li>Tell your dentist and doctors that you have a joint replacement. In the UK, antibiotics are not routinely needed before dental treatment.</li>
<li>Look after your bones and reduce the risk of falls, especially as you get older.</li>
<li>Seek advice if the joint becomes newly painful, swollen or unstable. See <a href="/problem-joint-replacement/">painful or worn joint replacements</a>.</li>
</ul>
""",
"sources": [NICE_157],
"related": ["hip-replacement-recovery", "knee-replacement-recovery", "how-long-do-hip-and-knee-replacements-last", "why-do-joint-replacements-fail"],
},
{
"slug": "why-do-joint-replacements-fail",
"nav": "Why do joint replacements fail?",
"group": "guides",
"card": "The common reasons a hip or knee replacement needs revising, and the warning signs.",
"title": "Why Do Hip and Knee Replacements Fail? | Mr Krishna Boddu",
"description": "The common reasons hip and knee replacements fail, including loosening, wear, infection, instability and fracture, the warning signs, and how problems are assessed and treated.",
"h1": "Why do hip and knee replacements fail?",
"lead": "Most hip and knee replacements work well for many years. A small number develop problems, sometimes many years later. Knowing the reasons and the warning signs helps problems to be found early.",
"about": ("MedicalCondition", "Complication of joint prosthesis"),
"reviewed": REVIEWED2,
"body": """
<h2>The common reasons</h2>
<ul>
<li><strong>Loosening:</strong> over many years, the bond between the implant and the bone can weaken. This is the most common reason for revision in the long term.</li>
<li><strong>Wear:</strong> the bearing surfaces slowly wear. Modern materials wear much less than older ones.</li>
<li><strong>Infection:</strong> uncommon, at about 1 in 100, but it can happen soon after surgery or years later if bacteria spread from elsewhere in the body.</li>
<li><strong>Instability:</strong> a hip that dislocates, or a knee that feels wobbly or gives way.</li>
<li><strong>Fracture around the implant:</strong> usually after a fall, and more likely when bones are weakened by osteoporosis.</li>
<li><strong>Stiffness:</strong> a knee that does not bend or straighten enough.</li>
<li><strong>Arthritis progressing:</strong> after a partial knee replacement, arthritis can develop in the rest of the knee.</li>
</ul>

<h2>Warning signs</h2>
<ul>
<li>New pain, or pain that is getting worse</li>
<li>Swelling or warmth around the joint</li>
<li>The joint feeling unstable or giving way</li>
<li>Clicking, grinding or squeaking</li>
</ul>
<div class="callout warn"><p><strong>Get medical advice the same day</strong> if your joint becomes hot, red and swollen and you feel unwell or feverish. This can be a sign of infection. In an emergency, call 999.</p></div>

<h2>How problems are assessed</h2>
<p>I will examine the joint and compare new X-rays with earlier ones. Blood tests check for infection, and sometimes fluid is taken from the joint with a needle. A CT scan can show the position of the implant and the bone around it. Not every problem needs further surgery, and some are treated with physiotherapy or other measures. See <a href="/problem-joint-replacement/">painful or worn joint replacements</a>.</p>

<h2>Revision surgery</h2>
<p>When further surgery is needed, a revision operation replaces part or all of the joint. See <a href="/revision-hip-replacement/">revision hip replacement</a> and <a href="/revision-knee-replacement/">revision knee replacement</a>.</p>

<h2>Reducing the risk</h2>
<ul>
<li>Keep to a healthy weight and stay active</li>
<li>Get infections elsewhere in the body treated promptly</li>
<li>Look after your bone health and reduce the risk of falls</li>
</ul>
""",
"sources": [NJR_REASONS, NICE_157],
"related": ["problem-joint-replacement", "revision-hip-replacement", "revision-knee-replacement", "how-long-do-hip-and-knee-replacements-last"],
},
]

