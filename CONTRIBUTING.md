# Contributing to Scifusion

Thanks for helping make school science clearer for everyone. There are two ways to contribute.

## 1. Fix or improve content

All content lives in `tools/data/`, one Python module per book:

```
6_science.py  7_science.py  8_science.py  9_science.py  10_science.py
11_physics.py 11_chemistry.py 11_biology.py
12_physics.py 12_chemistry.py 12_biology.py
```

A topic looks like this:

```python
T("Photosynthesis",
  "One-paragraph summary shown as the page lead.",
  ["Key point one.", "Key point two.", "Key point three."],
  [E("Example title", "The reasoning, worked out step by step."),
   E("Second example", "A different angle on the same idea.")],
  [M("Question?", "Right|Wrong|Wrong|Wrong", 0, "Why the right answer is right."),
   S("Short-answer question?", "Model answer.", "Optional longer explanation.")],
  terms=[("Chlorophyll", "The green pigment that captures light.")],
  formulas=["6CO~2~ + 6H~2~O -> C~6~H~12~O~6~ + 6O~2~"])
```

### Rules the build enforces

* every topic has ≥ 2 worked examples (`E`)
* every topic has ≥ 3 practice questions (`Q`), with a non-empty answer and explanation
* MCQ answers are a valid zero-based index into the options
* no duplicate chapter or topic names within a book
* every chapter has at least one topic

### Inline formatting

| Write | Renders as |
| --- | --- |
| `**text**` | **bold** |
| `*text*` | *italic* |
| `` `text` `` | `code` |
| `H~2~O` | H<sub>2</sub>O |
| `m/s^2^` | m/s² |

## 2. Improve the site or generator

The generator is `tools/build.py`. It renders `docs/` (the website, published with GitHub Pages) and `books/`
(the Markdown books). Keep it dependency-free: standard library only, so contributors can build with plain Python.

## Checklist before opening a pull request

```bash
python3 tools/build.py --check   # validate content
python3 tools/build.py           # regenerate docs/ and books/
python3 tools/check_links.py     # no broken internal links
git add tools/data docs books    # include the generated output
```

Commit the regenerated files together with your source change — CI fails if `docs/` or `books/` are stale.

## Writing style

* Plain language, short sentences, one idea per sentence.
* Explain *why*, not only *what* — examples should reason through the answer.
* Use SI units and correct symbols (`°C`, `m/s²`, `CO₂`, `H₂SO₄`).
* Include Indian examples and contexts where they help (monsoon, crops, festivals, local ecology).
* Be accurate. If a fact is uncertain or a syllabus caveat applies, say so instead of guessing.
* Practice questions should be answerable from the topic itself.

## Code of conduct

Be respectful and constructive. This is a study resource for students as young as eleven.
