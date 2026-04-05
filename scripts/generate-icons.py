#!/usr/bin/env python3
"""Generate PWA icons for ultimate-css.
Outputs a branded square icon in PNG at the sizes the manifest + Apple touch icon need."""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pathlib import Path

OUT = Path(__file__).parent.parent / "assets" / "icons"
OUT.mkdir(parents=True, exist_ok=True)

BG_TOP    = (78,  56, 217)   # indigo-600
BG_BOTTOM = (139, 92, 246)   # indigo-500
FG        = (255, 255, 255)


def oklch_to_rgb_linear(lightness, chroma, hue_deg):
    """Approximate OKLCH to sRGB (for correct brand colors on the icon)."""
    # Simple linear gradient between two hand-picked sRGB values; we don't
    # need a full color-space conversion for the icon background.
    return (0, 0, 0)


def make_gradient(size):
    img = Image.new("RGB", (size, size), BG_TOP)
    top = BG_TOP
    bot = BG_BOTTOM
    for y in range(size):
        t = y / max(1, size - 1)
        r = int(top[0] * (1 - t) + bot[0] * t)
        g = int(top[1] * (1 - t) + bot[1] * t)
        b = int(top[2] * (1 - t) + bot[2] * t)
        for x in range(size):
            img.putpixel((x, y), (r, g, b))
    return img


def rounded_mask(size, radius_ratio=0.22):
    mask = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(mask)
    r = int(size * radius_ratio)
    d.rounded_rectangle((0, 0, size, size), radius=r, fill=255)
    return mask


def find_font(size):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size=size)
    return ImageFont.load_default()


def draw_brand(img, size):
    d = ImageDraw.Draw(img)
    # A stylized square-bracket mark — unambiguous CSS / code reference.
    stroke = max(2, int(size * 0.055))
    margin = int(size * 0.24)
    # Left bracket
    x1 = margin
    y1 = int(size * 0.30)
    y2 = int(size * 0.70)
    tick = int(size * 0.12)
    d.line([(x1 + tick, y1), (x1, y1), (x1, y2), (x1 + tick, y2)], fill=FG, width=stroke, joint="curve")
    # Right bracket
    x2 = size - margin
    d.line([(x2 - tick, y1), (x2, y1), (x2, y2), (x2 - tick, y2)], fill=FG, width=stroke, joint="curve")
    # Center slash (CSS feel)
    cx = size // 2
    d.line([(cx - int(size * 0.07), y2 - int(size * 0.02)),
            (cx + int(size * 0.07), y1 + int(size * 0.02))],
           fill=FG, width=stroke)


def make_icon(size, rounded=True):
    img = make_gradient(size)
    draw_brand(img, size)
    if rounded:
        rgba = img.convert("RGBA")
        rgba.putalpha(rounded_mask(size))
        return rgba
    return img.convert("RGBA")


def main():
    # Maskable (safe zone): flat square, no rounding — browser can mask it.
    maskable = make_icon(512, rounded=False)
    maskable.save(OUT / "icon-maskable-512.png", optimize=True)

    # Standard any-purpose icons: pre-rounded for desktop dock.
    for size in (192, 512):
        img = make_icon(size, rounded=True)
        img.save(OUT / f"icon-{size}.png", optimize=True)

    # Apple touch icon: 180x180, full-bleed (iOS/macOS will apply its own mask).
    apple = make_icon(180, rounded=False)
    apple.save(OUT / "apple-touch-icon.png", optimize=True)

    # Favicon 32x32.
    fav = make_icon(32, rounded=True)
    fav.save(OUT / "favicon-32.png", optimize=True)

    print("icons written to", OUT)


if __name__ == "__main__":
    main()
