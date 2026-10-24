/* Highlights the module you are reading in the jump-link strip
   (theory.html .toolbar, eli5.html nav.chips) and keeps that link scrolled
   into view, since on phones the strip scrolls sideways. */
(function () {
    'use strict';

    var strip = document.querySelector('.toolbar, nav.chips');
    if (!strip) return;

    var links = Array.prototype.slice.call(strip.querySelectorAll('a[href^="#"]'));
    var targets = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
    var current = null;

    function update() {
        var line = strip.getBoundingClientRect().bottom + 24;
        var hit = null;
        targets.forEach(function (t, i) {
            if (t && t.offsetParent !== null && t.getBoundingClientRect().top <= line) hit = links[i];
        });
        if (hit === current) return;
        if (current) current.classList.remove('current');
        current = hit;
        if (!current) return;
        current.classList.add('current');
        if (strip.scrollWidth > strip.clientWidth) {
            var left = current.offsetLeft - (strip.clientWidth - current.offsetWidth) / 2;
            strip.scrollTo({ left: Math.max(0, left), behavior: 'smooth' });
        }
    }

    var queued = false;
    window.addEventListener('scroll', function () {
        if (queued) return;
        queued = true;
        requestAnimationFrame(function () { queued = false; update(); });
    }, { passive: true });
    window.addEventListener('resize', update);
    update();
})();
