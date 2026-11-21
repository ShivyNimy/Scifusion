
(function () {
  "use strict";

  // ---------- search ----------
  var input = document.getElementById("q") || document.getElementById("home-q");
  var results = document.getElementById("results");
  if (results && input) {
    var cache = null;
    var count = document.getElementById("search-count");
    var load = function () {
      if (cache) return Promise.resolve(cache);
      return fetch("search.json").then(function (r) { return r.json(); }).then(function (d) { cache = d; return d; });
    };
    var params = new URLSearchParams(location.search);
    if (params.get("q")) input.value = params.get("q");
    var render = function (data) {
      var q = input.value.trim().toLowerCase();
      results.innerHTML = "";
      if (!q) { count.textContent = "Type to search " + data.length + " topics."; return; }
      var words = q.split(/\s+/);
      var hits = data.map(function (e) {
        var hay = (e.t + " " + e.x + " " + e.c).toLowerCase();
        var score = 0;
        words.forEach(function (w) {
          if (e.t.toLowerCase().indexOf(w) !== -1) score += 6;
          if (e.c.toLowerCase().indexOf(w) !== -1) score += 2;
          if (hay.indexOf(w) !== -1) score += 1;
        });
        return { e: e, score: score };
      }).filter(function (h) { return h.score > 0; }).sort(function (a, b) { return b.score - a.score; }).slice(0, 40);
      count.textContent = hits.length ? hits.length + " result" + (hits.length > 1 ? "s" : "") + " for \u201c" + input.value + "\u201d" : "No results. Try a simpler word.";
      hits.forEach(function (h) {
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = h.e.u;
        a.innerHTML = "<h3>" + h.e.t + "</h3>";
        var p = document.createElement("p");
        p.textContent = h.e.c;
        var s = document.createElement("p");
        s.textContent = h.e.x.slice(0, 170) + "\u2026";
        li.appendChild(a); li.appendChild(p); li.appendChild(s);
        results.appendChild(li);
      });
    };
    load().then(render);
    input.addEventListener("input", function () { load().then(render); });
  }

  // ---------- quiz ----------
  var quiz = document.getElementById("quiz");
  if (!quiz) return;
  var body = document.getElementById("quiz-body");
  var progress = document.getElementById("quiz-progress");
  var result = document.getElementById("quiz-result");
  var submit = document.getElementById("quiz-submit");
  var restart = document.getElementById("quiz-restart");
  var data = [];
  var current = [];
  var picked = {};

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  function pick(pool, n) {
    return shuffle(pool.slice()).slice(0, n);
  }
  function makeSet() {
    var mcq = pick(data.filter(function (q) { return q.type === "mcq"; }), 7);
    var short = pick(data.filter(function (q) { return q.type !== "mcq"; }), 3);
    if (mcq.length + short.length < 6) {
      mcq = pick(data.filter(function (q) { return q.type === "mcq"; }), 4);
      short = pick(data.filter(function (q) { return q.type !== "mcq"; }), 2);
    }
    return shuffle(mcq.concat(short));
  }
  function renderSet() {
    body.innerHTML = "";
    picked = {};
    result.hidden = true;
    current = makeSet();
    progress.textContent = current.length + " questions \u00b7 " +
      (quiz.dataset.chapter ? quiz.dataset.chapter : (quiz.dataset.scope === "subject" ? "whole subject" : "this chapter"));
    current.forEach(function (q, i) {
      var card = document.createElement("article");
      card.className = "q";
      var head = document.createElement("div");
      head.className = "q-head";
      var pill = document.createElement("span");
      pill.className = "pill";
      pill.textContent = q.type === "mcq" ? "MCQ" : "Short";
      var text = document.createElement("span");
      text.className = "q-text";
      text.textContent = (i + 1) + ". " + q.q;
      head.appendChild(pill); head.appendChild(text);
      card.appendChild(head);
      if (q.type === "mcq") {
        var wrap = document.createElement("div");
        q.options.forEach(function (opt, j) {
          var b = document.createElement("button");
          b.type = "button"; b.className = "choice"; b.textContent = String.fromCharCode(65 + j) + ". " + opt;
          b.addEventListener("click", function () {
            wrap.querySelectorAll(".choice").forEach(function (x) { x.className = "choice"; });
            b.classList.add(j === q.answer ? "correct" : "wrong");
            if (j !== q.answer) wrap.querySelectorAll(".choice")[q.answer].classList.add("correct");
            picked[i] = j;
          });
          wrap.appendChild(b);
        });
        card.appendChild(wrap);
      } else {
        var ta = document.createElement("textarea");
        ta.placeholder = "Write your answer, then open the model answer.";
        ta.rows = 2;
        ta.style.cssText = "width:100%;margin-top:8px;padding:10px;border-radius:10px;border:1px solid var(--line);background:var(--bg);color:var(--ink);font:inherit";
        card.appendChild(ta);
        var ans = document.createElement("details");
        ans.className = "answer";
        var sum = document.createElement("summary");
        sum.textContent = "Show model answer";
        var ab = document.createElement("div");
        ab.className = "answer-body";
        ab.textContent = q.solution;
        ans.appendChild(sum); ans.appendChild(ab);
        card.appendChild(ans);
      }
      var link = document.createElement("p");
      link.className = "muted small";
      link.style.margin = "10px 0 0";
      var a = document.createElement("a");
      a.href = q.url; a.textContent = q.topic;
      link.appendChild(document.createTextNode("From "));
      link.appendChild(a);
      link.appendChild(document.createTextNode(" \u00b7 " + q.chapter));
      card.appendChild(link);
      body.appendChild(card);
    });
  }
  fetch(quiz.dataset.src).then(function (r) { return r.json(); }).then(function (d) {
    data = d;
    if (quiz.dataset.chapter) {
      data = d.filter(function (q) { return q.chapter === quiz.dataset.chapter; });
    }
    if (!data.length) { progress.textContent = "No questions yet."; return; }
    renderSet();
  });
  if (restart) restart.addEventListener("click", renderSet);
  if (submit) submit.addEventListener("click", function () {
    var total = 0, correct = 0;
    body.querySelectorAll(".q").forEach(function (card, i) {
      var q = current[i];
      if (!q || q.type !== "mcq") return;
      total++;
      if (picked[i] === q.answer) correct++;
      var ex = card.querySelector(".answer");
      if (!ex) {
        ex = document.createElement("details");
        ex.className = "answer"; ex.open = true;
        var sm = document.createElement("summary");
        sm.textContent = "Explanation";
        var bd = document.createElement("div");
        bd.className = "answer-body";
        ex.appendChild(sm); ex.appendChild(bd);
        card.appendChild(ex);
      }
      card.querySelector(".answer-body").textContent =
        "Answer: " + q.options[q.answer] + ". " + q.solution;
    });
    result.hidden = false;
    result.textContent = "You scored " + correct + " / " + total + " on the MCQs. " +
      (correct === total ? "Perfect \u2014 try a new set." : "Review the topics marked above, then try a new set.");
    if (result.scrollIntoView) result.scrollIntoView({ behavior: "smooth", block: "center" });
  });
})();
