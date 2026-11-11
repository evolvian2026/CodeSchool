"""Build the 'Think Like a Coder' teacher book for a class.

Usage: python -P -E docs/books/tools/build_teacher.py <class number> [out.pdf]
Lesson notes come from docs/books/class<N>/teacher.py (LESSONS keyed by chapter number, TMETA);
chapter content, answers and styles come from the student book (class<N>/content.py via build_book).
"""
import pathlib, sys, importlib.util
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_book as B
import build_specimen as S
import figures as F
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Spacer, Table, TableStyle, PageBreak, NextPageTemplate, KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents

CH, META, CLASS, PROJECTS = B.CH, B.META, B.CLASS, B.PROJECTS
P, box, icon, C, CW, LM, PW, PH = B.P, B.box, B.icon, B.C, B.CW, B.LM, B.PW, B.PH
table, heading, checklist = S.table, S.heading, S.checklist
_spec = importlib.util.spec_from_file_location(f"teacher_class{CLASS}", B.BOOKS / f"class{CLASS}" / "teacher.py")
_t = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_t)
LESSONS, TMETA = _t.LESSONS, _t.TMETA
_args = [a for a in sys.argv[1:] if not a.isdigit()]
OUT = _args[0] if _args else str(B.BOOKS / f"CodeSchool-Class{CLASS}-Teacher-Book.pdf")
NAVY = "#1F2A44"
PERIODS = TMETA.get("periods_per_chapter", 5)


def words_list(ch):
    return ", ".join(f"<i>{w}</i>" for w, _ in ch["words"])


def join_and(items):
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


# ------------------------------------------------------------------ front matter
def contents_page():
    toc = TableOfContents(); toc.dotsMinLevel = 0
    toc.levelStyles = [ParagraphStyle("tt", parent=B.S["toc0"], leading=15 if len(CH) + len(PROJECTS) > 12 else 17.5)]
    return [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), P("What's inside", "h", fontSize=24, leading=30), Spacer(1, 4), toc]


def about_pages():
    hours, periods = TMETA["hours"], len(CH) * PERIODS + TMETA.get("review_periods", 0)
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), B.TocMark("About this teacher book", "about"), heading("About this teacher book"),
         P(f"This book goes with the <i>Think Like a Coder</i> Class {CLASS} workbook. It gives you a plan for every chapter, so that a maths or class teacher "
           f"can teach computational thinking confidently without being a computer specialist. CBSE suggests about <b>{hours} hours</b> a year for Class {CLASS}; "
           f"the plans here use <b>{periods} periods of 40 minutes</b>, which is about {round(periods * 40 / 60)} hours."), Spacer(1, 8)]
    s += [box([checklist([f"<b>A year plan</b> showing which chapter to teach in which term, next to the NCERT maths chapter.",
                          f"<b>A {PERIODS}-period plan for every chapter</b>: what you do and what students do in each period.",
                          "<b>A hands-on activity</b> for every chapter, with set-up steps and a tip.",
                          "<b>Common mistakes</b> to watch for, and how to support or stretch students.",
                          "<b>An exit check</b> with answers, and what to note in the observation journal.",
                          "<b>The answer key</b> for every page of the student workbook.",
                          "<b>Photocopiable</b> observation journal and term summary pages at the back."], "#14A3A3")],
              "#14A3A3", "What is in this book", icon("star")), Spacer(1, 10)]
    s += [box([checklist(["Read the chapter in the student book and these notes. Most lessons need 5 to 10 minutes to prepare.",
                          "Get the kit items ready (listed under <i>At a glance</i>). Everything is reusable.",
                          "Plan pairs in advance: mix confident readers with children who prefer talking and acting out.",
                          "Teach the CT chapter in the same week or fortnight as the matching NCERT maths chapter, so the maths is fresh.",
                          "Keep it active: children should talk, act out and build more than they listen."], "#8B5CF6")],
              "#8B5CF6", "Before you start", icon("check")), Spacer(1, 10)]
    s += [box([P("No computers are needed. Every idea is taught with paper, cards, the floor mat and talk. These are the same ideas children will later use in block coding "
                 "and AI: steps in order, loops, decisions, data and testing. A projector helps for showing pages but is optional.", "body")], "#5B6577", "No computer lab needed")]
    return s


def year_plan():
    rows = [["Ch", "Chapter", "Coder skill", "Level", "Periods", "Term"]]
    for ch in CH:
        term = next((t for t, chs in TMETA["terms"] if ch["n"] in chs), "")
        rows.append([B.ch_badge(ch), ch["title"], ch["skill"], ch["level"], str(PERIODS), term])
    rp = TMETA.get("review_periods", 0)
    if rp:
        rows.append(["", "Revision and term assessment", "Review games, the term summary and parent feedback", "All", str(rp), "Both"])
    total = len(CH) * PERIODS + rp
    s = [NextPageTemplate("body"), PageBreak(), B.TocMark("Year plan", "yearplan"), heading("Year plan"),
         P(f"{len(CH)} chapters of {PERIODS} periods each, plus {rp} periods for revision and assessment: <b>{total} periods</b> of 40 minutes in all. "
           "Teach each chapter alongside the NCERT maths chapter with the same name; the order and timing can follow your school's maths plan.", "body"), Spacer(1, 6),
         table(rows, [28, 112, CW - 28 - 112 - 44 - 46 - 60, 44, 46, 60], font=9)]
    return s


def assessment_pages():
    s = [NextPageTemplate("body"), PageBreak(), B.TocMark("Assessment", "assessment"), heading("Assessment and the observation journal"),
         P("CBSE asks for continuous, competency-based assessment in CT&amp;AI: written puzzles, group activities and a <b>Teacher Observation Journal</b>. "
           "This book makes that simple. In each chapter, the exit check and the 'what to note' box tell you what to look for; record one level per child per skill "
           "every few chapters, not every lesson.", "body"), Spacer(1, 6)]
    s += [table(TMETA["assess"], [100] + [(CW - 100) / 4] * 4, font=9), Spacer(1, 10)]
    s += [box([checklist(["<b>Watch and listen</b> during activities: explaining, predicting and fixing show understanding better than a written answer.",
                          "<b>Use the exit check</b> at the end of each chapter: two quick questions, answers in this book.",
                          "<b>Compare with self-checks</b>: each chapter ends with 'How did I do?', where children colour a face for each 'I can' statement.",
                          "<b>Summarise each term</b> on the term summary page: one level per area and a short comment for the report card."], "#14A3A3")],
              "#14A3A3", "How to assess without extra tests", icon("check")), Spacer(1, 10)]
    s += [KeepTogether([box([P("Use the four levels for every skill. <b>Beginning</b>: needs help to start. <b>Developing</b>: succeeds with prompts or a partner. "
                               "<b>Secure</b>: succeeds alone on familiar problems. <b>Extending</b>: solves new problems and explains why. "
                               "Most children will be Developing or Secure; that is expected and healthy.", "body")], "#5B6577", "The four levels")])]
    return s


# ------------------------------------------------------------------ chapter notes
def period_rows(ch, L):
    ex, b, a = ch["example"], ch["build"], L["activity"]
    rows = [["Period", "Focus", "Teacher does", "Students do"],
            ["1", "Learn and see", f"Read Robo's tip aloud and teach the words {words_list(ch)}. Work through the example <i>{ex['title']}</i> on the board, "
                               "asking for a prediction before each step.", "Predict each step, then explain the example to a partner in their own words."],
            ["2", f"Hands-on: {a['title']}", "Run the activity below. Move between groups and note who can explain the idea.", a.get("students", "Work in pairs or groups, act it out and record what they did.")],
            ["3", "Try it!", "Set questions 1-5. After about 15 minutes, pairs swap books and check with the answer key. Discuss the hardest question together.",
             "Answer questions 1-5. Explain one answer to the class."],
            ["4", "Now you build it", f"{b['intro']} Model the first card or step, then let pairs finish.", b["task"]],
            ["5", "Challenge and check", "Give the challenge to early finishers, then solve it together. Run the exit check and note levels in the journal.",
             "Try the challenge, colour 'How did I do?' and answer the exit check."]]
    return rows


def lesson_story(ch, L):
    col = ch["color"]
    tch = dict(ch, kicker="TEACHER NOTES  ·  " + ch.get("kicker", f"CHAPTER {ch['n']}"))
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(ch), B.Banner(tch), Spacer(1, 8)]
    glance = [["At a glance", ""],
              ["Students will", join_and(ch["ican"]) + "."],
              ["Key words", ", ".join(f"<b>{w}</b> ({m})" for w, m in ch["words"])],
              ["Materials", L["materials"]],
              ["Time", f"{PERIODS} periods of 40 minutes"],
              ["Link", L.get("link", f"Teach alongside chapter {ch['n']} of {META['textbook_long']}.")]]
    s += [table(glance, [92, CW - 92], head_color=col, font=9.5), Spacer(1, 8)]
    s += [KeepTogether([P(f"<font color='{col}'><b>Period by period</b></font>", "h", fontSize=13, leading=17), Spacer(1, 2),
                        table(period_rows(ch, L), [40, 82, (CW - 122) / 2, (CW - 122) / 2], head_color=col, font=9)]), Spacer(1, 8)]
    a = L["activity"]
    acts = [P(a["intro"], "body")] if a.get("intro") else []
    for k, st in enumerate(a["steps"], 1):
        acts.append(P(f"<font name='KidBl' color='#2BB673'>{k}.</font>&nbsp; {st}", "body", leftIndent=14, firstLineIndent=-14))
    if a.get("tip"):
        acts.append(P(f"<b>Tip:</b> {a['tip']}", "small"))
    s += [KeepTogether([box(acts, "#2BB673", "Hands-on activity: " + a["title"], icon("blocks"))]), Spacer(1, 8)]
    s += [KeepTogether([box([checklist(L["mistakes"], "#E5484D")], "#E5484D", "Common mistakes to watch for")]), Spacer(1, 8)]
    s += [KeepTogether([box([P(f"<b>Support:</b> {L['support']}<br/><b>Stretch:</b> {L['stretch']}", "body")], "#8B5CF6", "Different paces")]), Spacer(1, 8)]
    ex = [P("Two quick questions at the end of the chapter:", "body")]
    for k, (q, ans) in enumerate(L["exit"], 1):
        ex.append(P(f"<b>{k}.</b> {q} <font color='#5B6577'>(Answer: {ans})</font>", "body"))
    ic = ch["ican"]
    look = L.get("look") or [f"needs help to {ic[0]}", f"can {ic[0]} with prompts or a partner", f"can {ic[0]} and {ic[1]} alone",
                             f"can {ic[-1]} and explain why"]
    ex.append(P("<b>Note in the journal:</b> " + "; ".join(f"<b>{lv}</b> ({t})" for lv, t in zip(("Beginning", "Developing", "Secure", "Extending"), look)) + ".", "body"))
    s += [KeepTogether([box(ex, "#14A3A3", "Exit check and what to note", icon("check"))]), Spacer(1, 8)]
    ans = [P(f"<b>{i}.</b> {q['answer']}", "ans") for i, q in enumerate(ch["practice"], 1)]
    ans += [P(f"<b>Build it:</b> {ch['build']['answer']}", "ans"), P(f"<b>Challenge:</b> {ch['challenge']['answer']}", "ans")]
    s += [KeepTogether([box(ans, "#5B6577", "Answer key")])]
    return s


# ------------------------------------------------------------------ back matter
def journal_page():
    skills = TMETA["journal_skills"]
    head = ["Student"] + skills + ["Notes"]
    w_skill = 70
    widths = [110] + [w_skill] * len(skills) + [CW - 110 - w_skill * len(skills)]
    data = [[P(f"<b>{h}</b>", "small", textColor=colors.white) for h in head]]
    lv = P("<font size='7.5' color='#9AA5B8'>B  D  S  E</font>", "small", alignment=1)
    data += [[""] + [lv] * len(skills) + [""] for _ in range(18)]
    t = Table(data, colWidths=widths, rowHeights=[None] + [26] * 18)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), C("#14A3A3")), ("GRID", (0, 0), (-1, -1), 0.6, C("#B8C2D3")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    return [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), B.TocMark("Observation journal (photocopy)", "journal"),
            heading("Observation journal"), P(f"Class {CLASS} ____  Section ____  Term ____  Chapters ________. Circle one level per skill: "
                                              "<b>B</b>eginning, <b>D</b>eveloping, <b>S</b>ecure, <b>E</b>xtending. You may photocopy this page.", "small"), Spacer(1, 6), t]


def summary_page():
    rows = [["Area", "Level (circle one)", "Teacher comment"]]
    for a in TMETA["summary_areas"]:
        rows.append([a, "B    D    S    E", ""])
    t = Table([[P(f"<b>{c}</b>" if i == 0 else c, "q", fontSize=10, textColor=colors.white if i == 0 else B.INK) for c in r] for i, r in enumerate(rows)],
              colWidths=[150, 110, CW - 260], rowHeights=[None] + [46] * (len(rows) - 1))
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), C("#14A3A3")), ("GRID", (0, 0), (-1, -1), 0.6, C("#B8C2D3")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    s = [NextPageTemplate("body"), PageBreak(), B.TocMark("Term summary (photocopy)", "summary"), heading("Term summary for the report card"),
         P("One copy per child each term. Fill it from the observation journal and the child's self-checks. You may photocopy this page.", "small"), Spacer(1, 10),
         P("<b>Name</b> ______________________________  <b>Class</b> ______  <b>Section</b> ______  <b>Term</b> ______", "body"), Spacer(1, 8), t, Spacer(1, 12),
         box([P("Write one strength and one next step, in words a parent understands. For example: <i>Explains steps clearly and fixes bugs in routes; "
                "next step: spotting the core of a pattern.</i>", "body")], "#5B6577", "Writing comments"), Spacer(1, 14),
         P("<b>Class teacher</b> ____________________   <b>Date</b> __________", "body")]
    return s


# ------------------------------------------------------------------ cover and document
def on_teacher_cover(c, doc):
    c.saveState()
    c.setFillColor(C(NAVY)); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    c.setFillColor(C("#2B3A5C")); c.rect(0, 0, PW, PH * 0.30, stroke=0, fill=1)
    for x, y, r, col in ((470, 700, 30, "#FFD23F"), (530, 800, 22, "#EC4899"), (548, 590, 46, "#14A3A3"), (70, 470, 26, "#8B5CF6"), (540, 380, 28, "#2BB673")):
        c.setFillColor(C(col)); c.circle(x, y, r, stroke=0, fill=1)
    c.setFillColor(C("#FFD23F")); c.roundRect(LM + 10, PH - 84, 140, 26, 13, stroke=0, fill=1)
    c.setFillColor(B.INK); c.setFont("KidB", 11); c.drawCentredString(LM + 80, PH - 75, "TEACHER BOOK")
    c.setFillColor(colors.white); c.setFont("KidBl", 48); c.drawString(LM + 10, PH - 150, "Think Like")
    c.drawString(LM + 10, PH - 202, "a Coder")
    c.setFillColor(C("#FFD23F")); c.setFont("Fun", 22); c.drawString(LM + 14, PH - 240, f"Teacher book for Class {CLASS}")
    c.setFillColor(colors.white); c.setFont("Kid", 12.5)
    for k, line in enumerate([f"A {PERIODS}-period plan for every chapter", "Hands-on activities, common mistakes and exit checks",
                              "Answer keys, assessment guide and photocopiable journal"]):
        c.drawString(LM + 14, PH - 268 - k * 18, line)
    F.robo(220, color=F.YELLOW, wave=True).drawOn(c, PW - 290, 250)
    c.setFillColor(colors.white); c.setFont("KidB", 12.5)
    c.drawString(LM + 10, 190, "For CBSE's Computational Thinking and AI curriculum, 2026-27")
    c.setFont("Kid", 11)
    c.drawString(LM + 10, 170, f"Goes with Think Like a Coder, Class {CLASS}  ·  {META['cover_follows']}")
    c.setFillColor(C("#FFD23F")); c.roundRect(LM + 10, 112, 196, 30, 15, stroke=0, fill=1)
    c.setFillColor(B.INK); c.setFont("KidB", 11); c.drawCentredString(LM + 108, 122, "SAMPLE EDITION  ·  DRAFT")
    c.setFillColor(colors.white); c.setFont("Kid", 8.5)
    c.drawString(LM + 10, 52, "© 2026 Bullseye Knowledge System Limited. All rights reserved.")
    c.drawString(LM + 10, 40, "CodeSchool is a working name. Not an official CBSE or NCERT publication.")
    c.restoreState()


class TeacherDoc(BaseDocTemplate):
    def __init__(self, fn):
        super().__init__(fn, pagesize=B.A4, leftMargin=B.LM, rightMargin=B.RM, topMargin=B.TM, bottomMargin=B.BM,
                         title=f"Think Like a Coder - Class {CLASS} teacher book", author="CodeSchool, Bullseye Knowledge System Limited",
                         subject=f"Teacher book with lesson plans for Class {CLASS}")
        fr = Frame(B.LM, B.BM, CW, PH - B.TM - B.BM, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate("cover", [fr], onPage=on_teacher_cover), PageTemplate("body", [fr], onPageEnd=B.on_body)])
        self.chapter = None
        self.default_header = f"Teacher book  ·  Class {CLASS}"
        self.footer_note = "Teacher book · draft for review"


def build():
    story = [Spacer(1, 1)]
    story += contents_page()
    story += about_pages()
    lesson = S.how_lesson_runs()
    lesson.insert(2, B.TocMark("How a lesson runs", "lesson"))
    story += lesson
    story += year_plan()
    story += assessment_pages()
    for ch in CH:
        story += lesson_story(ch, LESSONS[ch["n"]])
    story += journal_page()
    story += summary_page()
    doc = TeacherDoc(OUT)
    doc.multiBuild(story)
    print("built", OUT)


if __name__ == "__main__":
    build()
