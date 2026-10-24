/* Keeps MathJax formulas inside narrow (mobile) screens.
   MathJax 3 cannot line-break, so any formula wider than its container is
   turned into its own horizontal scroller instead of pushing the page wider.
   Display math always gets this; inline math only when it actually overflows,
   so normal inline formulas keep their baseline alignment. */
(function () {
    'use strict';

    var style = document.createElement('style');
    style.textContent =
        'mjx-container[display="true"]{max-width:100%;overflow-x:auto;overflow-y:hidden;padding:2px 0;}' +
        'mjx-container.mjx-wide{display:inline-block;max-width:100%;overflow-x:auto;overflow-y:hidden;vertical-align:middle;}';
    document.head.appendChild(style);

    function blockAncestor(el) {
        var a = el.parentElement;
        while (a && a !== document.body && getComputedStyle(a).display.indexOf('inline') === 0) a = a.parentElement;
        return a || document.body;
    }

    function fit() {
        var list = document.querySelectorAll('mjx-container:not([display="true"])');
        for (var i = 0; i < list.length; i++) {
            var c = list[i];
            c.classList.remove('mjx-wide');
            var w = c.getBoundingClientRect().width;
            if (!w) continue; // hidden (closed <details>, closed drawer) — re-checked on toggle
            var box = blockAncestor(c);
            if (w > box.clientWidth) c.classList.add('mjx-wide');
        }
    }

    var timer;
    function fitSoon() { clearTimeout(timer); timer = setTimeout(fit, 120); }

    window.addEventListener('load', function () {
        var mj = window.MathJax;
        if (mj && mj.startup && mj.startup.promise) mj.startup.promise.then(fit);
        else fit();
    });
    window.addEventListener('resize', fitSoon);
    document.addEventListener('toggle', fitSoon, true);   // <details> opened
    document.addEventListener('click', fitSoon, true);    // drawers / tabs revealed
})();
