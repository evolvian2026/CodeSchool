"""Extra drawings for the Class 6 book. Re-exports figures.py, figures_c4.py and figures_c5.py, so content can use one module."""
import math
from figures_c5 import *  # noqa: F401,F403  (re-export shared, Class 4 and Class 5 figures)
from figures import _t, C, INK, SOFT, WHITE, YELLOW, ORANGE, RED, GREEN, BLUE, PURPLE, PINK, TEAL, PALE, arrow_shape
from reportlab.graphics.shapes import Drawing, Rect, Circle, Line, Polygon, PolyLine, Ellipse, Group

GRID = C("#B8C2D3")


def compass8(size=120):
    """An 8-point compass rose: N, NE, E, SE, S, SW, W, NW (45 degrees apart)."""
    d = Drawing(size, size)
    c = size / 2
    r = c - 18
    d.add(Circle(c, c, r, fillColor=WHITE, strokeColor=INK, strokeWidth=1.2))
    names = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    for k, nm in enumerate(names):
        a = math.radians(90 - 45 * k)
        x, y = c + r * math.cos(a), c + r * math.sin(a)
        d.add(Line(c, c, x, y, strokeColor=RED if nm == "N" else (INK if len(nm) == 1 else SOFT), strokeWidth=2 if len(nm) == 1 else 1))
        lx, ly = c + (r + 10) * math.cos(a), c + (r + 10) * math.sin(a) - 3.5
        d.add(_t(lx, ly, nm, 9 if len(nm) == 1 else 8, "KidBl" if len(nm) == 1 else "KidB", INK if len(nm) == 1 else SOFT))
    d.add(Circle(c, c, 3, fillColor=INK))
    return d


def odd_squares(n=4, gap=9):
    """Squares of dots built from L-shaped layers: 1, 1+3, 1+3+5, ... (sum of odd numbers is a square)."""
    cols = [ORANGE, BLUE, GREEN, PURPLE, PINK]
    w = sum(k * gap + 30 for k in range(1, n + 1)) + 10
    d = Drawing(w, n * gap + 30)
    x0 = 10
    for k in range(1, n + 1):
        for i in range(k):
            for j in range(k):
                layer = max(i, j)
                d.add(Circle(x0 + i * gap + 4, 20 + j * gap + 4, 3.3, fillColor=cols[layer % len(cols)], strokeColor=None))
        d.add(_t(x0 + (k * gap) / 2, 4, "+".join(str(2 * m + 1) for m in range(k)), 8, "KidB", SOFT))
        x0 += k * gap + 30
    return d


def _is_prime(v):
    return v > 1 and all(v % k for k in range(2, int(v ** 0.5) + 1))


def number_grid(n=30, cols=10, cell=26, show=True):
    """Numbers 1..n in a grid. show=True: primes in green, the rest crossed out (the sieve)."""
    rows = (n + cols - 1) // cols
    d = Drawing(cols * cell + 4, rows * cell + 4)
    for v in range(1, n + 1):
        r, c = (v - 1) // cols, (v - 1) % cols
        x, y = 2 + c * cell, 2 + (rows - 1 - r) * cell
        p = _is_prime(v)
        d.add(Rect(x, y, cell, cell, fillColor=C("#DDF4E8") if (show and p) else WHITE, strokeColor=GRID, strokeWidth=0.8))
        d.add(_t(x + cell / 2, y + cell / 2 - 4, v, 10, "KidBl" if (show and p) else "Kid", GREEN if (show and p) else (SOFT if show else INK)))
        if show and not p:
            d.add(Line(x + 5, y + 5, x + cell - 5, y + cell - 5, strokeColor=C("#C7CEDA"), strokeWidth=1))
    return d


def circle_points(n=12, step=None, start=None, size=130):
    """n equally spaced points numbered like a clock (n at the top). Joins start, start+step, ... until it returns."""
    d = Drawing(size, size)
    c = size / 2
    r = c - 16
    pos = {}
    for k in range(1, n + 1):
        a = math.radians(90 - 360 * k / n)
        pos[k] = (c + r * math.cos(a), c + r * math.sin(a))
    if step:
        s = start or step
        pts, v = [], s
        while True:
            pts += list(pos[v])
            v = (v + step - 1) % n + 1
            if v == s:
                pts += list(pos[v])
                break
        d.add(PolyLine(pts, strokeColor=ORANGE, strokeWidth=2))
    for k, (x, y) in pos.items():
        d.add(Circle(x, y, 3.2, fillColor=INK))
        a = math.radians(90 - 360 * k / n)
        d.add(_t(c + (r + 10) * math.cos(a), c + (r + 10) * math.sin(a) - 3.5, k, 8, "KidB", SOFT))
    return d


def lshape(a, b, c, dd, unit=13, units="m", split=True):
    """An L-shape: a bottom rectangle a x b with a c x dd rectangle on its top-left. Side lengths labelled."""
    w, h = a * unit, (b + dd) * unit
    d = Drawing(w + 60, h + 34)
    ox, oy = 30, 18
    pts = [0, 0, a, 0, a, b, c, b, c, b + dd, 0, b + dd]
    d.add(Polygon([ox + v * unit if i % 2 == 0 else oy + v * unit for i, v in enumerate(pts)],
                  fillColor=C("#FFF1D6"), strokeColor=INK, strokeWidth=1.6))
    if split:
        d.add(Line(ox, oy + b * unit, ox + c * unit, oy + b * unit, strokeColor=RED, strokeWidth=1.2, strokeDashArray=[4, 3]))
        d.add(_t(ox + a * unit / 2, oy + b * unit / 2 - 4, "A", 12, "KidBl", RED))
        d.add(_t(ox + c * unit / 2, oy + (b + dd / 2) * unit - 4, "B", 12, "KidBl", RED))
    d.add(_t(ox + a * unit / 2, oy - 13, f"{a} {units}", 9, "KidB"))
    d.add(_t(ox + a * unit + 4, oy + b * unit / 2 - 3, f"{b} {units}", 9, "KidB", INK, "start"))
    d.add(_t(ox + c * unit / 2, oy + (b + dd) * unit + 5, f"{c} {units}", 9, "KidB"))
    d.add(_t(ox - 4, oy + (b + dd) * unit / 2 - 3, f"{b + dd} {units}", 9, "KidB", INK, "end"))
    d.add(_t(ox + c * unit + 4, oy + (b + dd / 2) * unit - 3, f"{dd} {units}", 9, "KidB", SOFT, "start"))
    return d


def construction(w=300):
    """Perpendicular bisector: segment AB, equal circles from A and B meeting at P and Q, and the line PQ."""
    d = Drawing(w, 170)
    ax, bx, y = w / 2 - 60, w / 2 + 60, 85
    r = 80
    d.add(Circle(ax, y, r, fillColor=None, strokeColor=C("#9FC3F7"), strokeWidth=1, strokeDashArray=[3, 3]))
    d.add(Circle(bx, y, r, fillColor=None, strokeColor=C("#F7C59F"), strokeWidth=1, strokeDashArray=[3, 3]))
    hy = math.sqrt(r * r - 60 * 60)
    mx = w / 2
    d.add(Line(mx, y - hy - 8, mx, y + hy + 8, strokeColor=RED, strokeWidth=1.8))
    d.add(Line(ax, y, bx, y, strokeColor=INK, strokeWidth=2.2))
    for x, lab, dy in ((ax, "A", -15), (bx, "B", -15)):
        d.add(Circle(x, y, 3, fillColor=INK)); d.add(_t(x, y + dy, lab, 11, "KidBl"))
    for yy, lab in ((y + hy, "P"), (y - hy, "Q")):
        d.add(Circle(mx, yy, 3, fillColor=RED)); d.add(_t(mx + 12, yy - 3, lab, 11, "KidBl", RED))
    d.add(Rect(mx, y, 8, 8, fillColor=None, strokeColor=INK, strokeWidth=0.8))
    d.add(_t(mx + 12, y - 13, "M", 10, "KidB", SOFT, "start"))
    return d


def bar_neg(values, labels, w=400, unit=6, step=2, title=None):
    """Bar chart that allows negative values: bars above or below a zero line (for temperatures)."""
    lo, hi = min(0, min(values)), max(0, max(values))
    lo = step * math.floor(lo / step); hi = step * math.ceil(hi / step)
    h = (hi - lo) * unit + 34
    d = Drawing(w, h)
    x0, y0 = 34, 22
    yz = y0 + (0 - lo) * unit
    for v in range(lo, hi + 1, step):
        yy = y0 + (v - lo) * unit
        d.add(Line(x0, yy, w - 10, yy, strokeColor=C("#E3E8F0"), strokeWidth=0.6))
        d.add(_t(x0 - 6, yy - 3, v, 7.5, "Kid", SOFT, "end"))
    d.add(Line(x0, y0, x0, h - 6, strokeColor=INK, strokeWidth=1.2))
    d.add(Line(x0, yz, w - 10, yz, strokeColor=INK, strokeWidth=1.4))
    bw = (w - x0 - 16) / len(values)
    for i, (v, lab) in enumerate(zip(values, labels)):
        x = x0 + 8 + i * bw
        if v:
            d.add(Rect(x, min(yz, yz + v * unit), bw * 0.62, abs(v) * unit, fillColor=ORANGE if v > 0 else BLUE, strokeColor=INK, strokeWidth=0.8))
        d.add(_t(x + bw * 0.31, 6, lab, 8.5, "KidB"))
    return d


def creature(pattern, colour, label="", size=52):
    """A friendly made-up creature with stripes or spots, for the 'train a classifier' activity."""
    d = Drawing(size + 8, size + 22)
    cx, cy = (size + 8) / 2, size / 2 + 18
    body = Ellipse(cx, cy, size * 0.42, size * 0.36, fillColor=colour, strokeColor=INK, strokeWidth=1.2)
    d.add(body)
    if "stripes" in pattern:
        for k in (-1, 0, 1):
            x = cx + k * size * 0.17
            d.add(Line(x, cy - size * 0.28, x, cy + size * 0.10, strokeColor=INK, strokeWidth=2.2))
    if "spots" in pattern:
        for dx, dy in ((-0.2, -0.12), (0.18, -0.16), (0.02, 0.02), (-0.06, -0.24), (0.24, 0.02)):
            d.add(Circle(cx + dx * size, cy + dy * size, size * 0.05, fillColor=INK, strokeColor=None))
    for dx in (-0.12, 0.12):
        d.add(Circle(cx + dx * size, cy + size * 0.2, size * 0.075, fillColor=WHITE, strokeColor=INK, strokeWidth=0.8))
        d.add(Circle(cx + dx * size, cy + size * 0.2, size * 0.035, fillColor=INK))
    for dx in (-0.2, 0.2):
        d.add(Line(cx + dx * size, cy - size * 0.33, cx + dx * size, cy - size * 0.43, strokeColor=INK, strokeWidth=1.6))
    if label:
        d.add(_t(cx, 3, label, 10, "KidBl", INK if label != "?" else RED))
    return d


def creature_row(items, size=52):
    """items: [(pattern, colour, label)]; label '?' marks a creature still to be classified."""
    cs = [creature(p, col, lab, size) for p, col, lab in items]
    w = sum(c.width for c in cs) + 6 * len(cs)
    d = Drawing(w, cs[0].height)
    x = 0
    for c in cs:
        for el in c.contents:
            d.add(Group(el, transform=(1, 0, 0, 1, x, 0)))
        x += c.width + 6
    return d


def _box(d, x, y, w, h, text, fill, shape="rect", size=9):
    if shape == "oval":
        d.add(Rect(x - w / 2, y - h / 2, w, h, rx=h / 2, ry=h / 2, fillColor=fill, strokeColor=INK, strokeWidth=1.2))
    elif shape == "diamond":
        d.add(Polygon([x, y + h / 2, x + w / 2, y, x, y - h / 2, x - w / 2, y], fillColor=fill, strokeColor=INK, strokeWidth=1.2))
    else:
        d.add(Rect(x - w / 2, y - h / 2, w, h, rx=4, ry=4, fillColor=fill, strokeColor=INK, strokeWidth=1.2))
    d.add(_t(x, y - size * 0.35, text, size, "KidB"))


def head(x, y, direction, r=4.5, fill=INK):
    """A triangle arrow head with its tip at (x, y)."""
    dx, dy = {"down": (0, 1), "up": (0, -1), "right": (-1, 0), "left": (1, 0)}[direction]
    px, py = -dy, dx
    return Polygon([x, y, x + dx * r * 1.6 + px * r, y + dy * r * 1.6 + py * r, x + dx * r * 1.6 - px * r, y + dy * r * 1.6 - py * r],
                   fillColor=fill, strokeColor=None)


def _arrow(d, x1, y1, x2, y2, label=None, lx=0, ly=0):
    d.add(Line(x1, y1, x2, y2, strokeColor=INK, strokeWidth=1.3))
    direction = "down" if y2 < y1 else ("up" if y2 > y1 else ("right" if x2 > x1 else "left"))
    d.add(head(x2, y2, direction))
    if label:
        d.add(_t((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, label, 8.5, "KidBl", RED))


def flowchart(w=380, scale=1.0):
    """Water-cooler routine: start, join line, decision 'cooler free?' (no: wait, loop back), fill bottle, decision 'full?', end."""
    d = Drawing(w, 300)
    x = 130
    _box(d, x, 284, 80, 22, "Start", C("#DDF4E8"), "oval")
    _arrow(d, x, 273, x, 255)
    _box(d, x, 243, 150, 24, "Join the line at the arrow", C("#E3EEFF"))
    _arrow(d, x, 231, x, 213)
    _box(d, x, 193, 130, 40, "Cooler free?", C("#FFF1D6"), "diamond")
    # no -> wait, back to decision
    d.add(Line(x + 65, 193, 268, 193, strokeColor=INK, strokeWidth=1.3)); d.add(_t(x + 80, 197, "no", 8.5, "KidBl", RED))
    _box(d, 300, 193, 110, 24, "Wait behind line", C("#E3EEFF"))
    d.add(PolyLine([300, 205, 300, 222, x + 20, 222, x + 20, 212], strokeColor=INK, strokeWidth=1.3))
    d.add(head(x + 20, 212, "down"))
    _arrow(d, x, 173, x, 151, "yes", 14, 0)
    _box(d, x, 139, 130, 24, "Fill your bottle", C("#E3EEFF"))
    _arrow(d, x, 127, x, 109)
    _box(d, x, 89, 130, 40, "Bottle full?", C("#FFF1D6"), "diamond")
    d.add(PolyLine([x - 65, 89, 22, 89, 22, 139, x - 65, 139], strokeColor=INK, strokeWidth=1.3))
    d.add(head(x - 65, 139, "right")); d.add(_t(x - 80, 93, "no", 8.5, "KidBl", RED))
    _arrow(d, x, 69, x, 53, "yes", 14, 0)
    _box(d, x, 41, 150, 24, "Leave by the exit side", C("#E3EEFF"))
    _arrow(d, x, 29, x, 20)
    _box(d, x, 10, 80, 20, "End", C("#DDF4E8"), "oval")
    if scale != 1.0:
        g = Group(*d.contents); g.scale(scale, scale)
        d = Drawing(w * scale, 300 * scale); d.add(g)
    return d


def flow_shapes():
    """The three flowchart shapes, labelled."""
    d = Drawing(240, 56)
    _box(d, 38, 32, 74, 24, "Start / End", C("#DDF4E8"), "oval", 8.5)
    _box(d, 116, 32, 62, 24, "Step", C("#E3EEFF"), "rect", 8.5)
    _box(d, 196, 32, 86, 40, "Decision?", C("#FFF1D6"), "diamond", 8.5)
    for x, t in ((38, "oval"), (116, "box"), (196, "diamond")):
        d.add(_t(x, 2, t, 8, "Kid", SOFT))
    return d


def list_boxes(name, values, cell=40):
    """A list drawn as numbered boxes: positions 1, 2, 3, ... above the values."""
    w = 90 + len(values) * cell
    d = Drawing(w, 52)
    d.add(_t(80, 14, f"{name} =", 11, "KidBl", PURPLE, "end"))
    for i, v in enumerate(values):
        x = 88 + i * cell
        d.add(Rect(x, 4, cell - 4, 28, rx=5, ry=5, fillColor=WHITE, strokeColor=PURPLE, strokeWidth=1.4))
        d.add(_t(x + (cell - 4) / 2, 13, v, 11, "KidBl"))
        d.add(_t(x + (cell - 4) / 2, 38, i + 1, 8, "Kid", SOFT))
    return d


def password_meter(score, w=260):
    """A 4-segment strength bar: score 1 (weak) to 4 (strong)."""
    d = Drawing(w, 30)
    cols = [RED, ORANGE, YELLOW, GREEN]
    sw = (w - 70) / 4
    for k in range(4):
        d.add(Rect(4 + k * (sw + 2), 10, sw, 12, rx=3, ry=3, fillColor=cols[k] if k < score else C("#E3E8F0"), strokeColor=None))
    d.add(_t(4 + 4 * (sw + 2) + 6, 12, ["", "weak", "fair", "good", "strong"][score], 9, "KidB", INK, "start"))
    return d


def creature_sets(train, test, size=44):
    """Two labelled rows: training examples (with labels) and new creatures to classify (labelled '?')."""
    a, b = creature_row(train, size), creature_row(test, size)
    d = Drawing(max(a.width, b.width) + 10, a.height + b.height + 34)
    d.add(_t(2, d.height - 11, "Training examples (labelled)", 9, "KidB", SOFT, "start"))
    for el in a.contents:
        d.add(Group(el, transform=(1, 0, 0, 1, 0, b.height + 18)))
    d.add(_t(2, b.height + 4, "New creatures to classify", 9, "KidB", SOFT, "start"))
    for el in b.contents:
        d.add(Group(el, transform=(1, 0, 0, 1, 0, 0)))
    return d
