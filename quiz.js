/* Theme toggle + MCQ test mode. Expects window.QUIZ_BANK (see quiz_bank.js):
   { m: 1-12, src: 'assignment' | 'lecture', q, o: [4 options], a: correct index, e: explanation } */
(function () {
    'use strict';

    // ---------- Theme ----------
    var root = document.documentElement;
    var themeBtn = document.getElementById('theme-toggle-btn');
    function applyTheme(t) {
        root.setAttribute('data-theme', t);
        try { localStorage.setItem('theme', t); } catch (e) {}
        if (themeBtn) themeBtn.firstElementChild.textContent = t === 'dark' ? '☀️' : '🌙';
    }
    applyTheme(root.getAttribute('data-theme') || 'dark');
    if (themeBtn) themeBtn.addEventListener('click', function () {
        applyTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
    });

    // ---------- Test mode ----------
    var MODULES = [
        'Foundations of Reliability', 'Probability & System Reliability', 'Discrete Distributions',
        'Continuous Distributions & Hazard', 'Sampling & CLT', 'Point Estimation & CIs',
        'Hypothesis Testing & GoF', 'ANOVA', 'Correlation & Regression', 'Auto-Regression',
        'Logistic Regression', 'Bayes, k-NN & SVM'
    ];
    var bank = window.QUIZ_BANK || [];
    var overlay = document.getElementById('test-overlay');
    var rootEl = document.getElementById('test-root');
    var cfg = { scope: 'all', mods: [], src: 'both', count: 20, shuffle: true };
    var run = null;

    function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
    function shuffle(a) {
        a = a.slice();
        for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
        return a;
    }
    function typeset() {
        if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([rootEl]).catch(function () {});
    }
    function pool() {
        return bank.filter(function (x) {
            if (cfg.scope === 'pick' && cfg.mods.indexOf(x.m) < 0) return false;
            if (cfg.src !== 'both' && x.src !== cfg.src) return false;
            return true;
        });
    }
    function open() { overlay.classList.add('open'); document.body.style.overflow = 'hidden'; renderSetup(); }
    function close() { overlay.classList.remove('open'); document.body.style.overflow = ''; }

    function renderSetup() {
        var avail = pool().length;
        var modChips = MODULES.map(function (n, i) {
            var m = i + 1, cnt = bank.filter(function (x) { return x.m === m; }).length;
            var on = cfg.mods.indexOf(m) >= 0;
            return '<label class="test-chip' + (on ? ' on' : '') + '"><input type="checkbox" data-mod="' + m + '"' + (on ? ' checked' : '') + '> M' + m + ': ' + esc(n) + ' (' + cnt + ')</label>';
        }).join('');
        function radio(name, val, label, cur) {
            return '<label class="test-chip' + (cur === val ? ' on' : '') + '"><input type="radio" name="' + name + '" value="' + val + '"' + (cur === val ? ' checked' : '') + '> ' + label + '</label>';
        }
        var counts = [10, 20, 30, 50, 0].map(function (n) {
            return '<option value="' + n + '"' + (cfg.count === n ? ' selected' : '') + '>' + (n || 'All available') + '</option>';
        }).join('');
        rootEl.innerHTML =
            '<div class="test-topbar"><h2>📝 MCQ Test</h2><button class="test-btn ghost" data-act="close">✕ Close</button></div>' +
            '<div class="test-card"><h3>1. Scope</h3><div class="test-row">' +
            radio('scope', 'all', 'All modules', cfg.scope) + radio('scope', 'pick', 'Select modules', cfg.scope) + '</div>' +
            '<div class="test-mods' + (cfg.scope === 'pick' ? '' : ' disabled') + '">' + modChips + '</div></div>' +
            '<div class="test-card"><h3>2. Question source</h3><div class="test-row">' +
            radio('src', 'both', 'Both', cfg.src) + radio('src', 'assignment', 'Assignment questions', cfg.src) +
            radio('src', 'lecture', 'Lecture-based practice', cfg.src) + '</div></div>' +
            '<div class="test-card"><h3>3. Options</h3><div class="test-row"><label>Questions: <select class="test-select" id="t-count">' + counts + '</select></label>' +
            '<label class="test-chip' + (cfg.shuffle ? ' on' : '') + '"><input type="checkbox" id="t-shuffle"' + (cfg.shuffle ? ' checked' : '') + '> Shuffle</label></div></div>' +
            '<div class="test-row"><button class="test-btn" data-act="start"' + (avail ? '' : ' disabled') + '>Start test (' + avail + ' available)</button>' +
            (avail ? '' : '<span style="color:var(--text-muted)">Select at least one module with questions.</span>') + '</div>';
    }

    function startRun(qs) {
        run = { qs: qs, i: 0, ans: [] };
        renderQ();
    }

    function renderQ() {
        var item = run.qs[run.i], n = run.qs.length;
        var order = cfg.shuffle ? shuffle(item.o.map(function (_, k) { return k; })) : item.o.map(function (_, k) { return k; });
        run.order = order;
        run.answered = false;
        var opts = order.map(function (k, pos) {
            return '<div class="test-opt" data-k="' + k + '"><span class="k">' + 'ABCD'[pos] + '.</span><span>' + esc(item.o[k]) + '</span></div>';
        }).join('');
        rootEl.innerHTML =
            '<div class="test-topbar"><h2>📝 Question ' + (run.i + 1) + ' / ' + n + '</h2><button class="test-btn ghost" data-act="quit">End test</button></div>' +
            '<div class="test-progress"><div style="width:' + (run.i / n * 100) + '%"></div></div>' +
            '<div class="test-card"><div class="test-meta"><span class="test-tag">Module ' + item.m + ': ' + esc(MODULES[item.m - 1]) + '</span><span>' + (item.src === 'assignment' ? 'Assignment' : 'Lecture practice') + '</span></div>' +
            '<div class="test-q">' + esc(item.q) + '</div>' + opts +
            '<div class="test-exp" id="t-exp"><strong>Explanation:</strong> ' + esc(item.e || 'See the module notes.') + '</div></div>' +
            '<div class="test-row"><button class="test-btn" data-act="next" id="t-next" style="display:none">' + (run.i === n - 1 ? 'Finish' : 'Next →') + '</button></div>';
        typeset();
    }

    function pickOpt(el) {
        if (run.answered) return;
        run.answered = true;
        var item = run.qs[run.i], k = +el.getAttribute('data-k');
        run.ans[run.i] = k;
        rootEl.querySelectorAll('.test-opt').forEach(function (o) {
            o.classList.add('locked');
            if (+o.getAttribute('data-k') === item.a) o.classList.add('correct');
        });
        if (k !== item.a) el.classList.add('wrong');
        document.getElementById('t-exp').style.display = 'block';
        document.getElementById('t-next').style.display = '';
        typeset();
    }

    function renderResult() {
        var n = run.qs.length, ok = 0, byMod = {};
        run.qs.forEach(function (q, i) {
            var r = run.ans[i] === q.a;
            if (r) ok++;
            var b = byMod[q.m] || (byMod[q.m] = { t: 0, c: 0 });
            b.t++; if (r) b.c++;
        });
        var pct = n ? Math.round(ok / n * 100) : 0;
        var bars = Object.keys(byMod).sort(function (a, b) { return a - b; }).map(function (m) {
            var b = byMod[m], p = Math.round(b.c / b.t * 100);
            return '<div class="test-bar"><div>M' + m + ': ' + esc(MODULES[m - 1]) + '<div class="track"><div class="fill" style="width:' + p + '%"></div></div></div><div>' + b.c + '/' + b.t + '</div></div>';
        }).join('');
        var wrong = run.qs.map(function (q, i) { return { q: q, i: i }; }).filter(function (x) { return run.ans[x.i] !== x.q.a; });
        var review = wrong.map(function (x) {
            var yours = run.ans[x.i] === undefined ? '<em>skipped</em>' : esc(x.q.o[run.ans[x.i]]);
            return '<div class="test-review-item"><div class="test-q" style="font-size:.95rem">' + esc(x.q.q) + '</div>' +
                '<div>Your answer: ' + yours + '</div><div style="color:#4CAF50">Correct: ' + esc(x.q.o[x.q.a]) + '</div>' +
                '<div style="color:var(--text-muted);margin-top:.3rem">' + esc(x.q.e || '') + '</div></div>';
        }).join('');
        rootEl.innerHTML =
            '<div class="test-topbar"><h2>Results</h2><button class="test-btn ghost" data-act="close">✕ Close</button></div>' +
            '<div class="test-card"><div class="test-score">' + ok + ' / ' + n + ' <span style="font-size:1.2rem">(' + pct + '%)</span></div>' + bars + '</div>' +
            '<div class="test-row" style="margin-bottom:1rem"><button class="test-btn" data-act="setup">New test</button>' +
            (wrong.length ? '<button class="test-btn ghost" data-act="retry">Retry ' + wrong.length + ' missed</button>' : '') + '</div>' +
            (wrong.length ? '<div class="test-card"><h3>Review missed questions</h3>' + review + '</div>' : '<div class="test-card">Perfect score 🎉</div>');
        typeset();
    }

    rootEl.addEventListener('change', function (e) {
        var t = e.target;
        if (t.name === 'scope') cfg.scope = t.value;
        else if (t.name === 'src') cfg.src = t.value;
        else if (t.hasAttribute('data-mod')) {
            var m = +t.getAttribute('data-mod'), i = cfg.mods.indexOf(m);
            if (t.checked && i < 0) cfg.mods.push(m); else if (!t.checked && i >= 0) cfg.mods.splice(i, 1);
        }
        else if (t.id === 't-count') cfg.count = +t.value;
        else if (t.id === 't-shuffle') cfg.shuffle = t.checked;
        else return;
        renderSetup();
    });
    rootEl.addEventListener('click', function (e) {
        var opt = e.target.closest('.test-opt');
        if (opt) return pickOpt(opt);
        var b = e.target.closest('[data-act]');
        if (!b) return;
        var act = b.getAttribute('data-act');
        if (act === 'close') close();
        else if (act === 'setup') renderSetup();
        else if (act === 'start') {
            var qs = cfg.shuffle ? shuffle(pool()) : pool();
            if (cfg.count) qs = qs.slice(0, cfg.count);
            startRun(qs);
        }
        else if (act === 'next') { run.i++; run.i >= run.qs.length ? renderResult() : renderQ(); }
        else if (act === 'quit') { run.qs = run.qs.slice(0, run.i + (run.answered ? 1 : 0)); run.qs.length ? renderResult() : renderSetup(); }
        else if (act === 'retry') {
            startRun(run.qs.filter(function (q, i) { return run.ans[i] !== q.a; }));
        }
    });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && overlay.classList.contains('open')) close();
    });
    var openBtn = document.getElementById('open-test-btn');
    if (openBtn) openBtn.addEventListener('click', open);
    var tabBtn = document.getElementById('tab-test');
    if (tabBtn) tabBtn.addEventListener('click', open);
    if (location.hash === '#test') {
        history.replaceState(null, '', location.pathname + location.search);
        open();
    }
})();
