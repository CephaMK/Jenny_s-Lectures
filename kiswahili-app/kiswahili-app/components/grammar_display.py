"""
grammar_display.py
--------------------
Turns Hillary/Faith's raw grammar-check JSON into readable pass/fail
indicators, instead of showing `{"agreement": true}` to the user.
"""

import streamlit as st


def render_grammar(result: dict):
    st.subheader("Grammar Analysis")

    grammar = result.get("grammar", {})
    checks = grammar.get("checks", [])

    for check in checks:
        label = check.get("label", "Check")
        passed = check.get("passed", False)
        if passed:
            st.markdown(f"✅ {label}")
        else:
            st.markdown(f"⚠️ {label}")

    if grammar.get("valid"):
        st.success("Overall: Grammatically correct")
    else:
        st.warning("Overall: Possible grammar issue detected")
