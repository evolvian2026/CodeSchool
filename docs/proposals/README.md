# School proposals (drafts)

Two separate proposals a school can ask for, both drafts to be revised after school feedback:

| Proposal | PDF | Editable source |
|---|---|---|
| **Offline Programme**: printed workbooks, unplugged kits, teacher scripts; no student devices | [CodeSchool-Proposal-Offline.pdf](CodeSchool-Proposal-Offline.pdf) | [CodeSchool-Proposal-Offline.md](CodeSchool-Proposal-Offline.md) |
| **Online Programme**: app and browser on shared school devices, teacher dashboard, report-card export | [CodeSchool-Proposal-Online.pdf](CodeSchool-Proposal-Online.pdf) | [CodeSchool-Proposal-Online.md](CodeSchool-Proposal-Online.md) |

Each covers: proposal at a glance, why, objectives, scope, programme design (class-by-class), delivery, implementation timeline, teacher support, assessment, what the school provides, child safety and data protection, pilot success measures, investment, roles, risks, offline-vs-online comparison, next steps and a fillable school response form.

## Before sending to a school

- Replace `[School name]`, `[Phone]` and `[Email]` in the markdown, then regenerate the PDF.
- Prices are **indicative** (Rs 449 / Rs 599 booklist packs; Rs 299 + GST school licence), taken from the [competitors, buying and compliance research](../research/CodeSchool-Competitors-Buying-Compliance.pdf). Confirm after interviews.
- The online technical requirements are design targets to confirm in a device check.
- "CodeSchool" is a working name; the research recommends choosing a coined brand before printing.

## Editing and regenerating

1. Edit the `.md` file. Front matter at the top sets the cover. The body supports `##` sections, `###` sub-sections, `-` bullets, `1.` numbered lists, `|` tables, `>` callouts (`> [!warn]`, `[!good]`, `[!risk]`, `[!accent]`), and the `[[RESPONSE_FORM]]` marker.
2. Regenerate on Windows (needs Python with `reportlab` and `pypdf`, and the Segoe UI fonts):

```bash
python -P -E docs/proposals/tools/proposal_pdf.py docs/proposals/CodeSchool-Proposal-Offline.md docs/proposals/CodeSchool-Proposal-Offline.pdf
```

`tools/` holds the converter plus the shared style library (`build_pack.py` styles and `kit_common.py`) it loads.
