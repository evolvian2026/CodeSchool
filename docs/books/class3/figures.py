"""Drawn illustrations for the Class 3 book (ReportLab graphics). Every function returns a Drawing."""
from reportlab.graphics.shapes import Drawing, Rect, Circle, Line, Polygon, String, Ellipse, PolyLine, Wedge, Group
from reportlab.lib import colors

C = colors.HexColor
INK = C("#1F2A44")
SOFT = C("#5B6577")
PALE = C("#EEF2F7")
RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK = (C(x) for x in
    ["#E5484D", "#F5A524", "#FFD23F", "#2BB673", "#14A3A3", "#3B82F6", "#8B5CF6", "#EC4899"])
WHITE = colors.white


def _t(x, y, s, size=11, font="KidB", color=INK, anchor="middle"):
    return String(x, y, str(s), fontName=font, fontSize=size, fillColor=color, textAnchor=anchor)


# ----------------------------------------------------------------- mascot
def robo(size=70, color=TEAL, wave=False, mood="smile"):
    d = Drawing(size, size * 1.15)
    s = size / 100.0
    g = Group()
    g.add(Line(50, 96, 50, 108, strokeColor=INK, strokeWidth=2.2))
    g.add(Circle(50, 110, 5, fillColor=ORANGE, strokeColor=INK, strokeWidth=1.5))
    g.add(Rect(18, 58, 64, 40, rx=12, ry=12, fillColor=color, strokeColor=INK, strokeWidth=2))
    g.add(Rect(26, 66, 48, 24, rx=8, ry=8, fillColor=WHITE, strokeColor=INK, strokeWidth=1.2))
    for ex in (40, 60):
        g.add(Circle(ex, 80, 4.6, fillColor=INK, strokeColor=None))
        g.add(Circle(ex + 1.5, 81.6, 1.4, fillColor=WHITE, strokeColor=None))
    if mood == "smile":
        g.add(PolyLine([42, 71, 46, 68.5, 50, 68, 54, 68.5, 58, 71], strokeColor=INK, strokeWidth=1.8))
    else:
        g.add(Circle(50, 70, 2.6, fillColor=INK, strokeColor=None))
    g.add(Circle(28, 72, 3, fillColor=PINK, strokeColor=None))
    g.add(Circle(72, 72, 3, fillColor=PINK, strokeColor=None))
    g.add(Rect(26, 16, 48, 40, rx=10, ry=10, fillColor=color, strokeColor=INK, strokeWidth=2))
    g.add(Circle(50, 36, 7, fillColor=YELLOW, strokeColor=INK, strokeWidth=1.4))
    g.add(Rect(30, 4, 12, 14, rx=4, ry=4, fillColor=SOFT, strokeColor=INK, strokeWidth=1.4))
    g.add(Rect(58, 4, 12, 14, rx=4, ry=4, fillColor=SOFT, strokeColor=INK, strokeWidth=1.4))
    if wave:
        g.add(PolyLine([74, 46, 86, 58, 90, 72], strokeColor=INK, strokeWidth=5))
        g.add(Circle(90, 74, 5, fillColor=color, strokeColor=INK, strokeWidth=1.4))
    else:
        g.add(PolyLine([74, 46, 84, 34], strokeColor=INK, strokeWidth=5))
    g.add(PolyLine([26, 46, 16, 34], strokeColor=INK, strokeWidth=5))
    g.scale(s, s)
    d.add(g)
    return d


# ----------------------------------------------------------------- generic pieces
def code_card(label, kind="step", w=96, h=30, color=BLUE):
    """A coloured code block like a Scratch-style card."""
    d = Drawing(w, h)
    d.add(Rect(1, 1, w - 2, h - 2, rx=8, ry=8, fillColor=color, strokeColor=INK, strokeWidth=1.2))
    d.add(Rect(14, h - 5, 16, 4, fillColor=color, strokeColor=None))
    x0 = 10
    if kind in ("up", "down", "left", "right"):
        d.add(arrow_shape(16, h / 2, kind, 9, WHITE))
        x0 = 28
    d.add(_t(x0 + (w - x0) / 2 - 2, h / 2 - 4, label, 10, "KidB", WHITE))
    return d


def arrow_shape(cx, cy, direction, r=8, fill=INK):
    pts = {"up": [0, 1, -0.8, -0.2, -0.3, -0.2, -0.3, -1, 0.3, -1, 0.3, -0.2, 0.8, -0.2],
           "down": [0, -1, -0.8, 0.2, -0.3, 0.2, -0.3, 1, 0.3, 1, 0.3, 0.2, 0.8, 0.2],
           "right": [1, 0, 0.2, 0.8, 0.2, 0.3, -1, 0.3, -1, -0.3, 0.2, -0.3, 0.2, -0.8],
           "left": [-1, 0, -0.2, 0.8, -0.2, 0.3, 1, 0.3, 1, -0.3, -0.2, -0.3, -0.2, -0.8]}[direction]
    return Polygon([cx + pts[i] * r if i % 2 == 0 else cy + pts[i] * r for i in range(len(pts))],
                   fillColor=fill, strokeColor=None)


def arrow_row(dirs, size=24, gap=6, color=BLUE):
    w = len(dirs) * (size + gap)
    d = Drawing(w, size + 2)
    for i, k in enumerate(dirs):
        x = i * (size + gap)
        d.add(Rect(x, 1, size, size, rx=6, ry=6, fillColor=color, strokeColor=INK, strokeWidth=1))
        d.add(arrow_shape(x + size / 2, 1 + size / 2, k, size * 0.32, WHITE))
    return d


def shape(kind, cx, cy, r, fill, stroke=INK):
    if kind == "circle":
        return Circle(cx, cy, r, fillColor=fill, strokeColor=stroke, strokeWidth=1.2)
    if kind == "square":
        return Rect(cx - r, cy - r, 2 * r, 2 * r, fillColor=fill, strokeColor=stroke, strokeWidth=1.2)
    if kind == "triangle":
        return Polygon([cx, cy + r, cx - r, cy - r * 0.85, cx + r, cy - r * 0.85], fillColor=fill, strokeColor=stroke, strokeWidth=1.2)
    if kind == "diamond":
        return Polygon([cx, cy + r, cx - r, cy, cx, cy - r, cx + r, cy], fillColor=fill, strokeColor=stroke, strokeWidth=1.2)
    if kind == "star":
        import math
        p = []
        for i in range(10):
            a = math.pi / 2 + i * math.pi / 5
            rr = r if i % 2 == 0 else r * 0.45
            p += [cx + rr * math.cos(a), cy + rr * math.sin(a)]
        return Polygon(p, fillColor=fill, strokeColor=stroke, strokeWidth=1.2)
    if kind == "blank":
        return Rect(cx - r, cy - r, 2 * r, 2 * r, rx=4, ry=4, fillColor=WHITE, strokeColor=SOFT, strokeWidth=1.2, strokeDashArray=[3, 2])
    raise ValueError(kind)


SHAPE_COL = {"circle": RED, "square": BLUE, "triangle": GREEN, "diamond": ORANGE, "star": YELLOW}


def shape_row(kinds, r=11, gap=8, labels=False):
    w = len(kinds) * (2 * r + gap)
    d = Drawing(w, 2 * r + (14 if labels else 4))
    for i, k in enumerate(kinds):
        cx = r + i * (2 * r + gap)
        cy = r + (12 if labels else 2)
        if k == "?":
            d.add(shape("blank", cx, cy, r, WHITE)); d.add(_t(cx, cy - 4, "?", 12, "KidB", SOFT))
        else:
            d.add(shape(k, cx, cy, r, SHAPE_COL.get(k, PALE)))
        if labels:
            d.add(_t(cx, 0, chr(65 + i), 8, "Kid", SOFT))
    return d


# ----------------------------------------------------------------- chapter figures
def alphabet_strip(shift=0, highlight="", w=470):
    letters = [chr(65 + i) for i in range(26)]
    cell = w / 26
    d = Drawing(w, 64 if shift else 24)
    top = 28 if shift else 2
    for i, ch in enumerate(letters):
        hi = ch in highlight
        d.add(Rect(i * cell, top, cell - 1, 20, rx=3, ry=3, fillColor=YELLOW if hi else PALE, strokeColor=SOFT, strokeWidth=0.5))
        d.add(_t(i * cell + cell / 2, top + 6, ch, 9, "KidB"))
    if shift:
        for i, ch in enumerate(letters):
            j = (i + shift) % 26
            d.add(Rect(i * cell, 2, cell - 1, 20, rx=3, ry=3, fillColor=C("#DDF4E8") if ch in highlight else WHITE, strokeColor=SOFT, strokeWidth=0.5))
            d.add(_t(i * cell + cell / 2, 8, letters[j], 9, "Kid", GREEN if ch in highlight else SOFT))
        d.add(_t(w - 2, 52, f"top row: plain letters   bottom row: coded (+{shift})", 7.5, "Kid", SOFT, "end"))
    return d


def cipher_wheel(size=110):
    import math
    d = Drawing(size, size)
    cx = cy = size / 2
    d.add(Circle(cx, cy, size / 2 - 2, fillColor=C("#FFF4D6"), strokeColor=INK, strokeWidth=1.4))
    d.add(Circle(cx, cy, size / 2 - 20, fillColor=C("#DDF4E8"), strokeColor=INK, strokeWidth=1.2))
    d.add(Circle(cx, cy, size / 2 - 40, fillColor=C("#FFFFFF"), strokeColor=INK, strokeWidth=0.8))
    for i in range(26):
        a = math.pi / 2 - i * 2 * math.pi / 26
        d.add(_t(cx + (size / 2 - 10) * math.cos(a), cy + (size / 2 - 10) * math.sin(a) - 3, chr(65 + i), 7.5, "KidB"))
        d.add(_t(cx + (size / 2 - 30) * math.cos(a), cy + (size / 2 - 30) * math.sin(a) - 3, chr(65 + (i + 3) % 26), 7, "KidB", GREEN))
    d.add(_t(cx, cy - 14, "key +3", 7, "KidB", SOFT))
    d.add(Circle(cx, cy, 4, fillColor=INK))
    return d


def views_example():
    """A drum (cylinder) and its top and side views."""
    d = Drawing(330, 90)
    d.add(Rect(20, 18, 60, 50, fillColor=ORANGE, strokeColor=INK, strokeWidth=1.2))
    d.add(Ellipse(50, 68, 30, 9, fillColor=YELLOW, strokeColor=INK, strokeWidth=1.2))
    d.add(Wedge(50, 18, 30, 180, 360, yradius=9, fillColor=ORANGE, strokeColor=INK, strokeWidth=1.2))
    d.add(_t(50, 0, "drum", 9, "Kid", SOFT))
    d.add(arrow_shape(110, 44, "right", 10, SOFT))
    d.add(Circle(170, 44, 26, fillColor=YELLOW, strokeColor=INK, strokeWidth=1.2))
    d.add(_t(170, 0, "top view", 9, "Kid", SOFT))
    d.add(Rect(240, 20, 60, 50, fillColor=ORANGE, strokeColor=INK, strokeWidth=1.2))
    d.add(_t(270, 0, "side view", 9, "Kid", SOFT))
    return d


def objects_and_views():
    d = Drawing(440, 92)
    # objects
    d.add(Circle(30, 60, 20, fillColor=RED, strokeColor=INK, strokeWidth=1.2)); d.add(_t(30, 28, "ball", 8, "Kid", SOFT))
    d.add(Rect(70, 42, 38, 38, fillColor=BLUE, strokeColor=INK, strokeWidth=1.2)); d.add(_t(89, 28, "dice", 8, "Kid", SOFT))
    d.add(Polygon([150, 82, 128, 42, 172, 42], fillColor=GREEN, strokeColor=INK, strokeWidth=1.2)); d.add(Ellipse(150, 42, 22, 6, fillColor=GREEN, strokeColor=INK, strokeWidth=1)); d.add(_t(150, 28, "party cap", 8, "Kid", SOFT))
    for i, lab in enumerate(["1", "2", "3"]):
        d.add(_t(30 + i * 60, 10, lab, 10, "KidB", TEAL))
    # top views
    x0 = 250
    d.add(Rect(x0, 40, 40, 40, fillColor=PALE, strokeColor=INK, strokeWidth=1.2)); d.add(_t(x0 + 20, 26, "A", 10, "KidB", PURPLE))
    d.add(Circle(x0 + 85, 60, 20, fillColor=PALE, strokeColor=INK, strokeWidth=1.2)); d.add(_t(x0 + 85, 26, "B", 10, "KidB", PURPLE))
    d.add(Circle(x0 + 150, 60, 20, fillColor=PALE, strokeColor=INK, strokeWidth=1.2)); d.add(Circle(x0 + 150, 60, 3, fillColor=INK)); d.add(_t(x0 + 150, 26, "C", 10, "KidB", PURPLE))
    d.add(_t(x0 + 85, 2, "top views", 8, "Kid", SOFT))
    return d


def block_stack(cols, size=22, palette=(BLUE, ORANGE, GREEN, PURPLE)):
    """Front view of block towers: cols = list of heights."""
    w = len(cols) * size + 4
    d = Drawing(w, max(cols) * size + 4)
    for i, h in enumerate(cols):
        for j in range(h):
            d.add(Rect(2 + i * size, 2 + j * size, size, size, fillColor=palette[(i + j) % len(palette)], strokeColor=INK, strokeWidth=1))
    return d


def build_options():
    """Three tower pictures for 'which matches the instructions'."""
    d = Drawing(330, 70)
    def blk(x, y, c):
        d.add(Rect(x, y, 22, 22, fillColor=c, strokeColor=INK, strokeWidth=1))
    # a) two red side by side, blue on left
    blk(10, 4, RED); blk(32, 4, RED); blk(10, 26, BLUE); d.add(_t(32, 54, "a", 10, "KidB", PURPLE))
    # b) two red side by side, blue on right
    blk(120, 4, RED); blk(142, 4, RED); blk(142, 26, BLUE); d.add(_t(142, 54, "b", 10, "KidB", PURPLE))
    # c) red, blue stacked, red side
    blk(230, 4, BLUE); blk(252, 4, RED); blk(230, 26, RED); d.add(_t(252, 54, "c", 10, "KidB", PURPLE))
    return d


def number_line(start, end, step, hops=0, w=440, mark_every=None):
    d = Drawing(w, 56)
    y = 16
    d.add(Line(10, y, w - 10, y, strokeColor=INK, strokeWidth=1.4))
    n = (end - start) // (mark_every or step)
    unit = (w - 20) / max(n, 1)
    for i in range(n + 1):
        x = 10 + i * unit
        d.add(Line(x, y - 4, x, y + 4, strokeColor=INK, strokeWidth=1))
        d.add(_t(x, 2, start + i * (mark_every or step), 8, "Kid", SOFT))
    hop_units = step // (mark_every or step)
    for h in range(hops):
        x1 = 10 + h * hop_units * unit; x2 = x1 + hop_units * unit
        pts = []
        for k in range(21):  # smooth jump arc
            u = k / 20
            pts += [x1 + (x2 - x1) * u, y + 4 + 26 * 4 * u * (1 - u)]
        d.add(PolyLine(pts, strokeColor=ORANGE, strokeWidth=2.2))
        d.add(arrow_shape(x2 - 1, y + 7, "down", 4, ORANGE))
    return d


def dots_growth(counts=(1, 3, 5), r=4):
    d = Drawing(300, 58)
    x = 10
    for k, n in enumerate(counts):
        for i in range(n):
            d.add(Circle(x + (i % 5) * 11, 40 - (i // 5) * 11, r, fillColor=[RED, BLUE, GREEN, PURPLE][k % 4], strokeColor=None))
        d.add(_t(x + 20, 2, f"step {k + 1}", 8, "Kid", SOFT))
        x += 80
    d.add(shape("blank", x + 22, 34, 18, WHITE)); d.add(_t(x + 22, 30, "?", 12, "KidB", SOFT)); d.add(_t(x + 22, 2, f"step {len(counts) + 1}", 8, "Kid", SOFT))
    return d


def halves_options():
    d = Drawing(420, 70)
    # a circle in two equal halves
    d.add(Circle(40, 38, 26, fillColor=YELLOW, strokeColor=INK, strokeWidth=1.2)); d.add(Line(40, 12, 40, 64, strokeColor=INK, strokeWidth=1.4))
    d.add(_t(40, 0, "a", 10, "KidB", PURPLE))
    # b rectangle split unequally
    d.add(Rect(100, 14, 80, 46, fillColor=C("#FBD5E5"), strokeColor=INK, strokeWidth=1.2)); d.add(Line(125, 14, 125, 60, strokeColor=INK, strokeWidth=1.4))
    d.add(_t(140, 0, "b", 10, "KidB", PURPLE))
    # c square split by diagonal
    d.add(Rect(215, 12, 50, 50, fillColor=C("#D6E8FF"), strokeColor=INK, strokeWidth=1.2)); d.add(Line(215, 12, 265, 62, strokeColor=INK, strokeWidth=1.4))
    d.add(_t(240, 0, "c", 10, "KidB", PURPLE))
    # d triangle split off-centre
    d.add(Polygon([340, 64, 300, 12, 380, 12], fillColor=C("#DDF4E8"), strokeColor=INK, strokeWidth=1.2)); d.add(Line(340, 64, 318, 12, strokeColor=INK, strokeWidth=1.4))
    d.add(_t(340, 0, "d", 10, "KidB", PURPLE))
    return d


def base10(h, t, o):
    d = Drawing(330, 70)
    x = 4
    for _ in range(h):
        d.add(Rect(x, 8, 52, 52, fillColor=C("#FFE7A8"), strokeColor=INK, strokeWidth=1))
        for k in range(1, 10):
            d.add(Line(x + k * 5.2, 8, x + k * 5.2, 60, strokeColor=ORANGE, strokeWidth=0.4))
            d.add(Line(x, 8 + k * 5.2, x + 52, 8 + k * 5.2, strokeColor=ORANGE, strokeWidth=0.4))
        x += 60
    for _ in range(t):
        d.add(Rect(x, 8, 6, 52, fillColor=C("#BFE3FF"), strokeColor=INK, strokeWidth=1))
        x += 10
    x += 8
    for i in range(o):
        d.add(Rect(x + (i % 3) * 8, 8 + (i // 3) * 8, 6, 6, fillColor=C("#C9F2D8"), strokeColor=INK, strokeWidth=0.8))
    return d


def buttons_machine(start=135):
    d = Drawing(330, 74)
    d.add(Rect(4, 8, 150, 60, rx=10, ry=10, fillColor=PALE, strokeColor=INK, strokeWidth=1.3))
    d.add(Rect(18, 30, 122, 28, rx=6, ry=6, fillColor=INK))
    d.add(_t(79, 38, start, 16, "KidBl", C("#7CF2B9")))
    d.add(_t(79, 14, "counter", 8, "Kid", SOFT))
    d.add(Circle(200, 38, 18, fillColor=GREEN, strokeColor=INK, strokeWidth=1.2)); d.add(_t(200, 34, "+10", 10, "KidB", WHITE)); d.add(_t(200, 6, "green", 8, "Kid", SOFT))
    d.add(Circle(270, 38, 18, fillColor=RED, strokeColor=INK, strokeWidth=1.2)); d.add(_t(270, 34, "+100", 9, "KidB", WHITE)); d.add(_t(270, 6, "red", 8, "Kid", SOFT))
    return d


def rakhi_set(cols=(RED, BLUE, RED, YELLOW, BLUE, RED, GREEN, YELLOW, RED, BLUE)):
    d = Drawing(330, 40)
    for i, c in enumerate(cols):
        x = 14 + i * 31
        d.add(Line(x - 13, 20, x + 13, 20, strokeColor=ORANGE, strokeWidth=2))
        d.add(Circle(x, 20, 9, fillColor=c, strokeColor=INK, strokeWidth=1))
        d.add(Circle(x, 20, 3.4, fillColor=WHITE, strokeColor=None))
    return d


def packets(groups=5, each=4):
    d = Drawing(340, 52)
    for g in range(groups):
        x = 6 + g * 64
        d.add(Rect(x, 4, 56, 44, rx=8, ry=8, fillColor=C("#FFF4D6"), strokeColor=INK, strokeWidth=1))
        for k in range(each):
            d.add(Circle(x + 14 + (k % 2) * 26, 16 + (k // 2) * 20, 7, fillColor=[RED, BLUE, GREEN, PURPLE][k % 4], strokeColor=INK, strokeWidth=0.8))
    return d


def balance(left="", right="", tilt=-1):
    """tilt -1: left side down (left heavier); 1: right down; 0 level."""
    d = Drawing(200, 86)
    d.add(Polygon([100, 52, 88, 8, 112, 8], fillColor=SOFT, strokeColor=INK, strokeWidth=1))
    dy = 10 * tilt
    d.add(Line(40, 52 + dy, 160, 52 - dy, strokeColor=INK, strokeWidth=2.4))
    for x, y, lab in ((40, 52 + dy, left), (160, 52 - dy, right)):
        d.add(Line(x, y, x - 16, y - 18, strokeColor=INK, strokeWidth=1)); d.add(Line(x, y, x + 16, y - 18, strokeColor=INK, strokeWidth=1))
        d.add(Rect(x - 22, y - 22, 44, 5, rx=2, ry=2, fillColor=ORANGE, strokeColor=INK, strokeWidth=1))
        d.add(_t(x, y - 14, lab, 9, "KidB"))
    return d


def tile_strip(pattern, w=440, start_label="START", end_label="END", hops=None):
    """pattern: string of 'w'/'g' tiles."""
    n = len(pattern)
    cell = (w - 80) / n
    d = Drawing(w, 50)
    d.add(_t(20, 18, start_label, 8, "KidB", GREEN))
    for i, ch in enumerate(pattern):
        x = 40 + i * cell
        d.add(Rect(x, 8, cell - 2, 26, rx=4, ry=4, fillColor=C("#9AA5B8") if ch == "g" else WHITE, strokeColor=INK, strokeWidth=1))
        d.add(_t(x + cell / 2 - 1, 0, i + 1, 7, "Kid", SOFT))
    d.add(_t(w - 18, 18, end_label, 8, "KidB", RED))
    return d


def ribbons(lengths, names, unit=2.6):
    d = Drawing(440, len(lengths) * 20 + 4)
    cols = [RED, BLUE, GREEN, PURPLE, ORANGE]
    for i, (L, n) in enumerate(zip(lengths, names)):
        y = 4 + (len(lengths) - 1 - i) * 20
        d.add(_t(30, y + 4, n, 9, "KidB", INK, "end"))
        d.add(Rect(38, y, L * unit, 13, rx=6, ry=6, fillColor=cols[i % 5], strokeColor=INK, strokeWidth=0.8))
    return d


def bars_sort(values, highlight=()):
    d = Drawing(300, max(values) * 8 + 24)
    for i, v in enumerate(values):
        x = 10 + i * 46
        d.add(Rect(x, 16, 34, v * 8, rx=4, ry=4, fillColor=ORANGE if i in highlight else BLUE, strokeColor=INK, strokeWidth=1))
        d.add(_t(x + 17, 2, v, 10, "KidB"))
    return d


def clock(h, m, size=62):
    import math
    d = Drawing(size, size)
    c = size / 2
    d.add(Circle(c, c, c - 2, fillColor=WHITE, strokeColor=INK, strokeWidth=1.6))
    for k in range(12):
        a = math.pi / 2 - k * math.pi / 6
        d.add(Line(c + (c - 6) * math.cos(a), c + (c - 6) * math.sin(a), c + (c - 3) * math.cos(a), c + (c - 3) * math.sin(a), strokeColor=INK, strokeWidth=1))
    ah = math.pi / 2 - ((h % 12) + m / 60) * math.pi / 6
    am = math.pi / 2 - m * math.pi / 30
    d.add(Line(c, c, c + (c * 0.48) * math.cos(ah), c + (c * 0.48) * math.sin(ah), strokeColor=INK, strokeWidth=2.6))
    d.add(Line(c, c, c + (c * 0.75) * math.cos(am), c + (c * 0.75) * math.sin(am), strokeColor=RED, strokeWidth=1.6))
    d.add(Circle(c, c, 2.4, fillColor=INK))
    return d


def clocks_row(times):
    d = Drawing(len(times) * 90, 80)
    for i, (h, m, lab) in enumerate(times):
        g = clock(h, m)
        for el in g.contents:
            el2 = el
            d.add(Group(el2, transform=(1, 0, 0, 1, 10 + i * 90, 14)))
        d.add(_t(41 + i * 90, 2, lab, 9, "KidB", PURPLE))
    return d


def calendar_strip(days=("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"), highlight=None):
    d = Drawing(440, 34)
    for i, dd in enumerate(days):
        d.add(Rect(4 + i * 62, 4, 56, 26, rx=6, ry=6, fillColor=YELLOW if dd == highlight else PALE, strokeColor=INK, strokeWidth=0.8))
        d.add(_t(32 + i * 62, 12, dd, 10, "KidB"))
    return d


def grid(rows, cols, robot=None, items=None, walls=(), cell=28, path=None, labels=True):
    """robot=(r,c); items={(r,c): ('label', colour)}; walls=[(r,c)]; rows counted from bottom (0)."""
    items = items or {}
    w = cols * cell + (18 if labels else 4)
    h = rows * cell + (18 if labels else 4)
    d = Drawing(w, h)
    ox = 16 if labels else 2
    oy = 16 if labels else 2
    for r in range(rows):
        for c in range(cols):
            fill = C("#F7F9FC") if (r + c) % 2 == 0 else WHITE
            if (r, c) in walls:
                fill = C("#5B6577")
            d.add(Rect(ox + c * cell, oy + r * cell, cell, cell, fillColor=fill, strokeColor=C("#C9D2E0"), strokeWidth=0.8))
    if labels:
        for c in range(cols):
            d.add(_t(ox + c * cell + cell / 2, 2, chr(65 + c), 8, "Kid", SOFT))
        for r in range(rows):
            d.add(_t(7, oy + r * cell + cell / 2 - 3, r + 1, 8, "Kid", SOFT))
    if path:
        pts = []
        for (r, c) in path:
            pts += [ox + c * cell + cell / 2, oy + r * cell + cell / 2]
        d.add(PolyLine(pts, strokeColor=ORANGE, strokeWidth=3, strokeDashArray=[4, 3]))
    for (r, c), (lab, col) in items.items():
        x = ox + c * cell; y = oy + r * cell
        d.add(Rect(x + 3, y + 3, cell - 6, cell - 6, rx=5, ry=5, fillColor=col, strokeColor=INK, strokeWidth=1))
        d.add(_t(x + cell / 2, y + cell / 2 - 3.5, lab, 8.5, "KidB", WHITE))
    if robot:
        r, c = robot
        x = ox + c * cell; y = oy + r * cell
        d.add(Rect(x + 6, y + 6, cell - 12, cell - 14, rx=4, ry=4, fillColor=TEAL, strokeColor=INK, strokeWidth=1))
        d.add(Circle(x + cell / 2 - 4, y + cell / 2 - 1, 1.6, fillColor=WHITE)); d.add(Circle(x + cell / 2 + 4, y + cell / 2 - 1, 1.6, fillColor=WHITE))
        d.add(Line(x + cell / 2, y + cell - 8, x + cell / 2, y + cell - 3, strokeColor=INK, strokeWidth=1))
    return d


def pictograph():
    d = Drawing(360, 92)
    rows = [("Laddoo", 4, ORANGE), ("Barfi", 2, PINK), ("Jalebi", 5, YELLOW)]
    for i, (n, k, c) in enumerate(rows):
        y = 64 - i * 26
        d.add(_t(52, y + 2, n, 9, "KidB", INK, "end"))
        for j in range(k):
            d.add(Circle(70 + j * 24, y + 6, 9, fillColor=c, strokeColor=INK, strokeWidth=0.8))
    d.add(Circle(240, 10, 6, fillColor=PALE, strokeColor=INK, strokeWidth=0.8)); d.add(_t(250, 6, "= 2 sweets", 8, "Kid", SOFT, "start"))
    return d


def trace_table(rows, cols=("Step", "What happens", "Marbles")):
    """Returns a list for a Table: header + rows."""
    return [list(cols)] + [list(r) for r in rows]


def timeline(events):
    d = Drawing(440, 54)
    d.add(Line(10, 24, 430, 24, strokeColor=INK, strokeWidth=1.6))
    n = len(events)
    for i, (t, lab) in enumerate(events):
        x = 20 + i * (400 / max(n - 1, 1))
        d.add(Circle(x, 24, 6, fillColor=[RED, ORANGE, GREEN, BLUE, PURPLE][i % 5], strokeColor=INK, strokeWidth=1))
        d.add(_t(x, 34, t, 8, "KidB", SOFT))
        d.add(_t(x, 6, lab, 8, "Kid", INK))
    return d


def mini_map():
    """Nani Maa trip: house -> bus stop -> station -> Nani's house."""
    d = Drawing(440, 70)
    places = [("Home", BLUE), ("Bus stop", ORANGE), ("Station", PURPLE), ("Nani's house", PINK)]
    for i, (p, c) in enumerate(places):
        x = 20 + i * 135
        d.add(Rect(x, 26, 70, 30, rx=8, ry=8, fillColor=c, strokeColor=INK, strokeWidth=1))
        d.add(_t(x + 35, 37, p, 9, "KidB", WHITE))
        if i < len(places) - 1:
            d.add(Line(x + 72, 41, x + 133, 41, strokeColor=INK, strokeWidth=1.4, strokeDashArray=[4, 3]))
            d.add(arrow_shape(x + 128, 41, "right", 5, INK))
    d.add(_t(220, 6, "Step 1           Step 2           Step 3", 8, "Kid", SOFT))
    return d
