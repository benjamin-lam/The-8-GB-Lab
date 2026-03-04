def generate(prompt: str, feedback: str = "") -> str:
    """Baseline generator.

    Replace later with Ollama adapter.
    The dummy generator simply returns a structured placeholder with the prompt summary.
    """
    # Keep it deterministic and transparent.
    head = "## Baseline Generator (Dummy)\n"
    fb = f"\n**Reviewer-Feedback (eingearbeitet):** {feedback}\n" if feedback else ""
    return (
        head
        + fb
        + "\n**Hinweis:** Hier ist noch kein LLM angeschlossen.\n"
        + "Du kannst jetzt den Ollama-Adapter aktivieren und denselben API-Flow behalten.\n\n"
        + "### Echo der Aufgabe\n"
        + prompt[:900]
    )
