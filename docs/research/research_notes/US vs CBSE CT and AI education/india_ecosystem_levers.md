# India's wider school CT/AI ecosystem: landscape, implementation gaps and improvement levers (as of November 2026)

Scope note: this file covers the ecosystem around the CBSE CT&AI Classes 3-8 curriculum, which is researched elsewhere and not repeated here. Research date is 6 November 2026. Many sources are news reports or secondary summaries of government replies; primary pages on pib.gov.in and business-standard.com returned HTTP 403 to the fetch tool, so several official figures are cited via mirrors or news reports and are flagged as such. An "Annual Report 2026" PDF from educationforallinindia.com was found, but it is image-only and could not be read.

## 1. National policy: NEP 2020, NCF-SE 2023, MoE October 2025 announcement, NCERT, IndiaAI/MSDE programmes, ATL, 2026 developments

### Takeaway
The national basis is NEP 2020 Para 4.25 (mathematics and CT throughout school, coding from the Middle Stage, Grades 6-8) and NCF-SE 2023 Section 2.3.4.2. On that basis the Ministry of Education announced in October 2025 that "AI & CT" would start from Class 3 in all schools from 2026-27. That announcement covers all schools, but the only implemented, board-level curriculum so far is CBSE's. Around it sit several short, voluntary, non-curricular programmes: SOAR (MSDE, 3 x 15 h), YUVAi (MeitY, Classes 8-12, selective), and AI for All (4 h, CBSE/Intel). There are also announcements still in the pipeline: NCERT Class 11-12 AI textbooks (team formed December 2025) and 50,000 new ATLs (announced in the 2025 Budget, against just over 10,000 labs existing).

### Cited Findings
- **NEP 2020 Para 4.25:** It places "mathematics and computational thinking" throughout the school years and says coding will be introduced at the Middle Stage (Grades 6-8). This is as summarised in a 2021 Rajya Sabha answer. — [Rajya Sabha PQ, 8 Dec 2021](https://rsdebate.nic.in/bitstream/123456789/722047/1/PQ_255_08122021_U1149_p184_p184.pdf)
- **CBSE's stated policy basis:** CBSE's own 2026-27 CT&AI webinar deck says the curriculum operationalises NEP 2020 Para 4.25 and NCF-SE 2023 Section 2.3.4.2 Part A. — [CBSE CTAI Webinar PPT 2026-27](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf)
- **CT versus coding in RIE Bhopal guidance:** An NCERT-family institution (RIE Bhopal IQAC) argues that the emphasis should be on CT "rather than coding merely". It also says CT or coding may be integrated into existing subjects such as mathematics. This is the conceptual basis for India's maths-integrated, unplugged-first approach. — [RIE Bhopal, "Computational Thinking and its importance in School Education"](https://riebhopal.nic.in/IQAC\Computational_Thinking_and_its_importance_in_School_Education.pdf)
- **Ministry of Education announcement (around 30-31 October 2025):** "AI & CT" will be introduced from Grade 3 in the 2026-27 session in all schools, aligned with NEP 2020 and NCF-SE 2023. The Ministry described it as a "nascent yet significant step". It is coordinating with CBSE, NCERT, KVS, NVS and state education departments. CBSE set up an expert committee chaired by Prof. Karthik Raman (IIT Madras). Teacher training is to run through NISHTHA and "grade-specific" programmes, with video-based resources. — [PIB release PRID 2184211](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2184211&reg=48&lang=2) (403 to fetch; content via search summary); [DD News](https://ddnews.gov.in/en/ai-curriculum-to-be-introduced-in-all-schools-from-class-3-onwards/); [EducationWorld](https://educationworld.in/ai-and-computational-thinking-to-be-taught-from-class-3-in-all-schools-from-2026-27/); [Careers360](https://news.careers360.com/students-learn-ai-computational-thinking-from-class-3-starting-2026-27-cbse-ncert-frame-curriculum); [LatestLY/IANS on NISHTHA modules](https://www.latestly.com/agency-news/india-news-ai-curriculum-teacher-training-will-be-done-through-nishtha-modules-video-based-learning-resources-7185608.html)
  - An earlier wire report (10 October 2025) already said the Centre would introduce AI from Class 3 from 2026-27. — [The Week/PTI, 10 Oct 2025](https://www.theweek.in/wire-updates/national/2025/10/10/del91-edu-ai-education.html)
  - **Mandatory or not:** The official PIB and DD News wording says AI & CT will be "introduced" in all schools. It does not use the word "mandatory". Commercial blogs call it mandatory. State boards are not bound by CBSE's curriculum. — [EducationWorld](https://educationworld.in/ai-and-computational-thinking-to-be-taught-from-class-3-in-all-schools-from-2026-27/)
- **CBSE curriculum launch:** The Union Education Minister launched the CBSE CT&AI curriculum around 7 April 2026. — [Vision IAS, 7 Apr 2026](https://visionias.in/current-affairs/news-today/2026-04-07/society/cbse-curriculum-on-computational-thinking-ct-and-artificial-intelligence-ai-launched-by-union-education-minister)
- **NCERT Class 11-12 AI textbooks:** NCERT constituted a dedicated textbook development team to design AI syllabi and textbooks for Classes 11 and 12. This was reported to Parliament around 22 December 2025. No publication date had been found as of November 2026, and a July 2026 roundup still describes it as "began developing". — [Tribune](https://www.tribuneindia.com/news/india/ncert-constitutes-team-to-develop-class-11-12-textbooks-on-ai/); [India Today NE, 22 Dec 2025](https://www.indiatodayne.in/national/story/ncert-to-develop-ai-textbooks-for-classes-11-and-12-as-india-pushes-future-ready-education-1320597-2025-12-22); [EducationWorld](https://educationworld.in/ncert-to-develop-ai-syllabi-and-textbooks-for-classes-11-and-12/); [Organiser, 12 Jul 2026](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **NCERT Grade 6 vocational textbook:** It includes an "Animation and Games" project that uses AI tools. — [EducationWorld](https://educationworld.in/ncert-to-develop-ai-syllabi-and-textbooks-for-classes-11-and-12/) (via search summary)
- **SOAR (Skilling for AI Readiness):**
  - Run by the Ministry of Skill Development and Entrepreneurship (MSDE), launched July 2025.
  - For Classes 6-12, it offers three micro-credentials of 15 hours each: "AI to be Aware", "AI to Acquire" and "AI to Aspire", 45 hours in total.
  - Educators get a 45-hour module.
  - Reported enrolment for "AI to Be Aware" was about 1.17 lakh; completion is unclear.
  - Some quiz sites wrongly attribute SOAR to MeitY. Government sources say MSDE.

  — [PIB backgrounder PDF, Oct 2025](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/oct/doc20251022671301.pdf); [Vikaspedia](https://en.vikaspedia.in/viewcontent/education/artificial-intelligence/skilling-for-ai-readiness); [IANS, 22 Oct 2025](https://ianslive.in/soar-laying-foundation-for-digitally-inclusive-competitive-and-self-reliant-india-govt--20251022111512); [Skill Reporter](https://www.skillreporter.com/news/msde/skilling-for-ai-readiness-soar-msde-skill-impact-bond-apprenticeship-pmkvy-naps)
  - A news feature says a CBSE "Skilling for AI Readiness" 15-hour module runs in more than 18,000 CBSE schools for Classes 6-8. This could not be confirmed against a primary CBSE circular. — [The Secretariat](https://thesecretariat.in/article/india-s-schools-step-into-the-ai-era-with-nationwide-training-plan)
- **YUVAi (Youth for Unnati and Vikas with AI):** A MeitY/IndiaAI programme for students in Classes 8-12. It is selective: shortlisted students get online deep-dive training and a 3-day in-person boot camp with mentors. It is the successor to "Responsible AI for Youth". — [IndiaAI](https://indiaai.gov.in/news/meity-announces-yuvai-the-new-edition-of-responsible-ai-for-youth)
- **AI for All:** A free, 4-hour self-paced AI awareness course from the Ministry of Education, CBSE and Intel India. It was launched on NEP 2020's first anniversary (July 2021). — [Organiser, 12 Jul 2026](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **IndiaAI Mission:** Its outlay is Rs 10,371.92 crore over five years, aimed mainly at compute, datasets and research rather than schools. — [The Secretariat](https://thesecretariat.in/article/india-s-schools-step-into-the-ai-era-with-nationwide-training-plan)
- **Online courses:** SWAYAM hosts more than 110 AI courses with more than 4.1 million enrolments. These are mostly higher-education and adult courses. — [The Secretariat](https://thesecretariat.in/article/india-s-schools-step-into-the-ai-era-with-nationwide-training-plan)
- **Atal Tinkering Labs (NITI Aayog/AIM):**
  - The Union Budget 2025-26 (1 February 2025) announced 50,000 ATLs in government schools over five years, with the aim that all government secondary-school students have ATL access.
  - In a Rajya Sabha reply on 3 December 2025, the Education Minister said "over 10,000" ATLs had been established, across private and government schools.
  - No progress count toward the 50,000 target was found.

  — [Business Today, 1 Feb 2025](https://www.businesstoday.in/union-budget/story/union-budget-2025-govt-to-set-up-atal-tinkering-labs-in-50000-schools-over-five-years-462949-2025-02-01); [MoE PIB PDF](https://education.gov.in/sites/upload_files/mhrd/files/PIB2098805.pdf); [Amar Ujala](https://results.amarujala.com/photo-gallery/current-affairs/union-budget-2025-what-are-atal-tinkering-labs-that-will-be-expanded-in-education-budget-read-here)
- **NITI Aayog school-education report (around May 2026):** It flags fragmented school structures, learning-outcome gaps, uneven infrastructure (including uneven digital access in smaller and remote schools), teacher workforce shortages and governance weaknesses. It recommends AI-led reforms in pedagogy and system planning, expanded digital and broadcast learning, and better teacher management. — [Business Standard](https://www.business-standard.com/education/news/niti-flags-gaps-in-school-education-system-calls-for-ai-led-reforms-126050700823_1.html) (403 to fetch; content via search summary)

### Inferences
- India's national design separates concepts. The curriculum layer (CBSE CT&AI, NCERT) is CT-first and unplugged. AI "skilling" is pushed through short, voluntary credential programmes (SOAR, YUVAi, AI for All) run by different ministries: MoE, MSDE and MeitY. That spread across ministries is itself a coordination risk.
- The phrase "all schools from 2026-27" is an announcement. Effective coverage depends on each of roughly 30+ state boards adopting it, and that adoption is patchy (see Section 2).
- Pipeline items that are announced but not delivered as of November 2026: NCERT Class 11-12 AI textbooks, the 50,000 ATLs, and any NCERT-authored CT/AI textbook for state boards.

### Gaps
- **NCERT's 20-hour Grades 9-12 AI module:** It is named in the brief, but I found no 2025-26 source confirming its current form or status. NCERT's own site was not reachable in this pass.
- **"AI Ready Bharat":** I found no reliable source for a programme under that name.
- **DIKSHA/PM e-Vidya CT/AI content:** I found no count of CT/AI content items or usage figures.
- **Exact NEP wording:** Beyond the Para 4.25 summary, I did not verify mentions in Paras 4.23-4.24 or 23.x (which concern AI and technology), against the NEP PDF in this pass.

## 2. States and other boards: Kerala, Tamil Nadu, AP, Telangana, Karnataka, Maharashtra, Delhi, Gujarat, Punjab, UP, others; CISCE

### Takeaway
State activity is real but uneven, and mostly at pilot or announcement stage. Kerala (KITE) has the most mature in-curriculum ICT/AI sequence: Scratch by Class 4, AI/computer vision in Class 7 since 2024, and Python in Classes 9-10. Tamil Nadu's TN SPARK has scaled from 85 pilot schools (September 2025) to about 5,000 government schools (July 2026). Punjab, Telangana and Haryana announced AI rollouts in 2026. Karnataka uses a vocational (NSQF) route. CISCE offers Robotics & AI as an elective subject, not a compulsory primary curriculum.

### Cited Findings
- **Kerala (KITE):**
  - **2024:** AI was introduced in the Class 7 ICT textbook. Its "Computer Vision" chapter has students build a program that recognises facial expressions, using PictoBlox and Scratch.
  - **2025 revised ICT textbooks (August 2025):** Students build simple Scratch games by Class 4 and design their first computer game by Class 6. Python follows in Classes 9-10, and the textbooks integrate AVGC (animation, visual effects, gaming and comics) and AI. The Class 8-10 volumes were due after Onam 2025.
  - No source confirmed "robotics in Class 10" specifically. Python is the documented Class 9-10 content.

  — [ThePrint/PTI, 30 May 2024](https://theprint.in/india/kerala-includes-artificial-intelligence-ai-learning-in-school-textbooks/2107933); [IndiaAI](https://indiaai.gov.in/news/kerala-introduces-artificial-intelligence-in-school-curriculums); [Onmanorama, 24 Aug 2025](https://www.onmanorama.com/career-and-campus/top-news/2025/08/24/kite-ict-textbooks-launch.amp.html)
- **Tamil Nadu (TN SPARK: Tamil Nadu Schools Programme for AI, Robotics and Knowledge of Online Tools):**
  - **Launch, around 14-15 September 2025:** A pilot in 85 government schools in Coimbatore district for Classes 6-9, with 1-2 periods a week.
  - **Materials and teachers:** Bilingual Tamil-English textbooks; tools are Blockly, Turtle Art and Scratch, plus HTML basics and cyber-safety. Trained maths and science teachers deliver it.
  - **By July 2026:** Running as a pilot in about 5,000 government schools. Plans are to extend it statewide to Classes 6-8, with state-board textbooks for Classes 9-10 next year, Classes 11-12 later, and an elective in Classes 11-12. SCERT will train maths and science teachers in government and aided schools.
  - **Partner figure:** An NGO partner reports 340 schools, 67,000 students and 46 facilitators.

  — [Business Today, 15 Sep 2025](https://www.businesstoday.in/technology/news/story/tamil-nadu-launches-tn-spark-to-train-government-school-students-in-ai-coding-and-robotics-494009-2025-09-15); [The News Minute](https://www.thenewsminute.com/amp/story/tamil-nadu/tn-launches-pilot-ai-robotics-programme-in-govt-schools); [Hans India](https://www.thehansindia.com/news/national/tn-plans-ai-emerging-technologies-curriculum-for-all-govt-schools-1100094); [NewKerala, Jul 2026](https://www.newkerala.com/news/a/tn-plans-ai-emerging-technologies-curriculum-all-govt-880.htm); [ILP](https://www.ilpnet.org/transforming-67000-young-learners-with-practical-tech-education/)
  - **Why TN has its own track:** Tamil Nadu has not adopted NEP 2020 (it has its own State Education Policy). That makes TN SPARK a parallel, non-NEP track. *(This is training-data context; not re-verified in this pass.)*
- **Karnataka:**
  - AI is not a separate academic subject. It is offered as an NSQF vocational course for Classes 9-10 in 1,642 government high schools. Officials are reportedly considering AI training from Class 6.
  - Amazon announced advanced coding and AI modules in 100 Karnataka schools (headline only seen).
  - Cyient Foundation's VijAIpatha pilot covers 5 schools, 2,000+ students and 200+ teachers.

  — [Sakshi Education, 2026](https://education.sakshi.com/en/schools/education-news/karnataka-schools-ai-subject-class-9-10-students-2026-200190); [Global Education News](https://globaleducationnews.org/karnataka-ai-education-push-government-schools-explore-training-from-class-6/); [Careers360](https://news.careers360.com/amazon-introduce-advanced-coding-and-ai-modules-in-100-karnataka-schools/amp); [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **Telangana:**
  - In February 2026 the Chief Minister directed officials to introduce AI education from school level and to train teachers through short courses. This is a directive; no curriculum was found.
  - A blog claims only about 21% of Telangana government schools have fully functional computer facilities. This is a secondary figure.

  — [Careers360](https://news.careers360.com/telangana-cm-a-revanth-reddy-directs-introduction-of-ai-education-from-school-level); [NextGen Learner, Mar 2026](https://nextgenlearner.in/2026/03/03/telangana-introduces-ai-into-school-curriculum/)
- **Punjab:**
  - On 3 July 2026, Education Minister Harjot Singh Bains announced an AI curriculum in all government schools "from next month", after a year of preparation.
  - A news feature calls Punjab "the only state with an AI curriculum already in government schools". This is uncorroborated and conflicts with Kerala's in-textbook AI since 2024.

  — [Careers360](https://news.careers360.com/ai-be-introduced-in-govt-schools-in-punjab-education-minister); [Let's Data Science](https://letsdatascience.com/news/punjab-announces-statewide-ai-curriculum-for-schools-aa47ece2); [The Secretariat](https://thesecretariat.in/article/india-s-schools-step-into-the-ai-era-with-nationwide-training-plan)
- **Haryana:** Government schools were to begin AI courses from March 2026 (headline). — [Tribune](https://www.tribuneindia.com/news/haryana/state-government-schools-to-begin-ai-courses-from-march-2026/amp)
- **Madhya Pradesh:** AI courses run in 53 government schools (6,462 students). 274 Sandipani Schools teach AI to 50,000+ students. — [Organiser, Jul 2026](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **Chhattisgarh:** A 3-year robotics and AI programme with Magic Bus India Foundation covers 800 government schools, about 40,000 students and 1,600 teachers. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **Gujarat:** Its Vidya Samiksha Kendra is an AI/data use for governance (54,000 schools, 1.15 crore students, 508 crore data points a year). It is not a student AI curriculum. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **Rajasthan:** "Padhai With AI" and AI-powered assessments (45 lakh+ students assessed; 26 lakh+ AI reading tests in 10 days). This is AI used for assessment, not AI taught. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **Uttar Pradesh:** The PM SHRI expansion to 1,713 government schools is noted. A Kalpana Chawla Space Science & Innovation Lab (Classes 6-8) was announced. No UP statewide AI or coding curriculum was found. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **Maharashtra:** Only a Pune city-level item was found: 1,200 AI-enabled smart classrooms reaching 44,000 students. No state curriculum was found. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **CISCE (ICSE/ISC):**
  - Robotics & AI became an ICSE subject for Classes 9-10 from 2023-24 (subject code 66, a 100-mark paper). It was slated for ISC Classes 11-12 from 2025-26.
  - The curriculum was developed with IIT Delhi's Technology Innovation Hub (MoU).
  - No official circular was found making AI or robotics compulsory in Classes 1-8. "Tech Tinkerer"-type Class 1-8 offerings appear to be vendor products.

  — [Careers360](https://news.careers360.com/iit-delhi-technology-innovation-hub-help-design-cisce-syllabus-curriculum-in-robotics-ai-data-science-machine-learning/amp); [Analytics India Mag](https://analyticsindiamag.com/cisce-to-introduce-robotics-ai-ml-and-data-science-curriculum-teams-up-with-iit-delhi/); [Dinamalar](https://l-www.dinamalar.com/news/kalvimalar-news-en/-cisce-to-introduce-robotics-ai-for-classes-11-12-by-2025-26/52413); [Aasoka](https://aasoka.com/blog/cisce-reforms-academic-session-2025-26-ai-robotics-curriculum/)

### Inferences
- **States split into three models:**
  - **(a) In-textbook ICT/AI with plugged tools:** Kerala, and TN SPARK, which uses Scratch and Blockly. These are much more coding-forward than CBSE's no-coding Classes 3-8 curriculum.
  - **(b) Vocational/NSQF electives in secondary:** Karnataka, and CISCE's elective.
  - **(c) Political announcements awaiting curricula:** Punjab, Telangana, Haryana.
- **Kerala's lever is enabling infrastructure.** Its decades-old IT@School/KITE system (state-run lab hardware, FOSS tools and ICT textbooks) makes it the domestic proof that a state board can run plugged CT at scale. *(The history is from training data; the 2024-25 facts are cited above.)*
- **Many 2026 state "AI" initiatives use AI rather than teach it.** Gujarat VSK and Rajasthan assessments are examples. Comparisons with the US should keep that distinction.

### Gaps
- **Andhra Pradesh, Delhi, Maharashtra (statewide), Gujarat (student curriculum) and UP:** No verified 2025-26 school AI or coding curriculum announcements were found.
- **Whether state boards adopted the CBSE/NCERT CT&AI framework for 2026-27:** No count was found.
- **Independent evaluations:** None found for TN SPARK, Kerala's AI chapter, or Karnataka's NSQF AI course.

## 3. Teachers: workforce, training scale, pre-service (B.Ed.), shortages

### Takeaway
India has more than 1 crore (10 million) school teachers. CT/AI is to be taught by existing subject teachers, mainly maths and science, not by computer specialists. Training relies on NISHTHA/DIKSHA online modules and CBSE CPD. No official count of teachers trained specifically in CT/AI was found. Computer instructors in government systems are largely contractual and low-paid.

### Cited Findings
- **Teacher headcount:** Total school teachers crossed 1 crore for the first time in UDISE+ 2024-25, about 6% above 2022-23. — [Vision IAS on UDISE+ 2024-25](https://dce.visionias.in/news-today/2025-08-29/society/unified-district-information-system-for-education-plus-udise-2024-25-report-released-by-ministry-of-education); [Careers360](https://news.careers360.com/udise-2024-school-enrolment-drops-11-lakh-secondary-retention-at-47-teachers-1-crore-dropouts-gre-ptr-report-education-ministry/amp)
- **Single-teacher schools:**
  - National count of 1,04,125 in 2024-25, down from 1,10,971. Andhra Pradesh has the most such schools; UP has the most students in them.
  - Another report says over 33 lakh students are enrolled in single-teacher schools.
  - An analysis of UDISE+ 2025-26 says single-teacher schools rose again (16,357 in Andhra Pradesh alone).

  — [DoSEL/PIB PDF](https://dsel.education.gov.in/sites/default/files/update/PIB2161543.pdf); [ETV Bharat](https://www.etvbharat.com/en/!state/andhra-pradesh-tops-in-single-teacher-schools-udise-plus-report-enn25082902581); [ThePrint](https://theprint.in/india/education/over-33-lakh-indian-students-enrolled-in-schools-with-just-one-teacher-issue-most-stark-in-up-jharkhand/2733622); [Education for All in India, UDISE+ 2025-26](https://educationforallinindia.com/single-teacher-schools-schools-without-enrolment-udise-2025-26/)
- **NISHTHA scale (not AI-specific):** More than 63.17 lakh teachers were trained under various NISHTHA programmes in 2019-22, according to the Minister of State, December 2024. The original NISHTHA launch targeted 42 lakh elementary teachers. — [News On AIR, 16 Dec 2024](https://www.newsonair.gov.in/over-63-lakh-teachers-trained-under-different-nishtha-programs-from-2019-22); [Punekar News](https://www.punekarnews.in/?p=44571)
- **NISHTHA as the AI & CT channel:** The Ministry says NISHTHA modules and video resources are the foundation for the AI & CT rollout, and that training is "grade-specific and time-bound". Blogs call NISHTHA AI training "mandatory" on DIKSHA, but this was not confirmed officially. — [LatestLY/IANS](https://www.latestly.com/agency-news/india-news-ai-curriculum-teacher-training-will-be-done-through-nishtha-modules-video-based-learning-resources-7185608.html); [Extramarks blog](https://www.extramarks.com/blogs/schools/nishtha-2026-27-preparing-teachers-for-new-age-learning/)
- **Training-scale estimates:**
  - Reports say the government plans to train "nearly 10 million" (1 crore) teachers in AI.
  - An IIT expert estimated that the first phase (5 million teachers) needs about 200-500 core AI experts, about 10,000 master trainers and about 6 lakh district or cluster trainers.
  - Officials reportedly see teacher training as the biggest hurdle.

  — [The Secretariat](https://thesecretariat.in/article/india-s-schools-step-into-the-ai-era-with-nationwide-training-plan); [TechWire Asia, Nov 2025](https://techwireasia.com/2025/11/india-ai-curriculum-schools-2026/)
- **Who teaches:** TN SPARK and Tamil Nadu's statewide plan use maths and science teachers trained by SCERT, not computer teachers. — [Business Today](https://www.businesstoday.in/technology/news/story/tamil-nadu-launches-tn-spark-to-train-government-school-students-in-ai-coding-and-robotics-494009-2025-09-15); [Hans India](https://www.thehansindia.com/news/national/tn-plans-ai-emerging-technologies-curriculum-for-all-govt-schools-1100094)
- **Industry teacher training (older data):**
  - The Intel-CBSE MoU (March 2020) covered AI curriculum and educator training.
  - Intel's AI for Youth reached 1,13,487 students and 12,464 educators across 10,198 schools in 35 states and UTs, as reported in December 2021.

  — [YourStory, Dec 2021](https://yourstory.com/2021/12/indias-next-gen-innovators-intel-ai-programs-cbse-government-schools); [IndiaAI](https://indiaai.gov.in/news/intel-partners-cbse-to-teach-ai-in-high-school)
- **Contractual computer instructors:**
  - KVS hires part-time contractual "Computer Instructors" (BE/BTech, BCA, MCA or MSc CS/IT) each session.
  - A Puducherry government notice for "Instructor in Computer Science" offered Rs 8,500 a month on contract.

  — [KVS Kokrajhar 2024-25](https://kokrajhar.kvs.ac.in/sites/default/files/Contractual%20Teachers%20Interview%202024-25.pdf); [Puducherry notice](https://www.py.gov.in/sites/default/files/education-notification-appl.pdf)
- **Teacher AI literacy:** ORF cites a survey in which 70% of teachers used AI in the classroom but only 57% could identify basic AI misconceptions. — [ORF](https://www.orfonline.org/research/using-ai-to-protect-teaching-time-and-improve-learning-quality-in-indian-schools)

### Inferences
- India's model of a subject teacher plus online CPD is the opposite of a specialist CS-teacher model. It scales on paper, but depends on cascade training quality. Earlier NISHTHA cascades were criticised for completion-over-competence (not re-verified here).
- **Where specialists exist, they are poorly paid:** Pay for contractual ICT instructors (about Rs 8,500 a month in at least one UT) signals low status and high churn. This is relevant to any ICT lab's functionality.

### Gaps
- **National count of computer/CS teachers:** Not found; UDISE+ subject-wise teacher data was not retrieved.
- **Teachers trained specifically in CT/AI in 2025-26:** No official count found, whether via NISHTHA, CBSE CPD or SOAR's educator track.
- **Pre-service (B.Ed. / ITEP):** No source checked on whether the NCTE's 4-year Integrated Teacher Education Programme or B.Ed. syllabi include CT/AI.
- **Microsoft and Google teacher AI programmes in India:** No 2025-26 figures found. A Google-UNICEF 3-year AI education partnership covering India was noted ([Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)), but no India-specific numbers.

## 4. Infrastructure: UDISE+ computers/internet, ICT labs sanctioned vs functional, smart classrooms, student devices

### Takeaway
UDISE+ 2024-25 (released 28 August 2025) reports 64.7% of schools with computers and 63.5% with internet, up sharply year on year. The government-private gap is large: internet is about 58.6% in government schools vs 77.1% in private ones, and computers in Bihar government schools are 16.5% vs 72% in private schools. Samagra Shiksha has sanctioned about 1.5-1.8 lakh ICT labs and a similar number of smart classrooms, but functional counts lag sanctions. At home, about 90% of rural 14-16-year-olds have a smartphone in the household, but only 27-38% own one.

### Cited Findings
- **UDISE+ 2024-25 national figures:**
  - Schools with computers: 64.7%, up from 57.2% in 2023-24.
  - Schools with internet: 63.5%, up from 53.9%.
  - Internet is at 100% in Chandigarh, Delhi and Lakshadweep.

  — [ThePrint, 29 Aug 2025](https://theprint.in/india/education/govt-report-flags-digital-divide-in-schools-25-in-bihar-bengal-have-computer-facilities-65-nationally/2731591); [PIB UDISE+ release, 28 Aug 2025 (mirror)](https://educationforallinindia.com/wp-content/uploads/2025/08/PIB-UDISEPlus-2024-25-Press-Release-August-28-2025.pdf); [Education for All in India](https://educationforallinindia.com/?p=19653)
- **Lagging states (UDISE+ 2024-25):**
  - Computers: Bihar 25.2% overall (government 16.5%, private 72%); West Bengal 25.1% (government 21.3%, private 53.3%); Meghalaya 19.7%.
  - Internet: West Bengal 18.6%.

  — [ThePrint](https://theprint.in/india/education/govt-report-flags-digital-divide-in-schools-25-in-bihar-bengal-have-computer-facilities-65-nationally/2731591)
- **Government vs private internet:** About 58.6% vs 77.1%. These are secondary current-affairs summaries of UDISE+ 2024-25, not checked against the UDISE+ tables. — [RACE IAS](https://mail.raceias.com/current-affairs/udise-report); [TechWire Asia](https://techwireasia.com/2025/11/india-ai-curriculum-schools-2026/)
- **State-wise UDISE+ facilities tables (2024-25):** — [State-wise share of schools by facilities, UDISE+ 2024-25 (mirror PDF)](https://educationforallinindia.com/wp-content/uploads/2025/10/State-wise-share-of-schools-by-facilities-UDISEPlus-2024-25-Ministry-of-Education.pdf); [MoE Parliament annexure on functional computer labs in government schools](https://www.education.gov.in/sites/upload_files/mhrd/files/parliament_annexure_en/1561_en.pdf) (not opened)
- **Electricity:** Over 25,000 schools still lacked electricity in 2024-25. — [Education for All in India](https://educationforallinindia.com/63-percent-of-indian-schools-now-online-yet-over-25000-languish-without-electricity/)
- **"Functional computers" vs "computers available":** Commentary citing UDISE+ says only about 58% of schools have functional computers. That is lower than the 64.7% availability figure, and the definitions differ. — [Education for All in India](https://educationforallinindia.com/ai-in-indian-school-education-opportunities-and-challenges-for-universal-access/)
- **Samagra Shiksha ICT labs and smart classrooms (figures conflict by date and source):**
  - As of 31 May 2025, 1,46,040 smart classrooms had been approved (Lok Sabha).
  - A secondary summary gives 1,56,213 ICT labs approved, of which 1,14,552 were functional (about 73%), and 86,753 smart classrooms functional (about 59% of approved). The functional figures were not confirmed against the reply itself.
  - On the PRABANDH portal the Minister cited 1,76,669 ICT labs and 1,75,936 smart classrooms sanctioned (undated).
  - An older MoE review gave 1,20,614 ICT labs sanctioned vs 78,498 functional (65%), and 82,120 smart classrooms sanctioned vs 9,833 functional (12%).
  - A Lok Sabha reply of 28 July 2025 approved 20,456 more ICT labs (Rs 911.13 crore) to saturate functional secondary and senior secondary schools.

  — [Free Press Journal](https://www.freepressjournal.in/amp/education/146-lakh-smart-classrooms-in-schools-approved-till-may-31-minister-of-education-dharmendra-pradhan); [LS reply PDF](https://www.education.gov.in/sites/upload_files/mhrd/files/parliament_annexure_en/LSUQNo-47.pdf); [DoSEL review minutes](https://dsel.education.gov.in/sites/default/files/4MoM.pdf); [ICT Samagra scheme page](https://dsel.education.gov.in/scheme/ict-samagra)
- **Fund utilisation:** Punjab reportedly spent only one-third of its digital-education funds. — [News Minimalist (aggregator)](https://www.newsminimalist.com/articles/punjab-spent-one-third-of-digital-education-funds-4dde2a39)
- **Jammu & Kashmir:** It got approval for 1,915 ICT labs and 3,910 smart classrooms over 2021-22 to 2025-26, per a Lok Sabha reply reported in 2026. — [Kashmir Life](https://kashmirlife.net/centre-approves-1915-ict-labs-3910-smart-classrooms-for-jammu-kashmir-schools-445102/)
- **ASER 2024 (rural; digital module for ages 14-16, 605 districts, published January 2025):**
  - About 90% have a smartphone at home and about 82% can use one.
  - Personal ownership is 27% of 14-year-olds and 37.8% of 16-year-olds.
  - Among users, more than half used a phone for education in the reference week and about 75% used social media.
  - About 70% of boys vs 62% of girls could bring a smartphone to do the digital tasks.
  - 65.9% nationally could do the digital tasks; Nagaland was 82.7%. Denominators vary across reports.

  — [ThePrint](https://theprint.in/india/education/in-rural-india-82-2-teens-aged-14-16-know-how-to-use-smartphone-but-only-57-use-it-for-studies/2467560); [Ideas for India](https://www.ideasforindia.in/topics/human-development/youth-s-digital-readiness-in-rural-india.html); [Careers360](https://news.careers360.com/aser-report-says-over-56-percent-children-14-16-age-group-use-smartphone-for-educational-purpose/amp); [Morung Express](https://morungexpress.com/nagalands-rural-youth-show-strong-digital-skills)

### Inferences
- **The "no coding, unplugged" CBSE design fits these numbers.** About one-third of all schools have no computer, and the figure is well under half for government schools in the poorest states. In US terms, India is designing for a device-poor median school.
- **Home devices are shared, not personal.** Household smartphones are near-universal but personal ownership is low and gendered. Home-based digital CT practice would disadvantage girls and younger children.
- **Sanctioned-vs-functional is the core implementation gap.** Older data show only 12% of sanctioned smart classrooms functional, and roughly 65-73% of ICT labs. Reasons include procurement delays, electricity and connectivity, maintenance contracts and contractual instructors (inferred; see Section 7).

### Gaps
- **Official UDISE+ 2024-25 computer and internet figures by management type:** Not retrieved nationally. The parliamentary annexure exists but was not opened.
- **UDISE+ 2025-26:** Infrastructure figures not retrieved; only single-teacher data was seen.
- **Smart-class share in UDISE+ 2024-25:** Not found.

## 5. Assessment and outcomes: PARAKH, PISA 2025, Bebras India, Indian CT studies

### Takeaway
India has no national assessment of CT or AI literacy. India did not take part in PISA 2025, so it has no data on PISA's "Learning in the Digital World" innovative domain. Bebras India (ACM India CSpathshala) is the only large CT assessment-like activity, with national participation in the tens of thousands (Goa alone had 16,000+ registrants). No rigorous evaluations of CT/AI interventions in Indian schools were found in this pass.

### Cited Findings
- **PISA 2025:** India declined to take part, reported March 2025. The government cited pandemic learning gaps, reversing an earlier commitment. India's only PISA participation was 2009+ (Tamil Nadu and Himachal Pradesh), where it ranked 73rd of 74. — [The Wire](https://thewire.in/education/india-opts-out-of-pisa-2025); [The Morning Context](https://www.themorningcontext.com/internet/india-declines-to-participate-in-pisa-in-2025-yet-again); [EducationWorld](https://www.educationworld.in/india-says-no-to-pisa-test-again)
- **Bebras India Challenge:**
  - Organised by ACM India's CSpathshala; free, online, for ages 8-19, in 12 languages.
  - The 2025 edition ran 3-25 November 2025.
  - In Goa (via SCERT), 16,000+ students participated and 8,912 completed it.
  - The 2021 edition had 22,000+ students from 260+ schools in 16 states.

  — [Bebras India (about)](https://sites.google.com/view/bebrasindia/about); [Bebras India register](https://sites.google.com/view/bebrasindia/register); [Herald Goa](https://www.heraldgoa.in/goa/goa/6-goan-students-rank-best-in-india-at-computational-thinking-contest/418235); [GD Goenka](https://gdgps.gdgoenka.com/news/bebras-india-thinking-challenge-2021-winners)
- **AI used for assessment:** Rajasthan assessed 45 lakh+ students and ran 26 lakh+ AI reading tests in 10 days. This is AI for assessment, not assessment of AI. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **CBSE CT&AI assessment design:** Assessment from Class 6 relies on projects, presentations, reflective journals and assignments rather than exams. *(Covered elsewhere; mentioned only as context.)* — [PiyushAI blog](https://www.piyushwairale.com/blog/ct-ai-teacher-training-for-cbse-2026-27-computational-thinking-artificial-intelligence)

### Inferences
- **India lacks external CT benchmarks.** Without PISA participation and with PARAKH/NAS not measuring CT (see Gaps), there is no way to measure whether the 2026-27 curriculum improves CT. A cheap lever is to use Bebras-style tasks, which already exist in 12 Indian languages, as a diagnostic.

### Gaps
- **PARAKH:** No source found on whether PARAKH Rashtriya Sarvekshan (November 2024 cycle) or any planned cycle measures CT or digital competencies. The 2024 survey covered Grades 3, 6 and 9 in language, maths, EVS/science and social science; this is training data, not verified here.
- **Bebras India national totals for 2024 or 2025:** Not found.
- **Peer-reviewed Indian studies** (for example CSpathshala, IIT Bombay, IIT Gandhinagar CCL, CT effect sizes): Not retrieved in this pass.

## 6. Industry and civil society

### Takeaway
Industry programmes, led by Intel, have shaped India's AI school curriculum since 2019-20. A wide fringe of corporate-CSR and NGO pilots now runs in government schools (Amazon, Cyient, Google-UNICEF, Magic Bus, ILP), but each typically reaches tens of thousands of students, not millions, and has no published evaluation.

### Cited Findings
- **Intel:** Intel-CBSE MoU (March 2020). AI for Youth reached 1.13 lakh students, 12,464 educators and 10,198 schools by December 2021. With the Ministry of Education and CBSE, it co-created "AI for All" (4 h, 2021). — [YourStory](https://yourstory.com/2021/12/indias-next-gen-innovators-intel-ai-programs-cbse-government-schools); [HRKatha](https://www.hrkatha.com/news/intel-and-cbse-to-make-prepare-students-for-ai/); [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **CBSE's existing AI electives:** These are Class 8-10 electives (code 417 in Class 9-10) with AI integration across subjects, and schools must apply for approval. IBM SkillsBuild/1M1B developed the Class 11-12 AI elective. — [CBSE AI Integration Manual](https://cbseacademic.nic.in/web_material/Curriculum20/AI_Integration_Manual.pdf); [1M1B Wikipedia](https://en.wikipedia.org/wiki/1M1B)
- **Amazon:** Coding and AI modules in 100 Karnataka schools (headline). — [Careers360](https://news.careers360.com/amazon-introduce-advanced-coding-and-ai-modules-in-100-karnataka-schools/amp)
- **Cyient Foundation VijAIpatha (Karnataka):** 5 schools, 2,000+ students, 200+ teachers. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **Magic Bus India Foundation with Chhattisgarh:** 800 schools, 40,000 students, 1,600 teachers. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **Google and UNICEF:** A 3-year AI education partnership covering India, Brazil, Pakistan and Kenya. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **Robotex India:** 24,000+ government-school students. — [Organiser](https://organiser.org/2026/07/12/369461/bharat/how-nep-2020-is-building-future-ready-schools-through-14-ai-initiatives/)
- **ILP with TN SPARK:** 340 schools, 67,000 students, 46 facilitators. — [ILP](https://www.ilpnet.org/transforming-67000-young-learners-with-practical-tech-education/)
- **ACM India CSpathshala:** Runs Bebras India (see Section 5). — [Bebras India](https://sites.google.com/view/bebrasindia/about)
- **IIT Madras:** Chairs the CBSE CT&AI expert committee (Prof. Karthik Raman). — [EducationWorld](https://educationworld.in/ai-and-computational-thinking-to-be-taught-from-class-3-in-all-schools-from-2026-27/)
- **IIT Delhi Technology Innovation Hub:** Co-designed CISCE's Robotics/AI curriculum. — [Careers360](https://news.careers360.com/iit-delhi-technology-innovation-hub-help-design-cisce-syllabus-curriculum-in-robotics-ai-data-science-machine-learning/amp)
- **Navneet AI:** 500+ schools, 2,000 teachers, 14 states. — [The Secretariat](https://thesecretariat.in/article/india-s-schools-step-into-the-ai-era-with-nationwide-training-plan)

### Inferences
- **Industry content is entrenched, which carries vendor-content risk.** CBSE's AI electives grew from Intel and IBM content, and the 2026 national design relies on IIT-led committees. India's AI education content is co-produced with industry far more than India's CT content (maths-integrated, NCERT/CBSE-led).

### Gaps
- No 2025-26 figures were found for Intel's "AI for Citizens" or AI for Youth, Microsoft, Google India teacher training, Amazon Future Engineer India totals, Tata (STRIVE/Tata ClassEdge), Wadhwani AI, Pratham, IIT Madras "Bodhan AI", or IIT Gandhinagar CCL. These were not retrieved in this pass and should not be asserted without sources.
- No information was found on AIM's corporate ATL partnerships (for example, ATL "Mentor India", or AI modules with Intel, Microsoft or Amazon) for 2025-26.

## 7. Gaps and improvement levers: what researchers, government bodies and think tanks say

### Takeaway
The recurring diagnosis has five parts:
- **Teachers:** not enough trained teachers, and too much reliance on cascade or online CPD.
- **Devices:** an infrastructure gap between sanctioned and functional ICT, sharpest in government schools in eastern and north-eastern states.
- **Measurement:** no external measurement, and no PISA participation.
- **Coordination:** fragmentation across ministries (MoE, MSDE, MeitY, NITI) and between Centre and states.
- **Language and age:** age-appropriateness and language needs.

Evidence-based levers visible in India's own record: Kerala's state-owned ICT system, TN's bilingual textbooks with subject teachers, Bebras' 12-language unplugged tasks, ATL saturation, and functional-lab monitoring on PRABANDH.

### Cited Findings
- **NITI Aayog (around May 2026):** Teacher shortages, uneven infrastructure, digital access gaps in small and remote schools, and governance weaknesses. It recommends better teacher management, digital and broadcast learning, and AI in pedagogy and planning. — [Business Standard](https://www.business-standard.com/education/news/niti-flags-gaps-in-school-education-system-calls-for-ai-led-reforms-126050700823_1.html)
- **ORF:**
  - Use AI to protect teaching time, not to replace teachers.
  - AI tools should be free or affordable for government and low-fee schools.
  - Public-private partnerships could subsidise AI assistants so the divide does not widen.
  - Teachers' AI misconceptions persist (70% use AI vs 57% able to identify basic misconceptions).

  — [ORF](https://www.orfonline.org/research/using-ai-to-protect-teaching-time-and-improve-learning-quality-in-indian-schools)
- **Experts and teacher unions (The Secretariat):**
  - Assess trainer capacity before rollout (the IIT estimate of master trainers is in Section 3).
  - The All India Primary Teachers Federation says the urban-rural digital divide must be closed first and lessons must be age-appropriate.
  - Experts raise data privacy, bias and misinformation, and "AI replacing thinking".
  - They recommend teacher-controlled guardrails and source-check prompts, and Centre-State coordination.

  — [The Secretariat](https://thesecretariat.in/article/india-s-schools-step-into-the-ai-era-with-nationwide-training-plan)
- **International benchmarks cited in Indian debate:** Beijing has required at least 8 hours a year of AI education since 2025, and Hong Kong 10-14 hours of AI at junior secondary since 2023. 55.6% of countries are developing AI curricula. — [The Secretariat](https://thesecretariat.in/article/india-s-schools-step-into-the-ai-era-with-nationwide-training-plan)
- **PISA non-participation critique:** Commentators argue that withdrawing "citing learning loss during Covid" is unsound, because it removes international benchmarking. — [Deccan Herald, "Why PISA matters"](https://www.deccanherald.com/opinion/why-pisa-matters-3169865); [The Wire](https://thewire.in/education/india-opts-out-of-pisa-2025)
- **Sanctioned-vs-functional gap as a monitoring problem:**
  - Older MoE review: 9,833 of 82,120 smart classrooms functional and 78,498 of 1,20,614 ICT labs functional.
  - The 2025 ICT lab approvals are explicitly aimed at "functional" secondary schools.

  — [DoSEL review minutes](https://dsel.education.gov.in/sites/default/files/4MoM.pdf); [LS reply](https://www.education.gov.in/sites/upload_files/mhrd/files/parliament_annexure_en/LSUQNo-47.pdf)
- **Digital divide commentary:** Specialised AI training reaches only a fraction of teachers despite Samagra Shiksha digital-literacy training. — [Education for All in India](https://educationforallinindia.com/ai-in-indian-education-promise-of-inclusion-meets-the-reality-of-divides/)
- **Domestic levers that already work at some scale:**
  - **Kerala:** A state-owned ICT textbook series from Class 1, Scratch/PictoBlox, Python in Classes 9-10, and AVGC/AI integration. — [Onmanorama](https://www.onmanorama.com/career-and-campus/top-news/2025/08/24/kite-ict-textbooks-launch.amp.html)
  - **Tamil Nadu:** Bilingual textbooks, maths and science teachers as instructors, and phased scale-up from 85 to about 5,000 schools in 10 months. — [Business Today](https://www.businesstoday.in/technology/news/story/tamil-nadu-launches-tn-spark-to-train-government-school-students-in-ai-coding-and-robotics-494009-2025-09-15); [NewKerala](https://www.newkerala.com/news/a/tn-plans-ai-emerging-technologies-curriculum-all-govt-880.htm)
  - **Bebras India:** Free unplugged CT tasks in 12 languages; Goa ran it through SCERT for 16,000+ students. — [Herald Goa](https://www.heraldgoa.in/goa/goa/6-goan-students-rank-best-in-india-at-computational-thinking-contest/418235)
  - **ATLs:** Saturation of government secondary schools via the 50,000 lab target. — [MoE PIB PDF](https://education.gov.in/sites/upload_files/mhrd/files/PIB2098805.pdf)

### Inferences (improvement levers, derived from the cited evidence above)
1. **Fund maintenance as well as hardware.** The main infrastructure lever is converting sanctioned ICT labs and smart classrooms into functional ones. Tie Samagra Shiksha releases to functional status on PRABANDH/UDISE+, and fund multi-year maintenance, electricity and connectivity, plus a non-contractual lab coordinator.
2. **Keep CT unplugged at primary, but plan for plugged CT at middle and secondary.** Kerala and TN show state boards can deliver block coding with modest hardware. The 50,000 ATLs and about 1.5-1.8 lakh ICT labs could carry Class 6-10 project hours if they are scheduled for timetabled use, not just extracurricular tinkering.
3. **Use a subject-teacher model with a real coaching layer.** Most CT/AI teaching will be done by maths and science teachers, so cascade quality matters most. The IIT estimate (about 10,000 master trainers and about 6 lakh cluster trainers) suggests BRC/CRC (block and cluster resource centre) and DIET (district teacher-education institute) structures should be resourced explicitly. Pre-service (ITEP/B.Ed.) inclusion is an unverified gap.
4. **Measure CT.** Add CT items to PARAKH, reconsider PISA participation (2029 cycle), and use Bebras tasks, already available in 12 languages, as a low-cost diagnostic.
5. **Make language a design input.** Follow TN's bilingual-textbook model and Bebras' 12-language approach, rather than English-first AI content inherited from industry.
6. **Rationalise the ministry-specific programmes into one coherent pathway.** Today they are separate: MoE CT&AI, MSDE SOAR, MeitY YUVAi, NITI/AIM ATL, and state pilots. They could map to one progression, with a clear distinction between AI-use-for-governance (Gujarat, Rajasthan) and AI-literacy curricula.
7. **Address equity at home.** Shared, gendered smartphone access (ASER 2024) argues against homework that needs a device. Scheduled in-school device time should come first.

### Gaps
- **Think tanks:** No 2025-26 reports were found from Central Square Foundation, Centre for Policy Research or Brookings India specifically on CT/AI in schools. Brookings India rebranded as CSEP in 2020; not searched.
- **CAG / standing committees:** No CAG performance audit or Parliamentary Standing Committee on Education report on ICT@Schools or Samagra Shiksha ICT was retrieved in this pass. Earlier CAG audits of ICT@Schools exist in several states (training-data knowledge; not verified).
- **Policy churn:** CBSE's Class 9 CT&AI deferral (Acad-70/2026) is covered elsewhere. No other systematic list of reversals was compiled; PISA 2022 and 2025 withdrawals are the clearest documented examples.
