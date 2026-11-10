"""Extra drawings for the Class 5 book. Re-exports figures.py and figures_c4.py, so content can use one module."""
import math
from figures_c4 import *  # noqa: F401,F403  (re-export shared and Class 4 figures)
from figures import _t, C, INK, SOFT, WHITE, YELLOW, ORANGE, RED, GREEN, BLUE, PURPLE, PINK, TEAL, PALE
from reportlab.graphics.shapes import Drawing, Rect, Circle, Line, Polygon, PolyLine, Wedge, Group


def turn_angle(deg, w=150, label=True):
    """A turn of `deg` degrees clockwise from facing up, with an arc."""
    d = Drawing(w, 110)
    cx, cy, r = w / 2, 46, 40
    d.add(Line(cx, cy, cx, cy + r, strokeColor=INK, strokeWidth=2))
    a = math.radians(90 - deg)
    d.add(Line(cx, cy, cx + r * math.cos(a), cy + r * math.sin(a), strokeColor=RED, strokeWidth=2.4))
    pts = []
    for k in range(31):
        t = math.radians(90 - deg * k / 30)
        pts += [cx + 18 * math.cos(t), cy + 18 * math.sin(t)]
    d.add(PolyLine(pts, strokeColor=ORANGE, strokeWidth=2))
    d.add(Circle(cx, cy, 3, fillColor=INK))
    if label:
        d.add(_t(cx, 2, f"{deg}° clockwise", 9, "KidB", SOFT))
    return d


def compass(size=70):
    d = Drawing(size, size)
    c = size / 2
    d.add(Circle(c, c, c - 4, fillColor=WHITE, strokeColor=INK, strokeWidth=1.2))
    d.add(Polygon([c, size - 10, c - 5, c, c + 5, c], fillColor=RED, strokeColor=None))
    d.add(Polygon([c, 10, c - 5, c, c + 5, c], fillColor=SOFT, strokeColor=None))
    for lab, x, y in (("N", c, size - 9), ("S", c, 2), ("E", size - 7, c - 3), ("W", 7, c - 3)):
        d.add(_t(x, y, lab, 9, "KidBl", INK))
    return d


def function_machine(inp, rule, out="?", w=360):
    d = Drawing(w, 70)
    d.add(Rect(4, 18, 60, 34, rx=8, ry=8, fillColor=YELLOW, strokeColor=INK, strokeWidth=1.2)); d.add(_t(34, 30, inp, 13, "KidBl"))
    d.add(Line(66, 35, 110, 35, strokeColor=INK, strokeWidth=1.6))
    d.add(Rect(112, 6, 136, 58, rx=12, ry=12, fillColor=PURPLE, strokeColor=INK, strokeWidth=1.4))
    d.add(_t(180, 38, "rule", 8.5, "Kid", WHITE)); d.add(_t(180, 22, rule, 12, "KidBl", WHITE))
    d.add(Line(250, 35, 292, 35, strokeColor=INK, strokeWidth=1.6))
    d.add(Rect(294, 18, 60, 34, rx=8, ry=8, fillColor=C("#DDF4E8"), strokeColor=INK, strokeWidth=1.2)); d.add(_t(324, 30, out, 13, "KidBl"))
    d.add(_t(34, 4, "input", 8, "Kid", SOFT)); d.add(_t(324, 4, "output", 8, "Kid", SOFT))
    return d


def variable_boxes(pairs):
    """pairs: [(name, value)] drawn as labelled boxes, like variables."""
    d = Drawing(len(pairs) * 120, 62)
    for i, (name, val) in enumerate(pairs):
        x = 6 + i * 120
        d.add(Rect(x, 4, 104, 34, rx=8, ry=8, fillColor=WHITE, strokeColor=ORANGE, strokeWidth=2))
        d.add(_t(x + 52, 15, val, 14, "KidBl"))
        d.add(Rect(x + 8, 34, 88, 20, rx=10, ry=10, fillColor=ORANGE, strokeColor=None))
        d.add(_t(x + 52, 40, name, 9, "KidB", WHITE))
    return d


def coins_row(n=8, labels=True, odd=None):
    d = Drawing(n * 40 + 10, 52)
    for i in range(n):
        x = 24 + i * 40
        d.add(Circle(x, 30, 15, fillColor=C("#F7C948") if i != odd else C("#E8A33D"), strokeColor=INK, strokeWidth=1.2))
        d.add(Circle(x, 30, 10, fillColor=None, strokeColor=C("#B9852A"), strokeWidth=0.8))
        if labels:
            d.add(_t(x, 4, i + 1, 9, "KidB", SOFT))
    return d


def search_range(low, high, guesses=(), w=440):
    """A number strip low..high; each guess shades the half that is ruled out."""
    d = Drawing(w, 50)
    n = high - low + 1
    cell = (w - 20) / n
    out = set()
    for g, direction in guesses:
        if direction == "higher":
            out |= set(range(low, g + 1))
        else:
            out |= set(range(g, high + 1))
    for i in range(n):
        v = low + i
        x = 10 + i * cell
        d.add(Rect(x, 16, cell - 1, 22, fillColor=C("#D9DEE7") if v in out else WHITE, strokeColor=C("#9AA5B8"), strokeWidth=0.6))
        if n <= 32 or v % 5 == 0 or v in (low, high):
            d.add(_t(x + cell / 2, 22, v, 7 if n > 20 else 8.5, "KidB" if v not in out else "Kid", INK if v not in out else SOFT))
    for g, _ in guesses:
        x = 10 + (g - low) * cell + cell / 2
        d.add(Polygon([x, 14, x - 5, 4, x + 5, 4], fillColor=RED, strokeColor=None))
    return d


def quilt(pattern, cell=26):
    """pattern: list of strings; 'R','B','Y','G','P' solid squares, 'r','b','y','g' half-triangles on white."""
    cols = {"R": RED, "B": BLUE, "Y": YELLOW, "G": GREEN, "P": PURPLE, "O": ORANGE, "W": WHITE}
    n_r, n_c = len(pattern), len(pattern[0])
    d = Drawing(n_c * cell + 4, n_r * cell + 4)
    for r, row in enumerate(pattern):
        for c, ch in enumerate(row):
            x = 2 + c * cell; y = 2 + (n_r - 1 - r) * cell
            if ch.isupper():
                d.add(Rect(x, y, cell, cell, fillColor=cols[ch], strokeColor=INK, strokeWidth=0.8))
            else:
                d.add(Rect(x, y, cell, cell, fillColor=WHITE, strokeColor=INK, strokeWidth=0.8))
                d.add(Polygon([x, y, x + cell, y, x, y + cell], fillColor=cols[ch.upper()], strokeColor=INK, strokeWidth=0.6))
    return d


def stopwatch(text="0:12", size=90):
    d = Drawing(size, size + 10)
    c = size / 2
    d.add(Rect(c - 7, size - 4, 14, 10, rx=3, ry=3, fillColor=SOFT, strokeColor=INK, strokeWidth=1))
    d.add(Circle(c, c, c - 4, fillColor=WHITE, strokeColor=INK, strokeWidth=2))
    d.add(Rect(c - 30, c - 12, 60, 24, rx=6, ry=6, fillColor=INK))
    d.add(_t(c, c - 5, text, 14, "KidBl", C("#7CF2B9")))
    return d


def rotation_design(n=4, size=110):
    """n petals turned evenly around a centre (rotational symmetry)."""
    d = Drawing(size, size)
    c = size / 2
    cols = [PINK, ORANGE, PURPLE, BLUE, GREEN, RED, TEAL, YELLOW]
    for k in range(n):
        a = 2 * math.pi * k / n
        pts = []
        for t in range(0, 181, 15):
            u = math.radians(t)
            rr = 40 * math.sin(u)
            ang = a + (u - math.pi / 2) * 0.35
            pts += [c + rr * math.cos(ang), c + rr * math.sin(ang)]
        d.add(Polygon(pts, fillColor=cols[k % len(cols)], strokeColor=INK, strokeWidth=1))
    d.add(Circle(c, c, 7, fillColor=YELLOW, strokeColor=INK, strokeWidth=1))
    return d


def pictograph_rows(rows, key, w=380):
    """rows: [(label, count_of_symbols, colour)]; half symbols allowed with .5. key: text such as '= 10 litres'."""
    d = Drawing(w, len(rows) * 26 + 26)
    for i, (lab, k, col) in enumerate(rows):
        y = len(rows) * 26 - i * 26
        d.add(_t(70, y + 2, lab, 9, "KidB", INK, "end"))
        full = int(k)
        for j in range(full):
            d.add(Circle(90 + j * 24, y + 6, 9, fillColor=col, strokeColor=INK, strokeWidth=0.8))
        if k - full >= 0.5:
            d.add(Wedge(90 + full * 24, y + 6, 9, 90, 270, fillColor=col, strokeColor=INK, strokeWidth=0.8))
    d.add(Circle(96, 8, 7, fillColor=PALE, strokeColor=INK, strokeWidth=0.8)); d.add(_t(108, 4, key, 8.5, "Kid", SOFT, "start"))
    return d


def treasure_map(rows=5, cols=6, start=(0, 0), items=None, walls=(), cell=30):
    """A grid map with a compass in the corner (rows from the bottom)."""
    g = grid(rows, cols, robot=start, items=items or {}, walls=walls, cell=cell)
    d = Drawing(g.width + 80, max(g.height, 80))
    for el in g.contents:
        d.add(el)
    comp = compass(64)
    for el in comp.contents:
        d.add(Group(el, transform=(1, 0, 0, 1, g.width + 12, d.height - 70)))
    return d
