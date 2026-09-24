# mock_api.py
# A tiny stand-in for "your teammate's" backend.
# Goal: practice calling AN API you didn't write, not this one specifically.
# Run with: uvicorn mock_api:app --reload

import random
import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AnalyzeRequest(BaseModel):
    text: str


@app.post("/analyze")
def analyze_text(request: AnalyzeRequest):
    text = request.text.strip()

    # Simulate real-world messiness on purpose, so you practice handling it:
    time.sleep(random.uniform(0.3, 1.2))          # unpredictable latency
    if text.lower() == "fail":                    # force an error case to test your try/except
        return {"error": "simulated backend failure"}, 500

    if not text:
        return {"word": "", "score": 0, "note": "empty input"}

    return {
        "word": text,
        "length": len(text),
        "score": random.randint(1, 100),
        "note": f"Processed '{text}' successfully",
    }
