"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea that
sounds ridiculous at first glance but makes sense as a real business.
Python 3.13 standard library only, no network at run time.
"""

import os

ENTRY = (
    "We sell naming rights to potholes, because the café on the corner "
    "pays $50 a month to sponsor the crater outside its door — and the "
    "city fills sponsored holes first."
)


def main() -> None:
    # Gate assertions: one sentence, 1-200 chars, non-empty.
    assert ENTRY.strip(), "entry must not be empty"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over 200"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), (
        "entry must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
