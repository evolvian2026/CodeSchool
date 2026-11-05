# School interview plan

**Status:** draft, 5 Nov 2026 · **Owner:** Anoop Dobhal · **Based on:** [Kids coding curriculum and market](reports/Kids%20coding%20curriculum%20and%20market.md)

## Why we are interviewing

The research says the paying customer is a private CBSE or ICSE school that needs to deliver CBSE's new Computational Thinking and AI curriculum (CT&AI) for Classes 3-8 with non-specialist teachers. That conclusion rests on documents, not on conversations with schools. Before any design or code, we need to hear from schools whether it holds.

The deadline is set by the school buying cycle. Book and resource lists for the April 2027 session close around **December 2026 to January 2027**. Interviews should finish by **mid-December 2026** so the findings can shape a pilot offer while schools are still deciding.

## Hypotheses to test

Each interview should produce evidence for or against these. "Kill" means: if most schools say this, rethink the plan.

| # | Hypothesis | Supported if | Kill signal |
|---|---|---|---|
| H1 | CBSE schools are implementing CT&AI for Classes 3-8 in 2026-27 | Most CBSE schools have timetabled it, at least for some classes | Most treat the "advised" circular as optional and have done nothing |
| H2 | Schools struggle to deliver it with the teachers they have | Coordinators name teacher capacity, lesson planning or assessment as the problem | Schools say the free CBSE books are enough |
| H3 | Principals will pay for a product that sits alongside the free CBSE books | They name a budget line and a price range without prompting, or accept one of the price anchors | "We only use free material" from most schools in the target fee tiers |
| H4 | Rs 200-800 per student per year is an acceptable price | Most schools put their ceiling inside or above that range | Ceilings consistently below Rs 200 |
| H5 | Unplugged-first lessons with optional devices fit the schools' real equipment | Device audits show a lab shared across many classes, or a projector only | Every school has 1:1 devices (then unplugged-first matters less) |
| H6 | A maths teacher can run one level in one period with a script and no training | The paper-prototype walkthrough is completed within a period, with only minor questions | Teachers say they can't run it without a CS teacher |
| H7 | Assessment and reporting are a reason to buy | Coordinators want class dashboards and report-card-ready grades | Schools don't assess CT&AI at all |
| H8 | ICSE schools have a similar need for Classes 1-8 | ICSE heads describe a Computer Studies gap or want CT&AI alignment | ICSE schools are happy with their publisher's textbook |

## Who to interview

**Target: 15-20 schools**, with 2-4 people per school. That is 40-60 interviews.

| Dimension | Mix |
|---|---|
| Board | About 12 CBSE, 4-5 ICSE, 1-2 state board (Kerala is the best comparison) |
| Fee tier (annual tuition) | Budget (under about Rs 30,000), mid (Rs 30,000-1,00,000), premium (over Rs 1,00,000), about a third each |
| Location | At least 3 states; a mix of metro, tier 2 and tier 3 cities |
| School type | Mostly standalone private schools; 2-3 that belong to a chain (chains buy centrally) |
| Language | At least 4 schools that teach mainly in Hindi or a regional language |

**Roles at each school:**

| Role | Why | Length |
|---|---|---|
| Principal or owner | Budget, buying decision, price | 30 min |
| CBSE / academic coordinator | How CT&AI is being implemented, timetable, assessment | 30-40 min |
| Class 3-5 maths or EVS (TWAU) teacher | The person who will actually teach CT&AI in Classes 3-5 | 40 min, including the paper prototype |
| Computer teacher (if any) | Devices, labs, Classes 6-8 practice | 30 min |
| Parents (optional, 3-5 per school through the school) | Willingness to pay for home practice, AI vs coding priorities | 15 min |

**Recruiting:** start with personal and alumni networks, then school associations and sahodaya complexes (CBSE school clusters), then LinkedIn outreach to coordinators. Offer a free summary of findings across schools as the reason to take part. Don't offer a discount on a product that doesn't exist yet.

## Ground rules

- **Learn, don't sell.** Don't pitch until the last five minutes, and only if asked.
- **Ask about past behaviour, not hypotheticals.** "What did you buy last year for computer classes?" beats "Would you buy…?"
- **Consent first.** Get verbal consent to take notes and permission before recording. Say that the school won't be named in anything shared.
- **No children.** Don't interview or record students. Classroom observation needs the principal's written permission, and no student names or faces are recorded.
- **Record evidence.** Use a direct quote wherever possible, and note who said it (role, not name).

## Interview guides

### 1. Principal or owner (30 min)

**Context (5 min)**
1. Tell me about the school: board, number of students, Classes covered, fees roughly.
2. Who decides which books and digital products the school buys, and when?

**CT&AI and computing today (10 min)**

3. How are you handling CBSE's Computational Thinking and AI curriculum this year? (ICSE: How do you teach computers in Classes 1-8?)
4. What do you use for computer classes now: a textbook series, a platform, anything else? What does it cost?
5. What's working, and what isn't?

**Buying and budget (10 min)**

6. Walk me through the last time you bought a new academic product. Who was involved, and how long did it take?
7. When do your book and resource lists close for the next session?
8. Is the cost of products like this passed on to parents in fees, or paid from the school budget?
9. **Price anchors:** "Some products like this cost about Rs 200, Rs 500 or Rs 800 per student per year. Which of those would be easy, hard or impossible for your school?" Note the reaction, not just the answer.

**Close (5 min)**

10. If you could fix one thing about how computing or CT&AI is taught here, what would it be?
11. Who else here should I talk to? Would you be open to a free pilot in one or two sections next session?

### 2. CBSE / academic coordinator (30-40 min)

1. Has the school timetabled CT&AI for Classes 3-8 this year? Which classes, and how many periods a week?
2. Who teaches it in Classes 3-5? In Classes 6-8?
3. Are you using the CBSE student and teacher books? How are teachers finding them?
4. Did teachers attend NISHTHA or any other training for CT&AI? Was it useful?
5. How is CT&AI being assessed? How does it appear on report cards?
6. What do parents ask about it?
7. What would make it easier to deliver: lesson plans, worksheets, a platform, training, assessment tools?
8. Have any vendors approached you about CT&AI? What did they offer, and at what price?
9. (ICSE) Have you heard anything from CISCE about CT or AI for the younger classes?

### 3. Class 3-5 maths or EVS teacher (40 min)

**Their experience (15 min)**

1. How long have you been teaching, and which subjects?
2. Have you taught any CT&AI lessons yet? Tell me about the last one.
3. What was hardest to prepare or explain?
4. How much time do you have to plan a new lesson in a typical week?
5. Have you used any computer or tablet activities with your class? What happened?

**Paper prototype (20 min)**

Show a printed **Band B, Level B3 (conditionals)** lesson that follows the PRIMM-plus-Parsons template: predict and run, investigate, modify, solve a Parsons problem, make. Ask the teacher to think aloud while reading it, then ask:

6. Could you run this in one period tomorrow? What would stop you?
7. Which step would your students find hardest?
8. What would you change?
9. Would you use it on a projector, on paper, or in the computer lab?

**Close (5 min)**

10. What would make you look forward to teaching this, instead of seeing it as extra work?

### 4. Computer teacher (30 min)

**Device audit:** record these as numbers, not impressions.

1. How many working computers or tablets does the school have, and where are they?
2. How many classes share the lab? How many minutes of lab time does a Class 4 section get each week?
3. What's the internet like in the lab and in classrooms?
4. Is there a projector or smart board in classrooms? How many work?
5. What operating system and specification are the devices (Windows, Android, how old)?

**Practice**

6. What do you teach in Classes 3-8 today, and with which tools (Scratch, PictoBlox, Python, MS Office)?
7. When do students first write Python or another text language? How does it go?
8. What do students find hardest when they move from blocks to typing code?

### 5. Parents (optional, 15 min)

1. What does your child do in computer or CT&AI class? How do you know?
2. What do you want them to learn about computers and AI over the next few years?
3. Have you ever paid for coding classes or apps outside school? Why did you stop or continue?
4. If the school's program had a home practice part, how much would you pay a month, if anything?
5. What would make you trust an education app?

## Note template

Copy this for each interview and save as `docs/research/interviews/<school-code>-<role>.md`. Use no real names. That folder is ignored by Git because this repository is public, so the notes stay on your computer only; back them up somewhere private.

```markdown
# <School code> · <Role> · <Date>

- Board / fee tier / city type / medium:
- Interviewer:
- Recorded: yes / no

## Key quotes
- "..."

## Facts
- CT&AI timetabled: yes / no / partly (Classes: )
- Current product and cost:
- Book list closes:
- Price-anchor reaction (200 / 500 / 800):
- Devices (from audit):

## Hypothesis evidence
| H# | For / Against / Unclear | Evidence |
|---|---|---|

## Surprises

## Follow-ups
```

## Analysis

1. After each interview, fill in the template on the same day.
2. Every 5 schools, update a running tally of For / Against / Unclear for each hypothesis.
3. After all interviews, group quotes by theme (affinity mapping), separately for each fee tier and board.
4. Write a 2-page findings memo: what we learned, which hypotheses held, what changes in the product plan, and whether to make a pilot offer.

**Decision rule:** go ahead with a December pilot offer if H1, H2 and H3 are supported in at least half of the CBSE schools and H4 holds in the mid and premium tiers. If H1 fails, the product shouldn't depend on the CBSE circular: revisit the parent channel and the ICSE and state-board angles.

## Timeline

| Week | Dates (2026) | Work |
|---|---|---|
| 1 | 9-13 Nov | Finalise guides, print the Level B3 paper prototype, start recruiting |
| 2-4 | 16 Nov - 4 Dec | Interviews: about 6 schools a week |
| 5 | 7-11 Dec | Final interviews, tally hypotheses |
| 6 | 14-18 Dec | Findings memo and go/no-go on the pilot offer |

## Materials

All drafted in [interview-materials/](interview-materials/):

- [One-page introduction for schools](interview-materials/intro-letter.md), with the opening and consent script.
- [Level B3 paper prototype](interview-materials/level-b3-paper-prototype.md): one lesson of about 4 printed pages.
- [Device audit sheet](interview-materials/device-audit-sheet.md) for the computer teacher.
- [Tracking sheet template](interview-materials/tracking-sheet-template.csv). Copy it to a private file before adding contacts.
