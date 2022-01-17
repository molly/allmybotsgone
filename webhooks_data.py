import re

SCAMMY = [
    r"help(ed)? me",
    r"\bhmu\b",
    r"instagram",
    r"\bdm\b",
    r"direct me?ss?a?ge?",
    r"inbox",
    r"recover",
    r"support",
]

EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
SCAMMY_PATTERN = re.compile(r"(" + r"|".join(SCAMMY) + r")", re.IGNORECASE)
