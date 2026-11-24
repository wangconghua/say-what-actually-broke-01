#!/usr/bin/env python3
"""Say What Actually Broke: one line of error copy that tells the brutal truth."""

import os

ERROR_LINE = "Your file is 2 GB. The limit is 2 MB. Optimism is not a compression algorithm."

OUT_PATH = "/output/entry.txt"

# Words that explain the joke instead of being the joke. A funny line must
# land on its own; if it has to say it is funny, it is not.
META_HUMOR_WORDS = ("funny", "joke", "haha", "lol", "hilarious")

# Generic apologies say nothing about what broke. The brief wants the real
# failure named in plain words, not an apology in generalities.
APOLOGY_WORDS = ("sorry", "apologise", "apologize", "our apologies", "we apologise", "we apologize")

# The line must name a concrete failure, not gesture at one.
FAILURE_WORDS = ("file", "disk", "database", "server", "memory", "network", "deploy", "upload", "download", "password", "session", "payment")


def validate(line: str) -> None:
    if not (1 <= len(line) <= 200) or line.isspace() or "\n" in line:
        raise ValueError("entry must be one line of 1-200 characters, not only whitespace")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    lowered = line.lower()
    for word in META_HUMOR_WORDS:
        if word in lowered:
            raise ValueError(f"entry must not explain its own joke (found {word!r})")
    for word in APOLOGY_WORDS:
        if word in lowered:
            raise ValueError(f"entry must name the failure, not apologise for it (found {word!r})")
    if not any(word in lowered for word in FAILURE_WORDS):
        raise ValueError("entry must name a concrete failure")


def main():
    # The gate wants 1-200 characters, not only whitespace, on a single line.
    # The joke: the upload failed on a hard size limit, and the twist is that
    # optimism is not a compression algorithm — a specific failure, a plain
    # number the user can act on, and a punchline a colleague would repeat.
    validate(ERROR_LINE)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ERROR_LINE)


if __name__ == "__main__":
    main()
