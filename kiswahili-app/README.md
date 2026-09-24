# Kiswahili Language Intelligence Engine — UI (CEPHA's part)

Phase 1 prototype: a working Streamlit app with fake/hardcoded analysis
data, structured so it can be pointed at Brian's real FastAPI later
without any rewrite.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

Then open the local URL Streamlit prints (usually http://localhost:8501).

## Try it

Type one of these into the input box and click **Analyze**:

- `Ninampenda`
- `Anasoma`

Anything else will fall back to a demo example so the UI never looks empty.

## Project structure

```
app.py                    # main entry point — wires components together
backend_client.py         # ONLY file to change when connecting to real API
components/
  input_panel.py          # word/sentence/question input
  morphology_display.py   # renders morphology results
  grammar_display.py      # renders grammar check results
  explanation.py          # plain-language explanation + "ask" box
demo/
  demo_cases.json         # example inputs for the presentation
  demo_script.md          # step-by-step demo walkthrough
presentation/              # put screenshots/diagrams here later
```

## Connecting to the real backend (Phase 2)

Open `backend_client.py`:

1. Uncomment the `import requests` line and the `requests.post(...)` block
   at the bottom of `analyze()`.
2. Delete or ignore the `FAKE_RESPONSES` dictionary above it.
3. Set `API_URL` to Brian's actual endpoint.

Nothing in `app.py` or `components/` needs to change — they only care
about the dictionary shape `analyze()` returns (`word`, `morphemes`,
`subject`, `tense`, `object_class`, `root`, `grammar`, `explanation`).

## Development phases

1. ✅ Basic Streamlit UI with fake data (this prototype)
2. Connect to Brian's API
3. Display real morphology results (Peter)
4. Display real grammar results (Hillary/Faith)
5. Improve explanations
6. Polish demo/presentation
7. Add RAG/chatbot prototype (`rag/` folder, later)
