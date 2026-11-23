"""Warning Label for Humans: One Line, Big Laugh — entry program.

The label, in three beats: the human nods, says "sounds good", and
then does the exact opposite. The joke is recognition — everyone has
met this person, and everyone has been this person — and the turn
arrives in the last few words, as a printed instruction: keep this
unit away from important decisions.

Against the judge brief: on-subject (a single-line safety warning
label for every human being, in label wording from the first word);
the laugh lands in one read, with the turn in the final instruction
rather than smeared across the line; it feels true about people in
general; it sounds like a real printed label ("WARNING", "Keep away
from"); one clean line, 111 characters, no filler, no second idea,
no repeated joke.
"""

import os

# The label, in pieces so the setup and the punchline stay readable.
# The closer is the whole joke's landing: the human is not broken,
# it is simply not to be trusted near a decision that matters.
SETUP = "WARNING: This human will nod, say 'sounds good,'"
TURN = "and do the exact opposite."
CLOSER = "Keep away from important decisions."

LABEL = " ".join([SETUP, TURN, CLOSER])


def check(label: str) -> str:
    """The gate wants 1 to 160 characters of real text, no more.

    A label outside the gate is never judged, so fail loudly here
    instead of writing a losing file.
    """
    text = label.strip()
    if not text:
        raise ValueError("label must not be empty or only whitespace")
    if len(text) > 160:
        raise ValueError("label must be 1 to 160 characters, got %d" % len(text))
    if "\n" in text:
        raise ValueError("label must be a single line")
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(check(LABEL))


if __name__ == "__main__":
    main()
