# EXP-0001 Baseline steht

## Hypothese
Ein sequenzieller Orchestrator mit FTS5-Retrieval, Dummy-Generator und regelbasiertem Review
kann auf low-resource Hardware laufen und die Denkstruktur (PDD) sichtbar machen.

## Änderung
- Baseline Repo erstellt
- PDD Artefakte eingeführt (Actors/Constraints/Template/Compiler)
- Evolution-Log + Metriken

## Messung
- `/health` ok
- `/orchestrate` liefert Antwort + Metrics
- `pytest` grün

## Ergebnis
Die Architektur ist lauffähig und nachvollziehbar.
Nächster Engpass ist nicht Code – sondern wie gut Prompt-Synthesis + Reviewer Feedback zusammenarbeiten.

## Nächster Schritt
Dummy-Generator durch Ollama ersetzen, ohne den Workflow zu ändern.
