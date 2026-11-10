# Supplier quote requests

Draft requests to replace the estimates in the [costs and competitor report](../reports/CodeSchool%20costs%20and%20competitor%20teardown.md) with real numbers. That report's cost figures are built from published rates, not quotes, so these are the first things to confirm.

| File | Send to | What it settles |
|---|---|---|
| [01-printer-quote-request.md](01-printer-quote-request.md) | 3 offset printers | Cost per workbook at 1,000-20,000 copies, paper rate, GST, lead time, a 50-copy specimen run |
| [02-kit-quote-request.md](02-kit-quote-request.md) | 2-3 card and game makers | Cost per classroom kit, die charges, a prototype, GST classification |
| [03-distributor-terms-enquiry.md](03-distributor-terms-enquiry.md) | 2-3 distributors and 2-3 booksellers | Real discount off MRP, credit days, returns: the numbers that decide the margin |
| [quote-comparison-template.csv](quote-comparison-template.csv) | — | One row per supplier, item and quantity, to compare replies side by side |

## How to use them

1. Fill in the [square brackets]: dates, city or PIN code, phone, email. Each file has a short WhatsApp opener to get an email ID first.
2. Send all requests in the same week, with the same specification, so the quotes compare like for like. Ask for replies within about 10 days.
3. Record each reply in a **private** copy of the comparison sheet: `quote-comparison.private.csv`. Files named `*.private.*` are ignored by Git.
4. When the quotes are in, the per-student margin tables in the costs report can be re-run with real numbers.

## Timing

Most schools finalise next year's booklist in December-January. Specimen copies would be needed by about mid-December for an April 2027 start, so the printer and kit requests are urgent if that start date is chosen. The distributor enquiry is useful either way.

## Keep it private

**This repository is public.** Don't commit supplier names, contacts, quotes or negotiated terms. Use school-style codes (P1-P3 for printers, K1-K2 for kit makers, D1-D2 for distributors, B1 for booksellers) in anything shared.

## Before signing anything

- Ask a chartered accountant to confirm GST on the workbook (nil), the kit (5%?), any book-plus-kit bundle and the online licence (18%). See the costs report.
- Treat these requests as enquiries, not orders. Each file says so.
- Don't share full lesson content with suppliers before an agreement. These requests share only specifications.
