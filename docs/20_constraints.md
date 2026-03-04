# Constraints

## Low-Resource First
- CPU ist ok, RAM ist knapp.
- keine parallelen Modelle
- keine Embeddings als Pflicht
- klare Timeouts, klare Logs

## Engineering-Prinzipien
- KISS / YAGNI
- kleine Schritte (1–2h)
- testbar, messbar, dokumentiert

## Safety (Baseline)
- keine offensichtlichen „Execution“-Primitiven (`eval`, `exec`, `os.system`, `subprocess.Popen`)
- Reviewer blockt diese Muster deterministisch

Quelle der Wahrheit:
- `pdd/constraints.yaml`
