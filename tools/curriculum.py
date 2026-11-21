"""Top-level curriculum map for Scifusion.

Each class has one or more subjects (a Class 6-10 "Science" book, or the
separate Physics / Chemistry / Biology books of Classes 11-12).  The subject
code is also the file name of the content module in this package:
``tools/data/<code>.py``.
"""

CLASSES = [
    ("6", "Class 6"),
    ("7", "Class 7"),
    ("8", "Class 8"),
    ("9", "Class 9"),
    ("10", "Class 10"),
    ("11", "Class 11"),
    ("12", "Class 12"),
]

# (class key, [(subject code, subject title, full subject name), ...])
SUBJECTS = {
    "6": [("6-science", "Science", "Science")],
    "7": [("7-science", "Science", "Science")],
    "8": [("8-science", "Science", "Science")],
    "9": [("9-science", "Science", "Science")],
    "10": [("10-science", "Science", "Science")],
    "11": [
        ("11-physics", "Physics", "Physics"),
        ("11-chemistry", "Chemistry", "Chemistry"),
        ("11-biology", "Biology", "Biology"),
    ],
    "12": [
        ("12-physics", "Physics", "Physics"),
        ("12-chemistry", "Chemistry", "Chemistry"),
        ("12-biology", "Biology", "Biology"),
    ],
}

ALL_SUBJECT_CODES = [code for _, subs in SUBJECTS.items() for code, _, _ in subs]


def subject_title(code):
    for _, subs in SUBJECTS.items():
        for c, short, full in subs:
            if c == code:
                return short
    raise KeyError(code)


def class_of(code):
    return code.split("-")[0]
