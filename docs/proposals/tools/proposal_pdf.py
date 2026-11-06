"""Editable proposal pipeline: markdown (with a small front-matter block) -> styled, interactive PDF.

Markdown supported: ## / ### headings, paragraphs, - bullets (two-space indent for sub-bullets),
1. numbered lists, | tables |, > callouts (optional [!good] [!warn] [!risk] [!accent] tag),
[[RESPONSE_FORM]] (fillable school response form), [[PAGEBREAK]].
"""
import sys, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit_common import load, make_doc_class

MD, OUT = sys.argv[1], sys.argv[2]
globals().update(load(OUT))

raw = pathlib.Path(MD).read_text(encoding="utf-8").splitlines()
fm, body = {}, raw
if raw and raw[0].strip() == "---":
    end = raw.index("---", 1)
    for ln in raw[1:end]:
        k, _, v = ln.partition(":")
        fm[k.strip()] = v.strip()
    body = raw[end + 1:]


def expand(lines, base, depth=0):
    """Replace [[INCLUDE relative/path.md]] lines with that file's lines (shared sections)."""
    out = []
    for ln in lines:
        m = re.fullmatch(r"\s*\[\[INCLUDE\s+(.+?)\]\]\s*", ln)
        if m and depth < 3:
            inc = (base / m.group(1)).resolve()
            out += expand(inc.read_text(encoding="utf-8").splitlines(), inc.parent, depth + 1)
        else:
            out.append(ln)
    return out


body = expand(body, pathlib.Path(MD).resolve().parent)
split = lambda v: [x.strip() for x in v.split("|")] if v else []

KitDoc = make_doc_class(globals(), fm.get("header", "Proposal"), fm.get("kicker", "CODESCHOOL"),
                        fm.get("title", "Proposal"), split(fm.get("lines")), split(fm.get("meta")))


def inline(s):
    links = []
    def grab(m):
        links.append((m.group(1), m.group(2))); return f"\x00{len(links) - 1}\x00"
    s = re.sub(r"\[([^\]]+?)\]\(([^)\s]+?)\)", grab, s)
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    def put(m):
        t, u = links[int(m.group(1))]
        return f'<a href="{esc(u)}" color="{LINK}"><u>{re.sub(r"[*][*](.+?)[*][*]", r"<b>\1</b>", esc(t))}</u></a>'
    return re.sub(r"\x00(\d+)\x00", put, s)


def ptable(lines):
    rows = []
    for ln in lines:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            continue
        rows.append(cells)
    n = len(rows[0])
    lens = [min(max(max(len(r[i]) if i < len(r) else 0 for r in rows), 18 if i == 0 else 8), 140) for i in range(n)]
    widths = [l / sum(lens) for l in lens]
    data = [[Paragraph(inline(c), HEADC if ri == 0 else (CELLB if ci == 0 else CELL)) for ci, c in enumerate(r)] + [""] * (n - len(r))
            for ri, r in enumerate(rows)]
    t = Table(data, colWidths=[w * CW for w in widths], repeatRows=1)
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
          ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
          ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE), ("BACKGROUND", (0, 0), (-1, 0), PRIMARY)]
    st += [("BACKGROUND", (0, i), (-1, i), ZEBRA) for i in range(2, len(data), 2)]
    t.setStyle(TableStyle(st))
    return [t, Spacer(1, 7)]


def response_form():
    out = [H("School response form", 1, "response"),
           P("Fill this in on screen or on paper and return it to CodeSchool. It is an expression of interest, not a contract.", SMALL)]
    fields = [("School name", "r_school"), ("Board and city", "r_board"), ("Contact person and role", "r_contact"),
              ("Phone / email", "r_phone"), ("Classes and sections for the pilot", "r_classes"),
              ("Approximate number of students", "r_students"), ("Preferred start date", "r_start")]
    for lab, key in fields:
        out.append(labeled_field(lab, key, 0.32))
    t = Table([[Paragraph("<b>Programme of interest</b>", CELLB),
                FChoice("r_programme", ["-", "Offline programme", "Online programme", "Both / hybrid", "Not sure yet"], 0.4 * CW)]],
              colWidths=[0.32 * CW, 0.68 * CW])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 4)]))
    out += [t, Spacer(1, 4), labeled_field("Questions or changes you would like", "r_notes", 0.32, 54, True)]
    return out


story = [Spacer(1, 1), NextPageTemplate("body"), PageBreak()]
toc = TableOfContents(); toc.levelStyles = [TOC0, TOC1]; toc.dotsMinLevel = 0
story += [H("Contents", 0, "contents", "Contents"), Spacer(1, 4),
          callout([P(fm.get("draftnote", "Draft for discussion. Scope, timeline and prices will be finalised with the school."))], "warn", "Draft"),
          Spacer(1, 8), toc]

buf, tbl, n, first = [], [], 0, True
def flush():
    global buf
    if buf:
        story.append(Paragraph(inline(" ".join(x.strip() for x in buf)), BODY)); buf = []
def flush_tbl():
    global tbl
    if tbl:
        story.extend(ptable(tbl)); tbl = []

for ln in body:
    s = ln.rstrip()
    if s.startswith("|"):
        flush(); tbl.append(s); continue
    flush_tbl()
    if s.startswith("## "):
        flush(); n += 1
        h = s[3:].strip()
        story += [NextPageTemplate("body"), PageBreak() if first or fm.get("breaks") == "all" else CondPageBreak(90 * mm), Spacer(1, 10),
                  H(h, 0, f"s{n}", h)]
        first = False
    elif s.startswith("### "):
        flush(); story.append(H(s[4:].strip(), 1))
    elif s.startswith("  - "):
        flush(); story.append(Paragraph(inline(s[4:]), BUL2, bulletText="–"))
    elif s.startswith("- "):
        flush(); story.append(Paragraph(inline(s[2:]), BUL, bulletText="•"))
    elif re.match(r"^\d+\. ", s):
        flush(); num, txt = s.split(". ", 1)
        story.append(Paragraph(inline(txt), BUL, bulletText=f"{num}."))
    elif s.startswith(">"):
        flush()
        txt = s.lstrip("> ").strip()
        m = re.match(r"\[!(\w+)\]\s*(.*)", txt)
        kind, txt = (m.group(1), m.group(2)) if m else ("info", txt)
        story.append(callout([Paragraph(inline(txt), BODY)], kind if kind in ("info", "warn", "risk", "good", "accent") else "info"))
    elif s.strip() == "[[RESPONSE_FORM]]":
        flush(); story += response_form()
    elif s.strip() == "[[PAGEBREAK]]":
        flush(); story += [NextPageTemplate("body"), PageBreak()]
    elif not s.strip():
        flush()
    else:
        buf.append(s)
flush(); flush_tbl()

KitDoc(OUT).multiBuild(story)
print("built", OUT)
