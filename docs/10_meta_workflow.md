# Meta-Workflow

## Modell (Denksystem)
Der Workflow ist bewusst simpel und sequenziell:

1. **Orchestrator**: nimmt Intent an, wendet Constraints an, steuert Iteration
2. **Retriever**: liefert Kontext aus der Knowledge Base (FTS5)
3. **Generator**: produziert einen Entwurf (Dummy → später Ollama)
4. **Reviewer**: prüft deterministisch (Regeln) + gibt Feedback
5. **Evolution-Log**: speichert Run + Metriken (Zeit/RAM/Iterationen)

## Warum diese Reihenfolge?
- „Kontext vor Kreativität“: erst Retrieval, dann Generation
- „Review ist Pflicht“: LLMs sind höflich → wir brauchen Widerstand
- „Metriken statt Vibes“: low-resource zwingt zu bewussten Tradeoffs

## Artefakte (PDD Layer)
- `pdd/actors.yaml`
- `pdd/constraints.yaml`
- `pdd/prompt_template.md`
- `lib/pdd/prompt_compiler.py`

Der Prompt ist Ergebnis dieser Artefakte, nicht der Startpunkt.
