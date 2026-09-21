#!/usr/bin/env python3
"""Crop editor headshots into the square avatars the site uses.

Framing rule: the head (top of hair to bottom of chin) fills 85% of the square,
sitting slightly above centre, with the face horizontally centred. That reads
correctly all the way down to the 24px byline avatar, which is where a loose
passport crop falls apart.

To swap a photo: drop the new file in SRC, measure three numbers off it —
top of hair, bottom of chin, horizontal centre of the face, in source pixels —
put them in FACES, and run this. Nothing else needs touching; the templates and
schema reference the output by slug.

    python3 _build/tools/crop_portraits.py

The originals live in _build/source/authors/ so this stays reproducible.
"""
from PIL import Image, ImageFilter
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.environ.get("PORTRAIT_SRC", os.path.join(ROOT, "_build", "source", "authors"))
OUT = os.path.join(ROOT, "images", "authors")
SIZES = (192, 64)          # profile block / everything smaller
HEAD_FILL = 1.18           # square side as a multiple of head height
TOP_BIAS = 0.35            # share of the spare room that goes above the head

FACES = {                              # source file : (slug, hair_top, chin, face_cx)
 "jordan-whitcombe.png": ("jordan-whitcombe", 10, 180, 100),
 "sam-kavanagh.png":     ("sam-kavanagh",     12, 188, 104),
 "aroha-tainui.png":     ("aroha-tainui",     20, 190,  98),
 "priya-raman.png":      ("priya-raman",      22, 180, 100),
 "manaia-kerr.png":      ("manaia-kerr",      16, 150,  72),
}


def load(path):
    im = Image.open(path)
    if im.mode == "RGBA":
        bg = Image.new("RGB", im.size, (238, 238, 240))
        bg.paste(im, mask=im.split()[3])
        im = bg
    return im.convert("RGB")


def extend(im, l, t, r, b):
    """Grow the canvas by replicating edge pixels. Invisible against a studio
    backdrop, where a flat fill leaves a visible band."""
    w, h = im.size
    out = Image.new("RGB", (w + l + r, h + t + b))
    out.paste(im, (l, t))
    if t: out.paste(im.crop((0, 0, w, 1)).resize((w, t)), (l, 0))
    if b: out.paste(im.crop((0, h - 1, w, h)).resize((w, b)), (l, h + t))
    W, H = out.size
    if l: out.paste(out.crop((l, 0, l + 1, H)).resize((l, H)), (0, 0))
    if r: out.paste(out.crop((W - r - 1, 0, W - r, H)).resize((r, H)), (W - r, 0))
    return out


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    for fname, (slug, hair_top, chin, cx) in FACES.items():
        im = load(os.path.join(SRC, fname))
        w, h = im.size
        head = chin - hair_top
        side = int(head * HEAD_FILL)
        y0 = hair_top - int((side - head) * TOP_BIAS)
        x0 = cx - side // 2
        l, t = max(0, -x0), max(0, -y0)
        r, b = max(0, x0 + side - w), max(0, y0 + side - h)
        if l or t or r or b:
            im = extend(im, l, t, r, b)
            x0 += l; y0 += t
        im = im.crop((x0, y0, x0 + side, y0 + side))
        for px in SIZES:
            out = im.resize((px, px), Image.LANCZOS)
            out = out.filter(ImageFilter.UnsharpMask(1.0, 70 if px <= 64 else 45, 2))
            out.save(os.path.join(OUT, "%s-%d.jpg" % (slug, px)), "JPEG",
                     quality=90, optimize=True, progressive=True)
        print("  %-20s head fills %.0f%% of a %dpx square" % (slug, head / side * 100, side))


if __name__ == "__main__":
    main()
