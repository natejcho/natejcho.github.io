// Mobile menu toggle + "Text" folder dropdown
(function () {
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  document.querySelectorAll('.nav-folder-toggle').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var li = btn.closest('.has-folder');
      var open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  // Close dropdown when clicking elsewhere (desktop)
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.has-folder')) {
      document.querySelectorAll('.has-folder.open').forEach(function (li) {
        li.classList.remove('open');
        var b = li.querySelector('.nav-folder-toggle');
        if (b) b.setAttribute('aria-expanded', 'false');
      });
    }
  });
})();
