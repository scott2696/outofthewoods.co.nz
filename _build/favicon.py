#!/usr/bin/env python3
"""Generates the site icon set. Run from build.py.

The mark: a deep-ink rounded square carrying a kowhai-gold card diamond with a
notched upper-right "edge" cut in aqua. It reads as *casino* at 48px, which is
the smallest size Google will render in a SERP favicon slot, and it stays
legible as a maskable Android icon because the diamond sits inside the 80%
safe circle.
"""
import os
from PIL import Image, ImageDraw

SIZES = (48, 96, 144, 192, 512)
INK = (12, 17, 32)
INK_2 = (20, 28, 50)
GOLD = (255, 178, 32)
GOLD_HI = (255, 209, 102)
AQUA = (61, 220, 196)


def _master(px=1024):
    img = Image.new("RGBA", (px, px), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # vertical ink gradient ground, clipped to a rounded square
    grad = Image.new("RGBA", (px, px))
    gd = ImageDraw.Draw(grad)
    for y in range(px):
        t = y / float(px - 1)
        gd.line([(0, y), (px, y)],
                fill=(int(INK_2[0] + (INK[0] - INK_2[0]) * t),
                      int(INK_2[1] + (INK[1] - INK_2[1]) * t),
                      int(INK_2[2] + (INK[2] - INK_2[2]) * t), 255))
    mask = Image.new("L", (px, px), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, px - 1, px - 1],
                                           radius=int(px * 0.225), fill=255)
    img.paste(grad, (0, 0), mask)

    # aqua edge notch, top-right
    d = ImageDraw.Draw(img)
    notch = Image.new("RGBA", (px, px), (0, 0, 0, 0))
    ImageDraw.Draw(notch).polygon(
        [(px * 0.58, 0), (px, 0), (px, px * 0.42)], fill=AQUA + (255,))
    img.paste(notch, (0, 0), Image.composite(
        notch.split()[3], Image.new("L", (px, px), 0), mask))

    # gold diamond
    cx, cy, r = px * 0.5, px * 0.53, px * 0.315
    d.polygon([(cx, cy - r * 1.14), (cx + r * 0.86, cy),
               (cx, cy + r * 1.14), (cx - r * 0.86, cy)], fill=GOLD + (255,))
    # top-left facet highlight
    d.polygon([(cx, cy - r * 1.14), (cx, cy),
               (cx - r * 0.86, cy)], fill=GOLD_HI + (255,))
    return img


def build(root):
    m = _master()
    for s in SIZES:
        m.resize((s, s), Image.LANCZOS).save(
            os.path.join(root, "favicon-%dx%d.png" % (s, s)), "PNG", optimize=True)
    # apple touch icon on an opaque ground
    at = Image.new("RGB", (180, 180), INK)
    at.paste(m.resize((180, 180), Image.LANCZOS), (0, 0),
             m.resize((180, 180), Image.LANCZOS))
    at.save(os.path.join(root, "apple-touch-icon.png"), "PNG", optimize=True)
    # multi-resolution .ico for legacy crawlers
    m.resize((64, 64), Image.LANCZOS).save(
        os.path.join(root, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    return len(SIZES) + 2


if __name__ == "__main__":
    print(build(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
