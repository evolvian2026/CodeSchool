# Prospect list (private)

This folder holds the working list of target schools for the April 2027 launch. **Everything with school-level data stays private.** Files named `*.private.*` are ignored by Git and never reach the public repository. Only this README and the script are committed.

## 1. Download from CBSE SARAS (by hand)

CBSE's directory blocks automated tools, so the downloads are done by hand in a normal browser.

1. Open [saras.cbse.gov.in](https://saras.cbse.gov.in/) → **List of Affiliated Schools**.
2. Search by **state** for: Uttarakhand, Himachal Pradesh, Punjab, Rajasthan, Uttar Pradesh, Haryana, Delhi and Chandigarh.
   - Large states (UP, Rajasthan, Haryana, Punjab) may be easier **district by district**.
   - For the NCR, also check Gurugram, Faridabad (Haryana) and Gautam Buddh Nagar (Noida) and Ghaziabad (UP).
3. If the results page has an **Export / Excel** button, use it. If not, select the results table, copy it and paste into Excel.
4. Save each file here with `.private.` in the name, for example:
   - `saras-haryana.private.xlsx`
   - `saras-up-lucknow.private.xlsx`
   - `saras-delhi.private.csv`

Any column layout is fine; the script matches columns by their headings.

## 2. Build the list

```bash
python -P -E docs/research/prospects/build_prospects.py
```

It reads every `saras-*.private.xlsx` / `.csv` in this folder and writes:

| Output | Contents |
|---|---|
| `launch-schools.private.csv` | One row per school: affiliation number, school, address, district, state, management type, private or not, launch-area flag, website, official email and phone (where SARAS gives them), source file, date |
| `launch-schools-summary.private.txt` | Counts by state, district, management type and launch area |

Principal names are **not** copied into the output, to keep personal data to the minimum. Duplicates (the same affiliation number in two downloads) are merged.

## 3. Add official contacts

Next, each school's **official** email and phone are added from the Mandatory Public Disclosure page CBSE requires schools to publish on their own websites, starting with the four launch areas (Delhi NCR, Chandigarh tricity, Lucknow, Jaipur). Each added contact records its source URL and date.

## Rules

- Use only official school contacts (school email, office phone). No personal mobiles, no bought lists.
- Follow the outreach rules in the [contacts guide](../CodeSchool-School-Contacts-Guide.pdf): no cold WhatsApp, calls and SMS only from TRAI-registered numbers, an opt-out in every email, no inducements to schools.
- Delete a school's contact details if it asks, and keep a suppression list (`suppression.private.csv`).
