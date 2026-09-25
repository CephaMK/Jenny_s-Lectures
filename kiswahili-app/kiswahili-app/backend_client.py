"""
backend_client.py
------------------
This is the ONLY file you will need to change once Brian's FastAPI is ready.

Right now, `analyze()` returns fake/hardcoded data that mimics what the
real API will eventually return. Everything else in the app (components,
app.py) talks to this function and doesn't care whether the data is fake
or real.

WHEN BRIAN'S API IS READY:
    1. Uncomment the `requests.post(...)` block below.
    2. Delete (or ignore) the FAKE_RESPONSES dictionary.
    That's it — nothing else in the project needs to change.
"""

import time

# import requests  # <-- uncomment when connecting to the real API

API_URL = "http://localhost:8000/analyze"  # Brian's endpoint, once it exists


# ---------------------------------------------------------------------------
# FAKE DATA (Phase 1) — stand-ins for Peter's morphology + Hillary/Faith's
# grammar engine, shaped exactly like the JSON the real API is expected to
# return (see the architecture doc, section 10).
# ---------------------------------------------------------------------------
FAKE_RESPONSES = {
    "ninampenda": {
        "word": "Ninampenda",
        "morphemes": ["ni", "na", "m", "pend", "a"],
        "subject": "1st person singular",
        "tense": "present",
        "object_class": "Class 1",
        "root": "pend",
        "gloss": "love",
        "grammar": {
            "valid": True,
            "checks": [
                {"label": "Subject agreement", "passed": True},
                {"label": "Object agreement", "passed": True},
                {"label": "Verb structure", "passed": True},
            ],
        },
        "explanation": (
            "The word 'ninampenda' means 'I love him/her'. The prefix 'ni-' "
            "marks the subject (I), '-na-' marks present tense, '-m-' marks "
            "a Class 1 object (him/her), 'pend' is the root meaning 'love', "
            "and the final '-a' closes the verb."
        ),
    },
    "anasoma": {
        "word": "Anasoma",
        "morphemes": ["a", "na", "som", "a"],
        "subject": "3rd person singular",
        "tense": "present",
        "object_class": "None",
        "root": "som",
        "gloss": "read",
        "grammar": {
            "valid": True,
            "checks": [
                {"label": "Subject agreement", "passed": True},
                {"label": "Object agreement", "passed": True},
                {"label": "Verb structure", "passed": True},
            ],
        },
        "explanation": (
            "The word 'anasoma' means 'he/she is reading'. The prefix 'a-' "
            "marks a 3rd person singular subject, '-na-' marks present "
            "tense, and 'som' is the root meaning 'read'."
        ),
    },
}

DEFAULT_RESPONSE_KEY = "ninampenda"


def analyze(text: str) -> dict:
    """
    Send `text` to the backend NLP system and return the parsed analysis.

    Phase 1 (now): returns fake data so the UI can be built and demoed
    without depending on Peter, Hillary/Faith, or Brian being finished.

    Phase 2 (later): calls Brian's real FastAPI endpoint instead.
    """
    time.sleep(0.4)  # tiny delay so the UI's loading spinner is visible

    key = text.strip().lower().replace(".", "")
    if key in FAKE_RESPONSES:
        return FAKE_RESPONSES[key]

    # Unknown input in Phase 1: return the default example but flag it,
    # so the UI still has something to show during early demos/testing.
    fallback = dict(FAKE_RESPONSES[DEFAULT_RESPONSE_KEY])
    fallback = {**fallback, "word": text, "note": "Demo mode: showing example analysis for unrecognized input."}
    return fallback

    # -------------------------------------------------------------------
    # REAL VERSION (uncomment once Brian's API exists, delete code above):
    #
    # response = requests.post(API_URL, json={"text": text}, timeout=10)
    # response.raise_for_status()
    # return response.json()
    # -------------------------------------------------------------------
