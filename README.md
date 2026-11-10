# CodeSchool

CodeSchool is a project by [evolvian2026](https://github.com/evolvian2026).

> A level-based programme that helps Indian schools teach computational thinking, coding and AI in Classes 3-8, built for CBSE's new CT&AI curriculum.

## Overview

From the 2026-27 session, CBSE asks schools to teach Computational Thinking and AI (CT&AI) in Classes 3-8: 50 hours a year in Classes 3-5 and 100 hours a year in Classes 6-8, including 40 hours of projects. CBSE's free handbooks provide puzzles that follow the NCERT maths chapters, but they include no coding, no project materials or rubrics, little hands-on AI and no way to track progress.

CodeSchool fills those gaps, chapter by chapter, alongside CBSE's books:

- **Levels for every maths chapter**, from warm-ups with hints to "now you build it" coding challenges.
- **Two ways to deliver:** an **Offline Programme** (printed workbooks, unplugged kits and teacher scripts, with no student devices) and an **Online Programme** (an app and browser platform on shared school devices, with automatic checking).
- **Hands-on AI** for Classes 6-8, and **project kits** with rubrics for the 40 project hours.
- **Teacher support:** period-by-period scripts, orientation, and an observation journal or dashboard that produces report-card summaries.
- **Child data by design:** no student data offline; school-controlled roll-number accounts online.

**Status:** research stage. No code yet. Next comes interviewing 15-20 schools (November-December 2026), followed by a free pilot in January-March 2027.

## Research

Foundational curriculum and market research (no code yet):

- **[CodeSchool Research Pack (PDF)](docs/research/CodeSchool-Research-Pack.pdf)**: everything below in one interactive 37-page PDF: scope, findings, CBSE review, action plan, interview plan and fillable interview forms. Fill the forms in a private copy, not in this public repository.
- **[US vs CBSE: CT and AI (PDF)](docs/research/CodeSchool-US-vs-CBSE-CT-AI-Report.pdf)** ([markdown](docs/research/reports/US%20vs%20CBSE%20CT%20and%20AI%20education.md)): how the USA teaches computational thinking and AI from which grade, how it differs from CBSE's Classes 3-8 curriculum, improvements for India, and what it means for CodeSchool.
- **[Competitors, buying and compliance (PDF)](docs/research/CodeSchool-Competitors-Buying-Compliance.pdf)** ([markdown](docs/research/reports/CT%20kit%20competitors%20buying%20and%20compliance.md)): who sells CBSE CT&AI material and at what price, how schools buy and what CBSE/state rules and GST allow, children's data law (DPDP) for a school product, the "CodeSchool" brand risk, and recommended pricing, channel and interview changes.
- **[India's schools: data report (PDF)](docs/research/CodeSchool-India-Schools-Report.pdf)** ([markdown](docs/research/reports/India%20schools%20enrolment%20and%20infrastructure.md)): how many schools India has (government, aided, private) and their enrolment and teachers (UDISE+ 2025-26), special categories (Kendriya Vidyalayas, Navodaya, Sainik, Army Public, Eklavya, KGBV and other residential schools), board affiliation counts, teaching resources (electricity, computers, internet, projectors, smart classrooms, ICT labs), offline and online learning support and home device access, with market sizing and offline-vs-online implications for CodeSchool.
- **[Costs and competitors (PDF)](docs/research/CodeSchool-Costs-and-Competitors.pdf)** ([markdown](docs/research/reports/CodeSchool%20costs%20and%20competitor%20teardown.md)): what it costs to print, kit, sell and deliver CodeSchool, channel margins and school-commission risk, GST, content and platform costs, per-student margins and break-even at Rs 449 / Rs 599 / Rs 299, and a teardown of the competing CT&AI books and platforms. All cost figures are estimates to confirm with real quotes.
- **[School decision-makers and contacts (PDF)](docs/research/CodeSchool-School-Contacts-Guide.pdf)** ([markdown](docs/research/reports/India%20school%20decision%20makers%20and%20contacts.md)): who proposes, approves and pays in private schools, chains, associations and government systems (KVS, NVS, Sainik, AWES, EMRS, states); official organisation-level contact routes; where each school's official contacts are published; outreach rules (DPDP, TRAI, WhatsApp); and a five-wave outreach sequence for the 29 January booklist close. Organisation contacts only; re-check each before use.
- **[Interview Field Kit (PDF)](docs/research/CodeSchool-Interview-Field-Kit.pdf)**: print-and-fill kit for school visits: pre-visit checklist, intro letter, participant information and consent record, interview guides with note space for each role, the full Level B3 lesson with cut-out student sheet, observation sheet, device audit and same-day debrief.
- **[Hindi letter and consent (PDF)](docs/research/CodeSchool-Hindi-Letter-and-Consent.pdf)**: Hindi introduction letter, participant information sheet, opening script and a bilingual consent record, for Hindi-medium schools. Have a fluent Hindi speaker check it before sending.
- **[Research Tracker (Excel)](docs/research/CodeSchool-Research-Tracker.xlsx)**: school pipeline, interview log, hypothesis evidence, action plan, Gantt timeline and CBSE monitor, with a dashboard that checks the go/no-go decision rule automatically. Save your working copy as `CodeSchool-Research-Tracker.private.xlsx` outside this repository.
- **[Decision Kit (PDF)](docs/research/CodeSchool-Decision-Kit.pdf)**: after the interviews: findings memo, go/no-go check against the decision rule, pilot success criteria, and draft pilot offer and letter-of-intent templates.

- [Kids coding curriculum and market](docs/research/reports/Kids%20coding%20curriculum%20and%20market.md): when coding starts in Indian and international schools, a grade-by-grade level framework, and the market landscape.
- [CBSE verification](docs/research/cbse-verification.md): the report's CBSE claims checked against the official circulars and syllabi (5 Nov 2026).
- [CBSE handbook review](docs/research/cbse-handbook-review.md): what the free CBSE CT&AI books contain, and the gaps CodeSchool could fill.
- [Research notes](docs/research/research_notes/Kids%20coding%20curriculum%20and%20market/): the source notes behind the report.
- [School interview plan](docs/research/school-interview-plan.md): hypotheses, sample, interview guides and timeline for validating the research with schools.
- [Interview materials](docs/research/interview-materials/): intro letter, Level B3 paper prototype, device audit sheet and tracking sheet.
- [Prospect list (private)](docs/research/prospects/README.md): how to download CBSE SARAS lists by hand and build the private launch-school list with `build_prospects.py`. School-level files are git-ignored.
- [Supplier quote requests](docs/research/supplier-quotes/): draft requests to printers, kit makers, distributors and booksellers, plus a comparison sheet, to replace the cost estimates with real quotes.

## Launch plan

- **[April 2027 launch plan (PDF)](docs/plan/CodeSchool-April-2027-Launch-Plan.pdf)** ([markdown](docs/plan/April-2027-launch-plan.md)): a dated plan worked back from the first day of the 2027-28 session. Launch scope: the full range for all six classes (decided 10 November 2026), with a content production plan and a 15 January checkpoint. It also covers the specimen format and online timing decisions due by 20 November, specimens by 15 December, booklist adoption, the pilot, orders, print and kits by 15 March, and teacher orientation, with owners, budget and risks.

## Sample books

Illustrated workbooks that follow the NCERT maths chapters in the same order as CBSE's 2026-27 CT&AI handbooks. Each chapter has theory (Learn), a worked example, five practice questions, a coding-on-paper task, a challenge, a self-check and a coder fact, plus answers, a glossary and cut-out code cards. All questions are original. Each class also has a 24-page specimen booklet for school visits (programme overview, three full chapters, a sample teacher script, the classroom kit, assessment, a note for parents and next steps).

| Class | Full book | Specimen booklet | Content |
|---|---|---|---|
| 3 | [Think Like a Coder, Class 3 (PDF, 49 pp)](docs/books/CodeSchool-Class3-Think-Like-a-Coder.pdf) | [Class 3 specimen (PDF, 24 pp)](docs/books/CodeSchool-Class3-Specimen-Booklet.pdf) | [class3/content.py](docs/books/class3/content.py) |
| 4 | [Think Like a Coder, Class 4 (PDF, 50 pp)](docs/books/CodeSchool-Class4-Think-Like-a-Coder.pdf) | [Class 4 specimen (PDF, 24 pp)](docs/books/CodeSchool-Class4-Specimen-Booklet.pdf) | [class4/content.py](docs/books/class4/content.py) |
| 5 | [Think Like a Coder, Class 5 (PDF, 53 pp)](docs/books/CodeSchool-Class5-Think-Like-a-Coder.pdf) | [Class 5 specimen (PDF, 24 pp)](docs/books/CodeSchool-Class5-Specimen-Booklet.pdf) | [class5/content.py](docs/books/class5/content.py) |

Build them with the shared tools (the number is the class):

```bash
python -P -E docs/books/tools/build_book.py 4
python -P -E docs/books/tools/build_specimen.py 4
```

## School proposals (drafts)

- [Offline Programme proposal (PDF)](docs/proposals/CodeSchool-Proposal-Offline.pdf): printed workbooks, unplugged kits and teacher scripts; no student devices.
- [Online Programme proposal (PDF)](docs/proposals/CodeSchool-Proposal-Online.pdf): app and browser on shared school devices, teacher dashboard, report-card export.
- Editable markdown sources and regeneration steps: [docs/proposals/](docs/proposals/README.md).

## Getting started

```bash
git clone https://github.com/evolvian2026/CodeSchool.git
cd CodeSchool
```

_Add setup and run instructions here once the project has code._

## Project structure

| Folder | Contents |
|---|---|
| `docs/research/` | Research PDFs, the tracker workbook, CBSE verification and handbook review, and the school interview plan |
| `docs/research/reports/` | Full research reports in markdown, with citations |
| `docs/research/research_notes/` | Source notes behind each report |
| `docs/research/interview-materials/` | Intro letter, paper prototype lesson, device audit sheet and tracking template |
| `docs/proposals/` | Offline and Online school proposals (PDF and editable markdown) |
| `docs/proposals/shared/` | Appendices shared by both proposals |
| `docs/proposals/tools/` | Converter that turns the proposal markdown into PDFs |

## Contributing

1. Create a branch: `git switch -c feature/your-change`
2. Commit your changes with a clear message.
3. Push the branch and open a pull request.

## License

Copyright (c) 2026 Bullseye Knowledge System Limited. All rights reserved.

This is proprietary material. No part of it may be copied, modified or distributed without the written permission of Bullseye Knowledge System Limited. See [LICENSE](LICENSE).
