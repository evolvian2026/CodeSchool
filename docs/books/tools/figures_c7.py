"""Extra drawings for the Class 7 book. Re-exports the Class 3-6 figures, so content can use one module."""
import math
from figures_c6 import *  # noqa: F401,F403  (re-export shared, Class 4, 5 and 6 figures)
from figures import _t, C, INK, SOFT, WHITE, YELLOW, ORANGE, RED, GREEN, BLUE, PURPLE, PINK, TEAL, PALE
from figures_c6 import head
from reportlab.graphics.shapes import Drawing, Rect, Circle, Line, Polygon, PolyLine, Wedge, Group
from reportlab.pdfbase import pdfmetrics

GRID = C("#B8C2D3")


def expr_tree(tree, w=300, level_h=46):
    """An expression tree. tree is a number/str, or (op, left, right). Operators in purple circles, numbers in boxes."""
    def depth(t):
        return 1 + max(depth(t[1]), depth(t[2])) if isinstance(t, tuple) else 1
    def leaves(t):
        return leaves(t[1]) + leaves(t[2]) if isinstance(t, tuple) else 1
    dp = depth(tree)
    d = Drawing(w, dp * level_h + 6)
    slot = (w - 20) / leaves(tree)

    def place(t, x0, lvl):
        """Returns centre x; draws subtree spanning leaves from x0."""
        y = d.height - 22 - lvl * level_h
        if not isinstance(t, tuple):
            x = x0 + slot / 2
            d.add(Rect(x - 17, y - 12, 34, 24, rx=5, ry=5, fillColor=C("#FFF1D6"), strokeColor=INK, strokeWidth=1.1))
            d.add(_t(x, y - 4.5, t, 12, "KidBl"))
            return x, 1
        lx, ln = place(t[1], x0, lvl + 1)
        rx, rn = place(t[2], x0 + ln * slot, lvl + 1)
        x = (lx + rx) / 2
        cy = y - level_h
        d.add(Line(x, y - 13, lx, cy + 12, strokeColor=SOFT, strokeWidth=1.3))
        d.add(Line(x, y - 13, rx, cy + 12, strokeColor=SOFT, strokeWidth=1.3))
        d.add(Circle(x, y, 14, fillColor=PURPLE, strokeColor=None))
        d.add(_t(x, y - 5, t[0], 14, "KidBl", WHITE))
        return x, ln + rn
    place(tree, 10, 0)
    return d


def binary_cards(n=None, bits=5, w=60, h=74):
    """Binary dot cards 16, 8, 4, 2, 1. If n is given, cards for its 1-bits are face up and the bit is written below."""
    d = Drawing(bits * (w + 8), h + 22)
    vals = [2 ** k for k in range(bits - 1, -1, -1)]
    for i, v in enumerate(vals):
        x = i * (w + 8) + 2
        on = n is None or (n & v)
        d.add(Rect(x, 20, w, h, rx=6, ry=6, fillColor=WHITE if on else C("#3A4560"), strokeColor=INK, strokeWidth=1.2))
        if on:
            cols = 4 if v >= 8 else (2 if v >= 2 else 1)
            rows = max(1, v // cols)
            for k in range(v):
                cx = x + w / 2 + ((k % cols) - (cols - 1) / 2) * 11
                cy = 20 + h / 2 + 6 + ((k // cols) - (rows - 1) / 2) * -9
                d.add(Circle(cx, cy, 3.4, fillColor=ORANGE, strokeColor=None))
            d.add(_t(x + w / 2, 25, v, 10, "KidBl", SOFT))
        if n is not None:
            d.add(_t(x + w / 2, 4, 1 if on else 0, 13, "KidBl", PURPLE))
    return d


def matchsticks(n=3, s=26):
    """n squares in a row made of matchsticks (3n + 1 sticks)."""
    d = Drawing(n * s + 16, s + 16)
    def stick(x1, y1, x2, y2):
        d.add(Line(x1, y1, x2, y2, strokeColor=C("#C98A3D"), strokeWidth=3.2))
        d.add(Circle(x2, y2, 2.6, fillColor=RED, strokeColor=None))
    for i in range(n):
        x = 8 + i * s
        stick(x + 2, 8, x + s - 2, 8)
        stick(x + 2, 8 + s, x + s - 2, 8 + s)
        if i == 0:
            stick(x, 10, x, 6 + s)
        stick(x + s, 10, x + s, 6 + s)
    return d


def matchstick_row(counts=(1, 2, 3), s=22):
    parts = [matchsticks(k, s) for k in counts]
    w = sum(p.width for p in parts) + 30 * len(parts)
    d = Drawing(w, parts[0].height + 16)
    x = 0
    for k, p in zip(counts, parts):
        for el in p.contents:
            d.add(Group(el, transform=(1, 0, 0, 1, x, 16)))
        d.add(_t(x + p.width / 2, 2, f"{k} square{'s' if k > 1 else ''}: {3 * k + 1} sticks", 8.5, "KidB", SOFT))
        x += p.width + 30
    return d


def pyramid(rows, cell=40):
    """Number pyramid; rows from the top, e.g. [['23'], ['', ''], ['3', 'P', '4']]. Each block = sum of the two below."""
    n = len(rows)
    d = Drawing(n * cell + 10, n * 30 + 6)
    for r, row in enumerate(rows):
        y = d.height - 30 - r * 30
        x0 = 5 + (n - len(row)) * cell / 2
        for i, v in enumerate(row):
            letter = str(v).isalpha()
            d.add(Rect(x0 + i * cell, y, cell, 28, fillColor=C("#FFF1D6") if letter else WHITE, strokeColor=INK, strokeWidth=1.1))
            d.add(_t(x0 + i * cell + cell / 2, y + 9, v, 12, "KidBl", PURPLE if letter else INK))
    return d


def cross_angles(a=65, size=150, labels=None):
    """Two straight lines crossing; the four angles labelled (a, 180-a, a, 180-a) unless labels are given."""
    d = Drawing(size, size * 0.72)
    cx, cy, r = size / 2, size * 0.36, size * 0.46
    t = math.radians(a)
    d.add(Line(cx - r, cy, cx + r, cy, strokeColor=INK, strokeWidth=1.8))
    d.add(Line(cx - r * 0.75 * math.cos(t), cy - r * 0.75 * math.sin(t), cx + r * 0.75 * math.cos(t), cy + r * 0.75 * math.sin(t), strokeColor=INK, strokeWidth=1.8))
    labs = labels or [f"{a}°", f"{180 - a}°", f"{a}°", f"{180 - a}°"]
    mids = [a / 2, a + (180 - a) / 2, 180 + a / 2, 180 + a + (180 - a) / 2]
    cols = [RED, BLUE, RED, BLUE]
    for lab, m, col in zip(labs, mids, cols):
        mm = math.radians(m)
        d.add(_t(cx + 26 * math.cos(mm), cy + 26 * math.sin(mm) - 4, lab, 9.5, "KidBl", col))
    return d


def punch_cards(patterns, keep=None, names="RGB", w=58):
    """Punched cards: each pattern is a string of 'U' (light ON: notch) and 'O' (light OFF: hole). Cards not in keep are greyed out."""
    keep = set(patterns if keep is None else keep)
    per_row = min(len(patterns), 8)
    rows = (len(patterns) + per_row - 1) // per_row
    d = Drawing(per_row * (w + 6), rows * 66 + 4)
    for i, p in enumerate(patterns):
        x = (i % per_row) * (w + 6) + 2
        y = d.height - 64 - (i // per_row) * 66
        live = p in keep
        d.add(Rect(x, y, w, 60, rx=5, ry=5, fillColor=C("#FFF7E0") if live else C("#EEF0F4"), strokeColor=INK if live else GRID, strokeWidth=1.3 if live else 0.8))
        gap = w / (len(p) + 1)
        for k, ch in enumerate(p):
            hx = x + gap * (k + 1)
            if ch == "U":
                d.add(Rect(hx - 4, y + 48, 8, 12, fillColor=WHITE, strokeColor=INK if live else GRID, strokeWidth=0.8))
            else:
                d.add(Circle(hx, y + 52, 3.6, fillColor=WHITE, strokeColor=INK if live else GRID, strokeWidth=0.8))
            d.add(_t(hx, y + 34, names[k], 7.5, "KidB", SOFT))
            d.add(_t(hx, y + 20, "on" if ch == "U" else "off", 6.5, "Kid", (GREEN if ch == "U" else RED) if live else GRID))
        if not live:
            d.add(Line(x + 4, y + 4, x + w - 4, y + 56, strokeColor=C("#C7CEDA"), strokeWidth=1.2))
        d.add(_t(x + w / 2, y + 5, p, 8, "KidBl", INK if live else GRID))
    return d


def pie_chart(values, labels, size=150, colours=None):
    """A pie chart with a legend on the right showing each label, value and angle."""
    cols = colours or [BLUE, ORANGE, GREEN, PURPLE, PINK, TEAL, RED, YELLOW]
    total = float(sum(values))
    d = Drawing(size + 190, size)
    cx, cy, r = size / 2, size / 2, size / 2 - 4
    start = 90
    for i, v in enumerate(values):
        ang = 360 * v / total
        d.add(Wedge(cx, cy, r, start - ang, start, fillColor=cols[i % len(cols)], strokeColor=WHITE, strokeWidth=1.5))
        start -= ang
    step = min(20, (size - 8) / len(values))
    for i, (v, lab) in enumerate(zip(values, labels)):
        y = size - 14 - i * step
        d.add(Rect(size + 14, y, 12, 12, fillColor=cols[i % len(cols)], strokeColor=None))
        d.add(_t(size + 32, y + 2, f"{lab}: {v}  ({round(360 * v / total)}°)", 9.5, "KidB", INK, "start"))
    return d


def scatter(points, xlabel, ylabel, w=300, h=170, xmax=None, ymax=None, colour=None):
    """A scatter plot. points: [(x, y)] or [(x, y, colour)]."""
    xmax = xmax or max(p[0] for p in points) * 1.1
    ymax = ymax or max(p[1] for p in points) * 1.1
    d = Drawing(w, h)
    x0, y0 = 34, 26
    d.add(Line(x0, y0, w - 8, y0, strokeColor=INK, strokeWidth=1.2))
    d.add(Line(x0, y0, x0, h - 6, strokeColor=INK, strokeWidth=1.2))
    for k in range(1, 5):
        xx = x0 + (w - 8 - x0) * k / 4
        d.add(_t(xx, y0 - 11, round(xmax * k / 4), 7.5, "Kid", SOFT))
        yy = y0 + (h - 6 - y0) * k / 4
        d.add(_t(x0 - 5, yy - 3, round(ymax * k / 4), 7.5, "Kid", SOFT, "end"))
    for p in points:
        col = p[2] if len(p) > 2 else (colour or BLUE)
        d.add(Circle(x0 + (w - 8 - x0) * p[0] / xmax, y0 + (h - 6 - y0) * p[1] / ymax, 4.5, fillColor=col, strokeColor=INK, strokeWidth=0.6))
    d.add(_t((x0 + w) / 2, 2, xlabel, 8.5, "KidB", SOFT))
    g = Group(_t(0, 0, ylabel, 8.5, "KidB", SOFT))
    g.transform = (0, 1, -1, 0, 10, (y0 + h) / 2)
    d.add(g)
    return d


def item_cards(items, w=84, h=46, per_row=5):
    """Picture-card style labels: items = [(name, tag, colour)], e.g. ('banana peel', 'wet', GREEN)."""
    rows = (len(items) + per_row - 1) // per_row
    d = Drawing(min(len(items), per_row) * (w + 6), rows * (h + 6))
    for i, (name, tag, col) in enumerate(items):
        x = (i % per_row) * (w + 6)
        y = d.height - h - (i // per_row) * (h + 6)
        d.add(Rect(x, y, w, h, rx=6, ry=6, fillColor=WHITE, strokeColor=INK, strokeWidth=1))
        size = 9
        while pdfmetrics.stringWidth(name, "KidB", size) > w - 8 and size > 6.5:
            size -= 0.5
        d.add(_t(x + w / 2, y + h - 18, name, size, "KidB"))
        if tag:
            tw = pdfmetrics.stringWidth(tag, "KidB", 8) + 12
            d.add(Rect(x + w / 2 - tw / 2, y + 5, tw, 14, rx=7, ry=7, fillColor=col, strokeColor=None))
            d.add(_t(x + w / 2, y + 9, tag, 8, "KidB", WHITE))
    return d

