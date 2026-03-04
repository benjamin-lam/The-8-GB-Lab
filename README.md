# PDD Low-Resource Orchestrator (Baseline Repo)


## Doc-first
Dieses Projekt wird **als laufendes Log** entwickelt: Doku ist der Kern, Code der Beweis.
Siehe:
- `docs/` (laufende Dokumentation)
- `DOD.md` (Definition of Done)

Baseline-Repository für einen **ressourcenschonenden** Meta-Workflow (FastAPI Orchestrator + SQLite FTS Retriever + regelbasierter Reviewer + Evolution-Log).
Ziel: auf **8 GB RAM / ältere CPU** lauffähig, transparent, messbar, iterativ ausbaubar.

## Features (Baseline)
- FastAPI Service: `POST /orchestrate`
- Retriever: SQLite **FTS5** über Markdown-Dateien in `knowledge_base/`
- Generator: **Dummy** (baseline) + Adapter-Stub für Ollama (später aktivieren)
- Reviewer: einfache, regelbasierte Checks (Python-Output, verbotene Patterns)
- Evolution-Log: SQLite DB mit Metriken (Latenzen, Iterationen, RAM)
- Tests: Minimal-Tests für API + Retriever
- Scripts: `index_kb.py` zum Indexieren der Knowledge Base

## Quickstart (lokal)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Knowledge Base indexieren (FTS)
python scripts/index_kb.py

# Server starten
uvicorn app.main:app --reload
```

Test Request:
```bash
curl -s -X POST http://127.0.0.1:8000/orchestrate \
  -H "Content-Type: application/json" \
  -d '{"user_prompt":"Schreibe ein Python-Skript, das Git-Logs analysiert"}' | jq
```

## Tests
```bash
pytest -q
```

## Repo-Struktur
```
app/                    FastAPI App (Entry + Routing)
lib/
  retrieval/            SQLite FTS5 Retriever (Indexer + Query)
  generator/            Dummy Generator + Ollama Adapter Stub
  review/               Regelbasierter Reviewer
  log/                  Evolution-Log (SQLite)
  metrics/              Metriken (Zeit, RAM, CPU)
knowledge_base/         Markdown-Dokumente (als Kontext)
scripts/                Index/Utilities
tests/                  Pytest Tests
```

## Nächste Schritte (PDD-Loop)
1) Dummy Generator ersetzen durch `lib/generator/ollama.py` (HTTP)  
2) Reviewer-Regeln erweitern (Artefakt-spezifisch)  
3) Metriken visualisieren (einfacher CLI-Report / JSON Export)  
4) Prompt-Synthesis sauberer machen (Rollen + Constraints)  


## PDD Layer (100%)
- `pdd/actors.yaml`: explizite Rollen
- `pdd/constraints.yaml`: Constraints/Nicht-Ziele
- `pdd/prompt_template.md`: Prompt als Artefakt
- `lib/pdd/prompt_compiler.py`: kompiliert Prompt aus Artefakten + Kontext + Memory
