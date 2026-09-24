# app.py
# Practice sandbox: calling an unfamiliar API + calling an AI model, then deploying.
# Everything marked "REPLACE THIS" is where a teammate's real code will eventually go.

import os
import requests
import streamlit as st

# ============================================================
# 1. CONFIG  (REPLACE THIS: swap for your teammate's real URL)
# ============================================================
API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="Integration Practice", page_icon="🧪", layout="centered")
st.title("🧪 Integration Practice Sandbox")
st.caption("Practicing: call an API → handle failure → call an AI model → display results.")

# ============================================================
# 2. CALL A TEAMMATE'S API
# ============================================================
st.header("1. Call the backend API")
user_input = st.text_input("Text to send to the backend:", value="hello there")

if st.button("Call API"):
    try:
        with st.spinner("Calling backend..."):
            resp = requests.post(API_URL, json={"text": user_input}, timeout=5)

        if resp.status_code == 200:
            data = resp.json()
            st.success("Got a response:")
            st.json(data)
            st.session_state["last_api_result"] = data
        else:
            st.error(f"Backend returned status {resp.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("🚨 Can't reach the backend. Is `uvicorn mock_api:app --reload` running?")
    except requests.exceptions.Timeout:
        st.error("🚨 Backend took too long to respond.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")

st.divider()

# ============================================================
# 3. CALL AN AI MODEL
#    Uses a real Anthropic call if ANTHROPIC_API_KEY is set,
#    otherwise falls back to a mock so the app still runs.
#    (REPLACE THIS section with your team's real RAG/LLM call
#     once it's ready — the UI around it doesn't need to change.)
# ============================================================
st.header("2. Ask the AI")
question = st.text_input("Ask a question about the result above:")


def call_ai(prompt: str) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        # MOCK fallback — no key configured
        return f"[MOCK RESPONSE] I'd explain: '{prompt}' — set ANTHROPIC_API_KEY for a real answer."

    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
    except Exception as e:
        return f"[AI call failed: {e}]"


if st.button("Ask AI") and question:
    context = st.session_state.get("last_api_result", {})
    prompt = f"Given this data: {context}\n\nAnswer this question: {question}"
    with st.spinner("Thinking..."):
        answer = call_ai(prompt)
    st.info(answer)

st.divider()
st.caption(
    "Deploy this to Streamlit Community Cloud to practice the full flow end to end. "
    "See README.md for how to swap in real teammate code."
)
