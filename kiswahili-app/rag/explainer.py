def generate_explanation(result: dict, retrieved_knowledge=None):
    """
    Generate a human-readable explanation from the actual
    morphology analysis and retrieved project knowledge.
    """

    if not isinstance(result, dict):
        return "No valid analysis is available."

    word = result.get("word", "")
    word_type = result.get("type", "")

    explanation_parts = []

    # Basic information
    if word:
        if word_type == "verb":
            explanation_parts.append(
                f'"{word}" has been identified as a verb.'
            )
        elif word_type == "noun":
            explanation_parts.append(
                f'"{word}" has been identified as a noun.'
            )
        else:
            explanation_parts.append(
                f'"{word}" has been analyzed by the morphology engine.'
            )

    # Verb analysis
    if word_type == "verb":

        root = result.get("root")
        subject_marker = result.get("subject_marker")
        tense_marker = result.get("tense_marker")
        object_marker = result.get("object_marker")

        tense = result.get("tense")
        subject = result.get("subject")
        object_analysis = result.get("object")

        if root:
            explanation_parts.append(
                f'The root is "{root}".'
            )

        if subject_marker:
            subject_text = subject_marker

            if isinstance(subject, dict):
                person = subject.get("person")
                noun_class = subject.get("class")

                if person:
                    subject_text += f", indicating {person.replace("_", " ")}"

                if noun_class:
                    subject_text += f" (noun class {noun_class})"

            explanation_parts.append(
                f'The subject marker "{subject_text}" identifies the subject.'
            )

        if tense_marker:
            tense_name = ""

            if isinstance(tense, dict):
                tense_name = tense.get("name") or tense.get("tense") or ""

            if tense_name:
                tense_name = tense_name.replace("_", " ")

                explanation_parts.append(
                    f'The tense marker "{tense_marker}" indicates {tense_name}.'
                )
            else:
                explanation_parts.append(
                    f'The tense marker is "{tense_marker}".'
                )

        if object_marker:
            explanation_parts.append(
                f'The object marker is "{object_marker}".'
            )

        if object_analysis and isinstance(object_analysis, dict):
            object_person = object_analysis.get("person")
            if object_person:
                explanation_parts.append(
                    f'The object marker refers to {object_person.replace("_", " ")}.'
                )

    # Noun analysis
    elif word_type == "noun":

        noun_class = result.get("noun_class")

        if isinstance(noun_class, dict):
            noun_class_name = noun_class.get("class")
            prefix = noun_class.get("prefix")

            if noun_class_name:
                explanation_parts.append(
                    f'The noun belongs to noun class {noun_class_name}.'
                )

            if prefix:
                explanation_parts.append(
                    f'The noun class prefix is "{prefix}".'
                )

    # Retrieved knowledge
    if retrieved_knowledge:
        explanation_parts.append(
            f'The system also retrieved {len(retrieved_knowledge)} '
            'related example(s) from the Kiswahili knowledge base.'
        )

    return " ".join(explanation_parts)