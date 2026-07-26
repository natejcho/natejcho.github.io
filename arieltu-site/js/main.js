// Mobile menu toggle, "Text" inline folder, and lite YouTube embeds.
(function () {
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // "Text" folder expands inline within the sidebar (accordion). Pages
  // inside the folder render it already open server-side.
  document.querySelectorAll('.has-folder').forEach(function (li) {
    var btn = li.querySelector('.nav-folder-toggle');
    if (btn) {
      btn.addEventListener('click', function () {
        var open = li.classList.toggle('open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    }
  });

  // ---- Lite YouTube ----
  // Each .video-embed[data-yt] starts as a thumbnail + play button.
  // The heavy YouTube iframe is only created when the visitor clicks,
  // so pages with many videos load instantly.
  document.querySelectorAll('.video-embed[data-yt]').forEach(function (box) {
    var id = box.getAttribute('data-yt');

    var btn = document.createElement('button');
    btn.className = 'yt-facade';
    btn.setAttribute('aria-label', 'Play video');

    var img = document.createElement('img');
    img.src = 'https://i.ytimg.com/vi/' + id + '/hqdefault.jpg';
    img.alt = '';
    img.loading = 'lazy';
    // Prefer the HD thumbnail when YouTube has one (it 404s to a 120px
    // gray image otherwise, which we detect by its width).
    var hd = new Image();
    hd.onload = function () { if (hd.naturalWidth > 200) img.src = hd.src; };
    hd.src = 'https://i.ytimg.com/vi/' + id + '/maxresdefault.jpg';

    var play = document.createElement('span');
    play.className = 'yt-btn';
    play.setAttribute('aria-hidden', 'true');

    btn.appendChild(img);
    btn.appendChild(play);
    box.appendChild(btn);

    btn.addEventListener('click', function () {
      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1';
      iframe.title = 'YouTube video';
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      iframe.allowFullscreen = true;
      box.replaceChild(iframe, btn);
    });
  });
})();
