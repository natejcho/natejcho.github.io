#!/usr/bin/env python3
"""Generate labeled SVG placeholders for each image on the original site.

Each placeholder is named after the original file so real images can be
dropped in later (as .jpg/.png) with a one-line find/replace in the HTML.
"""
import html
import os

OUT = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUT, exist_ok=True)

# (filename, width, height, label)
PLACEHOLDERS = [
    # About
    ("arieltu-portrait", 1000, 1250, "Portrait: arieltu.jpg"),
    # Documentaries
    ("doc-chip-boom", 1280, 720, "Invisible Costs of Taiwan's Chip Boom (still)"),
    ("doc-superstitions", 1280, 720, "Superstitions (still)"),
    ("doc-dw-ryan-righ", 1280, 720, "DW: Ryan & Righ (still)"),
    ("doc-rittenhouse", 1280, 720, "The Trials of Kyle Rittenhouse (still)"),
    # Projects
    ("project-1", 1200, 800, "Project image 1.jpg"),
    ("project-2", 1200, 800, "Project image 2.jpg"),
    ("project-3", 1200, 800, "Project image 3.jpg"),
    # Photos page (order follows original page)
    ("photo-rally-1", 1200, 800, "Stop Asian Hate rally — photo 1"),
    ("photo-rally-2", 1200, 800, "Stop Asian Hate rally — photo 2"),
    ("photo-heatwave-1", 1200, 800, "Heat wave — photo 1"),
    ("photo-rally-3", 1200, 800, "Stop Asian Hate rally — photo 3"),
    ("photo-heatwave-2", 1200, 800, "Heat wave — photo 2"),
    ("photo-heatwave-3", 1200, 800, "Heat wave — photo 3"),
    ("photo-heatwave-4", 1200, 800, "Heat wave — photo 4"),
    ("photo-heatwave-5", 1200, 800, "Heat wave — photo 5"),
    ("photo-heatwave-6", 1200, 800, "Heat wave — photo 6"),
    ("photo-metoo-1", 1200, 800, "Culture of silence — photo 1"),
    ("photo-metoo-2", 1200, 800, "Culture of silence — photo 2"),
    ("photo-skidrow-1", 1200, 800, "Surviving Skid Row — photo 1"),
    ("photo-skidrow-2", 1200, 800, "Surviving Skid Row — photo 2"),
    ("photo-skidrow-3", 1200, 800, "Surviving Skid Row — photo 3"),
    ("photo-caregivers-1", 1200, 800, "Overeducated & underemployed — photo 1"),
    ("photo-daca-1", 1200, 800, "DACA — photo 1"),
    ("photo-daca-2", 1200, 800, "DACA — photo 2"),
    ("photo-daca-3", 1200, 800, "DACA — photo 3"),
    ("photo-magnolia-1", 1200, 800, "玉蘭花產業 — photo 1"),
    ("photo-magnolia-2", 1200, 800, "玉蘭花產業 — photo 2"),
    ("photo-magnolia-3", 1200, 800, "玉蘭花產業 — photo 3"),
    ("photo-magnolia-4", 1200, 800, "玉蘭花產業 — photo 4"),
]

TPL = """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <rect width="100%" height="100%" fill="#ececec"/>
  <rect x="1" y="1" width="{w2}" height="{h2}" fill="none" stroke="#d5d5d5" stroke-width="2"/>
  <g fill="#9a9a9a" font-family="Helvetica, Arial, sans-serif" text-anchor="middle">
    <text x="50%" y="47%" font-size="{fs}" font-weight="bold">PLACEHOLDER</text>
    <text x="50%" y="47%" dy="{dy}" font-size="{fs2}">{label}</text>
  </g>
</svg>
"""

for name, w, h, label in PLACEHOLDERS:
    fs = max(20, w // 28)
    svg = TPL.format(
        w=w, h=h, w2=w - 2, h2=h - 2,
        fs=fs, fs2=max(14, w // 46), dy=int(fs * 1.6),
        label=html.escape(label),
    )
    with open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

print(f"wrote {len(PLACEHOLDERS)} placeholders to {OUT}")
