# Metrics

## Warum Metriken?
Weil „fühlt sich schnell an“ kein Engineering ist – vor allem nicht auf low-resource.

## Baseline-Metriken (pro Run)
- retrieval_time_ms
- generation_time_ms
- review_time_ms
- ram_usage_mb
- iterations

## Interpretation (kurz)
- Steigt `retrieval_time_ms` stark → Index/Query prüfen, KB wächst
- Steigt `generation_time_ms` → Modell/Prompt-Größe/Timeouts
- Steigen `iterations` → Reviewer zu streng oder Prompt-Synthesis zu schwach
- Steigt `ram_usage_mb` → Leaks/Imports/Modell-Setup

## Wo gespeichert?
- `data/pdd.sqlite3` → Tabelle `evolution` → `metrics_json`
