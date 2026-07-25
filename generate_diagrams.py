"""
SafePlate Kenya v4 - Labeled Diagram & Infographic Generator
Creates programmatic labeled scientific diagrams and 3D infographics using Python PIL / Matplotlib.
"""

import os
from PIL import Image, ImageDraw, ImageFont

def draw_anatomy_diagram():
    width, height = 1000, 600
    img = Image.new('RGB', (width, height), color='#0f172a')
    draw = ImageDraw.Draw(img)

    # Header
    draw.rectangle([(0, 0), (width, 70)], fill='#1e293b')
    draw.text((30, 20), "PESTICIDE TO HUMAN CELL TOXICITY PATHWAY & ORGANIC DEFENSE", fill='#10b981')

    # Draw 5 Stage Blocks
    stages = [
        ("STAGE 1: Crop Spray", "Pesticides applied on crops\n(Chlorfenapyr, Acephate)", "#ef4444", (50, 120)),
        ("STAGE 2: Produce Transit", "Unwashed vegetables transported\nto public markets (Githurai)", "#f59e0b", (240, 120)),
        ("STAGE 3: Gut Ingestion", "Chemicals pass into stomach\n& intestinal lining", "#f59e0b", (430, 120)),
        ("STAGE 4: Blood Transit", "Lipophilic molecules enter plasma\nand circulate through body", "#ef4444", (620, 120)),
        ("STAGE 5: Cell Toxicity", "Mitochondrial stress &\nuncoupled oxidative phosphorylation", "#ef4444", (810, 120))
    ]

    for title, desc, color, (x, y) in stages:
        # Card Box
        draw.rectangle([(x, y), (x + 150, y + 220)], fill='#1e293b', outline=color, width=2)
        draw.text((x + 10, y + 15), title, fill='#ffffff')
        draw.text((x + 10, y + 60), desc, fill='#94a3b8')

        # Arrow
        if x < 800:
            draw.line([(x + 155, y + 110), (x + 185, y + 110)], fill='#10b981', width=4)
            draw.polygon([(x + 185, y + 105), (x + 195, y + 110), (x + 185, y + 115)], fill='#10b981')

    # Lower Shield Section: Organic Bio-Shield
    draw.rectangle([(50, 400), (950, 550)], fill='#064e3b', outline='#10b981', width=3)
    draw.text((70, 420), "🛡️ THE SAFEPLATE ORGANIC BIO-SHIELD SOLUTION", fill='#34d399')
    draw.text((70, 460), "1. 1:3 Vinegar or 2% Salt Water Wash removes 60-70% of surface residues before gut absorption.\n2. Transitioning to PCPB 109 Registered Biopesticides (Neem, Bt, ICIPE 20) eliminates cellular toxicity hazards.", fill='#ffffff')

    os.makedirs("assets/images", exist_ok=True)
    out_path = "assets/images/anatomy_diagram.png"
    img.save(out_path)
    print(f"Generated Anatomy Diagram at: {out_path}")

def draw_wash_infographic():
    width, height = 1000, 500
    img = Image.new('RGB', (width, height), color='#070a12')
    draw = ImageDraw.Draw(img)

    draw.rectangle([(0, 0), (width, 60)], fill='#0f172a')
    draw.text((30, 18), "HOUSEHOLD 60-70% PESTICIDE WASH REDUCTION GUIDE", fill='#f59e0b')

    steps = [
        ("STEP 1: RINSE", "Rinse vegetables under\nrunning cold water.", "#3b82f6", (50, 100)),
        ("STEP 2: SOAK (10 MINS)", "Soak in 1:3 Vinegar or\n2% Salt Solution.", "#10b981", (280, 100)),
        ("STEP 3: PEEL SKINS", "Peel outer skin of\ntomatoes/carrots.", "#f59e0b", (510, 100)),
        ("STEP 4: SAFE MEAL", "Achieve 68% residue\nreduction safety!", "#059669", (740, 100))
    ]

    for title, desc, color, (x, y) in steps:
        draw.rectangle([(x, y), (x + 200, y + 240)], fill='#1e293b', outline=color, width=3)
        draw.text((x + 15, y + 20), title, fill=color)
        draw.text((x + 15, y + 80), desc, fill='#ffffff')

    out_path = "assets/images/infographic_wash_3d.png"
    img.save(out_path)
    print(f"Generated Wash Infographic at: {out_path}")

if __name__ == "__main__":
    draw_anatomy_diagram()
    draw_wash_infographic()
