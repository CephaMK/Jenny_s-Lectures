# Integration Practice Sandbox

A stripped-down project for practicing three things:
1. Calling an API you didn't build
2. Calling an AI model
3. Deploying the result

## Run it locally

Terminal 1:
```
pip install -r requirements.txt
uvicorn mock_api:app --reload
```

Terminal 2:
```
streamlit run app.py
```

Try:
- Normal input → see the API response
- Typing `fail` → see your error handling kick in
- Stopping the `uvicorn` server, then clicking "Call API" → see the connection-error message
- Asking a question in the AI section (works with or without an API key — see below)

## Practicing the real AI call (optional)

If you set an environment variable `ANTHROPIC_API_KEY` before running Streamlit,
the "Ask AI" button will make a real call to Claude instead of the mock text.
This is the exact pattern you'll use for a real RAG/LLM integration later —
only the prompt-building logic changes.

```
export ANTHROPIC_API_KEY=your_key_here
streamlit run app.py
```

## Deploying (Streamlit Community Cloud)

1. Push this folder to a GitHub repo.
2. Go to share.streamlit.io and connect the repo, pointing at `app.py`.
3. Your deployed app can't reach `127.0.0.1` (your laptop), so either:
   - Deploy `mock_api.py` too (e.g. on Render or Railway, free tier), and update `API_URL`, or
   - Just use this to practice the AI-call + deploy flow, and test the API-call flow locally.
4. If using the real AI call, add `ANTHROPIC_API_KEY` under your app's "Secrets" in Streamlit Cloud settings — never commit it to GitHub.

## When your teammates' real code arrives

- **Backend API (Brian):** change `API_URL` in `app.py` to his real endpoint. If his JSON
  field names differ from this mock's (`word`, `score`, `note`), just update the `data.get(...)`
  calls — the try/except structure around it stays the same.
- **Morphology/RAG (Peter/Hillary):** these likely live behind the backend API, so your
  Streamlit code may not need to change at all — you'll just start receiving real data.
- **Real AI/RAG call:** replace the body of `call_ai()` with the real prompt-construction
  logic (e.g. pulling retrieved context from a vector DB first). The rest of the app —
  the button, the spinner, the `st.info()` display — stays exactly the same.
