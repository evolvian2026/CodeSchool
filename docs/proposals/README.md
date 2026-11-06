# School proposals (drafts)

Two separate proposals a school can ask for, both drafts to be revised after school feedback:

| Proposal | PDF | Editable source |
|---|---|---|
| **Offline Programme**: printed workbooks, unplugged kits, teacher scripts; no student devices | [CodeSchool-Proposal-Offline.pdf](CodeSchool-Proposal-Offline.pdf) | [CodeSchool-Proposal-Offline.md](CodeSchool-Proposal-Offline.md) |
| **Online Programme**: app and browser on shared school devices, teacher dashboard, report-card export | [CodeSchool-Proposal-Online.pdf](CodeSchool-Proposal-Online.pdf) | [CodeSchool-Proposal-Online.md](CodeSchool-Proposal-Online.md) |

Each is a detailed school proposal (about 23-25 pages) with: a covering letter to the principal, proposal at a glance, about CodeSchool, the school's needs (CBSE requirements and handbook gaps), objectives and class-wise outcomes, scope, programme design, class-by-class overview, annual plan for 2027-28, sample weekly timetable, delivery, implementation phases and a week-by-week pilot plan, teacher development, assessment, parent engagement, governance, what the school provides, child safety and data protection, pilot success measures, investment and payment terms, roles, risks, offline-vs-online comparison, FAQs, assumptions, glossary, next steps and a fillable school response form. The Online proposal adds technical onboarding and support targets.

### Shared appendices

Both proposals pull in the same appendices from `shared/`, so edit them once:

| File | Contents |
|---|---|
| [shared/curriculum-map.md](shared/curriculum-map.md) | Appendix A: chapter-by-chapter map of every NCERT maths chapter, Classes 3-8, to CodeSchool levels |
| [shared/ai-and-projects.md](shared/ai-and-projects.md) | Appendix B: AI chapters for Classes 6-8 with offline and online activities; Appendix C: project kits and the 10-week project plan |
| [shared/assessment-lesson-teachers.md](shared/assessment-lesson-teachers.md) | Appendix D: rubrics and report-card format; Appendix E: sample lesson; Appendix F: teacher development plan |

## Before sending to a school

- Replace `[School name]`, `[Principal name]`, `[City]`, `[Date]`, `[Phone]` and `[Email]` in the markdown, then regenerate the PDF.
- Prices are **indicative** (Rs 449 / Rs 599 booklist packs; Rs 299 + GST school licence), taken from the [competitors, buying and compliance research](../research/CodeSchool-Competitors-Buying-Compliance.pdf). Confirm after interviews.
- The online technical requirements are design targets to confirm in a device check.
- "CodeSchool" is a working name; the research recommends choosing a coined brand before printing.

## Editing and regenerating

1. Edit the `.md` file. Front matter at the top sets the cover. The body supports `##` sections, `###` sub-sections, `-` bullets, `1.` numbered lists, `|` tables, `>` callouts (`> [!warn]`, `[!good]`, `[!risk]`, `[!accent]`), the `[[RESPONSE_FORM]]` and `[[PAGEBREAK]]` markers, and `[[INCLUDE shared/file.md]]` to pull in a shared section.
2. Regenerate on Windows (needs Python with `reportlab` and `pypdf`, and the Segoe UI fonts):

```bash
python -P -E docs/proposals/tools/proposal_pdf.py docs/proposals/CodeSchool-Proposal-Offline.md docs/proposals/CodeSchool-Proposal-Offline.pdf
```

`tools/` holds the converter plus the shared style library (`build_pack.py` styles and `kit_common.py`) it loads.
