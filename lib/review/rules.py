import re

FORBIDDEN = [
    r"\beval\s*\(",
    r"\bexec\s*\(",
    r"\bos\.system\s*\(",
    r"\bsubprocess\.Popen\s*\(",
]

def review_pythonish_output(text: str) -> dict:
    """Very small baseline reviewer.

    Goals:
    - Block obvious dangerous patterns
    - Encourage a main entrypoint when code is present
    - Keep it transparent and deterministic
    """
    low = text.lower()

    for pat in FORBIDDEN:
        if re.search(pat, low):
            return {"valid": False, "feedback": f"Verbotenes Muster gefunden: `{pat}`. Entferne es."}

    # If there's a python code block, check for def main or if __name__ guard
    has_code = "```" in text and ("python" in low or "```" in text)
    if has_code:
        if ("def main" not in low) and ("if __name__" not in low):
            return {"valid": False, "feedback": "Wenn du Python-Code lieferst: bitte `def main()` oder `if __name__ == "__main__":` ergänzen."}

    return {"valid": True, "feedback": ""}
