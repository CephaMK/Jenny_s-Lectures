def answer_question(question: str, analysis: dict, retrieved=None):
    """
    Answer a question about the current morphology analysis.

    The answer is generated from the actual NLP analysis
    and retrieved project knowledge.
    """

    if not question or not question.strip():
        return "Please enter a question."

    if not isinstance(analysis, dict):
        return "No valid language analysis is available."

    question_lower = question.lower()

    word = analysis.get("word", "")
    word_type = analysis.get("type", "")

    root = analysis.get("root")
    subject_marker = analysis.get("subject_marker")
    tense_marker = analysis.get("tense_marker")
    object_marker = analysis.get("object_marker")

    tense = analysis.get("tense")
    subject = analysis.get("subject")

    # ---------------------------------------------------------
    # SUBJECT QUESTIONS
    # ---------------------------------------------------------

    if (
        "subject" in question_lower
        or "a-" in question_lower
        or "who" in question_lower
    ):

        if subject_marker:

            answer = (
                f'In "{word}", the subject marker is "{subject_marker}".'
            )

            if isinstance(subject, dict):

                person = subject.get("person")
                noun_class = subject.get("class")

                if person:
                    answer += (
                        f" It represents {person.replace('_', ' ')}."
                    )

                if noun_class:
                    answer += (
                        f" The analysis identifies it as noun class "
                        f"{noun_class}."
                    )

            return answer

    # ---------------------------------------------------------
    # TENSE QUESTIONS
    # ---------------------------------------------------------

    if (
        "tense" in question_lower
        or "present" in question_lower
        or "time" in question_lower
    ):

        if tense_marker:

            tense_name = ""

            if isinstance(tense, dict):
                tense_name = (
                    tense.get("name")
                    or tense.get("tense")
                    or ""
                )

            if tense_name:
                tense_name = tense_name.replace("_", " ")

                return (
                    f'In "{word}", the tense marker is '
                    f'"{tense_marker}". '
                    f"It indicates {tense_name}."
                )

            return (
                f'In "{word}", the tense marker is '
                f'"{tense_marker}".'
            )

    # ---------------------------------------------------------
    # ROOT QUESTIONS
    # ---------------------------------------------------------

    if (
        "root" in question_lower
        or "stem" in question_lower
        or "meaning" in question_lower
    ):

        if root:
            return (
                f'The root extracted from "{word}" is "{root}".'
            )

    # ---------------------------------------------------------
    # OBJECT QUESTIONS
    # ---------------------------------------------------------

    if "object" in question_lower:

        if object_marker:

            return (
                f'In "{word}", the object marker is '
                f'"{object_marker}".'
            )

        return (
            f'The morphology analysis does not identify '
            f'an object marker in "{word}".'
        )

    # ---------------------------------------------------------
    # GENERAL QUESTIONS
    # ---------------------------------------------------------

    answer_parts = []

    if word:
        answer_parts.append(
            f'The current word is "{word}".'
        )

    if word_type:
        answer_parts.append(
            f"The morphology engine identifies it as a {word_type}."
        )

    if root:
        answer_parts.append(
            f'The extracted root is "{root}".'
        )

    if subject_marker:
        answer_parts.append(
            f'The subject marker is "{subject_marker}".'
        )

    if tense_marker:
        answer_parts.append(
            f'The tense marker is "{tense_marker}".'
        )

    if retrieved:
        answer_parts.append(
            f"The system also found {len(retrieved)} "
            "related examples in the knowledge base."
        )

    if answer_parts:
        return " ".join(answer_parts)

    return (
        "I could not find enough information in the current "
        "analysis to answer that question."
    )