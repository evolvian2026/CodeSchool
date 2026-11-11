"""Build the 'Think Like a Coder' sample examination papers for a class: a half-yearly and an annual paper, each with a
blueprint and a marking scheme; Classes 6-8 add a practical and project assessment guide.

Usage: python -P -E docs/books/tools/build_papers.py <class number> [out.pdf]
Questions come from docs/books/class<N>/papers.py (PAPERS, plus PRACTICAL for Classes 6-8). Chapter names come from the
student book (class<N>/content.py via build_book).

Paper patterns (CBSE publishes no CT&AI question-paper pattern for Classes 3-8; these follow the handbooks' written tests
and CBSE's usual competency-based question types):
  Classes 3-5: 40 marks, 1 1/2 hours. A: 8 x 1 MCQ, B: 6 x 2 very short, C: 4 x 3 short, D: 2 x 4 case-based.
  Classes 6-8: 50 marks, 2 hours. A: 10 x 1 MCQ and assertion-reason, B: 5 x 2, C: 5 x 3, D: 2 x 5 long, E: 1 x 5 case-based.
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

CH, CLASS = B.CH, B.CLASS
P, box, icon, C, CW, LM, PW, PH = B.P, B.box, B.icon, B.C, B.CW, B.LM, B.PW, B.PH
table, heading, checklist = S.table, S.heading, S.checklist
_spec = importlib.util.spec_from_file_location(f"papers_class{CLASS}", B.BOOKS / f"class{CLASS}" / "papers.py")
_p = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_p)
PAPERS, PRACTICAL = _p.PAPERS, getattr(_p, "PRACTICAL", None)
_args = [a for a in sys.argv[1:] if not a.isdigit()]
OUT = _args[0] if _args else str(B.BOOKS / f"CodeSchool-Class{CLASS}-Sample-Papers.pdf")
NAVY = "#1E3A5F"
CHN = {ch["n"]: ch for ch in CH}
MIDDLE = CLASS >= 6

if MIDDLE:
    SUBJECT, MARKS, TIME = "Computational Thinking and Artificial Intelligence", 50, "2 hours"
    SECTIONS = [("A", "Multiple choice and assertion-reason", 10, 1), ("B", "Very short answer", 5, 2), ("C", "Short answer", 5, 3),
                ("D", "Long answer", 2, 5), ("E", "Case-based question", 1, 5)]
else:
    SUBJECT, MARKS, TIME = "Computational Thinking", 40, "1½ hours"
    SECTIONS = [("A", "Multiple choice", 8, 1), ("B", "Very short answer", 6, 2), ("C", "Short answer", 4, 3), ("D", "Case-based questions", 2, 4)]
LEVELS = [("R", "Remember", "recall a fact or term"), ("U", "Understand", "explain or interpret an idea"),
          ("Ap", "Apply", "use an idea or rule in a new problem"), ("An", "Analyse and create", "trace, debug, compare, design or justify")]
LINES = {1: 1, 2: 2, 3: 4, 4: 2, 5: 6}  # answer lines by marks (question-cum-answer papers, Classes 3-5)


def marks(q):
    return sum(m for _, m in q["parts"]) if q.get("parts") else q["m"]


def check():
    for p in PAPERS:
        qs = p["questions"]
        for letter, _, n, m in SECTIONS:
            sec = [q for q in qs if q["s"] == letter]
            assert len(sec) == n, (p["key"], letter, len(sec))
            assert all(marks(q) == m for q in sec), (p["key"], letter, [marks(q) for q in sec])
        assert sum(marks(q) for q in qs) == MARKS, p["key"]
        assert [q["s"] for q in qs] == sorted(q["s"] for q in qs), p["key"]
        for q in qs:
            assert q["ch"] in CHN and q["lv"] in dict((l[0], 1) for l in LEVELS), (p["key"], q["q"][:40])
            if q["s"] == "A":
                assert q.get("opts"), q["q"][:40]


# ------------------------------------------------------------------ the question paper
def paper_header(p):
    t = Table([[P(f"<b>SAMPLE PAPER  ·  {p['name'].upper()}</b>", "q", fontSize=10, textColor=colors.white, alignment=1)],
               [P(f"Class {CLASS}  ·  {SUBJECT}", "h", fontSize=16, leading=20, alignment=1)],
               [P(f"Syllabus: {p['scope']}", "small", alignment=1)]], colWidths=[CW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), C(NAVY)), ("BOX", (0, 0), (-1, -1), 1.2, C(NAVY)),
                           ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    info = Table([[P(f"<b>Time allowed:</b> {TIME}", "body", spaceAfter=0), P(f"<b>Maximum marks:</b> {MARKS}", "body", spaceAfter=0, alignment=2)],
                  [P("<b>Name:</b> ______________________________", "body", spaceAfter=0),
                   P("<b>Section:</b> ______  <b>Roll no.:</b> ______", "body", spaceAfter=0, alignment=2)]], colWidths=[CW / 2, CW / 2])
    info.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 3)]))
    return [t, Spacer(1, 6), info, Spacer(1, 4)]


def instructions():
    secs = "; ".join(f"Section {l}: {name.lower()}, {n} question{'s' if n > 1 else ''} of {m} mark{'s' if m > 1 else ''} each"
                     for l, name, n, m in SECTIONS)
    items = [f"This paper has {sum(s[2] for s in SECTIONS)} questions in {len(SECTIONS)} sections. All questions are compulsory.",
             secs + ".", "Marks for each question are shown on the right.",
             "No calculator or computer is needed. Show your working: marks are given for correct steps."]
    if MIDDLE:
        items.insert(3, "Write your answers on the separate answer sheet. Draw tables and diagrams neatly where asked.")
    else:
        items.insert(3, "Write your answers in the space given below each question.")
    rows = [[P(f"{i}.", "small", textColor=B.INK), P(t, "small", textColor=B.INK)] for i, t in enumerate(items, 1)]
    t = Table(rows, colWidths=[16, CW - 36])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 2), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    return [Table([[P("<b>General instructions</b>", "small", textColor=B.INK)], [t]], colWidths=[CW],
                  style=[("BOX", (0, 0), (-1, -1), 0.8, C("#B8C2D3")), ("BACKGROUND", (0, 0), (-1, -1), C("#F4F6FA")),
                         ("LEFTPADDING", (0, 0), (-1, -1), 8)]), Spacer(1, 8)]


def section_head(letter, name, n, m):
    t = Table([[P(f"<b>SECTION {letter}</b>  ·  {name}", "q", fontSize=11.5, textColor=colors.white),
                P(f"<b>{n} x {m} = {n * m} marks</b>", "q", fontSize=10.5, textColor=colors.white, alignment=2)]], colWidths=[CW - 130, 130])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), C(NAVY)), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return t


def question(i, q):
    content = [P(q["q"], "q", fontSize=11.5, leading=15.5)]
    if q.get("fig"):
        content += [Spacer(1, 3), q["fig"](), Spacer(1, 2)]
    if q.get("opts") and max(len(o) for o in q["opts"]) > 40:  # long options (assertion-reason): one per line
        rows = [[P(f"<font name='KidBl' color='{NAVY}'>{chr(97 + k)})</font>&nbsp; {o}", "q", fontSize=11)] for k, o in enumerate(q["opts"])]
        t = Table(rows, colWidths=[CW - 80])
        t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
        content += [Spacer(1, 2), t]
    elif q.get("opts"):
        content += [Spacer(1, 2), B.options(q["opts"], NAVY)]
    if q.get("parts"):
        for k, (txt, m) in enumerate(q["parts"]):
            row = Table([[P(f"({chr(97 + k)})", "q", fontSize=11.5), P(txt, "q", fontSize=11.5, leading=15.5),
                          P(f"[{m}]", "small", textColor=B.INK, alignment=2)]], colWidths=[22, CW - 100, 30])
            row.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 2), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
            content.append(row)
            if not MIDDLE:
                content += [B.lines(q.get("lines", LINES[m]), CW - 80)]
    elif not MIDDLE and not q.get("opts"):
        content += [Spacer(1, 3), B.lines(q.get("lines", LINES[q["m"]]), CW - 80)]
    m = "" if q.get("parts") else f"[{q['m']}]"
    t = Table([[P(f"<b>{i}.</b>", "q", fontSize=11.5), content, P(m, "small", textColor=B.INK, alignment=2)]], colWidths=[26, CW - 56, 30])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 5 if MIDDLE else 7)]))
    return t


def paper_story(p):
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter({"n": 0, "title": "", "color": NAVY, "header": f"Sample paper  ·  {p['name']}"}),
         B.TocMark(f"{p['name']} (question paper)", p["key"])]
    s += paper_header(p) + instructions()
    i, blk = 0, []
    for letter, name, n, m in SECTIONS:
        for k, q in enumerate([q for q in p["questions"] if q["s"] == letter]):
            i += 1
            if blk:
                s.append(KeepTogether(blk))
            blk = [section_head(letter, name, n, m), Spacer(1, 5), question(i, q)] if k == 0 else [question(i, q)]
        blk.append(Spacer(1, 4))
    # the end marker stays with the last question
    s.append(KeepTogether(blk + [P("<b>*** End of the question paper ***</b>", "small", alignment=1, textColor=B.INK)]))
    return s


# ------------------------------------------------------------------ teacher pages
def blueprint(p):
    qs = p["questions"]
    chs = sorted({q["ch"] for q in qs})
    head = ["Chapter"] + [f"{l}" for l, *_ in SECTIONS] + ["Marks"]
    rows = [head]
    for n in chs:
        cells = []
        for l, *_ in SECTIONS:
            v = sum(marks(q) for q in qs if q["ch"] == n and q["s"] == l)
            cells.append(str(v) if v else "")
        rows.append([B.ch_label(CHN[n])] + cells + [str(sum(marks(q) for q in qs if q["ch"] == n))])
    rows.append(["Total"] + [str(n * m) for _, _, n, m in SECTIONS] + [str(MARKS)])
    w = 40
    t1 = table(rows, [CW - w * (len(SECTIONS) + 1)] + [w] * (len(SECTIONS) + 1), font=9)
    lv = [["Level", "What the student does", "Marks", "Share"]]
    for code, name, what in LEVELS:
        v = sum(marks(q) for q in qs if q["lv"] == code)
        lv.append([name, what, str(v), f"{round(100 * v / MARKS)}%"])
    t2 = table(lv, [110, CW - 230, 60, 60], font=9.5)
    return [KeepTogether([P(f"Blueprint: {p['name']}", "h", fontSize=14, leading=18), P(f"Syllabus: {p['scope']}. Marks by chapter and section.", "small"),
                          Spacer(1, 3), t1, Spacer(1, 6), P("Marks by thinking level", "q", fontName="KidB", fontSize=11),
                          P("Each question is counted at its main thinking level.", "small"), Spacer(1, 2), t2]), Spacer(1, 12)]


def scheme(p):
    s = [P(f"Marking scheme: {p['name']}", "ansh", fontSize=12.5, leading=16)]
    for i, q in enumerate(p["questions"], 1):
        g = f" <font color='#5B6577'>({q['guide']})</font>" if q.get("guide") else ""
        s.append(P(f"<b>{i}.</b> {q['answer']}{g}", "ans"))
    return s


def teacher_story():
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), B.TocMark("Blueprints", "blueprints"), heading("Blueprints")]
    for p in PAPERS:
        s += blueprint(p)
    s += [NextPageTemplate("twocol"), PageBreak(), B.TocMark("Marking schemes", "schemes"),
          P("Marking schemes", "h", fontSize=22, leading=27),
          P("Accept any correct method and any sensible wording. Give part marks for correct steps, even when the final answer has a slip.", "small"),
          Spacer(1, 4)]
    for p in PAPERS:
        s += scheme(p) + [Spacer(1, 6)]
    s += [NextPageTemplate("body")]
    return s


def practical_story():
    pr = PRACTICAL
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), B.TocMark("Practical and project assessment", "practical"),
         heading("Practical and project assessment"),
         P("CBSE's Classes 6-8 handbooks assess CT&AI through practical examinations, project presentations and reflective journals as well as "
           "written tests. CBSE has not fixed how the marks are split, so the school decides. One way to make a 100-mark annual result:", "body"),
         table([["Component", "Marks", "Evidence"], ["Written examination (this paper)", "50", "Annual sample paper"],
                ["Practical examination (unplugged)", "20", "Two stations from the list below, 10 marks each"],
                ["Projects (two 20-hour projects)", "20", "Project rubrics in the workbook; presentation and data sheets"],
                ["Observation journal and reflection", "10", "Teacher Observation Journal levels from the teacher book"]], [200, 60, CW - 260], font=10),
         Spacer(1, 8), P("Practical examination stations", "h", fontSize=14, leading=18),
         P("Each station takes about 15 minutes. Students work alone or in pairs with paper, cards or the classroom kit; the examiner "
           "watches, asks the two questions shown, and marks with the rubric. No computer is needed.", "small"), Spacer(1, 4)]
    rows = [["Station", "Task", "Examiner asks"]]
    for st in pr["stations"]:
        rows.append([st[0], st[1], st[2]])
    s += [table(rows, [110, CW - 290, 180], font=9.5), Spacer(1, 8), P("Rubric for each station (10 marks)", "h", fontSize=14, leading=18), Spacer(1, 2)]
    s += [table([["Criterion", "Marks", "Full marks when the student ..."],
                 ["Understands the task", "2", "restates the goal and what a correct result looks like"],
                 ["Method", "4", "follows or designs clear, ordered steps; uses the right CT or AI idea"],
                 ["Result and checking", "2", "gets a correct result and checks or tests it"],
                 ["Explaining", "2", "answers the examiner's questions with reasons, using the right words"]], [150, 50, CW - 200], font=10)]
    return s


# ------------------------------------------------------------------ front matter
def contents_page():
    toc = TableOfContents(); toc.dotsMinLevel = 0
    toc.levelStyles = [ParagraphStyle("pt", parent=B.S["toc0"], leading=19)]
    return [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), P("What's inside", "h", fontSize=24, leading=30), Spacer(1, 4), toc]


def about_page():
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), B.TocMark("About these papers", "about"), heading("About these papers"),
         P(f"These are two sample examination papers for Class {CLASS}: a <b>half-yearly</b> paper on the term-1 chapters and an <b>annual</b> paper on "
           f"the whole year. They go with <i>Think Like a Coder</i>, Class {CLASS}, and with the chapter assessments. All questions are new.", "body"),
         Spacer(1, 4), P("How they follow CBSE", "h", fontSize=14, leading=18)]
    pts = ["CBSE does not hold board examinations for Classes 3-8 and has not published a question-paper pattern for CT&AI. Schools set their own "
           "papers. These papers follow what CBSE's CT&AI handbooks describe: <b>competency-based</b> written tests with CT puzzles, with no "
           "'write a program' questions and no computer needed.",
           "The question types are the ones CBSE uses in its competency-based papers: multiple choice"
           + (", assertion-reason, short and long answers, and a case-based question." if MIDDLE else ", short answers and case-based questions."),
           "Questions are spread across four thinking levels (remember, understand, apply, analyse and create), with most marks for applying and "
           "analysing. The blueprints show the split.",
           "Chapters follow the order of CBSE's 2026-27 CT&AI handbooks and the NCERT maths chapters"
           + (", including the four AI chapters." if MIDDLE else ".")]
    if MIDDLE:
        pts.append("The handbooks also assess Classes 6-8 through practical examinations, project presentations and reflective journals. "
                   "The last section gives unplugged practical stations, a rubric and one way to combine the marks.")
    s += [checklist(pts, NAVY), Spacer(1, 6), P("Paper design", "h", fontSize=14, leading=18), Spacer(1, 2)]
    rows = [["Section", "Question type", "Questions", "Marks"]] + [[l, name, str(n), f"{n} x {m} = {n * m}"] for l, name, n, m in SECTIONS]
    rows.append(["", f"Total  ·  {TIME}", str(sum(s_[2] for s_ in SECTIONS)), str(MARKS)])
    s += [table(rows, [56, CW - 56 - 80 - 90, 80, 90], font=10), Spacer(1, 8)]
    s += [box([checklist(["Use the half-yearly paper in September and the annual paper in February-March, or as mock tests before the school's own exams.",
                          ("Print one paper per student; students answer on separate answer sheets." if MIDDLE else
                           "Print one paper per student; the papers have space for answers."),
                          "Read questions aloud to students who find reading hard: the paper tests thinking, not reading.",
                          "Mark with the marking scheme; accept any correct method, and give part marks for correct steps.",
                          "Use the blueprints to set your own papers in the same pattern."], "#14A3A3")], "#14A3A3", "Using the papers", icon("check"))]
    return s


def on_cover(c, doc):
    c.saveState()
    c.setFillColor(C(NAVY)); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    c.setFillColor(C("#264B78")); c.rect(0, 0, PW, PH * 0.30, stroke=0, fill=1)
    for x, y, r, col in ((470, 700, 30, "#FFD23F"), (530, 800, 22, "#EC4899"), (548, 590, 46, "#2BB673"), (70, 470, 26, "#14A3A3"), (540, 380, 28, "#F5A524")):
        c.setFillColor(C(col)); c.circle(x, y, r, stroke=0, fill=1)
    c.setFillColor(C("#FFD23F")); c.roundRect(LM + 10, PH - 84, 150, 26, 13, stroke=0, fill=1)
    c.setFillColor(B.INK); c.setFont("KidB", 11); c.drawCentredString(LM + 85, PH - 75, "SAMPLE PAPERS")
    c.setFillColor(colors.white); c.setFont("KidBl", 48); c.drawString(LM + 10, PH - 150, "Think Like")
    c.drawString(LM + 10, PH - 202, "a Coder")
    c.setFillColor(C("#FFD23F")); c.setFont("Fun", 22); c.drawString(LM + 14, PH - 240, f"Sample examination papers, Class {CLASS}")
    c.setFillColor(colors.white); c.setFont("Kid", 12.5)
    lines = ["Half-yearly and annual papers", f"{MARKS} marks, {TIME}, with blueprints and marking schemes"]
    if MIDDLE:
        lines.append("Practical stations and project assessment")
    for k, line in enumerate(lines):
        c.drawString(LM + 14, PH - 268 - k * 18, line)
    F.robo(220, color=F.YELLOW, wave=True).drawOn(c, PW - 290, 250)
    c.setFillColor(colors.white); c.setFont("KidB", 12.5)
    c.drawString(LM + 10, 190, "For CBSE's Computational Thinking and AI curriculum, 2026-27")
    c.setFont("Kid", 11)
    c.drawString(LM + 10, 170, f"Goes with Think Like a Coder, Class {CLASS}  ·  Photocopiable for school use")
    c.setFillColor(C("#FFD23F")); c.roundRect(LM + 10, 112, 196, 30, 15, stroke=0, fill=1)
    c.setFillColor(B.INK); c.setFont("KidB", 11); c.drawCentredString(LM + 108, 122, "SAMPLE EDITION  ·  DRAFT")
    c.setFillColor(colors.white); c.setFont("Kid", 8.5)
    c.drawString(LM + 10, 52, "© 2026 Bullseye Knowledge System Limited. All rights reserved.")
    c.drawString(LM + 10, 40, "CodeSchool is a working name. Not an official CBSE or NCERT publication.")
    c.restoreState()


class PaperDoc(BaseDocTemplate):
    def __init__(self, fn):
        super().__init__(fn, pagesize=B.A4, leftMargin=B.LM, rightMargin=B.RM, topMargin=B.TM, bottomMargin=B.BM,
                         title=f"Think Like a Coder - Class {CLASS} sample examination papers", author="CodeSchool, Bullseye Knowledge System Limited",
                         subject=f"Half-yearly and annual sample papers for Class {CLASS}")
        fr = Frame(B.LM, B.BM, CW, PH - B.TM - B.BM, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        gap = 18
        left = Frame(B.LM, B.BM, (CW - gap) / 2, PH - B.TM - B.BM, id="l", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        right = Frame(B.LM + (CW + gap) / 2, B.BM, (CW - gap) / 2, PH - B.TM - B.BM, id="r", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate("cover", [fr], onPage=on_cover), PageTemplate("body", [fr], onPageEnd=B.on_body),
                               PageTemplate("twocol", [left, right], onPageEnd=B.on_body)])
        self.chapter = None
        self.default_header = f"Sample papers  ·  Class {CLASS}"
        self.footer_note = "Sample examination papers · photocopiable for school use"


def build():
    check()
    story = [Spacer(1, 1)] + contents_page() + about_page()
    for p in PAPERS:
        story += paper_story(p)
    story += teacher_story()
    if MIDDLE and PRACTICAL:
        story += practical_story()
    PaperDoc(OUT).multiBuild(story)
    print("built", OUT)


if __name__ == "__main__":
    build()
