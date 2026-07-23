#!/usr/bin/env python3
"""Render all pages of the rebuilt arieltu.com static site."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SOCIAL = """<div class="social-row">
  <a href="mailto:arieltuu@gmail.com" aria-label="Email">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 4h20v16H2V4zm2 2v.5l8 5.4 8-5.4V6H4zm16 2.9-8 5.4-8-5.4V18h16V8.9z"/></svg>
  </a>
  <a href="https://www.instagram.com/dooomay/" target="_blank" rel="noopener" aria-label="Instagram">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3H7zm5 3.5A4.5 4.5 0 1 1 7.5 12 4.5 4.5 0 0 1 12 7.5zm0 2A2.5 2.5 0 1 0 14.5 12 2.5 2.5 0 0 0 12 9.5zM17.8 5a1.2 1.2 0 1 1-1.2 1.2A1.2 1.2 0 0 1 17.8 5z"/></svg>
  </a>
  <a href="http://www.linkedin.com/in/ariel-tu-journalist" target="_blank" rel="noopener" aria-label="LinkedIn">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1-.02 5 2.5 2.5 0 0 1 .02-5zM3 9h4v12H3V9zm7 0h3.8v1.7h.05A4.18 4.18 0 0 1 17.6 8.8c4 0 4.4 2.6 4.4 6V21h-4v-5.5c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9V21h-4V9z"/></svg>
  </a>
</div>"""

# The sidebar shows two visually distinct groups, matching the original
# Squarespace layout: primary pages (bold) and work pages (lighter).
NAV_PRIMARY = [
    ("About", "index.html", "about"),
    ("Honors", "honors/", "honors"),
    ("Documentaries", "documentaries/", "documentaries"),
]

NAV_SECONDARY = [
    ("Video Journalism", "video-journalism/", "video-journalism"),
    ("Video Series: TaiwaNyc", "taiwanyc/", "taiwanyc"),
    ("TEXT_FOLDER", None, None),
    ("Photos", "photos/", "photos"),
    ("中文作品", "104371213252/", "chinese"),
]

TEXT_SUBNAV = [
    ("Associated Press", "associated-press/", "associated-press"),
    ("Law &amp; Crime", "law-crime/", "law-crime"),
    ("Huffington Post", "huffington-post/", "huffington-post"),
    ("Multimedia Projects", "projects/", "projects"),
]


def nav_group(nav_items, prefix, active, cls):
    items = []
    for label, href, key in nav_items:
        if label == "TEXT_FOLDER":
            # The folder opens inline inside the sidebar (accordion), and is
            # rendered already-open on its own subpages.
            is_open = any(k == active for _, _, k in TEXT_SUBNAV)
            sub = "\n".join(
                f'          <li><a href="{prefix}{h}"{aria(active, k)}>{l}</a></li>'
                for l, h, k in TEXT_SUBNAV
            )
            items.append(
                f'      <li class="has-folder{" open" if is_open else ""}">\n'
                f'        <button class="nav-folder-toggle" aria-expanded='
                f'"{"true" if is_open else "false"}">Text</button>\n'
                '        <ul class="nav-folder">\n' + sub + "\n        </ul>\n      </li>"
            )
        else:
            # Root index needs prefix-less handling for "About"
            target = prefix + href if href != "index.html" else (prefix + "index.html")
            items.append(f'      <li><a href="{target}"{aria(active, key)}>{label}</a></li>')
    return f'    <ul class="nav-group {cls}">\n' + "\n".join(items) + "\n    </ul>"


def nav_html(prefix, active):
    return (nav_group(NAV_PRIMARY, prefix, active, "nav-primary") + "\n" +
            nav_group(NAV_SECONDARY, prefix, active, "nav-secondary"))


def aria(active, key):
    return ' aria-current="page"' if active == key else ""


def page(title, active, prefix, body, wide=False, extra_head=""):
    page_cls = "page page--wide" if wide else "page"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="Ariel Tu is a documentary filmmaker and a bilingual journalist.">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap">
<link rel="stylesheet" href="{prefix}css/style.css">
{extra_head}</head>
<body>

<header class="site-header">
  <h1 class="site-title"><a href="{prefix}index.html">Ariel Tu</a></h1>
  <button class="menu-toggle" aria-expanded="false" aria-controls="site-nav">
    <span class="bars" aria-hidden="true"><span></span><span></span><span></span></span>Menu
  </button>
  <nav class="site-nav" id="site-nav" aria-label="Main">
{nav_html(prefix, active)}
  </nav>
  {SOCIAL}
</header>

<main class="{page_cls}">
{body}
</main>

<footer class="site-footer">
  {SOCIAL}
</footer>

<script src="{prefix}js/main.js"></script>
</body>
</html>
"""


def yt(video_id):
    # Lite embed: JS builds a thumbnail facade inside this div; the real
    # YouTube iframe is only injected when the visitor clicks play.
    # <noscript> fallback keeps videos working without JS.
    return (f'<div class="video-embed" data-yt="{video_id}">'
            f'<noscript><iframe src="https://www.youtube-nocookie.com/embed/{video_id}" '
            f'title="YouTube video" allowfullscreen '
            f'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture">'
            f'</iframe></noscript></div>')


def fb(video_url, poster=None, text_h=115):
    # show_text=true keeps the post description / hashtags / like counts
    # visible. The plugin scales its video to the iframe width (16:9) and
    # renders ~text_h px of post text below it; js/main.js keeps the
    # embed's height in sync with its rendered width (the inline height
    # is only a pre-JS estimate). Facebook also often refuses to render a
    # video thumbnail for logged-out visitors, so when a poster is given
    # we lay our own thumbnail + play button over the video area; a click
    # reveals the Facebook player underneath (js/main.js).
    from urllib.parse import quote
    src = ("https://www.facebook.com/plugins/video.php?height=314&href="
           + quote(video_url, safe="") + "&show_text=true&width=560")
    facade = ""
    if poster:
        facade = (f'<button class="fb-facade" aria-label="Play video">'
                  f'<img src="../assets/{poster}.svg" alt="" loading="lazy">'
                  f'<span class="play-btn" aria-hidden="true"></span></button>')
    est_height = 704 * 9 // 16 + text_h  # content column ≈ 704px wide
    return (f'<div class="video-embed fb-embed" data-text-h="{text_h}" '
            f'style="height:{est_height}px">'
            f'<iframe src="{src}" title="Facebook video" loading="lazy" allowfullscreen '
            f'scrolling="no" allow="encrypted-media"></iframe>{facade}</div>')


def ph(name, alt):
    return f'assets/{name}.svg', alt


# ----------------------------------------------------------------
# Page bodies
# ----------------------------------------------------------------

about_body = """  <div class="about-layout">
    <figure class="about-portrait">
      <img src="assets/arieltu-portrait.svg" alt="Portrait of Ariel Tu" width="1000" height="1250">
    </figure>
    <div class="about-bio">
      <p>Ariel Tu is a documentary filmmaker and a bilingual journalist.</p>

      <p>Her experience ranges from covering breaking news for the Associated Press and conducting investigative reporting alongside Brian Ross at the Law&amp;Crime Network, to producing long-form documentaries for major networks such as HBO and A&amp;E.</p>

      <p>She is also known for her popular video series TaiwaNYC, through which she highlighted the achievements of Taiwanese professionals in New York City and explored the complicated nature of living internationally.</p>

      <p>Ariel is a graduate of University of Southern California, with a master&rsquo;s degree in journalism.</p>

      <p>She can write, shoot, produce and edit.</p>
    </div>
  </div>
"""

honors_body = """  <ul class="honors-list">
    <li>2024 Taiwan International Human Rights Film Festival Nominee</li>
    <li>2024 National Culture and Arts Foundation Documentary Production Grant Recipient</li>
    <li>2023 Emmy Award Nominee</li>
    <li>2019 SOPA Award Finalist</li>
    <li>2019 AAJA National Journalism Award</li>
    <li>2017 TEDX Talk: &ldquo;Becoming a Journalist: I Made My First Business Card&rdquo;</li>
    <li>2017 Xinzhuan Award</li>
    <li>2015 Li Zheng-Yu News Award</li>
  </ul>

  <hr>

  <ul class="honors-list">
    <li>2024 臺灣國際人權影展短片入圍</li>
    <li>2024 國家文化藝術基金會紀錄片創作專案補助</li>
    <li>2023 艾美獎紀錄片入圍</li>
    <li>2019 亞洲出版業協會「卓越新聞獎」提名</li>
    <li>2019 亞裔美籍記者協會新聞獎</li>
    <li>2017 TEDX Talk: 22歲實踐記者夢，從自製一張名片開始</li>
    <li>2017 新傳獎最佳新聞平面專題第一名</li>
    <li>2015 李政育新聞獎純淨新聞類第一名</li>
  </ul>
"""

docs_body = """  <article class="work-entry">
    <p class="work-title"><a href="https://www.hbo.com/unveiled-surviving-la-luz-del-mundo" target="_blank" rel="noopener">Unveiled: Surviving La Luz del Mundo</a> | HBO | Field Producer | 2022</p>
    <p class="work-link"><a href="https://www.hbo.com/unveiled-surviving-la-luz-del-mundo" target="_blank" rel="noopener">https://www.hbo.com/unveiled-surviving-la-luz-del-mundo</a></p>
    <p class="work-note">Nominated for an Emmy Award (Outstanding Crime and Justice Documentary)</p>
  </article>

  <article class="work-entry">
    <p class="work-title"><a href="https://youtu.be/DCe-ZZ-tfgg" target="_blank" rel="noopener">Invisible Costs of Taiwan&rsquo;s Chip Boom</a> | TaiwanPlus | Director &amp; Producer | 2026</p>
    <figure><img src="../assets/doc-chip-boom.svg" alt="Still from Invisible Costs of Taiwan's Chip Boom" width="1280" height="720"></figure>
  </article>

  <article class="work-entry">
    <p class="work-title"><a href="https://www.taiwanplus.com/shows/culture/superstitions" target="_blank" rel="noopener">Superstitions</a> | TaiwanPlus | Executive Producer | 2025</p>
    <figure><img src="../assets/doc-superstitions.svg" alt="Still from Superstitions" width="1280" height="720"></figure>
  </article>

  <article class="work-entry">
    <p class="work-title"><a href="https://youtu.be/y7iSvwnvUww" target="_blank" rel="noopener">兩岸第一對：Ryan與Righ的同婚之路</a>｜Deutsche Welle 德國之聲 ｜Director ｜2025</p>
    <figure><img src="../assets/doc-dw-ryan-righ.svg" alt="Still from 兩岸第一對：Ryan與Righ的同婚之路" width="1280" height="720"></figure>
  </article>

  <article class="work-entry">
    <p class="work-title"><a href="https://tvfinternational.com/programme/29981/the-trials-of-kyle-rittenhouse?trailer=1" target="_blank" rel="noopener">The Trials of Kyle Rittenhouse</a> | Law&amp;Crime Network | Producer | 2024</p>
    <figure><img src="../assets/doc-rittenhouse.svg" alt="Still from The Trials of Kyle Rittenhouse" width="1280" height="720"></figure>
  </article>

  <article class="work-entry">
    <p class="work-title"><a href="https://www.hulu.com/series/cult-justice-f4cd29c6-5b11-40f6-a6f8-b99ca8e64b7f" target="_blank" rel="noopener">Cult Justice</a> | HULU | Producer | 2023</p>
    <p class="work-link"><a href="https://lawandcrimeproductions.com/work/cult-justice/" target="_blank" rel="noopener">https://lawandcrimeproductions.com/work/cult-justice/</a></p>
  </article>

  <article class="work-entry">
    <p class="work-title"><a href="https://www.aetv.com/shows/killer-cases" target="_blank" rel="noopener">Killer Cases</a> | A&amp;E | Producer | 2022-2023</p>
    <p class="work-link"><a href="https://www.aetv.com/shows/killer-cases" target="_blank" rel="noopener">https://www.aetv.com/shows/killer-cases</a></p>
  </article>
"""

vj_ids = ["41AmCcgg9hw", "qEXrODPL-Cw", "617knCkXUMA", "r1nn7KGN6ds",
          "AZEnxHBcYSM", "5MaoiK97q6g", "vVrUXnE69aw", "43d_0H9a56s",
          "RBEW3WS71sQ", "r9LYLD431MI", "XwpwJ2HxKDM"]
vj_body = "  " + "\n  ".join(yt(v) for v in vj_ids) + "\n"

taiwanyc_body = f"""  <h2>Season 1</h2>

  <div class="episode">
    <p class="ep-title">EP1: <a href="http://bit.ly/taiwanyc-9m88" target="_blank" rel="noopener">9m88 ─ 歌手、音樂人 Singer Song Writer</a></p>
    {fb("https://www.facebook.com/Crossing.cw/videos/950250001977527/", "fb-taiwanyc-ep1")}
  </div>

  <div class="episode">
    <p class="ep-title">EP2: <a href="http://bit.ly/taiwanyc-mitchlin" target="_blank" rel="noopener">林明學 Mitch Lin ─ 配樂作曲家 Film Score Composer</a></p>
    {fb("https://www.facebook.com/Crossing.cw/videos/704495246736831/", "fb-taiwanyc-ep2")}
  </div>

  <div class="episode">
    <p class="ep-title">EP3: <a href="http://bit.ly/taiwanyc-mia" target="_blank" rel="noopener">Mia ─ Taiwanese Waves主辦人、經紀人 Taiwanese Waves Founder &amp; Music Agent</a></p>
    {fb("https://www.facebook.com/Crossing.cw/videos/508582750011452/", "fb-taiwanyc-ep3")}
  </div>

  <div class="episode">
    <p class="ep-title">EP4: <a href="http://bit.ly/taiwanyc-seaformosa" target="_blank" rel="noopener">海味鮮台派 Sea Formosa ─ 返鄉投票影像企劃 Voting Video Project</a></p>
    {fb("https://www.facebook.com/Crossing.cw/videos/2618864651566880/", "fb-taiwanyc-ep4")}
  </div>

  <div class="episode">
    <p class="ep-title">EP5 &amp; 6: <a href="https://www.facebook.com/watch/?v=2539421076306380" target="_blank" rel="noopener">黃再添 Patrick Huang ─ 布魯克林藝站創辦人 Founder of Brooklyn Artists Studio</a></p>
    {fb("https://www.facebook.com/Crossing.cw/videos/2539421076306380/", "fb-taiwanyc-ep5")}
    {fb("https://www.facebook.com/Crossing.cw/videos/2730619417192517/", "fb-taiwanyc-ep6")}
  </div>

  <div class="episode">
    <p class="ep-title"><a href="https://www.facebook.com/Crossing.cw/videos/358580865580597" target="_blank" rel="noopener">EP 7: 886 ─ 紐約台菜餐廳 Taiwanese Restaurant in NY</a></p>
    {fb("https://www.facebook.com/Crossing.cw/videos/358580865580597/", "fb-taiwanyc-ep7")}
  </div>

  <div class="episode">
    <p class="ep-title"><a href="https://fb.watch/ln33siT9f3/" target="_blank" rel="noopener">EP 8: 系列回顧 Season Finale</a></p>
    {fb("https://www.facebook.com/Crossing.cw/videos/4414730291941938/", "fb-taiwanyc-ep8")}
  </div>

  <h2>Season 2</h2>

  <div class="episode">
    <p class="ep-title"><a href="https://www.facebook.com/Crossing.cw/videos/2519584064988033" target="_blank" rel="noopener">EP 1: Isabelle Chiang 菜鳥的職涯筆記 — 職涯教練 Career Coach</a></p>
    {fb("https://www.facebook.com/Crossing.cw/videos/2519584064988033/", "fb-taiwanyc-s2ep1")}
  </div>
"""

ap_links = [
    ("AP Exclusive: Tests show toxin in chain stores\u2019 jewelry", "https://apnews.com/63aa51c1f9d943d8844cfbf11fba84e8"),
    ("Los Angeles takes step toward banning sale of fur products", "https://apnews.com/c792344880844bd283a4012774a16cfa"),
    ("Memorials held for 2008 LA train crash that killed 25", "https://www.apnews.com/5bc7822879f54012abdd832443f5f9b6/Memorials-held-for-2008-LA-train-crash-that-killed-25"),
    ("1st Los Angeles temporary homeless housing site set to open", "https://www.apnews.com/80f2f75b13494da28a71c09e5b9ddf0c/1st-Los-Angeles-temporary-homeless-housing-site-set-to-open"),
    ("LA teachers authorize a strike if no labor deal is reached", "https://www.apnews.com/ee81a030a71e4ac7952ab01cdd669c46/LA-teachers-authorize-a-strike-if-no-labor-deal-is-reached"),
    ("Hundreds of fish die in lagoon in tony Malibu, California", "https://www.apnews.com/d0499ab5499e418eb4c479d1f4d4f802/Hundreds-of-fish-die-in-lagoon-in-tony-Malibu,-California"),
    ("University to expand into LA\u2019s old Herald Examiner building", "https://www.apnews.com/85f1d10268f84c9994b585ca282a0865/University-to-expand-into-LA's-old-Herald-Examiner-building"),
    ("Man who swindled $13 million from VA sentenced to 6 years", "https://www.apnews.com/182187212361455491f749d906d0d55c"),
    ("Stinky \u2018corpse flower\u2019 in full bloom in California", "https://www.apnews.com/c195efee8bd44f8d9479bbc643cabf71/Stinky-'corpse-flower'-in-full-bloom-in-California"),
    ("Famous pool at California\u2019s Hearst Castle being filled again", "https://www.apnews.com/84c1b85825e74a73986541ea0269ce21/Famous-pool-at-California's-Hearst-Castle-being-filled-again"),
    ("Judge sets deadline for Army specialist\u2019s citizenship ruling", "https://www.apnews.com/3cbf16d16fc44ed6974b6ade7070c390/Judge-sets-deadline-for-Army-specialist's-citizenship-ruling"),
    ("Judge dismisses case against suspected LA \u2018Skid Row Stabber\u2019", "https://apnews.com/8124568688ff4532b50933f666c737a8"),
    ("Famed California research center settles 2 gender bias suits", "https://www.apnews.com/7eb49115cd154c208dd7821acd88923e/Famed-California-research-center-settles-2-gender-bias-suits"),
    ("5 killed after plane nosedived into California parking lot", "https://www.apnews.com/6094d45578e14cb0b704b7902ded7c78/5-killed-when-small-plane-crashes-in-California-parking-lot"),
    ("Apple store planned for historic theater on LA\u2019s Broadway", "https://www.apnews.com/0aa42a0328d0471db9aba9fb3a5d8218/Apple-store-planned-for-historic-theater-on-LA's-Broadway"),
    ("Family of hostage killed by Los Angeles police files claim", "https://apnews.com/e1595828de7749a3a2f18fd67fd0cb77/Family-of-hostage-killed-by-Los-Angeles-police-files-claim"),
    ("Stinky \u2018corpse flower\u2019 expected to bloom in California", "https://www.apnews.com/4fc6ad7b5f87404890af39d4811be456/Stinky-'corpse-flower'-expected-to-bloom-in-California"),
    ("Chinese turtle-smuggling flight attendants fined in LA", "https://www.apnews.com/a179ce519f73490caff92cf8ec902cc4/Chinese-turtle-smuggling-flight-attendants-fined-in-LA"),
    ("LA sheriff releases sketch in renewed probe of 2005 killing", "https://www.apnews.com/e9de0ee1a8de46feab761ea9016780f4/LA-sheriff-releases-sketch-in-renewed-probe-of-2005-killing"),
    ("2 sentenced in murder of Chinese grad student in Los Angeles", "https://www.apnews.com/e5d22bdbfb8748fdabd0e86e138d9213/2-sentenced-in-murder-of-Chinese-grad-student-in-Los-Angeles"),
    ("LeBron James a no-show at pizza party celebrating LA arrival", "https://www.apnews.com/a396ef065f744f2a87e975a8d3149dab/LeBron-James-a-no-show-at-pizza-party-celebrating-LA-arrival"),
    ("Wounded burro evades capture in Southern California", "https://www.usnews.com/news/best-states/california/articles/2018-07-19/wounded-burro-evades-capture-in-southern-california"),
    ("Harvey Weinstein asks judge to dismiss Ashley Judd lawsuit", "https://www.apnews.com/a8be5a8caaae45b4bd790fe290de70de/Harvey-Weinstein-asks-judge-to-dismiss-Ashley-Judd-lawsuit"),
    ("Southern California hit by record-breaking heat wave", "https://www.apnews.com/85bb3d85ee244405b7636501f370682d"),
]
ap_body = ('  <p>I covered major breaking news and court cases in and around Los Angeles at the AP.</p>\n'
           '  <ul class="article-list">\n' +
           "\n".join(f'    <li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in ap_links) +
           "\n  </ul>\n")

lc_links = [
    ("Their 21-Year-Old Daughter Was Murdered by a Fake Uber Driver. Here\u2019s What the Grieving Parents Are Doing to Help Keep Others Safe.", "https://lawandcrime.com/ross-investigates/their-21-year-old-daughter-was-murdered-by-a-fake-uber-driver-heres-what-the-grieving-parents-are-doing-to-help-keep-others-safe/"),
    ("\u2018The Problem Was Much Bigger Than We Initially Expected\u2019: Virginia Summer Camp Faces New Sexual Abuse and Cover-up Allegations", "https://lawandcrime.com/ross-investigates/the-problem-was-much-bigger-than-we-initially-expected-virginia-summer-camp-faces-new-sexual-abuse-and-cover-up-allegations/"),
    ("Leader of Troubled Summer Camp Retires Following Allegations of Rape and Sexual Abuse", "https://lawandcrime.com/ross-investigates/leader-of-troubled-summer-camp-retires-following-allegations-of-rape-and-sexual-abuse/"),
    ("\u2018They\u2019re Probably Going to Try to Kill Him\u2019: Inmate and Former Prison Warden Agree Derek Chauvin Will Be \u2018Instant Target\u2019 in Prison", "https://lawandcrime.com/ross-investigates/theyre-probably-going-to-try-to-kill-him-inmate-and-former-prison-warden-agree-derek-chauvin-will-be-instant-target-in-prison/"),
    ("Former CIA Officer Speaks Out About Mysterious Illness \u2018Havana Syndrome\u2019", "https://lawandcrime.com/ross-investigates/former-cia-officer-speaks-out-about-mysterious-illness-havana-syndrome/"),
    ("Lawsuit: United States Tennis Association Failed to Protect Young Athletes from Sexual Abuse by Coach", "https://lawandcrime.com/ross-investigates/lawsuit-united-states-tennis-association-failed-to-protect-young-athletes-from-sexual-abuse-by-coach/"),
    ("Eight Women Allege Harassment and Sexual Abuse at \u2018Cult-Like\u2019 Virginia Summer Camp", "https://lawandcrime.com/ross-investigates/eight-women-allege-harassment-and-sexual-abuse-at-cult-like-virginia-summer-camp/"),
    ("Ex-Minneapolis Police Chief Speaks Out on Derek Chauvin Trial and \u2018Systemic Racism\u2019 on the Force", "https://lawandcrime.com/ross-investigates/ex-minneapolis-police-chief-speaks-out-on-derek-chauvin-trial-and-systemic-racism-on-the-force/"),
    ("\u2018I\u2019m Angry\u2019: Man Once Shot by Derek Chauvin Speaks Out as Murder Trial in George Floyd\u2019s Death Begins", "https://lawandcrime.com/ross-investigates/im-angry-man-once-shot-by-derek-chauvin-speaks-out-as-murder-trial-in-george-floyds-death-begins/"),
    ("Double Whammy: New York AG Sues Amazon for Failing to Protect Workers from COVID-19 as Alabama Employees Vote on Union", "https://lawandcrime.com/ross-investigates/double-whammy-new-york-ag-sues-amazon-for-failing-to-protect-workers-from-covid-19-as-alabama-employees-vote-on-union/"),
    ("Medical Ethicist: Olympic Athletes Should Be Allowed to Go to the Head of the Vaccine Line", "https://lawandcrime.com/ross-investigates/medical-ethicist-olympic-athletes-should-be-allowed-to-go-to-the-head-of-the-vaccine-line/"),
    ("FTC Complaint Puts Walmart\u2019s \u2018Made in USA\u2019 Labels Under the Microscope", "https://lawandcrime.com/ross-investigates/ftc-complaint-puts-walmarts-made-in-usa-labels-under-the-microscope/"),
    ("\u2018The Greatest Deception Ever\u2019: Firefighters and Scientists Sound the Alarm About Cancer-Causing Chemicals in Protective Gear", "https://lawandcrime.com/ross-investigates/the-greatest-deception-ever-firefighters-and-scientists-sound-the-alarm-about-cancer-causing-chemicals-in-protective-gear/"),
    ("Activist Nan Goldin Says Multi-Billion Dollar Purdue Pharma Settlement Not Enough: Sackler Family Should \u2018Go to Jail\u2019", "https://lawandcrime.com/ross-investigates/activist-nan-goldin-says-multi-billion-dollar-purdue-pharma-settlement-not-enough-sackler-family-should-go-to-jail/"),
    ("Alleged \u2018Handmaiden\u2019 Enters Guilty Plea in Megachurch Sexual Abuse Case", "https://lawandcrime.com/ross-investigates/alleged-handmaiden-enters-guilty-plea-in-megachurch-sexual-abuse-case/"),
    ("EXCLUSIVE: Outrage over Teen Swimmers Sexually Abused by USA Swimming Coaches", "https://lawandcrime.com/high-profile/exclusive-outrage-over-teen-swimmers-sexually-abused-by-usa-swimming-coaches/"),
    ("\u2018He Will Understand My Dilemma With the Corrupt\u2019 DOJ: Whistleblower Seeks Pardon From Trump", "https://lawandcrime.com/uncategorized/he-will-understand-my-dilemma-with-the-corrupt-doj-whistleblower-seeks-pardon-from-trump/"),
    ("Abuse Victims Call for \u2018Holy Week\u2019 Atonement by the Catholic Church", "https://lawandcrime.com/uncategorized/abuse-victims-call-for-holy-week-atonement-by-the-catholic-church/"),
    ("Former Senator\u2019s Wife Wants FBI To Investigate Alleged Bank Fraud", "https://lawandcrime.com/high-profile/former-senators-wife-wants-fbi-to-investigate-alleged-bank-fraud/"),
    ("Lawyer Who Questioned Donald Trump About Felix Sater Says He Told \u2018Flat Untruth\u2019 Under Oath", "https://lawandcrime.com/ross-investigates/lawyer-who-questioned-donald-trump-under-oath-says-he-told-flat-untruth-under-oath/"),
    ("Monday Hearing Set for ISIS Bride After State Department Says She Has \u2018No Legal Basis\u2019 Being in U.S.", "https://lawandcrime.com/ross-investigates/monday-hearing-set-for-isis-bride-who-wants-to-come-home/"),
    ("Stanford Ethics Professor Slams Museums for Taking OxyContin $$", "https://lawandcrime.com/ross-investigates/stanford-ethics-professor-slams-museums-for-taking-oxycontin/"),
    ("Inside the El Chapo Trial; Brutality, Bribes, Murder, Mistresses", "https://lawandcrime.com/high-profile/inside-the-el-chapo-trial-brutality-bribes-murder-mistresses/"),
    ("Human Rights Watch: Saudi Dissidents Owed an Apology, Honesty from Twitter", "https://lawandcrime.com/high-profile/human-rights-watch-saudi-dissidents-owed-an-apology-honesty-from-twitter/"),
]
lc_body = ('  <ul class="article-list article-list--em">\n' +
           "\n".join(f'    <li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in lc_links) +
           "\n  </ul>\n")

hp_body = """  <ul class="article-list">
    <li><a href="https://www.huffingtonpost.com/entry/skid-row-homeless-women_us_5acfa9e9e4b0edca2cb7cb57" target="_blank" rel="noopener">Surviving Skid Row: Women&rsquo;s stories of assault, fear, and finding friendship</a></li>
  </ul>
"""

projects_body = """  <article class="project">
    <figure><img src="../assets/project-1.svg" alt="The culture of silence — lead image" width="1200" height="800"></figure>
    <h3>The culture of silence:<br>Filipino women hesitate to say #MeToo when no one says me</h3>
    <p>The #MeToo and #TimesUp movements have swept the U.S. in the last year, emboldening women to step forward to name their assailants and to demand justice for victims of sexual misconduct and violence. In the Philippines, more than 7,000 miles away, women and girls can only dream of finding similar relief in a country they describe as full of rapists, where survivors of sexual violence must remain in the shadows, afraid to speak up.</p>
    <a class="read-link" href="https://uscstoryspace.com/2017-2018/yaolintu/capstone/index.html" target="_blank" rel="noopener">Read</a>
  </article>

  <article class="project">
    <figure><img src="../assets/project-2.svg" alt="Overeducated and underemployed — lead image" width="1200" height="800"></figure>
    <h3>Overeducated and underemployed:<br>Filipino migrants armed with degrees only find work as caregivers</h3>
    <p>Once a university dean in the Philippines, Aleja Plaza never thought she would become a caregiver for the elderly. Since she came to Los Angeles from Mindanao in 2012, her daily routine has switched from approving courses and conducting research to changing diapers and spoon feeding senior citizens.</p>
    <a class="read-link" href="https://uscstoryspace.com/2017-2018/yaolintu/Fall_Final/index.html" target="_blank" rel="noopener">Read</a>
  </article>

  <article class="project">
    <figure><img src="../assets/project-3.svg" alt="Keeping their heads down — lead image" width="1200" height="800"></figure>
    <h3>Keeping their heads down:<br>Many asians remain silent in the DACA debate</h3>
    <p>Gabrielle Cabalza was 9 years old when she realized her family was not like everyone else&rsquo;s. One day after school, she walked into the dining room, where the air was dense with fear and sadness. She found her parents sobbing at the table because of a traffic ticket.</p>
    <a class="read-link" href="http://archive.uscstoryspace.com/2017-2018/yaolintu/Fall_Midterm/midtermtemplate/" target="_blank" rel="noopener">READ</a>
  </article>
"""


def grid(*names_alts):
    figs = "\n".join(
        f'      <figure><img src="../assets/{n}.svg" alt="{a}" loading="lazy" width="1200" height="800"></figure>'
        for n, a in names_alts)
    return f'    <div class="photo-grid">\n{figs}\n    </div>'


photos_body = f"""  <section class="photo-section">
    <p class="photo-caption">Stop Asian Hate rally</p>
{grid(("photo-rally-1", "Stop Asian Hate rally"), ("photo-rally-2", "Stop Asian Hate rally"), ("photo-rally-3", "Stop Asian Hate rally"))}
  </section>

  <section class="photo-section">
    <p class="photo-caption">Southern California hit by record-breaking heat wave</p>
{grid(("photo-heatwave-1", "Record-breaking heat wave"), ("photo-heatwave-2", "Record-breaking heat wave"), ("photo-heatwave-3", "Record-breaking heat wave"), ("photo-heatwave-4", "Record-breaking heat wave"), ("photo-heatwave-5", "Record-breaking heat wave"), ("photo-heatwave-6", "Record-breaking heat wave"))}
  </section>

  <section class="photo-section">
    <p class="photo-caption">The culture of silence:<br>Filipino women hesitate to say #MeToo when no one says me</p>
{grid(("photo-metoo-1", "The culture of silence"), ("photo-metoo-2", "The culture of silence"))}
  </section>

  <section class="photo-section">
    <p class="photo-caption">Surviving Skid Row:<br>Women&rsquo;s stories of assault, fear, and finding friendship</p>
{grid(("photo-skidrow-1", "Surviving Skid Row"), ("photo-skidrow-2", "Surviving Skid Row"), ("photo-skidrow-3", "Surviving Skid Row"))}
  </section>

  <section class="photo-section">
    <p class="photo-caption">Overeducated and underemployed:<br>Filipino migrants armed with degrees only find work as caregivers</p>
{grid(("photo-caregivers-1", "Overeducated and underemployed"),)}
  </section>

  <section class="photo-section">
    <p class="photo-caption">Keeping their heads down: Many asians remain silent in the DACA debate</p>
{grid(("photo-daca-1", "DACA"), ("photo-daca-2", "DACA"), ("photo-daca-3", "DACA"))}
  </section>

  <section class="photo-section">
    <p class="photo-caption">你買的玉蘭花是這樣來的──<br>撐起數百弱勢家庭的玉蘭花產業</p>
{grid(("photo-magnolia-1", "玉蘭花產業"), ("photo-magnolia-2", "玉蘭花產業"), ("photo-magnolia-3", "玉蘭花產業"), ("photo-magnolia-4", "玉蘭花產業"))}
  </section>
"""

chinese_body = f"""  <h3 class="pub-heading">報導者：</h3>
  <ul class="article-list">
    <li><a href="https://www.twreporter.org/a/opinion-atlanta-spa-shootings-with-fears-of-asian-women-bias" target="_blank" rel="noopener">亞特蘭大槍擊案背後的種族、性別和階級──那些亞裔女性面對的騷擾和恐懼</a></li>
    <li><a href="https://www.twreporter.org/a/covid-19-usa-mask-policy-crisis" target="_blank" rel="noopener">美國「口罩防疫」轉彎記：混亂宣傳、拖延官僚燒出疫情危機</a></li>
    <li><a href="https://www.twreporter.org/a/sexual-assault-philippines-metoo" target="_blank" rel="noopener">沒有Me，何來＃MeToo──菲律賓消失的性侵受害者</a></li>
    <li><a href="https://www.twreporter.org/a/daca-plan-end-cabalza-story" target="_blank" rel="noopener">走過沈寂的年少 在美亞裔無證青年的告白</a></li>
    <li><a href="https://www.twreporter.org/a/asian-american-immigrants-keep-silent-on-daca" target="_blank" rel="noopener">亞裔無證移民的恥感，讓他們在DACA裡噤聲</a></li>
    <li><a href="https://www.twreporter.org/a/white-champak-vender" target="_blank" rel="noopener">你買的玉蘭花是這樣來的──撐起數百弱勢家庭的玉蘭花產業</a></li>
  </ul>

  {fb("https://www.facebook.com/twreporter/videos/3137423189888156/", "fb-twreporter", 161)}

  <h3 class="pub-heading">換日線：</h3>
  <ul class="article-list">
    <li><a href="https://crossing.cw.com.tw/blogTopic.action?id=797&amp;nid=11127" target="_blank" rel="noopener">種族、語言與「被包裝的」美國夢──我在美聯社實習的那些日子</a></li>
    <li><a href="https://crossing.cw.com.tw/blogTopic.action?id=797&amp;nid=8597" target="_blank" rel="noopener">每個人都有故事──隨機採訪一個陌生人，能不能帶回好報導？</a></li>
    <li><a href="https://crossing.cw.com.tw/blogTopic.action?id=797&amp;nid=8522" target="_blank" rel="noopener">我帶著筆桿，穿梭洛杉磯的暗角重新定義「安全」</a></li>
  </ul>

  <h3 class="pub-heading">上報：</h3>
  <ul class="article-list">
    <li><a href="http://intnews7.wixsite.com/escapingworkers" target="_blank" rel="noopener">逃跑移工的「牢」動真相</a></li>
    <li><a href="https://www.upmedia.mg/news_info.php?SerialNo=15111" target="_blank" rel="noopener">台灣人真的冷漠嗎？ 戳破移工議題的同溫層泡泡</a></li>
  </ul>

  <h3 class="pub-heading">關鍵評論網：</h3>
  <ul class="article-list">
    <li><a href="https://www.thenewslens.com/article/45733" target="_blank" rel="noopener">做個積極的閱聽人不能只有抱怨，請用行動表明「我想看見更多深度新聞」</a></li>
  </ul>

  <h3 class="pub-heading">天下獨評：</h3>
  <ul class="article-list">
    <li><a href="https://opinion.cw.com.tw/blog/profile/52/article/4190" target="_blank" rel="noopener">悲劇後再省──誰成全了這場死刑議題的炒作？</a></li>
  </ul>
"""

PAGES = [
    # (out_path, title, active_key, prefix, body, wide)
    ("index.html", "Ariel Tu", "about", "", about_body, False),
    ("honors/index.html", "Honors — Ariel Tu", "honors", "../", honors_body, False),
    ("documentaries/index.html", "Documentaries — Ariel Tu", "documentaries", "../", docs_body, False),
    ("video-journalism/index.html", "Video Journalism — Ariel Tu", "video-journalism", "../", vj_body, False),
    ("taiwanyc/index.html", "TaiwaNyc — Ariel Tu", "taiwanyc", "../", taiwanyc_body, False),
    ("associated-press/index.html", "Associated Press — Ariel Tu", "associated-press", "../", ap_body, False),
    ("law-crime/index.html", "Law & Crime — Ariel Tu", "law-crime", "../", lc_body, False),
    ("huffington-post/index.html", "Huffington Post — Ariel Tu", "huffington-post", "../", hp_body, False),
    ("projects/index.html", "Multimedia Projects — Ariel Tu", "projects", "../", projects_body, False),
    ("photos/index.html", "Photos — Ariel Tu", "photos", "../", photos_body, True),
    ("104371213252/index.html", "杜曜霖 — Ariel Tu", "chinese", "../", chinese_body, False),
]

for out_path, title, active, prefix, body, wide in PAGES:
    html_out = page(title, active, prefix, body, wide)
    full = os.path.join(ROOT, out_path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html_out)
    print("wrote", out_path)

# /text mirrors the live site: it forwards to Associated Press.
redirect = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=../associated-press/">
<link rel="canonical" href="../associated-press/">
<title>Text — Ariel Tu</title>
</head>
<body>
<p><a href="../associated-press/">Continue to Text &rsaquo; Associated Press</a></p>
</body>
</html>
"""
with open(os.path.join(ROOT, "text/index.html"), "w", encoding="utf-8") as f:
    f.write(redirect)
print("wrote text/index.html (redirect)")
