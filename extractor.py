"""Week 2 homework: fix the date extractor.

Our event bot reads show notices and puts the EVENT date on the calendar.
Right now it grabs the first date it sees, which is often the RSVP deadline.

Your job: change extract_event_date() so it returns the date of the event itself.
Only edit this file. Run the tests with:  python -m unittest -v
"""

import re
from datetime import datetime

NOTICE = (
    "BK UNDERGROUND SESSIONS #12: Presale RSVP lottery drops October 14, 2026 at 6:00 PM online. "
    "Secret warehouse doors open October 21, 2026 at 11:00 PM for the live set. "
    "Curfew strictly midnight. 21+ only."
)

DATE_PATTERN = r"(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}), (\d{4})"


def to_iso(match):
    """Turn a regex match like 'October 21, 2026' into '2026-10-21'."""
    return datetime.strptime(match.group(0), "%B %d, %Y").strftime("%Y-%m-%d")


def extract_event_date_old(text):
    """Return the event date as 'YYYY-MM-DD', or None if the notice has no event date.

    BUG: this returns the first date in the text, even when that date is a deadline.
    """
    match = re.search(DATE_PATTERN, text)
    if match:
        return to_iso(match)
    return None

import re

def extract_event_date(text):
    """Return the event date as 'YYYY-MM-DD', or None if the notice has no event date."""

    non_event_terms = (
        "rsvp",
        "presale",
        "by",
        "closes",
        "deadline",
        "register",
        "registration",
        "apply",
        "application",
        "submit",
        "submission",
        "due",
    )

    # Split into sentences/clauses so a deadline in another
    # part of the notice doesn't disqualify the event date.
    parts = re.split(r'[.\n;]+', text)

    for part in parts:
        match = re.search(DATE_PATTERN, part)

        if not match:
            continue

        lower_part = part.lower()

        # Ignore dates associated with non-event activities.
        if any(term in lower_part for term in non_event_terms):
            continue

        return to_iso(match)

    return None

if __name__ == "__main__":
    print("Event date:", extract_event_date(NOTICE))
