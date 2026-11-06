# Builds the CodeSchool research pack PDF (interactive: outline, clickable TOC,
# internal + external links, fillable AcroForm fields).
import re, sys, datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, Flowable, KeepTogether,
                                NextPageTemplate, CondPageBreak)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.pdfbase.pdfmetrics import stringWidth

OUT = sys.argv[1]
FONTS = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("UI", FONTS + r"\segoeui.ttf"))
pdfmetrics.registerFont(TTFont("UI-B", FONTS + r"\segoeuib.ttf"))
pdfmetrics.registerFont(TTFont("UI-I", FONTS + r"\segoeuii.ttf"))
pdfmetrics.registerFont(TTFont("UI-BI", FONTS + r"\segoeuiz.ttf"))
pdfmetrics.registerFont(TTFont("UI-SB", FONTS + r"\seguisb.ttf"))
pdfmetrics.registerFont(TTFont("Mono", FONTS + r"\consola.ttf"))
from reportlab.lib.fonts import addMapping
addMapping("UI", 0, 0, "UI"); addMapping("UI", 1, 0, "UI-B")
addMapping("UI", 0, 1, "UI-I"); addMapping("UI", 1, 1, "UI-BI")

# ---------- palette ----------
INK = colors.HexColor("#1F2933")
MUTED = colors.HexColor("#52606D")
PRIMARY = colors.HexColor("#0B5563")     # deep teal
PRIMARY_L = colors.HexColor("#E3F1F3")
ACCENT = colors.HexColor("#C2410C")      # burnt orange
ACCENT_L = colors.HexColor("#FDEFE6")
GOOD = colors.HexColor("#2F855A"); GOOD_L = colors.HexColor("#E6F4EC")
WARN = colors.HexColor("#B7791F"); WARN_L = colors.HexColor("#FDF5E1")
BAD = colors.HexColor("#C53030");  BAD_L = colors.HexColor("#FBE9E9")
RULE = colors.HexColor("#CBD2D9"); ZEBRA = colors.HexColor("#F5F7FA")
LINK = "#0B5563"

PAGE_W, PAGE_H = A4
LM = RM = 17 * mm; TM = 20 * mm; BM = 18 * mm
CW = PAGE_W - LM - RM

# ---------- styles ----------
def S(name, **kw):
    base = dict(fontName="UI", fontSize=9.6, leading=13.6, textColor=INK, spaceAfter=5)
    base.update(kw); return ParagraphStyle(name, **base)
BODY = S("body")
SMALL = S("small", fontSize=8.3, leading=11.2)
CELL = S("cell", fontSize=8.2, leading=10.8, spaceAfter=0)
CELLB = S("cellb", fontName="UI-B", fontSize=8.2, leading=10.8, spaceAfter=0)
HEADC = S("headc", fontName="UI-B", fontSize=8.2, leading=10.6, textColor=colors.white, spaceAfter=0)
BUL = S("bul", leftIndent=12, bulletIndent=2, spaceAfter=2.5)
BUL2 = S("bul2", leftIndent=24, bulletIndent=14, spaceAfter=2, fontSize=9.2, leading=12.8)
H1 = S("h1", fontName="UI-B", fontSize=21, leading=26, textColor=PRIMARY, spaceBefore=0, spaceAfter=4)
H1SUB = S("h1sub", fontName="UI", fontSize=10.5, leading=14.5, textColor=MUTED, spaceAfter=12)
H2 = S("h2", fontName="UI-B", fontSize=13.5, leading=17, textColor=INK, spaceBefore=12, spaceAfter=5, keepWithNext=1)
H3 = S("h3", fontName="UI-SB", fontSize=10.8, leading=14, textColor=PRIMARY, spaceBefore=8, spaceAfter=3, keepWithNext=1)
CODE = S("code", fontName="Mono", fontSize=8, leading=10.4, textColor=INK, spaceAfter=0)
TOC0 = S("toc0", fontName="UI-B", fontSize=10.5, leading=15, leftIndent=0, textColor=INK)
TOC1 = S("toc1", fontName="UI", fontSize=9.2, leading=12.6, leftIndent=14, textColor=MUTED)

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def md(s):
    """mini-markdown -> reportlab markup: **b**, _i_, `code`, [t](url|#anchor)."""
    links = []
    def grab(m):
        links.append((m.group(1), m.group(2)))
        return f"\x00{len(links) - 1}\x00"
    s = re.sub(r"\[([^\]]+?)\]\(([^)\s]+?)\)", grab, s)
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w/])_(.+?)_(?![\w])", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r'<font name="Mono">\1</font>', s)
    def put(m):
        t, u = links[int(m.group(1))]
        t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc(t))
        return f'<a href="{esc(u)}" color="{LINK}"><u>{t}</u></a>'
    s = re.sub(r"\x00(\d+)\x00", put, s)
    return s.replace("\n", "<br/>")

def P(s, st=BODY): return Paragraph(md(s), st)
def Praw(s, st=BODY): return Paragraph(s, st)
def bullets(items, st=BUL):
    out = []
    for it in items:
        if isinstance(it, (list, tuple)):
            out += [Paragraph(md(x), BUL2, bulletText="–") for x in it]
        else:
            out.append(Paragraph(md(it), st, bulletText="•"))
    return out

# ---------- headings with outline + TOC ----------
class Heading(Paragraph):
    def __init__(self, text, style, level, key, short=None):
        self.toc_level = level; self.key = key; self.short = short or text
        super().__init__(f'<a name="{key}"/>{md(text)}', style)

_h = {"n": 0}
def H(text, level=1, key=None, short=None):
    _h["n"] += 1
    key = key or f"h{_h['n']}"
    st = {0: H1, 1: H2, 2: H3}[level]
    return Heading(text, st, level, key, short)

def section(title, sub, key):
    return [NextPageTemplate("body"), PageBreak(), H(title, 0, key), P(sub, H1SUB)]

# ---------- boxes ----------
def callout(text_flows, kind="info", title=None):
    bg, bar = {"info": (PRIMARY_L, PRIMARY), "warn": (WARN_L, WARN), "risk": (BAD_L, BAD),
               "good": (GOOD_L, GOOD), "accent": (ACCENT_L, ACCENT)}[kind]
    flows = []
    if title: flows.append(Paragraph(f"<b>{esc(title)}</b>", S("ct", fontName="UI-B", textColor=bar, spaceAfter=3)))
    flows += text_flows if isinstance(text_flows, list) else [text_flows]
    t = Table([[flows]], colWidths=[CW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg),
                           ("LINEBEFORE", (0, 0), (0, -1), 3, bar),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 6)])

def tbl(rows, widths, header=True, zebra=True, font=CELL, first_bold=False, valign="TOP", extra=None):
    data = []
    for r_i, row in enumerate(rows):
        cells = []
        for c_i, c in enumerate(row):
            if isinstance(c, str):
                st = HEADC if (header and r_i == 0) else (CELLB if (first_bold and c_i == 0) else font)
                cells.append(Paragraph(md(c), st))
            else:
                cells.append(c)
        data.append(cells)
    t = Table(data, colWidths=[w * CW for w in widths], repeatRows=1 if header else 0)
    st = [("VALIGN", (0, 0), (-1, -1), valign),
          ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
          ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
          ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE)]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), PRIMARY)]
    if zebra:
        for i in range(1 if header else 0, len(data)):
            if (i % 2 == 0): st.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    if extra: st += extra
    t.setStyle(TableStyle(st))
    return t

# ---------- form fields ----------
FIELD_BORDER = colors.HexColor("#9AA5B1"); FIELD_FILL = colors.HexColor("#F7FBFC")
class FText(Flowable):
    def __init__(self, name, w, h=13, value="", multiline=False, tooltip=None, fs=8):
        super().__init__(); self.name, self.w, self.h, self.value = name, w, h, value
        self.multiline, self.tooltip, self.fs = multiline, tooltip or name, fs
    def wrap(self, aw, ah): return self.w, self.h
    def draw(self):
        self.canv.acroForm.textfield(name=self.name, tooltip=self.tooltip, value=self.value,
            x=0, y=0, width=self.w, height=self.h, relative=True, fontName="Helvetica", fontSize=self.fs,
            borderColor=FIELD_BORDER, fillColor=FIELD_FILL, textColor=INK, borderWidth=0.6,
            borderStyle="solid", forceBorder=True, maxlen=2000 if self.multiline else 300,
            fieldFlags="multiline" if self.multiline else "")

class FCheck(Flowable):
    def __init__(self, name, size=11, tooltip=None):
        super().__init__(); self.name, self.size, self.tooltip = name, size, tooltip or name
    def wrap(self, aw, ah): return self.size, self.size
    def draw(self):
        self.canv.acroForm.checkbox(name=self.name, tooltip=self.tooltip, x=0, y=0, size=self.size,
            relative=True, buttonStyle="check", borderColor=PRIMARY, fillColor=colors.white,
            textColor=PRIMARY, borderWidth=0.8, forceBorder=True, fieldFlags="")

class FChoice(Flowable):
    def __init__(self, name, options, w, h=13, value=None, tooltip=None):
        super().__init__(); self.name, self.options, self.w, self.h = name, options, w, h
        self.value = value or options[0]; self.tooltip = tooltip or name
    def wrap(self, aw, ah): return self.w, self.h
    def draw(self):
        self.canv.acroForm.choice(name=self.name, tooltip=self.tooltip, value=self.value,
            options=self.options, x=0, y=0, width=self.w, height=self.h, relative=True,
            fontName="Helvetica", fontSize=7.5, borderColor=FIELD_BORDER, fillColor=FIELD_FILL,
            textColor=INK, borderWidth=0.6, forceBorder=True, fieldFlags="combo")

def labeled_field(label, name, w_label=0.3, h=13, multiline=False, value=""):
    t = Table([[Paragraph(md(label), CELLB), FText(name, CW * (1 - w_label) - 10, h, value, multiline)]],
              colWidths=[CW * w_label, CW * (1 - w_label)])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 3)]))
    return t

# ---------- graphics ----------
def stat_tiles(items, cols=3):
    cells, row = [], []
    w = CW / cols
    for big, small, color in items:
        f = [Paragraph(f'<font color="{color}">{esc(big)}</font>', S("big", fontName="UI-B", fontSize=19, leading=23, spaceAfter=1)),
             Paragraph(md(small), S("bs", fontSize=8.2, leading=10.8, textColor=MUTED, spaceAfter=0))]
        row.append(f)
        if len(row) == cols: cells.append(row); row = []
    if row: cells.append(row + [""] * (cols - len(row)))
    t = Table(cells, colWidths=[w] * cols)
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0, colors.white),
                           ("INNERGRID", (0, 0), (-1, -1), 4, colors.white),
                           ("BACKGROUND", (0, 0), (-1, -1), ZEBRA),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 9), ("TOPPADDING", (0, 0), (-1, -1), 8),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return t

def layers_chart():
    W, Hh = CW, 150
    d = Drawing(W, Hh)
    left = 118; right = W - 8; n = 12
    cw = (right - left) / n
    top = Hh - 22
    d.add(String(left, Hh - 10, "Class", fontName="UI-B", fontSize=7.5, fillColor=MUTED))
    for c in range(1, 13):
        x = left + (c - 1) * cw
        d.add(String(x + cw / 2, Hh - 20, str(c), fontName="UI", fontSize=7.5, fillColor=MUTED, textAnchor="middle"))
        d.add(Line(x, top - 4, x, 14, strokeColor=colors.HexColor("#E4E7EB"), strokeWidth=0.5))
    rows = [
        ("Unplugged CT", [(1, 2, "#9FD3DB", "NEP intent"), (3, 8, PRIMARY.hexval(), "CBSE CT&AI 3-8")]),
        ("Block coding (Scratch)", [(3, 5, "#F6AD7B", "CBSE Cl. 3-5")]),
        ("'Coding' in policy", [(6, 8, ACCENT.hexval(), "NEP Middle Stage")]),
        ("Examined text code", [(9, 10, "#B7C4CF", "ICSE Java"), (11, 12, INK.hexval(), "CBSE Python")]),
    ]
    rh = 22
    for i, (label, segs) in enumerate(rows):
        y = top - 12 - (i + 1) * (rh + 6)
        d.add(String(0, y + 7, label, fontName="UI-SB", fontSize=8, fillColor=INK))
        for a, b, col, txt in segs:
            col = col if isinstance(col, str) else col
            c = colors.HexColor(col if col.startswith("#") else "#" + col[2:] if col.startswith("0x") else col)
            x0 = left + (a - 1) * cw; x1 = left + b * cw
            d.add(Rect(x0 + 1, y, x1 - x0 - 2, rh, fillColor=c, strokeColor=None, rx=3, ry=3))
            tc = colors.white if col in (PRIMARY.hexval(), ACCENT.hexval(), INK.hexval()) else INK
            d.add(String((x0 + x1) / 2, y + 7.5, txt, fontName="UI", fontSize=7, fillColor=tc, textAnchor="middle"))
    xb = left + 3.5 * cw
    d.add(Line(xb, top - 2, xb, 10, strokeColor=ACCENT, strokeWidth=1.2, strokeDashArray=[3, 2]))
    d.add(String(xb + 3, 2, "Founder's belief: 'around Class 4'", fontName="UI-B", fontSize=7.5, fillColor=ACCENT))
    return d

def fix_hex(c):  # reportlab hexval returns '0xRRGGBB'
    return "#" + c.hexval()[2:]

def coverage_chart():
    rows = ["Puzzle bank by maths chapter", "Unplugged activities", "Coding / Scratch",
            "AI teaching text (student book)", "AI support in teacher book",
            "Hands-on AI", "Project briefs & rubrics", "Assessment templates"]
    # P=provided, L=limited, M=missing, N=n/a
    grid = {
        "Puzzle bank by maths chapter": "PPPPPP",
        "Unplugged activities": "LLLLLL",
        "Coding / Scratch": "MMMMMM",
        "AI teaching text (student book)": "NNNPPP",
        "AI support in teacher book": "NNNLLL",
        "Hands-on AI": "NNNMMP",
        "Project briefs & rubrics": "NNNMMM",
        "Assessment templates": "MMMMMM",
    }
    colmap = {"P": (GOOD, "Provided"), "L": (WARN, "Thin"), "M": (BAD, "Missing"), "N": (colors.HexColor("#D9DEE3"), "n/a")}
    W = CW; left = 150; cw = (W - left - 4) / 6; rh = 17
    Hh = 26 + rh * len(rows) + 26
    d = Drawing(W, Hh)
    for j, cl in enumerate(range(3, 9)):
        d.add(String(left + j * cw + cw / 2, Hh - 12, f"Class {cl}", fontName="UI-B", fontSize=7.8, fillColor=INK, textAnchor="middle"))
    for i, r in enumerate(rows):
        y = Hh - 26 - (i + 1) * rh
        d.add(String(0, y + 5, r, fontName="UI", fontSize=7.8, fillColor=INK))
        for j, ch in enumerate(grid[r]):
            c, lab = colmap[ch]
            d.add(Rect(left + j * cw + 1.5, y + 1, cw - 3, rh - 2.5, fillColor=c, strokeColor=None, rx=2, ry=2))
            d.add(String(left + j * cw + cw / 2, y + 5.5, lab, fontName="UI", fontSize=6.8,
                         fillColor=colors.white if ch in "PMLW" else MUTED, textAnchor="middle"))
    # legend note
    d.add(String(0, 4, "Class 8 hands-on AI = three Teachable Machine labs (need computer, internet, webcam, microphone).",
                 fontName="UI-I", fontSize=7, fillColor=MUTED))
    return d

def gantt():
    tasks = [("Finalise guides, print prototype, recruit", 0, 1, PRIMARY),
             ("Interviews (~6 schools a week)", 1, 4, ACCENT),
             ("Final interviews + hypothesis tally", 4, 5, WARN),
             ("Findings memo + pilot go/no-go", 5, 6, GOOD),
             ("Book lists close at schools (Dec-Jan)", 5, 8, colors.HexColor("#8795A1"))]
    weeks = ["9 Nov", "16 Nov", "23 Nov", "30 Nov", "7 Dec", "14 Dec", "21 Dec", "28 Dec+"]
    W = CW; left = 170; cw = (W - left - 4) / len(weeks); rh = 18
    Hh = 22 + rh * len(tasks) + 6
    d = Drawing(W, Hh)
    for j, w in enumerate(weeks):
        d.add(String(left + j * cw + 2, Hh - 11, w, fontName="UI-B", fontSize=7.2, fillColor=MUTED))
        d.add(Line(left + j * cw, Hh - 15, left + j * cw, 2, strokeColor=colors.HexColor("#E4E7EB"), strokeWidth=0.5))
    for i, (t, a, b, c) in enumerate(tasks):
        y = Hh - 20 - (i + 1) * rh
        d.add(String(0, y + 5, t, fontName="UI", fontSize=7.8, fillColor=INK))
        d.add(Rect(left + a * cw + 1, y + 1, (b - a) * cw - 2, rh - 4, fillColor=c, strokeColor=None, rx=3, ry=3))
    return d

def hours_bar():
    W, Hh = CW, 48
    d = Drawing(W, Hh)
    segs = [("Advanced CT 40 h", 40, PRIMARY), ("Intro AI 20 h", 20, ACCENT), ("Interdisciplinary projects 40 h (no material in books)", 40, BAD)]
    x = 0; scale = W / 100
    for lab, v, c in segs:
        d.add(Rect(x, 18, v * scale - 2, 22, fillColor=c, strokeColor=None, rx=3, ry=3))
        d.add(String(x + 6, 26, lab, fontName="UI-B", fontSize=7.8, fillColor=colors.white))
        x += v * scale
    d.add(String(0, 4, "Classes 6-8: 100 hours a year each (Classes 3-5: 50 h embedded in Maths and TWAU)", fontName="UI-I", fontSize=7.2, fillColor=MUTED))
    return d

# ---------- doc template ----------
class Doc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        super().__init__(fn, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
                         title="CodeSchool Research Pack", author="Anoop Dobhal (CodeSchool)",
                         subject="Kids coding curriculum, market, CBSE CT&AI review and school interview plan",
                         keywords="CodeSchool, CBSE, computational thinking, AI, coding, interviews", **kw)
        self.section = ""
        fr = Frame(LM, BM, CW, PAGE_H - TM - BM, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate("cover", [fr], onPage=draw_cover),
                               PageTemplate("body", [fr], onPageEnd=draw_chrome)])
    def afterFlowable(self, f):
        if isinstance(f, Heading):
            lvl = f.toc_level
            if lvl == 0: self.section = f.short
            if lvl <= 1 and f.key != "contents":
                self.notify("TOCEntry", (lvl, esc(f.short), self.page, f.key))
            self.canv.bookmarkPage(f.key)
            olvl = min(lvl, getattr(self, "_olvl", -1) + 1)
            self._olvl = olvl
            self.canv.addOutlineEntry(f.short, f.key, level=olvl, closed=False)

def draw_chrome(canv, doc):
    canv.saveState()
    canv.setFillColor(PRIMARY); canv.rect(0, PAGE_H - 9 * mm, PAGE_W, 9 * mm, fill=1, stroke=0)
    canv.setFillColor(colors.white); canv.setFont("UI-B", 8)
    canv.drawString(LM, PAGE_H - 6 * mm, "CodeSchool  ·  Research Pack")
    canv.setFont("UI", 8)
    canv.drawRightString(PAGE_W - RM, PAGE_H - 6 * mm, doc.section)
    canv.setStrokeColor(RULE); canv.setLineWidth(0.5)
    canv.line(LM, 12 * mm, PAGE_W - RM, 12 * mm)
    canv.setFillColor(MUTED); canv.setFont("UI", 7.5)
    canv.drawString(LM, 8 * mm, "6 November 2026  ·  github.com/evolvian2026/CodeSchool")
    canv.drawRightString(PAGE_W - RM, 8 * mm, f"Page {doc.page}")
    canv.setFillColor(PRIMARY); canv.setFont("UI-B", 7.5)
    label = "↑ Back to contents"
    w = stringWidth(label, "UI-B", 7.5)
    x = PAGE_W / 2 - w / 2
    canv.drawString(x, 8 * mm, label)
    canv.linkRect("", "contents", (x - 2, 6.5 * mm, x + w + 2, 11 * mm), relative=0, thickness=0)
    canv.restoreState()

def draw_cover(canv, doc):
    canv.saveState()
    canv.setFillColor(PRIMARY); canv.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canv.setFillColor(colors.HexColor("#0E6A7A")); canv.rect(0, 0, PAGE_W, PAGE_H * 0.36, fill=1, stroke=0)
    canv.setFillColor(ACCENT); canv.rect(LM, PAGE_H - 62 * mm, 26 * mm, 2.2 * mm, fill=1, stroke=0)
    canv.setFillColor(colors.white)
    canv.setFont("UI-B", 11); canv.drawString(LM, PAGE_H - 50 * mm, "CODESCHOOL  ·  FOUNDATIONAL RESEARCH")
    canv.setFont("UI-B", 34); canv.drawString(LM, PAGE_H - 80 * mm, "Research Pack")
    canv.setFont("UI", 15)
    canv.drawString(LM, PAGE_H - 92 * mm, "When programming starts in Indian schools, a level-based")
    canv.drawString(LM, PAGE_H - 99 * mm, "design per grade, the market, CBSE's free CT&AI books,")
    canv.drawString(LM, PAGE_H - 106 * mm, "and the plan to validate it all with schools.")
    canv.setFont("UI", 10.5); canv.setFillColor(colors.HexColor("#CFE7EA"))
    y = PAGE_H * 0.36 - 22 * mm
    for line in ["Prepared for: Anoop Dobhal, founder, CodeSchool",
                 "Status: research complete; school interviews start 16 November 2026",
                 "Version: 6 November 2026  ·  Repository: github.com/evolvian2026/CodeSchool",
                 "Interactive PDF: clickable contents, bookmarks, source links, fillable forms"]:
        canv.drawString(LM, y, line); y -= 7 * mm
    canv.restoreState()

# =====================================================================
story = []
story += [Spacer(1, 1), NextPageTemplate("body"), PageBreak()]

# ---------- How to use ----------
story += [H("How to use this PDF", 0, "howto", "How to use this PDF"),
          P("This pack brings every research document from the CodeSchool repository into one place, with tools to act on it.", H1SUB)]
story += [tbl([
    ["Feature", "How to use it"],
    ["**Clickable contents**", "Every line on the [contents page](#contents) jumps to its section. Every page has a **↑ Back to contents** link in the footer."],
    ["**Bookmarks**", "Open the bookmarks or outline panel in your PDF reader (Acrobat, Edge, Chrome, Foxit) to move between sections and sub-sections."],
    ["**Source links**", "Underlined teal text opens the official circular, syllabus, handbook or news source. Internal links jump within this PDF."],
    ["**Fillable forms**", "The [action checklist](#actions), [hypothesis tracker](#tracker), [interview note form](#noteform), [device audit](#audit) and [B3 observation sheet](#b3obs) have fields you can type in, tick and choose from. Save with **File → Save** in Acrobat Reader or Edge. Some browsers' built-in viewers don't save form data."],
    ["**Print**", "Each form page prints cleanly. Print the B3 lesson and device audit pages for interviews."],
], [0.22, 0.78], first_bold=False)]
story.append(callout([P("This repository is **public** on GitHub. Fill the interview forms in a **separate copy saved outside the repository**, with no real names. Never commit filled copies. The `.gitignore` already blocks `docs/research/interviews/` and `*.private.*` files, so name your copy `CodeSchool-Research-Pack.private.pdf`.")], "risk", "Privacy: keep filled forms out of git"))
story.append(H("Source labels used throughout", 2, "labels"))
story += [tbl([
    ["Label", "Meaning"],
    ["**Official**", "Checked against a board or government document (CBSE circular, syllabus, handbook, NEP)."],
    ["**News**", "Mainstream press."],
    ["**Secondary**", "Publisher, vendor or blog source."],
    ["**Background knowledge**", "Taken from well-known documents without re-checking in this research; verify before quoting."],
    ["**Low-quality estimate**", "Paid market-research figures with undisclosed methods."],
    ["**Hypothesis / recommendation**", "A design or pricing proposal to be tested, not a fact."],
], [0.28, 0.72])]

# ---------- TOC ----------
toc = TableOfContents(); toc.levelStyles = [TOC0, TOC1]; toc.dotsMinLevel = 0
story += [PageBreak(), H("Contents", 0, "contents", "Contents"), Spacer(1, 4), toc]

# =====================================================================
# 1 EXECUTIVE SUMMARY
story += section("1. Executive summary", "The short answer, the evidence behind it, and what to do next.", "exec")
story.append(callout([P("**\"Around 4th standard\" is right about classrooms and wrong about policy.** Children commonly meet Scratch around Class 3-4 in private-school books and Kerala's state books. Officially, India has four different starting points: unplugged computational thinking (CT) from the Foundational Stage (NEP) and from **Class 3** in CBSE (2026-27); block coding as a CBSE Class 3-5 competency; \"coding activities\" in Classes 6-8 (NEP); and examined text programming only from **Class 9 (ICSE, Java)** or **Class 11 (CBSE, Python)**.")], "accent", "The answer to the founding question"))
story.append(stat_tiles([
    ("Class 3", "CBSE's CT&AI curriculum starts here in 2026-27 (50 h a year in Classes 3-5)", fix_hex(PRIMARY)),
    ("0 of 12", "free CBSE handbooks contain any coding", fix_hex(BAD)),
    ("120 h", "of Classes 6-8 projects with no briefs or rubrics in any book", fix_hex(BAD)),
    ("d ≈ 0.4", "learning effect of game 'levels' in programming; badges and points show none", fix_hex(GOOD)),
    ("Rs 449 / 599", "booklist pack prices to test (Classes 3-5 / 6-8); Uolo Tekie starts at Rs 799", fix_hex(ACCENT)),
    ("Dec-Jan", "school book lists close for the April session: the sales deadline", fix_hex(WARN)),
]))
story.append(H("Key findings", 1, "keyfind"))
story += bullets([
    "**Programming starts in layers, not at one class.** Thinking from Class 3 (CBSE), Scratch around Class 3-5 in practice, \"coding activities\" in Classes 6-8, and text programming from Class 9 (ICSE) or Class 11 (CBSE). CBSE's Classes 9-10 Computer Applications (165) has **no programming**. See [section 3](#start).",
    "**A level-based structure per grade is feasible and evidence-backed.** Levels are the one game mechanic with a measured learning effect. Recommended: five bands (A: Classes 1-2 to E: 11-12) of mastery-gated levels, separate from class, with placement tests and Express catch-up tracks. See [section 4](#levels).",
    "**Schools, not parents, pay.** Parent-paid live coding collapsed (WhiteHat Jr; Tynker sold for ~$2.2M after a ~$200M purchase). School bundles survive (LEAD Group Rs 387 Cr FY26). Recommended model: **B2B2C**. See [section 5](#market).",
    "**CBSE gives away the puzzles but not the hard parts.** Across all 12 books: no coding, no project materials, no assessment templates; AI teaching text only in student books; hands-on AI only in Class 8. See [section 7](#handbooks).",
    "**CBSE is telling schools coding isn't needed.** Its April 2026 webinar presents \"no coding/software\" as a design choice. Selling \"CBSE requires coding\" would contradict the Board. See [section 7.12](#webinar).",
    "**Best openings are what CBSE admits is unfinished:** the promised project list with rubrics and AI concept handouts are still not published, plus teacher support and assessment.",
    "**The biggest risks are policy churn and empty labs.** CBSE \"advises\" the curriculum and already deferred Class 9; only 64.7% of schools have computer facilities. See [section 8](#risks).",
])
story.append(H("Positioning in one line", 1, "posline"))
story.append(callout([P("**CodeSchool is the easiest way to deliver the parts of CBSE CT&AI that CBSE didn't provide:** project kits, AI teacher support, hands-on AI on low-end equipment, assessment and progress tracking, with coding as the \"now you build it\" tool. It sits on top of the free books instead of replacing them.")], "good"))
story.append(H("Top five next actions", 1, "top5"))
story += [tbl([
    ["#", "Action", "When"],
    ["1", "Fill the contact placeholders in the intro letter, print 20 B3 lessons and device audit sheets", "9-11 Nov"],
    ["2", "Shortlist 25-30 schools matching the sample mix and send the first 10 intro letters", "by 13 Nov"],
    ["3", "Run interviews with ~6 schools a week; fill the note form the same day", "16 Nov - 11 Dec"],
    ["4", "Test the two new risks directly: coding demand, and whether CBSE's project list has arrived", "every coordinator interview"],
    ["5", "Write the 2-page findings memo and make the pilot go/no-go call", "14-18 Dec"],
], [0.06, 0.74, 0.2])]
story.append(P("The full, fillable list is in [section 9: Action plan](#actions).", SMALL))

# =====================================================================
# 2 SCOPE
story += section("2. Scope and method", "What was asked, what was covered, how, and what was left out.", "scope")
story.append(H("The brief", 1, "brief"))
story.append(callout([P("_\"Before starting development, conduct market and curriculum research to determine the exact grade level at which programming is introduced in schools. While my initial understanding is around the 4th standard, I would like to verify this. Additionally, explore the feasibility of a level-based learning structure tailored to each grade. Do not start building or writing code yet; focus entirely on foundational research.\"_")], "info", "Founder's request"))
story.append(H("Research questions", 1, "rq"))
story += [tbl([
    ["#", "Question", "Answered in"],
    ["Q1", "At exactly which grade is programming formally introduced in Indian (and peer) school systems? Is \"around Class 4\" right?", "[Section 3](#start)"],
    ["Q2", "Is a level-based structure tailored to each grade feasible, and what does the evidence say about levels, mastery and progression?", "[Section 4](#levels)"],
    ["Q3", "What does the market look like: players, failures, business models, pricing and size?", "[Section 5](#market)"],
    ["Q4", "Are the CBSE facts right? (added after the first report)", "[Section 6](#verify)"],
    ["Q5", "What do CBSE's free CT&AI books actually contain, and what gaps remain? (added)", "[Section 7](#handbooks)"],
    ["Q6", "How do we validate all this with schools before building? (added)", "[Section 10](#interviews)"],
], [0.07, 0.73, 0.2])]
story.append(H("In scope and out of scope", 1, "inout"))
inout = Table([[
    [Paragraph("<b>In scope</b>", S("x", fontName="UI-B", textColor=GOOD))] + bullets([
        "India: NEP 2020, NCF-SE 2023, CBSE (fully verified), ICSE/CISCE, Kerala, Tamil Nadu, Karnataka, Atal Tinkering Labs, private textbooks",
        "Peers: England, USA, Finland, Australia, NZ, Estonia, Singapore, China, Korea, Japan, UAE",
        "Learning progressions and evidence on levels, mastery, PRIMM, Parsons, unplugged, block-to-text",
        "Market: Indian and global players, B2C vs B2B, pricing anchors, market-size claims",
        "All 12 CBSE CT&AI handbooks and the April 2026 webinar slides",
        "School interview plan and materials"]),
    [Paragraph("<b>Out of scope (not done)</b>", S("x2", fontName="UI-B", textColor=BAD))] + bullets([
        "Any app design, code or prototype software (by instruction)",
        "Primary data: no schools, teachers or parents interviewed yet",
        "Maharashtra, AP/Telangana, Delhi boards (no reliable sources)",
        "CISCE Classes 1-8 guidelines, AI 417 / IT 402 syllabi, NCF-SE PDF (not read directly)",
        "Legal review of child-data rules (DPDP Act)",
        "A bottom-up market model from UDISE+ data"]),
]], colWidths=[CW / 2, CW / 2])
inout.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (0, 0), GOOD_L),
                           ("BACKGROUND", (1, 0), (1, 0), BAD_L), ("LEFTPADDING", (0, 0), (-1, -1), 8),
                           ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                           ("INNERGRID", (0, 0), (-1, -1), 4, colors.white)]))
story += [inout, Spacer(1, 6)]
story.append(H("Method", 1, "method"))
story += [tbl([
    ["Stage", "What was done", "Output"],
    ["1. Desk research", "Parallel research on Indian curricula, global curricula, learning progression evidence and the market; synthesised into one report with labelled sources", "[Main report](https://github.com/evolvian2026/CodeSchool/blob/main/docs/research/reports/Kids%20coding%20curriculum%20and%20market.md) + 4 research notes"],
    ["2. Interview plan", "Hypotheses, sample, role guides, analysis and decision rule", "[Interview plan](https://github.com/evolvian2026/CodeSchool/blob/main/docs/research/school-interview-plan.md)"],
    ["3. Interview materials", "Intro letter and consent script, Level B3 paper lesson, device audit, tracking sheet", "[Materials folder](https://github.com/evolvian2026/CodeSchool/tree/main/docs/research/interview-materials)"],
    ["4. CBSE verification", "Full text of circulars Acad-15, -18, -70 of 2026, the CT&AI curriculum, and CA 165 / CS 083 / IP 065 syllabi", "[Verification note](https://github.com/evolvian2026/CodeSchool/blob/main/docs/research/cbse-verification.md)"],
    ["5. Handbook review", "All 12 student and teacher handbooks (Classes 3-8) and the 45-slide webinar deck", "[Handbook review](https://github.com/evolvian2026/CodeSchool/blob/main/docs/research/cbse-handbook-review.md)"],
], [0.2, 0.5, 0.3])]
story.append(H("Limitations", 1, "limits"))
story += bullets([
    "**No primary research yet.** Every conclusion about what schools want or will pay is a hypothesis until interviews are done.",
    "**Market size is unknown.** Published figures conflict by up to 12x and have no stated method; none should be used.",
    "**Uneven evidence.** No study ties specific coding concepts to specific ages; no block-to-text study covers ages 10-13; no Indian parent survey exists.",
    "**Handbook reading depth varies.** Front matter, activities and AI chapters were read in full in all books; Class 5 puzzle chapters were skimmed.",
    "**Corrections were made along the way.** Two CBSE claims in the first draft were wrong and one later correction was itself reversed; the record is kept in [section 6](#verify).",
])

# =====================================================================
# 3 WHEN DOES PROGRAMMING START
story += section("3. When does programming start?", "Four different answers depending on what \"programming\" means. Treating them as one causes the confusion.", "start")
story.append(layers_chart())
story.append(P("Indian Class _n_ is roughly England Year _n_+1. The dashed line marks the founder's starting belief.", SMALL))
story.append(H("The verdict, layer by layer", 1, "verdict"))
story += [tbl([
    ["Layer", "Earliest official start", "Where children actually meet it", "Is \"around Class 4\" right?"],
    ["**Unplugged CT**", "Foundational Stage, preschool to Class 2 (NEP intent); **Class 3** (CBSE, 2026-27, 50 h a year)", "Class 3 CBSE handbooks; Kerala Class 3 logic games", "**No. One class too late.**"],
    ["**Block coding (Scratch)**", "**Class 3-5** competency in CBSE's framework, where devices allow", "Class 3 private textbooks; Kerala Class 4; ICSE-aligned books Classes 4-5", "**Yes, roughly.** This is what the belief describes."],
    ["**\"Coding\" in policy**", "**Classes 6-8** (NEP Middle Stage; CBSE CT&AI 6-8; optional modules since 2021)", "Scratch games, HTML, BASIC-256 or intro Python in Class 6 textbooks", "**No. Two classes too early.**"],
    ["**Graded text programming**", "**Class 9** elective in ICSE (Java); **Class 11** in CBSE (Python, CS 083 / IP 065)", "Kerala Python in Classes 9-10; some Class 6 books preview Python", "**No. Five to seven classes too early.**"],
], [0.18, 0.3, 0.3, 0.22])]
story.append(H("Board-by-board status (November 2026)", 1, "boards"))
story += [tbl([
    ["Board / programme", "Start", "What is taught", "Source"],
    ["NEP 2020", "CT from Foundational Stage; coding activities Classes 6-8", "Puzzles and games for CT (para 4.25); policy, not a syllabus", "[Official](https://static.pib.gov.in/WriteReadData/userfiles/NEP_Final_English_0.pdf)"],
    ["CBSE CT&AI, Classes 3-8", "**Class 3** (2026-27)", "3-5: maths-puzzle CT, 50 h in Maths and TWAU; 6-8: 100 h (40 CT, 20 AI, 40 projects). Schools \"advised\"; Acad-18 says it \"mandates\" content", "[Acad-15](https://cbseacademic.nic.in/web_material/Circulars/2026/15_Circular_2026.pdf), [curriculum](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_Pri_2026-27.pdf)"],
    ["CBSE Class 9 CT&AI", "**Deferred** for 2026-27", "Acad-70 (29 Oct 2026): modules \"shall not be the part of the curriculum for these batches\"", "[Acad-70](https://cbseacademic.nic.in/web_material/Circulars/2026/70_Circular_2026.pdf)"],
    ["CBSE Classes 9-12 electives", "CA 165 (Cl. 9-10); CS 083 / IP 065 (Cl. 11-12)", "CA 165: office tools and HTML, **no programming**; CS / IP: **Python**, SQL, Pandas", "Official syllabi"],
    ["CISCE (ICSE) 1-8", "No official class", "Publishers decide; Scratch around Classes 3-5", "Secondary"],
    ["ICSE 9-10", "Class 9 elective", "Java with BlueJ; Robotics & AI", "Secondary"],
    ["Kerala (KITE)", "Class 3 logic; **Class 4 Scratch**", "Games Class 6, AI Class 7, Python 9-10, robotics Class 10", "News"],
    ["Tamil Nadu", "Class 6", "TN SPARK pilot in ~5,000 government schools", "News"],
    ["Karnataka", "Class 9 (AI vocational)", "Class 6 under study", "Secondary"],
    ["Atal Tinkering Labs", "Class 6", "~10,000 labs; tinkering, not a curriculum", "News"],
    ["Private textbooks", "Class 3 Scratch", "Scratch Classes 3-6; HTML or intro Python in Class 6", "Secondary"],
], [0.2, 0.2, 0.42, 0.18])]
story.append(callout([P("**Two caveats.** (1) It is unclear how mandatory CBSE's Class 3-8 curriculum is: \"advised\" in Acad-15, \"mandates\" in Acad-18, but no board exam or enforcement. (2) Devices limit everything: UDISE+ 2024-25 shows only **64.7%** of schools with computer facilities (Bihar government schools 16.5%).")], "warn"))
story.append(H("International comparison", 1, "intl"))
story += [tbl([
    ["Country", "CT / algorithms start", "Blocks", "Text language", "Mandatory?"],
    ["England", "Age 5 (KS1)", "Ages 7-11 (KS2)", "Ages 11-14, at least one textual (KS3)", "Statutory (maintained schools)"],
    ["USA (CSTA 2026)", "PK/K", "Elementary (Code.org CSF)", "Middle/high school", "Voluntary; 12 states require CS to graduate"],
    ["Finland", "Grade 1, age 7", "Grades 3-6", "Grades 7-9 in maths", "Yes, embedded"],
    ["Australia", "Foundation, age 5", "Years 3-6", "Years 7-8", "To Year 8"],
    ["Singapore", "P4-P6 (Code for Fun)", "10-hour CFF in all primaries", "O-level Python (elective)", "CFF yes; AI for Fun opt-in"],
    ["China", "~Grade 3 (IT subject)", "Primary graphical", "Python in junior/senior high", "IT compulsory; Beijing 8 AI h/yr"],
    ["South Korea", "Grades 5-6", "Elementary informatics", "Middle school", "Yes"],
    ["UAE", "Kindergarten", "n/d", "n/d", "Government schools, 2025-26"],
    ["**India**", "Class 3 formally (~age 8)", "Class 3-5 competency", "ICSE Cl. 9; CBSE Cl. 11", "\"Advised\"; programming elective"],
], [0.16, 0.2, 0.2, 0.24, 0.2])]
story.append(P("**Pattern everywhere:** unplugged at 5-7, blocks at 7-11, text at 11-14, exam CS at 14-16. AI is being layered on top of CS, and in places reversed (Korea downgraded AI textbooks within six months). Several peer rows are background knowledge; verify before quoting externally."))

# =====================================================================
# 4 LEVELS
story += section("4. A level-based structure per grade", "Feasible and evidence-backed: five bands of mastery-gated levels that are separate from the child's class.", "levels")
story += bullets([
    "**Levels work.** Costa's 2023 meta-analysis: gamification gain in programming of **d ≈ 0.4**, largely from levels; badges, points, avatars and leaderboards had no significant learning effect.",
    "**Frameworks already use bands.** CSTA (multi-year levels), Bebras (two-year age groups) and Code.org's A-F courses with \"Express\" catch-up versions.",
    "**Developmental seams** fall around age 7-8 (structured → open blocks) and 10-12 (concrete → abstract), not at every grade.",
])
story.append(H("Recommended framework (recommendation)", 1, "bands"))
story += [tbl([
    ["Band", "Levels", "Concepts and tools", "Exit outcome", "Alignment"],
    ["**A: Explorers**\nClasses 1-2", "A1 sequencing · A2 debugging · A3 repeat · A4 events · A5 story project", "Unplugged first, then icon blocks in 10-20 min teacher-led sessions; story framing", "Follows and gives precise instructions; fixes one bug; makes a short story", "NEP Foundational intent; no CBSE mandate (cheap, mostly printable)"],
    ["**B: Builders**\nClasses 3-5", "B1 loops · B2 events · B3 conditionals · B4 nested/while · B5 variables · B6 CT puzzles · B7 capstone", "Unplugged intro then Scratch-style blocks; Android-first, offline; printable sheets", "Builds an interactive game with events, conditionals and a loop; explains it", "**CBSE CT&AI 3-5** (50 h); needs a strand mapped to the NCERT maths chapters"],
    ["**C: Makers**\nClasses 6-8", "C1 functions · C2 lists/data · C3 AI literacy I · C4 Python behind blocks · C5 reading Python · C6 writing Python · C7 AI literacy II · C8 project", "Blocks and text together, then text; Parsons scaffolds; no-code AI tools", "Multi-part project; reads and modifies Python; trains and critiques a classifier", "**CBSE CT&AI 6-8** (100 h); NEP coding activities; block-to-text bridge"],
    ["**D: Coders**\nClasses 9-10", "D1-D6: Python consolidation, modular code, data structures, algorithms, data/AI project, testing AI-written code", "Text; Python track (CBSE/state) and Java track (ICSE)", "Writes and tests modular programs; evaluates AI code", "No CBSE programming subject here: the Scratch-to-Python gap"],
    ["**E: Specialists**\nClasses 11-12", "E1-E6 exam tracks plus specialties", "Text; portfolios; exam practice", "Board-exam readiness and a portfolio", "CBSE CS 083 / IP 065, ISC CS; separate later business"],
], [0.12, 0.24, 0.24, 0.2, 0.2])]
story.append(H("How levels decouple from class", 1, "decouple"))
story += bullets([
    "**Default entry level and an age-appropriate \"skin\"** for each class; the level comes from what the child can show.",
    "**10-15 minute adaptive placement check** on joining; **\"challenge to skip\"** tests at each level boundary.",
    "**Mastery gating** at ~80-90% of check items, with spaced review.",
    "**Teacher override** so a class can stay together on a period plan (overrides recorded, remediation queued).",
    "**Express tracks:** Junior (Classes 4-5 newcomers cover Band A fast), Middle (Classes 6-8 beginners cover A-B in a term), Senior (Class 9 beginners straight into Python/Java).",
])
story.append(H("One lesson template a non-specialist can run", 1, "template"))
tpl = Table([[Paragraph(f"<b>{a}</b><br/>{b}", S("tp", fontSize=8.2, leading=10.8, textColor=colors.white, alignment=TA_CENTER, spaceAfter=0))
              for a, b in [("1 Predict & run", "worked example"), ("2 Investigate", "tracing questions"), ("3 Modify", "guided change"),
                           ("4 Parsons", "reorder blocks"), ("5 Make", "open-ended")]]], colWidths=[CW / 5] * 5)
tpl.setStyle(TableStyle([("BACKGROUND", (0, 0), (3, 0), PRIMARY), ("BACKGROUND", (4, 0), (4, 0), ACCENT),
                         ("INNERGRID", (0, 0), (-1, -1), 3, colors.white), ("TOPPADDING", (0, 0), (-1, -1), 8),
                         ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
story += [tpl, P("PRIMM with a Parsons bridge. Steps 1-4 can be auto-graded; step 5 protects against puzzle-only progression. A worked example is the [Level B3 lesson](#b3).", SMALL)]
story.append(H("Evidence behind each design choice", 1, "evidence"))
story += [tbl([
    ["Design choice", "What the evidence says", "Strength"],
    ["Levels as the core mechanic", "d ≈ 0.4 in programming, driven by levels; badges/points/leaderboards no significant effect", "Moderate"],
    ["Badges optional, private, mastery-based", "Badges and leaderboards lowered motivation and scores in one study; game elements raise quantity not quality", "Moderate (contested)"],
    ["Mastery gating", "Direction strong; realistic effects much smaller than Bloom's \"2 sigma\"", "Strong direction; size contested"],
    ["PRIMM lessons", "UK quasi-experiment, ages 11-14: PRIMM group scored higher", "Moderate; nothing below age 11"],
    ["Parsons problems", "Same gains as writing code, in less time", "Moderate; one null study"],
    ["Data-driven hints", "iSnap next-step hints; explaining \"why\" helps", "Moderate"],
    ["Block-to-text around Classes 7-8", "Blocks faster for concepts; advantage fades ~10 weeks after Java, no harm", "Moderate; no study at ages 10-13"],
    ["Unplugged then plugged", "Large unplugged effects but plateaus; hands-on beat unplugged-only", "Moderate"],
    ["Story-based tools for Classes 1-2", "d = 0.81 programming → CT at ages 3-7; structured tools best", "Moderate"],
    ["Screen time", "No hard cap for ages 6-8 in any guideline", "Weak; a design decision"],
    ["Scripted support for teachers", "Mostly satisfaction data; teacher readiness moderates outcomes", "Weak"],
], [0.28, 0.52, 0.2])]

# =====================================================================
# 5 MARKET
story += section("5. Market", "Parent-paid live coding burned out; school bundles survived. Free basics push value into alignment, assessment and teacher support.", "market")
story.append(H("B2C collapsed, B2B survived", 1, "b2c"))
story += [tbl([
    ["Player", "Model", "What happened", "Source label"],
    ["WhiteHat Jr", "B2C live 1:1 classes", "~150,000 paid students at 2020 peak; 26.73% of BYJU's FY21 loss; layoffs, lawsuits, refund complaints", "News / user posts"],
    ["Tynker (BYJU's)", "B2C app + schools", "Bought for ~$200M, sold for ~$2.2M (2025)", "News"],
    ["BrightChamps", "B2C live classes", "FY23 revenue Rs 20.6 Cr vs loss Rs 159.5 Cr", "News"],
    ["LEAD Group", "**B2B school bundle**", "FY26 revenue **Rs 387 Cr**; EBITDA breakeven; Rs 415 Cr ARR", "News"],
    ["Eupheus / Extramarks", "B2B school bundles", "~Rs 225 Cr / Rs 233 Cr FY24", "News"],
    ["Codingal / PlanetSpark", "B2C live", "Good ratings and growth, but teachers cost Rs 700-2,833 per class", "News / secondary"],
], [0.18, 0.18, 0.46, 0.18])]
story.append(callout([P("**Recommended model: B2B2C.** Sell a per-student annual licence to private CBSE and ICSE schools (collected in fees), add a free parent view and an optional paid home-practice tier. Government (B2G) is a second stage through ATL and ICT-lab vendors on GeM. Book lists close **December-January** for an April start.")], "good"))
story.append(H("Where the paid value has to sit", 1, "value"))
story.append(P("Basic block coding is free (Code.org, Scratch, CBSE books). Schools pay for what they struggle with:"))
story += bullets([
    "**Syllabus mapping** to CBSE CT&AI, CISCE and state syllabi (by NCERT maths chapter).",
    "**Assessment and reporting** for an internally assessed subject.",
    "**Support for non-specialist teachers:** period scripts, answer keys, misconception notes, a \"who is stuck\" dashboard.",
    "**Android-first, offline delivery** (90% of rural teens have a phone at home; ~31% own one).",
    "**Regional languages.**",
    "**A structured block-to-text bridge** for Classes 6-8, which neither CBSE nor Scratch provides.",
])
story.append(H("Positioning and pricing hypotheses", 1, "pricing"))
story += [tbl([
    ["Element", "Hypothesis", "Confidence"],
    ["Core offer (Classes 3-8), revised 6 Nov 2026", "**Rs 449 (Classes 3-5) and Rs 599 (Classes 6-8) booklist packs**, or a **Rs 299 + GST** school licence for premium schools; was Rs 200-800", "Hypothesis; printed CT&AI books sell at Rs 179-630, Uolo Tekie from Rs 799 ([competitors report](https://github.com/evolvian2026/CodeSchool/blob/main/docs/research/CodeSchool-Competitors-Buying-Compliance.pdf))"],
    ["Classes 1-2 (Band A)", "Free or nominal inside the school licence", "Hypothesis"],
    ["Classes 9-12 exam tracks", "Separate add-on priced above the core", "Hypothesis"],
    ["Parent tier", "Free progress view; paid home practice billed monthly, no EMI, published refund policy; test below Rs 500/month", "Hypothesis"],
    ["B2G", "Software + teacher-training layer alongside ATL / ICT vendors", "Hypothesis"],
], [0.25, 0.45, 0.3])]
story.append(callout([P("**Market size is unknown; do not quote published figures.** \"$14B coding for kids in India\" has no source. Global estimates range $514M-$6.5B; Indian K-12 estimates differ 2x. Illustration only: 5M private-school students × Rs 500-1,500 = Rs 250-750 Cr a year across the market. The real model is schools × Class 3-8 enrolment × realised price, from UDISE+ and pilot conversion.")], "risk"))
story.append(P("**Pitch shift:** AI literacy is replacing \"learn to code\". Code.org rebranded Hour of Code as Hour of AI (Dec 2025); CBSE named its mandate \"Computational Thinking and AI\". Avoid outcome promises (ASCI found 5 of 7 WhiteHat Jr ads in potential violation)."))

# =====================================================================
# 6 VERIFICATION
story += section("6. CBSE facts checked against official documents", "Every CBSE claim in the report was rechecked against the full official text on 5 November 2026.", "verify")
story += [tbl([
    ["Claim", "Verdict", "What the documents say"],
    ["CT&AI for Classes 3-8 starts in 2026-27", "**Confirmed**", "Acad-15/2026, 1 April 2026"],
    ["Schools \"advised\", not ordered", "**Confirmed, with nuance**", "Acad-15 \"advised\"; Acad-18 \"mandates\" content and schools \"should\" use the free books"],
    ["50 h (3-5); 100 h (6-8: 40 CT + 20 AI + 40 projects)", "**Confirmed**", "Curriculum sections 3.4 and 10.2"],
    ["Classes 3-5 embedded in Maths and TWAU", "**Confirmed**", "Books follow the NCERT maths chapter order"],
    ["Scratch named for Classes 3-5", "**Confirmed**", "Competency C-6, a single competency"],
    ["Teachable Machine named for Classes 6-8", "**Right for Class 8 books; not in the curriculum**", "Curriculum names no tool. Class 8 student book names Teachable Machine and Machine Learning for Kids with three labs; Classes 6-7 name none"],
    ["Python not a Class 3-8 topic", "**Confirmed**", "Appears only in the \"Aims\""],
    ["Class 9 CT&AI dropped for 2026-27 batch", "**Confirmed**", "Acad-70/2026, 29 Oct 2026"],
    ["Compulsory Class 9 in 2027-28; Class 10 exam 2028-29", "**Still unconfirmed**", "Neither circular says this"],
    ["CA 165 teaches Python/HTML in Classes 9-10", "**Wrong**", "No programming: office tools (9), HTML/CSS (10)"],
    ["CBSE's first programming subject is in Class 11", "**Confirmed (new)**", "Python in CS 083 and IP 065"],
    ["Teacher training through NISHTHA", "**Not supported; CBSE runs its own CPD**", "Webinar: 2026-27 theme \"Computational Thinking and Understanding AI\"; district/regional 1-day workshops, lead-school half-days, DD PM e-Vidya videos"],
], [0.33, 0.2, 0.47], extra=[])]
story.append(H("What this changes for CodeSchool", 1, "verifyimp"))
story += bullets([
    "**No CBSE student meets a programming language before Class 11.** Band C (block-to-text) and Band D sit in that gap.",
    "**Classes 3-5 CT is maths puzzles in NCERT chapter order**, so Band B needs a strand mapped to those chapters.",
    "**Explicit if-then is a Class 7 outcome**, but if-then rules appear in puzzles from Class 3, so Level B3 at Class 4 is a stretch, not a mismatch.",
    "**Classes 6-8 AI is taught by computer teachers**: they are buyers for Band C, not just a device audit.",
    "**Platform-agnostic and free-first**: no incumbent tool, and schools are steered to free options; sell tooling and assessment, not content.",
])
story.append(callout([P("**Correction history.** The first draft said CA 165 teaches programming (wrong) and named Teachable Machine for Classes 6-8. A later \"correction\" said no tool was named anywhere; reading the Class 8 student book showed the original notes were right about the handbooks. The verification table above is the final position.")], "info"))

# =====================================================================
# 7 HANDBOOKS
story += section("7. CBSE CT&AI handbook review", "All 12 free books (student and teacher, Classes 3-8) plus the 28 April 2026 webinar. These are what every school will compare CodeSchool with.", "handbooks")
story.append(H("7.1 What was read", 1, "hbread"))
books = [("3", 53, 96), ("4", 52, 111), ("5", 61, 118), ("6", 84, 110), ("7", 86, 98), ("8", 75, 92)]
rows = [["Class", "Student Handbook", "Teacher Handbook"]]
for c, s, t in books:
    rows.append([f"**Class {c}**",
                 f"[{s} pages](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_Pri{c}SH_2026-27.pdf)",
                 f"[{t} pages](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_Pri{c}TH_2026-27.pdf)"])
story += [tbl(rows, [0.2, 0.4, 0.4])]
story += bullets([
    "**Read in full in every book:** front matter (goals, outcomes, hours, pedagogy, assessment), every activity, every AI chapter.",
    "**Read question by question:** puzzle chapters of Class 3 TH, Class 4 SH and Classes 6-8 TH; AI chapters of Classes 6-8 SH.",
    "**Skimmed:** Class 5 puzzles and the other student-book puzzle chapters (same questions as the teacher books, without solutions).",
    "**Made by:** Centre for Creative Learning, IIT Gandhinagar, with experts from IIT Madras, Azim Premji University, MNIT and NITTTR. Activities cite [CS Unplugged](https://www.csunplugged.org/).",
])
story.append(H("7.2 Coverage at a glance", 1, "hbcover"))
story.append(coverage_chart())
story.append(H("7.3 Book by book", 1, "hbtable"))
story += [tbl([
    ["Class", "CT chapters", "Unplugged activities", "AI part", "Coding", "Projects"],
    ["3", "14", "**Caesar cipher** with a paper cipher wheel", "None", "None", "n/a"],
    ["4", "14", "**Coin Flip Magic** (parity, error detection); floor **Sorting Network**", "None", "None", "n/a"],
    ["5", "15", "**Searching with a weighing scale** (linear vs divide-and-conquer)", "None", "None", "n/a"],
    ["6", "10", "12-point circle step rule", "4 chapters: AI basics incl. supervised/unsupervised/reinforcement learning, data, patterns, digital ethics. No hands-on", "None", "**None**"],
    ["7", "8", "Punched-card sorting; logic punch cards", "4 chapters: domains, classification/regression/clustering, case studies, charts, bias. No hands-on", "None", "**None**"],
    ["8", "7", "Height in decimal/binary/ternary \"pipes\"", "4 chapters + **3 Teachable Machine labs**", "None", "**None**"],
], [0.07, 0.09, 0.27, 0.35, 0.09, 0.13])]
story += [tbl([
    ["", "Student Handbook", "Teacher Handbook"],
    ["Puzzles", "Questions only", "Same questions with worked solutions"],
    ["Activities", "Worksheet pages", "Lesson plan with timings (30-45 min), template/worksheet/video links, CT skills"],
    ["AI chapters (6-8)", "**Teaching text** with examples, then exercises", "**Exercises and answer keys only**"],
], [0.2, 0.4, 0.4])]
story.append(hours_bar())

findings = [
 ("7.4 Finding 1: built around the maths lesson", "f1",
  ["Every book is \"a companion to the Mathematics textbook\" and \"follows the same chapter sequence\". Chapter titles match the new NCERT maths books one for one (e.g. Class 3: _What's in a Name?_ … _The Surajkund Fair_; Class 8: _A Square and a Cube_ … _Proportional Reasoning_)."],
  "Index everything CodeSchool sells for Classes 3-8 by **NCERT maths chapter** so a teacher finds \"today's\" material in one tap."),
 ("7.5 Finding 2: the puzzles are hard, even in Class 3", "f2",
  ["Class 3 (age 8) includes finding the heavier of 12 balls in the fewest weighings, data-sufficiency questions and multi-clue passcodes. Student books give no hints or answers and no easier-to-harder ramp."],
  "Levels add real value: warm-ups, hints and worked examples for the same chapter skills, with harder levels for those ready."),
 ("7.6 Finding 3: rules, branching and search from Class 3, always as puzzles", "f3",
  ["Class 3: \"When on a WHITE block, he must skip the next TWO blocks. When on a BLACK block, … the next ONE\" (an if-then rule); a frog that jumps 4 and slips 2 (a loop); path tiles from Home. Class 4: a rule with an exception; tracing a button sequence. Class 5: linear search vs divide-and-conquer. Students only **follow** or **compare** algorithms, never **write** them."],
  "Band B levels as \"**the puzzle in this chapter, now you build it**\". Level B3 fits the Class 3 skip rule and Class 4 _Hide and Seek_ / _The Cleanest Village_."),
 ("7.7 Finding 4: no coding in any book, and CBSE says that's intended", "f4",
  ["Scratch is a listed Classes 3-5 competency and CG-3 covers computers, hardware and software, but none of the 12 books has content for either. The webinar says \"No coding/software\", \"no 'write a program'\", and for Class 6 \"Recognise — not build\"."],
  "The coding gap is real on paper but schools may not feel it. Sell coding as a \"now you build it\" extension or via parents, not as a CBSE requirement. **Test in interviews** (coordinator Q9, H10)."),
 ("7.8 Finding 5: 40% of Middle Stage time has no materials", "f5",
  ["Each of Classes 6-8 gives 40 h to \"two required projects\". No brief, rubric or example in any book, though the Class 6 book tells teachers to use \"clear rubrics\". The webinar gives one topic per grade (Class 6 weather across states; Class 7 \"Nutri-Quest\" meal planner; Class 8 sports data) and promises an \"AI Project list with rubrics\" as coming soon: still not on the CT&AI page six months later."],
  "**Project kits for Classes 6-8** cover 120 hours across three years. The window may close when CBSE publishes its list: check monthly and align to its topics."),
 ("7.9 Finding 6: AI is taught in student books; only Class 8 is hands-on", "f6",
  ["Student books explain AI in plain text with Indian examples (Turing Test, ML types, classification/regression/clustering, ICMR TB X-ray screening, Pune waste app). Teacher books carry only exercises and answer keys. Classes 6-7 have no hands-on AI. Class 8 has three Teachable Machine labs: a waste classifier (photos of plastic/paper/organic), voice commands (Start/Stop/Help) and a cat/dog bias test (dataset \"in the Drive\", no link in the text). Each group needs a computer, internet, webcam and microphone. The Class 8 text uses a six-stage lifecycle while its outcome uses four stages."],
  "**Teacher scripts and slides** for AI chapters; **hands-on AI for Classes 6-7**; a **device-light, projector version** of the Class 8 labs with datasets supplied."),
 ("7.10 Finding 7: few, borrowed, online-dependent activities", "f7",
  ["Eight unplugged CT activities across six classes, mostly adapted from CS Unplugged, relying on Google Docs, YouTube and tinyurl links; the sorting network has to be chalked on the floor."],
  "A printable, offline activity kit with a teacher script for **every** chapter."),
 ("7.11 Finding 8: continuous assessment, nothing to track it", "f8",
  ["Every book lists written CT puzzle tests, group activities and a **Teacher Observation Journal**; none gives a template, rubric or record."],
  "A simple observation journal and progress record mapped to CBSE competencies, printable for report cards."),
]
for title, key, body, sowhat in findings:
    story.append(H(title, 1, key))
    story += [P(b) for b in body]
    story.append(callout([P(sowhat)], "good", "So what for CodeSchool"))

story.append(H("7.12 What the CBSE webinar adds (28 April 2026)", 1, "webinar"))
story.append(P("Source: [webinar slides](https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf) (45 slides, read in full); [recording](https://youtube.com/live/KXYvvXZtYyk) not yet watched."))
story += [tbl([
    ["Topic", "What the slides say", "Implication"],
    ["Coding", "\"No coding/software\"; \"no 'write a program'… no expectation of computer access for assessment\"; \"largely unplugged\"", "Don't pitch \"CBSE requires coding\""],
    ["AI depth", "Class 6: \"Recognise — not build… don't need to write code or train models\"", "Class 8 labs go further than this"],
    ["Projects", "One data-project topic per grade; \"AI Project list with rubrics\" coming soon", "Biggest open gap; time-limited"],
    ["Coming soon", "Dedicated CT&AI page (now live); AI \"Concept Handouts\"; project list with rubrics", "Two of three still missing"],
    ["Who teaches 6-8", "CT through Maths, Science **and Social Sciences**; AI and projects \"anchored by the Computer teacher\"", "More teachers to support"],
    ["Training", "Annual theme \"Computational Thinking and Understanding AI\": district 1-day (6 CPD h), lead-school half-day (3 h), online, DD PM e-Vidya CBSE 15, regional workshops", "Short training → in-product guidance matters"],
    ["Teacher book claim", "\"Everything in the student handbook, plus\" solutions", "Not true for the 6-8 AI chapters"],
], [0.16, 0.54, 0.3])]
story.append(H("7.13 Don't compete with the books: sit on top of them", 1, "ontop"))
story += [tbl([
    ["CBSE gives (free)", "CodeSchool could give (paid)"],
    ["Puzzle banks by maths chapter, Classes 3-8", "The same skills as **levels** with hints, on-ramps and auto-checked practice, on phone, projector or paper"],
    ["No coding in any class", "**Block-coding levels** tied to each chapter's puzzles (\"now you build it\")"],
    ["8 unplugged activities across six classes", "An activity for every chapter, printable kits and a teacher script"],
    ["No project materials", "**Project kits for Classes 6-8**: briefs, rubrics, examples, assessment"],
    ["AI text in student books; answer keys for teachers", "**Teacher scripts and slides** for every AI chapter"],
    ["Hands-on AI only in Class 8, needing devices and internet", "**Hands-on AI for 6-7** and a device-light Class 8 lab version"],
    ["\"Teacher Observation Journal\" with no template", "A **progress journal and dashboard** mapped to CBSE competencies"],
], [0.42, 0.58])]

# =====================================================================
# 8 RISKS
story += section("8. Risks and open questions", "Three assumptions could fail: the CBSE curriculum holds, schools have devices, and principals pay for something CBSE gives away free.", "risks")
story += [tbl([
    ["Risk", "Why it matters", "Mitigation"],
    ["**Policy volatility**", "CBSE \"advises\" Classes 3-8 and deferred Class 9; Korea reversed AI textbooks", "Concept-based framework; board mapping as a swappable layer"],
    ["**CBSE says no coding** (new)", "Webinar presents no-coding as a design choice", "Lead with projects, AI support and assessment; coding as extension"],
    ["**CBSE fills the project gap** (new)", "Project list with rubrics promised", "Ship fast; align kits to CBSE topics; monitor monthly"],
    ["**Devices and labs**", "64.7% have computer facilities; many sanctioned labs not working", "Unplugged-first, printable kits, projector mode, offline Android"],
    ["**Free substitutes**", "Code.org, Scratch, CBSE books", "Sell alignment, assessment, teacher tooling, languages"],
    ["**Teacher capacity**", "Non-specialist teachers; one-day CBSE training", "Scripted PRIMM template, micro-videos, auto-grading, dashboard"],
    ["**Shallow puzzle progression**", "Points raise quantity, not quality", "A make step in every level; capstones"],
    ["**Advancing without mastery**", "Pacing pressure undermined Cognitive Tutor", "Mastery gates; logged overrides"],
    ["**Trust**", "WhiteHat Jr ads, suits and refunds damaged the sector", "Monthly billing, refund policy, no outcome claims"],
    ["**Sales cycle**", "Book lists close Dec-Jan", "Pilot-ready product and materials by ~September"],
    ["**Children's data**", "Data on minors", "Legal review of DPDP child-consent rules before launch"],
], [0.24, 0.38, 0.38])]
story.append(H("Open questions and how to answer them", 1, "openq"))
story += [tbl([
    ["Open question", "Ask whom", "How to validate"],
    ["Did schools implement CBSE CT&AI in 2026-27, with what?", "Principals, coordinators", "15-20 school interviews"],
    ["Will principals pay alongside free books, and how much?", "Principals, owners", "Price anchors; LOIs before December"],
    ["Can a maths teacher run a level in one period untrained?", "Class 3-5 teachers", "B3 paper prototype walkthrough"],
    ["What devices exist per class?", "Computer teachers, IT", "Device audit"],
    ["Do schools want coding despite CBSE's message?", "Coordinators, computer teachers", "Coordinator Q9; H10"],
    ["Which language mix first?", "Parents, teachers", "Survey in 2-3 states"],
    ["Coding, AI literacy or school-grade support for parents?", "Parents", "Indian parent survey (none exists)"],
    ["Does CISCE or a state board adopt Class 3 CT&AI?", "CISCE, SCERT", "Track circulars; ICSE heads"],
    ["Does placement + Express work in mixed classes?", "Pilot students", "Run in 2-3 Class 6-7 sections"],
], [0.42, 0.22, 0.36])]

# =====================================================================
# 9 ACTION PLAN (fillable)
story += section("9. Action plan", "Tick actions as you finish them, add an owner and change the status. Due dates are pre-filled and editable.", "actions")
story.append(callout([P("Fields are live: click a box to tick, type in Owner and Due, pick a Status. Save the file to keep your entries (outside the public repository).")], "info"))
STATUS = ["Not started", "In progress", "Done", "Blocked", "Dropped"]
groups = [
 ("A. This week: get ready (9-13 Nov)", [
   ("A1", "Fill [your number] / [your email] in the intro letter; decide on a Hindi version", "9 Nov"),
   ("A2", "Create a private notes folder outside the repo and a backup location", "9 Nov"),
   ("A3", "Print 20 copies of the B3 lesson (teacher pages 1-3, student page 4) and 20 device audit sheets", "11 Nov"),
   ("A4", "Copy the tracking sheet to a private file; shortlist 25-30 schools matching the sample mix", "13 Nov"),
   ("A5", "Send intro letters to the first 10 schools via networks and sahodaya complexes", "13 Nov"),
 ]),
 ("B. Interviews (16 Nov - 11 Dec)", [
   ("B1", "Run ~6 schools a week; 2-4 roles per school", "11 Dec"),
   ("B2", "Fill the interview note form on the same day as each interview", "ongoing"),
   ("B3", "Update the hypothesis tracker after every 5 schools", "every 5 schools"),
   ("B4", "Ask every coordinator about coding plans despite CBSE's \"no coding\" message (Q9)", "every school"),
   ("B5", "Ask whether CBSE's project list / rubrics or AI handouts have reached the school (Q8)", "every school"),
   ("B6", "Do a device audit wherever there is a computer teacher; check Class 8 lab readiness", "every school"),
 ]),
 ("C. Decide (14-18 Dec)", [
   ("C1", "Group quotes by theme per fee tier and board; write the 2-page findings memo", "16 Dec"),
   ("C2", "Apply the decision rule: go / no-go on a December pilot offer", "18 Dec"),
   ("C3", "If go: send pilot offers and collect letters of intent before book lists close", "Jan 2027"),
 ]),
 ("D. Close research gaps", [
   ("D1", "Watch the CBSE webinar recording for anything not on the slides", "20 Nov"),
   ("D2", "Read NCF-SE 2023 directly for the CT goal wording", "30 Nov"),
   ("D3", "Get CISCE Classes I-VIII Computer Studies guidelines and AI 417 / IT 402 syllabi", "30 Nov"),
   ("D4", "Open the handbook links: Google Docs worksheets, YouTube videos, Class 8 cat/dog dataset", "30 Nov"),
   ("D5", "Collect UDISE+ 2025-26 device and Class 3-8 enrolment data for a bottom-up market model", "Dec"),
   ("D6", "Legal review of DPDP Act child-data consent obligations", "before pilot"),
   ("D7", "Check Google Play ratings for PictoBlox, CuriousJr and Codingal", "Dec"),
 ]),
 ("E. Monitor CBSE", [
   ("E1", "Check the CT&AI page monthly for the project list with rubrics and Concept Handouts", "monthly"),
   ("E2", "Track circulars on Class 9 CT&AI for 2027-28 and any CISCE/state adoption", "monthly"),
 ]),
 ("F. Only after a \"go\" decision", [
   ("F1", "Map every NCERT maths chapter (Classes 3-8) to CT skills and candidate levels", "Jan 2027"),
   ("F2", "Draft one project kit per class, aligned with CBSE's example topics", "Feb 2027"),
   ("F3", "Design a device-light, projector version of the Class 8 Teachable Machine labs", "Feb 2027"),
   ("F4", "Write teacher scripts and slides for the Class 6 AI chapters", "Mar 2027"),
 ]),
 ("G. Go-to-market (added 6 Nov 2026)", [
   ("G1", "Apply the interview-guide changes and add H11-H13 (done in this version)", "13 Nov"),
   ("G2", "Check the current CBSE bye-laws text on supplementary and digital material", "20 Nov"),
   ("G3", "Get samples of Oxford, Goyal, Tekie.AI, Thinking Juggernaut and PiyushAI materials", "27 Nov"),
   ("G4", "Shortlist 3-5 coined brand names; trademark attorney search (Classes 9, 16, 28, 41, 42)", "4 Dec"),
   ("G5", "Tax adviser: GST on a printed workbook bundled with an access code", "4 Dec"),
   ("G6", "Confirm specimen and booklist deadlines with interviewed schools", "11 Dec"),
   ("G7", "Data-protection lawyer: the six DPDP questions and a school data processing agreement", "15 Jan 2027"),
 ]),
]
for g, items in groups:
    story.append(H(g, 1, None, g))
    rows = [["Done", "ID", "Action", "Owner", "Due", "Status"]]
    for aid, act, due in items:
        rows.append([FCheck(f"act_{aid}_done", tooltip=f"{aid} done"), f"**{aid}**", act,
                     FText(f"act_{aid}_owner", 0.12 * CW - 8, 13, "Anoop"),
                     FText(f"act_{aid}_due", 0.13 * CW - 8, 13, due),
                     FChoice(f"act_{aid}_status", STATUS, 0.15 * CW - 8)])
    story.append(tbl(rows, [0.075, 0.055, 0.47, 0.12, 0.13, 0.15], valign="MIDDLE"))

# =====================================================================
# 10 INTERVIEW PLAN
story += section("10. School interview plan", "Validate the research with 15-20 schools before any design or code. Interviews finish by mid-December, while schools are still choosing next year's resources.", "interviews")
story.append(gantt())
story.append(H("10.1 Hypotheses (H1-H13)", 1, "hyp"))
HYP = [
 ("H1", "CBSE schools are implementing CT&AI for Classes 3-8 in 2026-27", "Most have timetabled it, at least for some classes", "Most treat \"advised\" as optional and did nothing"),
 ("H2", "Schools struggle to deliver it with the teachers they have", "Coordinators name teacher capacity, planning or assessment", "Free CBSE books are enough"),
 ("H3", "Principals will pay for a product alongside the free books", "They name a budget line and price range, or accept an anchor", "\"We only use free material\" in target tiers"),
 ("H4", "A Rs 300-600 package is acceptable (Rs 449/599 booklist pack or Rs 299 + GST licence)", "Most mid/premium ceilings at or above Rs 300 for a package", "Ceilings consistently below Rs 300"),
 ("H5", "Unplugged-first lessons with optional devices fit real equipment", "Shared lab or projector only", "Every school has 1:1 devices"),
 ("H6", "A maths teacher can run one level in one period with a script", "B3 walkthrough fits a period with minor questions", "Can't run it without a CS teacher"),
 ("H7", "Assessment and reporting are a reason to buy", "Coordinators want dashboards and report-card grades", "Schools don't assess CT&AI"),
 ("H8", "ICSE schools have a similar need for Classes 1-8", "ICSE heads describe a gap or want CT&AI alignment", "Happy with publisher textbook"),
 ("H9", "Schools want a Scratch-to-Python route for Classes 6-10", "Students reach Class 11 Python unprepared; demand for earlier Python", "Content with Scratch until Class 11"),
 ("H10", "What CBSE didn't provide is what schools struggle with: coding, projects, hands-on AI, journal", "Named as unsolved, unprompted", "Free handbooks cover their needs"),
 ("H11", "Schools will put a CT&AI workbook with app access on the booklist", "Principals name the booklist as the route", "New booklist items blocked and no school budget"),
 ("H12", "Schools will replace their current Computers book with a combined pack", "Principals name the book they would drop", "Locked into a multi-year series"),
 ("H13", "Student-data handling matters to buyers", "Coordinators raise data or consent unprompted", "Nobody cares; compliance is a cost, not a selling point"),
]
story += [tbl([["#", "Hypothesis", "Supported if", "Kill signal"]] + [[f"**{a}**", b, c, d] for a, b, c, d in HYP],
              [0.06, 0.36, 0.3, 0.28])]
story.append(H("10.2 Who to interview", 1, "sample"))
story += [tbl([
    ["Dimension", "Mix (15-20 schools, 40-60 interviews)"],
    ["Board", "About 12 CBSE, 4-5 ICSE, 1-2 state board (Kerala best comparison)"],
    ["Fee tier", "Budget (< Rs 30,000), mid (Rs 30,000-1,00,000), premium (> Rs 1,00,000): about a third each"],
    ["Location", "At least 3 states; metro, tier 2 and tier 3"],
    ["School type", "Mostly standalone private; 2-3 chain schools"],
    ["Language", "At least 4 schools teaching mainly in Hindi or a regional language"],
], [0.22, 0.78])]
story += [tbl([
    ["Role", "Why", "Length"],
    ["Principal / owner", "Budget, decision, price", "30 min"],
    ["CBSE / academic coordinator", "Implementation, timetable, assessment", "30-40 min"],
    ["Class 3-5 maths or EVS teacher", "Who actually teaches CT in 3-5; paper prototype", "40 min"],
    ["Computer teacher", "Devices, labs, Classes 6-8 AI and projects", "30 min"],
    ["Parents (optional)", "Home practice, AI vs coding priorities", "15 min"],
], [0.3, 0.55, 0.15])]
story.append(P("**Recruiting:** personal and alumni networks → school associations and sahodaya complexes → LinkedIn outreach to coordinators. Offer a free cross-school summary; don't offer discounts on a product that doesn't exist."))
story.append(callout(bullets([
    "**Learn, don't sell.** No pitch until the last five minutes, and only if asked.",
    "**Past behaviour, not hypotheticals.** \"What did you buy last year?\" beats \"Would you buy…?\"",
    "**Consent first.** Verbal consent for notes; permission before recording; school won't be named.",
    "**No children.** No student interviews or recordings; observation needs written permission.",
    "**Record evidence.** Direct quotes, attributed by role, not name.",
]), "warn", "Ground rules"))
story.append(H("10.3 Interview guides", 1, "guides"))
GUIDES = [
 ("Principal or owner (30 min)", [
   "Tell me about the school: board, students, classes, fees roughly.",
   "Who decides which books and digital products the school buys, and when? **Who signs the website book list; does a fee committee review it?**",
   "How are you handling CBSE's CT&AI curriculum this year? (ICSE: how do you teach computers in Classes 1-8?)",
   "**Which Computers and CT&AI books are on your 2026-27 list, from which publisher, at what price? Did you consider Oxford, Goyal or Uolo's Tekie?**",
   "What's working, and what isn't?",
   "Walk me through the last time you bought a new academic product.",
   "When do your book lists close? **How do publishers work with you (specimens, training, terms), and by when must specimens arrive?** Don't ask about commissions.",
   "**Which fee heads do you charge (computer, smart class, activity)? Would a new product go on the book list, an existing fee, or the school budget? Has a fee committee ever questioned a charge?**",
   "**Do parents buy books from the school, a named shop, or anywhere?**",
   "**Price anchors (packages):** \"a Rs 300 licence plus GST, a Rs 450-600 workbook with app access on the book list, or an Rs 800 book-plus-platform with training: easy, hard or impossible?\" Then: **would it replace your current computer book?**",
   "If you could fix one thing about how computing or CT&AI is taught here, what would it be?",
   "Who else should I talk to? Open to a free pilot in one or two sections?"]),
 ("CBSE / academic coordinator (30-40 min)", [
   "Has CT&AI been timetabled for Classes 3-8? Which classes, how many periods?",
   "Who teaches it in Classes 3-5? In Classes 6-8?",
   "Are you using the free CBSE books? How are teachers finding them?",
   "Did teachers attend CBSE training (district/regional workshops, lead-school sessions, DD PM e-Vidya videos)? Useful?",
   "How is CT&AI assessed? **CBSE hasn't published marks weightage or a report-card format. What will this year's report card show?**",
   "What do parents ask about it?",
   "What would make it easier: lesson plans, worksheets, a platform, training, assessment tools?",
   "Classes 6-8 have 40 hours of projects and the books have no materials. What are students doing? Who designs and marks them? **Has CBSE's promised project list with rubrics arrived?**",
   "**CBSE's webinar says \"no coding/software\". Will the school teach Scratch or any coding in Classes 3-8 anyway? Why or why not?**",
   "How are teachers keeping the Teacher Observation Journal? Is there a format?",
   "Have vendors approached you about CT&AI (**Oxford, Goyal, Uolo Tekie, STEMpedia, LEAD, Thinking Juggernaut, PiyushAI, Scaleopal**)? What did they offer, at what price?",
   "**When an app needs student logins, who creates them and what does the school share? Does the school take parent consent for apps? Has anyone raised the DPDP Act?**",
   "(ICSE) Anything from CISCE about CT or AI for younger classes?"]),
 ("Class 3-5 maths or EVS teacher (40 min)", [
   "How long have you been teaching, which subjects?",
   "Have you taught CT&AI lessons yet? Tell me about the last one.",
   "What was hardest? Are the handbook puzzles too easy, about right, too hard? Have you tried the activities (Caesar cipher, Coin Flip Magic, Sorting Network, weighing-scale search)?",
   "How much time do you have to plan a new lesson each week?",
   "Have you used computer or tablet activities with your class? What happened?",
   "**Paper prototype (20 min):** walk through the [B3 lesson](#b3), then: Could you run this tomorrow? Hardest step? What would you change? Projector, paper or lab?",
   "What would make you look forward to teaching this?"]),
 ("Computer teacher (30 min)", [
   "**Device audit** (use the [audit form](#audit)): devices, lab sharing, internet, projectors, OS and age.",
   "What do you teach in Classes 3-8 today, with which tools?",
   "CBSE gives you the AI literacy part and project assessment in Classes 6-8. Doing it this year? With which tools? **The Class 8 book has three Teachable Machine labs: has anyone run them? Do you have webcams, microphones and internet?**",
   "When do students first write Python? CBSE has none before Class 11. How do students cope with Class 11 Python?",
   "What do students find hardest moving from blocks to typing code?",
   "**How do students log in to any platform today: roll number, school email or a parent's phone?**"]),
 ("Parents (optional, 15 min)", [
   "What does your child do in computer or CT&AI class? How do you know?",
   "What do you want them to learn about computers and AI?",
   "Have you paid for coding classes or apps outside school? Why stop or continue?",
   "If the school program had home practice, how much would you pay a month?",
   "What would make you trust an education app? **Comfortable with the school giving an app your child's class and roll number? Do you use DigiLocker?**",
   "**Where did you buy this year's books?**"]),
]
for title, qs in GUIDES:
    story.append(H(title, 2, None, title))
    story += [Paragraph(md(q), BUL, bulletText=f"{i}.") for i, q in enumerate(qs, 1)]
story.append(H("10.4 Analysis and decision rule", 1, "decision"))
story += bullets([
    "Fill the [note form](#noteform) the same day.",
    "Every 5 schools, update the [hypothesis tracker](#tracker).",
    "After all interviews, group quotes by theme (affinity mapping) separately per fee tier and board.",
    "Write a 2-page memo: what we learned, which hypotheses held, what changes, and whether to make a pilot offer.",
])
story.append(callout([P("**Go ahead with a December pilot offer if H1, H2 and H3 are supported in at least half of the CBSE schools, H4 holds in the mid and premium tiers, and H11 (booklist route) holds in at least half of mid- and premium-tier schools.** If H1 fails, the product shouldn't depend on the CBSE circular: revisit the parent channel and the ICSE and state-board angles.")], "accent", "Decision rule"))
story += [tbl([
    ["Week", "Dates (2026)", "Work"],
    ["1", "9-13 Nov", "Finalise guides, print the B3 prototype, start recruiting"],
    ["2-4", "16 Nov - 4 Dec", "Interviews: about 6 schools a week"],
    ["5", "7-11 Dec", "Final interviews, tally hypotheses"],
    ["6", "14-18 Dec", "Findings memo and go/no-go on the pilot offer"],
], [0.12, 0.25, 0.63])]

# =====================================================================
# 11 HYPOTHESIS TRACKER (fillable)
story += section("11. Hypothesis tracker", "Update after every 5 schools: count schools where the evidence was For, Against or Unclear, then set a running verdict.", "tracker")
VERD = ["Too early", "Supported", "Mixed", "Not supported"]
rows = [["#", "Hypothesis", "For", "Against", "Unclear", "Verdict", "Key quote / note"]]
for a, b, c, d in HYP:
    rows.append([f"**{a}**", b, FText(f"h_{a}_for", 0.08 * CW - 10, 14), FText(f"h_{a}_against", 0.08 * CW - 10, 14),
                 FText(f"h_{a}_unclear", 0.08 * CW - 10, 14), FChoice(f"h_{a}_verdict", VERD, 0.13 * CW - 10, 14),
                 FText(f"h_{a}_note", 0.26 * CW - 10, 26, multiline=True)])
story.append(tbl(rows, [0.07, 0.30, 0.08, 0.08, 0.08, 0.13, 0.26], valign="MIDDLE"))
story.append(Spacer(1, 8))
story.append(labeled_field("Schools interviewed so far", "tracker_count", 0.3))
story.append(labeled_field("CBSE schools where H1+H2+H3 supported", "tracker_h123", 0.3))
story.append(labeled_field("H4 holds in mid and premium tiers?", "tracker_h4", 0.3))
story.append(labeled_field("Running decision", "tracker_decision", 0.3, value="Too early to call"))

# =====================================================================
# 12 MATERIALS
story += section("12. Interview materials", "Ready to use: intro letter, opening script, the Level B3 paper lesson, and fillable forms for notes and the device audit.", "materials")
story.append(H("12.1 Introduction letter (one page)", 1, "letter"))
letter = [
 "Dear [Principal / Coordinator name],",
 "I'm **Anoop Dobhal**, and I'm researching how schools are teaching **Computational Thinking and AI** in Classes 3-8, including CBSE's new curriculum for 2026-27. Before building anything, I want to understand what schools and teachers actually need.",
 "**I'm requesting short conversations** with up to four people at [School name]: the principal or owner (30 min), the academic or CBSE coordinator (30-40 min), a Class 3-5 maths or EVS teacher (40 min, including feedback on one printed sample lesson) and the computer teacher, if any (30 min). In person, by phone or by video, between **16 November and 11 December 2026**.",
 "**What I'll ask about:** how CT&AI and computer classes are going, what teachers find hard, what equipment is available, and how the school chooses resources. **What this isn't:** a sales visit. There's no product to buy yet.",
 "**Your privacy:** the school and staff won't be named in anything I share; notes only, audio only with agreement; I won't talk to, photograph or record any students; you can skip any question or stop at any time.",
 "**What you get:** a free summary of what I learn from 15-20 schools, sent in January 2027.",
 "Phone / WhatsApp: [your number] · Email: [your email]",
 "Warm regards, Anoop Dobhal, CodeSchool",
]
story.append(callout([P(x) for x in letter], "info"))
story.append(H("12.2 Opening script (read aloud)", 1, "script"))
story.append(callout([P("_\"Thank you for your time. I'm researching how schools teach computational thinking and AI, so that anything we build later actually helps teachers and students. This isn't a sales call. I'll take notes. Is it all right if I also record the audio, just for my own notes? It won't be shared. Your name and the school's name won't appear in anything I share. You can skip any question or stop at any time. Do you have any questions before we start?\"_")], "accent"))

story.append(H("12.3 Level B3: Robo makes choices (paper prototype)", 1, "b3"))
story += [tbl([
    ["**Band / level**", "B (Builders, Classes 3-5) · Level B3: conditionals"],
    ["**Written for**", "Class 4 (works for Classes 3-5) · one 40-minute period · no devices (projector optional)"],
    ["**Structure**", "PRIMM + Parsons: Predict & Run → Investigate → Modify → Parsons → Make"],
    ["**Learning goal**", "Explain that an **if-else** block makes the program choose between two actions, checked every time the loop repeats"],
    ["**Curriculum link**", "Class 4 _Hide and Seek_ and _The Cleanest Village_; Class 3 skip rule (_Filling and Lifting_). Explicit if-then is a CBSE Class 7 outcome, so B3 is a deliberate stretch the interviews test"],
], [0.22, 0.78], header=False)]
def code(lines):
    t = Table([[Paragraph("<br/>".join(esc(l).replace(" ", "&nbsp;") for l in lines), CODE)]], colWidths=[CW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F1F4F6")),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 6),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return t
story.append(H("Step 1. Predict and run (8 min)", 2))
story.append(code(["   1          2          3          4          5",
                   "[ START ]  [ PUDDLE ]  [ plain ]  [ PUDDLE ]  [ plain ]",
                   "  Robo >", "",
                   "when green flag clicked", "repeat 4 times", "    move forward 1 square",
                   "    if < on a puddle? > then", "        say [Splash!]", "    else", "        say [Step]", "    end", "end"]))
story.append(P("Pairs write what Robo will say before running it. One student acts as Robo on the floor grid. **Answer:** Splash! · Step · Splash! · Step."))
story.append(H("Step 2. Investigate (8 min)", 2))
story += [tbl([
    ["#", "Question", "Answer", "Listen for"],
    ["1", "How many times did Robo say \"Splash!\"? Why?", "2: on a puddle twice", "Linking output to squares"],
    ["2", "Which block makes Robo choose?", "The if-else block", "Not pointing to \"repeat\""],
    ["3", "If every square were plain?", "Step × 4", "Else runs when the condition is false"],
    ["4", "If the if-else were after (outside) the repeat?", "Checks once, on square 5: \"Step\"", "**Hardest:** checking every time needs the loop"],
], [0.05, 0.4, 0.27, 0.28])]
story.append(P("**Misconceptions:** \"both branches run\" (point to if… then… else); \"the if checks once at the start\" (act it out square by square)."))
story.append(H("Steps 3-5: modify, Parsons, make (22 min)", 2))
story += bullets([
    "**Modify (8 min):** new row with STAR squares; change only the if-else so Robo says \"Star!\". Output: Step · Star! · Star! · Step. Stretch: jump instead of speaking.",
    "**Parsons (8 min):** reorder jumbled blocks so Robo reaches GOAL without hitting a wall; `turn left` is the trick block. Answer: `repeat 6 times / if wall ahead then turn right else move forward`.",
    "**Make (6 min):** pairs draw five squares and write \"If Robo is on a ___ square, then ___, else ___\"; swap and predict.",
    "**Exit ticket (2 min):** `[START][puddle][puddle][plain]`, repeat 3 → Splash! · Splash! · Step; circle the choosing block.",
])
story.append(P("Full teacher script and student sheet: [level-b3-paper-prototype.md](https://github.com/evolvian2026/CodeSchool/blob/main/docs/research/interview-materials/level-b3-paper-prototype.md).", SMALL))

# B3 observation sheet (fillable)
story.append(CondPageBreak(120 * mm))
story.append(H("12.4 B3 observation sheet (fillable)", 1, "b3obs"))
story.append(labeled_field("School code · teacher role · date", "b3_header", 0.3))
rows = [["Step", "Planned", "Teacher's estimate", "Questions or hesitations (quote)", "Would change it?"]]
for i, (stp, mins) in enumerate([("1. Predict and run", "8 min"), ("2. Investigate", "8 min"), ("3. Modify", "8 min"),
                                  ("4. Parsons puzzle", "8 min"), ("5. Make", "6 min"), ("Exit ticket", "2 min")]):
    rows.append([stp, mins, FText(f"b3_est_{i}", 0.14 * CW - 8, 13), FText(f"b3_q_{i}", 0.4 * CW - 8, 24, multiline=True),
                 FChoice(f"b3_chg_{i}", ["-", "No", "Small change", "Big change"], 0.16 * CW - 8)])
story.append(tbl(rows, [0.18, 0.12, 0.14, 0.4, 0.16], valign="MIDDLE"))
story.append(Spacer(1, 6))
for i, q in enumerate(["Could you run this in one period tomorrow? What would stop you?",
                       "Which step would your students find hardest?",
                       "What would you change?",
                       "Projector, paper or computer lab?",
                       "Is the answer key enough, or would you need more help? What kind?",
                       "Which maths chapter could this sit inside? Is if-else too early for Class 4?"], 1):
    story.append(labeled_field(f"{i}. {q}", f"b3_after_{i}", 0.42, 24, True))
sc = Table([[Paragraph("<b>Teacher could run it without help</b>", CELL), FChoice("b3_score_run", ["-", "Yes", "With small changes", "No"], 0.25 * CW),
             Paragraph("<b>Estimated total time</b>", CELL), FChoice("b3_score_time", ["-", "Fits one period", "Needs two periods", "Unclear"], 0.22 * CW)]],
           colWidths=[0.24 * CW, 0.27 * CW, 0.24 * CW, 0.25 * CW])
sc.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 6)]))
story.append(sc)

# Interview note form
story += [NextPageTemplate("body"), PageBreak(), H("12.5 Interview note form (fillable)", 1, "noteform")]
story.append(callout([P("One form per interview. Use **school codes (S01-S20)** and roles, never names. Save filled copies outside the repository.")], "risk"))
story.append(labeled_field("School code · role · date", "n_header", 0.3))
story.append(labeled_field("Board / fee tier / city type / medium", "n_profile", 0.3))
story.append(labeled_field("Interviewer", "n_interviewer", 0.3, value="Anoop Dobhal"))
rec = Table([[Paragraph("<b>Audio recorded (with consent)</b>", CELL), FCheck("n_recorded"),
              Paragraph("<b>CT&amp;AI timetabled</b>", CELL), FChoice("n_timetabled", ["-", "Yes", "Partly", "No", "Not CBSE"], 0.2 * CW),
              Paragraph("<b>Device summary</b>", CELL), FChoice("n_devices", ["-", "A paper only", "B lab weekly or less", "C projector", "D 1 per 2", "E near 1:1"], 0.2 * CW)]],
            colWidths=[0.2 * CW, 0.06 * CW, 0.15 * CW, 0.22 * CW, 0.13 * CW, 0.24 * CW])
rec.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
story += [rec, Spacer(1, 4)]
story.append(labeled_field("Key quotes", "n_quotes", 0.3, 54, True))
story.append(labeled_field("Current product and cost", "n_product", 0.3))
story.append(labeled_field("Book list closes", "n_booklist", 0.3))
pa = Table([[Paragraph("<b>Price-anchor reaction</b>", CELLB)] +
            sum([[Paragraph(lab, CELL), FChoice(f"n_price_{k}", ["-", "Easy", "Hard", "Impossible"], 0.12 * CW)] for k, lab in (("300", "Rs 300 licence"), ("500", "Rs 450-600 pack"), ("800", "Rs 800 platform"))], [])],
           colWidths=[0.16 * CW] + [0.14 * CW, 0.14 * CW] * 3)
pa.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
story += [pa, Spacer(1, 4)]
EV = ["Not discussed", "For", "Against", "Unclear"]
rows = [["#", "Hypothesis (short)", "Evidence", "Notes / quote"]]
for a, b, c, d in HYP:
    rows.append([f"**{a}**", b, FChoice(f"n_{a}_ev", EV, 0.15 * CW - 6), FText(f"n_{a}_note", 0.37 * CW - 8, 14)])
story.append(tbl(rows, [0.07, 0.39, 0.16, 0.38], valign="MIDDLE"))
story.append(Spacer(1, 4))
story.append(labeled_field("Surprises", "n_surprises", 0.3, 36, True))
story.append(labeled_field("Follow-ups", "n_followups", 0.3, 36, True))

# Device audit
story += [NextPageTemplate("body"), PageBreak(), H("12.6 Device audit (fillable)", 1, "audit")]
story.append(P("Fill with the computer teacher or IT staff, one per school. Write **numbers**, not impressions; write \"don't know\" rather than guessing. Ask to see the lab."))
story.append(labeled_field("School code · date · filled with (role)", "a_header", 0.34))
AUD = [
 ("1. Computer lab", ["Number of computer labs", "Computers in main lab (total)", "…of which working today", "Operating system",
                      "Approx. age of most computers (years)", "Typical RAM", "Students in a typical section",
                      "Students per working computer in a lab period", "Sections sharing the lab", "Lab minutes/week: Class 4 section",
                      "Lab minutes/week: Class 7 section", "Scratch / PictoBlox installed? Online or offline?", "Python installed?"]),
 ("2. Tablets and other devices", ["School-owned tablets", "…Android / iPad / other", "…working today", "Which classes can use them?",
                                   "Do students bring phones/tablets for classwork?"]),
 ("3. Classrooms", ["Classrooms (Classes 3-8)", "…with projector or smart board", "…working today",
                    "…with teacher laptop/PC connected", "Projector in Class 3-5 rooms?"]),
 ("4. Internet and Class 8 labs", ["Internet in lab (yes / no / unreliable)", "Internet in classrooms", "Connection type",
                                   "How often does it fail in a lesson?", "Filter? Is scratch.mit.edu / teachablemachine allowed?",
                                   "Webcams available (number)", "Microphones / headsets available (number)"]),
 ("5. Power, support and funding", ["Power cuts in school hours", "Backup power for lab", "Who fixes devices, how long?",
                                    "Lab funded by a scheme (Samagra Shiksha ICT, ATL)?", "Atal Tinkering Lab? In use?",
                                    "Devices planned for next session?"]),
]
for title, qs in AUD:
    story.append(H(title, 2))
    rows = [[Paragraph(md(q), CELL), FText(f"a_{title[0]}_{i}", 0.5 * CW - 10, 13)] for i, q in enumerate(qs)]
    t = tbl(rows, [0.5, 0.5], header=False, valign="MIDDLE")
    story.append(t)
story.append(Spacer(1, 6))
summ = Table([[Paragraph("<b>Interviewer's summary</b>", CELLB),
               FChoice("a_summary", ["-", "A: few/no devices, paper", "B: shared lab weekly or less", "C: projector in most rooms",
                                      "D: ~1 device per 2 students", "E: near 1:1"], 0.5 * CW)]], colWidths=[0.3 * CW, 0.7 * CW])
summ.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
story += [summ, Spacer(1, 4), labeled_field("Notes", "a_notes", 0.3, 40, True)]

story.append(H("12.7 Tracking sheet (columns)", 1, "trackcols"))
story.append(P("Use [tracking-sheet-template.csv](https://github.com/evolvian2026/CodeSchool/blob/main/docs/research/interview-materials/tracking-sheet-template.csv) for S01-S20; copy it to a **private** file before adding contacts. Better: use the [Research Tracker workbook](https://github.com/evolvian2026/CodeSchool/blob/main/docs/research/CodeSchool-Research-Tracker.xlsx), which logs H1-H13 evidence and checks the decision rule automatically."))

# =====================================================================
# 13 APPENDIX
story += section("13. Appendix", "Document index, key sources and glossary.", "appendix")
story.append(H("13.1 Documents in the repository", 1, "docindex"))
GH = "https://github.com/evolvian2026/CodeSchool/blob/main/"
story += [tbl([
    ["Document", "What it contains"],
    [f"[README.md]({GH}README.md)", "Project overview and links to all research"],
    [f"[Kids coding curriculum and market]({GH}docs/research/reports/Kids%20coding%20curriculum%20and%20market.md)", "Main research report (sections 3-5, 8)"],
    [f"[Research notes]({GH.replace('/blob/', '/tree/')}docs/research/research_notes/Kids%20coding%20curriculum%20and%20market)", "India curriculum, global curricula, learning progression, market landscape"],
    [f"[cbse-verification.md]({GH}docs/research/cbse-verification.md)", "CBSE claims checked against official documents (section 6)"],
    [f"[cbse-handbook-review.md]({GH}docs/research/cbse-handbook-review.md)", "All 12 handbooks + webinar (section 7)"],
    [f"[school-interview-plan.md]({GH}docs/research/school-interview-plan.md)", "Hypotheses, sample, guides, analysis, timeline (section 10)"],
    [f"[interview-materials/]({GH.replace('/blob/', '/tree/')}docs/research/interview-materials)", "Intro letter, B3 lesson, device audit, tracking sheet (section 12)"],
], [0.42, 0.58])]
story.append(H("13.2 Key official sources", 1, "sources"))
SRC = [
 ("CBSE CT&AI page (all handbooks)", "https://cbseacademic.nic.in/ct-ai.html"),
 ("CBSE CT&AI curriculum, Classes 3-8 (2026-27)", "https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_Pri_2026-27.pdf"),
 ("Circular Acad-15/2026: launch", "https://cbseacademic.nic.in/web_material/Circulars/2026/15_Circular_2026.pdf"),
 ("Circular Acad-18/2026: resource books", "https://cbseacademic.nic.in/web_material/Circulars/2026/18_Circular_2026.pdf"),
 ("Circular Acad-70/2026: Class 9 scheme", "https://cbseacademic.nic.in/web_material/Circulars/2026/70_Circular_2026.pdf"),
 ("CBSE webinar slides, 28 April 2026", "https://cbseacademic.nic.in/web_material/CurriculumMain27/CTAI_WebinarPPT_2026-27.pdf"),
 ("CBSE webinar recording", "https://youtube.com/live/KXYvvXZtYyk"),
 ("Computer Applications 165, Class IX", "https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart1/Computer_Applications_SecP1IX_2026-27.pdf"),
 ("Computer Science 083", "https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Computer_Science_SecP2_2026-27.pdf"),
 ("Informatics Practices 065", "https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Informatics_Practices_SecP2_2026-27.pdf"),
 ("NEP 2020", "https://static.pib.gov.in/WriteReadData/userfiles/NEP_Final_English_0.pdf"),
 ("Samagra Shiksha ICT (DoSEL)", "https://dsel.education.gov.in/scheme/ict-samagra"),
 ("CSTA PK-12 Standards (2026)", "https://csteachers.org/pk12standards/"),
 ("England computing programmes of study", "https://www.gov.uk/government/publications/national-curriculum-in-england-computing-programmes-of-study/national-curriculum-in-england-computing-programmes-of-study"),
 ("Costa 2023: game concepts in programming learning", "https://repositorio.iscte-iul.pt/bitstream/10071/29213/1/article_95533.pdf"),
 ("Sentance, Waite & Kallia 2019: PRIMM", "https://core.ac.uk/download/237088209.pdf"),
 ("CS Unplugged", "https://www.csunplugged.org/"),
 ("Teachable Machine", "https://teachablemachine.withgoogle.com"),
]
story += [tbl([["Source", "Link"]] + [[a, f"[{u.replace('https://', '')[:70]}{'…' if len(u) > 78 else ''}]({u})"] for a, u in SRC], [0.4, 0.6])]
story.append(P("The main report has the full list of 100+ labelled sources, including news and secondary items.", SMALL))
story.append(H("13.3 Glossary", 1, "glossary"))
story += [tbl([
    ["Term", "Meaning"],
    ["CT", "Computational thinking: decomposition, pattern recognition, abstraction, algorithms, data, troubleshooting"],
    ["CT&AI", "CBSE's Computational Thinking and Artificial Intelligence curriculum for Classes 3-8 (2026-27)"],
    ["TWAU", "The World Around Us, the NCERT environmental studies subject in Classes 3-5"],
    ["SH / TH", "Student Handbook / Teacher Handbook"],
    ["NCF-SE", "National Curriculum Framework for School Education, 2023"],
    ["PRIMM", "Predict, Run, Investigate, Modify, Make: a lesson structure for programming"],
    ["Parsons problem", "Put jumbled code blocks in the right order"],
    ["Band / level", "CodeSchool's proposed multi-class bands (A-E) made of mastery-gated levels"],
    ["Express track", "A fast catch-up route for older beginners"],
    ["B2B2C", "Sell to schools, reach parents through the school"],
    ["GeM", "Government e-Marketplace, India's public procurement portal"],
    ["CPD", "Continuing professional development for teachers"],
    ["DPDP Act", "India's Digital Personal Data Protection Act, 2023"],
    ["LOI", "Letter of intent"],
], [0.2, 0.8])]

# =====================================================================
doc = Doc(OUT)
doc.multiBuild(story)
print("built", OUT)
