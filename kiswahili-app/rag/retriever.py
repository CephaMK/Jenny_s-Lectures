import json
import re
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "sentences_data.json"


def load_dataset():
    """Load the project's Kiswahili sentence knowledge base."""
    if not DATA_PATH.exists():
        return []

    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get("sentences", [])

    except (OSError, json.JSONDecodeError):
        return []


def normalize_text(text):
    """Normalize text for simple retrieval."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", " ", text)
    return text


def score_record(record, query_terms):
    """
    Calculate a simple relevance score for one knowledge-base record.
    Higher score means the record matches more query terms.
    """

    sentence = normalize_text(record.get("sentence", ""))
    analysis = normalize_text(
        record.get("word_by_word_morphological_analysis", "")
    )

    score = 0

    for term in query_terms:
        if term in sentence:
            score += 3

        if term in analysis:
            score += 2

    return score


def retrieve(query, top_k=5):
    """
    Retrieve the most relevant examples from the Kiswahili knowledge base.
    """

    if not query or not query.strip():
        return []

    dataset = load_dataset()

    normalized_query = normalize_text(query)

    query_terms = [
        term
        for term in normalized_query.split()
        if len(term) > 1
    ]

    scored_records = []

    for record in dataset:
        score = score_record(record, query_terms)

        if score > 0:
            scored_records.append((score, record))

    scored_records.sort(
        key=lambda item: item[0],
        reverse=True
    )

    results = []

    for score, record in scored_records[:top_k]:
        results.append({
            "score": score,
            "sentence": record.get("sentence", ""),
            "analysis": record.get(
                "word_by_word_morphological_analysis",
                ""
            ),
            "number": record.get("number")
        })

    return results

def retrieve_for_analysis(analysis, top_k=5):
    """
    Retrieve knowledge using the actual morphology analysis
    returned by the NLP engine.
    """

    if not isinstance(analysis, dict):
        return []

    search_terms = []

    word = analysis.get("word")
    root = analysis.get("root")
    subject_marker = analysis.get("subject_marker")
    tense_marker = analysis.get("tense_marker")
    object_marker = analysis.get("object_marker")

    if word:
        search_terms.append(str(word))

    if root:
        search_terms.append(str(root))

    if subject_marker:
        search_terms.append(str(subject_marker))

    if tense_marker:
        search_terms.append(str(tense_marker))

    if object_marker:
        search_terms.append(str(object_marker))

    query = " ".join(search_terms)

    return retrieve(query, top_k=top_k)