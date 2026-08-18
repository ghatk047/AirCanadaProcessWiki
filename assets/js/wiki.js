/* ============================================================
   Air Canada Process Wiki - client behaviour
   Single clean implementation. Every page sets window.AC_ROOT
   (relative prefix to the site root) before loading this file.
   ============================================================ */
(function () {
  "use strict";

  var ROOT = window.AC_ROOT || "";          // relative prefix to the site root
  var BASE = ROOT + "assets/";              // relative prefix to /assets/
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  function store(k, v) {
    try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); }
    catch (e) { return null; }
  }

  /* ---------------- Theme ---------------- */
  function applyTheme(t) {
    document.documentElement.setAttribute("data-theme", t);
    var b = $("#theme-btn");
    if (b) {
      b.innerHTML = t === "dark"
        ? '☀️ <span class="lbl">Light</span>'
        : '\u{1F319} <span class="lbl">Dark</span>';
      b.setAttribute("aria-label", t === "dark" ? "Switch to light mode" : "Switch to dark mode");
    }
  }
  function initTheme() {
    var saved = store("ac-theme");
    if (!saved) {
      saved = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }
    applyTheme(saved);
    var b = $("#theme-btn");
    if (b) b.addEventListener("click", function () {
      var next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      store("ac-theme", next); applyTheme(next);
    });
  }

  /* ---------------- Reading progress ---------------- */
  function initProgress() {
    var bar = $("#progress-bar");
    if (!bar) return;
    function upd() {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var pct = h > 0 ? (window.scrollY / h) * 100 : 0;
      bar.style.width = Math.min(100, Math.max(0, pct)) + "%";
    }
    window.addEventListener("scroll", upd, { passive: true });
    window.addEventListener("resize", upd);
    upd();
  }

  /* ---------------- Back to top ---------------- */
  function initBackToTop() {
    var btn = $("#back-to-top");
    if (!btn) return;
    window.addEventListener("scroll", function () {
      btn.classList.toggle("show", window.scrollY > 300);
    }, { passive: true });
    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------------- Sidebar ----------------
     Collapses only on explicit toggle click. No mouseleave auto-collapse. */
  function initSidebar() {
    var t = $("#sb-toggle");
    if (store("ac-sidebar") === "collapsed") document.body.classList.add("sb-collapsed");
    if (t) t.addEventListener("click", function (e) {
      e.preventDefault(); e.stopPropagation();
      if (window.innerWidth <= 860) {
        document.body.classList.toggle("sb-open");
      } else {
        var c = document.body.classList.toggle("sb-collapsed");
        store("ac-sidebar", c ? "collapsed" : "open");
      }
    });
    var m = $("#mob-menu");
    if (m) m.addEventListener("click", function (e) {
      e.preventDefault(); document.body.classList.toggle("sb-open");
    });
    // Keep the active sidebar entry in view on load.
    var act = $(".sidebar .l3-link.active") || $(".sidebar .l2-link.active") || $(".sidebar .l1-link.active");
    if (act) { try { act.scrollIntoView({ block: "center" }); } catch (e) {} }
  }

  /* ---------------- Collapsible phase groups ---------------- */
  function initPhases() {
    $$(".phase-head").forEach(function (h) {
      h.addEventListener("click", function () {
        var g = h.closest(".phase-group");
        if (!g) return;
        g.classList.toggle("collapsed");
        var id = g.getAttribute("data-phase-id");
        if (id) store("ac-phase-" + id, g.classList.contains("collapsed") ? "1" : "0");
      });
    });
    $$(".phase-group").forEach(function (g) {
      var id = g.getAttribute("data-phase-id");
      if (id && store("ac-phase-" + id) === "1") g.classList.add("collapsed");
    });
  }

  /* ---------------- Copy PID ---------------- */
  function initCopyPid() {
    $$(".pid-badge").forEach(function (b) {
      b.addEventListener("click", function () {
        var pid = b.getAttribute("data-pid") || b.textContent.trim();
        var done = function () {
          var old = b.innerHTML;
          b.classList.add("copied");
          b.innerHTML = "✓ Copied";
          setTimeout(function () { b.classList.remove("copied"); b.innerHTML = old; }, 1300);
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(pid).then(done, done);
        } else {
          var ta = document.createElement("textarea");
          ta.value = pid; document.body.appendChild(ta); ta.select();
          try { document.execCommand("copy"); } catch (e) {}
          document.body.removeChild(ta); done();
        }
      });
    });
  }

  /* ---------------- Lightbox ---------------- */
  var LB = { scale: 1, x: 0, y: 0, drag: false, sx: 0, sy: 0 };
  function lbApply() {
    var img = $("#lb-img");
    if (!img) return;
    img.style.transform = "translate(" + LB.x + "px," + LB.y + "px) scale(" + LB.scale + ")";
    var lab = $("#lb-zoom-pct");
    if (lab) lab.textContent = Math.round(LB.scale * 100) + "%";
  }
  function lbZoom(f) { LB.scale = Math.min(8, Math.max(0.15, LB.scale * f)); lbApply(); }
  function lbReset() { LB.scale = 1; LB.x = 0; LB.y = 0; lbApply(); }
  function lbClose() {
    var lb = $("#lightbox");
    if (lb) { lb.classList.remove("open"); document.body.style.overflow = ""; }
  }
  function lbOpen(src, title) {
    var lb = $("#lightbox"), img = $("#lb-img"), t = $("#lb-title");
    if (!lb || !img) return;
    img.src = src;
    if (t) t.textContent = title || "";
    lbReset();
    lb.classList.add("open");
    document.body.style.overflow = "hidden";
  }
  function initLightbox() {
    // Trigger on .diagram-wrap img -- EA pages use the same class deliberately.
    $$(".diagram-wrap img").forEach(function (img) {
      img.addEventListener("click", function (e) {
        e.preventDefault(); e.stopPropagation();
        lbOpen(img.getAttribute("src"), img.getAttribute("alt") || "");
      });
    });
    var lb = $("#lightbox");
    if (!lb) return;

    lb.addEventListener("click", function (e) {
      if (e.target === lb || e.target.classList.contains("lb-stage")) { e.preventDefault(); lbClose(); }
    });
    var map = { "lb-in": function () { lbZoom(1.25); }, "lb-out": function () { lbZoom(0.8); },
                "lb-reset": lbReset, "lb-close": lbClose };
    Object.keys(map).forEach(function (id) {
      var b = document.getElementById(id);
      if (b) b.addEventListener("click", function (e) { e.preventDefault(); e.stopPropagation(); map[id](); });
    });
    var dl = $("#lb-open");
    if (dl) dl.addEventListener("click", function (e) {
      e.stopPropagation();
      var img = $("#lb-img");
      if (img && img.src) window.open(img.src, "_blank");
    });

    lb.addEventListener("wheel", function (e) {
      if (!lb.classList.contains("open")) return;
      e.preventDefault();
      lbZoom(e.deltaY < 0 ? 1.12 : 0.89);
    }, { passive: false });

    var img = $("#lb-img");
    if (img) {
      img.addEventListener("mousedown", function (e) {
        e.preventDefault(); LB.drag = true;
        LB.sx = e.clientX - LB.x; LB.sy = e.clientY - LB.y;
        img.classList.add("dragging");
      });
      window.addEventListener("mousemove", function (e) {
        if (!LB.drag) return;
        LB.x = e.clientX - LB.sx; LB.y = e.clientY - LB.sy; lbApply();
      });
      window.addEventListener("mouseup", function () {
        LB.drag = false; if (img) img.classList.remove("dragging");
      });
      img.addEventListener("dblclick", function (e) { e.preventDefault(); lbZoom(1.5); });
    }
  }

  /* ---------------- Search ----------------
     Index carries L1/L2/L3 names AND every L4 step name. */
  var IDX = null, IDX_LOADING = false;
  function loadIndex(cb) {
    if (IDX) { cb(IDX); return; }
    if (IDX_LOADING) { setTimeout(function () { loadIndex(cb); }, 120); return; }
    IDX_LOADING = true;
    fetch(BASE + "js/search-index.json")
      .then(function (r) { return r.json(); })
      .then(function (d) { IDX = d; IDX_LOADING = false; cb(IDX); })
      .catch(function () { IDX = { docs: [] }; IDX_LOADING = false; cb(IDX); });
  }

  function score(doc, q) {
    var n = (doc.n || "").toLowerCase(), p = (doc.p || "").toLowerCase();
    if (p === q) return 1000;
    if (n === q) return 900;
    if (p.indexOf(q) === 0) return 800;
    if (n.indexOf(q) === 0) return 700;
    var s = 0;
    if (n.indexOf(q) > -1) s = 500 - n.indexOf(q);
    else if (p.indexOf(q) > -1) s = 400;
    else if ((doc.s || "").toLowerCase().indexOf(q) > -1) s = 200;   // step names
    else if ((doc.y || "").toLowerCase().indexOf(q) > -1) s = 150;   // systems
    else return 0;
    if (doc.t === "process") s += 40;
    return s;
  }

  function renderResults(list, q) {
    var box = $("#search-results");
    if (!box) return;
    if (!q) { box.classList.remove("open"); box.innerHTML = ""; return; }
    if (!list.length) {
      box.innerHTML = '<div class="sr-empty">No match for &ldquo;' + esc(q) + '&rdquo;</div>';
      box.classList.add("open"); return;
    }
    var html = '<div class="sr-head">' + list.length + ' result' + (list.length === 1 ? "" : "s") + "</div>";
    list.forEach(function (d, i) {
      html += '<a class="sr-item' + (i === 0 ? " sel" : "") + '" href="' + ROOT + d.u + '">' +
              (d.p ? '<span class="sr-pid">' + esc(d.p) + "</span> " : "") +
              '<span class="sr-name">' + esc(d.n) + "</span>" +
              '<span class="sr-path">' + esc(d.c || "") + "</span></a>";
    });
    box.innerHTML = html;
    box.classList.add("open");
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function initSearch() {
    var inp = $("#search-input"), box = $("#search-results");
    if (!inp || !box) return;

    function position() {
      var r = inp.getBoundingClientRect();
      box.style.left = Math.max(8, Math.min(r.left, window.innerWidth - box.offsetWidth - 8)) + "px";
    }

    var timer = null;
    inp.addEventListener("input", function () {
      clearTimeout(timer);
      timer = setTimeout(function () {
        var q = inp.value.trim().toLowerCase();
        if (q.length < 2) { renderResults([], ""); return; }
        loadIndex(function (idx) {
          var hits = [];
          (idx.docs || []).forEach(function (d) {
            var s = score(d, q);
            if (s > 0) hits.push({ d: d, s: s });
          });
          hits.sort(function (a, b) { return b.s - a.s; });
          renderResults(hits.slice(0, 40).map(function (h) { return h.d; }), q);
          position();
        });
      }, 110);
    });

    inp.addEventListener("focus", function () { loadIndex(function () {}); });

    inp.addEventListener("keydown", function (e) {
      var items = $$(".sr-item", box);
      var cur = items.findIndex(function (i) { return i.classList.contains("sel"); });
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        if (!items.length) return;
        if (cur > -1) items[cur].classList.remove("sel");
        var next = e.key === "ArrowDown"
          ? (cur + 1) % items.length
          : (cur <= 0 ? items.length - 1 : cur - 1);
        items[next].classList.add("sel");
        items[next].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter") {
        e.preventDefault();
        var sel = cur > -1 ? items[cur] : items[0];
        if (sel) window.location.href = sel.getAttribute("href");
      } else if (e.key === "Escape") {
        inp.value = ""; renderResults([], ""); inp.blur();
      }
    });

    document.addEventListener("click", function (e) {
      if (!box.contains(e.target) && e.target !== inp) box.classList.remove("open");
    });
    window.addEventListener("resize", position);
  }

  /* ---------------- TOC scrollspy ---------------- */
  function initToc() {
    var links = $$(".toc a");
    if (!links.length) return;
    var targets = links.map(function (a) {
      return document.getElementById(a.getAttribute("href").slice(1));
    });
    function upd() {
      var best = 0, y = window.scrollY + 160;
      targets.forEach(function (t, i) { if (t && t.offsetTop <= y) best = i; });
      links.forEach(function (a, i) { a.classList.toggle("active", i === best); });
    }
    window.addEventListener("scroll", upd, { passive: true });
    upd();
  }

  /* ---------------- Keyboard navigation ---------------- */
  function closeAllOverlays() {
    lbClose();
    var kh = $("#kbd-help"); if (kh) kh.classList.remove("open");
    var sr = $("#search-results"); if (sr) sr.classList.remove("open");
    document.body.classList.remove("sb-open");
  }
  function navigateProcess(dir) {
    var nav = window.AC_NAV || {};
    var url = dir === "next" ? nav.next : nav.prev;
    if (url) window.location.href = url;
  }
  function initKeys() {
    document.addEventListener("keydown", function (e) {
      var tag = (e.target.tagName || "").toLowerCase();
      var typing = tag === "input" || tag === "textarea" || tag === "select" || e.target.isContentEditable;

      if (e.key === "Escape") { closeAllOverlays(); return; }

      // Lightbox-scoped keys
      var lb = $("#lightbox");
      if (lb && lb.classList.contains("open")) {
        if (e.key === "+" || e.key === "=") { e.preventDefault(); lbZoom(1.25); return; }
        if (e.key === "-" || e.key === "_") { e.preventDefault(); lbZoom(0.8); return; }
        if (e.key === "0") { e.preventDefault(); lbReset(); return; }
      }

      if (typing) return;
      if (e.metaKey || e.ctrlKey || e.altKey) return;

      if (e.key === "/") {
        e.preventDefault();
        var inp = $("#search-input");
        if (inp) { inp.focus(); inp.select(); }
      } else if (e.key === "j") { e.preventDefault(); navigateProcess("next"); }
      else if (e.key === "k") { e.preventDefault(); navigateProcess("prev"); }
      else if (e.key === "p") { e.preventDefault(); window.print(); }
      else if (e.key === "d") {
        e.preventDefault();
        var next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
        store("ac-theme", next); applyTheme(next);
      }
      else if (e.key === "?") {
        e.preventDefault();
        var kh = $("#kbd-help"); if (kh) kh.classList.toggle("open");
      }
      else if (e.key === "[") {
        e.preventDefault();
        var t = $("#sb-toggle"); if (t) t.click();
      }
    });
    var kh = $("#kbd-help");
    if (kh) kh.addEventListener("click", function (e) {
      if (e.target === kh) kh.classList.remove("open");
    });
  }

  /* ---------------- Boot ---------------- */
  function boot() {
    initTheme(); initProgress(); initBackToTop(); initSidebar();
    initPhases(); initCopyPid(); initLightbox(); initSearch(); initToc(); initKeys();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
