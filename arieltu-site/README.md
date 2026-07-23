# arieltu.com — static rebuild

A dependency-free static rebuild of the Squarespace site. Plain HTML + CSS +
a tiny bit of JS for the mobile menu. No build step, no framework.

## Structure

```
index.html              About (homepage)
honors/                 Honors
documentaries/          Documentaries
video-journalism/       Video Journalism (YouTube embeds)
taiwanyc/               Video Series: TaiwaNYC (Facebook embeds)
text/                   Redirects to associated-press/ (mirrors the live site)
associated-press/       Text > Associated Press
law-crime/              Text > Law & Crime
huffington-post/        Text > Huffington Post
projects/               Text > Multimedia Projects
photos/                 Photos
104371213252/           中文作品 (URL kept identical to the original)
css/style.css           All styling
js/main.js              Mobile menu + Text dropdown
assets/                 Placeholder images (see IMAGE-MAP.md)
build.py                Regenerates all HTML pages (optional; edit + rerun)
make_placeholders.py    Regenerates placeholder SVGs (optional)
```

Folder-per-page layout means the URLs match the current site exactly
(`arieltu.com/honors`, `arieltu.com/photos`, etc.), so existing links and
bookmarks keep working after the move.

## Preview locally

Open `index.html` in a browser, or for a proper local server:

```
cd arieltu-site
python3 -m http.server 8000
# visit http://localhost:8000
```

(The Facebook/YouTube embeds need a real server or deployed site to load —
some browsers block them on file:// URLs.)

## Deploy to GitHub Pages

1. Create a new GitHub repository (e.g. `arieltu.com` or `<username>.github.io`).
2. Push this folder's contents to the repo root (not inside a subfolder).
3. Repo → Settings → Pages → Source: "Deploy from a branch" → branch `main`,
   folder `/ (root)` → Save.
4. The site appears at `https://<username>.github.io/<repo>/` within a minute
   or two.
5. Custom domain: in the same Pages settings, enter `www.arieltu.com`, then at
   your domain registrar add a `CNAME` record pointing `www` →
   `<username>.github.io`, and four `A` records on the apex `arieltu.com` →
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
   Enable "Enforce HTTPS" once the certificate is issued (can take ~1 hr).

## Before canceling Squarespace

1. Download every image listed in `IMAGE-MAP.md` (the CDN URLs die with the
   subscription).
2. Drop them into `assets/` and swap the `.svg` references in the HTML.
3. Verify the deployed site, then move DNS, then cancel.
