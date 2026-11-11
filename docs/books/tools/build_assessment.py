"""Build the 'Think Like a Coder' assessment book for a class: one 10-mark assessment per chapter, with answers and marking guides.

Usage: python -P -E docs/books/tools/build_assessment.py <class number> [out.pdf]
Questions come from docs/books/class<N>/assessment.py (TESTS keyed by chapter number); chapter names, levels and colours
come from the student book (class<N>/content.py via build_book).
Each test: Section A, 3 multiple-choice questions (1 mark each); Section B, 2 short answers (2 marks each);
Section C, 1 'think like a coder' task (3 marks). Total 10 marks.
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

CH, META, CLASS = B.CH, B.META, B.CLASS
P, box, icon, C, CW, LM, PW, PH = B.P, B.box, B.icon, B.C, B.CW, B.LM, B.PW, B.PH
table, heading, checklist = S.table, S.heading, S.checklist
_spec = importlib.util.spec_from_file_location(f"assessment_class{CLASS}", B.BOOKS / f"class{CLASS}" / "assessment.py")
_a = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_a)
TESTS = _a.TESTS
_args = [a for a in sys.argv[1:] if not a.isdigit()]
OUT = _args[0] if _args else str(B.BOOKS / f"CodeSchool-Class{CLASS}-Assessment-Book.pdf")
PLUM = "#3B2A6B"
SECTIONS = [("A", "Choose the right answer", "#3B82F6"), ("B", "Answer in a few words or steps", "#F5A524"), ("C", "Think like a coder", "#2BB673")]
LEVELS = [("9-10", "Extending", "#2BB673"), ("7-8", "Secure", "#14A3A3"), ("4-6", "Developing", "#F5A524"), ("0-3", "Beginning", "#E5484D")]


def check_tests():
    for ch in CH:
        qs = TESTS[ch["n"]]
        secs = [q["s"] for q in qs]
        assert secs == ["A", "A", "A", "B", "B", "C"], (ch["n"], secs)
        assert all(q.get("opts") for q in qs[:3]), ch["n"]
        assert sum(marks(q) for q in qs) == 10, ch["n"]


def marks(q):
    return {"A": 1, "B": 2, "C": 3}[q["s"]]


# ------------------------------------------------------------------ a test page
def header_block(ch):
    col = ch["color"]
    title = f"<font color='{col}'>Assessment {B.ch_badge(ch)}</font>&nbsp; {ch['title']}"
    sub = f"Coder skill: {ch['skill']}  ·  Level {ch['level']}  ·  30 minutes  ·  10 marks"
    fields = Table([[P("<b>Name</b> ______________________________", "body", spaceAfter=0),
                     P("<b>Section</b> ______", "body", spaceAfter=0),
                     P("<b>Date</b> __________", "body", spaceAfter=0),
                     P("<b>Score</b> ____ / 10", "body", spaceAfter=0)]],
                   colWidths=[CW * 0.44, CW * 0.17, CW * 0.2, CW * 0.19])
    fields.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    t = Table([[P(title, "h", fontSize=18, leading=22)], [P(sub, "small")], [fields]], colWidths=[CW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), B.tint(col, 0.9)), ("BOX", (0, 0), (-1, -1), 1.2, C(col)),
                           ("ROUNDEDCORNERS", [10, 10, 10, 10]), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return t


def section_bar(letter, name, col, total):
    t = Table([[P(f"<font color='white'><b>Section {letter}</b>&nbsp;&nbsp;{name}</font>", "q", fontSize=11),
                P(f"<font color='white'><b>{total} marks</b></font>", "q", fontSize=10, alignment=2)]], colWidths=[CW - 80, 80])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), C(col)), ("ROUNDEDCORNERS", [7, 7, 7, 7]), ("TOPPADDING", (0, 0), (-1, -1), 3),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8)]))
    return t


def q_block(i, q, col, cut=0):
    m = marks(q)
    parts = [P(q["q"] + f"&nbsp; <font size='9' color='#5B6577'>[{m} mark{'s' if m > 1 else ''}]</font>", "q")]
    if q.get("fig"):
        parts += [Spacer(1, 4), q["fig"](), Spacer(1, 2)]
    if q.get("opts"):
        parts += [Spacer(1, 3), B.options(q["opts"], col)]
    if q.get("boxes"):
        parts += [Spacer(1, 4), B.answer_boxes(q["boxes"])]
    n = q.get("lines", 0 if (q.get("opts") or q.get("boxes")) else (2 if q["s"] == "B" else 4))
    if n:
        n = max(1 if q["s"] == "B" else 2, n - cut)  # cut: writing lines given up so the test fits on one page
        parts += [Spacer(1, 6 if cut < 2 else 3), B.lines(n)]
    t = Table([[B.number_badge(i, col), parts]], colWidths=[34, CW - 34])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 3),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 6 if cut < 2 else 3)]))
    return t


FH = PH - B.TM - B.BM  # body frame height


def test_body(ch, cut):
    qs = TESTS[ch["n"]]
    s, i = [header_block(ch), Spacer(1, 6)], 0
    for letter, name, col in SECTIONS:
        group = [q for q in qs if q["s"] == letter]
        for k, q in enumerate(group):
            i += 1
            if k == 0:  # keep the section bar with its first question
                s.append(KeepTogether([section_bar(letter, name, col, sum(marks(x) for x in group)), Spacer(1, 4), q_block(i, q, col, cut)]))
            else:
                s.append(KeepTogether([q_block(i, q, col, cut)]))
        s.append(Spacer(1, 2))
    return s


def height(flowables):
    return sum(sum(g.wrap(CW, FH)[1] for g in (f._content if isinstance(f, KeepTogether) else [f])) for f in flowables)


def test_story(ch):
    for cut in range(4):  # give up writing lines until the whole test fits on one page
        body = test_body(ch, cut)
        if height(body) <= FH - 6:
            break
    else:
        raise SystemExit(f"Assessment {ch['n']} does not fit on one page")
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(dict(ch, header=f"Assessment {B.ch_badge(ch)}  ·  {ch['title']}")),
         B.TocMark(f"{B.ch_label(ch)}", f"t{ch['n']}")] + body
    faces = B.ican(["finish this test", "show my thinking", "check my answers"], ch["color"])
    s += [B.IfFits(Table([[Spacer(1, 4)], [P("<b>How did I do?</b> Colour a face.", "small")], [faces]], colWidths=[CW],
                         style=[("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))]
    return s


# ------------------------------------------------------------------ front matter
def contents_page():
    toc = TableOfContents(); toc.dotsMinLevel = 0
    toc.levelStyles = [ParagraphStyle("at", parent=B.S["toc0"], leading=14.5 if len(CH) > 12 else 17)]
    return [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), P("What's inside", "h", fontSize=24, leading=30), Spacer(1, 4), toc]


def about_page():
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), B.TocMark("Using these assessments", "about"), heading("Using these assessments"),
         P(f"This book has one assessment for every chapter of <i>Think Like a Coder</i>, Class {CLASS}. Each assessment fits on one page, "
           "takes about 30 minutes and is marked out of 10. Use it after the chapter's last period, or as a revision check later in the term. "
           "All questions are new: they test the same skills as the workbook, not the same questions.", "body"), Spacer(1, 6)]
    rows = [["Section", "What it checks", "Questions", "Marks"],
            ["A", "Knowing and understanding the chapter's ideas", "3 multiple choice", "3 x 1"],
            ["B", "Applying the idea to a short problem, with working", "2 short answers", "2 x 2"],
            ["C", "Thinking like a coder: write, trace, fix or explain a program or plan", "1 task", "1 x 3"]]
    s += [table(rows, [56, CW - 56 - 110 - 54, 110, 54], font=10), Spacer(1, 8)]
    lv = [["Score", "Journal level", "What it usually means"],
          ["9-10", "Extending", "Solves new problems and explains the reasoning"],
          ["7-8", "Secure", "Applies the idea correctly on their own"],
          ["4-6", "Developing", "Understands with prompts; makes some slips"],
          ["0-3", "Beginning", "Needs more practice with the chapter's idea"]]
    s += [P("Turning a score into a journal level", "h", fontSize=14, leading=18), Spacer(1, 2), table(lv, [60, 100, CW - 160], font=10), Spacer(1, 8)]
    s += [box([checklist(["Read the questions aloud for children who find reading hard: we are testing thinking, not reading.",
                          "Give full marks for any correct method, even if it differs from the answer key; the marking guides list what to look for.",
                          "Give part marks in Sections B and C for correct working, even when the final answer has a slip.",
                          "Record the score on the class record sheet, and use it with your observations in the journal, not instead of them.",
                          "Go over the test with the class: the most common mistakes are a lesson plan for the next period."], "#8B5CF6")],
              "#8B5CF6", "Good practice", icon("check"))]
    return s


def record_sheet():
    head = ["Student"] + [B.ch_badge(ch) for ch in CH] + ["Avg"]
    n = len(CH)
    w_name, w_avg = 104, 34
    w = (CW - w_name - w_avg) / n
    data = [[P(f"<b>{h}</b>", "small", textColor=colors.white, alignment=1, fontSize=7.5 if len(h) > 2 else 8.5) for h in head]]
    data += [[""] * (n + 2) for _ in range(20)]
    t = Table(data, colWidths=[w_name] + [w] * n + [w_avg], rowHeights=[None] + [24] * 20)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), C(PLUM)), ("GRID", (0, 0), (-1, -1), 0.6, C("#B8C2D3")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("LEFTPADDING", (1, 0), (-1, -1), 1), ("RIGHTPADDING", (1, 0), (-1, -1), 1)]))
    return [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), B.TocMark("Class record sheet (photocopy)", "record"), heading("Class record sheet"),
            P(f"Class {CLASS} ____  Section ____  Term ____. Write each score out of 10. You may photocopy this page.", "small"), Spacer(1, 6), t]


def answer_key():
    s = [NextPageTemplate("twocol"), PageBreak(), B.SetChapter(None), B.TocMark("Answers and marking guide", "answers"),
         P("Answers and marking guide", "h", fontSize=22, leading=27),
         P("Accept any correct method. Part marks are shown in brackets for Sections B and C.", "small"), Spacer(1, 4)]
    for ch in CH:
        items = [P(f"<font color='{ch['color']}'>{B.ch_label(ch)}</font>", "ansh")]
        for i, q in enumerate(TESTS[ch["n"]], 1):
            g = f" <font color='#5B6577'>({q['guide']})</font>" if q.get("guide") else ""
            items.append(P(f"<b>{i}.</b> {q['answer']}{g}", "ans"))
        s.append(KeepTogether(items))
    s += [NextPageTemplate("body")]
    return s


# ------------------------------------------------------------------ cover and document
def on_cover(c, doc):
    c.saveState()
    c.setFillColor(C(PLUM)); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    c.setFillColor(C("#4C3A86")); c.rect(0, 0, PW, PH * 0.30, stroke=0, fill=1)
    for x, y, r, col in ((470, 700, 30, "#FFD23F"), (530, 800, 22, "#EC4899"), (548, 590, 46, "#2BB673"), (70, 470, 26, "#14A3A3"), (540, 380, 28, "#F5A524")):
        c.setFillColor(C(col)); c.circle(x, y, r, stroke=0, fill=1)
    c.setFillColor(C("#FFD23F")); c.roundRect(LM + 10, PH - 84, 170, 26, 13, stroke=0, fill=1)
    c.setFillColor(B.INK); c.setFont("KidB", 11); c.drawCentredString(LM + 95, PH - 75, "ASSESSMENT BOOK")
    c.setFillColor(colors.white); c.setFont("KidBl", 48); c.drawString(LM + 10, PH - 150, "Think Like")
    c.drawString(LM + 10, PH - 202, "a Coder")
    c.setFillColor(C("#FFD23F")); c.setFont("Fun", 22); c.drawString(LM + 14, PH - 240, f"Chapter assessments for Class {CLASS}")
    c.setFillColor(colors.white); c.setFont("Kid", 12.5)
    for k, line in enumerate([f"{len(CH)} one-page assessments, one for every chapter", "10 marks each: choose, apply and think like a coder",
                              "Answers, marking guides and a class record sheet"]):
        c.drawString(LM + 14, PH - 268 - k * 18, line)
    F.robo(220, color=F.YELLOW, wave=True).drawOn(c, PW - 290, 250)
    c.setFillColor(colors.white); c.setFont("KidB", 12.5)
    c.drawString(LM + 10, 190, "For CBSE's Computational Thinking and AI curriculum, 2026-27")
    c.setFont("Kid", 11)
    c.drawString(LM + 10, 170, f"Goes with Think Like a Coder, Class {CLASS}  ·  Photocopiable for classroom use")
    c.setFillColor(C("#FFD23F")); c.roundRect(LM + 10, 112, 196, 30, 15, stroke=0, fill=1)
    c.setFillColor(B.INK); c.setFont("KidB", 11); c.drawCentredString(LM + 108, 122, "SAMPLE EDITION  ·  DRAFT")
    c.setFillColor(colors.white); c.setFont("Kid", 8.5)
    c.drawString(LM + 10, 52, "© 2026 Bullseye Knowledge System Limited. All rights reserved.")
    c.drawString(LM + 10, 40, "CodeSchool is a working name. Not an official CBSE or NCERT publication.")
    c.restoreState()


class AssessDoc(BaseDocTemplate):
    def __init__(self, fn):
        super().__init__(fn, pagesize=B.A4, leftMargin=B.LM, rightMargin=B.RM, topMargin=B.TM, bottomMargin=B.BM,
                         title=f"Think Like a Coder - Class {CLASS} assessment book", author="CodeSchool, Bullseye Knowledge System Limited",
                         subject=f"Chapter assessments for Class {CLASS}")
        fr = Frame(B.LM, B.BM, CW, PH - B.TM - B.BM, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        gap = 18
        left = Frame(B.LM, B.BM, (CW - gap) / 2, PH - B.TM - B.BM, id="l", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        right = Frame(B.LM + (CW + gap) / 2, B.BM, (CW - gap) / 2, PH - B.TM - B.BM, id="r", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate("cover", [fr], onPage=on_cover), PageTemplate("body", [fr], onPageEnd=B.on_body),
                               PageTemplate("twocol", [left, right], onPageEnd=B.on_body)])
        self.chapter = None
        self.default_header = f"Assessment book  ·  Class {CLASS}"
        self.footer_note = "Assessment book · photocopiable for classroom use"


def build():
    check_tests()
    story = [Spacer(1, 1)]
    story += contents_page()
    story += about_page()
    for ch in CH:
        story += test_story(ch)
    story += answer_key()
    story += record_sheet()
    doc = AssessDoc(OUT)
    doc.multiBuild(story)
    print("built", OUT)


if __name__ == "__main__":
    build()
