"""Build a 'Think Like a Coder' class workbook (CodeSchool sample edition) as a PDF.

Usage: python -P -E docs/books/tools/build_book.py <class number> [out.pdf]
Content comes from docs/books/class<N>/content.py (CH, FACTS, META).
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak,
                                KeepTogether, NextPageTemplate, Flowable, CondPageBreak)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.graphics.shapes import Drawing, Rect, Circle, Line, String, Polygon, PolyLine

import figures as F
import importlib.util

BOOKS = pathlib.Path(__file__).resolve().parents[1]
CLASS = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 3
_spec = importlib.util.spec_from_file_location(f"content_class{CLASS}", BOOKS / f"class{CLASS}" / "content.py")
_content = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_content)
CH, FACTS, META = _content.CH, _content.FACTS, _content.META
PROJECTS = getattr(_content, "PROJECTS", [])  # optional project units (Classes 6-8)


def ch_label(ch):
    return ch.get("toc", f"{ch['n']}. {ch['title']}")


def ch_badge(ch):
    return ch.get("badge", str(ch["n"]))


def ch_short(ch):
    return ch.get("short", f"Ch {ch['n']}")

FONTS = pathlib.Path("C:/Windows/Fonts")
for name, fn in [("Kid", "segoeui.ttf"), ("KidB", "segoeuib.ttf"), ("KidBl", "seguibl.ttf"), ("KidI", "segoeuii.ttf"),
                 ("Fun", "segoeprb.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(FONTS / fn)))
pdfmetrics.registerFontFamily("Kid", normal="Kid", bold="KidB", italic="KidI", boldItalic="KidB")

_args = [a for a in sys.argv[1:] if not a.isdigit()]
OUT = _args[0] if _args and __name__ == "__main__" else str(BOOKS / f"CodeSchool-Class{CLASS}-Think-Like-a-Coder.pdf")
PW, PH = A4
LM = RM = 40
TM, BM = 62, 52
CW = PW - LM - RM
C = colors.HexColor
INK, SOFT = C("#1F2A44"), C("#5B6577")


def tint(hexcol, f=0.86):
    c = C(hexcol)
    return colors.Color(c.red + (1 - c.red) * f, c.green + (1 - c.green) * f, c.blue + (1 - c.blue) * f)


S = {
    "body": ParagraphStyle("body", fontName="Kid", fontSize=11.5, leading=16, textColor=INK, spaceAfter=4),
    "q": ParagraphStyle("q", fontName="Kid", fontSize=12, leading=16.5, textColor=INK),
    "small": ParagraphStyle("small", fontName="Kid", fontSize=9, leading=12, textColor=SOFT),
    "h": ParagraphStyle("h", fontName="KidBl", fontSize=17, leading=21, textColor=INK),
    "boxtitle": ParagraphStyle("bt", fontName="KidBl", fontSize=13, leading=16, textColor=colors.white),
    "say": ParagraphStyle("say", fontName="KidB", fontSize=11.5, leading=15.5, textColor=INK),
    "word": ParagraphStyle("word", fontName="KidB", fontSize=10, leading=12.5, textColor=INK),
    "toc0": ParagraphStyle("toc0", fontName="KidB", fontSize=12, leading=17.5, textColor=INK, leftIndent=0),
    "ans": ParagraphStyle("ans", fontName="Kid", fontSize=9.5, leading=12.5, textColor=INK),
    "ansh": ParagraphStyle("ansh", fontName="KidBl", fontSize=11, leading=14, textColor=INK, spaceBefore=6),
}


# ------------------------------------------------------------------ small building blocks
def P(t, st="body", **kw):
    return Paragraph(t, ParagraphStyle("x", parent=S[st], **kw) if kw else S[st])


def pill(text, bg, fg=colors.white, size=10, pad=5):
    w = pdfmetrics.stringWidth(text, "KidB", size) + 2 * pad + 4
    d = Drawing(w, size + 2 * pad)
    d.add(Rect(0, 0, w, size + 2 * pad, rx=(size + 2 * pad) / 2, ry=(size + 2 * pad) / 2, fillColor=bg, strokeColor=None))
    d.add(String(w / 2, pad + 1.5, text, fontName="KidB", fontSize=size, fillColor=fg, textAnchor="middle"))
    return d


def box(content, color, title=None, icon=None, pad=10):
    """Rounded coloured panel with an optional title tab."""
    rows = []
    if title:
        head = Table([[icon or "", P(title, "boxtitle")]], colWidths=[26 if icon else 0.1, None])
        head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
        rows.append([head])
    rows.append([content])
    t = Table(rows, colWidths=[CW])
    st = [("LEFTPADDING", (0, 0), (-1, -1), pad), ("RIGHTPADDING", (0, 0), (-1, -1), pad), ("TOPPADDING", (0, 0), (-1, -1), 6),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 8), ("BACKGROUND", (0, 0), (-1, -1), tint(color, 0.88)), ("ROUNDEDCORNERS", [10, 10, 10, 10]),
          ("BOX", (0, 0), (-1, -1), 1.2, C(color))]
    if title:
        st += [("BACKGROUND", (0, 0), (-1, 0), C(color)), ("TOPPADDING", (0, 0), (-1, 0), 5), ("BOTTOMPADDING", (0, 0), (-1, 0), 5)]
    t.setStyle(TableStyle(st))
    return t


def icon(kind, color="#FFFFFF", size=20):
    d = Drawing(size, size)
    c = C(color)
    if kind == "bulb":
        d.add(Circle(10, 12, 6.5, fillColor=c, strokeColor=None)); d.add(Rect(7, 2, 6, 4, fillColor=c, strokeColor=None))
    elif kind == "eye":
        d.add(PolyLine([1, 10, 6, 15, 14, 15, 19, 10, 14, 5, 6, 5, 1, 10], strokeColor=c, strokeWidth=2)); d.add(Circle(10, 10, 3, fillColor=c, strokeColor=None))
    elif kind == "pencil":
        d.add(Polygon([3, 3, 3, 8, 14, 19, 19, 14, 8, 3], fillColor=c, strokeColor=None))
    elif kind == "blocks":
        d.add(Rect(2, 2, 8, 8, fillColor=c, strokeColor=None)); d.add(Rect(11, 2, 8, 8, fillColor=c, strokeColor=None)); d.add(Rect(6.5, 11, 8, 8, fillColor=c, strokeColor=None))
    elif kind == "star":
        d.add(F.shape("star", 10, 10, 9, c, None))
    elif kind == "check":
        d.add(PolyLine([3, 10, 8, 4, 17, 16], strokeColor=c, strokeWidth=3))
    return d


def number_badge(n, color):
    d = Drawing(24, 24)
    d.add(Circle(12, 12, 11, fillColor=C(color), strokeColor=None))
    d.add(String(12, 7.5, str(n), fontName="KidBl", fontSize=12, fillColor=colors.white, textAnchor="middle"))
    return d


def answer_boxes(n, w=58, h=28):
    d = Drawing(n * (w + 10), h + 4)
    for i in range(n):
        d.add(Rect(2 + i * (w + 10), 2, w, h, rx=6, ry=6, fillColor=colors.white, strokeColor=C("#9AA5B8"), strokeWidth=1.2))
    return d


def lines(n, w=None):
    w = w or CW - 50
    d = Drawing(w, n * 24 + 2)
    for i in range(n):
        d.add(Line(0, 4 + i * 24, w, 4 + i * 24, strokeColor=C("#B8C2D3"), strokeWidth=1, strokeDashArray=[2, 3]))
    return d


def options(opts, color):
    cells = []
    for i, o in enumerate(opts):
        cells.append(P(f"<font name='KidBl' color='{color}'>{chr(97 + i)})</font>&nbsp; {o}", "q", fontSize=11))
    n = len(opts)
    per = 4 if max(len(o) for o in opts) < 16 else 2
    rows = [cells[i:i + per] + [""] * (per - len(cells[i:i + per])) for i in range(0, n, per)]
    t = Table(rows, colWidths=[(CW - 50) / per] * per)
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    return t


def data_table(rows, color, blanks=True, widths=None):
    t = Table([[P(c, "q", fontName="KidB" if i == 0 else "Kid", fontSize=10.5) for c in r] for i, r in enumerate(rows)],
              colWidths=widths or [60, 170, 90])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.8, C("#B8C2D3")), ("BACKGROUND", (0, 0), (-1, 0), tint(color, 0.7)),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white]), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return t


def card_kind_color(kind, default):
    return {"loop": "#F5A524", "if": "#8B5CF6", "event": "#E5484D"}.get(kind, default)


def code_cards(cards):
    ds = []
    for label, kind, col in cards:
        k = kind if kind in ("up", "down", "left", "right") else "step"
        w = max(70, pdfmetrics.stringWidth(label, "KidB", 10) + (42 if k != "step" else 24))
        ds.append(F.code_card(label, k, w=w, h=30, color=C(card_kind_color(kind, col))))
    rows, row, used = [], [], 0
    for d in ds:
        if used + d.width + 8 > CW - 30 and row:
            rows.append(row); row, used = [], 0
        row.append(d); used += d.width + 8
    if row: rows.append(row)
    out = []
    for r in rows:
        t = Table([r], colWidths=[d.width + 8 for d in r], hAlign="LEFT")
        t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
        out.append(t)
    return out


class IfFits(Flowable):
    """Draws its content only if it fits in the space left on the page; otherwise takes no space."""
    def __init__(self, content):
        super().__init__(); self.content = content; self._h = 0
    def wrap(self, aw, ah):
        w, h = self.content.wrap(aw, ah)
        self._h = h if h <= ah else 0
        return aw, self._h
    def split(self, aw, ah):
        return []
    def draw(self):
        if self._h:
            self.content.drawOn(self.canv, 0, 0)


class TocMark(Flowable):
    """Adds a contents entry and bookmark for back-matter pages."""
    def __init__(self, text, key):
        super().__init__(); self.text, self.key = text, key; self.width = self.height = 0
    def wrap(self, *a):
        return 0, 0
    def draw(self):
        self.canv.bookmarkPage(self.key); self.canv.addOutlineEntry(self.text, self.key, level=0)
        self.canv._doctemplate.notify("TOCEntry", (0, self.text, self.canv.getPageNumber(), self.key))


class SetChapter(Flowable):
    """Zero-size marker that tells the page decorations which chapter we are in."""
    def __init__(self, ch):
        super().__init__(); self.ch = ch; self.width = self.height = 0
    def wrap(self, *a):
        return 0, 0
    def draw(self):
        self.canv._doctemplate.chapter = self.ch


class Banner(Flowable):
    def __init__(self, ch):
        super().__init__(); self.ch = ch; self.width = CW; self.height = 112
    def wrap(self, *a):
        return CW, self.height
    def draw(self):
        c = self.canv; ch = self.ch; col = C(ch["color"])
        c.saveState()
        c.setFillColor(col); c.roundRect(0, 0, CW, self.height, 16, stroke=0, fill=1)
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.14))
        for x, y, r in ((CW - 140, 96, 26), (CW - 60, 18, 18), (40, 104, 12), (300, 6, 14)):
            c.circle(x, y, r, stroke=0, fill=1)
        c.setFillColor(colors.white); c.circle(52, 56, 34, stroke=0, fill=1)
        bd = ch_badge(ch); bs = 30 if len(bd) <= 2 else 22
        c.setFillColor(col); c.setFont("KidBl", bs); c.drawCentredString(52, 56 - bs * 0.36, bd)
        c.setFillColor(colors.white); c.setFont("KidB", 10); c.drawString(100, 86, ch.get("kicker", f"CHAPTER {ch['n']}") + f"  ·  LEVEL {ch['level']}")
        title = ch["title"]; size = 26
        while pdfmetrics.stringWidth(title, "KidBl", size) > CW - 215 and size > 14:  # shrink long titles to clear Robo
            size -= 1
        c.setFont("KidBl", size); c.drawString(100, 54, title)
        skill = ch.get("skill_prefix", "Coder skill: ") + ch["skill"]; ssize = 11.5
        while pdfmetrics.stringWidth(skill, "KidB", ssize) > CW - 215 and ssize > 8:  # shrink long skill lines to clear Robo
            ssize -= 0.5
        c.setFont("KidB", ssize); c.drawString(100, 30, skill)
        c.setFont("Kid", 9); c.drawString(100, 13, ch.get("source", f"Goes with {META['textbook_short']}, chapter {ch['n']}"))
        c.restoreState()
        r = F.robo(70, color=C("#FFFFFF") if False else F.YELLOW, wave=True)
        r.drawOn(c, CW - 86, 18)
        self.canv._doctemplate.notify("TOCEntry", (0, ch_label(ch), self.canv.getPageNumber(), f"ch{ch['n']}"))
        c.bookmarkPage(f"ch{ch['n']}"); c.addOutlineEntry(ch_label(ch), f"ch{ch['n']}", level=0)


def robo_says(text, color):
    bubble = Table([[P(text, "say")]], colWidths=[CW - 110])
    bubble.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.white), ("BOX", (0, 0), (-1, -1), 1.4, C(color)),
                                ("ROUNDEDCORNERS", [12, 12, 12, 12]), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                                ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    t = Table([[F.robo(58, color=C(color)), bubble]], colWidths=[80, CW - 90])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    return t


def word_chips(words, color):
    cells = [P(f"<font color='{color}'><b>{w}</b></font><br/><font size='8.5' color='#5B6577'>{m}</font>", "word") for w, m in words]
    t = Table([cells], colWidths=[(CW - 24) / len(cells)] * len(cells))
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.white), ("BOX", (0, 0), (-1, -1), 0.8, C(color)),
                           ("INNERGRID", (0, 0), (-1, -1), 0.8, tint(color, 0.5)), ("ROUNDEDCORNERS", [8, 8, 8, 8]),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LEFTPADDING", (0, 0), (-1, -1), 8)]))
    return t


def question(i, q, color):
    parts = [P(q["q"], "q")]
    if q.get("fig"):
        parts += [Spacer(1, 4), q["fig"](), Spacer(1, 2)]
    if q.get("table"):
        parts += [Spacer(1, 4), data_table(q["table"], color)]
    if q.get("opts"):
        parts += [Spacer(1, 3), options(q["opts"], color)]
    if q.get("boxes"):
        parts += [Spacer(1, 4), answer_boxes(q["boxes"])]
    if q.get("lines"):
        parts += [Spacer(1, 6), lines(q["lines"])]
    t = Table([[number_badge(i, color), parts]], colWidths=[34, CW - 34])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 2),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 9), ("LINEBELOW", (0, 0), (-1, -1), 0.6, tint(color, 0.6))]))
    return KeepTogether([t])


def section_head(text, color, ic):
    t = Table([[icon(ic, color, 22), P(text, "h", textColor=C(color))]], colWidths=[30, CW - 30])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return t


def ican(items, color):
    cells = []
    for it in items:
        d = Drawing(150, 40)
        for k, fc in enumerate(["#2BB673", "#F5A524", "#E5484D"]):
            x = 12 + k * 26
            d.add(Circle(x, 26, 9, fillColor=colors.white, strokeColor=C(fc), strokeWidth=1.6))
            d.add(Circle(x - 3, 28, 1.2, fillColor=C(fc))); d.add(Circle(x + 3, 28, 1.2, fillColor=C(fc)))
            mouth = [x - 4, 23, x, 21, x + 4, 23] if k == 0 else ([x - 4, 22.5, x + 4, 22.5] if k == 1 else [x - 4, 21, x, 23, x + 4, 21])
            d.add(PolyLine(mouth, strokeColor=C(fc), strokeWidth=1.2))
        cells.append([P("I can " + it + ".", "word", fontSize=10), d])
    t = Table([cells], colWidths=[CW / 3 - 6] * 3)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (-1, -1), colors.white), ("BOX", (0, 0), (-1, -1), 1, C(color)),
                           ("INNERGRID", (0, 0), (-1, -1), 0.6, tint(color, 0.5)), ("ROUNDEDCORNERS", [10, 10, 10, 10]), ("TOPPADDING", (0, 0), (-1, -1), 6)]))
    return t


# ------------------------------------------------------------------ chapter
def example_box(ex, col, title="Example"):
    exs = [P(f"<b>{ex['title']}</b>", "q")]
    for k, st in enumerate(ex["steps"], 1):
        exs.append(P(f"<font name='KidBl' color='{col}'>{k}.</font>&nbsp; {st}", "body", leftIndent=14, firstLineIndent=-14))
    if ex.get("fig"):
        exs += [Spacer(1, 6), ex["fig"]()]
    if ex.get("table"):
        exs += [Spacer(1, 6), data_table(ex["table"], col, widths=ex.get("widths"))]
    return box(exs, "#F5A524" if col != "#F5A524" else "#E5484D", title, icon("eye"))


def tickbox(size=14):
    d = Drawing(size + 2, size + 2)
    d.add(Rect(1, 1, size, size, rx=3, ry=3, fillColor=colors.white, strokeColor=C("#9AA5B8"), strokeWidth=1.2))
    return d


def score_dots(n=4, color="#14A3A3"):
    d = Drawing(n * 17, 16)
    for k in range(n):
        d.add(Circle(8 + k * 17, 8, 7, fillColor=colors.white, strokeColor=C(color), strokeWidth=1.2))
        d.add(String(8 + k * 17, 5, str(k + 1), fontName="KidB", fontSize=7.5, fillColor=C(color), textAnchor="middle"))
    return d


def drawspace(h, w=CW - 30):
    d = Drawing(w, h + 2)
    d.add(Rect(0, 0, w, h, rx=10, ry=10, fillColor=colors.white, strokeColor=C("#B8C2D3"), strokeDashArray=[4, 3]))
    return d


def grid_table(header, rows, widths, color, blank_rows=0, row_h=None, font=10):
    data = [[P(f"<b>{c}</b>", "q", fontSize=font, leading=font + 3) for c in header]]
    data += [[P(str(c), "q", fontSize=font, leading=font + 3) for c in r] for r in rows]
    data += [[""] * len(header) for _ in range(blank_rows)]
    t = Table(data, colWidths=widths, rowHeights=None if row_h is None else [None] + [row_h] * (len(data) - 1))
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.8, C("#B8C2D3")), ("BACKGROUND", (0, 0), (-1, 0), tint(color, 0.7)),
                           ("BACKGROUND", (0, 1), (-1, -1), colors.white), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return t


def project_story(p):
    """A 20-hour project unit: brief, plan, worked example, data sheet, design space, rubric and reflection."""
    col = p["color"]
    s = [NextPageTemplate("body"), PageBreak(), SetChapter(p), Banner(p), Spacer(1, 10)]
    big = [P(p["question"], "q", fontName="KidBl", fontSize=13.5, leading=18, textColor=C(col)), Spacer(1, 4)] + [P(t) for t in p["brief"]]
    big += [Spacer(1, 4), word_chips(p["words"], col)]
    s += [box(big, col, "The big question", icon("bulb")), Spacer(1, 10)]
    rows = [[P("<b>Weeks</b>", "small"), P("<b>Stage</b>", "small"), P("<b>What I do</b>", "small"), P("<b>Done</b>", "small")]]
    for wk, stage, what in p["plan"]:
        rows.append([P(wk, "q", fontSize=10), P(f"<font color='{col}'><b>{stage}</b></font>", "q", fontSize=10.5),
                     P(what, "body", fontSize=10, leading=13, spaceAfter=0), tickbox()])
    t = Table(rows, colWidths=[52, 96, CW - 52 - 96 - 40, 40])
    t.setStyle(TableStyle([("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, C("#F3F6FB")]), ("LINEBELOW", (0, 0), (-1, 0), 1, C(col)),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                           ("ALIGN", (3, 0), (3, -1), "CENTER")]))
    s += [KeepTogether([section_head("My project plan", col, "check"), t])]
    # worked example and data sheet
    s += [NextPageTemplate("body"), PageBreak(), example_box(p["example"], col, "How a coder does it"), Spacer(1, 10)]
    sh = p["sheet"]
    n = len(sh["header"])
    widths = sh.get("widths", [CW / n] * n)
    s += [KeepTogether([section_head(sh["title"], col, "pencil"), P(sh["intro"], "small"), Spacer(1, 4),
                        grid_table(sh["header"], sh.get("rows", []), widths, col, sh.get("blank", 6), sh.get("row_h", 20))])]
    for d in p.get("draw", []):
        s += [Spacer(1, 10), KeepTogether([box([P(d["text"]), Spacer(1, 6), drawspace(d.get("h", 150))], "#2BB673", d["title"], icon("blocks"))])]
    # rubric, fairness and reflection
    s += [NextPageTemplate("body"), PageBreak(), robo_says(p["robo"], col), Spacer(1, 8), section_head("How good is my project?", col, "star"),
          P("Score each row from 1 (just starting) to 4 (excellent). Then your teacher scores it too. Talk about any row where the scores differ.", "small"), Spacer(1, 4)]
    rows = [[P("<b>What we check</b>", "small"), P("<b>What excellent (4) looks like</b>", "small"), P("<b>Me</b>", "small"), P("<b>Teacher</b>", "small")]]
    for crit, good in p["rubric"]:
        rows.append([P(f"<b>{crit}</b>", "q", fontSize=10.5, leading=13), P(good, "body", fontSize=10, leading=13, spaceAfter=0), score_dots(4, col), score_dots(4, "#5B6577")])
    t = Table(rows, colWidths=[112, CW - 112 - 152, 76, 76])
    t.setStyle(TableStyle([("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, C("#F3F6FB")]), ("LINEBELOW", (0, 0), (-1, 0), 1, C(col)),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    s += [t, Spacer(1, 10)]
    fair = [Table([[tickbox(), P(q, "body", spaceAfter=0)]], colWidths=[24, CW - 24 - 28],
                  style=[("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]) for q in p["ethics"]]
    s += [KeepTogether([box(fair, "#8B5CF6", "Fair, safe and honest?", icon("check"))]), Spacer(1, 10)]
    refl = []
    for q in p["reflect"]:
        refl += [P(q, "q"), lines(2, CW - 30)]
    s += [KeepTogether([box(refl, "#14A3A3", "Looking back", icon("pencil"))])]
    return s


def chapter_story(ch):
    col = ch["color"]
    s = [NextPageTemplate("body"), PageBreak(), SetChapter(ch), Banner(ch), Spacer(1, 10)]
    learn = [P(t) for t in ch["learn"]] + [Spacer(1, 6), word_chips(ch["words"], col)]
    s += [box(learn, col, "Learn", icon("bulb")), Spacer(1, 8), robo_says(ch["robo"], col), Spacer(1, 8)]
    s += [KeepTogether([example_box(ch["example"], col)])]
    fact = Table([[icon("star", "#F5A524", 26), P(f"<font name='Fun' color='{col}'>Coder fact!</font>&nbsp; " + FACTS[ch["n"]], "body")]], colWidths=[34, CW - 44])
    fact.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("BACKGROUND", (0, 0), (-1, -1), colors.white), ("BOX", (0, 0), (-1, -1), 1.2, C("#F5A524")),
                              ("ROUNDEDCORNERS", [12, 12, 12, 12]), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    s += [IfFits(Table([[Spacer(1, 12)], [fact]], colWidths=[CW], style=[("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))]
    # practice
    s += [NextPageTemplate("body"), PageBreak(), section_head("Try it!", col, "pencil"),
          P("Circle the right answer, or write it in the box.", "small"), Spacer(1, 6)]
    for i, q in enumerate(ch["practice"], 1):
        s.append(question(i, q, col))
    # build + challenge + I can
    b = ch["build"]
    bs = [P(b["intro"])]
    if b.get("fig"):
        bs += [Spacer(1, 4), b["fig"]()]
    bs += [Spacer(1, 6)] + code_cards(b["cards"]) + [Spacer(1, 6), P(b["task"])]
    if b.get("drawspace"):
        d = Drawing(CW - 30, 90); d.add(Rect(0, 0, CW - 30, 88, rx=10, ry=10, fillColor=colors.white, strokeColor=C("#B8C2D3"), strokeDashArray=[4, 3])); bs += [Spacer(1, 6), d]
    else:
        bs += [Spacer(1, 6), lines(3, CW - 30)]
    s += [CondPageBreak(230), Spacer(1, 6), KeepTogether([box(bs, "#2BB673", "Now you build it", icon("blocks"))]), Spacer(1, 10)]
    chs = [P(ch["challenge"]["q"], "q"), Spacer(1, 6), lines(2, CW - 30)]
    s += [KeepTogether([box(chs, "#8B5CF6", "Challenge", icon("star"))]), Spacer(1, 10)]
    s += [KeepTogether([section_head("How did I do?", col, "check"), ican(ch["ican"], col)])]
    return s


# ------------------------------------------------------------------ page decorations
def on_body(c, doc):
    ch = getattr(doc, "chapter", None)
    col = C(ch["color"]) if ch else C("#14A3A3")
    c.saveState()
    c.setFillColor(tint(ch["color"] if ch else "#14A3A3", 0.82)); c.roundRect(LM - 10, PH - 44, CW + 20, 26, 13, stroke=0, fill=1)
    c.setFillColor(col); c.setFont("KidB", 9.5)
    c.drawString(LM, PH - 34, ch.get("header", f"Chapter {ch['n']}  ·  {ch['title']}") if ch else getattr(doc, "default_header", "Think Like a Coder"))
    c.setFont("Kid", 9); c.drawRightString(PW - RM, PH - 34, f"Think Like a Coder  ·  Class {CLASS}")
    c.setFillColor(col); c.circle(PW / 2, 26, 12, stroke=0, fill=1)
    c.setFillColor(colors.white); c.setFont("KidBl", 10); c.drawCentredString(PW / 2, 22.5, str(doc.page))
    c.setFillColor(SOFT); c.setFont("Kid", 7)
    c.drawString(LM, 22, getattr(doc, "footer_note", "CodeSchool sample edition · draft for review"))
    c.drawRightString(PW - RM, 22, "© 2026 Bullseye Knowledge System Limited")
    c.restoreState()


def on_cover(c, doc):
    c.saveState()
    c.setFillColor(C("#14A3A3")); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    c.setFillColor(C("#0E7C7C")); c.rect(0, 0, PW, PH * 0.30, stroke=0, fill=1)
    # playful shapes
    for x, y, r, colr in ((470, 700, 30, "#FFD23F"), (530, 800, 22, "#EC4899"), (548, 590, 46, "#F5A524"), (70, 470, 26, "#8B5CF6"),
                          (540, 360, 30, "#2BB673"), (110, 380, 14, "#FFD23F"), (330, 815, 12, "#ffffff")):
        c.setFillColor(C(colr)); c.circle(x, y, r, stroke=0, fill=1)
    c.setFillColor(C("#FFFFFF")); c.setFont("KidB", 13); c.drawString(LM + 10, PH - 70, f"CodeSchool  ·  Class {CLASS}")
    c.setFont("KidBl", 54); c.drawString(LM + 10, PH - 150, "Think Like")
    c.drawString(LM + 10, PH - 208, "a Coder")
    tag = META.get("cover_tag", f"Computational thinking for Class {CLASS}"); ts = 22
    while pdfmetrics.stringWidth(tag, "Fun", ts) > 440 and ts > 14:  # keep clear of the orange circle
        ts -= 0.5
    c.setFillColor(C("#FFD23F")); c.setFont("Fun", ts); c.drawString(LM + 14, PH - 246, tag)
    c.setFillColor(colors.white); c.setFont("Kid", 13)
    c.drawString(LM + 14, PH - 274, "Learn it  ·  See it  ·  Try it  ·  Build it")
    r = F.robo(230, color=F.YELLOW, wave=True)
    r.drawOn(c, PW - 300, 250)
    # code cards row
    x = LM + 10
    for lab, k, colr in META.get("cover_cards", (("Start", "step", F.BLUE), ("Repeat 3 times", "step", F.ORANGE), ("move", "right", F.BLUE), ("If dry, water", "step", F.PURPLE))):
        w = pdfmetrics.stringWidth(lab, "KidB", 10) + (42 if k != "step" else 26)
        d = F.code_card(lab, k, w=w, h=30, color=colr); d.drawOn(c, x, 300); x += w + 8
    c.setFillColor(colors.white); c.setFont("KidB", 12)
    c.drawString(LM + 10, 190, META["cover_follows"])
    c.setFont("Kid", 11)
    c.drawString(LM + 10, 170, "Built for CBSE's Computational Thinking and AI curriculum, 2026-27")
    c.drawString(LM + 10, 152, META.get("cover_line", "Theory, worked examples, practice, coding on paper and challenges"))
    c.setFillColor(C("#FFD23F")); c.roundRect(LM + 10, 92, 196, 30, 15, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont("KidB", 11); c.drawCentredString(LM + 108, 102, "SAMPLE EDITION  ·  DRAFT")
    c.setFillColor(colors.white); c.setFont("Kid", 8.5)
    c.drawString(LM + 10, 52, "© 2026 Bullseye Knowledge System Limited. All rights reserved.")
    c.drawString(LM + 10, 40, "CodeSchool is a working name. Not an official CBSE or NCERT publication.")
    c.restoreState()


# ------------------------------------------------------------------ front and back matter
def front_matter():
    s = [NextPageTemplate("body"), PageBreak()]
    s += [Spacer(1, 4), robo_says(META.get("welcome", "Hello! I am <b>Robo</b>. I think like a coder, and soon you will too! In this book we will solve puzzles, crack secret codes, guide robots and write programs, all on paper."), "#14A3A3"), Spacer(1, 12)]
    s += [P("How this book works", "h"), Spacer(1, 6)]
    parts = [("Learn", "bulb", "#14A3A3", "Robo explains one big idea in simple words, with the new coder words to remember."),
             ("Example", "eye", "#F5A524", "A worked example shows the idea step by step."),
             ("Try it!", "pencil", "#3B82F6", "Five practice questions. Circle the answer or write it in the box."),
             ("Now you build it", "blocks", "#2BB673", "Coding on paper: put code cards in order, fix bugs and write your own programs."),
             ("Challenge", "star", "#8B5CF6", "A harder puzzle for when you are ready for more."),
             ("How did I do?", "check", "#E5484D", "Colour a face to show how sure you feel.")]
    if PROJECTS:
        parts.append(("Projects", "bulb", "#EC4899", META.get("projects_note", "Longer projects over several weeks: plan, collect data, build, test and present.")))
    rows = []
    for name, ic, col, desc in parts:
        badge = Table([[icon(ic, "#FFFFFF", 20), P(name, "boxtitle", fontSize=11.5)]], colWidths=[24, 116])
        badge.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), C(col)), ("ROUNDEDCORNERS", [8, 8, 8, 8]), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                   ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
        rows.append([badge, P(desc)])
    t = Table(rows, colWidths=[160, CW - 160])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("BOTTOMPADDING", (0, 0), (-1, -1), 8), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    s += [t, Spacer(1, 10), P("My code cards", "h"), Spacer(1, 4),
          P("Coders use cards like these. Each colour means something different. You will find cut-out cards at the back of the book.")]
    s += code_cards(META.get("front_cards", [("Step: do this", "step", "#3B82F6"), ("Repeat: a loop", "loop", "#F5A524"), ("If: a decision", "if", "#8B5CF6"),
                     ("When: an event", "event", "#E5484D"), ("move", "right", "#3B82F6")]))
    s += [Spacer(1, 12), box([P(META.get("chapters_note", f"Each chapter goes with the same chapter of {META['textbook_long']}, so it can be used in maths periods. ")
                                + META.get("hours_note", "CBSE suggests about 50 hours of computational thinking a year in Classes 3-5. The coding here needs no computer: "
                                "children act out, write and check programs on paper, which builds the same ideas used later in block coding and AI. ") +
                                "Answers are at the back. Encourage children to explain their thinking, not just the answer.")],
                             "#5B6577", "For teachers and parents")]
    # contents
    toc = TableOfContents(); toc.dotsMinLevel = 0
    n_entries = len(CH) + len(PROJECTS) + 3  # chapters, projects, answers, words, cards
    toc.levelStyles = [S["toc0"] if n_entries <= 18 else ParagraphStyle("toc0s", parent=S["toc0"], leading=14.5)]
    def cells(ch):
        return [P(f"<font color='{ch['color']}'><b>{ch_badge(ch)}</b></font>", "q", fontSize=10), P(ch["skill"], "body", fontSize=9.5, leading=12, spaceAfter=0), P(ch["level"], "small", fontSize=8)]
    hdr = [P("<b>Ch</b>", "small"), P("<b>Coder skill</b>", "small"), P("<b>Level</b>", "small")]
    skills = [hdr + hdr]
    units = CH + PROJECTS
    half_n = (len(units) + 1) // 2  # two columns; works for any number of chapters
    for i in range(half_n):
        right = cells(units[i + half_n]) if i + half_n < len(units) else ["", "", ""]
        skills.append(cells(units[i]) + right)
    half = (CW - 12) / 2
    st = Table(skills, colWidths=[28, half - 70, 42, 28, half - 70, 42])
    st.setStyle(TableStyle([("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, C("#F3F6FB")]), ("LINEBELOW", (0, 0), (-1, 0), 1, C("#14A3A3")),
                            ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]))
    s += [NextPageTemplate("body"), PageBreak(), P("What's inside", "h", fontSize=24, leading=30), Spacer(1, 4), toc, Spacer(1, 10),
          P("Coder skills in this book", "h"), P(META["levels_note"], "small"), Spacer(1, 4), st]
    return s


def back_matter():
    s = [NextPageTemplate("twocol"), PageBreak(), SetChapter(None)]
    s += [TocMark("Answers", "answers"), P("Answers", "h", fontSize=24, leading=30), P("Many questions have more than one good answer. Accept any answer that follows the rule and can be explained.", "small"), Spacer(1, 6)]
    blocks = []
    for ch in CH:
        items = [P(f"<font color='{ch['color']}'>{ch_label(ch)}</font>", "ansh")]
        for i, q in enumerate(ch["practice"], 1):
            items.append(P(f"<b>{i}.</b> {q['answer']}", "ans"))
        items.append(P(f"<b>Build it:</b> {ch['build']['answer']}", "ans"))
        items.append(P(f"<b>Challenge:</b> {ch['challenge']['answer']}", "ans"))
        blocks.append(items)
    for p in PROJECTS:
        if p.get("answer"):
            blocks.append([P(f"<font color='{p['color']}'>{ch_label(p)}</font>", "ansh"), P(p["answer"], "ans")])
    for b in blocks:
        s += [KeepTogether(b)]
    s += [NextPageTemplate("body")]
    # glossary
    s += [NextPageTemplate("body"), PageBreak(), TocMark("Coder words", "words"), P("Coder words", "h", fontSize=24, leading=30), Spacer(1, 6)]
    seen, rows = set(), []
    for ch in CH + PROJECTS:
        for w, m in ch["words"]:
            if w not in seen:
                seen.add(w); rows.append((w, m, ch_short(ch)))
    rows.sort(key=lambda r: r[0].lower())
    t = Table([[P(f"<b>{w}</b>", "q", fontSize=10.5, leading=13), P(m, "body", fontSize=10.5, leading=13, spaceAfter=0), P(n, "small")] for w, m, n in rows], colWidths=[150, CW - 210, 60])
    t.setStyle(TableStyle([("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, C("#F3F6FB")]), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("ROUNDEDCORNERS", [8, 8, 8, 8])]))
    s += [t]
    # cut-out cards
    s += [NextPageTemplate("body"), PageBreak(), TocMark("Cut-out code cards", "cards"), P("Cut-out code cards", "h", fontSize=24, leading=30),
          P("Ask an adult to help you cut along the dotted lines. Use the cards to build programs on your desk, then act them out with a friend.", "small"), Spacer(1, 8)]
    cards = META.get("cutout_cards", [("up", "up"), ("down", "down"), ("left", "left"), ("right", "right"), ("Start", "step"), ("Repeat ___ times", "loop"),
             ("If ___", "if"), ("else", "if"), ("When ___ happens", "event"), ("add ___", "step"), ("take away ___", "step"), ("Stop", "step")])
    cells = []
    for lab, kind in cards:
        k = kind if kind in ("up", "down", "left", "right") else "step"
        cells.append(F.code_card(lab, k, w=150, h=46, color=C(card_kind_color(kind, "#3B82F6"))))
    rows = [cells[i:i + 3] for i in range(0, len(cells), 3)]
    rows = [r for r in rows for _ in range(2)]  # two of each
    t = Table(rows, colWidths=[CW / 3] * 3, rowHeights=[66] * len(rows))
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.9, C("#9AA5B8"), None, (4, 3)), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    s += [t]
    return s


class Doc(BaseDocTemplate):
    def __init__(self, fn):
        super().__init__(fn, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
                         title=f"Think Like a Coder - Class {CLASS} (CodeSchool sample edition)", author="CodeSchool, Bullseye Knowledge System Limited",
                         subject=f"Computational thinking workbook for Class {CLASS}")
        fr = Frame(LM, BM, CW, PH - TM - BM, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        gap = 18
        left = Frame(LM, BM, (CW - gap) / 2, PH - TM - BM, id="l", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        right = Frame(LM + (CW + gap) / 2, BM, (CW - gap) / 2, PH - TM - BM, id="r", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate("cover", [fr], onPage=on_cover), PageTemplate("body", [fr], onPageEnd=on_body),
                               PageTemplate("twocol", [left, right], onPageEnd=on_body)])
        self.chapter = None


def build():
    story = [Spacer(1, 1)]
    story += front_matter()
    for ch in CH:
        story += chapter_story(ch)
    for p in PROJECTS:
        story += project_story(p)
    story += back_matter()
    doc = Doc(OUT)
    doc.multiBuild(story)
    print("built", OUT)


if __name__ == "__main__":
    build()
