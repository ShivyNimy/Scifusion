# Scifusion

**Every science topic for Classes 6–12 — with worked examples and practice questions — in one free, open, searchable place.**

[![build](https://github.com/ShivyNimy/Scifusion/actions/workflows/build.yml/badge.svg)](https://github.com/ShivyNimy/Scifusion/actions/workflows/build.yml)
[![deploy](https://github.com/ShivyNimy/Scifusion/actions/workflows/pages.yml/badge.svg)](https://github.com/ShivyNimy/Scifusion/actions/workflows/pages.yml)

Scifusion turns the complete school science syllabus into structured study material: each topic has a plain-language
summary, the key points to remember, key vocabulary, formulas where relevant, **at least two worked examples**, and
**at least three practice questions with explained answers**.

## What's inside

| Class | Books | Chapters | Topics |
| --- | --- | --- | --- |
| 6 | Science | 16 | 32 |
| 7 | Science | 18 | 36 |
| 8 | Science | 18 | 36 |
| 9 | Science | 15 | 30 |
| 10 | Science | 14 | 28 |
| 11 | Physics · Chemistry · Biology | 14 · 14 · 22 | 28 · 28 · 44 |
| 12 | Physics · Chemistry · Biology | 14 · 14 · 13 | 28 · 28 · 26 |
| **Total** | **11 books** | **172** | **344** |

**688 worked examples · 1,032 practice questions (688 MCQs with explanations + 344 short-answer model answers)**

Every subject also gets a randomised quiz, and every chapter gets its own quick quiz.

## Browse at three levels

* **Website** (`docs/`) — a static site with dark mode, instant search, instant-marked quizzes, breadcrumbs,
  previous/next topic navigation and a print-friendly "complete notes" page per book.
* **Markdown books** (`books/`) — one self-contained file per subject, readable directly on GitHub.
* **Source data** (`tools/data/`) — the curriculum as tidy Python modules, easy to review, diff and extend.

## Publish with GitHub Pages

The repository includes a GitHub Actions deployment workflow (`.github/workflows/pages.yml`). After these changes are
merged into `main`, enable **Settings → Pages → Build and deployment → Source: GitHub Actions** in the repository.
The workflow then validates and deploys the generated `docs/` site on each push to `main`.

The site URL will be **https://shivynimy.github.io/Scifusion/** once Pages is enabled and the first deployment completes.

## Build it yourself

```bash
python3 tools/build.py            # regenerate docs/ and books/
python3 tools/build.py --check    # validate content only
python3 tools/serve.py            # local preview on http://localhost:8000 (binds 0.0.0.0)
```

No dependencies are needed beyond Python 3.8+. The generator:

1. imports every subject module from `tools/data/`,
2. **validates** the content (≥2 examples, ≥3 questions, valid MCQ answer indices, no duplicate slugs, non-empty
   answers),
3. renders 700+ HTML pages, the search index and the per-subject quiz JSON,
4. writes one Markdown book per subject,
5. reports totals in `build/stats.json`.

## Repository layout

```
tools/
  model.py            content helpers: T(), C(), E(), M(), S(), SUBJECT()
  curriculum.py       classes and subjects map
  build.py            validator + static-site generator
  serve.py            tiny local preview server
  data/               one module per book
    6_science.py  …  10_science.py
    11_physics.py 11_chemistry.py 11_biology.py
    12_physics.py 12_chemistry.py 12_biology.py
docs/                 generated website (GitHub Pages root)
books/                generated Markdown books
.github/workflows/    CI validation + Pages deployment
```

## Adding or editing content

```python
C(3, "Metals and Non-metals", [
    T("Reactivity Series",
      "One-line summary that becomes the page lead.",
      ["Key point one.", "Key point two.", "Key point three."],
      [E("Worked example title", "The reasoning, not just the answer."),
       E("Second example", "A second angle on the same idea.")],
      [M("Question?", "Correct|Distractor|Distractor|Distractor", 0, "Why the answer is right."),
       S("Short-answer question?", "Model answer.", "Optional longer explanation.")],
      terms=[("Term", "Definition")],
      formulas=["2H~2~ + O~2~ -> 2H~2~O"]),
])
```

Inline mini-markup works everywhere: `**bold**`, `*italic*`, `` `code` ``, `~subscript~`, `^superscript^`.

After editing, run `python3 tools/build.py` and commit both the data change **and** the regenerated `docs/` and
`books/` output. CI runs the validator on every push, so a broken topic fails the build instead of shipping.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full checklist.

## Design goals

* **Science-first.** No ads, accounts, trackers or CDNs; all runtime assets are served from this repository.
* **Exam-shaped practice.** Every question has an answer and an explanation, and MCQs are marked instantly.
* **Open and verifiable.** Content is plain data, validated on every build, so errors can be spotted and fixed in
  review.

## Notes

* Content follows the themes and chapter sequence of the NCERT/CBSE syllabus and is equally useful for ICSE and
  state boards. Scifusion is an independent study resource, not an official NCERT publication.
* The syllabus differs slightly by year. Where a chapter was removed from the current NCERT rationalised syllabus
  but remains widely taught (for example Class 10 "Management of Natural Resources"), it is kept and labelled.

## License

Content is released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) and code under the MIT
License. Use it, print it, translate it, teach from it — just keep the attribution.
