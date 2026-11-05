# CBSE facts checked against official documents

**Checked:** 5 November 2026 · **Method:** I read the full text of each official PDF from cbseacademic.nic.in. Quotes are verbatim and kept short.

This note confirms or corrects the CBSE claims in [Kids coding curriculum and market](reports/Kids%20coding%20curriculum%20and%20market.md). The report has been updated to match.

## Summary

| Claim in the report | Verdict | What the documents say |
|---|---|---|
| CT&AI for Classes 3-8 starts in 2026-27 | **Confirmed** | Circular Acad-15/2026, 1 April 2026 |
| Schools are "advised", not ordered | **Confirmed, with nuance** | Acad-15 says "advised", but Acad-18 says the curriculum "mandates" its content, and schools "should" use the free books |
| 50 h a year (Classes 3-5), 100 h (Classes 6-8: 40 CT + 20 AI + 40 projects) | **Confirmed** | Curriculum sections 3.4 and 10.2 |
| Classes 3-5 embedded in Maths and The World Around Us (TWAU) | **Confirmed** | Resource books follow the NCERT Maths chapter order |
| Scratch named for Classes 3-5 | **Confirmed** | Competency C-6, a single competency |
| Teachable Machine named for Classes 6-8 | **Right for Class 8 handbooks; not in the curriculum** | The curriculum document names no tool and only says "no-code AI tools". The Class 8 Student Handbook names Teachable Machine and Machine Learning for Kids and has three step-by-step Teachable Machine labs. The Classes 6 and 7 books name no tool (see the [handbook review](cbse-handbook-review.md)) |
| Python is not a Class 3-8 topic | **Confirmed** | Python appears only in the "Aims" section |
| Class 9 CT&AI modules dropped for the 2026-27 batch | **Confirmed** | Acad-70/2026, 29 October 2026 |
| Compulsory Class 9 CT&AI in 2027-28 and a Class 10 board exam in 2028-29 | **Still unconfirmed** | Neither circular says this |
| Computer Applications (165) teaches Python and HTML in Classes 9-10 | **Wrong** | No programming at all: office tools in Class 9, HTML/CSS in Class 10 |
| CBSE's first programming subject is in Class 11 | **Confirmed (new finding)** | Python in Computer Science 083 and Informatics Practices 065 |
| Teacher training is through NISHTHA | **Not supported; CBSE runs its own CPD** | No CBSE document mentions NISHTHA. The [28 April 2026 webinar slides](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf) describe CBSE's own plan: a 2026-27 annual training theme, "Computational Thinking and Understanding AI", delivered through one-day district and regional workshops (6 CPD hours each), half-day lead-school sessions (3 hours), online Board sessions and videos on the DD PM e-Vidya CBSE 15 channel |

## 1. Circular Acad-15/2026: launch

Source: https://cbseacademic.nic.in/web_material/Circulars/2026/15_Circular_2026.pdf

- **Date and subject:** 01.04.2026. "Launch of CBSE Curriculum Framework for Computational Thinking (CT) and Artificial Intelligence (AI) for Classes III–VIII (Session 2026–27)".
- **Scope:** CBSE "introduces the… Curriculum for Classes III–VIII from the academic session 2026–27".
- **Status:** it calls the document "the prescribed curriculum", then says "All schools are advised to take necessary steps for effective implementation of the curriculum."
- It doesn't mention assessment, books or training. Those are in the other documents.

## 2. Circular Acad-18/2026: resource books

Source: https://cbseacademic.nic.in/web_material/Circulars/2026/18_Circular_2026.pdf

- **Date and subject:** 9 April 2026. "Students' and Teachers' Resource books for course on Computational Thinking and Artificial Intelligence (CT&AI) for classes 3rd to 8th".
- **Stronger wording than Acad-15:** "The curriculum mandates CT + AI + Ethics + Unplugged Learning." And: "Schools should download these resource books and use these for classroom transaction."
- **Free, and tied to maths:** the handbooks are "available on http://cbseacademic.nic.in/". They are "a companion to the NCERT Mathematics textbooks (the concepts of TWAU are interwoven)" and "follow the same chapter sequence as in Mathematics".
- **Teaching approach:** "the process of thinking is more important than arriving at the correct answer"; teachers should use prompts rather than give solutions.
- **Class 9, later superseded:** it said other AI courses would be "discontinued for class IX, session 2026-27 onwards", and that NCERT modules would be used for internal assessment in Classes 9-12. Acad-70 (section 4) later kept AI 417 as a Class 9 skill subject and dropped the CT&AI modules for this year's Class 9.

## 3. The CT&AI curriculum for Classes 3-8

Source: https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_Pri_2026-27.pdf (31 pages)

**Hours and delivery** (sections 2.1, 3.4 and 10.2)
- Classes 3-5: **50 hours a year**, "Integrated into Mathematics & TWAU", with extra CT questions "via resource books".
- Classes 6-8: **100 hours a year**: Advanced CT skills 40, Introductory AI concepts 20, Interdisciplinary projects 40.
- The time "is flexible, and schools can go beyond the allocated time".

**Platform and tools**
- It is built "without dependence on any specific platform". Schools have "flexibility… to choose the platform… without being tied to specific software or technology". It "recommends harnessing… free and open-source tools".
- **Scratch** is named once, in Classes 3-5 competency C-6: "parts of a computer, input/output devices, file management, internet safety, educational software, and block-based coding (e.g. Scratch)".
- **No AI tool is named in the curriculum itself.** Class 8 says "simple no-code AI tools (image classifiers, chatbots, data prediction apps)". Class 7 says "applying them to a small dataset using AI tools". The Class 8 handbooks do: the student book uses Teachable Machine for three hands-on labs and also mentions Machine Learning for Kids.
- **Python** appears only in the Aims: "tools of technology, such as Python programming, help in modelling".

**What Classes 3-5 actually cover** (section 10.1)
- It is **maths-puzzle CT, not coding**: abstract thinking (3-D views, flips, symmetry), pattern recognition, decomposition with clues, and algorithmic thinking.
- **Class 4 algorithmic thinking:** "follow a set of well-defined, elaborate conditions" to solve problems including "Movements on grids or direction-based paths" and "Multi-step instructions involving moves, changes, transfers, swaps".
- **Explicit if-then logic comes later.** It first appears in **Class 7** ("algorithms with conditional branching", "if–then reasoning") and in Class 8 ("Conditional instructions (if–then, either–or, must/must not)").

**What Classes 6-8 cover** (section 10.2)
- CT, tied to the maths textbooks.
- AI syllabus, 20 hours a year in each class:
  - Class 6: what AI is, data types, patterns, ethics
  - Class 7: classification, regression and clustering on a small dataset; computer vision, NLP and data science; charts; bias
  - Class 8: the AI project cycle, no-code tools, fairness, responsible AI

**Who teaches** (section 8.1)
- Classes 3-5: "Mathematics and other subject teachers… using special worksheets and handbooks".
- Classes 6-8: "subject teachers (for CT resources) and Computer teachers (for AI Literacy resources)". Projects "will be assessed by the Computer teacher".

**Assessment** (section 9.2)
- Classes 3-5: "Written tests with CT questions and puzzles; interactive group activities (e.g. treasure hunts); Teacher Observation Journal". Assessment is linked to Maths and TWAU.
- Classes 6-8: "Written tests; interactive group activities; practical examinations; Teacher Observation Journal; thematic projects".
- No board examination is mentioned.

## 4. Circular Acad-70/2026: Class 9 scheme

Source: https://cbseacademic.nic.in/web_material/Circulars/2026/70_Circular_2026.pdf

- **Date and subject:** 29 October 2026. "Scheme of Studies for Class IX 2026-27".
- **The deferral:** "the subject 'Individuals in Society' and the 'Modules of CT & AI' in Class IX (2026-27)… shall not be the part of the curriculum for these batches". The reason given is "To align the introduction of this curricular area with the implementation schedule".
- **Vocational education is compulsory.** Students pick "Kaushal Vikas" (internally assessed) or one of 22 skill subjects with a Class 10 board exam. These include **402 Information Technology**, **417 Artificial Intelligence** and **419 Data Science**.
- **Computer Applications** is listed among the 57 *optional* subjects.
- **Nothing about the future:** it says nothing about CT&AI becoming compulsory in 2027-28 or about a 2028-29 board exam.

## 5. Computing subject syllabi, 2026-27

**Computer Applications, 165:** https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart1/Computer_Applications_SecP1IX_2026-27.pdf and …SecP1X_2026-27.pdf
- **Class 9:** Basics of IT, Cyber safety, Office tools (word processor, presentations, spreadsheets including `IF()`), Lab 50.
- **Class 10:** Networking, HTML (with CSS), Cyber ethics, Practicals 50.
- **No programming language** in either class.

**Computer Science, 083:** https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Computer_Science_SecP2_2026-27.pdf
- **Class 11:** "Computational Thinking and Programming - I" (45 of 70 theory marks) in **Python**: data types, operators, if/elif, for/while, strings, lists, tuples, dictionaries and modules. Practicals include a report file of at least 20 Python programs.
- **Class 12:** functions, exceptions, text/binary/CSV files, stacks, networks, SQL, and Python-SQL connectivity.

**Informatics Practices, 065:** https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Informatics_Practices_SecP2_2026-27.pdf
- **Class 11:** Python basics, lists, dictionaries, an introduction to NumPy, MySQL, and emerging trends.
- **Class 12:** Pandas, Matplotlib, SQL functions and joins, networks, and societal impacts.

## What this changes for CodeSchool

1. **A CBSE student meets no programming language in any CBSE subject before Class 11.** Classes 9-10 Computer Applications is office tools and HTML. That leaves a gap from Class 6 to Class 10 between Scratch and Python. Band C (the block-to-text bridge) and Band D sit squarely in that gap.
2. **CBSE's Classes 3-5 CT is maths puzzles mapped to NCERT maths chapters, not coding.** To sell into CBSE Classes 3-5, Band B needs a strand that follows the maths chapter order of the free CBSE resource books, alongside the block-coding levels.
3. **Explicit if-then logic is a Class 7 outcome in CBSE.** Level B3 (if-else at Class 4) is ahead of that. Grid paths and "following conditions" do appear at Class 4, so B3 is a stretch, not a mismatch. The teacher interviews should test it.
4. **The Classes 6-8 AI strand is taught by computer teachers.** The computer-teacher interview is a buyer conversation for Band C, not just a device audit.
5. **The curriculum is platform-agnostic and favours free tools.** No vendor is named, so there's no incumbent tool. Schools are pointed toward free options, which strengthens the case for selling teacher tooling and assessment rather than content.
