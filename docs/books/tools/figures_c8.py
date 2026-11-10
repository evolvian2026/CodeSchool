"""Extra drawings for the Class 8 book. Re-exports the Class 3-7 figures, so content can use one module."""
from figures_c7 import *  # noqa: F401,F403  (re-export shared and Class 4-7 figures)
from figures import _t, C, INK, SOFT, WHITE, YELLOW, ORANGE, RED, GREEN, BLUE, PURPLE, PINK, TEAL, PALE
from reportlab.graphics.shapes import Drawing, Rect, Line
from reportlab.pdfbase import pdfmetrics


def _digits(n, base):
    ds = []
    while n:
        ds.append(n % base); n //= base
    return ds[::-1] or [0]


def pipes_compare(n, bases=(10, 2, 3), w=440, bar_h=20):
    """One bar per base: the length n built from pipes whose lengths are powers of the base (as in CBSE's pipes activity)."""
    cols = [BLUE, ORANGE, GREEN, PURPLE, PINK, TEAL]
    d = Drawing(w, len(bases) * (bar_h + 22) + 4)
    x0 = 92
    scale = (w - x0 - 8) / n
    for r, b in enumerate(bases):
        y = d.height - (r + 1) * (bar_h + 22) + 14
        ds = _digits(n, b)
        k = len(ds) - 1
        d.add(_t(x0 - 8, y + 6, f"base {b}: {''.join(map(str, ds))}", 9.5, "KidBl", INK, "end"))
        x = x0
        for i, dig in enumerate(ds):
            p = b ** (k - i)
            for _ in range(dig):
                seg = p * scale
                d.add(Rect(x, y, seg, bar_h, fillColor=cols[(k - i) % len(cols)], strokeColor=WHITE, strokeWidth=1))
                if pdfmetrics.stringWidth(str(p), "KidB", 8) + 3 < seg:
                    d.add(_t(x + seg / 2, y + 6, p, 8, "KidB", WHITE))
                x += seg
    return d


def area_model(a, b, w=300, h=150):
    """Area model for (a1 + a2) x (b1 + b2): a = (a1, a2) across, b = (b1, b2) down, with each part's product. Not to scale."""
    d = Drawing(w, h + 30)
    x0, y0 = 30, 6
    W, H = w - x0 - 10, h - 10
    xs = [x0, x0 + W * 0.6, x0 + W]
    ys = [y0 + H, y0 + H - H * 0.6, y0]
    cols = [[C("#DCEBFF"), C("#FFF1D6")], [C("#E8E1FF"), C("#DDF4E8")]]
    for i in range(2):
        for j in range(2):
            d.add(Rect(xs[i], ys[j + 1], xs[i + 1] - xs[i], ys[j] - ys[j + 1], fillColor=cols[j][i], strokeColor=INK, strokeWidth=1.2))
            d.add(_t((xs[i] + xs[i + 1]) / 2, (ys[j] + ys[j + 1]) / 2 - 5, f"{a[i]} x {b[j]} = {a[i] * b[j]}", 10, "KidBl"))
    for i in range(2):
        d.add(_t((xs[i] + xs[i + 1]) / 2, y0 + H + 10, a[i], 11, "KidBl", BLUE))
        d.add(_t(x0 - 8, (ys[i] + ys[i + 1]) / 2 - 4, b[i], 11, "KidBl", PURPLE, "end"))
    return d
