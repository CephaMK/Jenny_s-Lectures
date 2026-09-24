"""
morphology_display.py
----------------------
Turns Peter's raw morphology JSON into a readable visual breakdown,
instead of showing raw JSON to the user.
"""

import streamlit as st


def render_morphology(result: dict):
    st.subheader("Morphological Analysis")

    word = result.get("word", "")
    morphemes = result.get("morphemes", [])

    st.markdown(
        f"<div style='font-family:Fraunces,serif;font-size:26px;"
        f"color:var(--gold);margin-bottom:10px;'>{word}</div>",
        unsafe_allow_html=True,
    )

    if morphemes:
        root = result.get("root", "")
        chips = []
        for m in morphemes:
            is_root = m == root
            style = (
                "border:1px solid var(--gold);color:var(--gold);font-weight:600;"
                if is_root
                else "border:1px solid var(--gold-soft);color:var(--text);"
            )
            chips.append(
                f"<span style='background:var(--bg);{style}"
                f"padding:6px 10px;border-radius:4px;font-size:14px;'>{m}</span>"
            )
        chip_html = " <span style='color:var(--text-dim);'>+</span> ".join(chips)
        st.markdown(
            f"<div style='margin-bottom:16px;'>{chip_html}</div>",
            unsafe_allow_html=True,
        )

    attrs = [
        ("Subject", result.get("subject", "—")),
        ("Tense", result.get("tense", "—")),
        ("Object", result.get("object_class", "—")),
        ("Root", result.get("root", "—")),
    ]
    cards_html = ""
    for label, value in attrs:
        cards_html += (
            "<div style='border-left:2px solid var(--gold-soft);padding:8px 0 8px 12px;'>"
            f"<div style='color:var(--text-dim);font-size:12.5px;margin-bottom:3px;'>{label}</div>"
            f"<div style='color:var(--text);font-size:16px;font-weight:500;'>{value}</div>"
            "</div>"
        )
    st.markdown(
        f"<div style='display:grid;grid-template-columns:repeat(2,1fr);"
        f"gap:14px;margin-bottom:8px;'>{cards_html}</div>",
        unsafe_allow_html=True,
    )

    if result.get("note"):
        st.info(result["note"])
