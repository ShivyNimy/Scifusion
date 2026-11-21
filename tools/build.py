#!/usr/bin/env python3
"""Scifusion static-site generator.

Turns the Python curriculum data in ``tools/data`` into:

* ``docs/``            - a browsable, searchable, offline-friendly website
* ``books/``           - one Markdown book per subject
* ``build/stats.json`` - counts used by the README and CI

Usage::

    python3 tools/build.py            # build everything
    python3 tools/build.py --check    # validate content only (no writes)
"""

from __future__ import annotations

import argparse
import html
import importlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.curriculum import CLASSES, SUBJECTS, ALL_SUBJECT_CODES  # noqa: E402

DOCS = ROOT / "docs"
BOOKS = ROOT / "books"
BUILD = ROOT / "build"
SITE_NAME = "Scifusion"


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------
def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return re.sub(r"-{2,}", "-", text)


def esc(text: str) -> str:
    return html.escape(str(text), quote=False)


_SUB = re.compile(r"(?<!\\)~([^~]+)(?<!\\)~")
_SUP = re.compile(r"(?<!\\)\^([^^]+)(?<!\\)\^")


def fmt(text: str) -> str:
    """Convert inline mini-markup to HTML (input is plain text)."""
    out = esc(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", out)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = _SUB.sub(r"<sub>\1</sub>", out)
    out = _SUP.sub(r"<sup>\1</sup>", out)
    return out


def plain(text: str) -> str:
    """Strip inline mini-markup for plain-text contexts (search, JSON)."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", str(text))
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"~(.*?)~", r"\1", text)
    text = re.sub(r"\^(.*?)\^", r"\1", text)
    return text


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # F-string templates leave indentation on intentionally blank lines. Keep
    # generated output tidy and make `git diff --check` useful for contributors.
    has_final_newline = text.endswith("\n")
    text = "\n".join(line.rstrip() for line in text.splitlines())
    if has_final_newline:
        text += "\n"
    path.write_text(text, encoding="utf-8")


def load_subjects():
    subjects = []
    for code in ALL_SUBJECT_CODES:
        modname = "tools.data." + code.replace("-", "_")
        mod = importlib.import_module(modname)
        data = getattr(mod, "SUBJECT_DATA")
        data["code"] = code
        # normalise chapter/topic slugs
        for ch in data["chapters"]:
            ch["slug"] = "chapter-%02d-%s" % (ch["number"], slugify(ch["name"]))
            for i, topic in enumerate(ch["topics"], 1):
                topic["slug"] = slugify(topic["name"])
                topic["num"] = "%d.%d" % (ch["number"], i)
        subjects.append(data)
    return subjects


# --------------------------------------------------------------------------
# validation
# --------------------------------------------------------------------------
class ContentError(Exception):
    pass


def validate(subjects):
    errors = []
    total_q = 0
    for sub in subjects:
        seen_ch = set()
        for ch in sub["chapters"]:
            if ch["slug"] in seen_ch:
                errors.append(f"{sub['code']}: duplicate chapter slug {ch['slug']}")
            seen_ch.add(ch["slug"])
            seen_t = set()
            if not ch["topics"]:
                errors.append(f"{sub['code']} ch{ch['number']}: no topics")
            for t in ch["topics"]:
                where = f"{sub['code']} ch{ch['number']} '{t['name']}'"
                if t["slug"] in seen_t:
                    errors.append(f"{where}: duplicate topic slug")
                seen_t.add(t["slug"])
                if len(t["examples"]) < 2:
                    errors.append(f"{where}: needs at least 2 examples")
                if len(t["questions"]) < 3:
                    errors.append(f"{where}: needs at least 3 practice questions")
                if len(t["key_points"]) < 3:
                    errors.append(f"{where}: needs at least 3 key points")
                if not t["summary"].strip():
                    errors.append(f"{where}: empty summary")
                for q in t["questions"]:
                    total_q += 1
                    if q["type"] == "mcq":
                        opts = q["options"]
                        if not (2 <= len(opts) <= 6):
                            errors.append(f"{where}: MCQ needs 2-6 options")
                        if not isinstance(q["answer"], int) or not 0 <= q["answer"] < len(opts):
                            errors.append(f"{where}: MCQ answer index out of range")
                        if len(set(o.lower() for o in opts)) != len(opts):
                            errors.append(f"{where}: duplicate MCQ options")
                    if not q.get("q"):
                        errors.append(f"{where}: empty question")
                    if not q.get("solution"):
                        errors.append(f"{where}: question without solution")
    if errors:
        raise ContentError("\n".join(errors))
    stats = summarise(subjects)
    print("Validated OK:", stats["topics"], "topics,", total_q, "questions")
    return stats


def summarise(subjects):
    chapters = topics = examples = questions = mcqs = keypoints = 0
    for sub in subjects:
        chapters += len(sub["chapters"])
        for ch in sub["chapters"]:
            topics += len(ch["topics"])
            for t in ch["topics"]:
                examples += len(t["examples"])
                keypoints += len(t["key_points"])
                questions += len(t["questions"])
                mcqs += sum(1 for q in t["questions"] if q["type"] == "mcq")
    return {
        "chapters": chapters,
        "topics": topics,
        "examples": examples,
        "questions": questions,
        "mcqs": mcqs,
        "key_points": keypoints,
    }


# --------------------------------------------------------------------------
# HTML shell
# --------------------------------------------------------------------------
def page(prefix, title, body, extra_head="", body_class="", description=""):
    desc = esc(description or "Free science notes, worked examples and practice questions for Classes 6 to 12.")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} &middot; {SITE_NAME}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/style.css">
{extra_head}
</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{prefix}index.html">
      <span class="logo">&#9883;</span>
      <span class="brand-text"><strong>{SITE_NAME}</strong><small>Science, fused into clarity</small></span>
    </a>
    <nav class="top-nav" aria-label="Main">
      <a href="{prefix}index.html">Home</a>
      <a href="{prefix}#classes">Classes</a>
      <a href="{prefix}search.html">Search</a>
      <a href="{prefix}about.html">About</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-inner">
    <p><strong>{SITE_NAME}</strong> &middot; Science notes for Classes 6&ndash;12 &middot; built from open, hand-written curriculum data.</p>
    <p class="muted">Content follows the NCERT/CBSE science themes and is equally useful for ICSE and state boards. Found a mistake? Open an issue.</p>
  </div>
</footer>
<script src="{prefix}assets/app.js" defer></script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# components
# --------------------------------------------------------------------------
def breadcrumb(prefix, items):
    parts = []
    for name, href in items:
        if href:
            parts.append(f'<a href="{prefix}{href}">{esc(name)}</a>')
        else:
            parts.append(f"<span aria-current=\"page\">{esc(name)}</span>")
    return '<nav class="crumb" aria-label="Breadcrumb">' + " <span>/</span> ".join(parts) + "</nav>"


def examples_html(topic):
    out = ['<div class="examples">']
    for i, ex in enumerate(topic["examples"], 1):
        out.append(
            f'<article class="example"><h4><span class="ex-num">Example {i}</span> {fmt(ex["title"])}</h4>'
            f"<p>{fmt(ex['text'])}</p></article>"
        )
    out.append("</div>")
    return "\n".join(out)


def question_html(i, q):
    if q["type"] == "mcq":
        opts = "".join(f'<span class="opt">{chr(65 + j)}. {fmt(o)}</span>' for j, o in enumerate(q["options"]))
        label = "MCQ"
    else:
        opts = ""
        label = "Short answer"
    return f"""<li class="q" data-type="{q['type']}">
  <div class="q-head"><span class="pill">{label}</span> <span class="q-text">{fmt(q['q'])}</span></div>
  {f'<div class="options">{opts}</div>' if opts else ''}
  <details class="answer"><summary>Show answer</summary>
    <div class="answer-body">
      {'<p class="correct"><strong>Answer:</strong> ' + fmt(q['options'][q['answer']]) + '</p>' if q['type'] == 'mcq' else ''}
      <p>{fmt(q['solution'])}</p>
    </div>
  </details>
</li>"""


def practice_html(topic, start=1):
    items = "\n".join(question_html(i, q) for i, q in enumerate(topic["questions"], start))
    return f'<ol class="questions" start="{start}">{items}</ol>'


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------
def build_home(subjects, stats):
    cards = []
    for key, label in CLASSES:
        subs = [s for s in subjects if s["class_key"] == key]
        links = "".join(
            f'<a class="subject-chip" href="class-{key}/{s["code"]}/index.html">{esc(s["title"])}'
            f'<span>{len(s["chapters"])} ch</span></a>'
            for s in subs
        )
        n_topics = sum(len(t["topics"]) for s in subs for t in s["chapters"])
        cards.append(f"""<article class="class-card">
  <div class="class-top"><span class="class-num">{esc(label)}</span><span class="muted">{n_topics} topics</span></div>
  <div class="subject-chips">{links}</div>
</article>""")

    body = f"""
<section class="hero">
  <div class="wrap">
    <h1>Every science topic, <span class="grad">one clear place</span>.</h1>
    <p class="lead">Class 6 to 12 &middot; Biology, Chemistry &amp; Physics &middot; {stats['topics']} topics,
    {stats['examples']} worked examples and {stats['questions']} practice questions, all free and open.</p>
    <form class="search-form" action="search.html" method="get" role="search">
      <label class="sr-only" for="home-q">Search topics</label>
      <input id="home-q" name="q" type="search" placeholder="Try &ldquo;photosynthesis&rdquo;, &ldquo;Ohm&rsquo;s law&rdquo;, &ldquo;mole concept&rdquo;&hellip;" autocomplete="off">
      <button type="submit">Search</button>
    </form>
    <div class="stat-row">
      <div><strong>{stats['chapters']}</strong><span>chapters</span></div>
      <div><strong>{stats['topics']}</strong><span>topics</span></div>
      <div><strong>{stats['examples']}</strong><span>worked examples</span></div>
      <div><strong>{stats['questions']}</strong><span>practice questions</span></div>
    </div>
  </div>
</section>

<section class="wrap section" id="classes">
  <h2>Choose your class</h2>
  <div class="class-grid">{''.join(cards)}</div>
</section>

<section class="wrap section how">
  <h2>How to use Scifusion</h2>
  <ol class="steps">
    <li><strong>Read the topic.</strong> A tight summary, the key points you must remember, and the vocabulary.</li>
    <li><strong>Study the examples.</strong> Every topic ships with at least two worked examples &mdash; not just answers.</li>
    <li><strong>Practise.</strong> MCQs with instant explanations plus short-answer questions to write out.</li>
    <li><strong>Test yourself.</strong> Each subject has a randomised quiz built from every chapter.</li>
  </ol>
</section>
"""
    write(DOCS / "index.html", page("", "Home", body))


def build_class_pages(subjects, stats):
    for key, label in CLASSES:
        subs = [s for s in subjects if s["class_key"] == key]
        prefix = "../"
        cards = []
        for s in subs:
            n_topics = sum(len(t["topics"]) for t in s["chapters"])
            n_q = sum(len(t["questions"]) for t in s["chapters"] for t in t["topics"])
            chaps = "".join(
                f'<li><a href="{s["code"]}/{ch["slug"]}/index.html">{ch["number"]}. {esc(ch["name"])}</a>'
                f'<span class="muted">{len(ch["topics"])} topics</span></li>'
                for ch in s["chapters"]
            )
            cards.append(f"""<article class="subject-card">
  <h2><a href="{s["code"]}/index.html">{esc(s["title"])}</a></h2>
  <p class="muted">{esc(s['book'])} &middot; {len(s['chapters'])} chapters &middot; {n_topics} topics &middot; {n_q} questions</p>
  <ol class="chapter-list">{chaps}</ol>
</article>""")
        body = f"""<div class="wrap">
{breadcrumb(prefix, [(SITE_NAME, 'index.html'), (label, None)])}
<div class="page-head"><h1>{esc(label)} Science</h1>
<p class="lead">Complete chapter and topic list for {esc(label)}.</p></div>
<div class="subject-grid">{''.join(cards)}</div>
</div>"""
        write(DOCS / f"class-{key}" / "index.html", page(prefix, label, body, description=f"Science topics, notes, examples and practice questions for {label}."))


def build_subject_page(sub, stats):
    key = sub["class_key"]
    outdir = DOCS / f"class-{key}" / sub["code"]
    prefix = "../../"
    chapters = []
    n_q = 0
    for ch in sub["chapters"]:
        topics = "".join(
            f'<li><a href="{ch["slug"]}/{t["slug"]}/index.html">{t["num"]} {esc(t["name"])}</a></li>'
            for t in ch["topics"]
        )
        ch_q = sum(len(t["questions"]) for t in ch["topics"])
        n_q += ch_q
        chapters.append(f"""<article class="chapter-row">
  <div class="chapter-row-main">
    <h2><a href="{ch['slug']}/index.html">{ch['number']}. {esc(ch['name'])}</a></h2>
    <p class="muted">{len(ch['topics'])} topics &middot; {sum(len(t['examples']) for t in ch['topics'])} examples &middot; {ch_q} questions</p>
  </div>
  <ul class="topic-mini">{topics}</ul>
</article>""")
    n_topics = sum(len(c["topics"]) for c in sub["chapters"])
    body = f"""<div class="wrap">
{breadcrumb(prefix, [(SITE_NAME, 'index.html'), ("Class " + key, f"class-{key}/index.html"), (sub['title'], None)])}
<div class="page-head">
  <p class="eyebrow">Class {key} &middot; {esc(sub['book'])}</p>
  <h1>{esc(sub['title'])}</h1>
  <p class="lead">{fmt(sub['intro'])}</p>
  <div class="actions">
    <a class="btn" href="quiz.html">Take the full-subject quiz &rarr;</a>
    <a class="btn ghost" href="print.html">Print all notes</a>
  </div>
  <p class="muted small">{len(sub['chapters'])} chapters &middot; {n_topics} topics &middot; {n_q} practice questions</p>
</div>
<div class="chapters">{''.join(chapters)}</div>
</div>"""
    write(outdir / "index.html", page(prefix, f"Class {key} {sub['title']}", body,
                                     description=f"Class {key} {sub['title']}: {n_topics} topics with examples and practice questions."))


def build_chapter_page(sub, ch):
    key = sub["class_key"]
    outdir = DOCS / f"class-{key}" / sub["code"] / ch["slug"]
    prefix = "../../../"
    cards = []
    for t in ch["topics"]:
        cards.append(f"""<article class="topic-card">
  <p class="topic-num">Topic {t['num']}</p>
  <h2><a href="{t['slug']}/index.html">{esc(t['name'])}</a></h2>
  <p>{fmt(t['summary'])}</p>
  <p class="muted small">{len(t['examples'])} worked examples &middot; {len(t['questions'])} practice questions</p>
  <a class="more" href="{t['slug']}/index.html">Study this topic &rarr;</a>
</article>""")
    body = f"""<div class="wrap">
{breadcrumb(prefix, [(SITE_NAME, 'index.html'), ("Class " + key, f"class-{key}/index.html"),
                     (sub['title'], f"class-{key}/{sub['code']}/index.html"), (ch['name'], None)])}
<div class="page-head">
  <p class="eyebrow">Class {key} {esc(sub['title'])} &middot; Chapter {ch['number']}</p>
  <h1>{esc(ch['name'])}</h1>
  {f'<p class="lead">{fmt(ch["intro"])}</p>' if ch.get('intro') else ''}
  <div class="actions"><a class="btn" href="quiz.html">Quiz on this chapter</a>
    <a class="btn ghost" href="../quiz.html">Full-subject quiz</a></div>
</div>
<div class="topic-grid">{''.join(cards)}</div>
</div>"""
    write(outdir / "index.html", page(prefix, f"{ch['number']}. {ch['name']}", body,
                                     description=f"{ch['name']} - Class {key} {sub['title']} notes, examples and practice questions."))

    quiz_body = f"""<div class="wrap">
{breadcrumb(prefix, [(SITE_NAME, 'index.html'), ("Class " + key, f"class-{key}/index.html"),
                     (sub['title'], f"class-{key}/{sub['code']}/index.html"),
                     (ch['name'], f"class-{key}/{sub['code']}/{ch['slug']}/index.html"), ('Quiz', None)])}
<div class="page-head"><h1>{esc(ch['name'])} &mdash; quick quiz</h1>
<p class="lead">Ten questions from this chapter only. MCQs are marked instantly; short answers have model answers.</p></div>
<div class="quiz" id="quiz" data-src="../quiz.json" data-chapter="{esc(ch['name'])}">
  <div class="quiz-bar"><span id="quiz-progress">Loading&hellip;</span><button class="btn ghost" id="quiz-restart">New set</button></div>
  <div id="quiz-body"></div>
  <div class="quiz-actions"><button class="btn" id="quiz-submit">Check answers</button></div>
  <div id="quiz-result" class="quiz-result" hidden></div>
</div>
</div>"""
    write(outdir / "quiz.html", page(prefix, f"{ch['name']} quiz", quiz_body, body_class="quiz-page"))


def build_topic_page(sub, ch, topic, prev, nxt):
    key = sub["class_key"]
    outdir = DOCS / f"class-{key}" / sub["code"] / ch["slug"] / topic["slug"]
    prefix = "../../../../"
    kps = "".join(f"<li>{fmt(k)}</li>" for k in topic["key_points"])
    formulas = ""
    if topic["formulas"]:
        fl = "".join(f'<div class="formula">{fmt(f)}</div>' for f in topic["formulas"])
        formulas = f'<section class="block"><h3>Key formulas</h3><div class="formulas">{fl}</div></section>'
    terms = ""
    if topic["terms"]:
        dl = "".join(f"<dt>{fmt(term)}</dt><dd>{fmt(desc)}</dd>" for term, desc in topic["terms"])
        terms = f'<section class="block"><h3>Key terms</h3><dl class="terms">{dl}</dl></section>'

    nav = []
    if prev:
        nav.append(f'<a class="pager prev" href="{prev[0]}"><span>Previous</span>{esc(prev[1])}</a>')
    if nxt:
        nav.append(f'<a class="pager next" href="{nxt[0]}"><span>Next</span>{esc(nxt[1])}</a>')
    pager = f'<nav class="pager-nav" aria-label="Topic navigation">{"".join(nav)}</nav>' if nav else ""

    body = f"""<div class="wrap">
{breadcrumb(prefix, [(SITE_NAME, 'index.html'), ("Class " + key, f"class-{key}/index.html"),
                     (sub['title'], f"class-{key}/{sub['code']}/index.html"),
                     (ch['name'], f"class-{key}/{sub['code']}/{ch['slug']}/index.html"), (topic['name'], None)])}
<article class="topic">
  <header class="topic-head">
    <p class="eyebrow">Class {key} {esc(sub['title'])} &middot; Chapter {ch['number']} &middot; Topic {topic['num']}</p>
    <h1>{esc(topic['name'])}</h1>
    <p class="lead">{fmt(topic['summary'])}</p>
    <p class="muted small">{len(topic['examples'])} worked examples &middot; {len(topic['questions'])} practice questions</p>
  </header>

  <section class="block">
    <h2>Key points</h2>
    <ul class="keypoints">{kps}</ul>
  </section>

  <section class="block">
    <h2>Worked examples</h2>
    {examples_html(topic)}
  </section>
  {formulas}
  {terms}

  <section class="block practice">
    <h2>Practice questions</h2>
    <p class="muted small">Try each question before opening the answer.</p>
    {practice_html(topic)}
  </section>

  {pager}
</article>
</div>"""
    write(outdir / "index.html", page(prefix, topic["name"], body,
                                     description=topic["summary"][:160],
                                     body_class="topic-page"))


def build_quiz_pages(sub, all_subjects):
    key = sub["class_key"]
    outdir = DOCS / f"class-{key}" / sub["code"]
    prefix = "../../"
    for name, title, pool in (
        ("quiz.html", "Quiz", "subject"),
        ("print.html", "Printable notes", "print"),
    ):
        if pool == "print":
            continue
        body = f"""<div class="wrap">
{breadcrumb(prefix, [(SITE_NAME, 'index.html'), ('Class ' + key, f'class-{key}/index.html'),
                     (sub['title'], f"class-{key}/{sub['code']}/index.html"), ('Quiz', None)])}
<div class="page-head"><h1>{esc(sub['title'])} quiz</h1>
<p class="lead">Ten random questions drawn from all {len(sub['chapters'])} chapters. MCQs are marked instantly; short answers can be revealed after you write yours.</p></div>
<div class="quiz" id="quiz" data-src="quiz.json" data-scope="subject">
  <div class="quiz-bar"><span id="quiz-progress">Loading&hellip;</span><button class="btn ghost" id="quiz-restart">New set</button></div>
  <div id="quiz-body"></div>
  <div class="quiz-actions"><button class="btn" id="quiz-submit">Check answers</button></div>
  <div id="quiz-result" class="quiz-result" hidden></div>
</div>
</div>"""
        write(outdir / name, page(prefix, f"{sub['title']} quiz", body, body_class="quiz-page"))

    # print page: every chapter, notes and answers, no JS needed
    sections = []
    for ch in sub["chapters"]:
        for t in ch["topics"]:
            kps = "".join(f"<li>{fmt(k)}</li>" for k in t["key_points"])
            exs = "".join(f"<p><strong>{fmt(e['title'])}.</strong> {fmt(e['text'])}</p>" for e in t["examples"])
            qs = "".join(
                f"<li><strong>Q.</strong> {fmt(q['q'])} <em>Ans.</em> "
                + (fmt(q["options"][q["answer"]]) + ". " if q["type"] == "mcq" else "")
                + fmt(q["solution"]) + "</li>"
                for q in t["questions"]
            )
            sections.append(f"""<section class="print-topic">
<h2>{t['num']} {esc(t['name'])}</h2>
<p>{fmt(t['summary'])}</p>
<h3>Key points</h3><ul>{kps}</ul>
<h3>Examples</h3>{exs}
<h3>Practice</h3><ol class="print-q">{qs}</ol>
</section>""")
    body = f"""<div class="wrap print-doc">
<p class="crumb"><a href="{prefix}index.html">{SITE_NAME}</a> / Class {key} {esc(sub['title'])} / Print</p>
<h1>Class {key} {esc(sub['title'])} &mdash; complete notes</h1>
<p class="muted">All {sum(len(c['topics']) for c in sub['chapters'])} topics, examples and answers. Use your browser's Print &rarr; Save as PDF.</p>
{''.join(sections)}
</div>"""
    write(outdir / "print.html", page(prefix, f"{sub['title']} complete notes", body, body_class="print-page"))


def build_quiz_json(subject):
    key = subject["class_key"]
    out = []
    for ch in subject["chapters"]:
        for t in ch["topics"]:
            for q in t["questions"]:
                item = {
                    "i": len(out),
                    "chapter": ch["name"],
                    "topic": t["name"],
                    "url": f"{ch['slug']}/{t['slug']}/index.html",
                    "type": q["type"],
                    "q": q["q"],
                    "solution": plain(q["solution"]),
                }
                if q["type"] == "mcq":
                    item["options"] = q["options"]
                    item["answer"] = q["answer"]
                out.append(item)
    path = DOCS / f"class-{key}" / subject["code"] / "quiz.json"
    write(path, json.dumps(out, ensure_ascii=False, separators=(",", ":")))


def build_search(subjects):
    entries = []
    for sub in subjects:
        for ch in sub["chapters"]:
            for t in ch["topics"]:
                entries.append({
                    "t": t["name"],
                    "s": sub["title"],
                    "c": f"Class {sub['class_key']} \u00b7 {ch['name']}",
                    "k": sub["class_key"],
                    "u": f"class-{sub['class_key']}/{sub['code']}/{ch['slug']}/{t['slug']}/index.html",
                    "x": plain(t["summary"] + " " + " ".join(t["key_points"]))[:400],
                })
    write(DOCS / "search.json", json.dumps(entries, ensure_ascii=False, separators=(",", ":")))

    body = f"""<div class="wrap">
<h1>Search</h1>
<form class="search-form" role="search" onsubmit="return false;">
  <label class="sr-only" for="q">Search topics</label>
  <input id="q" type="search" placeholder="Search all topics, terms and key points&hellip;" autocomplete="off">
</form>
<p class="muted small" id="search-count">Type to search.</p>
<ul class="search-results" id="results"></ul>
</div>"""
    write(DOCS / "search.html", page("", "Search", body))


def build_about(stats, subjects):
    body = f"""<div class="wrap">
<h1>About Scifusion</h1>
<p class="lead">Scifusion is a free, open science library for Classes 6 to 12. It covers
{stats['chapters']} chapters and {stats['topics']} topics with {stats['examples']} worked examples and
{stats['questions']} practice questions.</p>

<h2>What's inside</h2>
<ul>
  <li><strong>Every chapter</strong> of the NCERT/CBSE science syllabus for Classes 6&ndash;10, plus separate Physics, Chemistry and Biology books for Classes 11&ndash;12.</li>
  <li><strong>Topic pages</strong> with a summary, key points, key terms, formulas where relevant, and at least two worked examples.</li>
  <li><strong>Practice</strong> &mdash; MCQs with explanations and short-answer questions with model answers.</li>
  <li><strong>A randomised quiz</strong> for every subject, and printable notes for offline study.</li>
</ul>

<h2>How it is built</h2>
<p>All content is hand-written as plain Python data in <code>tools/data/</code>. A small generator
(<code>tools/build.py</code>) validates the data and produces this site in <code>docs/</code> plus
Markdown books in <code>books/</code>. There are no trackers, no accounts and no external CDNs
&mdash; the site works offline.</p>

<h2>Contributing</h2>
<ol>
  <li>Edit or add a subject file in <code>tools/data/</code> (copy an existing one as a template).</li>
  <li>Run <code>python3 tools/build.py</code> &mdash; it checks that every topic has at least two examples and three questions with answers.</li>
  <li>Commit both the data change and the regenerated site.</li>
</ol>

<h2>Coverage</h2>
<table class="coverage"><thead><tr><th>Class</th><th>Subject</th><th>Chapters</th><th>Topics</th><th>Questions</th></tr></thead><tbody>
{''.join(f"<tr><td>{s['class_key']}</td><td>{esc(s['title'])}</td><td>{len(s['chapters'])}</td><td>{sum(len(c['topics']) for c in s['chapters'])}</td><td>{sum(len(t['questions']) for c in s['chapters'] for t in c['topics'])}</td></tr>" for s in subjects)}
</tbody></table>
<p class="muted small">Scifusion is an independent study resource. It follows the themes of the NCERT/CBSE syllabus but is not an official NCERT publication.</p>
</div>"""
    write(DOCS / "about.html", page("", "About", body))


# --------------------------------------------------------------------------
# 404, assets
# --------------------------------------------------------------------------
CSS = """
:root{--bg:#f7f9fc;--card:#fff;--ink:#12181f;--muted:#5b6b7c;--line:#dfe6ee;--brand:#0b6bcb;--brand-2:#0aa88a;--accent:#7c3aed;--amber:#f59e0b;--radius:14px;--shadow:0 1px 2px rgba(16,24,40,.06),0 8px 24px rgba(16,24,40,.06)}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--card:#151b23;--ink:#e6edf3;--muted:#9aa8b6;--line:#26313d;--brand:#4ea1ff;--brand-2:#2dd4bf;--accent:#c084fc;--shadow:0 1px 2px rgba(0,0,0,.4)}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 "Inter",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--brand);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.sr-only,.skip{position:absolute;left:-9999px}.skip:focus{left:8px;top:8px;background:var(--card);padding:8px 12px;border-radius:8px;z-index:9}
.site-header{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.header-inner{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:64px}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink)}.brand:hover{text-decoration:none}
.logo{width:36px;height:36px;border-radius:10px;display:grid;place-items:center;background:linear-gradient(135deg,var(--brand),var(--brand-2));color:#fff;font-size:20px}
.brand-text{display:flex;flex-direction:column;line-height:1.15}.brand-text small{color:var(--muted);font-size:11.5px}
.top-nav{display:flex;gap:6px;flex-wrap:wrap}.top-nav a{padding:8px 12px;border-radius:999px;color:var(--muted);font-weight:500}.top-nav a:hover{background:var(--card);color:var(--ink);text-decoration:none}
main{min-height:70vh}
.hero{padding:64px 0 40px;background:radial-gradient(900px 380px at 20% -10%,color-mix(in srgb,var(--brand) 16%,transparent),transparent),radial-gradient(700px 300px at 90% 0%,color-mix(in srgb,var(--brand-2) 16%,transparent),transparent)}
.hero h1{font-size:clamp(30px,5vw,52px);line-height:1.1;letter-spacing:-.02em;margin:0 0 14px}
.grad{background:linear-gradient(90deg,var(--brand),var(--brand-2));-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{font-size:clamp(17px,2.2vw,20px);color:var(--muted);max-width:70ch}
.search-form{display:flex;gap:8px;max-width:640px;margin:22px 0 26px}
.search-form input{flex:1;padding:13px 16px;border-radius:12px;border:1px solid var(--line);background:var(--card);color:var(--ink);font-size:16px;box-shadow:var(--shadow)}
.search-form input:focus{outline:2px solid var(--brand);outline-offset:1px}
.search-form button{padding:0 22px;border-radius:12px;border:0;background:var(--brand);color:#fff;font-weight:600;font-size:15px;cursor:pointer}
.stat-row{display:flex;gap:28px;flex-wrap:wrap}.stat-row div{display:flex;flex-direction:column}.stat-row strong{font-size:26px}.stat-row span{color:var(--muted);font-size:13px}
.section{padding:40px 0}.section h2{font-size:24px;margin:0 0 18px;letter-spacing:-.01em}
.class-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}
.class-card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:18px;box-shadow:var(--shadow)}
.class-top{display:flex;align-items:baseline;justify-content:space-between;margin-bottom:12px}
.class-num{font-weight:700;font-size:17px}
.muted{color:var(--muted)}.small{font-size:13.5px}
.subject-chips{display:flex;flex-wrap:wrap;gap:8px}
.subject-chip{display:inline-flex;align-items:center;gap:6px;padding:7px 12px;border-radius:999px;background:color-mix(in srgb,var(--brand) 10%,transparent);color:var(--brand);font-weight:600;font-size:14px}
.subject-chip span{font-weight:500;font-size:11.5px;opacity:.8}
.steps{display:grid;gap:12px;padding-left:20px}
.crumb{font-size:13.5px;color:var(--muted);margin:22px 0 6px;display:flex;gap:6px;flex-wrap:wrap}
.page-head{padding:10px 0 26px;border-bottom:1px solid var(--line);margin-bottom:26px}
.page-head h1{font-size:clamp(26px,4vw,38px);margin:4px 0 8px;letter-spacing:-.02em}
.eyebrow{text-transform:uppercase;letter-spacing:.08em;font-size:12px;color:var(--brand);font-weight:700;margin:0}
.actions{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0 10px}
.btn{display:inline-block;padding:10px 16px;border-radius:10px;background:var(--brand);color:#fff;font-weight:600;border:0;cursor:pointer;font-size:14.5px}
.btn:hover{text-decoration:none;filter:brightness(1.07)}
.btn.ghost{background:transparent;color:var(--brand);border:1px solid color-mix(in srgb,var(--brand) 40%,transparent)}
.subject-grid{display:grid;gap:22px;padding-bottom:50px}
.subject-card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:22px;box-shadow:var(--shadow)}
.subject-card h2{margin:0 0 4px;font-size:22px}
.chapter-list{margin:14px 0 0;padding-left:20px;display:grid;gap:4px}.chapter-list li{display:flex;justify-content:space-between;gap:10px}.chapter-list .muted{font-size:12.5px;white-space:nowrap}
.chapters{display:grid;gap:16px;padding-bottom:50px}
.chapter-row{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px;display:grid;grid-template-columns:1fr 1.1fr;gap:18px;box-shadow:var(--shadow)}
@media(max-width:760px){.chapter-row{grid-template-columns:1fr}}
.chapter-row h2{margin:0 0 4px;font-size:20px}
.topic-mini{margin:0;padding-left:18px;display:grid;gap:4px;font-size:14.5px}
.topic-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;padding-bottom:50px}
.topic-card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px;box-shadow:var(--shadow);display:flex;flex-direction:column}
.topic-num{margin:0;font-size:12px;text-transform:uppercase;letter-spacing:.07em;color:var(--brand);font-weight:700}
.topic-card h2{margin:4px 0 8px;font-size:19px}
.topic-card p{margin:0 0 10px;font-size:14.5px;color:var(--muted)}
.topic-card .more{margin-top:auto;font-weight:600;font-size:14px}
.topic{padding-bottom:40px}
.topic-head h1{margin:6px 0 10px;font-size:clamp(28px,4.4vw,42px);letter-spacing:-.02em}
.block{margin:34px 0}
.block h2{font-size:22px;margin:0 0 14px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.block h3{font-size:17px;margin:0 0 10px}
.keypoints{margin:0;padding-left:22px;display:grid;gap:8px}
.keypoints li{padding-left:2px}
.examples{display:grid;gap:14px}
.example{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--brand-2);border-radius:12px;padding:16px 18px}
.example h4{margin:0 0 6px;font-size:16px}.example p{margin:0}
.ex-num{display:inline-block;background:color-mix(in srgb,var(--brand-2) 14%,transparent);color:var(--brand-2);font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;padding:2px 8px;border-radius:999px;margin-right:6px;vertical-align:1px}
.formulas{display:flex;flex-wrap:wrap;gap:10px}
.formula{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--card);border:1px solid var(--line);padding:10px 14px;border-radius:10px;font-size:15px}
.terms{display:grid;grid-template-columns:max-content 1fr;gap:8px 18px;margin:0;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px}
.terms dt{font-weight:650}.terms dd{margin:0;color:var(--muted)}
@media(max-width:600px){.terms{grid-template-columns:1fr}.terms dd{margin-bottom:8px}}
.questions{list-style:none;padding:0;margin:0;display:grid;gap:14px;counter-reset:q}
.q{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;counter-increment:q}
.q-head{display:flex;gap:10px;align-items:flex-start}
.q-head::before{content:"Q" counter(q);font-weight:800;color:var(--brand);flex:none}
.pill{flex:none;font-size:11px;text-transform:uppercase;letter-spacing:.05em;background:color-mix(in srgb,var(--accent) 14%,transparent);color:var(--accent);padding:2px 8px;border-radius:999px;font-weight:700;margin-top:2px}
.q-text{font-weight:550}
.options{display:grid;grid-template-columns:1fr 1fr;gap:6px 16px;margin:10px 0 0 34px;font-size:14.5px;color:var(--muted)}
@media(max-width:640px){.options{grid-template-columns:1fr}}
details.answer{margin:10px 0 0 34px;font-size:14.5px}
details.answer summary{cursor:pointer;color:var(--brand);font-weight:600;font-size:13.5px}
.answer-body{background:color-mix(in srgb,var(--brand) 6%,transparent);border-radius:10px;padding:10px 14px;margin-top:8px}
.answer-body p{margin:4px 0}.correct{color:var(--brand-2)}
.pager-nav{display:flex;justify-content:space-between;gap:14px;border-top:1px solid var(--line);padding-top:22px;margin-top:10px}
.pager{display:flex;flex-direction:column;padding:12px 16px;border:1px solid var(--line);border-radius:12px;background:var(--card);max-width:48%}
.pager span{font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.pager.next{margin-left:auto;text-align:right}
.quiz{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px;box-shadow:var(--shadow);margin-bottom:50px}
.quiz-bar{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:16px;font-weight:600}
.quiz .q{counter-increment:none;background:var(--bg)}
.quizzes .q-head::before{content:none}
.quiz .q-head::before{content:""}
.quiz-result{margin-top:16px;padding:16px;border-radius:12px;background:color-mix(in srgb,var(--brand-2) 12%,transparent);font-weight:600}
.quiz-actions{margin-top:16px}
.opt{display:block}
.choice{display:block;width:100%;text-align:left;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:10px;padding:9px 12px;margin:6px 0;cursor:pointer;font-size:14.5px}
.choice:hover{border-color:var(--brand)}
.choice.correct{border-color:var(--brand-2);background:color-mix(in srgb,var(--brand-2) 14%,transparent)}
.choice.wrong{border-color:#e5484d;background:color-mix(in srgb,#e5484d 12%,transparent)}
.search-results{list-style:none;padding:0;display:grid;gap:10px;margin-bottom:50px}
.search-results li{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.search-results h3{margin:0 0 2px;font-size:17px}.search-results p{margin:2px 0;font-size:14px;color:var(--muted)}
.footer-inner{border-top:1px solid var(--line);padding:26px 20px 40px;font-size:13.5px;color:var(--muted)}
.footer-inner p{margin:4px 0}
.coverage{border-collapse:collapse;width:100%;font-size:14.5px;margin:12px 0}
.coverage th,.coverage td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left}
.coverage th{font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
@media print{.site-header,.site-footer,.pager-nav,.actions,details.answer summary{display:none}body{background:#fff;color:#000}.wrap{max-width:none}details.answer[open],.answer-body{display:block}.print-topic{page-break-inside:avoid}}
sup,sub{font-size:.75em}
"""

JS = r"""
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
"""

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#0b6bcb"/><stop offset="1" stop-color="#0aa88a"/></linearGradient></defs><rect width="64" height="64" rx="14" fill="url(#g)"/><text x="32" y="45" font-family="Georgia,serif" font-size="36" fill="#fff" text-anchor="middle">&#9883;</text></svg>"""


NOT_FOUND = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found &middot; Scifusion</title>
<style>
body{margin:0;min-height:100vh;display:grid;place-items:center;background:#0d1117;color:#e6edf3;
font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;padding:24px}
.card{max-width:520px;text-align:center}
h1{font-size:64px;margin:0;background:linear-gradient(90deg,#4ea1ff,#2dd4bf);
-webkit-background-clip:text;background-clip:text;color:transparent}
p{color:#9aa8b6}a{color:#4ea1ff;font-weight:600;margin:0 8px}
</style></head><body><div class="card">
<h1>404</h1>
<p>That page does not exist &mdash; but the science does.</p>
<p><a id="home" href="#">All classes</a> <a id="search" href="#">Search topics</a></p>
</div><script>
// Work out the repository root (works for project pages and custom domains).
(function(){
  var p = location.pathname, i = p.indexOf("/docs/");
  var root;
  if (i > -1) { root = p.slice(0, i + 6); }
  else { var seg = p.split("/").filter(Boolean); root = "/" + (seg.length > 1 ? seg[0] + "/" : ""); }
  document.getElementById("home").href = root + "index.html";
  document.getElementById("search").href = root + "search.html";
})();
</script></body></html>"""


def build_assets():
    write(DOCS / "assets" / "style.css", CSS)
    write(DOCS / "assets" / "app.js", JS)
    write(DOCS / "assets" / "favicon.svg", FAVICON)
    write(DOCS / ".nojekyll", "")
    write(DOCS / "404.html", NOT_FOUND)


# --------------------------------------------------------------------------
# markdown books
# --------------------------------------------------------------------------
def md(text):
    """Mini-markup -> markdown/HTML that GitHub renders."""
    out = str(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"**\1**", out)
    out = re.sub(r"`([^`]+)`", r"`\1`", out)
    out = re.sub(r"~(.*?)~", r"<sub>\1</sub>", out)
    out = re.sub(r"\^(.*?)\^", r"<sup>\1</sup>", out)
    return out


def build_books(subjects):
    for sub in subjects:
        lines = [f"# Class {sub['class_key']} {sub['title']}", "",
                 f"> {sub['book']}", "", md(sub["intro"]), "",
                 f"**{len(sub['chapters'])} chapters \u00b7 "
                 f"{sum(len(c['topics']) for c in sub['chapters'])} topics \u00b7 "
                 f"{sum(len(t['questions']) for c in sub['chapters'] for t in c['topics'])} practice questions**",
                 "", "---", ""]
        for ch in sub["chapters"]:
            lines += [f"## Chapter {ch['number']}. {ch['name']}", ""]
            if ch.get("intro"):
                lines += [md(ch["intro"]), ""]
            for t in ch["topics"]:
                lines += [f"### {t['num']} {t['name']}", "", md(t["summary"]), "", "**Key points**", ""]
                lines += [f"- {md(k)}" for k in t["key_points"]]
                lines += ["", "**Worked examples**", ""]
                for i, ex in enumerate(t["examples"], 1):
                    lines += [f"{i}. **{md(ex['title'])}.** {md(ex['text'])}", ""]
                if t["formulas"]:
                    lines += ["**Formulas**", ""] + [f"- `{md(f)}`" for f in t["formulas"]] + [""]
                if t["terms"]:
                    lines += ["**Key terms**", ""] + [f"- **{md(term)}** \u2014 {md(desc)}" for term, desc in t["terms"]] + [""]
                lines += ["**Practice questions**", ""]
                for i, q in enumerate(t["questions"], 1):
                    if q["type"] == "mcq":
                        opts = " ".join(f"({chr(65 + j)}) {md(o)}" for j, o in enumerate(q["options"]))
                        lines += [f"{i}. {md(q['q'])} {opts}",
                                  f"   - *Answer:* {md(q['options'][q['answer']])}. {md(q['solution'])}"]
                    else:
                        lines += [f"{i}. {md(q['q'])}", f"   - *Answer:* {md(q['solution'])}"]
                lines += [""]
        write(BOOKS / f"{sub['code']}.md", "\n".join(lines))


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate content only")
    args = ap.parse_args()

    subjects = load_subjects()
    stats = validate(subjects)
    if args.check:
        return

    if DOCS.exists():
        import shutil
        shutil.rmtree(DOCS)
    build_assets()
    build_home(subjects, stats)
    build_class_pages(subjects, stats)
    for sub in subjects:
        build_subject_page(sub, stats)
        build_quiz_pages(sub, subjects)
        build_quiz_json(sub)
        for ch in sub["chapters"]:
            build_chapter_page(sub, ch)
            flat = [t for c in sub["chapters"] for t in c["topics"]]
            for idx, topic in enumerate(flat):
                if topic in ch["topics"]:
                    prev = flat[idx - 1] if idx > 0 else None
                    nxt = flat[idx + 1] if idx + 1 < len(flat) else None
                    prev_link = None
                    nxt_link = None
                    if prev:
                        pc = next(c for c in sub["chapters"] if prev in c["topics"])
                        prev_link = ("../" + prev["slug"] + "/index.html" if pc is ch
                                     else f"../../{pc['slug']}/{prev['slug']}/index.html", prev["name"])
                    if nxt:
                        nc = next(c for c in sub["chapters"] if nxt in c["topics"])
                        nxt_link = ("../" + nxt["slug"] + "/index.html" if nc is ch
                                    else f"../../{nc['slug']}/{nxt['slug']}/index.html", nxt["name"])
                    build_topic_page(sub, ch, topic, prev_link, nxt_link)
    build_search(subjects)
    build_about(stats, subjects)
    build_books(subjects)

    BUILD.mkdir(exist_ok=True)
    write(BUILD / "stats.json", json.dumps(stats, indent=2))
    print("Built docs/ and books/ ·", stats)


if __name__ == "__main__":
    main()
