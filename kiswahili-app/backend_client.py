"""
backend_client.py
-----------------
Client used by the Streamlit frontend to communicate with the
real FastAPI backend.

The Streamlit UI should NOT need to know the FastAPI URL or
request format. It simply calls:

    analyze(text)

and receives the backend analysis.
"""

import requests


# Brian's real FastAPI server
API_BASE_URL = "http://127.0.0.1:8000"


def analyze(text: str, input_type: str = None) -> dict:
    """
    Send Kiswahili input to the real FastAPI backend.

    Parameters
    ----------
    text : str
        The Kiswahili word or sentence to analyze.

    input_type : str, optional
        "Word" or "Sentence".

        If not supplied, the function makes a simple inference:
        - text containing spaces -> Sentence
        - otherwise -> Word

    Returns
    -------
    dict
        The analysis returned by the real FastAPI backend.

    Raises
    ------
    ValueError
        If the input is empty or the input type is invalid.

    requests.RequestException
        If the FastAPI server cannot be reached or returns an HTTP error.
    """

    text = text.strip()

    if not text:
        raise ValueError("Input cannot be empty.")

    # ---------------------------------------------------------
    # Determine whether we are analyzing a word or sentence
    # ---------------------------------------------------------
    if input_type is None:
        if " " in text.strip():
            input_type = "Sentence"
        else:
            input_type = "Word"

    # ---------------------------------------------------------
    # WORD ANALYSIS
    # ---------------------------------------------------------
    if input_type.lower() == "word":
        url = f"{API_BASE_URL}/api/v1/analyze/word"

        response = requests.post(
            url,
            json={"word": text},
            timeout=10
        )

    # ---------------------------------------------------------
    # SENTENCE ANALYSIS
    # ---------------------------------------------------------
    elif input_type.lower() == "sentence":
        url = f"{API_BASE_URL}/api/v1/analyze/sentence"

        response = requests.post(
            url,
            json={"sentence": text},
            timeout=10
        )

    else:
        raise ValueError(
            f"Invalid input_type: {input_type}. "
            "Use 'Word' or 'Sentence'."
        )

    # Raise an exception for HTTP errors such as:
    # 400, 404, 500, 503, etc.
    response.raise_for_status()

    # FastAPI returns JSON
    data = response.json()

    # ---------------------------------------------------------
    # Check that the backend reports success
    # ---------------------------------------------------------
    if not data.get("success", False):
        raise RuntimeError(
            data.get("detail", "Backend analysis failed.")
        )

    # ---------------------------------------------------------
    # Return ONLY the actual analysis.
    #
    # FastAPI response looks like:
    #
    # {
    #     "success": True,
    #     "input": "...",
    #     "analysis": {...}
    # }
    #
    # The UI should receive the "analysis" part.
    # ---------------------------------------------------------
    if input_type == "Sentence":

        return {
        "analysis": data["analysis"],
        "grammar": data.get("grammar")
    }

    return data["analysis"]