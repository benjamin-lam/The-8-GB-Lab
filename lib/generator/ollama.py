"""Ollama Generator Adapter (Stub)

Not active by default in baseline. You'll wire it in when ready.
"""

import os
import httpx

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "phi3:mini")
TIMEOUT_S = float(os.environ.get("OLLAMA_TIMEOUT_S", "120"))

def generate(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }
    with httpx.Client(timeout=TIMEOUT_S) as client:
        r = client.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload)
        r.raise_for_status()
        data = r.json()
        return data.get("response", "")
