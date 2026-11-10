# Official School Directories in India and Rules for B2B Outreach to Schools

Scope: where a company launching a CBSE CT&AI programme (Classes 3-8, April 2027) can lawfully find each school's official contact details, and how it may contact schools by email, phone/SMS and WhatsApp. Current as of 10 November 2026. This is research, not legal advice. No individual's contact details were collected; only directory structures and rules are described. Several primary government sites (trai.gov.in PDF, udiseplus.gov.in PDF, devlocate.cisce.org) refused or failed automated fetches, so some points rest on secondary sources and are flagged.

## 1. CBSE SARAS directory and CBSE Mandatory Public Disclosure

### Takeaway
SARAS (saras.cbse.gov.in) is the official CBSE affiliated-school list. Each school's record shows its identity, address, website, principal's name and qualifications, school status/type and affiliation period, but the live detail page checked had **no email or phone field**. Official school email and phone numbers are more reliably found in each school's **Mandatory Public Disclosure** (Appendix IX of the Affiliation Bye-Laws). Schools must post this prominently on their own websites, and CBSE has been tightening enforcement through 2026.

### Cited Findings
- A live SARAS school detail page (URL pattern `saras.cbse.gov.in/SARAS/AffiliatedList/AfflicationDetails/<affiliation no.>`) shows these fields: Name of Institution, Affiliation Number, State, District, Postal Address, Pin Code, Website, Year of Foundation, Date of First Opening, Name of Principal/Head of Institution, Gender, Principal's Educational/Professional Qualifications, Administrative and Teaching Experience (years), Status of the School, School Type, Type of affiliation, Affiliation Period (From/To), Name of Trust/Society/Managing Committee, Remarks. **The page has no email or phone fields.** — [SARAS school detail page](https://saras.cbse.gov.in/SARAS/AffiliatedList/AfflicationDetails/2730312)
- SARAS has a "List of Affiliated Schools" view with category-wise listing, plus a "Contact Us" page with CBSE affiliation helplines. The search summary gives the affiliation query email as `cbse.aff@nic.in`. This is CBSE's own contact, not a school's. — [SARAS Category_Wise](https://saras.cbse.gov.in/SARAS/Home/Category_Wise)
- Older printouts of CBSE directory pages (for example on KVS school sites) show head/principal name, address, phone and email per school, plus an "Affiliated up to" date. So earlier or other views of the directory may have shown phone and email. **This conflicts** with the current detail page above, which has no contact fields. — [KVS Kutra affiliation printout](https://kutra.kvs.ac.in/sites/default/files/CBSE%20AFFLIATION%20CERTFICATE.pdf)
- Appendix IX "Mandatory Public Disclosure" was introduced by CBSE Circular No. 03 dated 05.03.2021. Schools must upload it "at prominent place on the website". A later CBSE notice requires a distinctly visible icon labelled "Mandatory Public Disclosure" on the home page. — [CBSE Circular 3 (SARAS)](https://saras.cbse.gov.in/saras/Circulars/Circular3.pdf); [KVS Colaba copy of CBSE notice](https://no1colaba.kvs.ac.in/sites/default/files/N_909_1703249154561%20%283%29.pdf)
- SARAS now generates the disclosure document ("Mandatory Disclosure Details – SARAS 6.0/7.0"). Schools have posted 2025 and 2026 versions with sections for general information, documents, results/academics, staff and infrastructure. — [DPS Bopal SARAS 6.0 disclosure](https://dpsbopal-ahd.edu.in/wp-content/uploads/2025/10/Mandatory-Disclosure-Details-_-SARAS-6.0.pdf); [Global Indian School SARAS 7.0, May 2026](https://globalindianschool.org/dubai/wp-content/uploads/2026/05/Mandatory-Disclosure-Details-_-SARAS-7.0-2.pdf)
- Search summaries say the disclosure can include the principal's contact number and email ID. I could not open the PDF to confirm the exact field labels. — [Mandatory Disclosure example, CHIREC 2025](https://www.chirec.ac.in/wp-content/uploads/sites/15/2023/11/Mandatory-Disclosure-Details-2025.pdf)
- CBSE Circular No. 1/2026 (12.01.2026) refers to a "Revised Format of Appendix IX" and tells schools to keep teacher details updated on their websites. — [PSBB Millennium copy of circular, Jan 2026](https://psbbmillenniumschool.org/wp-content/uploads/2026/01/circular-1.pdf)
- CBSE has warned schools to upload pupil-teacher ratio, results, fees and staff data online by 15 February 2026 "or face action". — [Careers360 news](https://news.careers360.com/cbse-schools-class-10-12-results-fees-student-teacher-details-online-by-february-15-2026-affiliation-rules-public-disclosures/amp)
- Compliance is patchy. One Careers360 analysis found only about 40% of disclosures fully completed as per norms. — [Careers360](https://news.careers360.com/how-many-schools-violate-cbse-regulations-on-mandatory-disclosures)

### Inferences
- Workable lawful pipeline: (1) use SARAS to list affiliated schools by state or district and capture school-level facts (name, affiliation no., address, website, affiliation validity, school type/status); (2) visit each school's own website and its "Mandatory Public Disclosure" page for the **official school email and phone** published under a CBSE obligation; (3) prefer generic institutional addresses (e.g., `principal@`, `info@`, `office@` at the school's domain) over personal mobiles or personal Gmail addresses.
- "Affiliation Period To" helps avoid wasting effort on lapsed schools, and "School Type"/"Status" (e.g., secondary/senior secondary, independent/KV/JNV) helps segment. SARAS does not cleanly show whether a school runs Classes 3-8, because affiliation is at secondary/senior secondary level. The disclosure or the school website gives class ranges.
- The disclosure is published by the school because CBSE bye-laws require it. That matters for the DPDP "legal obligation" limb (Section 3 below).

### Gaps
- No official bulk export (CSV/Excel) or API for SARAS was confirmed. Check the live portal for state/district list pages and any download button. Automated scraping may conflict with site terms. I did not find SARAS terms of use.
- How fresh the data is (how often schools update SARAS) was not documented. The 2026 enforcement push suggests records were being refreshed in 2026.
- The exact Appendix IX field list in the revised 2026 format (whether it includes school email, school phone and principal contact) could not be read, because the circular PDF is a scanned image. Verify against a current SARAS 7.0 disclosure.

## 2. UDISE+ / "Know Your School" / school report cards

### Takeaway
UDISE+ (udiseplus.gov.in) collects school contact details (landline, mobile, email, website) from every school. Public access, however, is to aggregated data and school report cards (profile, enrolment, teachers, infrastructure). I found **no evidence that contact fields are published publicly**, and the government has reportedly stopped sharing the 11-digit UDISE code with data users. Treat UDISE+ as a source for school existence and profile, not contacts.

### Cited Findings
- The UDISE+ Data Capture Format asks each school for "School Contact Details: STD Code, Landline Number, Mobile Number, Email, Website". This shows what schools **submit**, not what is published. — [UDISE+ DCF 2023-24 (via educationforallinindia)](https://educationforallinindia.com/wp-content/uploads/2023/09/data-capture-format-2023-24-DOSEL-MoE-India.pdf); [Meghalaya DCF 2021-22](https://ssa.megeducation.gov.in/Document/Forms/DCF-2021-22.pdf)
- The UDISE+ Data Sharing Policy has annexes with sample urban/rural school report cards, but the PDF link now returns 404 and its field list could not be read. — [UDISE+ DSP (link dead at time of research)](https://www.udiseplus.gov.in/assets/img/pdfFiles/DSP_english.pdf)
- A secondary guide says aggregated data is freely available, while raw data or data with personally identifiable information is restricted. It also says the public report card shows profile, enrolment, teacher and infrastructure data without login. This is a third-party source and unverified. — [Schoolites UDISE+ guide](https://schoolites.com/udise/school-report); [Anantam IAS](https://anantamias.com/udise-plus/)
- An education-data site reports that the 11-digit UDISE school ID "is no more shared with data users". — [Education for All in India](https://educationforallinindia.com/11-digit-udise-school-id-is-no-more-shared-with-data-users)

### Inferences
- Do not rely on UDISE+ for email or phone. Even if contacts could be extracted through logged-in state/official portals, using them for marketing would likely breach the data-sharing terms. They were also not "made publicly available", so the DPDP exclusion would be doubtful.

### Gaps
- Whether the live Know Your School / public report card (kys.udiseplus.gov.in) shows head-teacher name or school phone could not be checked directly.

## 3. Other boards and school systems: CISCE, IB, Cambridge, state boards, KVS, NVS

### Takeaway
CISCE runs an official public school locator whose listings include head and admin contact details. KVS schools each have an official sub-site (`<name>.kvs.ac.in`), and some KVS principals use `kvs.gov.in` addresses, but there is no consolidated official email directory, and older lists mix in Gmail/Yahoo addresses. IB, Cambridge and state-board finders could not be verified in this session.

### Cited Findings
- The CISCE official locator ("Locate a CISCE Affiliated School", devlocate.cisce.org) is a paginated directory of roughly 3,244 entries. Listings show school code, name, day/boarding status, classes offered, and the head's and admin's contact details. Automated fetch was refused (HTTP 403), so this is from search-result summaries. — [CISCE locator](https://devlocate.cisce.org/?page=22)
- KVS schools run official sub-domain websites on kvs.ac.in (e.g., kutra.kvs.ac.in, no1colaba.kvs.ac.in), which host their CBSE disclosures. — [KVS Kutra](https://kutra.kvs.ac.in/sites/default/files/CBSE%20AFFLIATION%20CERTFICATE.pdf); [KVS Colaba](https://no1colaba.kvs.ac.in/sites/default/files/N_909_1703249154561%20%283%29.pdf)
- A 2017 KVS procurement annex lists per-Vidyalaya emails, many on Gmail/Yahoo. An NCTE list uses `ppl.<place>@kvs.gov.in`-style addresses for some principals. So KVS email conventions are mixed, and older lists may be outdated. — [KVS annex 2017](https://kvs.ac.in/sites/default/files/ANN-3-29-12-2017.pdf); [NCTE pilot schools list](https://ncte.gov.in/Website/images/NMM/notice-board/List%20of%2030%20Pilot%20Schools%20for%20National%20Mission%20for%20Mentoring.pdf)
- A third-party source says there are about 1,228 KVs (1,225 in India). — [Wikipedia mirror, List of Kendriya Vidyalayas](https://ipfs.ssi.eecc.de/ipns/en.wikipedia-on-ipfs.org/wiki/List_of_Kendriya_Vidyalayas)

### Inferences
- KVs and JNVs are central government schools. Procurement and programme adoption are usually decided at KVS/NVS headquarters or regional office level, not by individual principals. Outreach should go through official channels (regional offices/HQ) rather than cold-contacting each principal for a sale. Gifts or inducements to government staff raise additional conduct-rule issues (covered elsewhere).
- CISCE contacts are published by the board itself, which supports a "made publicly available" argument, but not necessarily the "legal obligation" limb.

### Gaps
- IB ("Find an IB World School", ibo.org) and Cambridge ("Find a Cambridge school", cambridgeinternational.org) finders did not appear in search results. Their fields (whether they show email/phone) and terms of use are unverified.
- State board directories (e.g., state UDISE/education department school lists) were not researched for lack of budget.
- No official NVS/JNV consolidated directory was found. The NVS website (navodaya.gov.in) should be checked directly.
- CISCE locator terms of use and export options are unknown.

## 4. DPDP Act 2023 and DPDP Rules 2025: using principals' published official contacts

### Takeaway
Section 3(c)(ii) of the DPDP Act excludes from the Act personal data made publicly available (a) by the data principal themselves, or (b) by another person under a legal obligation to publish it. A principal's name and official contact posted in a CBSE-mandated disclosure plausibly fits limb (b). Commentators say firms must **document how each item became public**, and the exclusion's limits are untested in court. The Rules were notified in November 2025, and the substantive obligations (notice, consent, security, erasure, breach) apply from **13/14 May 2027**, just after the April 2027 launch. Lawyer review is needed.

### Cited Findings
- India Briefing (10 Sept 2026) paraphrases Section 3(c)(ii): the Act does not apply to personal data "made or caused to be made publicly available by the Data Principal" or by "another person who is under a legal obligation to make it publicly available". Its examples of the latter are corporate filings, court records and regulatory disclosures. — [India Briefing](https://www.india-briefing.com/news/india-dpdp-act-publicly-available-personal-data-46899.html/)
- The same source says businesses should map their data sources, record how each item became public, document why they rely on the exclusion, check website terms and IP/computer-access laws before scraping, do due diligence on purchased datasets, and set retention, security and onward-disclosure policies. Data obtained through unauthorised access or by circumventing restrictions raises separate legal issues. — [India Briefing](https://www.india-briefing.com/news/india-dpdp-act-publicly-available-personal-data-46899.html/)
- The Act does not expressly say that aggregation, enrichment, profiling or commercialisation takes data out of the exclusion, but commentators warn this is unsettled. One notes official interpretation "insists on compliance" despite the statutory text, and says the 2025 Rules do little to clarify Section 3(c)(ii). — [India Briefing](https://www.india-briefing.com/news/india-dpdp-act-publicly-available-personal-data-46899.html/); [Law School Policy Review, Jan 2026](https://lawschoolpolicyreview.com/2026/01/13/publicly-available-data-under-the-dpdp-act-the-limits-of-exemptions-in-ai-driven-processing/); [law.asia](https://law.asia/publicly-available-data-dpdpa/)
- No court ruling interpreting Section 3(c)(ii) was found. — [search of commentary incl. IAPP](https://iapp.org/news/a/scraping-public-data-in-india-innovation-enabler-or-privacy-threat-)
- DPDP Rules 2025 were notified in November 2025 with a staggered rollout. Some rules apply immediately, Rule 4 (consent managers) after one year (Nov 2026), and the main obligations (Rules 3, 5-16, 22, 23: notice, security, breach, retention/erasure, etc.) after 18 months. — [Storyboard18](https://www.storyboard18.com/amp/digital/breaking-govt-notifies-final-dpdp-rules-sets-staggered-rollout-with-key-obligations-for-data-fiduciaries-84201.htm); [PIB backgrounder (Nov 2025)](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf)
- **Date conflict:** India Briefing gives 13 November 2025 as the notification date, with principal provisions from 13 May 2027. Other sources give 14 November 2025 and 14 May 2027. — [India Briefing](https://www.india-briefing.com/news/india-dpdp-act-publicly-available-personal-data-46899.html/); [Storyboard18](https://www.storyboard18.com/amp/digital/breaking-govt-notifies-final-dpdp-rules-sets-staggered-rollout-with-key-obligations-for-data-fiduciaries-84201.htm)
- The IT Act SPDI Rules 2011 stay in force during the transition. — [Mondaq](https://www.mondaq.com/india/privacy-protection/1708830/dpdp-act-compliance-mandate)
- The Rules set specific retention/erasure timelines only for certain classes (e-commerce, online gaming, social media intermediaries), and sources disagree on the inactivity period. — [Mondaq](https://www.mondaq.com/india/privacy-protection/1708830/dpdp-act-compliance-mandate); [AMLegals](https://amlegals.com/digital-personal-data-protection-rules-2025/); [India Briefing Rules note](https://www.india-briefing.com/news/dpdp-rules-2025-india-data-protection-law-compliance-40769.html)

### Inferences
- Lowest-risk data model: store **institution-level** records (school name, affiliation no., official school email/phone/website, plus the principal's name and role as published), each with a source URL and capture date as provenance. Avoid personal mobiles, personal email addresses, and data from purchased lists of unclear origin.
- If the exclusion does not apply (e.g., a contact from a trade-show card, a non-mandated web page, or a purchased list), CodeSchool would be a Data Fiduciary. From May 2027 it would likely need: a lawful basis (consent or a "legitimate use"; there is no general "legitimate interests" ground in the DPDP Act), a notice, reasonable security safeguards, a way to handle access/correction/erasure requests, erasure once the purpose ends, and breach notification. Build these in now, because the CRM built for the April 2027 launch will be in use when they take effect.
- Practical retention rule: purge or anonymise non-responding prospect contacts after a defined period (e.g., 12-24 months after last interaction), and on any opt-out keep only a suppression entry. This is a suggested policy, not a legal requirement found in sources.

### Gaps (flag for lawyer)
- Does a principal's official contact in an Appendix IX disclosure meet the "legal obligation" limb, given the obligation sits with the school and its purpose is parent transparency, not vendor marketing?
- Does reusing public data for unrelated commercial outreach fall outside the exclusion (purpose limitation)?
- The DPDP penalty ceiling (commonly reported as up to Rs 250 crore per breach) was not verified from the statute in this session.
- Whether the final Rules impose a general minimum log-retention period on all Data Fiduciaries (reported in some commentary) was not verified.

## 5. TRAI TCCCPR 2018 and 2025 amendments: calls and SMS

### Takeaway
All commercial calls/SMS on Indian telecom networks must come from a principal entity registered on the telcos' DLT platform, using registered headers/templates. Promotional voice calls must use the **140** series and service/transactional calls the **1600** series. Telemarketing from ordinary 10-digit numbers is banned. Unregistered senders face a 15-day bar on first violation and 1-year disconnection plus blacklisting on repeat. Whether B2B calls (e.g., to schools) are covered is being litigated by IndiaMART in the Delhi High Court (notice issued Dec 2025). Until that is resolved, assume TCCCPR applies.

### Cited Findings
- Feb 2025 amendment: promotional calls on the 140 series, transactional/service calls on the new 1600 series. Telemarketing from 10-digit numbers is banned. — [TRAI PR No. 11/2025](https://cms.trai.gov.in/sites/default/files/2025-02/PR_No.11of2025.pdf) (primary, fetch failed); [FoneArena summary](https://fonearena.com/blog/?p=446114); [India TV](https://www.indiatvnews.com/technology/news/trai-new-rules-promotional-calls-sms-to-have-standardised-identifiers-fines-increased-for-violations-2025-02-17-976560)
- Complaints against unregistered senders no longer need the complainant to have registered a DND preference. The complaint window is now 7 days (was 3). The action threshold is 5 complaints in 10 days (was 10 in 7). Telcos must act within 5 days (was 30). — [FoneArena](https://fonearena.com/blog/?p=446114)
- Sender penalties: first violation bars outgoing services on all the sender's telecom resources for 15 days. Repeat violations bring "complete disconnection for one year" and blacklisting across all access providers. — [FoneArena](https://fonearena.com/blog/?p=446114)
- Access providers face financial disincentives of Rs 2 lakh / 5 lakh / 10 lakh for failing to curb UCC. They may take security deposits from senders and must sign binding agreements with registered senders/telemarketers. — [FoneArena](https://fonearena.com/blog/?p=446114)
- Promotional messages must carry a mandatory opt-out. After an opt-out, consent cannot be re-sought for 90 days. Headers carry suffixes -P (promotional), -S (service), -T (transactional), -G (government). — [FoneArena](https://fonearena.com/blog/?p=446114)
- Effective dates: the amendment applies 30 days after Gazette publication, with some regulations (8, 17, 20(a)-(b), 21(b)) after 60 days. — [FoneArena](https://fonearena.com/blog/?p=446114)
- Any business wishing to send commercial communication must register as a principal entity with a telecom service provider on the DLT platform. — [TRAI consultation paper CP 28.08.2024](https://trai.gov.in/sites/default/files/CP_28082024.pdf); [Sinch DLT explainer](https://community.sinch.com/t5/SMS-365-enterprise-service/India-Distributed-Ledger-Technology-DLT-Registration/ta-p/5361)
- TRAI has flagged promotional calls from 10-digit mobile **or landline** numbers using auto-dialers/robo-calls as a way of evading the rules. — [S.S. Rana](https://ssrana.in/?p=43797)
- Vendor explainers say the principal entity is vicariously liable for calls made by its outsourced telemarketers. This is a secondary source. — [FreJun](https://frejun.com/tcccpr-2025-consent-rules-140-series-campaigns/)
- IndiaMART challenges Regulation 25 of TCCCPR as applied to B2B communications. The Delhi HC issued notice to TRAI/DoT on 23 Dec 2025, impleaded COAI, and listed the matter for March 2026. No outcome was found. An earlier 2021 IndiaMART plea was denied interim relief. — [Bar & Bench](https://www.barandbench.com/news/delhi-high-court-seeks-centres-response-to-indiamarts-plea-against-spam-call-and-message-regulations); [Informist](https://informistmedia.com/MoneyWire/41357/hc-notice-to-trai-on-indiamart-plea-over-curbs-on-b2b-calls-to-regulate-spam); [Business Standard 2021](https://business-standard.com/article/companies/hc-refuses-firm-relief-in-plea-against-curbs-on-unsolicited-messages-121031501162_1.html)
- Base regulation text: TCCCPR 2018. — [TCCCPR 2018 (BSNL copy)](https://bsnl.co.in:443/opencms/export/finresult/TCCCPR_2018.pdf)

### Inferences
- For any **scaled or scripted** calling or SMS (call centre, auto-dialer, bulk SMS), CodeSchool should register as a principal entity on DLT, register headers and templates, and use 140-series numbers for promotional calls. Individual relationship calls by a salesperson's mobile to a school office (one-to-one, follow-ups after an enquiry) are a grey zone. Repeated complaints could still get that number barred, so keep cold calling low-volume and use registered infrastructure when in doubt.
- School landlines are subscriber numbers too. TCCCPR is framed around the telecom resource, not whether the recipient is a business, so it likely covers them. The pending IndiaMART case confirms B2B is not currently exempt.
- Post-enquiry follow-ups (the school asked for information) carry lower risk. Keep a record of the enquiry as consent evidence.

### Gaps (flag for lawyer)
- Whether the March 2026 hearing in IndiaMART v. TRAI produced any order.
- The exact wording of the "commercial communication" definition and of the B2B position in the regulation text (primary TRAI PDFs could not be fetched).
- Whether any 2025-2026 TRAI follow-up (e.g., on AI/robo-calls) has been finalised.

## 6. Commercial email in India

### Takeaway
India has **no standalone anti-spam/CAN-SPAM-style law**. Section 66A of the IT Act, which once covered offensive messages, was struck down, and TCCCPR covers telecom, not email. Email outreach is governed indirectly by the DPDP Act (personal data in addresses), consumer-protection law (misleading content), and the IT Act on fraud and phishing. Best practice is CAN-SPAM-style hygiene.

### Cited Findings
- India has no standalone anti-spam law, and the IT Act has no provision regulating "spamming" as such. — [iPleaders](https://blog.ipleaders.in/overview-laws-spamming-india/); [CIS India](https://cis-india.org/internet-governance/blog/anti-spam-laws-in-different-jurisdictions)
- Section 66A once covered such messages but was struck down by the Supreme Court. Spam is now pursued mainly through nuisance/tort or penal provisions. — [Governance Now](https://www.governancenow.com/gov-next/egov/spam-mail-can-land-you-jail); [iPleaders](https://blog.ipleaders.in/overview-laws-spamming-india/)
- The proposed Digital India Act was expected to address unsolicited commercial communications, but as of a 2023 client alert it had not been introduced. — [TTA client alert, Aug 2023](https://tta.in/annual-maintenance-email-marketing-india/); [S.S. Rana](https://ssrana.in/articles/government-to-deal-with-the-issue-of-scam-calls-in-the-digital-india-bill/)
- Misleading emails may fall under the Consumer Protection Act 2019, and the DPDP Act may matter for emails sent without a lawful basis. — [advocategandhi.com](https://advocategandhi.com/spam-emails-legal-challenges-cybersecurity-risks-and-regulatory-frameworks/)
- The Delhi High Court has issued an injunction restraining a party from sending unsolicited bulk email to ISP users, an early judicial order on spam. — [iPleaders](https://blog.ipleaders.in/laws-related-telemarketing-india/)

### Inferences
- Best practice: send from a real company domain with SPF/DKIM/DMARC set up; name the company, sender and postal address; write to official school addresses only; send a short, relevant first email with an easy one-click opt-out and honour it permanently through a suppression list; do not buy or scrape lists of personal addresses; cap volumes; and avoid misleading subject lines (e.g., implying CBSE endorsement). Gmail/Yahoo bulk-sender rules (authentication, one-click unsubscribe, low spam-complaint rates) also apply because many schools use Google Workspace. This is general industry knowledge, not verified this session.

### Gaps
- No current (2025-2026) confirmation was found of whether a Digital India Act draft with anti-spam provisions has been tabled.

## 7. WhatsApp Business policy

### Takeaway
WhatsApp requires **opt-in before any business-initiated message**. Messages outside the 24-hour customer-service window must use pre-approved templates, and stop requests must be honoured. Negative user feedback (blocks/reports) triggers messaging limits and can lead to a permanent ban covering the whole organisation. Cold WhatsApp outreach to school numbers taken from websites is not permitted.

### Cited Findings
- Businesses may contact people only if they have the person's number and "opt-in permission from the recipient confirming that they wish to receive subsequent messages". The business is "solely responsible" for its opt-in method and legal compliance. — [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/)
- Business-initiated conversations need approved templates, used only for their designated purpose. Free-form replies are allowed only inside the 24-hour customer-service window. WhatsApp can pause or reject templates at any time. — [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/)
- Businesses must honour requests to block, discontinue or opt out, whether made on or off WhatsApp, including removing the person from contact lists. Businesses must not "confuse, deceive, defraud, mislead, spam, or surprise people", and messaging "at scale in an unauthorized manner" is a violation. — [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/)
- WhatsApp may limit messaging based on user feedback, and may limit or remove access. Termination can bar the business and its organisation from all future use of WhatsApp products. — [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/)

### Inferences
- Use WhatsApp only after an opt-in captured on CodeSchool's own channels, for example a website or webinar form with a WhatsApp checkbox that names CodeSchool, or a school replying "yes, WhatsApp me". Keep a record of each opt-in. Do not mass-add numbers taken from disclosures.
- The policy text found does not explicitly mention purchased lists, but unconsented messaging at scale is prohibited outright.

### Gaps
- Whether an opt-in must name the specific business was not stated in the policy page as fetched (WhatsApp's Help Center opt-in guidance was not checked).

## 8. Practical etiquette for approaching schools

### Takeaway
I found no authoritative written source on sales etiquette towards Indian schools in this session, so the points below are inferences only. They match common practice in the Indian K-12 market: formal letter or email on letterhead, a request for an appointment with the principal or coordinator, specimen copies and demos, and no inducements.

### Cited Findings
- No sourced findings in this session.

### Inferences
- Approach the school's official email or office first with a formal introduction on company letterhead (PDF), naming CBSE-curriculum alignment factually without implying CBSE endorsement. Request an appointment with the principal or academic coordinator, and follow up by phone with the school office only to schedule.
- Timing: avoid exam and result periods and the admission rush. The academic year starts in April, so decisions for an April 2027 launch are typically made between roughly November and February. Verify this against primary-market research.
- Specimen and teacher copies plus a demo session are standard. Keep specimen supply modest and documented so it does not look like an inducement. Commission or kickback rules (CBSE affiliation bye-laws on commercial activity; government servant conduct rules for KVS/NVS staff) are covered elsewhere and are only noted here.
- For KVS/NVS/state government schools, go through headquarters or regional offices and public procurement routes rather than school-by-school sales.

### Gaps
- No primary or authoritative source was found on appointment norms or on the specimen-copy practice. Interviews with publishers' sales teams or school principals would close this gap.
