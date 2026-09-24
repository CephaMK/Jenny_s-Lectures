"""
styling.py
-----------
Injects custom CSS so the Streamlit app's look matches the earlier HTML
preview as closely as Streamlit allows.

Streamlit doesn't give full control over every widget's markup, so this
targets Streamlit's own CSS classes/data-testid attributes. These are not
officially documented and can change between Streamlit versions — if a
future streamlit upgrade breaks the look, check the class names via your
browser's inspector and update the selectors below.
"""

import streamlit as st

# Two palettes — same variable names, different values. The rest of the
# CSS below only ever references var(--x), so swapping this block is all
# that's needed to flip the whole app's look.
PALETTES = {
    "dark": {
        "--bg": "#12293A",
        "--panel": "#1B3B50",
        "--panel-line": "#2C5470",
        "--gold": "#E3A857",
        "--gold-soft": "#C98A3E",
        "--text": "#F3EEE2",
        "--text-dim": "#B9C6CE",
        "--ok": "#6FAE8A",
    },
    "light": {
        "--bg": "#FBF8F2",
        "--panel": "#FFFFFF",
        "--panel-line": "#DDD2C0",
        "--gold": "#B5762A",
        "--gold-soft": "#8F5A1E",
        "--text": "#2A241C",
        "--text-dim": "#5C5347",
        "--ok": "#3E7D57",
    },
}

STYLE_TEMPLATE = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Work+Sans:wght@400;500;600&display=swap" rel="stylesheet">

<style>
:root {{
    --bg: {bg};
    --panel: {panel};
    --panel-line: {panel_line};
    --gold: {gold};
    --gold-soft: {gold_soft};
    --text: {text};
    --text-dim: {text_dim};
    --ok: {ok};
}}

/* Base app + fonts */
html, body, [class*="css"] {{
    font-family: 'Work Sans', sans-serif !important;
}}

/* Titles use the display serif */
h1, h2, h3 {{
    font-family: 'Fraunces', serif !important;
    font-weight: 500 !important;
    color: var(--text) !important;
}}

/* Page background */
.stApp {{
    background-color: var(--bg);
}}

/* Streamlit's own chrome (sidebar + top header bar) */
section[data-testid="stSidebar"] {{
    background-color: var(--panel);
    border-right: 1px solid var(--panel-line);
}}
header[data-testid="stHeader"] {{
    background-color: var(--bg);
}}

/* Section "cards": wrap each component call in st.container(border=True)
   in your components, and this styles that container. */
div[data-testid="stVerticalBlockBorderWrapper"] {{
    background-color: var(--panel);
    border: 1px solid var(--panel-line) !important;
    border-radius: 6px;
    padding: 6px 10px;
}}

/* Buttons */
.stButton > button {{
    background-color: var(--gold);
    color: var(--bg);
    border: none;
    font-weight: 600;
    border-radius: 4px;
}}
.stButton > button:hover {{
    background-color: var(--gold-soft);
    color: var(--bg);
}}

/* Text inputs */
.stTextInput input, .stTextArea textarea {{
    background-color: var(--bg);
    color: var(--text);
    border: 1px solid var(--panel-line);
    border-radius: 4px;
}}

/* Radio buttons (input type selector) */
.stRadio > div {{
    gap: 6px;
}}
.stRadio label p {{
    color: var(--text) !important;
}}

/* General body/caption text */
p, span, div, label {{
    color: var(--text);
}}

/* Dividers */
hr {{
    border-color: var(--panel-line);
}}

/* Success / warning / info banners */
div[data-testid="stAlert"] {{
    border-radius: 4px;
}}
</style>
"""


def inject_custom_css(mode: str = "dark"):
    """
    Inject the CSS for either "dark" or "light" mode. Call this once near
    the top of app.py, after st.set_page_config().
    """
    palette = PALETTES.get(mode, PALETTES["dark"])
    css = STYLE_TEMPLATE.format(
        bg=palette["--bg"],
        panel=palette["--panel"],
        panel_line=palette["--panel-line"],
        gold=palette["--gold"],
        gold_soft=palette["--gold-soft"],
        text=palette["--text"],
        text_dim=palette["--text-dim"],
        ok=palette["--ok"],
    )
    st.markdown(css, unsafe_allow_html=True)


def render_theme_toggle():
    """
    Sidebar toggle for light/dark mode. Returns the selected mode string
    ("dark" or "light") and stores it in session_state so it persists
    across reruns.
    """
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "dark"

    with st.sidebar:
        choice = st.radio(
            "Appearance",
            options=["Dark", "Light"],
            index=0 if st.session_state.theme_mode == "dark" else 1,
            horizontal=True,
        )
    st.session_state.theme_mode = choice.lower()
    return st.session_state.theme_mode
