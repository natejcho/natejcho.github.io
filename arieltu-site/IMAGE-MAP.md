# Uploading the real images

The site now references the **exact filenames** of your exported images
(the ones in your Dropbox `website` folder). Small gray `.webp`
stand-ins with those same names are committed in `/assets`, so the site
renders fine today — and when you upload your real files, they replace
the stand-ins in place. **No renaming and no HTML edits needed.**

## How to upload

Either way works:

1. **GitHub website** — go to `arieltu-site/assets/` in the repo, click
   *Add file → Upload files*, and drag the files in. The web uploader
   accepts files up to **25 MB each**; every image in your Dropbox
   folder is well under that. (If you saw a "too large" error before, it
   was most likely an original photo over 25 MB — the compressed
   `.webp`/`.png` exports are fine.)
2. **git** — drop the files into `arieltu-site/assets/`, then
   `git add -A && git commit -m "Add real images" && git push`. Git
   pushes accept files up to 100 MB.

No CDN setup is needed: GitHub Pages already serves every committed
file through its own CDN (Fastly).

## Which files are used where

| Upload this file (exact name) | Used on |
| --- | --- |
| 01_arieltu.webp | About (portrait) |
| 02_unveiled.webp | Documentaries — Unveiled |
| 03_invisible+costs+of+TW+chib+boom.webp | Documentaries — Chip Boom |
| 04_Superstitions.webp | Documentaries — Superstitions |
| 05_兩岸第一對：Ryan與Righ的同婚之路.mp4.00_00_37_04.Still001.webp | Documentaries — Ryan與Righ |
| 06_the+trials+of+kyle+rittenhouse.webp | Documentaries — Rittenhouse |
| 07_cultjustice.webp | Documentaries — Cult Justice |
| 08_killer+cases.webp | Documentaries — Killer Cases |
| Multimedia_The culture of silence.webp | Multimedia Projects |
| Multimedia_Overeducated and underemployed.webp | Multimedia Projects |
| Multimedia_Keeping their heads down.webp | Multimedia Projects |

The `TAIWANYC_*.png` screenshots are **no longer needed** — the TaiwaNYC
and 中文作品 pages now use Facebook's stock embeds with no local poster
images.
