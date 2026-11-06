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
