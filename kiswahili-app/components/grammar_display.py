"""
grammar_display.py
------------------
Displays grammar information when the backend provides it.

The current FastAPI morphology endpoint does not yet return a
dedicated "grammar" object, so this component does not invent
grammar results.
"""

import streamlit as st


def render_grammar(result: dict):

    st.subheader("Grammar Analysis")

    grammar = result.get("grammar")

    # ---------------------------------------------------------
    # Grammar engine has returned actual grammar information
    # ---------------------------------------------------------

    if isinstance(grammar, dict):

        checks = grammar.get("checks", [])

        if checks:

            for check in checks:

                label = check.get("label", "Check")
                passed = check.get("passed", False)

                if passed:
                    st.markdown(f"✅ {label}")
                else:
                    st.markdown(f"⚠️ {label}")

        if grammar.get("valid") is True:

            st.success(
                "Overall: Grammatically correct"
            )

        elif grammar.get("valid") is False:

            st.warning(
                "Overall: Possible grammar issue detected"
            )

    # ---------------------------------------------------------
    # Current morphology endpoint does not provide grammar
    # ---------------------------------------------------------

    else:

        st.info(
            "The current backend analysis endpoint returned "
            "morphological information, but no dedicated grammar "
            "check result."
        )