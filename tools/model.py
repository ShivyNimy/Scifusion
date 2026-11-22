"""Data model helpers used by every content module.

Content is written as plain Python data so it is easy to review, diff and
reuse.  The helpers keep the curriculum files compact:

    C(1, "Chemical Reactions and Equations", [
        T(
            "Chemical Equations",
            "A chemical equation is a shorthand ...",
            ["Reactants are written on the left ...", ...],
            [E("Burning magnesium", "2Mg + O2 -> 2MgO ...")],
            [M("Which side ...?", "Left|Right|Both|Neither", 0, "Reactants are ..."),
             S("Balance H2 + O2 -> H2O.", "2H2 + O2 -> 2H2O", "...")],
            terms=[("Reactant", "A substance that is used up ...")],
            formulas=["2H2 + O2 -> 2H2O"],
        )
    ])

Inline formatting accepted in every text field:
``**bold**``, ``*italic*``, ``` `code` ```, ``~subscript~`` and ``^superscript^``.
"""

from __future__ import annotations


def E(title, text):
    """A worked example."""
    return {"title": title, "text": text}


def M(question, options, answer, solution):
    """A multiple-choice question.

    ``options`` may be a list or a single string with ``|`` separators.
    ``answer`` is the zero-based index of the correct option.
    """
    if isinstance(options, str):
        options = [o.strip() for o in options.split("|")]
    return {
        "type": "mcq",
        "q": question,
        "options": list(options),
        "answer": answer,
        "solution": solution,
    }


def S(question, answer, solution=None):
    """A short / long answer practice question."""
    return {
        "type": "short",
        "q": question,
        "answer": answer,
        "solution": solution if solution is not None else answer,
    }


def T(name, summary, key_points, examples, questions, terms=None, formulas=None):
    """One topic."""
    return {
        "name": name,
        "summary": summary,
        "key_points": list(key_points),
        "examples": list(examples),
        "questions": list(questions),
        "terms": [tuple(t) for t in (terms or [])],
        "formulas": list(formulas or []),
    }


def C(number, name, topics, intro=None):
    """One chapter."""
    return {
        "number": number,
        "name": name,
        "intro": intro,
        "topics": list(topics),
    }


def SUBJECT(code, title, class_key, book, intro, chapters):
    """A complete subject book."""
    return {
        "code": code,
        "title": title,
        "class_key": str(class_key),
        "book": book,
        "intro": intro,
        "chapters": list(chapters),
    }
