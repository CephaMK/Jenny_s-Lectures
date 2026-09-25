"""
morphology_display.py
----------------------
Displays the REAL morphology analysis returned by the FastAPI backend.
"""

import streamlit as st


def render_morphology(result: dict):

    st.subheader("Morphological Analysis")

    # ---------------------------------------------------------
    # Basic information
    # ---------------------------------------------------------

    word = result.get("word", "")
    word_type = result.get("type", "unknown")
    is_valid = result.get("is_valid", False)

    st.markdown(
        f"<div style='font-family:Fraunces,serif;font-size:26px;"
        f"color:var(--gold);margin-bottom:10px;'>{word}</div>",
        unsafe_allow_html=True,
    )

    # ---------------------------------------------------------
    # Validity
    # ---------------------------------------------------------

    if is_valid:
        st.success("✓ Valid Kiswahili word")
    else:
        st.warning("⚠ Word was not identified as a valid word")

    # ---------------------------------------------------------
    # Word type
    # ---------------------------------------------------------

    st.markdown(
        f"**Word type:** `{word_type}`"
    )

    # ---------------------------------------------------------
    # Morpheme / token representation
    # ---------------------------------------------------------

    tokens = result.get("tokens", [])

    if tokens:

        st.markdown("**Token sequence**")

        chips = []

        for token in tokens:

            chips.append(
                f"<span style='background:var(--bg);"
                f"border:1px solid var(--gold-soft);"
                f"color:var(--text);"
                f"padding:6px 10px;"
                f"border-radius:4px;"
                f"font-size:14px;'>{token}</span>"
            )

        chip_html = (
            " <span style='color:var(--text-dim);'>+</span> "
            .join(chips)
        )

        st.markdown(
            f"<div style='margin-bottom:16px;'>{chip_html}</div>",
            unsafe_allow_html=True,
        )

    # ---------------------------------------------------------
    # Morphological structure
    # ---------------------------------------------------------

    if word_type == "verb":

        subject_marker = result.get("subject_marker")
        tense_marker = result.get("tense_marker")
        object_marker = result.get("object_marker")
        root = result.get("root")
        suffix = result.get("suffix")

        st.markdown("**Verb structure**")

        structure = []

        if result.get("negative"):
            structure.append("Negative")

        if subject_marker:
            structure.append(f"Subject: {subject_marker}")

        if tense_marker:
            structure.append(f"Tense: {tense_marker}")

        if object_marker:
            structure.append(f"Object: {object_marker}")

        if root:
            structure.append(f"Root: {root}")

        if suffix:
            structure.append(f"Suffix: {suffix}")

        if structure:

            for item in structure:

                st.markdown(
                    f"- {item}"
                )

    # ---------------------------------------------------------
    # Extract nested tense information
    # ---------------------------------------------------------

    tense = result.get("tense")

    if isinstance(tense, dict):

        tense_name = tense.get("name") or tense.get("tense")
        marker = tense.get("marker")
        negative = tense.get("is_negative")

        if tense_name:

            st.markdown(
                f"**Tense:** `{tense_name}`"
            )

        if marker:

            st.markdown(
                f"**Tense marker:** `{marker}`"
            )

    # ---------------------------------------------------------
    # Extract nested subject information
    # ---------------------------------------------------------

    subject = result.get("subject")

    if isinstance(subject, dict):

        person = subject.get("person")
        marker = subject.get("marker")
        noun_class = subject.get("class")

        st.markdown("**Subject information**")

        if person:
            st.markdown(
                f"- Person: `{person}`"
            )

        if marker:
            st.markdown(
                f"- Marker: `{marker}`"
            )

        if noun_class:
            st.markdown(
                f"- Noun class: `{noun_class}`"
            )

    # ---------------------------------------------------------
    # Extract nested object information
    # ---------------------------------------------------------

    obj = result.get("object")

    if isinstance(obj, dict):

        st.markdown("**Object information**")

        if obj.get("marker"):
            st.markdown(
                f"- Marker: `{obj.get('marker')}`"
            )

        if obj.get("class"):
            st.markdown(
                f"- Class: `{obj.get('class')}`"
            )

    elif obj is None:

        st.markdown(
            "**Object:** None detected"
        )

    # ---------------------------------------------------------
    # Noun information
    # ---------------------------------------------------------

    noun_class = result.get("noun_class")

    if noun_class:

        st.markdown("**Noun class analysis**")

        if isinstance(noun_class, dict):

            for key, value in noun_class.items():

                st.markdown(
                    f"- **{key}:** `{value}`"
                )

        else:

            st.write(noun_class)

