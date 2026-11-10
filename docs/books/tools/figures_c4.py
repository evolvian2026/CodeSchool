"""Extra drawings for the Class 4 book. Re-exports everything in figures.py, so content can use one module."""
from figures import *  # noqa: F401,F403  (re-export shared figures)
from figures import _t, C, INK, SOFT, WHITE, YELLOW, ORANGE, RED, GREEN, BLUE, PURPLE, PINK, TEAL
from reportlab.graphics.shapes import Drawing, Rect, Circle, Line


def cube_net(labels="ABCDEF", cell=30):
    """Cross net: vertical strip A (top), C, E, F; B left of C, D right of C."""
    pos = {labels[0]: (1, 3), labels[1]: (0, 2), labels[2]: (1, 2), labels[3]: (2, 2), labels[4]: (1, 1), labels[5]: (1, 0)}
    cols = [BLUE, ORANGE, GREEN, PURPLE, PINK, TEAL]
    d = Drawing(3 * cell + 4, 4 * cell + 4)
    for i, (lab, (x, y)) in enumerate(pos.items()):
        d.add(Rect(2 + x * cell, 2 + y * cell, cell, cell, fillColor=cols[i], strokeColor=INK, strokeWidth=1.2))
        d.add(_t(2 + x * cell + cell / 2, 2 + y * cell + cell / 2 - 4, lab, 12, "KidBl", WHITE))
    return d


def nets_options(cell=16):
    """a) cross net (folds into a cube), b) 2 x 3 block (does not fold), c) staircase net (folds)."""
    nets = [[(1, 3), (0, 2), (1, 2), (2, 2), (1, 1), (1, 0)],
            [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)],
            [(0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0)]]
    d = Drawing(400, 4 * cell + 20)
    xs = [10, 120, 230]
    for k, net in enumerate(nets):
        for (x, y) in net:
            d.add(Rect(xs[k] + x * cell, 16 + y * cell, cell, cell, fillColor=C("#D6E8FF"), strokeColor=INK, strokeWidth=1))
        d.add(_t(xs[k] + 2 * cell, 0, "abc"[k], 10, "KidB", PURPLE))
    return d


def stacks_options(options, size=16):
    """Front views of block arrangements, e.g. [[1,2,1],[2,1,1],[1,1,2]] labelled a, b, c."""
    d = Drawing(400, max(max(o) for o in options) * size + 22)
    x = 10
    for k, cols in enumerate(options):
        for i, h in enumerate(cols):
            for j in range(h):
                d.add(Rect(x + i * size, 18 + j * size, size, size, fillColor=[BLUE, ORANGE, GREEN][(i + j) % 3], strokeColor=INK, strokeWidth=1))
        d.add(_t(x + len(cols) * size / 2, 2, "abc"[k], 10, "KidB", PURPLE))
        x += len(cols) * size + 70
    return d


def coin_grid(rows, cell=24, labels=True, check=False):
    """rows: strings of 'B' (black side up), 'W' (white side up) or '?' (empty). check=True tints the last row and column."""
    n_r, n_c = len(rows), len(rows[0])
    off = 16 if labels else 2
    d = Drawing(n_c * cell + off + 4, n_r * cell + off + 4)
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            x = off + c * cell
            y = off + (n_r - 1 - r) * cell
            is_check = check and (r == n_r - 1 or c == n_c - 1)
            d.add(Rect(x, y, cell, cell, fillColor=C("#FFF4D6") if is_check else C("#F7F9FC"), strokeColor=C("#C9D2E0"), strokeWidth=0.8))
            if ch == "?":
                d.add(Circle(x + cell / 2, y + cell / 2, cell * 0.36, fillColor=WHITE, strokeColor=SOFT, strokeWidth=1, strokeDashArray=[2, 2]))
            else:
                d.add(Circle(x + cell / 2, y + cell / 2, cell * 0.36, fillColor=INK if ch == "B" else WHITE, strokeColor=INK, strokeWidth=1))
    if labels:
        for c in range(n_c):
            d.add(_t(off + c * cell + cell / 2, 3, c + 1, 8, "Kid", SOFT))
        for r in range(n_r):
            d.add(_t(7, off + (n_r - 1 - r) * cell + cell / 2 - 3, r + 1, 8, "Kid", SOFT))
    return d


def sorting_network(inputs=None, comps=((0, 1), (1, 2), (0, 1)), w=330, outputs=None):
    """Horizontal wires with comparators. At each comparator the smaller number goes to the upper wire."""
    wires = len(inputs) if inputs else 3
    gap = 28
    h = wires * gap + 10
    d = Drawing(w, h)
    top = h - 14
    ys = [top - i * gap for i in range(wires)]
    for i, y in enumerate(ys):
        d.add(Line(40, y, w - 40, y, strokeColor=INK, strokeWidth=1.6))
        if inputs:
            d.add(Circle(24, y, 11, fillColor=YELLOW, strokeColor=INK, strokeWidth=1))
            d.add(_t(24, y - 4, inputs[i], 10, "KidB"))
        if outputs:
            d.add(Circle(w - 24, y, 11, fillColor=C("#DDF4E8"), strokeColor=INK, strokeWidth=1))
            d.add(_t(w - 24, y - 4, outputs[i], 10, "KidB"))
        else:
            d.add(Circle(w - 24, y, 11, fillColor=WHITE, strokeColor=SOFT, strokeWidth=1, strokeDashArray=[2, 2]))
    step = (w - 120) / max(len(comps), 1)
    for k, (a, b) in enumerate(comps):
        x = 70 + k * step + step / 2
        d.add(Line(x, ys[a], x, ys[b], strokeColor=ORANGE, strokeWidth=3))
        d.add(Circle(x, ys[a], 4, fillColor=ORANGE, strokeColor=None))
        d.add(Circle(x, ys[b], 4, fillColor=ORANGE, strokeColor=None))
    return d


def comparator(a, b):
    d = Drawing(260, 64)
    d.add(_t(20, 44, a, 14, "KidBl")); d.add(_t(20, 12, b, 14, "KidBl"))
    d.add(Line(34, 48, 226, 48, strokeColor=INK, strokeWidth=1.4)); d.add(Line(34, 16, 226, 16, strokeColor=INK, strokeWidth=1.4))
    d.add(Rect(100, 6, 60, 52, rx=8, ry=8, fillColor=ORANGE, strokeColor=INK, strokeWidth=1.2))
    d.add(_t(130, 34, "compare", 8.5, "KidB", WHITE)); d.add(_t(130, 22, "smaller up", 7.5, "Kid", WHITE))
    d.add(_t(244, 44, "?", 14, "KidBl", SOFT)); d.add(_t(244, 12, "?", 14, "KidBl", SOFT))
    return d


def shaded_parts(n=8, shaded=3, w=280, h=40):
    d = Drawing(w + 4, h + 4)
    cell = w / n
    for i in range(n):
        d.add(Rect(2 + i * cell, 2, cell, h, fillColor=ORANGE if i < shaded else WHITE, strokeColor=INK, strokeWidth=1.2))
    return d


def array_dots(rows, cols, r=6, gap=20, groups=None):
    """rows x cols dots; groups=k colours every k columns alike (to show equal groups)."""
    d = Drawing(cols * gap + 10, rows * gap + 6)
    palette = [RED, BLUE, GREEN, PURPLE, ORANGE, PINK]
    for i in range(rows):
        for j in range(cols):
            col = palette[(j // groups) % 6] if groups else palette[i % 6]
            d.add(Circle(10 + j * gap, rows * gap - 8 - i * gap, r, fillColor=col, strokeColor=INK, strokeWidth=0.6))
    return d


def decision_tree(q1, yes1, q2, yes2, no2, w=420):
    """Two-level yes/no tree: q1 -> yes: yes1; no: q2 -> yes: yes2, no: no2."""
    d = Drawing(w, 150)

    def node(x, y, text, fill):
        tw = max(90, len(text) * 6.2 + 16)
        d.add(Rect(x - tw / 2, y - 14, tw, 28, rx=10, ry=10, fillColor=fill, strokeColor=INK, strokeWidth=1.1))
        d.add(_t(x, y - 4, text, 9, "KidB", WHITE))

    def edge(x1, y1, x2, y2, lab):
        d.add(Line(x1, y1, x2, y2, strokeColor=INK, strokeWidth=1.2))
        d.add(_t((x1 + x2) / 2 + (10 if x2 > x1 else -10), (y1 + y2) / 2 + 2, lab, 8.5, "KidB", GREEN if lab == "yes" else RED))

    edge(w / 2, 118, w * 0.2, 94, "yes"); edge(w / 2, 118, w * 0.62, 94, "no")
    edge(w * 0.62, 66, w * 0.45, 36, "yes"); edge(w * 0.62, 66, w * 0.82, 36, "no")
    node(w / 2, 132, q1, BLUE)
    node(w * 0.2, 80, yes1, ORANGE)
    node(w * 0.62, 80, q2, BLUE)
    node(w * 0.45, 22, yes2, PURPLE)
    node(w * 0.82, 22, no2, GREEN)
    return d


def mirror_grid(filled, rows=4, cols=6, cell=22, show_mirror=False):
    """filled: set of (row, col) shaded on the left; a dashed mirror line in the middle. show_mirror=True also shades the reflection."""
    d = Drawing(cols * cell + 20, rows * cell + 34)
    for r in range(rows):
        for c in range(cols):
            on = (r, c) in filled or (show_mirror and (r, cols - 1 - c) in filled)
            d.add(Rect(10 + c * cell, 22 + (rows - 1 - r) * cell, cell, cell, fillColor=ORANGE if on else WHITE, strokeColor=C("#B8C2D3"), strokeWidth=0.8))
    for c in range(cols):
        d.add(_t(10 + c * cell + cell / 2, 8, chr(65 + c), 8, "Kid", SOFT))
    mx = 10 + cols / 2 * cell
    d.add(Line(mx, 18, mx, rows * cell + 30, strokeColor=RED, strokeWidth=2, strokeDashArray=[5, 3]))
    return d


def bar_chart(values, labels, w=400, unit=14):
    cols = [RED, ORANGE, YELLOW, PURPLE, GREEN, BLUE]
    top = max(values)
    h = top * unit + 40
    d = Drawing(w, h)
    x0, y0 = 30, 22
    for v in range(0, top + 1, 2):
        d.add(Line(x0, y0 + v * unit, w - 10, y0 + v * unit, strokeColor=C("#E3E8F0"), strokeWidth=0.6))
        d.add(_t(x0 - 8, y0 + v * unit - 3, v, 7.5, "Kid", SOFT, "end"))
    d.add(Line(x0, y0, w - 10, y0, strokeColor=INK, strokeWidth=1.2))
    d.add(Line(x0, y0, x0, h - 4, strokeColor=INK, strokeWidth=1.2))
    bw = (w - 60) / len(values)
    for i, (v, lab) in enumerate(zip(values, labels)):
        x = x0 + 12 + i * bw
        d.add(Rect(x, y0, bw * 0.6, v * unit, fillColor=cols[i % len(cols)], strokeColor=INK, strokeWidth=1))
        d.add(_t(x + bw * 0.3, 6, lab, 9, "KidB"))
    return d


def lamps_machine(a_on=False, b_on=False):
    d = Drawing(360, 76)
    for i, (lab, on) in enumerate((("A", a_on), ("B", b_on))):
        x = 40 + i * 80
        d.add(Circle(x, 46, 18, fillColor=YELLOW if on else C("#D9DEE7"), strokeColor=INK, strokeWidth=1.2))
        d.add(Rect(x - 7, 20, 14, 8, fillColor=SOFT, strokeColor=INK, strokeWidth=0.8))
        d.add(_t(x, 4, f"lamp {lab}", 8.5, "KidB", SOFT))
    d.add(Rect(196, 22, 70, 40, rx=8, ry=8, fillColor=BLUE, strokeColor=INK, strokeWidth=1.2))
    d.add(_t(231, 44, "Button 1", 9, "KidB", WHITE)); d.add(_t(231, 30, "flips A", 8, "Kid", WHITE))
    d.add(Rect(278, 22, 74, 40, rx=8, ry=8, fillColor=PURPLE, strokeColor=INK, strokeWidth=1.2))
    d.add(_t(315, 44, "Button 2", 9, "KidB", WHITE)); d.add(_t(315, 30, "flips both", 8, "Kid", WHITE))
    return d


def jugs(capacities=(5, 3), fills=(5, 0)):
    d = Drawing(260, 110)
    x = 20
    for cap, f in zip(capacities, fills):
        h = cap * 16
        d.add(Rect(x, 20, 60, h, rx=6, ry=6, fillColor=WHITE, strokeColor=INK, strokeWidth=1.4))
        if f:
            d.add(Rect(x + 2, 22, 56, f * 16 - 4, rx=4, ry=4, fillColor=C("#9AD0FF"), strokeColor=None))
        for k in range(1, cap):
            d.add(Line(x, 20 + k * 16, x + 8, 20 + k * 16, strokeColor=INK, strokeWidth=0.8))
        d.add(_t(x + 30, 6, f"{cap} L jug", 9, "KidB"))
        x += 100
    return d
