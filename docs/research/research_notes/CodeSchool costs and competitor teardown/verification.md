# Verification: "CodeSchool costs and competitor teardown"

Checked 10 November 2026. The report was not edited. Part A rechecks every derived number in Tables 1-7 and the text, using Python (rounding to the nearest rupee, as the report does). Part B spot-checks the main sourced claims against the cited URLs. Corrections come first in each part. "Line" means the line number in `docs/research/reports/CodeSchool costs and competitor teardown.md`.

Overall: **the arithmetic in Tables 3-7 is right.** Every contribution, percentage, break-even count and sensitivity figure recomputes to within Rs 1 or one school. The problems are elsewhere. One stated assumption (training) does not match the numbers used, one table cell is mis-rounded, one "corrected" range uses a different discount basis from the one the report argues for, and one sourced claim (the Scratch licence) is out of date.

## Part A. Arithmetic and internal consistency

### A1. Corrections and clarifications

| Claim | Report value | Checked value | Source | Verdict | Exact suggested fix |
|---|---|---|---|---|---|
| High-case training assumption (line 166) vs Tables 4 and 5 | "Rs 20,000 high", but the tables use Rs 100 per student | Rs 20,000 ÷ 270 = **Rs 74**. Rs 100 per student = **Rs 27,000** per school. Low: Rs 6,000 ÷ 270 = Rs 22 (table uses 20, which is fine). If Rs 74 were used, High contribution would be -162 (3-5) and -172 (6-8), and Online High would be **+Rs 22**, not -Rs 4, so "Never" in Table 6 would no longer hold. | Internal | Corrected | Line 166: replace "**Training.** Rs 6,000 per school in the low case, Rs 12,000 central and Rs 20,000 high." with "**Training.** About Rs 5,400 per school in the low case, Rs 12,000 central and Rs 27,000 high (Rs 20, Rs 45 and Rs 100 per student at 270 students). The high case sits above the Rs 8,000-25,000 range estimated later." |
| Overhead break-even, re-engineered schools (Table 6, line 216) | 92 | 37 lakh ÷ 148 = 25,000 students; ÷ 270 = 92.6, so **93** | Internal | Corrected | Line 216: "520 / 92 / 90" → "520 / 93 / 90" |
| "Corrected" net to CodeSchool on default terms (line 243) | "default terms give Rs 180-269 and Rs 240-359" | Those are the 40-60% range in Table 4. The report defines default terms as **45-55%** (heading at line 50; notes section 1). 45-55% gives **Rs 202-247** on Rs 449 and **Rs 270-329** on Rs 599. | Internal; channel_economics.md §1 | Corrected | Line 243: "On the evidence here, default terms give **Rs 180-269 and Rs 240-359**." → "On the evidence here, default terms (45-55% off MRP) give **Rs 202-247 and Rs 270-329**, and the full 40-60% range in Table 4 gives Rs 180-269 and Rs 240-359." |
| Paper cost per copy (line 13) | 0.28 kg "worth Rs 18-22", right after quoting maplitho at Rs 53-82/kg | 0.28 × 53-82 = **Rs 15-23**. Rs 18-22 needs Rs 63-78/kg, which is the band the notes actually used. The 0.28 kg weight checks: 56 leaves × 0.0624 m² × 70 g × 1.15 waste = 0.281 kg. | production_costs.md §1 | Corrected | Line 13: "uses about 0.28 kg of paper, worth Rs 18-22." → "uses about 0.28 kg of paper, worth Rs 18-22 at a mid-market Rs 63-78/kg (Rs 15-23 across the full Rs 53-82/kg range)." |
| Cash outlay at 100 schools (line 95) | "about Rs 31 lakh on print, kits and freight between December and February" | 13,500 × (58+30+12) + 13,500 × (72+46+15) = **Rs 31.5 lakh**. That is correct **only with kits charged over their two-year life**. In a year when every kit is bought new, the kit cost per student roughly doubles (less about Rs 3 of teacher book), which adds about Rs 9.5 lakh, for a total of about **Rs 41 lakh**. | Internal | Corrected (clarify) | Line 95: "would spend about **Rs 31 lakh on print, kits and freight** between December and February." → "would spend about **Rs 31 lakh on print, kits and freight** between December and February, with kits charged over their two-year life (nearer Rs 40 lakh in a year when every kit is bought new)." |
| "Rs 145-310" (line 3) and "OUP and Goyal at Rs 270-310 for Classes 6-8" (line 237) | Top of range Rs 310 | The Goyal print prices for Classes 6-8 are Rs 270/290/295 (BuyBooksIndia, Table 8). Rs 309.75 is the Merit Box online MRP, which is 1.05 × the Rs 295 print price. OUP Class 8 is Rs 305. The print range is therefore **Rs 270-305**. | BuyBooksIndia; Merit Box; OUP | Corrected (minor) | Line 3: "OUP and Goyal sell plain books at Rs 145-310." → "OUP and Goyal sell plain books at Rs 145-305." Line 237: "OUP and Goyal at Rs 270-310 for Classes 6-8" → "OUP and Goyal at Rs 270-305 for Classes 6-8" |
| Online hosting, low case (Table 5, line 196) | Rs 7 per student | The text (line 140) gives Rs 15,000-40,000 a month for 10,000 students, which is **Rs 18-48** per student a year. Rs 7 matches the notes' 1-lakh-student figure (Rs 60,000-1.5 lakh a month, about Rs 7-18). Hosting also appears in Table 3's annual "platform upkeep, hosting, DPDP" line, so it may be counted twice. | development_operating_costs.md (platform inferences) | Corrected (clarify) | After line 201 ("The model leaves out any paid generative-AI calls."), add: "The low hosting figure assumes about 1 lakh students; at 10,000 students hosting is Rs 18-48 a student. Table 3's annual platform line covers upkeep and DPDP, not per-student hosting." (Or remove hosting from the Table 3 line.) |
| Classes 6-8 kit line vs stated kit cost (Table 4) | 6-8 kit + teacher book: 24 / 46 / 89; kit cost given as "Rs 800-2,500 per section" | Back-solving at 35 per section, less about Rs 3-9 of teacher book: central 46 with a two-year life implies a **Rs 3,000** section kit, and high 89 with a one-year life implies **Rs 2,800**. Both are above the Rs 2,500 ceiling. The 3-5 lines fit (about Rs 1,400-2,100). | Internal | Corrected (clarify) | Line 164: after "Kit costs include one teacher book per section." add "The Classes 6-8 line also carries two project kits a year, which takes that kit to about Rs 2,800-3,000 a section." |
| Table 7: lines held constant | Not stated | Contributions of 123 / 174 reproduce **only if** freight (12/15) and specimens (25/30) stay at central values: 292-44-48-15-12-25-25 = 123; 389-58-62-25-15-30-25 = 174. | Internal | Confirmed (add note) | Below Table 7, add: "Freight and specimens stay at their central values (Rs 12/15 and Rs 25/30)." |
| School size (line 163) | "about 270 students … That is 88 lakh students across 33,248 schools" | 88 lakh ÷ 33,248 = **265**. The earlier report's 88 lakh also covers KV/JNV schools and assumes 300 per independent school. | India schools report, Table 18 | Corrected (minor) | Line 163: "A typical CBSE school has about 270 students in Classes 3-8" → "A typical CBSE school has about 265-270 students in Classes 3-8 (270 is used below)" |
| GST wedge vs contribution (line 114, Table 11 row 3) | "about the whole central-case contribution" | Rs 21 is 140% of the Rs 15 Classes 3-5 contribution. Rs 29 is 76% of the Rs 38 Classes 6-8 contribution. | Internal | Corrected (wording) | Line 114: "about the whole central-case contribution." → "more than the whole Classes 3-5 central contribution and three-quarters of the Classes 6-8 one." |

### A2. Recomputed and confirmed

| Claim | Report value | Checked value | Verdict |
|---|---|---|---|
| Table 4 net to publisher | 269/225/180; 359/300/240 | 449 × 0.6/0.5/0.4 = 269.4/224.5/179.6; 599 × … = 359.4/299.5/239.6 | Confirmed |
| Table 4 leakage | 32/40/49; 43/54/65 | 12%/18%/27% of net = 32.3/40.5/48.6; 43.1/54.0/64.8 | Confirmed |
| Leakage band 12-27% | 12-27% | returns 5-15 + bad debt 2-5 + credit 5-7 = 12-27 | Confirmed |
| Table 4 contribution | 139/15/-188; 194/38/-198 | 139/15/-188; 194/38/-198 | Confirmed |
| Contribution % of MRP | 31/3/-42; 32/6/-33 | 31.0/3.3/-41.9; 32.4/6.3/-33.1 | Confirmed |
| Print + kit ≈ 20% of MRP (central) | ~20%; summary "Rs 90-120 a pack" | (58+30)/449 = 19.6%; (72+46)/599 = 19.7%; Rs 88 and Rs 118 | Confirmed |
| S Chand material = 16-19% of MRP | 32% of net at 50-60% realisation | 0.32 × 0.50-0.60 = 16.0-19.2% | Confirmed |
| Freight 2-4% of MRP | Rs 8-24 | 2-4% = Rs 9-18 (449) and Rs 12-24 (599). The Rs 8 low is 1.8%. | Confirmed (within rounding) |
| Table 5 net | 299/269/224 | 299/269.1/224.25 | Confirmed |
| Table 5 collection loss | 15/27/45 | 14.95/26.9/44.85 | Confirmed |
| Table 5 contribution | 247/152/-4 | 247/152/-4 (at Rs 100 high training; see A1) | Confirmed |
| Rs 299 × 1.18 | Rs 353 | 352.82 | Confirmed |
| Rs 299 "63% below" Rs 799 | 63% | 62.6% | Confirmed |
| Table 7 net (35% discount) | 292 / 389 | 291.85 / 389.35 | Confirmed |
| Table 7 leakage 15% | 44 / 58 | 43.8 / 58.4 | Confirmed |
| Table 7 contribution | 123 (27%) / 174 (29%) | 123 (27.4%) / 174 (29.0%) | Confirmed |
| Table 6 offline low | Rs 166; 15,000; 56 | (139+194)/2 = 166.5; 25 lakh/166.5 = 15,015; 55.6 schools | Confirmed |
| Table 6 offline central default | Rs 26.5; 1,89,000; 700 | 50 lakh/26.5 = 188,679; 698.8 schools | Confirmed |
| Table 6 re-engineered | Rs 148; 34,000; 125 | 50 lakh/148 = 33,784; 125.1 schools | Confirmed |
| 125 schools = 0.4% of 33,248 | 0.4% | 0.38% | Confirmed |
| Table 6 online low / central | 8,100/30; 29,600/110 | 8,097/30.0; 29,605/109.6 | Confirmed |
| Table 6 overhead, offline default / online | 1.4 lakh/520; 24,000/90 | 139,623/517; 24,342/90.2 | Confirmed |
| Summary "1.9 lakh students, or 700 schools"; "34,000 … 125 schools" | as stated | as above | Confirmed |
| Three executives × 20 schools | 16,000 students; Rs 4.3 lakh | 60 × 270 = 16,200; × 26.5 = Rs 4.29 lakh | Confirmed |
| Table 3 totals | 45 / 95 / 148 lakh; overhead 19.5 / 37 / 62 lakh | 25+20, 50+45, 75+73; 5+2.5+12, 10+7.5+19.5, 20+15+27 | Confirmed |
| Content refresh 10-20% | 2.5 / 7.5 / 15 lakh | 10% of 25, 15% of 50, 20% of 75 | Confirmed |
| Field executives | 12 / 19.5 / 27 lakh | 3 × Rs 4 / 6.5 / 9 lakh | Confirmed |
| Platform Rs 26-62 lakh | USD 30-70k × 88 | 26.4-61.6 lakh | Confirmed |
| Platform high Rs 73 lakh | 73 | 62 + VAPT for 3 surfaces (up to 6) + DPDP 5 = 73 | Confirmed |
| Receivables peak at 100 schools | Rs 71 lakh | 13,500 × 225 + 13,500 × 300 = Rs 70.9 lakh | Confirmed |
| Mixed-supply GST on inclusive MRP | Rs 21 / Rs 29 | 449 × 5/105 = 21.4; 599 × 5/105 = 28.5 | Confirmed (if the pack became taxable, about Rs 2-3 of printing GST would become creditable, so the net hit is slightly lower) |
| +Rs 50 MRP → about Rs 20 | Rs 20 | 50 × 0.5 × 0.82 = 20.5 | Confirmed |
| 10 points of channel share → Rs 37 / Rs 49 | Rs 37-49 | 449 × 0.1 × 0.82 = 36.8; 599 × 0.1 × 0.82 = 49.1 | Confirmed |
| Matching Tekie at Rs 629 adds about Rs 12 | Rs 12 | 30 × 0.5 × 0.82 = 12.3 | Confirmed |
| Earlier report's net figures | Rs 270-315 / Rs 360-420 at 30-40% | Earlier report (CT kit … compliance, lines 159-160) states exactly these; 449 × 0.6-0.7 = 269-314; 599 × 0.6-0.7 = 359-419 | Confirmed |
| Table 7 routes reach earlier range | "higher figures reachable only through Table 7" | Rs 292 is inside 270-315; Rs 389 is inside 360-420 | Confirmed |
| Kit Rs 1,400 ÷ 35 | Rs 40; Rs 12-15 over 3 years | 40.0; 13.3 | Confirmed |
| Floor mat | Rs 430-1,440; Rs 2,560 | 36 × 12-40 = 432-1,440; 64 × 40 = 2,560 | Confirmed |
| "Threefold gap to Goyal" | ~3× | 449 / 145-165 = 2.7-3.1 | Confirmed |
| Per-school minimum Rs 25,000-30,000 | — | Rs 299 × 100 students = Rs 29,900 | Confirmed (consistent) |
| Conclusion "about Rs 150 to … Rs 15-40" | 152 vs 15/38 | matches Tables 4-5 | Confirmed |
| Slimmer 64-80 pp book saves Rs 8-15 | Rs 8-15 | 29-43% fewer pages × about Rs 26-33 of page-driven cost = Rs 7.5-14 | Confirmed |

## Part B. Sourced claims (spot-check)

### B1. Corrections

| Claim | Report value | Checked value | Source | Verdict | Exact suggested fix |
|---|---|---|---|---|---|
| Scratch code licence (line 143) | "Scratch's code is BSD-3" | scratch-gui, scratch-vm and scratch-render are now **AGPL-3.0-only**. The commit "chore!: set license to AGPL-3.0-only" landed on 25 Nov 2024. scratch-blocks is Apache-2.0. The TRADEMARK wording is confirmed. AGPL means a modified Scratch editor served to schools over the web must publish its source. | GitHub API `repos/scratchfoundation/{scratch-gui,scratch-vm,scratch-render,scratch-blocks}/license`; scratch-gui LICENSE commit history; [scratch-gui TRADEMARK](https://raw.githubusercontent.com/scratchfoundation/scratch-gui/develop/TRADEMARK) | Corrected | Line 143: "Free. Blockly and Teachable Machine are Apache 2.0, and Scratch's code is BSD-3. MIT bars using the Scratch name and cat to promote derived products, so a Scratch-based editor needs its own brand" → "Free. Blockly and Teachable Machine are Apache 2.0. Scratch's editor code (scratch-gui, scratch-vm, scratch-render) has been AGPL-3.0 since November 2024, so a modified Scratch editor offered online must publish its source; scratch-blocks is Apache 2.0. MIT also bars using the Scratch name and cat to promote derived products, so a Scratch-based editor needs its own brand" and add [scratch-gui LICENSE](https://github.com/scratchfoundation/scratch-gui/blob/develop/LICENSE) to the citations. |
| Jabalpur: 51 people, Rs 4.12 crore, ISBNs (line 69) | Cites SCC Online and LiveLaw for all of it | The facts are right, but neither cited page gives "51" or "Rs 4.12 crore". The Hitavada (28 May 2024) reports FIRs against 51 persons, Rs 81.30 crore of fees and Rs 4.12 crore of book commission. SCC Online and LiveLaw confirm that the MP High Court (B.P. Sharma J.) refused to quash the FIRs in April 2026, and they describe the ISBNs as "fake or duplicate". | [The Hitavada](https://www.thehitavada.com/Encyc/2024/5/28/DIRTY-BUSINESS-FIR-against-51-from-11-schools-21-nabbed-accused-illegally-hiked-school-fees-pocketted-commi.html); [SCC Online](https://www.scconline.com/blog/post/2026/04/29/mp-hc-no-relief-to-private-schools-for-unauthorized-fee-hike-and-book-selling/); [LiveLaw](https://www.livelaw.in/high-court/madhya-pradesh-high-court/madhya-pradesh-high-court-private-unaided-schools-fir-fake-isbns-school-fees-hike-531340) | Corrected (citation and wording) | Line 69: "over a Rs 4.12 crore "books commission" and unverifiable ISBNs. In April 2026 the High Court refused to quash them (" → "over a Rs 4.12 crore "books commission" ([The Hitavada, May 2024](https://www.thehitavada.com/Encyc/2024/5/28/DIRTY-BUSINESS-FIR-against-51-from-11-schools-21-nabbed-accused-illegally-hiked-school-fees-pocketted-commi.html)) and books with fake or duplicate ISBNs. In April 2026 the High Court refused to quash the FIRs (". Line 313: "Jabalpur FIRs cited unverifiable ISBNs" → "Jabalpur FIRs cited fake or duplicate ISBNs" |
| LEAD CCS (Table 9, line 276) | "Scratch Jr to Python, 26-week units"; "BCA or MCA teachers for Classes 6-8" | The page describes "a 26-week program", not 26-week units. For Classes 6-8 the teacher needs "either a BCA/ MCA or an equivalent diploma". "One computer for every two or three students" is confirmed. | [LEAD](https://leadschool.in/teaching-coding-to-kids-ccs-is-here-to-help-your-school) | Corrected | Line 276: "Scratch Jr to Python, 26-week units" → "Scratch Jr to Python, a 26-week programme"; "BCA or MCA teachers for Classes 6-8" → "teachers with a BCA, MCA or equivalent diploma for Classes 6-8" |
| LEAD FY26 loss (line 284) | Rs 34.5 crore, citing YourStory | Inc42: operating revenue Rs 386.7 crore (FY25 Rs 351.8 crore), net loss **Rs 34.5 crore** (FY25 Rs 43.3 crore). YourStory returned 403. A search summary says YourStory gives loss after tax of Rs 33.0 crore (not verified). | [Inc42](https://inc42.com/?p=570148) | Confirmed (add citation) | Line 284: "([YourStory](https://yourstory.com/2026/08/edtech-lead-fy26-revenue-rises-387-crore-losses-narrow-over-20-percent))" → "([YourStory](https://yourstory.com/2026/08/edtech-lead-fy26-revenue-rises-387-crore-losses-narrow-over-20-percent); [Inc42](https://inc42.com/?p=570148))" |

### B2. Confirmed

| Claim | Report value | Checked value | Source | Verdict | Fix |
|---|---|---|---|---|---|
| Printed books 4901 nil | Nil | "Exempt goods … Nil"; books portion nil | [TaxGarden](https://taxgarden.in/blog/gst-on-printing-services-books-packaging-india-2026) | Confirmed | — |
| Exercise books 4820: 12% → nil | 12% → nil | "Reduced from 12% to Nil under GST 2.0, effective 22 Sept 2025"; registers stay at 18% | TaxGarden | Confirmed | — |
| Printing with printer's paper, SAC 9989, 5% | 5% | "taxed at 5% with full input tax credit" | TaxGarden | Confirmed | — |
| Uncoated paper 18% | 18% | 4802 at 18% (Notif. 09/2025-CT(R), 17 Sept 2025), except exercise-book paper (nil, Notif. 10/2025) | [TaxGuru](https://taxguru.in/?p=993339) | Confirmed | — |
| Corrugated boxes 4819 5% | 5% | "cut from 12% to 5% under GST 2.0" | TaxGarden | Confirmed | — |
| Board games 9504 / puzzles 9503: 12% → 5% | 12% → 5% | Secondary tables give 12% → 5% for board games and playing cards. A CBIC circular confirms the 5% entry covers all non-electronic 9503 toys, puzzles included. The primary 9504 entry was not read. | Search of TaxGuru/L&S/CBIC summaries. The cited [ClearTax](https://cleartax.in/s/gst-rate-revamp-list-of-cheaper-and-costlier-items) page no longer lists these items. | Confirmed (secondary) | Optional: replace the ClearTax citation, which no longer carries item rates |
| Input-credit split for mixed outputs | Must be split | Rule 42/43 apportionment; exempt share reversed under s.17(2) | TaxGarden | Confirmed | — |
| Mixed vs composite supply | Mixed taxed at highest rate; composite at principal-supply rate | CGST Act s.8(b) (mixed: highest rate) and s.8(a) (composite: principal supply) | Statute | Confirmed | — |
| S Chand 80-85% of revenue in Jan-Mar | 80-85% | "80-85% of our annual number we do in that Q4" (Atul Soni) | [S Chand Q4 FY25 call](https://files.tijorifinance.com/insight/india/7264/Conference%20Call/CC-Mar25.pdf) | Confirmed | — |
| S Chand 68% gross margin FY25 | 68% | "highest annual gross margins at 68% vs 66% in FY24" | Same | Confirmed | — |
| S Chand receivables 140 days FY25, inventory 223 days | 140 / 223 | "140 days (vs. 143 days in Q4FY24)"; "223 days (vs. 284 …)"; NWC 151 days | Same | Confirmed | — |
| S Chand caps returns | Caps by policy | "strict policies in terms of sales return, which we have pegged to a certain level" | Same | Confirmed | — |
| S Chand receivables 160 days FY26 | 160 | 160 days (from 140); NWC 164 (from 151). The cited page now redirects to financialfilings.com and blocks bots; confirmed via search summaries of the transcript and multibagg.ai. | [financialreports.eu](https://financialreports.eu/filings/s-chand-and-company-limited/call-transcript/2026/47858706/) | Confirmed (secondary access) | — |
| MP High Court April 2026 | Refused to quash | Dismissed petitions to quash FIRs (decided 6 Apr 2026 per SCC; LiveLaw file dated 21 Apr 2026) | SCC Online; LiveLaw | Confirmed | See B1 for the citation fix |
| NHRC April 2026 notices to every state | All states | Notices to MoE, CBSE and all states and UTs; pan-India audit (article 29 Apr 2026) | [PrintWeek](https://www.printweek.in/article/nhrc-orders-audit-on-costly-school-textbooks/4j01mkmty0dd7xccg492abq94s) | Confirmed | — |
| Delhi DoE 1 April 2026 | Barred forced purchase from specific vendors | Issued "on Wednesday" (1 Apr 2026 was a Wednesday); "not to force students or parents to purchase … from specific vendors" | [Business Today](https://www.businesstoday.in/india/story/delhi-govt-orders-private-schools-to-stop-forcing-students-to-buy-books-uniforms-from-specific-vendors-523625-2026-04-02) | Confirmed | — |
| Uolo Tekie from Rs 799; 500K students, 1,000+ schools; home access; auto-graded homework; no offline stated | as stated | "Starting @ ₹799/Student/Year"; "500K+ students from 1000+ schools"; offline not mentioned | [Uolo](https://uolo.co/tekie.html) | Confirmed | — |
| Uolo raised US$7M in Dec 2025 | US$7M | $7M Pre-Series B led by Five Sigma, 10 Dec 2025 | [Outlook Business](https://www.outlookbusiness.com/start-up/investors/edtech-start-up-uolo-bags-7-mn-funding-from-five-sigma-other-investors) | Confirmed | — |
| Uolo FY24 loss Rs 58.1 crore on about Rs 27.9 crore revenue | as stated | Revenue Rs 27.95 crore (Indian Startup Times: Rs 27.9 crore); loss Rs 58.11 crore (TheKredible, via search; the page returned 530) | [Indian Startup Times](https://www.indianstartuptimes.com/?p=26900); TheKredible | Confirmed | — |
| LEAD needs 1 PC per 2-3 students | as stated | "One computer for every two or three students" | LEAD | Confirmed | See B1 for the wording fix |
| LEAD FY26 revenue Rs 387 crore | Rs 387 crore | Rs 386.7 crore | Inc42 | Confirmed | — |
| CBSE deck: platform agnostic, largely unplugged, no computer required | as stated | "Platform agnostic curriculum"; "Largely unplugged"; "no computer required. AI activities use simple digital tools where available." | [CBSE webinar deck](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf) | Confirmed | — |
| CBSE deck: assessment not "write a program", no computer access assumed | as stated | "There is no "write a program" … no expectation of computer access for assessment" | Same | Confirmed | — |
| CBSE deck: hours | 3-5: 50 h, CT only, inside Maths/TWAU; 6-8: 100 h = 40 CT + 20 AI + 40 projects | Exactly as stated ("Hours are indicative") | Same | Confirmed | — |
| CBSE deck: project rubrics "coming soon" | as stated | "COMING SOON … AI Project list with rubrics (40 hours, two projects per grade)" | Same | Confirmed | — |
| OUP Class 8 Rs 305, 152 pages | as stated | Rs 305; 152 pp; ISBN 9789373746487; "all-in-one"; matches recommended hours | [OUP](https://india.oup.com/product/computational-thinking-and-artificial-intelligence-class-8-9789373746487/) | Confirmed | — |
| Goyal Think Smart ~145-165 (3-5); 270-295 (6-8) | as stated | Print: Cl 6 Rs 270, Cl 7 Rs 290, Cl 8 Rs 295 (BuyBooksIndia); Cl 5 print MRP Rs 165. Merit Box MRPs Rs 152.25 / 162.75 / 304.5 / 309.75 are 1.05 × Rs 145 / 155 / 290 / 295. | [BuyBooksIndia](https://www.buybooksindia.com/think-smart-my-book-of-computational-thinking-artificial-intelligence-class-6-ay-2026-27--9789377390143-126029.htm); [Merit Box](https://meritbox.app/books/think-smart-my-book-of-computational-thinking-artificial-intelligence-class-5-ay-2026-27%29) | Confirmed | See A1 for the Rs 310 → 305 fix |
| Tekie.AI Accelerate Rs 579-629 on CMS booklist, under "Computational Thinking & ICT" | as stated | Grade 4 Rs 579, Grade 5 Rs 599, Grades 6-8 Rs 629; subject "Computational Thinking & ICT" | [CMS booklist](https://cmseducation.org/wp-content/uploads/2026/03/Classes-IV-to-VIII-2026-2027.pdf) | Confirmed | — |
| Orange has no CT&AI series for Classes 3-8 | None | The catalogue text has no CT&AI-titled series. CT appears only as a strand in its computer series, plus the slogan "Computational Thinking & AI". It lists 901, 417 and 843 AI titles, "More than 4000 workshops have been conducted last year", and a Test Paper Generator, Mini LMS and Capstone Project. Text was extracted from the PDF, so titles set only as images could be missed. | [Orange Catalogue 2026-27](https://www.orangewebsupport.co.in/assets/files/Catalogue/Catalogue26-27.pdf) | Confirmed | — |
| Blockly Apache 2.0 | Apache 2.0 | npm registry: blockly 13.4.0, licence Apache-2.0 | [npm blockly](https://npmjs.com/package/blockly) | Confirmed | — |
| Scratch trademark restriction | MIT bars use to promote derived products | TRADEMARK file confirms, word for word | scratch-gui TRADEMARK | Confirmed | See B1: the licence part is wrong |

### B3. Not checked

Paper tracker prices, kit and freight listings, salary and agency rates, Odisha AAR, Sonka, Navneet days, EdTechReview 36.5%, STEMpedia, STEMROBO and Ulipsu were not reopened in this pass. They feed (est.) ranges and none of them changes a verdict.
