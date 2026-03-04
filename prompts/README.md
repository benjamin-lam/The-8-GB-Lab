# Prompts

Dieses Verzeichnis archiviert Prompts, die an Tools/Modelle übergeben werden (z.B. Codex).

Ziel:
- Reproduzierbarkeit
- Nachvollziehbarkeit
- Lernkurve dokumentieren (was hat funktioniert, was nicht)

## Regeln

- Ein Prompt = eine Datei
- Dateiname: `YYYY-MM-DD_NNN_<topic>.md`
- Prompts sind "Input-Artefakte" und werden versioniert.

## Minimal-Metadaten pro Prompt

- tool/model: z.B. Codex
- purpose: Ziel des Prompts
- context links: Worklog/Decisions/Blueprints
- expected output: was soll rausfallen
- constraints: Non-goals, Quality Gates
- status: draft|used|retired