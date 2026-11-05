# Learning Science and Established Progressions for a Grade-wise, Level-based K-12 Programming Curriculum

Notes on evidence status. Each finding is tagged.
- **[V]** means the claim was checked this session against a search result or abstract from the cited source.
- **[BK]** means the claim comes from the researcher's background knowledge of a well-known primary source. The canonical URL is given, but the page was not re-fetched this session. The report writer should treat [BK] items as likely accurate but needing a quick verification before they are quoted precisely.

Evidence strength is labelled as **Strong** (meta-analyses or RCTs that replicate), **Moderate** (quasi-experiments or several consistent studies), or **Weak/Contested** (single studies, self-report, vendor data, or conflicting results).

---

## 1. Developmental readiness: what can children handle at ages 4-7, 8-10, 11-13 and 14+?

### Takeaway
Children as young as 4-7 can learn sequencing, simple loops, events and debugging, with large measured gains in computational thinking (CT). They do best with structured, tangible or icon-based tools (KIBO, ScratchJr, floor robots, unplugged play), and the work is best framed as literacy or storytelling rather than puzzles. Open-ended block coding (Scratch) shows its benefits from about age 8. Abstraction-heavy concepts such as variables, functions with parameters and text syntax fit better from about age 10-11 onward. Major frameworks (CSTA, Bebras, Code.org) all use 2-3-year age bands rather than single grades, which supports building "levels" around bands.

### Cited Findings
**Bers / DevTech (ages 4-8)**
- [V] Bers's "Coding as Another Language" (CAL) is a pedagogy for early-childhood CS. It describes six stages children pass through: emergent, coding/decoding, fluency, new knowledge, multiple purposes and purposefulness. The stage names are [BK] from the paper. — [Bers 2019, J. Computers in Education](https://sites.bc.edu/devtech/wp-content/uploads/sites/181/2019/11/Bers2019_Article_CodingAsAnotherLanguageAPedago.pdf); [Springer version](https://link.springer.com/article/10.1007/s40692-019-00147-3)
- [V] CAL is designed as "developmentally appropriate for children 4-8 years of age". It has 24 book-centered lessons and uses ScratchJr (on screen) and KIBO (a screen-free, keyboard-free robot). — [Bers 2021, Pixel-Bit](https://doaj.org/article/b5ac3ba5ced14f03bf18862380aab942)
- [V] Bers reports an RCT in which ScratchJr learners were compared with non-learners. She stresses that "coding is not the same as computational thinking": CT is the thought process, and coding is the language used to express it. — [Siegel Endowment interview](https://siegelendowment.org/insights/computer-science-education-as-coding-playgrounds)
- [V] Bers frames early coding as "playground, not playpen" and as storytelling rather than only puzzle-solving. — [MIT CMS podcast: "Coding in early childhood: storytelling or puzzle solving"](https://cms.mit.edu/podcast-video-marina-bers-coding-in-early-childhood-storytelling-or-puzzle-solving)
- [V] ScratchJr is designed for ages 5-7. Scratch is designed for ages 8-16. — [ScratchJr about](https://www.scratchjr.org/about/info) [BK URL]; [Scratch about](https://scratch.mit.edu/about) [BK URL]

**Meta-analytic evidence by age (Strong-Moderate)**
- [V] A meta-analysis reported a large effect (d = 0.81) of programming interventions on CT skills in children aged 3-7. This comes from Simonsmeier et al. 2025 as cited in a secondary paper, so the primary source has not been verified. — [MDPI Education Sciences 2025 citing it](https://www.mdpi.com/2227-7102/16/10/1763)
- [V] A meta-analysis on the cognitive effects of CT found that structured virtual and tangible coding (robotics) benefited preschoolers and first graders, while more unstructured virtual coding (for example Scratch-based) was significant for older students. — [Computers & Education 2023, "The cognitive effects of computational thinking"](https://www.sciencedirect.com/science/article/pii/S0360131523002385)
- [V] A review of ages 4-6 found that unplugged coding consistently supported foundational algorithmic understanding, decomposition and collaboration. Effectiveness depended on teacher readiness, infrastructure and children's developmental stage. — [Chen et al. 2023 review / related summary, Int. J. STEM Ed.](https://link.springer.com/10.1186/s40594-023-00434-7)

**Piagetian framing (textbook theory, weak as a design rule)**
- [BK] Piaget's stages are preoperational (about 2-7), concrete operational (about 7-11: logical operations on concrete objects) and formal operational (about 11+: abstract and hypothetical reasoning). This is commonly used to argue that abstract variables and parameters belong at 11+ and that tangible or embodied coding suits under-7s. Modern developmental science treats the stage boundaries as soft and domain-specific. — [Overview](https://en.wikipedia.org/wiki/Piaget%27s_theory_of_cognitive_development)

**Bebras age bands (task-difficulty calibration)**
- [V] The US Bebras age groups are Kits (6-8), Castors (8-10), Benjamins (10-12), Cadets (12-14), Juniors (14-16) and Seniors (16-18). Each has easy, medium and hard tasks. — [Bebras Challenge USA](https://bebraschallenge.org/)
- [V] The UK uses different names and bands: Juniors (10-12), Intermediates (12-14), Seniors (14-16) and Elites (16-19). These map to school years differently in each nation, and the challenge is open to ages 6-19. — [UK Bebras](https://www.bebras.uk)
- [V] Bebras International recommends six groups. Countries need not run every group, and the bands "may differ according to class level". — [bebras.org](https://www.bebras.org/node_19.html)

**CSTA level bands (see section 2)**
- [BK] The CSTA K-12 Standards (2017) are written as levels: 1A (ages 5-7, about K-2), 1B (ages 8-11, about 3-5), 2 (ages 11-14, about 6-8), 3A (ages 14-16, about 9-10) and 3B (ages 16-18, about 11-12). — [CSTA K-12 Standards](https://csteachers.org/k12standards/)

### Inferences
- One natural design has about five or six developmental bands, matching CSTA and Bebras: K-2, 3-5, 6-8, 9-10 and 11-12. Content within each band can be divided into fine-grained levels. A Grade 1-to-Grade 2 jump is developmentally small; a ScratchJr-to-Scratch jump (about age 7-8) and a concrete-to-abstract jump (about age 10-12) are the real seams.
- For Grades 1-2, the evidence favours structured, tangible or icon-based, story-driven activities over open-ended canvases.
- For Grades 3 and up, open-ended creation becomes productive.

### Gaps
- I did not retrieve the primary Relkin, de Ruiter and Bers RCT paper (CAL/ScratchJr, K-2) with its effect sizes. Only an interview reference was found.
- I found no strong studies that tie specific programming concepts (for example variables) to specific ages. The age claims rest on curricula and design consensus, not on controlled "readiness" studies.

---

## 2. Existing progressions and their concept order

### Takeaway
Well-regarded progressions follow a similar order: sequence, then loops, then events, then conditionals, then nested loops, then variables, then functions/procedures with parameters, then data structures and text languages. They use grade bands, and they spiral back to earlier concepts. The K-12 CS Framework sets the concept areas, and CSTA standards set leveled expectations. Code.org CSF A-F is the main example of a one-course-per-grade structure. It also offers "Express" courses for older beginners, which is effectively a level-not-grade escape hatch.

### Cited Findings
**K-12 CS Framework**
- [BK] There are five core concepts: Computing Systems, Networks & the Internet, Data & Analysis, Algorithms & Programming, and Impacts of Computing. There are seven practices, including fostering an inclusive culture, collaborating, recognizing and defining problems, developing and using abstractions, creating artifacts, testing and refining, and communicating. The grade-band outcomes are at the end of grades 2, 5, 8 and 12. Note that the items in the brief (algorithms, variables, control, modularity, program development) are **sub-concepts of Algorithms & Programming**, not top-level areas. "Events" and "functions" sit within control and modularity. — [K12cs.org](https://k12cs.org/)

**CSTA K-12 Standards**
- [BK] The standards are organised by the same five concepts and by levels 1A, 1B, 2, 3A and 3B. Identifiers look like "1A-AP-10" (level-concept-number). — [CSTA standards](https://csteachers.org/k12standards/)

**Code.org CS Fundamentals (K-5)**
- [V] Code.org moved from four courses (1-4) to six grade-aligned courses (A-F, K-5). Support for Courses 1-4 ended in 2023. — [Code.org support](https://support.code.org/hc/en-us/articles/26001058366093-Teaching-Computer-Science-Fundamentals-Courses-A-F); [CSF curriculum page](https://code.org/en-US/curriculum/computer-science-fundamentals)
- [V] The concepts by course, as far as the search confirmed:
  - Course A introduces loops and events.
  - Course B adds unplugged loops ("Getting Loopy").
  - Course C covers sequencing, loops and events.
  - Course D reviews loops and events and adds algorithms and conditionals.
  - Course F teaches variables in an interactive project, with more student autonomy.
  - Course E ends with a 4-5 week project cycle (plan, code, revise from feedback, present). — [Code.org CSF / support pages above](https://code.org/en-US/curriculum/computer-science-fundamentals); [CSF Unplugged](https://code.org/curriculum/unplugged)
- [BK] Courses A and B are designed for pre-readers. Course D adds while loops and nested loops. Course E adds functions. Course F adds for-loops with counters and functions with parameters. — [CSF curriculum](https://code.org/en-US/curriculum/computer-science-fundamentals)
- [V] The legacy Courses 1-4 covered six programming concepts: sequencing, loops, conditionals, events, functions and variables. — [Code.org proficiency evaluation 2016](https://code.org/about/evaluation/proficiency2016)
- [BK] Code.org offers **Express** courses (Pre-reader Express for about ages 4-7, and Express for about ages 9-18). They condense the A-F content for students who start late. This is a direct precedent for decoupling level from grade. — [Code.org Express](https://studio.code.org/s/express)

**Code.org CS Discoveries (6-10) and CS Principles (9-12)**
- [BK] CS Discoveries units include:
  - Problem Solving & Computing
  - Web Development (HTML/CSS as text)
  - Interactive Animations & Games (Game Lab: JavaScript in a block/text toggle editor)
  - The Design Process (App Lab)
  - Data & Society
  - Physical Computing
  - AI and Machine Learning

  CS Principles (AP) uses App Lab (JavaScript with a block/text toggle) and covers the Internet, data, algorithms and impacts. — [CSD](https://code.org/curriculum/csd); [CSP](https://code.org/curriculum/csp)

**Raspberry Pi Foundation "The Computing Curriculum" (TCC)**
- [V] PRIMM is part of the Raspberry Pi Foundation's pedagogy guidance, which underpins TCC. — [RPF PRIMM quick read](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf)
- [BK] TCC is free and covers Key Stages 1-4 (ages 5-16) with 500+ hours of lessons, organised by year group. It is built on a taxonomy of about 11 strands, including algorithms, programming, data and information, computer systems, networks, creating media, design and development, effective use of tools, impact of technology, and safety and security. Programming moves from floor robots and ScratchJr (KS1), to Scratch and physical computing (KS2), to Python (KS3-KS4). — [RPF Teach curriculum](https://www.raspberrypi.org/teach/curriculum/)

**Hour of Code**
- [BK] Hour of Code consists of one-hour, self-guided puzzle tutorials (Code.org and partners). It is designed for engagement and outreach, not as a progression. — [hourofcode.com](https://hourofcode.com/)

**India-specific (new and highly relevant)**
- [V] On 1 April 2026, CBSE Circular Acad-15/2026 launched a **Computational Thinking and AI curriculum for Classes III-VIII** from the 2026-27 session. Circular Acad-18/2026 released student and teacher resource books for each grade. — [CBSE curriculum PDF](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_Pri_2026-27.pdf); [Deccan Herald](https://www.deccanherald.com/education/classes-3-to-8-to-study-ai-and-computational-thinking-now-moe-launches-curriculum-3953365); [EdTechReview explainer](https://www.edtechreview.in/trends-insights/insights/cbse-ai-computational-thinking-curriculum-classes-3-8/)
- [V] For Classes 3-5, CT is integrated into Mathematics and "The World Around Us". This is about 50 hours a year of worksheets and puzzles, taught by existing subject teachers. Secondary explainers report that the framework rejects coding syntax as the entry point and names no coding tool for Classes 3-8. Activities include unplugged tasks such as a Caesar cipher in Class 3. — [STEMpedia blog](https://thestempedia.com/blog/cbse-computational-thinking-and-ai-curriculum-for-class-3-to-8/); [Codju guide](https://codju.com/blog/cbse-computational-thinking-ai-curriculum-2026-27/) (these are secondary sources; the official PDF could not be parsed this session)
- [BK] NEP 2020 states that activities involving coding will be introduced in the Middle Stage (Grades 6-8). — [NEP 2020 text](https://www.education.gov.in/sites/upload_files/mhrd/files/NEP_Final_English_0.pdf)

### Inferences
- A consensus concept order for levels is:
  1. sequencing
  2. loops
  3. events
  4. conditionals
  5. nested loops and while loops
  6. variables
  7. functions and parameters
  8. lists and data
  9. text syntax, then modular programs, data structures and algorithms
- Networks, data and impacts should run as parallel strands, not as levels.
- For an Indian product, aligning Grades 3-8 to the CBSE CT and AI curriculum is commercially and pedagogically important, because schools will need to deliver it with non-specialist teachers from 2026-27. A product that is unplugged-first and worksheet-compatible for Grades 3-5 fits the official direction.

### Gaps
- I could not parse the official CBSE PDF (binary). The grade-by-grade concept list, hours for Classes 6-8, and whether block coding appears in Classes 6-8 all need direct verification.
- The exact TCC year in which Python begins was not verified this session.

---

## 3. Block-to-text transition: when, and what evidence?

### Takeaway
High-quality evidence comes mostly from high school (Weintrop and Wilensky). Blocks give faster early conceptual gains and better attitudes, but the advantage disappears about 10 weeks after moving to a professional text language (Java), with no lasting harm. So blocks are a good on-ramp, not a dead end. Frame-based editors (Stride) and dual-modality editors (Pencil Code, Code.org's Droplet) are reasonable bridges, but there is no strong evidence that they beat a clean switch. No rigorous study fixes an optimal transition age. Curricula place it around ages 11-14 (Grades 6-8). Python is the most common first text language in school curricula, but evidence that it beats alternatives is weak.

### Cited Findings
- [V] Weintrop and Wilensky (ACM TOCE 2017) ran a 5-week quasi-experiment in two classes at the same high school, using the same curriculum in block-based or text-based isomorphic environments. Block students performed better on concept assessments and reported higher confidence and enjoyment. — [Weintrop & Wilensky 2017 (PDF)](https://ccl.northwestern.edu/2017/a3_weintrop_wilensky.pdf); [ResearchGate record](https://www.researchgate.net/publication/320678674_Comparing_Block-Based_and_Text-Based_Programming_in_High_School_Computer_Science_Classrooms)
- [V] A follow-up compared block, text and **hybrid** environments with 90 students across three sections. — [Weintrop & Wilensky IDC 2017](https://ccl.northwestern.edu/2017/Weintrop_Wilensky_IDC_2017.pdf)
- [V] In the transition study (Computers & Education 2019), students moved to Java after 5 weeks and were tracked for 10 weeks. The early block advantage faded, and there was no overall difference in achievement between learners who started with blocks and those who started with text. The sample was mostly male (49 male, 11 female). — [Weintrop & Wilensky 2019, C&E 142:103646](https://www.terpconnect.umd.edu/~weintrop/papers/Weintrop&Wilensky_2019_C&E.pdf)
- [V] High school students' own perceptions are that blocks feel easier, because of drag and drop, browsable blocks and readable labels. They also see blocks as less powerful or "inauthentic". — [Weintrop & Wilensky 2015 "To Block or Not to Block"](https://ccl.northwestern.edu/2014/Weintrop%20and%20Wilensky%20-%202015%20-%20To%20Block%20or%20Not%20to%20Block,%20That%20is%20the%20Question%20St.pdf)
- [V] Pencil Code was built so that learners could move freely between blocks and text, but the 2019 study's Pencil.cc variant locked each student into one mode. — [Weintrop & Wilensky 2019](https://www.terpconnect.umd.edu/~weintrop/papers/Weintrop&Wilensky_2019_C&E.pdf)
- [V] In the frame-based Stride editor, high-level structures (assignment, loops, conditionals) are inserted as coloured frames with no braces, while expressions remain typed text. An evaluation concluded that Java and Stride are "equally suited" to secondary education. Earlier work reported that students wrote code faster and completed more objectives in Stride. — [Frame-based editing: easing the transition (Kölling, Brown, Altadmri)](https://twistedsquare.com/Blocks-Text.pdf); [Evaluation of a frame-based editor](https://www.researchgate.net/publication/307089173_Evaluation_of_a_Frame-based_Programming_Editor)
- [V] CodeStruct (Weintrop group, IDC 2022) is an intermediary environment that supports novices moving from blocks to Python. — [Kazemitabaar et al. IDC 2022](https://www.terpconnect.umd.edu/~weintrop/papers/Kazemitabaar_et_al_IDC_2022.pdf)
- [V] An umbrella review of 33 CT research syntheses found that project-based learning, text-based programming and game-based learning show the most pronounced effects. — [Umbrella review 2025, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12733880/)

### Inferences
- A defensible plan is:
  - blocks only through about Grade 5
  - dual-modality or "peek at the text" from about Grades 5-7 (Code.org Game Lab / App Lab and Pencil Code precedents)
  - a full switch to text (Python) at about Grades 7-8, with structure editors or Parsons problems for scaffolding
  - text by default for Grades 9-12
- Readiness should gate the transition (by level), not grade alone.
- The Weintrop results reassure the design that students who started on blocks don't need to "unlearn" anything.

### Gaps
- I found no rigorous studies of the block-to-text transition at ages 10-13 specifically, and none comparing Python with JavaScript or other first text languages for school learners. The case for Python rests on adoption (TCC, GCSE, CBSE Class 11-12 CS), not experimental evidence.

---

## 4. Unplugged activities: effectiveness by age

### Takeaway
Unplugged CT activities have positive, often large, effects on CT test scores in K-9. They are especially useful for young children and low-device settings. Hands-on programming exercises produce larger gains than unplugged work alone, and pure unplugged instruction can plateau. The best evidence-based design is unplugged as a concept introduction, followed by plugged practice.

### Cited Findings
- [V] A systematic review of 49 K-12 studies included a meta-analysis of 13 studies with 16 effect sizes. It found a large overall effect, Hedges' g = 1.028 (95% CI 0.641-1.415). Board and card games were the most common format. — [Chen et al. 2023, Int. J. STEM Education](https://link.springer.com/10.1186/s40594-023-00434-7); [DOAJ](https://doaj.org/article/88ffb26ff7014481828d7717f343867a)
- [V] A meta-analysis of 29 articles compared unplugged activities (UA) with programming exercises (PE). Both improved CT, and **PE was more effective than UA**. — [Education and Information Technologies 2022](https://link.springer.com/doi/10.1007/s10639-022-10915-x)
- [V] A meta-analysis of unplugged programming for K-9 (15 studies) found g = .631. The authors warn that timing matters, to avoid a plateau effect. — [ETR&D meta-analysis record](https://vufind-test.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-c358t-e9bef564135f179e6073c16a124d28e9ac8dbbed29e2012ea2673cede1388c3e3)
- [V] Code.org embeds unplugged lessons throughout CSF A-F, for example "Getting Loopy". — [Code.org CSF Unplugged](https://code.org/curriculum/unplugged)

### Inferences
- Unplugged is strongest for Grades 1-3, low-device Indian classrooms and concept introduction at any age. It also fits the CBSE Classes 3-5 integration model and limits screen time for young children (section 9).
- The pooled effect sizes are inflated by small, researcher-made CT tests, so the *direction* is more reliable than the magnitude. Evidence strength is Moderate.

### Gaps
- I found no meta-analysis isolating the named CS Unplugged (Bell et al.) materials. There is also no age-stratified breakdown in the retrieved abstracts.

---

## 5. Gamification, levels and progression

### Takeaway
Gamification has a small-to-medium positive effect on learning on average. In programming, a multi-level meta-analysis found that the benefit is **driven mainly by "levels"** (d ≈ 0.4), while badges, points, avatars and leaderboards had no significant effect on learning. Game-based CT learning has a moderate effect (g ≈ 0.6). Risks are real but contested. They include lower intrinsic motivation when rewards are mandatory or competitive (Hanus and Fox, which was not a programming course), leaderboards demotivating weaker or introverted students, and gains in quantity rather than quality. This directly supports a level-based structure, and suggests making badges and leaderboards optional and non-competitive.

### Cited Findings
- [V] **Costa (2023)** is a multi-level meta-analysis of game concepts in programming learning, with 15 combined effect sizes. Gamification produced a significant gain (Cohen's d ≈ 0.4), largely attributable to **levels** (p < .05). Badges, points, avatars and leaderboards showed no significant effect on programming learning. — [ISCTE repository](https://repositorio.iscte-iul.pt/handle/10071/29213); [full text PDF](https://repositorio.iscte-iul.pt/bitstream/10071/29213/1/article_95533.pdf)
- [V] Huang et al. (ETR&D 2020) pooled 30 studies of gamified versus non-gamified education and found g = .464 (95% CI .244-.684), a small-to-medium effect. — [record](https://vufind-test.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-c380t-9ede3d4b2b6f697ac0d7e35b657235f51b99e0ba10ecdda6a717722dacb811173)
- [BK] Sailer and Homner (2020, Educational Psychology Review) found gamification effects of g ≈ .49 on cognitive outcomes, .36 on motivational outcomes and .25 on behavioural outcomes. Cognitive effects were less stable when only high-rigor studies were included. — [Sailer & Homner 2020](https://link.springer.com/article/10.1007/s10648-019-09498-w)
- [V] A 2025 review and meta-analysis covered gamification and CT specifically. — [Springer, Technology, Knowledge and Learning 2025](https://link.springer.com/article/10.1007/s10758-025-09906-x)
- [V] Ma et al. (2023) meta-analysed 27 studies of game-based learning for CT and found g = .600 (95% CI .465-.735). The authors recommend collaborative and unplugged games and tailoring to prior experience. — [J. Educational Computing Research 2023](https://journals.sagepub.com/doi/10.1177/07356331231178948)
- [V] Lu et al. (2022) analysed 24 studies (n = 2,134) and found a medium positive game-based learning effect on CT, moderated by game type and duration. — [ResearchGate](https://www.researchgate.net/publication/361434604_Effects_of_Game-Based_Learning_on_Students'_Computational_Thinking_A_Meta-Analysis)
- [V] Hanus and Fox (2015) found that students in a course with badges and a leaderboard ended with *lower* intrinsic motivation, satisfaction and exam scores than the non-gamified class. The effect has been attributed to social comparison and mandatory badges. This was **not** a programming course. — [Hanus & Fox 2015, Computers & Education](https://www.researchgate.net/publication/265644737_Assessing_the_effects_of_gamification_in_the_classroom_A_longitudinal_study_on_intrinsic_motivation_social_comparison_satisfaction_effort_and_academic_performance)
- [V] In introductory programming, badges did not increase intrinsic motivation. Intrinsic motivation declined over time in both conditions. — [Do Badges Affect Intrinsic Motivation in Introductory Programming Students?](https://www.researchgate.net/publication/337227066_Do_Badges_Affect_Intrinsic_Motivation_in_Introductory_Programming_Students)
- [V] Mekler et al. (2017) found that game elements did not affect competence or intrinsic motivation and acted as extrinsic incentives that raised performance *quantity*. Some reviews find no net effect on intrinsic motivation. — [Summary, Aalto thesis](https://aaltodoc.aalto.fi/bitstreams/6546c32a-8393-4546-b518-03e6ea9728fb/download); [Dialnet: "Gamification improves extrinsic but not intrinsic motivation"](https://dialnet.unirioja.es/descarga/articulo/8966615.pdf)
- [V] Poorly designed leaderboards can demotivate lower-ranked or introverted learners. This comes from a 2025 conference paper, so it is weak evidence. — [ICCMETS 2025](https://iccmets.com/proceedings/2025/paper-21.pdf)
- [V] Bers explicitly contrasts "storytelling vs puzzle-solving" in early coding. She warns that puzzle-only apps limit coding to a narrow problem-solving view instead of expressive literacy. — [MIT CMS podcast](https://cms.mit.edu/podcast-video-marina-bers-coding-in-early-childhood-storytelling-or-puzzle-solving)

### Inferences
- **Levels are the best-supported game mechanic for programming learning.** That is a strong argument that a level-based architecture is evidence-aligned.
- Points, badges and leaderboards should be cosmetic, optional, mastery-based (not speed-based) and not public by default for young children.
- To counter shallow puzzle-solving, each level band should end with an open-ended create or project task. Code.org Course E/F projects and the Use-Modify-Create "Create" phase are examples.

### Gaps
- I found no peer-reviewed effectiveness studies of Lightbot, CodeMonkey or CodeCombat specifically; the meta-analyses pool generic games. Evidence that puzzle-based "Hour of Code" style apps transfer to open-ended programming is thin. I found no direct study, but Bers's critique and the overjustification literature both warn about it.
- The primary Hanus and Fox paper was not opened, so the exam-score detail is [BK].

---

## 6. Mastery learning, adaptive learning and decoupling level from grade

### Takeaway
Mastery learning is well supported (meta-analytic averages of about d = 0.5-0.6). Bloom's "2-sigma" is an outlier that has not replicated: realistic tutoring gives about 0.3-0.4 SD and intelligent tutoring systems give about 0.66 SD. Much of the measured mastery effect shrinks on standardised tests. In programming, data-driven next-step hints (iSnap) and adaptive Parsons problems are proven building blocks. Code.org's Express courses and CSTA's "level" notation are precedents for separating the learner's level from their grade. Placement is best done with a short adaptive diagnostic plus "test-out" options at level boundaries.

### Cited Findings
- [V] In Bloom's 1984 work, the mastery-learning classes gained about 1 SD and the one-to-one tutored group about 2 SD. Von Hippel puts mastery alone at about 1.1. — [Education Next, "Two-Sigma Tutoring: Separating Science Fiction from Science Fact"](https://www.educationnext.org/two-sigma-tutoring-separating-science-fiction-from-science-fact/)
- [V] Only one of 65 tutoring studies reviewed (a 1972 dissertation, n = 32) reported a 2-sigma effect. Cohen, Kulik and Kulik (1982) found an average tutoring effect of about 0.33 SD. — [Education Next](https://www.educationnext.org/two-sigma-tutoring-separating-science-fiction-from-science-fact/)
- [V] VanLehn (2011) concluded that Bloom's effect was mostly due to the higher mastery threshold (90% versus 80%). Mastery-learning effects reportedly drop from d ≈ 0.5 on experimenter-made tests to about 0.08 on standardised tests (Kulik et al. 1990, via a secondary source). — [Nintil systematic review of Bloom's 2-sigma](https://nintil.com/bloom-sigma/)
- [V] Kulik and Fletcher's review of 50 ITS evaluations found a median effect of 0.66 SD. No replicated programme has reached 2.0 under realistic conditions. — [Future-Proof summary](https://www.future-proof.app/research-two-sigma/); [Wikipedia: Bloom's 2 sigma problem](https://en.wikipedia.org/wiki/Bloom%27s_2_sigma_problem)
- [V] In practice, mastery learning in Cognitive Tutor Algebra I was often not followed: students were advanced without mastery. This is an implementation caution. — [Mastery Learning in Practice (arXiv 1802.08616)](https://arxiv.org/pdf/1802.08616)
- [V] **iSnap** (NC State, Price, Marwan) gives real-time, data-driven next-step hints in block-based Snap!. The hints are derived from past student solutions by the SourceCheck algorithm, not hand-authored. Hints can target a whole script or a single block. A known weakness is that hints show "what" but not "why", so textual explanations were added. — [iSnap project](https://isnap.csc.ncsu.edu/home/public/project/isnap); [Marwan & Price 2023, IEEE TLT](https://isnap.csc.ncsu.edu/home/public/papers/Marwan2023TLT.pdf); [Marwan ITiCSE 2019](https://isnap.csc.ncsu.edu/home/public/papers/MarwanITiCSE2019.pdf)
- [V] **Parsons problems.** Across three studies (Ericson's dissertation), learners reached equivalent pre-post gains in significantly less time than writing or fixing code. Adaptive Parsons problems helped more learners succeed. A middle-school study (n = 199) found higher grades and less time for the Parsons group. One classroom study (n = 81) found time savings but no significant learning gain in either condition. A 2023 multi-institutional paper calls for more replication. — [Georgia Tech dissertation news](https://hg.gatech.edu/node/603172); [NSF PAR, Ericson](https://par.nsf.gov/search/author:%22Ericson,%20Barbara%20Jane%22); [Ericson et al. ITiCSE 2023](https://strathprints.strath.ac.uk/86100/1/Ericson_etal_ITiCSE_2023_Conducting_multi_institutional_studies_of_Parsons_problems.pdf); [Parsons scaffolding study](https://par.nsf.gov/biblio/10644057-scaffolding-novices-analyzing-when-how-parsons-problems-impact-novice-programming-integrated-science-assignment)
- [BK] Code.org Express courses (ages 9-18) let older beginners cover K-5 concepts quickly. This is an existing level-not-grade mechanism. — [Code.org Express](https://studio.code.org/s/express)
- [BK] Piech et al. (2015) used Code.org Hour of Code trajectories to infer hint policies automatically. Deep Knowledge Tracing (Piech et al., NeurIPS 2015) models skill mastery from interaction sequences. — [Piech et al. L@S 2015](https://dl.acm.org/doi/10.1145/2724660.2724668); [Deep Knowledge Tracing](https://arxiv.org/abs/1506.05908)

### Inferences
- Suggested architecture:
  1. Define a concept **level ladder**, for example L1-L12 or bands A-F, independent of grade.
  2. Each grade gets a **default entry level** and **age-appropriate skins** (themes, reading load, UI), so a Grade 7 beginner does Level 1-3 concepts with Grade 7 presentation (the Code.org Express model).
  3. Use a 10-15 minute adaptive placement check plus per-level "challenge to skip" tests.
  4. Gate level progression on mastery, for example passing 80-90% of check items, with spaced review.
  5. Use data-driven hints and Parsons problems as low-cost adaptivity.
- The evidence suggests that mastery gating and hints matter more than complex knowledge-tracing models. Bayesian Knowledge Tracing per concept strand is sufficient at first.
- Watch for "advancement without mastery" (the Cognitive Tutor finding) when teachers face pacing pressure.

### Gaps
- I found no empirical studies of placement tests for mixed-ability school programming classes. Placement design must rely on general psychometric practice.
- There is no published evaluation of Code.org's internal hint system effectiveness in the retrieved results.

---

## 7. PRIMM, Use-Modify-Create and Parsons as scaffolds

### Takeaway
PRIMM (Predict-Run-Investigate-Modify-Make) has the best school-level evidence of these scaffolds. A large UK quasi-experiment with ages 11-14 found better programming outcomes. Teachers, including non-specialists, also find it a usable lesson structure. Use-Modify-Create is a widely used, lighter-evidence progression model. Parsons problems give similar learning in less time (section 6). All three reduce cognitive load and suit non-specialist teachers.

### Cited Findings
- [V] PRIMM was developed by Sue Sentance (now at the Raspberry Pi Computing Education Research Centre, Cambridge) and is used widely in UK schools. — [Cambridge CSAP profile](https://www.csap.cam.ac.uk/network/sue-sentance/); [RPF PRIMM quick read 2023](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf)
- [V] Sentance, Waite and Kallia (2019), "Teaching computer programming with PRIMM: a sociocultural perspective", Computer Science Education 29(2-3):136-176, is grounded in Vygotskian theory. — [T&F DOI](https://informahealthcare.com/doi/epub/10.1080/08993408.2019.1608781); [Glasgow eprint](https://eprints.gla.ac.uk/229012)
- [BK] The 2019 study involved 13 schools and about 490 students aged 11-14. The PRIMM group scored significantly higher on a post-test than the control. Teachers valued the structure, especially "predict" and the focus on reading code before writing it. — [same paper, CORE PDF](https://core.ac.uk/download/237088209.pdf)
- [V] A companion paper is "Teachers' Experiences of using PRIMM to Teach Programming in School" (SIGCSE 2019, pp. 476-482). — [dblp](https://dblp1.uni-trier.de/rec/conf/sigcse/SentanceWK19.html)
- [V] RPF seminar slides on teaching programming with PRIMM. — [RPF slides](https://www.raspberrypi.org/app/uploads/2022/08/Teaching_Programming_with_PRIMM-1.pdf)
- [BK] Use-Modify-Create comes from Lee et al. (2011, ACM Inroads). Lytle et al. (ITiCSE 2019) compared UMC with non-UMC lesson progressions in middle-school STEM classes. UMC students found the work less difficult and felt more ownership, with similar or better completion. — [Lytle et al. 2019](https://dl.acm.org/doi/10.1145/3304221.3319786)

### Inferences
- A level template could follow the same shape at every level:
  1. Predict and Run with a worked example
  2. Investigate (tracing questions)
  3. Modify (guided changes)
  4. Parsons or fill-in-the-blank bridge
  5. Make/Create (open project)

  This is auto-gradable in steps 1-4, which helps non-CS teachers.
- PRIMM's "read before write" emphasis also counters the shallow trial-and-error puzzle play from section 5.

### Gaps
- PRIMM evidence is ages 11-14. I found no PRIMM studies with Grades 1-5. Use-Modify-Create evidence is mostly qualitative or small-scale.

---

## 8. Teacher-facing considerations for non-CS-trained (Indian) teachers

### Takeaway
Large programmes (Code.org, CBSE 2026-27) assume non-specialist teachers. They rely on fully scripted lesson plans, short self-paced professional development, unplugged materials and teacher handbooks. Independent evidence that scripted lessons *alone* drive outcomes is weak. One district study found that students who did extra CS work outside the scripted grade-level lessons improved more. Auto-grading, dashboards, PRIMM-style structure and unplugged worksheets lower the expertise barrier. India's new CBSE mandate creates immediate demand for this kind of support.

### Cited Findings
- [V] Code.org markets CSF as teachable with "no need to hire specialists". Its self-paced "Teaching CS Fundamentals" professional development is about 8 hours with no prerequisites, plus a 2-hour basics course. Code.org also runs 7-hour "Deep Dive" workshops. — [Code.org educate](https://code.org/educate); [Self-paced PD](https://code.org/en-US/professional-learning/self-paced-courses); [PD Deep Dive](https://code.org/professional-development-deep-dive)
- [V] Code.org reports more than 100,000 workshop participants and that 90% would recommend the programme. This is self-reported satisfaction, not an outcome measure. — [Code.org Medium](https://codeorg.medium.com/teach-computer-science-join-the-code-org-professional-learning-program-4f71bbcc1428)
- [V] Code.org's teacher training targets experienced teachers with little or no CS background, and focuses on pedagogy as much as content. — [EdWeek 2017](https://www.edweek.org/teaching-learning/for-code-org-training-computer-science-teachers-isnt-really-about-computer-science/2017/08)
- [V] In the Baltimore County "Time for CS" study (UChicago Outlier), Code.org CSF lessons were embedded in the literacy block. Completing a higher share of **extra** Code.org lessons and additional CS activities was associated with outcomes. Completing the grade-level lessons was **not**. — [Outlier Research findings](https://outlier.uchicago.edu/TimeforCS/findings)
- [V] CBSE will train teachers for the CT and AI curriculum through NISHTHA and grade-specific programmes, with dedicated teacher handbooks. Classes 3-5 will be taught by existing subject teachers. — [Free Press Journal](https://www.freepressjournal.in/education/cbse-ncert-introduce-ai-computational-thinking-curriculum-for-classes-3-to-8-teacher-training-to-begin-in-summer-break); [EdTechReview](https://www.edtechreview.in/trends-insights/insights/cbse-ai-computational-thinking-curriculum-classes-3-8/)
- [V] Teacher readiness is a key moderator of unplugged and early coding effectiveness. — [Int. J. STEM Ed. 2023](https://link.springer.com/10.1186/s40594-023-00434-7)

### Inferences
- Product implications:
  - minute-by-minute scripted lesson plans with "say this, ask this" prompts
  - teacher answer keys and common-misconception notes per level
  - auto-graded puzzles, with a class dashboard showing who is stuck and on which concept
  - printable unplugged kits for low-device days
  - short micro-PD videos per unit
  - CBSE CT and AI mapping for Grades 3-8
- The Baltimore finding suggests letting fast learners do self-paced extra levels and projects beyond the scripted lesson, which a level-based design does naturally.

### Gaps
- I found no rigorous Indian studies on the effectiveness of coding instruction by non-specialist teachers, and no data on the share of Indian teachers with CS training.
- No RCT of scripted versus unscripted CS lessons was found.

---

## 9. Screen-time guidance affecting Grades 1-3 app design

### Takeaway
WHO (2019) recommends no screen time under age 1 and no more than 1 hour of sedentary screen time for ages 2-4. AAP (2016) recommends no more than 1 hour a day of high-quality, co-viewed media for ages 2-5, and consistent limits for 6+. The Indian Academy of Pediatrics (2021/2022) recommends no screens under 2 and less than 1 hour for ages 2-5, with balanced, supervised use after that. None of these sets a hard cap at ages 6-8 (Grades 1-3). Together they support short screen sessions, unplugged and tangible alternatives, and adult-mediated use in early grades. The guidelines are themselves contested for focusing on quantity rather than content.

### Cited Findings
- [V] WHO's 2019 guidance: under 5s should have no more than 1 hour of screen time a day ("less is better"), and none is recommended under age 1. Critics said it focuses on quantity rather than content and context. The UK RCPCH said the evidence was too weak for thresholds. — [KTVU/AP report](https://www.ktvu.com/news/un-no-screen-time-for-babies-only-1-hour-for-kids-under-5); [WHO guideline](https://www.who.int/publications/i/item/9789241550536) [BK URL]
- [V] IAP 2021 guidance for parents: no screens under 2 years, and less than 1 hour a day for slightly older (2-5) children. It was formalised as "Indian Academy of Pediatrics Guidelines on Screen Time and Digital Wellness in Infants, Children and Adolescents", Indian Pediatrics 2022;59(3):235-244. — [IAP parent guideline PDF](https://aha.iapindia.org//pdf/Guidelines-Screen-Time-Guidelines-for-Parents-Ch-005.pdf); [Indian Pediatrics 2022 PDF](https://www.indianpediatrics.net/mar2022/235.pdf); [WHO SEARO index](https://imsear.searo.who.int/items/83e152e9-46a9-44a1-b8e7-8d3fe2e8cb22)
- [BK] AAP's "Media and Young Minds" (2016) says to avoid digital media other than video chat under 18-24 months. For ages 2-5, it recommends limiting use to 1 hour a day of high-quality programming, with parents co-viewing. For ages 6+, it recommends consistent limits through a Family Media Use Plan. — [AAP Pediatrics 2016](https://publications.aap.org/pediatrics/article/138/5/e20162591/60503/Media-and-Young-Minds)

### Inferences
- For Grades 1-3 (ages 6-8), keep on-screen segments to about 10-20 minutes within a lesson. Pair them with unplugged or tangible activities (KIBO-style or floor robots) and favour teacher-led or shared-screen modes over solo tablet time.
- Avoid engagement-maximising loops (streaks, infinite levels, push notifications) for young users.
- Bers's KIBO and the CAL work show that screen-free coding is viable for this age.

### Gaps
- I did not retrieve the IAP 2022 age table for ages 5-10 or 10-18 (it reportedly recommends limited, supervised recreational use). This should be verified in the Indian Pediatrics PDF.
- I found no guidance that distinguishes educational coding screen time from recreational screen time.

---

## Overall feasibility signal (for the synthesiser)
- A level-based structure is **feasible and evidence-aligned**. The supporting evidence is:
  1. "Levels" are the one gamification element with a significant learning effect in programming (Costa 2023).
  2. Mastery learning has robust moderate effects.
  3. Major frameworks already use multi-year levels or bands (CSTA 1A-3B, Bebras, K-12 CS Framework grade bands).
  4. Code.org Express shows precedent for level-not-grade entry.
- The key design risks are:
  - shallow puzzle-only progression (mitigate with Create/project levels)
  - extrinsic-reward overuse
  - advancement without true mastery
  - screen time for Grades 1-3
  - non-specialist teacher capacity, now urgent with CBSE's CT and AI curriculum for Classes 3-8 from 2026-27
