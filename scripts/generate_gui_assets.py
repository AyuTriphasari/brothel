#!/usr/bin/env python3
"""Generate all cyberpunk neon GUI assets for Brothel Connection."""

from PIL import Image, ImageDraw
import numpy as np
import os

GAME = '/root/game'

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def save(img, path):
    ensure_dir(path)
    img.save(path)
    print(f"  ✓ {os.path.relpath(path, GAME)}")

# ─── Textbox ───
def make_textbox():
    print("\n▸ Textbox")
    img = Image.new('RGBA', (1920, 278), (10, 10, 15, 200))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 1919, 2], fill=(0, 240, 255, 180))
    for i in range(8):
        a = int(60 * (1 - i/8))
        draw.rectangle([0, 3+i, 1919, 3+i], fill=(0, 240, 255, a))
    save(img, f'{GAME}/gui/textbox.png')

# ─── Frame ───
def make_frame():
    print("\n▸ Frame")
    img = Image.new('RGBA', (600, 300), (10, 10, 15, 220))
    draw = ImageDraw.Draw(img)
    for i in range(2):
        draw.rectangle([i, i, 599-i, 299-i], outline=(0, 240, 255, 200))
    draw.rectangle([3, 3, 596, 296], outline=(0, 240, 255, 60))
    save(img, f'{GAME}/gui/frame.png')

# ─── Overlays (using numpy for speed) ───
def make_overlays():
    print("\n▸ Overlays")
    # Main menu: left-side gradient darkness
    arr = np.zeros((1080, 1920, 4), dtype=np.uint8)
    arr[:, :, 0] = 8
    arr[:, :, 1] = 8
    arr[:, :, 2] = 12
    x = np.arange(1920)
    alpha = np.clip(220 * (1 - x / 700), 0, 220).astype(np.uint8)
    arr[:, :, 3] = alpha[np.newaxis, :]
    save(Image.fromarray(arr, 'RGBA'), f'{GAME}/gui/overlay/main_menu.png')

    # Game menu overlay
    img = Image.new('RGBA', (1920, 1080), (8, 8, 12, 180))
    save(img, f'{GAME}/gui/overlay/game_menu.png')

    # Confirm overlay
    img = Image.new('RGBA', (1920, 1080), (0, 0, 0, 180))
    save(img, f'{GAME}/gui/overlay/confirm.png')

# ─── Bars ───
def make_rounded_rect(w, h, color, is_bg=False, radius=4):
    img = Image.new('RGBA', (w, h), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    if is_bg:
        draw.rounded_rectangle([0, 0, w-1, h-1], radius=radius, fill=(26, 26, 46, 200))
        draw.rounded_rectangle([0, 0, w-1, h-1], radius=radius, outline=(42, 42, 62, 180))
    else:
        draw.rounded_rectangle([0, 0, w-1, h-1], radius=radius, fill=(*color, 220))
    return img

def make_bars():
    print("\n▸ Bars")
    c = (0, 240, 255)
    save(make_rounded_rect(300, 38, c), f'{GAME}/gui/bar/left.png')
    save(make_rounded_rect(300, 38, c, True), f'{GAME}/gui/bar/right.png')
    save(make_rounded_rect(38, 300, c), f'{GAME}/gui/bar/top.png')
    save(make_rounded_rect(38, 300, c, True), f'{GAME}/gui/bar/bottom.png')

# ─── Scrollbars ───
def make_scrollbars():
    print("\n▸ Scrollbars")
    d = f'{GAME}/gui/scrollbar'
    os.makedirs(d, exist_ok=True)
    for prefix in ['idle_', 'hover_']:
        tc = (0, 240, 255) if prefix == 'hover_' else (60, 60, 80)
        save(make_rounded_rect(300, 18, (26,26,46), True), f'{d}/horizontal_{prefix}bar.png')
        save(make_rounded_rect(60, 18, tc), f'{d}/horizontal_{prefix}thumb.png')
        save(make_rounded_rect(18, 300, (26,26,46), True), f'{d}/vertical_{prefix}bar.png')
        save(make_rounded_rect(18, 60, tc), f'{d}/vertical_{prefix}thumb.png')

# ─── Sliders ───
def make_sliders():
    print("\n▸ Sliders")
    d = f'{GAME}/gui/slider'
    os.makedirs(d, exist_ok=True)
    for prefix in ['idle_', 'hover_']:
        save(make_rounded_rect(525, 38, (26,26,46), True), f'{d}/horizontal_{prefix}bar.png')
        # Thumb
        thumb = Image.new('RGBA', (14, 38), (0,0,0,0))
        draw = ImageDraw.Draw(thumb)
        fc = (0, 240, 255, 255) if prefix == 'hover_' else (100, 100, 130, 220)
        draw.rounded_rectangle([0, 0, 13, 37], radius=4, fill=fc)
        save(thumb, f'{d}/horizontal_{prefix}thumb.png')
        # Vertical
        save(make_rounded_rect(38, 525, (26,26,46), True), f'{d}/vertical_{prefix}bar.png')
        vt = Image.new('RGBA', (38, 14), (0,0,0,0))
        draw = ImageDraw.Draw(vt)
        draw.rounded_rectangle([0, 0, 37, 13], radius=4, fill=fc)
        save(vt, f'{d}/vertical_{prefix}thumb.png')

# ─── Choice Buttons ───
def make_choice_buttons():
    print("\n▸ Choice Buttons")
    for prefix in ['idle_', 'hover_']:
        img = Image.new('RGBA', (1185, 60), (0,0,0,0))
        draw = ImageDraw.Draw(img)
        if prefix == 'hover_':
            draw.rounded_rectangle([0, 0, 1184, 59], radius=4, fill=(10, 10, 20, 220))
            draw.rounded_rectangle([0, 0, 1184, 59], radius=4, outline=(0, 240, 255, 200))
            draw.rounded_rectangle([1, 1, 1183, 58], radius=3, outline=(0, 240, 255, 80))
        else:
            draw.rounded_rectangle([0, 0, 1184, 59], radius=4, fill=(10, 10, 20, 160))
            draw.rounded_rectangle([0, 0, 1184, 59], radius=4, outline=(42, 42, 62, 150))
        save(img, f'{GAME}/gui/button/choice_{prefix}background.png')

# ─── Slot Buttons ───
def make_slot_buttons():
    print("\n▸ Slot Buttons")
    for prefix in ['idle_', 'hover_', 'selected_idle_', 'selected_hover_']:
        img = Image.new('RGBA', (414, 309), (0,0,0,0))
        draw = ImageDraw.Draw(img)
        if 'hover' in prefix:
            draw.rounded_rectangle([0, 0, 413, 308], radius=6, fill=(18, 18, 30, 200))
            draw.rounded_rectangle([0, 0, 413, 308], radius=6, outline=(0, 240, 255, 200))
        elif 'selected' in prefix:
            draw.rounded_rectangle([0, 0, 413, 308], radius=6, fill=(18, 18, 30, 200))
            draw.rounded_rectangle([0, 0, 413, 308], radius=6, outline=(255, 0, 160, 160))
        else:
            draw.rounded_rectangle([0, 0, 413, 308], radius=6, fill=(14, 14, 22, 180))
            draw.rounded_rectangle([0, 0, 413, 308], radius=6, outline=(42, 42, 62, 120))
        save(img, f'{GAME}/gui/button/slot_{prefix}background.png')

# ─── Radio/Check Foregrounds ───
def make_radio_check():
    print("\n▸ Radio/Check Foregrounds")
    for prefix in ['idle_', 'hover_', 'selected_idle_', 'selected_hover_']:
        for kind in ['radio', 'check']:
            img = Image.new('RGBA', (30, 38), (0,0,0,0))
            draw = ImageDraw.Draw(img)
            cx, cy, r = 12, 19, 8
            if 'selected' in prefix:
                c = (0, 240, 255)
                draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(*c, 200), width=2)
                draw.ellipse([cx-4, cy-4, cx+4, cy+4], fill=(*c, 255))
            else:
                draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(80, 80, 100, 150), width=2)
            save(img, f'{GAME}/gui/button/{kind}_{prefix}foreground.png')

# ─── Skip / Notify ───
def make_skip_notify():
    print("\n▸ Skip & Notify indicators")
    img = Image.new('RGBA', (300, 40), (10, 10, 15, 200))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 299, 1], fill=(0, 240, 255, 150))
    d.rectangle([0, 38, 299, 39], fill=(0, 240, 255, 150))
    save(img, f'{GAME}/gui/skip.png')

    img = Image.new('RGBA', (600, 40), (10, 10, 15, 200))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 2, 39], fill=(57, 255, 20, 200))
    save(img, f'{GAME}/gui/notify.png')

# ═══════════════════════════════════════════
if __name__ == '__main__':
    print("═══ Generating Cyberpunk GUI Assets ═══")
    make_textbox()
    make_frame()
    make_overlays()
    make_bars()
    make_scrollbars()
    make_sliders()
    make_choice_buttons()
    make_slot_buttons()
    make_radio_check()
    make_skip_notify()
    print("\n═══ ALL GUI ASSETS GENERATED ═══")
