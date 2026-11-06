# India child-data law for a school-sold edtech product (DPDP Act 2023 + DPDP Rules 2025), status as of 6 Nov 2026

Scope note: research notes, not legal advice. Sources are a mix of primary text mirrors (dpdpa.com reproductions of the Act and Rules), law-firm/advocate commentary (Juris Eagle, S.S. Rana, LiveLaw, Khaitan), trade press (MediaNama, SCC Online) and some compliance-vendor blogs (flagged where used). The official MeitY PDF of the Rules (meity.gov.in) and PIB returned HTTP 403 to automated fetch, so Rule text below comes from mirrors and commentary; the Gazette text (G.S.R. 846(E)) should be checked before relying on exact wording or rule numbers.

## 1. DPDP Act 2023: child definition, Section 9 duties, roles, core duties, penalties

### Takeaway
A "child" is anyone under 18. Section 9 needs verifiable consent from a parent or lawful guardian before any processing of a child's data. It also bars processing likely to harm a child's well-being and bans tracking, behavioural monitoring and targeted advertising directed at children; only the Rules' Fourth Schedule can lift the consent and tracking duties. The Section 9 obligations are NOT yet in force as of Nov 2026. They start 13 May 2027 (some trackers say 14 May 2027). Breaching them can cost up to Rs 200 crore.

### Cited Findings
- "Child" means an individual who has not completed the age of eighteen years. — [dpdpa.com, Section 9 page quoting Section 2](https://www.dpdpa.com/dpdpa2023/chapter-2/section9.html) (the page labels this clause 2(k). In the official Act it is generally cited as Section 2(f), so check the numbering against the Gazette).
- Section 9(1) says a Data Fiduciary must obtain verifiable consent of the parent (or lawful guardian, for a person with disability) before processing a child's personal data, in the manner prescribed. Section 9(2) bans processing "likely to cause any detrimental effect on the well-being of a child". Section 9(3) bans "tracking or behavioural monitoring of children or targeted advertising directed at children". Section 9(4) lets the Government exempt prescribed classes of fiduciaries or purposes from 9(1) and 9(3), subject to conditions. Section 9(5) lets the Government notify a lower age threshold for a fiduciary whose processing is "verifiably safe". — [dpdpa.com Section 9](https://www.dpdpa.com/dpdpa2023/chapter-2/section9.html)
- Section 9(2), the detrimental-effect bar, has no exemption: "Neither section 9(4) nor rule 12 lifts it." — [Juris Eagle, Harsha Swaroop P, 20 Nov 2025, reviewed 24 Oct 2026](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- Roles: a school that processes student data itself is the data fiduciary. If it engages a platform to process data on its behalf, the platform is a data processor and the institution stays responsible under Section 8(1). An edtech that deals with families directly is a data fiduciary in its own right. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- Section 8(2): a fiduciary may engage a processor only under "a valid contract". The Act does not prescribe what the contract must contain. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- A B2B platform acting solely as processor for an institution does not itself carry the parental-consent obligation, which sits with the institution as fiduciary. B2C platforms cannot rely on the school exemption. — [LiveLaw, Siddharth Shrivastava, 20 Oct 2026](https://www.livelaw.in/articles/dpdp-child-data-rules-demand-edtech-platforms-555317)
- Penalty Schedule (Section 33) maxima per contravention:
  - Failure of security safeguards (Section 8(5)): up to Rs 250 crore.
  - Failure to notify a breach (Section 8(6)): up to Rs 200 crore.
  - Breach of children's-data obligations (Section 9): up to Rs 200 crore.
  - Breach of Significant Data Fiduciary (SDF) obligations (Section 10): up to Rs 150 crore.

  The Board fixes the actual amount after inquiry, using the Section 33(2) factors. — [amlegals](https://amlegals.com/penalties-under-the-digital-personal-data-protection-act2023/); [dpdpa.com Schedule](https://dpdpa.com/theschedule.html) (one dpdpa.com page lists Section 8(5) as Rs 200 crore, but most sources say Rs 250 crore)
- Removal of Difficulties Order 2026 (S.O. 5458(E), dated 5 Oct 2026, gazetted 6 or 7 Oct 2026 depending on source) makes two wording fixes. It inserts "of" in Section 9(1), so the provision reads "personal data of a child or of a person with disability". It changes "periodic audit" to "periodic data audit" in Section 10(2)(c)(ii). It is clarificatory, with no new duties or deadlines. — [S.S. Rana](https://ssrana.in/articles/dpdp-removal-of-difficulties-order-2026-what-has-been-changed-for-childrens-data-and-sdf-audits/); [SCC Online, 15 Oct 2026](https://www.scconline.com/blog/post/2026/10/15/dpdp-removal-of-difficulties-order-2026/); [India Briefing](https://www.india-briefing.com/news/dpdp-removal-of-difficulties-order-2026-consent-data-audit-47274.html); [Conventus Law](https://conventuslaw.com/report/india-meity-clarifies-consent-and-audit-requirements-under-the-dpdp-act-through-the-removal-of-difficulties-order-2026/)
- Penalties, like the core obligations, take effect from May 2027. The Data Protection Board and its institutional provisions are already in force. — [S.S. Rana](https://ssrana.in/articles/dpdp-removal-of-difficulties-order-2026-what-has-been-changed-for-childrens-data-and-sdf-audits/)

### Inferences
- CodeSchool's classes are about ages 6 to 14, so every learner is a "child". There is no teen gray zone, and the full Section 9 regime applies to all student data.
- If CodeSchool processes data only on the school's documented instructions, it is most defensibly a processor. Once it uses student or parent data for its own purposes, it is likely acting as a fiduciary for that processing, with its own Section 9 consent and tracking-ban exposure. Its own purposes include product analytics across schools, AI model training, marketing to parents, and running the parent app on its own terms.
- The parent view is the riskiest part of the role analysis. If parents sign up directly with CodeSchool, CodeSchool has a direct relationship with families. The Juris Eagle and LiveLaw analysis treats that as fiduciary territory.

### Gaps
- I did not retrieve primary Act text for Sections 5 (notice), 6 (consent), 7 (legitimate uses), 8(6)-(8) (breach, erasure, grievance) or 10 (SDF). Their substance is well known but uncited here, so check them against the Act PDF.
- I found no source confirming whether Data Protection Board members have been appointed and the Board is operating as of Nov 2026.

## 2. DPDP Rules 2025: notification, phased commencement, verifiable parental consent, Fourth Schedule, SDF, transfers, consent managers

### Takeaway
The Rules were notified as G.S.R. 846(E) on 13 Nov 2025 (some sources say 14 Nov). They commence in three phases:
- **13 Nov 2025:** Board and institutional provisions.
- **About 13/14 Nov 2026:** the Consent Manager framework. This is days away and not yet live on 6 Nov 2026.
- **About 13/14 May 2027:** everything substantive, including notice, security, breach, retention, children's data, transfers and rights.

Rule 10 lets parental consent be verified against reliable identity and age details the fiduciary already holds, or via a virtual token from an authorised entity such as DigiLocker. The Fourth Schedule exempts educational institutions from 9(1) and 9(3) only for tracking and behavioural monitoring for educational activities or child safety. It does not expressly cover edtech vendors. A January 2026 proposal to shorten the timeline to 12 months had not been notified as of Oct 2026.

### Cited Findings
- Notification: G.S.R. 846(E) dated 13 Nov 2025. Act commencement notification G.S.R. 843(E) was published the same day. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions). Wikipedia gives 14 Nov 2025 — [Wikipedia](https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Rules,_2025); [EY summary](https://www.ey.com/en_in/insights/cybersecurity/transforming-data-privacy-digital-personal-data-protection-rules-2025)
- Phasing: Rule 1(2) sets three phases: on publication, after one year, and after eighteen months. — [search summary of DPDP trackers incl. dcomply](https://dpdpa.dcomply.in/rules/). The tracker dates are:
  - **13 Nov 2025:** Rules 1-2 and the Board, appeals and TDSAT rules.
  - **14 Nov 2026:** Consent Manager registration (Rule 4).
  - **14 May 2027:** notice, security, breach, retention, children, SDF, rights and cross-border.

  — [dcomply DPDP Rules table](https://dpdpa.dcomply.in/rules/). Other sources give 13 May 2027 for the final phase. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions); [S.S. Rana](https://ssrana.in/articles/dpdp-removal-of-difficulties-order-2026-what-has-been-changed-for-childrens-data-and-sdf-audits/). Note: the dcomply rule-number labels (e.g. "Rule 12 = SDF") appear to mix draft and final numbering, so use it for dates only.
- Timeline-compression proposal: in Jan 2026 MeitY reportedly considered cutting 18 months to 12, mainly for SDFs. — [Business Standard, 22 Jan 2026](https://www.business-standard.com/technology/tech-news/meity-may-cut-compliance-timeline-for-key-dpdp-rules-to-12-months-126012201293_1.html); [Legal500/S.S. Rana](https://www.legal500.com/intelligence/india/privacy/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs). Trackers report it NOT notified as of Sept/Oct 2026. — [dpdprules.org](https://dpdprules.org/blog/dpdp-18-months-to-12-months-proposal); [pyroniq](https://www.pyroniq.ai/resources/dpdpa-compliance-timeline) (vendor sources). The Oct 2026 Removal of Difficulties Order changed no timeline. — [S.S. Rana](https://ssrana.in/articles/dpdp-removal-of-difficulties-order-2026-what-has-been-changed-for-childrens-data-and-sdf-audits/)
- Rule 10 (verifiable consent for a child), per the dpdpa.com reproduction:
  - **10(1):** the fiduciary must adopt appropriate technical and organisational measures so a parent's verifiable consent is obtained before processing. It must use due diligence to check that the person identifying as parent is an identifiable adult. The check may use (a) reliable identity and age details already available with the fiduciary, or (b) details voluntarily provided by the individual, or through a virtual token mapped to those details and issued by an authorised entity.
  - **10(2):** "Adult" means 18 or over. "Authorised entity" means an entity entrusted by law or by the Central or a State Government with issuing identity and age details or a token, or a person it appoints. It includes details or tokens made available and verified by a Digital Locker Service Provider.
  - **Illustrations (four cases):** the parent is either already a registered user with reliable details (check own records) or not registered (check via authorised entity or DigiLocker token).

  — [dpdpa.com Rule 10](https://dpdpa.com/dpdparules/rule10.html)
- The final Rules tightened "authorised entity" from entities that "maintain" identity and age details to entities "entrusted with issuing" them, and expressly include Digital Locker. — [DSCI FAQ on Children and PwD data, as summarised in search](https://www.dsci.in/files/content/documents/2025/FAQs-on-Children-and-PwD-personal-data.pdf) (the PDF text could not be extracted, so this is a search-snippet characterisation)
- A school that already holds reliable parent identity and age details from admission can verify against its own records. A platform meeting a parent for the first time would need authorised-entity details or a DigiLocker token. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- Practical guidance from one advocate:
  - Don't rely on student-led OTP sign-up.
  - Use DigiLocker-style tokens, and offer assisted or video verification for parents without DigiLocker.
  - Avoid retaining parent ID documents.
  - Separate children's data from analytics and ML pipelines.

  — [LiveLaw, 20 Oct 2026](https://www.livelaw.in/articles/dpdp-child-data-rules-demand-edtech-platforms-555317)
- Fourth Schedule Part A (classes of fiduciaries for whom 9(1) and 9(3) do not apply):
  - **Item 3:** "A Data Fiduciary who is an educational institution", limited to tracking and behavioural monitoring for the institution's educational activities or for the safety of enrolled children.
  - **Item 4:** crèche or child day-care carers, limited to safety.
  - **Item 5:** a fiduciary "engaged by an educational institution, crèche or child care centre for transport of children", limited to location tracking during travel.

  The Note defines "educational institution" as "an institution of learning that imparts education, including vocational education". — [dpdpa.com Fourth Schedule](https://www.dpdpa.com/schedule/schedule4.html)
- Fourth Schedule Part B (purposes):
  1. Purposes in a child's interests under Indian law.
  2. Subsidies, benefits and services under Section 7(b).
  3. Creating a user account limited to email communication.
  4. Ensuring information likely to harm a child's well-being is not accessible to the child.
  5. Confirming a user is not a child, or doing Rule 10 due diligence.

  Each is limited to what is necessary. — [dpdpa.com Fourth Schedule](https://www.dpdpa.com/schedule/schedule4.html)
- Whether the school exemption covers a vendor or processor acting for the school is unsettled. On one reading, Section 9 binds only the fiduciary, so the processor needs no exemption. On the other, expressly naming transport providers in item 5 implies other vendors are excluded. "The text does not settle it." — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- Several commentators say commercial edtech platforms, test-prep apps, tutoring marketplaces and LMS vendors do not qualify as an "educational institution" on a settled reading. — [search summaries of codesnag / qodequay / dpdpactindia guides](https://www.qodequay.com/dpdpa-childrens-data-schools-edtech) (vendor blogs, so lower weight). MediaNama commentators note "education" is vague: does it cover only schools, or edtech too? — [MediaNama, 17 Nov 2025](https://www.medianama.com/2025/11/223-dpdp-rules-tracking-children-parental-consent/)
- No Fourth Schedule condition permits targeted advertising by any fiduciary. Admission, fee and exam records fall outside item 3 on an ordinary reading, so parental consent is needed. Learning analytics is unsettled: it could be "monitoring for educational activities" or ordinary processing needing consent. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- MediaNama critiques: the exemptions allow real-time location tracking of children for "safety" without parental consent, and "real-time location" is undefined (GPS, cell tower, IP). Child-rights advocate Chitra Iyer argues live tracking is not normal safety practice internationally. Advocate Samar Bansal argues exemptions should be strictly construed. — [MediaNama](https://www.medianama.com/2025/11/223-dpdp-rules-tracking-children-parental-consent/)
- Rule numbering conflict: commentary cites the exemption rule as Rule 12 (final numbering). The dpdpa.com headings show Rule 10 as covering "child or person with disability" and Rule 11 as exemptions, which looks like draft numbering. Final numbering appears to be:
  - Rule 10: child consent
  - Rule 11: persons with disability
  - Rule 12: exemptions
  - Rule 13: SDF
  - Rule 15: cross-border

  — [dpdpa.com Fourth Schedule page headings](https://www.dpdpa.com/schedule/schedule4.html) vs [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions) and [cross-border search summaries](https://ksandk.com/data-protection-and-data-privacy/cross-border-data-transfers-dpdp-act-india/). Verify against the Gazette.
- Breach (Rule 7): notify affected Data Principals and the Board without delay, then send the Board a detailed report within 72 hours of becoming aware, or longer if the Board allows on written request. Applies from May 2027. — [MediaNama breach explainer](https://www.medianama.com/2025/11/223-data-breach-reporting-timeline-of-dpdp-rules-2025-explained/); [Baker Botts](https://ourtake.bakerbotts.com/post/102lund/india-notifies-final-rules-for-digital-data-protection-act)
- Security and log retention: the Rules require logs and related personal data to be kept for at least one year unless law requires longer. Third Schedule erasure timelines (inactivity-based, with 48-hour pre-erasure notice) target large e-commerce, social media and online gaming intermediaries, not a school edtech. — [search summaries of final-Rules explainers: Baker Botts](https://ourtake.bakerbotts.com/post/102lund/india-notifies-final-rules-for-digital-data-protection-act), [Seqrite](https://www.seqrite.com/blog/dpdp-rules-are-here-what-changed-from-the-draft/) (verify exact Rule 6/8 wording)
- Cross-border (Section 16, operationalised in the Rules): India uses a negative-list model. No restricted-country list had been notified as of Sept 2026. Sectoral rules that are stricter prevail under Section 16(2). SDFs may face extra restrictions. — [KS&K](https://ksandk.com/data-protection-and-data-privacy/cross-border-data-transfers-dpdp-act-india/); [Bar & Bench column](https://www.barandbench.com/columns/the-dpdp-cross-border-transfer-rules-arent-live-yet-so-why-are-contracts-being-redrafted-as-if-they-are)
- SDFs need an India-resident DPO, an annual DPIA and an audit, plus algorithmic due diligence. Possible localisation applies to data classes the Government specifies. — [dcomply summary](https://dpdpa.dcomply.in/rules/). The Jan 2026 reports also mentioned notifying cross-border restrictions for SDFs. — [Legal500](https://www.legal500.com/intelligence/india/privacy/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs)
- Consent Managers: the Rules set registration and conduct standards, commencing about 14 Nov 2026. — [dcomply](https://dpdpa.dcomply.in/rules/); [Legal500 Rules summary](https://www.legal500.com/intelligence/india/privacy/digital-personal-data-protection-rules-2025-%E2%80%93-notified)

### Inferences
- In force on 6 Nov 2026: the Act's definitional and Board provisions, plus Rules 1-2 and the Board rules. Nothing that binds CodeSchool's product design is yet enforceable under DPDP. A pilot in the 2026-27 school year will still straddle 13/14 May 2027, so design it to the final standard now, especially since consent collected before May 2027 may not meet Rule 10 (Juris Eagle flags this).
- The safest exemption reading for CodeSchool: the school (an "institution of learning") holds the item 3 exemption. CodeSchool, as a pure processor, may do progress tracking only within the school's educational-activities purpose. Even then, rely on the school also obtaining verifiable parental consent, because a school pilot typically involves records outside item 3 (names, class, login accounts).
- The school's existing admission records (parent name, phone, ID) are the easiest Rule 10 route ("reliable details already available"). A DigiLocker-token flow is the route if CodeSchool runs a parent app directly.
- CodeSchool is very unlikely to be designated an SDF at pilot scale. SDF status is notified by the Government on volume and sensitivity factors, but children's data is a stated sensitivity factor, so watch this as the company scales.

### Gaps
- Exact Gazette wording for Rules 6, 7 and 8 (including whether the one-year log retention is in Rule 6 or Rule 8, and the Seventh Schedule purposes), plus Consent Manager eligibility (net worth figure not confirmed).
- No official MeitY FAQ on children's data was retrieved. The DSCI FAQ PDF could not be parsed.
- Exact final-phase day (13 vs 14 May 2027) is not resolved from primary text.

## 3. School as fiduciary, edtech as processor: contracts, and whether the education exemption covers the vendor

### Takeaway
The prevailing view is that the school is the fiduciary and an edtech processing on its behalf is a processor bound by a Section 8(2) contract. The school stays accountable under Section 8(1). Whether the Fourth Schedule item 3 exemption "flows down" to the vendor is expressly unsettled. Any processing the vendor does for its own purposes makes it a fiduciary, with no school exemption to lean on.

### Cited Findings
- School = fiduciary, platform engaged on its behalf = processor, institution remains responsible under Section 8(1). A platform dealing with families directly = fiduciary. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- A processor needs "a valid contract" (Section 8(2)). The Act and Rules do not list mandatory clauses. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- B2B processor: the consent obligation shifts to the institution. B2C: full obligations, no exemption. — [LiveLaw](https://www.livelaw.in/articles/dpdp-child-data-rules-demand-edtech-platforms-555317)
- Outside the exemption: marketing to parents via vendors, profiling students with third-party analytics, and using student photos in promotions. — [search summary of school-compliance guides](https://www.qodequay.com/dpdpa-childrens-data-schools-edtech); [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- Data collected for educational objectives cannot be repurposed for behavioural analytics, marketing optimisation or commercial analytics without fresh consent or an applicable exemption. — [Tsaaro blog (search summary)](https://tsaaro.com/blogs/teaching-in-the-age-of-dpdpa-when-child-safety-becomes-edtech%E2%80%99s-competitive-advantage)

### Inferences
- Expected processor-contract (DPA) clauses, drawn from Act duties rather than a prescribed list:
  - Process only on the school's documented instructions and for named purposes.
  - No secondary use: no ads, no profiling beyond the agreed learning features, no model training on identifiable data without the school's and parents' consent.
  - Security safeguards matching the Rules (encryption, access control, one-year logs).
  - Breach notice to the school fast enough for its "without delay" and 72-hour Board duties, and for CERT-In's 6 hours.
  - Sub-processor (cloud and AI API) approval and flow-down.
  - Help the school respond to Data Principal (parent) requests.
  - Erasure or return at end of term or contract, with certification.
  - Data location and transfer terms.
  - Audit rights.
  - Indemnity and liability caps sized against Rs 200-250 crore exposure.
- If CodeSchool wants aggregated cross-school analytics, use properly anonymised data and state it in the contract. Whether anonymised data falls outside "personal data" in practice is a lawyer question.

### Gaps
- No official MeitY or Board guidance on processor contracts or on the vendor/exemption question was found.
- No law-firm template DPA for the Indian school context was retrieved.

## 4. Related guidance: PRAGYATA, NCPCR, CBSE, IT Act/CERT-In, NEP/NDEAR, consumer protection, IEC code

### Takeaway
Outside DPDP, the binding obligations most relevant to CodeSchool are the IT Act framework, chiefly the CERT-In 2022 directions (6-hour incident reporting, 180-day logs), and consumer-protection advertising rules. Several other items are soft guidance rather than binding data law:
- PRAGYATA (MoE, July 2020): screen-time norms.
- NCPCR cyber-safety and anti-bullying guidance.
- The IAMAI India EdTech Consortium code (2022), self-regulatory and focused on mis-selling and grievances.

### Cited Findings
- PRAGYATA: Guidelines on Digital Education, released July 2020 by MoE (Dept of School Education). — [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1638541&reg=48&lang=2). Screen-time guidance, as usually summarised:
  - Pre-primary: at most about 30 minutes.
  - Classes 1-8: up to two sessions of 30-45 minutes.
  - Classes 9-12: up to four sessions.

  It also covers cyber safety and posture. — [Drishti IAS summary](https://www.drishtiias.com/daily-updates/daily-news-analysis/pragyata-guidelines-on-digital-education); [PRAGYATA PDF copy](https://cdn1.byjus.com/wp-content/uploads/2021/03/PRAGYATA_-Guidelines-on-Digital-Education.pdf) (summaries conflict on exact minutes, so check the official PDF)
- NCPCR documents:
  - Guidelines on cyber safety (draft, for the school safety manual).
  - "Being Safe Online" (2017).
  - Anti-bullying and cyberbullying guidance for schools (2023/2024).

  — [NCPCR guidelines page](https://ncpcr.gov.in/public/guidelines); [NCPCR draft cyber-safety guidelines PDF](https://ncpcr.gov.in/public/viewPdf/16613369326305fd6444e1b_cyber-safety-guidline.pdf); [KS&K on anti-bullying draft](https://ksandk.com/newsletter/ncpcr-proposes-anti-bullying-guidelines/). NCPCR reportedly plans guidelines for social media, gaming and AI platforms, including age assurance. These are a proposal, not issued. — [ThePrint](https://theprint.in/tech/ncpcr-summons-google-over-ai-kiss-hug-apps-to-issue-social-media-child-safety-norms-by-december/3071591/)
- IAMAI India EdTech Consortium (IEC), Jan 2022: a self-regulatory code covering no mis-selling, fair marketing and financing, and a two-tier grievance redressal mechanism. Members included Byju's, Unacademy, upGrad, Vedantu and Simplilearn. — [YourStory](https://yourstory.com/2022/01/iamai-india-edtech-consortium-code-of-conduct-edtech-firms); [Business Today](https://www.businesstoday.in/latest/corporate/story/iamai-establishes-consortium-for-edtech-firms-byjus-unacademy-upgrad-join-group-318741-2022-01-12)
- CCPA Guidelines for Prevention of Misleading Advertisement in Coaching Sector, 2024 (13 Nov 2024, under Section 18 of the Consumer Protection Act 2019). They apply to any person providing coaching and to endorsers, read with the 2022 misleading-ads guidelines. IEC/IAMAI were consulted, and CCPA has issued notices and penalties to coaching centres. — [Khaitan & Co](https://khaitanco.com/thought-leadership/Guidelines-for-Preventing-Misleading-Ads-in-Coaching); [MediaNama](https://www.medianama.com/2024/11/223-ccpa-new-guidelines-curb-misleading-ads-coaching-sect/); [TaxGuru reproduction](https://taxguru.in/?p=937913)
- CERT-In Directions dated 28 Apr 2022, effective 27 Jun 2022:
  - Report specified cyber incidents (about 20 categories) within 6 hours of noticing.
  - Keep ICT logs for a rolling 180 days, within India per most readings, or abroad if they can be produced in reasonable time per the CERT-In FAQ.
  - Synchronise clocks to NIC/NPL.
  - Designate a point of contact.

  These apply to any body corporate. — [Ahuva summary](https://www.ahuva.in/resources/cert-in-directions-2022-incident-reporting-log-retention/); [Siri Law](https://sirilawllp.com/a-comprehensive-guide-to-indias-cert-in-6-hour-cyber-incident-reporting-mandate/) (check against cert-in.org.in)

### Inferences
- The CERT-In 6-hour reporting runs in parallel with the DPDP breach duties (from May 2027) and is already in force, so the incident-response plan must cover both.
- The CCPA coaching guidelines and the IEC code mainly constrain marketing claims ("guaranteed results", "rank", testimonials using children). Treat student photos and testimonials as needing separate parental consent under DPDP as well.
- PRAGYATA screen-time norms are relevant to session design (short sessions for grades 1-5) and are a useful selling point to schools, though they are not data law.

### Gaps
- CBSE cyber-safety handbook or circulars: not retrieved.
- NEP 2020 / NDEAR data principles (consent, federated architecture) and APAAR ID student-data consent practice: not retrieved.
- IT Rules 2021 (intermediary due diligence) applicability to a B2B school edtech: not researched.
- Status of the IT Act Section 43A / SPDI Rules 2011 after DPDP (the Act is expected to omit 43A on full commencement): not confirmed with a source.
- No 2025-2026 MoE advisory specific to edtech data was found. Current IEC code activity was also not found.
- Internet Freedom Foundation commentary was not retrieved.

## 5. Practical design implications and what needs a lawyer

### Takeaway
Design for May 2027 now:
- **Data minimisation:** pseudonymous student IDs or roll numbers rather than full names where possible, and no location, device fingerprinting or third-party trackers.
- **Consent:** a school-led verifiable parental consent flow using the school's admission records, or DigiLocker for a direct parent app.
- **No ads, profiling or behavioural analytics** beyond the school-agreed learning purpose.
- **Strict processor contracts and India-friendly hosting.**

AI tutors and adaptive learning are the biggest legal grey zone because of the Section 9(3) bar on behavioural monitoring.

### Cited Findings
- Recommendations from the LiveLaw analysis: redesign onboarding for parental verification, use DigiLocker-style tokens, avoid storing parent IDs, reclassify existing children's data, and keep children's data out of analytics and ML pipelines. — [LiveLaw](https://www.livelaw.in/articles/dpdp-child-data-rules-demand-edtech-platforms-555317)
- Learning analytics may count either as monitoring for educational activities (exempt for the institution) or as ordinary processing that needs consent, which is unsettled. Targeted advertising is never permitted. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- Section 9(2), the detrimental-effect bar, is never exempted. — [Juris Eagle](https://juriseagle.com/insights/dpdp-children-data-educational-institutions)
- Cross-border transfers are currently unrestricted (empty negative list), but this can change by notification. — [KS&K](https://ksandk.com/data-protection-and-data-privacy/cross-border-data-transfers-dpdp-act-india/)
- CERT-In logs: 180 days, India-located per most readings. — [Ahuva](https://www.ahuva.in/resources/cert-in-directions-2022-incident-reporting-log-retention/)

### Inferences (design checklist, not legal advice)
- **Minimum data.** Use a school-issued roll number or pseudonymous ID plus class and section. A first name or display name only if teachers need it. No DOB beyond the grade, no photos, no address, no Aadhaar. Keep the name-to-ID mapping at the school, or in a separate, access-controlled store.
- **Consent.** Have the school issue the DPDP notice and collect parental consent. Rule 10 can be met from admission records, with CodeSchool supplying the notice text and a consent capture (paper or digital) per the school's Hindi/English consent sheet. For the parent view, either route it through the school's identity or verify via a DigiLocker token. Avoid student-created accounts and OTP-only sign-up.
- **Tracking and analytics.** Collect progress data (lessons completed, scores) only as part of the school's educational purpose. Don't use third-party ad or analytics SDKs, cross-school behavioural profiles, engagement nudges or dark patterns. Product telemetry should be aggregate or anonymised.
- **AI features.** Don't train models on identifiable student data. Configure AI API providers for zero retention under the processor contract. Don't profile emotion or behaviour. Make adaptive difficulty explainable and tied to curriculum. Have teachers review AI-generated content and moderate it for child safety, which supports Section 9(2) and the Part B item 4 purpose. Get a lawyer's view before launching any AI tutor that builds a persistent learner model.
- **Retention.** Erase or return data at the end of the academic year or contract, as the school directs. Keep security logs for one year (DPDP Rules) and 180 days (CERT-In), with minimal personal data in logs.
- **Hosting.** An India cloud region is simplest. It keeps CERT-In log location and possible future SDF or negative-list restrictions low-risk. List sub-processors and their regions in the DPA.
- **Security.** Encryption in transit and at rest, role-based access (teacher sees own class, parent sees own child), MFA for staff, and audit logs. Run a breach playbook covering CERT-In 6 hours, notice to the school, and the school's DPDP notices.
- **Timing.** A pilot running into or past May 2027 must already meet these standards. Record consent in a form that meets Rule 10, so it does not need re-collection.

### What still needs a lawyer
- Whether CodeSchool is a processor only, or a fiduciary (independent or joint) for the parent view, product analytics and AI features.
- Whether Fourth Schedule item 3 (educational institution) covers CodeSchool when it acts for the school, and whether adaptive learning or AI tutoring counts as "behavioural monitoring" barred by 9(3) or permitted "educational activities".
- Whether consent collected before May 2027 is valid, and transition arrangements for pilot data.
- Drafting the school DPA (liability caps against Rs 200-250 crore penalties, indemnities, breach timelines, sub-processor and AI provider terms).
- The anonymisation standard for cross-school analytics, and whether a CodeSchool-run parent app needs its own Rule 10 flow.
- Confirming exact Gazette rule numbers and dates (13 vs 14 Nov 2026 and May 2027), and checking for any notification between Oct and Nov 2026.
- Applicability of IT Rules 2021, SPDI Rules transition, consumer-protection advertising rules, and state-specific school procurement or data conditions.

### Gaps
- No primary source was found on AI-specific Indian guidance for children's edtech (e.g., a MeitY AI governance framework applied to education). Not researched within the tool budget.
- No source was found quantifying enforcement or Board actions against edtech to date. Penalties are not yet enforceable.
