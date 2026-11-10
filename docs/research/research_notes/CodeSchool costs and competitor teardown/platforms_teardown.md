# School-facing coding, CT and AI platforms in India: product teardown for CBSE Classes 3-8 (2026-27)

Research date: 10 November 2026. Scope: India, Classes 3-8, products competing for CBSE CT&AI hours. These notes build on the earlier report `reports/CT kit competitors buying and compliance.md` and mostly cover what each product contains rather than repeating its prices. **Convention:** "Claim" means the company says it about itself (website, press release, sponsored article). "Verified" means a primary or independent document confirms it (a CBSE document, an RoC filing as reported by Entrackr or Inc42, a school booklist, or an app-store aggregator).

## Q1. What does the CBSE 2026-27 CT&AI curriculum actually require? (the yardstick for "aligned" claims)

### Takeaway
CBSE's own design is **mostly unplugged, free-tool-first and platform-agnostic**. In Classes 3-5 it is pure CT built into Maths and The World Around Us (TWAU) periods, with no AI. In Classes 6-8 it is 100 hours: 40 hours of advanced CT, 20 hours of introductory AI and 40 hours of projects (two a year). Assessment explicitly expects **no programming and no computer access**. A vendor claiming "CBSE CT&AI aligned" because it teaches Scratch or Python on a laptop is therefore aligned with the spirit at most, not the letter. The gaps CBSE itself says are "coming soon" (the AI project list with rubrics, and concept handouts) are the clearest openings.

### Cited Findings
- **Verified (CBSE webinar deck, 2026-27):**
  - **Structure:** The Preparatory Stage (Classes 3-5) runs **50 hours a year**, "CT only – no AI yet". It is "integrated into Mathematics & The World Around Us", "worksheet- and puzzle-based", taught by existing subject teachers with "no additional load – embedded into existing Mathematics & TWAU periods". The Middle Stage (Classes 6-8) runs **100 hours a year**: advanced CT (40 hours), introductory AI (20 hours) and interdisciplinary projects (40 hours, two projects), with "subject teachers + computer teachers, in collaboration". Hours are "indicative" — [CBSE CT&AI Webinar PPT 2026-27](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf)
  - **Who teaches what:** In Classes 6-8, CT is delivered through Maths, Science and Social Science "similar to art-integrated learning", and "the AI Literacy and Interdisciplinary Project components are anchored by the Computer teacher". In Classes 3-5 CT "should be integrated into the existing chapter sequence and not added as a separate block" — [CBSE webinar PPT](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf)
  - **Tools:** The curriculum is "platform agnostic… free and open-source first… largely unplugged… A significant portion of CT learning happens with paper, puzzles, and discussion – no computer required. AI activities use simple digital tools where available." It also says students "don't need to write code or train models" — [CBSE webinar PPT](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf)
  - **Assessment:** End-of-chapter work uses MCQs, fill-in-the-blanks, short answers and "think and apply" questions. "There is no 'write a program'… no expectation of computer access for assessment" — [CBSE webinar PPT](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf)
  - **Projects:** Sample projects are Grade 6 "Exploring Weather and its Impact across States", Grade 7 "Nutri-Quest: Weekly Food Planner" and Grade 8 "Sports Participation and Performance Data". Each "culminates in a presentation, not a written exam" — [CBSE webinar PPT](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf)
  - **Resources:** Available now are the framework and a teacher handbook and student handbook for each grade. Listed as "coming soon / over the coming months" are a dedicated CT&AI page, "Concept Handouts" for the AI sections, and an "AI Project list with rubrics (40 hours, two projects per grade)" — [CBSE webinar PPT](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf)
  - **Training:** The 2026-27 training theme is "Computational Thinking and Understanding AI". Formats are District Level Deliberations (offline, one day, 6 CPD hours), half-day expert talks run by lead schools (3 CPD hours), Board-run regional workshops, and DD PM e-Vidya CBSE channel 15 — [CBSE webinar PPT](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf)
- **Verified:** CBSE launched the framework on 1 April 2026. The syllabi were prepared by faculty from IIT Madras, Azim Premji University and Dhirubhai Ambani School, curated with IIT Gandhinagar's Centre for Creative Learning, and approved by NCERT. **No corporate partner (Microsoft, Google, Intel, IBM) is named** — [Careers360](https://news.careers360.com/cbse-syllabus-computational-thinking-ai-artificial-intelligence-class-3-8-ncert-scert-iit-madras-gandhinagar-pisa-semiconductor/amp)
- **Verified:** The earlier CBSE AI offering for Classes 6-8 was a 15-hour "Skilling for AI Readiness" (SOAR) module, offered in more than 18,000 CBSE schools — [StudyBase / newsbytes summary via search](https://studybase.in/blogs/ministry-ai-curriculum-analysis) (secondary). The CBSE circular also states that other AI courses run until 2025-26 "stand discontinued for Class 9 from session 2026-27" — [CBSE Circular 18/2026](https://cbseacademic.nic.in/web_material/Circulars/2026/18_Circular_2026.pdf) (quoted in a search snippet; the full circular was not read)

### Inferences
- The strongest alignment claim any vendor can honestly make is "mapped to CBSE CT&AI learning outcomes, with activities that work unplugged". CodeSchool's offline-capable, shared-device design fits CBSE's "no computer required" stance better than lab- or 1:1-device products do, and this can be shown from CBSE's own deck.
- In Classes 3-5, CBSE wants CT inside Maths and TWAU periods, so a product sold as a separate "coding period" competes with the old Computers period, not with CT&AI hours. Products that index to NCERT Maths chapters fit the design. None found do this (see Q2 and Q3).
- The 40-hour project block in Classes 6-8 is anchored by the computer teacher and has no published rubrics yet. This is the one place where a digital tool (data collection, simple charts, a Teachable-Machine-style model) is useful but not mandated.

### Gaps
- The full framework PDF (CTAI_Pri_2026-27.pdf) was not text-extracted, so the exact learning-outcome codes are not listed here.
- Whether CBSE has published the project rubric list since the webinar (as of 10 Nov 2026) was not confirmed.

## Q2. What do the integrated school programmes (book + platform + training) contain?

### Takeaway
Uolo's Tekie is the only integrated programme found that is visibly sold **as** the CT&AI line in 2026-27, through school booklists. LEAD bundles coding inside a whole-school system and has heavy lab and teacher prerequisites. Extramarks, Teachmint, Next Education and Eduvate sell smart-class, ERP or robotics programmes, and none of them publicly lists a CT&AI-specific Classes 3-8 product with contents. None publishes offline capability for the student platform, and none publishes a data-protection posture beyond a privacy-policy link.

### Cited Findings

**Uolo — Tekie / "Tekie.AI" (Grades 1-8)**
- **Claim:** Sold as a Grades 1-8 computer science programme "starting @ Rs 799/student/year". It includes storytelling course books, animated videos, a coding platform "accessible from home", hands-on projects, robotics-kit projects, simulations and simple games, and "virtual environments". Teacher tools are automated attendance, auto-graded homework, an interactive teacher manual (e-book), a test-paper generator and year-round teacher training. Scale claimed is "500K+ students from 1000+ schools" and "160 million+ minutes of practice per month". The page names no block or Python language, does not mention CT&AI, and states no device, internet or offline requirements — [Uolo Tekie page](https://uolo.co/tekie.html)
- **Conflicting scale claim:** Search snippets of Uolo material say "trusted by 15,000+ schools across India, Southeast Asia and the Middle East". That figure is likely Uolo-wide across all products, not Tekie alone — [Uolo, search snippet](https://uolo.co/tekie.html); contrast with the "1000+ schools" figure on the same Tekie page
- **Verified (published books):** Uolo publishes a "Tekie.AI Computer Science" content book plus separate "Coding" books for Grades 1-8 (AY26 editions, with AY27 ebooks appearing). The books carry "NEP 2020 aligned" and "ICSE compliant" labels and a "digital coding platform included" note. A Grade 7 teacher manual is filed as "cbse_cs_g7_tm". The series "places Artificial Intelligence at its core" — [Issuu, Tekie Coding Book 8 AY26](https://issuu.com/tekie-app/docs/tekie.ai_computer_science_coding_book_8_ay26); [Issuu, Coding Book 7 AY27 ebook](https://issuu.com/tekie-app/docs/tekie.ai_computer_science_coding_book_7_ay27_ebook); [Issuu, CBSE CS G7 TM](https://issuu.com/tekie-app/docs/cbse_cs_g7_tm_ebook)
- **Verified (booklist adoption, from the earlier report):** City Montessori School, Lucknow lists "Tekie.AI – Accelerate" for 2026-27 under "Computational Thinking & ICT" at Rs 579 (Grade 4) to Rs 629 (Grades 6-8) — [CMS booklist](https://cmseducation.org/wp-content/uploads/2026/03/Classes-IV-to-VIII-2026-2027.pdf)
- **Verified (apps):** "Uolo Learn" is the student and parent app ("Tekie coding program… for students and parents connected to schools using Uolo") and "Uolo Teach" is the teacher app. Both are on the Apple App Store. No Google Play install count was found — [App Store, Uolo Learn](https://apps.apple.com/in/app/uolo-learn/id1627069461); [App Store, Uolo Teach](https://apps.apple.com/am/app/uolo-teach/id1621265109)
- **Funding and finances (verified via press):**
  - $7M round led by Five Sigma (Blume, Morphosis and Alicorn also participating), around December 2025 — [Outlook Business](https://www.outlookbusiness.com/start-up/investors/edtech-start-up-uolo-bags-7-mn-funding-from-five-sigma-other-investors); [Entrepreneur India](https://india.entrepreneur.com/news-and-trends/edtech-startup-uolo-bags-usd-7-mn-funding-led-by-five-sigma/500656)
  - Total raised is about $32.5M across 6 rounds — [CB Insights](https://www.cbinsights.com/company/uolo/financials)
  - FY24 revenue was about Rs 27.9 crore (+355%) — [Indian Startup Times](https://www.indianstartuptimes.com/?p=26900). The FY24 loss was Rs 58.11 crore — [TheKredible](https://thekredible.com/blogs/uolo-revenue-surges-4-5x-in-fy24-losses-narrow-to-rs-58-11-crore)
  - FY25 figures were not found.

**LEAD Group — LEAD School system, TECHBOOK, Coding & Computational Skills (CCS)**
- **Claim (2022 product article):** CCS covers Classes 1-8 in two 40-minute periods a week over a 26-week programme. Each unit follows a "Use, Think, Build" sequence, with 5-6 projects (for example a notes-sharing website, tic-tac-toe, snakes and ladders). Tools include Scratch Jr (Grade 3 maze puzzles) and Python (a Grade 6 Pythagoras visualisation).
  - **Prerequisites:** One computer per 2-3 students, a lab with internet ("optional for primary, essential for middle school") and a TV in both the classroom and the lab.
  - **Teachers:** Must complete LEAD training. Classes 6-8 teachers need a BCA, MCA or equivalent.
  - **Not stated:** Dashboard, pricing, offline use.
  - [LEAD School blog, 9 Dec 2022](https://leadschool.in/teaching-coding-to-kids-ccs-is-here-to-help-your-school)
- **Claim:** TECHBOOK, launched in September 2024, is an NCF-mapped paper textbook for Classes 1-8 that started with English, Maths and Science. LEAD projects that the "top 5,000 schools" will upgrade to Techbooks within four years — [Education21](https://education21.in/lead-group-launches-techbook-mapped-to-ncf-for-classes-1-8-expects-top-5000-schools-to-upgrade-to-techbooks-in-next-4-years); [CXOToday](https://cxotoday.com/press-release/lead-groups-techbook-set-to-disrupt-student-learning-in-india/)
- **Claim:** LEAD reports 9,000+ schools, 4.1M+ students and 65,000+ teachers in 400+ cities — [LEAD School](https://leadschool.in/)
- **Verified (RoC via press):** FY25 operating revenue was Rs 351.8 crore (+0.4%), the net loss was cut about 70% to Rs 43.3 crore, and EBITDA loss was about Rs 1 crore — [Entrackr](https://entrackr.com/fintrackr/edtech-unicorn-lead-cuts-losses-by-70-revenue-remains-flat-10462343); [Inc42](https://inc42.com/?p=526226). FY26 revenue rose about 10% to Rs 387 crore and the loss narrowed about 20% to Rs 34.5 crore — [YourStory, Aug 2026](https://yourstory.com/2026/08/edtech-lead-fy26-revenue-rises-387-crore-losses-narrow-over-20-percent); [Inc42](https://inc42.com/?p=570148)
- No evidence was found of a LEAD product labelled for CBSE CT&AI 2026-27.

**Extramarks — Smart Class Plus**
- **Claim:** Smart Class Plus launched in June 2023. It is an NEP-aligned content, assessment and classroom-management platform in Basic, Advanced and Pro tiers, with AI-driven "personalized learning paths, adaptive assessments" and an offline test feature ("create… offline tests with question bank; scan and upload for automated grading") — [Extramarks Smart Class Plus](https://www.extramarks.com/smart-class-plus); [eLearning Industry listing](https://elearningindustry.com/directory/elearning-software/extramarks-smart-class-plus)
- Extramarks has published CT&AI blog content (8 Oct 2026; 14 Jul 2026) but **no CT&AI Classes 3-8 product page was found** — [Extramarks blog](https://www.extramarks.com/blogs/schools/ai-computational-thinking-the-new-skills-shaping-cbse-classrooms/)
- **Verified (RoC via press):** FY24 revenue fell 37% to Rs 233 crore and the loss fell 85% to Rs 48 crore. Reliance's Infotel reportedly took a 38.5% stake in 2023 — [Entrackr](https://entrackr.com/fintrackr/extramarks-losses-drop-by-85-to-rs-48-cr-in-fy24-revenue-slips-37-8713664). FY25 figures were not found.
- Do not confuse Extramarks with **Ebix Smartclass**, which separately announced an "AI School" programme (Grades 1-12: AI, coding, robotics, IoT) targeting 1 crore students. That is a claim — [The Machine Maker](https://themachinemaker.com/news/ebix-smartclass-launches-ai-school-program-to-empower-1-crore-students-with-coding-and-ai-skills/)

**Teachmint — ERP plus interactive flat panels (Teachmint X / X2)**
- **Claim:** Teachmint X is an interactive flat panel with an inbuilt CPU and "EduAI" assistant tools (quizzes, explanations, lesson prompts, lecture summarisation). X2 is a Google EDLA-certified Android 14 panel with an on-device NPU, announced in March 2026 — [ThePrint/ANI press release](https://theprint.in/ani-press-releases/teachmint-launches-teachmint-x2-google-edla-certified-ai-interactive-flat-panel/2515375); [Teachmint blog](https://blog.teachmint.com/interactive-flat-panel-for-classrooms-in-india-2026)
- **Verified (RoC via press):** FY25 operating revenue rose about 4.3x to Rs 74 crore and the loss fell 57% to Rs 46.6 crore. Product (hardware) sales were the sole revenue source, which brings inventory risk — [Entrackr](https://entrackr.com/fintrackr/teachmints-revenue-jumps-43x-in-fy25-10550884); [Indian Startup Times](https://www.indianstartuptimes.com/startup-deep-dive/teachmint-deep-dive/)
- No Teachmint CT&AI curriculum or coding product was found.

**Eduvate (letseduvate.com) — robotics and coding programme**
- **Claim:**
  - Content: Coding and robotics modules "for students across all grade levels", built on robotics kits, "coding platforms", gamified challenges and team projects.
  - Teacher support: "Ready-to-use lesson plans, teaching guides", teacher workshops, assessment tools and "progress-tracking frameworks".
  - Not stated: languages, devices, pricing, partner count or any board alignment.
  - [Eduvate](https://www.letseduvate.com/services/robotics-and-coding-in-schools)
  - A search snippet of Eduvate pages says "Grade 1-9" and "1,200+ partner schools across 16+ states" — [Eduvate (snippet)](https://www.letseduvate.com/services/robotics-and-coding-in-schools)

**Ulipsu (Kidvento Education, Mysuru) — added; not on the original list**
- **Claim (sponsored PNN press release):**
  - Content: Classes 1-10 as a scheduled subject, with 20 domains including coding, AI, finance and data science. Each module ends in a project (for example a coin-toss predictor or a vehicle classifier), and Year-3 coding uses Google Colab.
  - Profiling: A Holland-Code interest assessment feeds a "Skill Intelligence Layer" from about 1,000-1,200 tracked touchpoints per student per year.
  - Scale: About 500 schools and "half a million students".
  - Finances: About $6M raised. FY25 revenue was Rs 9 crore, with Rs 20 crore targeted for FY26.
  - [The Tribune (PNN sponsored)](https://www.tribuneindia.com/news/business/half-a-million-students-are-building-things-their-parents-cant-explain-but-refuse-to-forget-how-ulipsu-deployed-ai-and-machine-learning-across-500-schools/)

**Educational Initiatives (Ei) — Mindspark CT, ASSET "AI & Digital Thinking"**
- **Claim:** Mindspark CT launched in March 2025, with scaffolded puzzles, coding projects and real-world data analysis. ASSET Computational Thinking was rebranded as an "AI and Digital Thinking" subject, planned to launch in December 2025, covering AI, Digital Literacy and CT — [Ei](https://ei.study/?p=15050)
- **Semi-independent:** An ICCE paper (written by Ei staff) analyses ASSET CT data from 8,994 Indian students in Grades 3-10 — [APSCE/ICCE](https://library.apsce.net/index.php/ICCE/article/view/5628)

### Inferences
- **Uolo is the only rival seen operating CodeSchool's exact play,** replacing the Computers book line with a CT&AI-branded book plus platform. Its public material leans on storytelling and robotics and shows **no evidence of unplugged, offline or shared-device design**. Its "coding platform accessible from home" points to a per-student, connected model. Its books are labelled ICSE or NEP, not CBSE CT&AI, so its alignment claim rests on the booklist heading and not on mapped outcomes.
- LEAD's CCS requires 1 computer per 2-3 students, internet for middle school and BCA/MCA teachers for Classes 6-8. This is the opposite of CBSE's "no extra load, unplugged" design, and of CodeSchool's shared-device positioning.
- **Ulipsu's per-student behavioural profiling** ("1,000-1,200 touchpoints", interest profiling) is the type of processing the DPDP analysis in the earlier report flags as likely "behavioural monitoring" of children. A clean, processor-only data posture is a credible point of difference for CodeSchool.
- Extramarks and Teachmint compete for the school's *digital budget* (panels and smart class) rather than for CT&AI content. They are potential channel partners or bundlers, not direct product rivals.

### Gaps
- No Uolo device, offline or data-privacy specs were found. The Uolo privacy policy was not read, and no Google Play listing or install count was found.
- Next Education was not found in any search result, so its coding, robotics or AI products and prices are **not covered**.
- Extramarks and LEAD 2026-27 CT&AI-specific SKUs, if any, were not found.
- Eduvate pricing and its delivery model (own trainer or school teacher) were not found.

## Q3. What do the coding, AI and robotics platform and kit/lab vendors offer?

### Takeaway
STEMpedia (PictoBlox) is the most capable *tool* rival. It offers block and Python coding plus image, pose, audio and text ML training, and has the largest verifiable app footprint (about 0.5-0.9M Android installs). It is hardware-led, however, with dollar-priced classroom packs, and it aligns to CBSE's skill subjects rather than CT&AI. STEMROBO, Avishkaar, Tinkerly and other ATL vendors sell labs and kits. Codingal, BrightChamps and WhiteHat Jr sell outsourced live-teacher or curriculum-licence models. None found publishes an offline, shared-device, teacher-led CT&AI product for Classes 3-8.

### Cited Findings

**STEMpedia — PictoBlox, Quarky kits, "Skillful Minds" books**
- **Claim (school offerings page):**
  - Packs: A "Mini AI & Robotics Classroom Pack" (6 Quarky Ultimate kits, 100 student course licences, 3 hours of teacher training) is listed at **$1,349** (was $1,599). A 12-kit pack (200 licences, 4 hours of training) and a 30-kit "AI & Robotics Lab" (600 yearlong licences, 5-day training, "Yearlong Curriculum for Class 3-12") are price-on-enquiry. The Quarky Ultimate Kit is $159.
  - Books: CBSE books are listed for Classes 1-8 (Skillful Minds, Digital Wizards), Subject 417 for Classes 9-10, and an ICSE series.
  - Not stated: any teacher dashboard or LMS, or offline use. The schools and students counters render "0+".
  - [STEMpedia school offerings](https://thestempedia.com/?p=56697)
- **Claim:** "Skillful Minds" books cost Rs 440-480 and include 3,000 PictoBlox AI credits, Codeavour competition entry and 25 lab activities. Their stated alignment is to the CBSE **Coding skill subject**, not CT&AI — [STEMpedia shop](https://thestempedia.com/shop/skillful-minds-computer-book-class-6/) (from earlier report)
- **Verified (app aggregators; figures vary):** PictoBlox Android has 500K+ downloads with a 4.22 rating from about 10.9K reviews — [AppBrain](https://www.appbrain.com/app/pictoblox-block-coding-ai/io.stempedia.pictoblox). A later snapshot shows about 935K installs and 12K ratings — [AppGoblin](https://appgoblin.info/apps/io.stempedia.pictoblox). Its ML features include image, pose and audio model training, face, text and speech recognition — [AppWisp](https://appwisp.com/app/android/io.stempedia.pictoblox). Desktop builds exist for Windows, macOS, Linux and Chromebook — [STEMpedia](https://thestempedia.com/?p=56697)
- **Claim:** "600+ lab setups, 65+ countries" — [STEMpedia (snippet)](https://thestempedia.com/?p=51908)

**STEMROBO — "Computational Thinking & AI for Schools" page**
- **Claim:**
  - Progression: Unplugged CT puzzles in Classes 3-5 ("no AI content yet"); AI literacy plus robotics builds in Class 6; classification, regression and clustering on small datasets in Class 7; the AI project lifecycle with a no-code tool plus bias and fairness in Class 8.
  - Delivery: A "NASSCOM-certified AI Connect platform" (block and text coding), robotics kits, AI hardware modules, labs and a "dedicated teacher training program".
  - Not stated: prices, scale, dashboard or offline use, and any explicit 2026-27 claim. The page says "NEP 2020-aligned".
  - [STEMROBO](https://www.stemrobo.com/computational-thinking-artificial-intelligence-for-schools/)

**Avishkaar — ATL and Tech Innovation Labs**
- **Claim:** Grades 1-12, 32 sessions a year of hands-on design-thinking projects (2024 brochure); robotics and AI tracks for lower grades and IoT and AI for higher grades; "1,000+ teachers trained" — [Avishkaar brochure 2024](https://assets.avishkaar.cc/marketing/CurriculumBrochure2024.pdf); [Avishkaar Tech Innovation Labs](https://institution.avishkaar.cc/avishkaar-tech-innovation-labs)
- **Claim vs claim:** Avishkaar says it has "set up more ATLs than any other organisation… 500+ schools". Press reports say 1,000+ labs — [Avishkaar ATL](https://home.avishkaar.cc/atl); [search summary](https://cxotoday.com/newsletter/top-5-companies-that-seek-to-offer-learning-through-atl-and-other-services-with-the-aid-of-ai-and-robotics/)
- **Finances:** Rs 5 crore pre-Series A in 2021 (Auxano, Mumbai Angels) — [EdTechReview](https://etrtest.edtechreview.in/2021/06/01/avishkaar-raises-5-cr-funding-to-expand-its-next-gen-technology-ed-platform). FY24 revenue was Rs 11.6 crore with a Rs 1.38 crore profit or loss (sign unclear), per an aggregator that was not checked against filings — [TheKredible](https://thekredible.com/company/avishkaar/financials)
- **ATL cost benchmark (verified, from earlier report):** One KV ATL tender was estimated at Rs 6.5 lakh for 60 students, about Rs 10,800 per student — [KVS tender](https://no1ambalacantt.kvs.ac.in/sites/default/files/ann4_1.pdf)

**Tinkerly (Jaipur)**
- **Verified (press):**
  - Content: Grade-wise logic, AI, IoT and coding curriculum for Grades 1-12, paired with physical kits — [Inc42](https://inc42.com/startups/tinkerly-looks-to-infuse-stem-courses-with-practical-ai-iot-robotics-kits/)
  - Funding: Rs 6.5 crore from **Navneet Tech Ventures** (a Navneet Education subsidiary), taking the total to Rs 10 crore. Seed investors were SucSEED, Gray Matters Capital, Keiretsu Forum and Rajasthan Angels — [YourStory 2021](https://yourstory.com/2021/11/startup-bharat-jaipur-based-tinkerly-coding)
- The website could not be fetched (expired TLS certificate on 10 Nov 2026) — tinkerly.com. Current product contents, pricing and scale are unknown.

**Codingal — school partnerships**
- **Claim:**
  - Curriculum: A "Customised Coding Curriculum designed for each school". Courses span Scratch, PictoBlox, App Inventor, Code.org, Python, JavaScript and "AI and Machine Learning".
  - Delivery: Codingal's own "computer science graduate teachers" *or* training of school teachers.
  - Tools and credentials: A "Master dashboard" tracking student and school-teacher performance, and STEM.org-accredited certificates.
  - Scale and alignment: "1 Million" students. No price and no CT&AI alignment are stated.
  - [Codingal school partnership](https://codingal.com/school-partnership)
- **Pricing model:** Codingal's own pricing policy is per-session (1:1 or group) — [Codingal pricing policy](https://www.codingal.com/pdfs/pricing-policy-document.pdf)
- **Finances (suspect):** Inc42 lists FY25 revenue of about Rs 1.4 lakh and total funding of $1.76M across 7 events. The revenue figure is implausibly small and probably a units error — [Inc42](https://inc42.com/company/codingal/financials/)

**BrightChamps, WhiteHat Jr, Camp K12**
- **BrightChamps claim:** "Portfolio of 100+ Schools" (undated). The model is in-school "Next-Gen Labs" plus teacher training — [BrightChamps school partnerships](https://leadership.brightchamps.com/school); [Outlook Startup](https://startup.outlookindia.com/topic/nep)
- **WhiteHat Jr (historical, verified press):**
  - 2019 school models: Curriculum licensing with teacher training; live 1:1 online classes in the school lab; after-school clubs — [MediaNews4U](https://www.medianews4u.com/edtech-startup-whitehat-jr-brings-ai-based-coding-to-schools)
  - Scale and ownership: 500 partner schools and 1.25 lakh students by August 2021 — [YourStory 2021](https://yourstory.com/2021/08/whitehat-jr-aims-teach-1million-students-coding-school-curriculum). Acquired by BYJU'S in August 2020 — [CB Insights](https://www.cbinsights.com/company/whitehat-jr)
  - No 2026 school activity was found.
- **Camp K12:** Not researched (no results surfaced).

**Other CT&AI-labelled vendors (from earlier report, uninspected):**
- Scaleopal Labs: engineers on campus, "zero-cost model", no prices — [Scaleopal](https://labs.scaleopal.com/insights/cbse-ct-ai-curriculum-classes-3-8-school-setup)
- PiyushAI: teacher manuals with rubrics, portal "Coming 2026" — [PiyushAI](https://piyushai.com/computational-thinking-and-artificial-intelligence-for-cbse/)
- Thinking Juggernaut: Rs 499-599 workbooks plus an AI kit and online teacher module — [Thinking Juggernaut](https://thinkingjuggernaut.in/blog/cbse-computational-thinking-ai-curriculum-classes-2026-27)
- Codju: a Grades 1-10 AI, ICT and robotics curriculum, NEP-aligned (claim) — [Codju](https://codju.com/blog/how-ai-is-actually-being-taught-in-indian-schools-today/)

### Inferences
- PictoBlox already covers "AI model training for kids" in a free-to-download app with desktop builds. CodeSchool should not try to out-feature it on ML tooling. It should compete on CT&AI-outcome mapping, the unplugged-plus-projector classroom flow, and teacher-ready lessons, none of which STEMpedia shows.
- Kit and lab vendors (STEMpedia packs at about $1,349 for 6 kits, ATL at about Rs 10,800 per student) price in a different league. CodeSchool's Offline Programme can be positioned as "the CT&AI hours without a lab".
- Codingal, BrightChamps and WhiteHat Jr are outsourced-teacher or after-school models built for 1:1 or small-group online delivery. They do not fit CBSE's teacher-anchored, in-period design, and their consumer-edtech heritage is a trust liability with principals.

### Gaps
- PictoBlox offline ML capability (whether model training works without internet on the desktop build) was not confirmed.
- STEMpedia's company financials and funding were not researched.
- Make Intern was not researched. No results surfaced.
- Prices and contents for Avishkaar, STEMROBO and Tinkerly school programmes were not found.

## Q4. What free alternatives (government, Big Tech, non-profit) compete for the same hours?

### Takeaway
The free layer is large and mostly **teacher training or content**, not a classroom product. CBSE's own free handbooks and training, Code.org's free Grades 3-8 curriculum in five Indian languages, CSpathshala's CC-BY lesson plans and Raspberry Pi's Experience AI cover content. Google's and Microsoft's 2026 programmes target **teacher AI use** (Gemini, Copilot), not student CT&AI. Intel and IBM work with CBSE historically targets Class 8 upwards. Nothing free found provides a ready per-class CT&AI sequence with a dashboard and project rubrics that works offline.

### Cited Findings
- **CBSE (verified):** Free handbooks for each grade, District Level Deliberations, regional workshops and DD e-Vidya content — [CBSE webinar PPT](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf). More than 450 one-day district sessions had been scheduled by August 2026, and the 3030 Eklavya series with IIT Gandhinagar is free (optional Rs 200 certificate) — [EdTechReview](https://www.edtechreview.in/trends-insights/insights/cbse-ai-computational-thinking-curriculum-classes-3-8/) (from earlier report)
- **Code.org (claim, own page):**
  - Offer: "Free access to our curricula". Partners implement a Grades 3-8 primary curriculum, NEP-aligned, with materials in Hindi, Marathi, Kannada, Tamil and Telugu.
  - Delivery: Through state and district partnerships (Maharashtra, Tamil Nadu, Telangana), Leadership for Equity (Andhra Pradesh, Haryana) and Peepul's three MCD schools in Delhi.
  - Reach: 2.2M Indian student accounts and 220,000 teachers.
  - No mention of CBSE.
  - [Code.org India](https://code.org/india)
- **Code.org claim:** It shared its AI curriculum with Profs Karthik Raman and S. Neethi of IIT Madras, who lead the CBSE-appointed expert committee, and says "selected lessons are being reviewed to inform curriculum design" — [Code.org India AI campaign](https://code.org/en-US/india-ai-education-campaign)
- **Google (verified press):**
  - Teacher training: On 19 May 2026 Google expanded its free, mobile-first AI training for educators (responsible Gemini use) to India, localised into six languages, starting with state pilots — [CXO Digital Pulse](https://www.cxodigitalpulse.com/?p=54219); [Google India blog](https://blog.google/intl/en-in/company-news/outreach-initiatives/new-partnerships-to-support-indias-educators-and-learners/)
  - ATL Saathi: A Gemini-powered desktop app to help teachers run Atal Tinkering Lab curriculum, in 100 schools at first with a target of 10,000 — [Deccan Herald](https://www.deccanherald.com/technology/artificial-intelligence/io-connect-india-2026-google-brings-ai-research-foundation-curriculum-atl-saathi-labs-for-schools-in-india-4073255)
  - DeepMind's AI Research Foundations: A free 56-hour programme aimed at technically prepared learners, not beginners — [CXO Digital Pulse](https://www.cxodigitalpulse.com/google-brings-free-ai-research-foundations-curriculum-to-india/)
- **Microsoft (verified press):** "Elevate for Educators" launched on 20 February 2026 to train 2M teachers across 200,000 institutions by 2030, with CBSE, NCERT and AICTE among delivery partners. Its pilot runs in Delhi's 75 CM SHRI schools using Copilot for lesson plans and assessments — [Microsoft Source Asia](https://news.microsoft.com/source/asia/features/microsoft-elevate-for-educators-brings-ai-to-the-worlds-largest-classroom/); [Free Press Journal](https://www.freepressjournal.in/education/microsoft-launches-elevate-for-educators-initiative-to-train-2-million-teachers-in-ai-across-india). Whether it is free to teachers was not confirmed.
- **Intel AI for Youth (verified, older press):** A CBSE MoU (2019-20) created an AI curriculum for Grade 8 and above, a 112-hour course, AI skills labs and teacher skilling. By late 2021 it had reached about 113,000 students and 12,000 educators across about 10,000 schools — [CRN India](https://www.crn.in/?p=29892); [YourStory 2021](https://yourstory.com:443/2021/12/indias-next-gen-innovators-intel-ai-programs-cbse-government-schools). An "AI for All" Intel–CBSE–MoE headline dated April 2026 was seen but not verified — [iConnect007](https://iconnect007.com/index.php/article/128479/intel-launches-ai-for-all-)
- **IBM (verified, older press):** Built the CBSE AI curriculum for senior classes (reported variously as Classes 8-10 or 11-12, piloted in about 200 schools across 13 states) — [Careers360](https://news.careers360.com/ibm-set-ai-curriculum-for-cbse-class-ix-xii/amp); [Analytics India Mag](https://analyticsindiamag.com/ai-news-updates/ibm-to-create-cbses-new-ai-curriculum-microsoft-to-train-teachers)
- **CBSE 2026 training (verified):** AI teacher training is scheduled for **Class XI** teachers on 1-3 July, 7-9 July, 15-17 September and 3-5 November 2026 — [CBSE Notification 76/2026](https://cbseacademic.nic.in/web_material/Notifications/2026/76_Notification_2026.pdf) (search snippet)
- **Other free options (from earlier report):** CSpathshala offers 200+ CC-BY lesson plans — [CSpathshala](https://cspathshala.org/). Experience AI (Raspberry Pi Foundation) launched in India on 13 July 2026 — [University of Southampton Delhi](https://www.delhi.southampton.ac.uk/news/press-release-experience-ai-educational-programme-comes-to-classrooms-in-india-through-raspberry-pi-foundation-and-university-of-southampton-delhi-partnership/)

### Inferences
- The Big Tech offers make *teachers* more AI-literate, which lowers the training barrier for CodeSchool's teacher-led product. They do not substitute for a Classes 3-8 student sequence. CodeSchool should position as complementary ("use your Microsoft or Google training; here is the class-by-class CT&AI kit").
- Code.org is the most credible free student-facing rival. Its India reach runs mainly through government and state programmes, not CBSE private schools, and it requires devices for most lessons. Its potential influence on the IIT Madras committee means the CBSE content may resemble Code.org's AI lessons.
- No CBSE partnership with IBM, Intel or Microsoft was found for the **Classes 3-8** CT&AI curriculum itself. Those tie-ups relate to senior-class AI subjects and teacher training.

### Gaps
- CodeMonkey's India school presence and pricing were not researched.
- Whether Microsoft Elevate for Educators or Google's training includes student CT content was not confirmed.
- The contents of the April 2026 Intel "AI for All" item were not confirmed.

## Q5. Pricing, business models, scale and financial health: the competitive ladder

### Takeaway
Only three public price points exist: print books at Rs 180-630, Uolo Tekie from Rs 799 per student per year (Tekie.AI books Rs 579-629 on booklists), and kit or lab packs at roughly Rs 10,000 or more per student-equivalent. Everyone else quotes on request. The financially strongest rivals (LEAD at about Rs 387 crore revenue and near breakeven; Teachmint at Rs 74 crore and hardware-led) are not CT&AI-specific. Uolo, the direct rival, is venture-funded (about $32M raised) and was loss-making at its last disclosed result (FY24 loss Rs 58 crore on about Rs 28 crore revenue).

### Cited Findings
| Product | Business model | Public price | Scale (claim or verified) | Finances | Source |
|---|---|---|---|---|---|
| Uolo Tekie / Tekie.AI | Book + platform + training, per student per year; booklist | From Rs 799 per student per year; Tekie.AI books Rs 579-629 (CMS) | Claim: 500K students, 1,000+ schools (Tekie); 15,000+ schools (Uolo-wide) | ~$32.5M raised; FY24 revenue ~Rs 27.9 cr, loss Rs 58.1 cr | [Uolo](https://uolo.co/tekie.html); [CMS](https://cmseducation.org/wp-content/uploads/2026/03/Classes-IV-to-VIII-2026-2027.pdf); [CB Insights](https://www.cbinsights.com/company/uolo/financials); [TheKredible](https://thekredible.com/blogs/uolo-revenue-surges-4-5x-in-fy24-losses-narrow-to-rs-58-11-crore) |
| LEAD (CCS, TECHBOOK) | Whole-school system subscription | Not public | Claim: 9,000+ schools, 4.1M students | FY26 revenue Rs 387 cr, loss Rs 34.5 cr | [LEAD](https://leadschool.in/); [YourStory](https://yourstory.com/2026/08/edtech-lead-fy26-revenue-rises-387-crore-losses-narrow-over-20-percent) |
| Extramarks Smart Class Plus | Smart-class platform tiers | Not public | n/a | FY24 revenue Rs 233 cr, loss Rs 48 cr | [Entrackr](https://entrackr.com/fintrackr/extramarks-losses-drop-by-85-to-rs-48-cr-in-fy24-revenue-slips-37-8713664) |
| Teachmint X/X2 + ERP | Hardware panels + software | Not public | Claim: 50+ countries | FY25 revenue Rs 74 cr, loss Rs 46.6 cr | [Entrackr](https://entrackr.com/fintrackr/teachmints-revenue-jumps-43x-in-fy25-10550884) |
| STEMpedia | Kits + licences + books | $1,349 for a 6-kit pack; books Rs 440-480 | Claim: 600+ labs; PictoBlox 0.5-0.9M installs | Not researched | [STEMpedia](https://thestempedia.com/?p=56697); [AppBrain](https://www.appbrain.com/app/pictoblox-block-coding-ai/io.stempedia.pictoblox) |
| Avishkaar | ATL/lab set-up + curriculum | ATL ~Rs 6.5 lakh per lab (KV tender, generic) | Claim: 500+ ATL schools | FY24 revenue ~Rs 11.6 cr (aggregator) | [Avishkaar](https://home.avishkaar.cc/atl); [TheKredible](https://thekredible.com/company/avishkaar/financials) |
| Tinkerly | Kits + curriculum | Not public | Unknown | Rs 10 cr raised (Navneet-backed) | [YourStory](https://yourstory.com/2021/11/startup-bharat-jaipur-based-tinkerly-coding) |
| Codingal | Own teachers or teacher training; per-session pricing for consumers | Not public for schools | Claim: 1M students | Inc42 data suspect | [Codingal](https://codingal.com/school-partnership); [Inc42](https://inc42.com/company/codingal/financials/) |
| Ulipsu | Scheduled-subject programme | Not public | Claim: ~500 schools, 0.5M students | Claim: FY25 revenue Rs 9 cr, ~$6M raised | [Tribune (sponsored)](https://www.tribuneindia.com/news/business/half-a-million-students-are-building-things-their-parents-cant-explain-but-refuse-to-forget-how-ulipsu-deployed-ai-and-machine-learning-across-500-schools/) |
| Eduvate | Robotics and coding programme | Not public | Claim: 1,200+ schools | Not found | [Eduvate](https://www.letseduvate.com/services/robotics-and-coding-in-schools) |
| Code.org, CBSE, CSpathshala, Experience AI, Google/Microsoft training | Free | Rs 0 | Code.org: 2.2M Indian student accounts | Non-profit or corporate | [Code.org India](https://code.org/india) |

- **Comparator (another vendor's claim):** Cyber Square advertises school coding plans "from as low as Rs 200 per student/month" — [Cyber Square blog](https://blog.cybersquare.org/blogs/post/affordable-online-coding-platforms-for-schools-in-india-cyber-square-guide). An IndiaMART "Coding Lab for Schools" listing shows Rs 99,000 per year — [IndiaMART](https://m.indiamart.com/proddetail/coding-lab-for-schools-26139005048.html)

### Inferences
- CodeSchool's Rs 299 + GST per student per year school licence is **less than half Tekie's Rs 799 entry price** and cheaper than most print CT&AI books once GST is set aside. The price is defensible if the pitch is "the CT&AI layer your teachers run on shared devices or a projector", not "a full CS programme".
- Most rivals hide prices. A published per-student price is itself a differentiator with cost-sensitive principals, and it helps compliance (booklist and website listing).
- Uolo's funding ($7M in December 2025) means it can afford school-by-school sales and discounting in 2026-27. Expect Tekie to be the incumbent in the schools CodeSchool targets.

### Gaps
- Tekie's actual negotiated per-school prices and discounts are unknown. The interview guides should ask about them.
- Uolo, Extramarks and STEMpedia FY25 or FY26 financials were not found.

## Q6. Cross-cutting features: devices, offline, teacher tools, assessment and data privacy (positioning map for CodeSchool)

### Takeaway
Across all products found, **none publicly states an offline-capable student platform built for shared devices** and mapped to CBSE CT&AI outcomes. Teacher tools are common (Uolo's auto-grading and test generator, Codingal's master dashboard, Extramarks' assessments). CT&AI-specific reporting, such as competency-wise records for CBSE's formative assessment or project rubric scoring, is not shown by anyone. Data privacy is uniformly undocumented beyond privacy-policy links, and at least one rival (Ulipsu) advertises heavy per-student profiling.

### Cited Findings
- **Devices and internet:**
  - LEAD CCS needs 1 PC per 2-3 students, internet for middle school and a TV in class and lab — [LEAD](https://leadschool.in/teaching-coding-to-kids-ccs-is-here-to-help-your-school)
  - Uolo stresses a coding platform "accessible from home" — [Uolo](https://uolo.co/tekie.html)
  - PictoBlox has desktop and mobile builds — [STEMpedia](https://thestempedia.com/?p=56697)
  - Ulipsu uses Google Colab (cloud) — [Tribune](https://www.tribuneindia.com/news/business/half-a-million-students-are-building-things-their-parents-cant-explain-but-refuse-to-forget-how-ulipsu-deployed-ai-and-machine-learning-across-500-schools/)
  - CBSE expects no computer for CT or for assessment — [CBSE PPT](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf)
  - Context: only 36.5% of schools have functional desktops (63.2% of private unaided schools) — [EdTechReview](https://www.edtechreview.in/trends-insights/insights/cbse-ai-computational-thinking-curriculum-classes-3-8/) (from earlier report)
- **Offline:** The only "offline" feature found is Extramarks' offline *test* creation with scan-and-grade — [Extramarks](https://www.extramarks.com/smart-class-plus). No vendor states offline student coding or AI activities.
- **Teacher tools:**
  - Uolo: attendance, auto-graded homework, interactive teacher manual, test-paper generator, year-round training — [Uolo](https://uolo.co/tekie.html)
  - Codingal: master dashboard and per-student dashboards — [Codingal](https://codingal.com/school-partnership)
  - Eduvate: lesson plans and progress tracking — [Eduvate](https://www.letseduvate.com/services/robotics-and-coding-in-schools)
  - STEMpedia: 3-hour to 5-day training, no dashboard stated — [STEMpedia](https://thestempedia.com/?p=56697)
- **Assessment:** Uolo has auto-grading, Codingal STEM.org certificates, and Ulipsu a per-module assessment plus profiling. None references CBSE CT&AI competencies or the project rubrics (which CBSE has not yet published) — sources as above.
- **Data and privacy:** No vendor page reviewed states DPDP readiness, roster-based provisioning or parental-consent handling. Ulipsu describes about 1,000-1,200 tracked touchpoints per student per year plus interest profiling — [Tribune (sponsored)](https://www.tribuneindia.com/news/business/half-a-million-students-are-building-things-their-parents-cant-explain-but-refuse-to-forget-how-ulipsu-deployed-ai-and-machine-learning-across-500-schools/)

### Inferences
- **The clearest open position for CodeSchool,** inferred from the absence of counter-evidence rather than proven: (1) CT&AI-outcome-mapped, class-by-class lessons that follow CBSE's integrated design, with Classes 3-5 inside Maths and TWAU periods; (2) offline-capable on shared devices or a single projector; (3) a teacher dashboard that records CBSE-style formative evidence and scores projects against rubrics once CBSE publishes them; (4) a processor-only DPDP posture; (5) a transparent Rs 299 + GST price.
- **The Offline Programme is the answer to LEAD-style and lab-style prerequisites.** It matches CBSE's own "no computer required" assessment design and can be sold where labs are not available.
- **Uolo Tekie is the benchmark to demo against.** Schools will compare storytelling books, robotics projects and the home platform with CodeSchool's offline, curriculum-mapped design. CodeSchool should prepare a side-by-side against Tekie.AI Accelerate for Grades 4-8.

### Gaps
- Vendors' actual app behaviour offline, their privacy policies and their data-sharing (for example third-party SDKs) were not inspected. Hands-on demos or app-store "Data safety" sections would close this.
- Play Store reviews for Uolo, Codingal or Tekie were not found, so classroom-reality complaints (login friction, internet dependence) are unknown.
