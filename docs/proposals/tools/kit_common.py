"""Shared helpers: reuses styles, flowables and form fields from build_pack.py
(everything above its story section), plus a configurable cover and page chrome."""
import sys, pathlib

BP = pathlib.Path(__file__).with_name("build_pack.py")
MARK = "# =====================================================================\nstory = []"

def load(out):
    src = BP.read_text(encoding="utf-8").split(MARK)[0]
    ns = {"__name__": "kitlib"}
    argv = sys.argv
    sys.argv = [str(BP), out]
    exec(compile(src, str(BP), "exec"), ns)
    sys.argv = argv
    return ns

def make_doc_class(ns, kit_name, cover_kicker, cover_title, cover_lines, cover_meta, footer_date="6 November 2026"):
    g = ns
    A4, LM, RM, TM, BM, CW, PAGE_W, PAGE_H = (g[k] for k in "A4 LM RM TM BM CW PAGE_W PAGE_H".split())
    colors, mm, stringWidth = g["colors"], g["mm"], g["stringWidth"]
    PRIMARY, ACCENT, RULE, MUTED = g["PRIMARY"], g["ACCENT"], g["RULE"], g["MUTED"]
    BaseDocTemplate, PageTemplate, Frame, Doc = g["BaseDocTemplate"], g["PageTemplate"], g["Frame"], g["Doc"]

    def chrome(canv, doc):
        canv.saveState()
        canv.setFillColor(PRIMARY); canv.rect(0, PAGE_H - 9 * mm, PAGE_W, 9 * mm, fill=1, stroke=0)
        canv.setFillColor(colors.white); canv.setFont("UI-B", 8)
        canv.drawString(LM, PAGE_H - 6 * mm, f"CodeSchool  ·  {kit_name}")
        canv.setFont("UI", 8); canv.drawRightString(PAGE_W - RM, PAGE_H - 6 * mm, doc.section)
        canv.setStrokeColor(RULE); canv.setLineWidth(0.5); canv.line(LM, 12 * mm, PAGE_W - RM, 12 * mm)
        canv.setFillColor(MUTED); canv.setFont("UI", 7.5)
        canv.drawString(LM, 8 * mm, f"{footer_date}  ·  github.com/evolvian2026/CodeSchool")
        canv.drawRightString(PAGE_W - RM, 8 * mm, f"Page {doc.page}")
        canv.setFillColor(PRIMARY); canv.setFont("UI-B", 7.5)
        label = "↑ Back to contents"; w = stringWidth(label, "UI-B", 7.5); x = PAGE_W / 2 - w / 2
        canv.drawString(x, 8 * mm, label)
        canv.linkRect("", "contents", (x - 2, 6.5 * mm, x + w + 2, 11 * mm), relative=0, thickness=0)
        canv.restoreState()

    def cover(canv, doc):
        canv.saveState()
        canv.setFillColor(PRIMARY); canv.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        canv.setFillColor(colors.HexColor("#0E6A7A")); canv.rect(0, 0, PAGE_W, PAGE_H * 0.36, fill=1, stroke=0)
        canv.setFillColor(ACCENT); canv.rect(LM, PAGE_H - 62 * mm, 26 * mm, 2.2 * mm, fill=1, stroke=0)
        canv.setFillColor(colors.white); canv.setFont("UI-B", 11)
        canv.drawString(LM, PAGE_H - 50 * mm, cover_kicker)
        canv.setFont("UI-B", 32); canv.drawString(LM, PAGE_H - 80 * mm, cover_title)
        canv.setFont("UI", 14.5); y = PAGE_H - 92 * mm
        for line in cover_lines:
            canv.drawString(LM, y, line); y -= 7 * mm
        canv.setFont("UI", 10.5); canv.setFillColor(colors.HexColor("#CFE7EA"))
        y = PAGE_H * 0.36 - 22 * mm
        for line in cover_meta:
            canv.drawString(LM, y, line); y -= 7 * mm
        canv.restoreState()

    class KitDoc(Doc):
        def __init__(self, fn):
            BaseDocTemplate.__init__(self, fn, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM,
                                     bottomMargin=BM, title=f"CodeSchool {kit_name}", author="Anoop Dobhal (CodeSchool)",
                                     subject=f"CodeSchool school research: {kit_name}")
            self.section = ""
            fr = Frame(LM, BM, CW, PAGE_H - TM - BM, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
            self.addPageTemplates([PageTemplate("cover", [fr], onPage=cover),
                                   PageTemplate("body", [fr], onPageEnd=chrome)])
    return KitDoc
