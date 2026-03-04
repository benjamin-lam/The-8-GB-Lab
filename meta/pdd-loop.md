# PDD Loop

Der PDD Loop ist der kleinste reproduzierbare Zyklus in diesem Repository.

Er soll verhindern, dass wir “viben bis es irgendwie klappt” und stattdessen sichtbar machen:
- was wir glauben
- was wir entscheiden
- was wir bauen
- was wir gelernt haben

Nicht als Ritual.
Als Schutz vor Zufall.

---

# TL;DR

```

Intent → Context → Plan → Build → Review → Decide → Log → Repeat

````

Wenn du nur eine Sache mitnimmst:

**Kein Build ohne Intent. Kein Change ohne Trace.**

---

# Warum ein Loop?

LLMs liefern schnell Output.
Das ist nützlich.

Aber: Geschwindigkeit ohne Loop erzeugt Software-Plastik.
Sie glänzt heute und wird morgen unwartbar.

Der Loop sorgt dafür, dass wir:
- Entscheidungen sichtbar machen
- Trade-offs festhalten
- Änderungen rückverfolgbar halten
- klein iterieren, statt groß zu fantasieren

---

# Artefakte im Loop

Der Loop erzeugt oder aktualisiert immer mindestens eines davon:

- **Worklog** (`/worklog/`) — Chronologie, was passiert ist
- **Decisions (ADR)** (`/decisions/`) — Trade-offs als Kanon
- **Prompts** (`/prompts/`) — Inputs an KI als versionierte Artefakte
- **Code / Docs** (`/docs`, `/scripts`, `/templates`) — Ergebnis

---

# Der Zyklus Schritt für Schritt

## 1 Intent

Was soll am Ende anders sein?

Minimal formulieren.
Ein Satz reicht.

Beispiele:
- “Build-Stubs schaffen, damit Markdown zu HTML wird.”
- “Workflow so dokumentieren, dass Codex ihn befolgen kann.”

## 2 Context

Was ist der aktuelle Stand?
Welche Constraints existieren?

- Repo-Struktur
- Non-goals (KISS/YAGNI)
- vorhandene ADRs
- vorhandene Worklog-Einträge

## 3 Plan

Eine konkrete Aufgabe, klein genug für 1–2 Stunden.

Wenn es größer ist:
zerlegen.

Output:
- Taskliste oder ein einzelner nächster Schritt.

## 4 Build

Implementieren.
Minimal.
Boring.
Reproduzierbar.

Wenn etwas nicht klar ist:
zurück zu Context/Plan.

## 5 Review

Kurz prüfen:

- Passt das zum Intent?
- Haben wir unbeabsichtigt Komplexität eingebaut?
- Ist es verständlich?
- Braucht es eine Decision (Trade-offs)?
- Fehlt Dokumentation?

Review ist kein Roman.
Es ist ein Gate.

## 6 Decide

Jetzt wird es verbindlich:

- Entscheidung akzeptieren
- Entscheidung verwerfen
- Entscheidung ersetzen (supersede)
- oder als “proposed” stehen lassen

Wenn Trade-offs:
ADR.

Wenn nicht:
Worklog reicht.

## 7 Log

Mindestens ein kurzer Eintrag in:
- Worklog (immer)
- Decisions (wenn Trade-offs)
- Prompts (wenn KI involviert)

Log ist der Preis für Nachvollziehbarkeit.

## 8 Repeat

Nächster Schritt wird wieder klein gemacht.

Der Loop ist endlos.
Das ist gewollt.

---

# Quality Gates (die harten Fragen)

Diese Fragen sind absichtlich unbequem.

1. Was ist das absolut Nötigste, um diesen Schritt zum Laufen zu bringen?
2. Welche Features können weg und später rein?
3. Wie kann ich das in 2 Wochen testen?
4. Wofür investiere ich gerade zu viel Zeit, ohne direkten Mehrwert?

Wenn du bei Frage 4 rot wirst:
zurück zu “Plan”.

---

# Mermaid: PDD Loop (High Level)

```mermaid
flowchart TD
  I[Intent] --> C[Context]
  C --> P[Plan 1 - 2h task]
  P --> B[Build]
  B --> R[Review Quality Gate]
  R -->|OK| D[Decide]
  R -->|Not OK| P
  D --> L[Log]
  L --> I
````

---

# Mermaid: Artefakt-Fluss (Repo)

```mermaid
flowchart LR
  Intent --> Worklog
  Context --> Worklog

  Plan --> Prompts
  Prompts --> Build

  Build --> Code[Code / Docs]
  Review --> Decisions

  Decisions --> Code
  Code --> Worklog
  Decisions --> Worklog

  Worklog --> Next[Next step]
  Next --> Intent
```

---

# Minimaler Loop (wenn du nur 15 Minuten hast)

1. Intent als ein Satz notieren
2. Plan: genau ein nächster Schritt (max. 15 min)
3. Build: kleinster Commit
4. Log: 5 Zeilen Worklog

Fertig.

---

# Typische Anti-Patterns

## “LLM hat gesagt, passt schon”

Kein Review.
Keine Decision.
Keine Trace.

Ergebnis:
Später niemand weiß, warum es so ist.

## “Wir machen erst mal alles perfekt”

Überarbeitung ohne Intent.
Zeitverlust ohne Nutzen.

## “Wir bauen jetzt das Framework”

Wenn du merkst, dass du eine Plattform baust:
Stop.
Zurück zu Plan.
Kleiner.

---

# Praktische Konventionen

* Jeder PR / Commit soll mindestens ein Artefakt aktualisieren:

    * Worklog oder Decision oder Prompt
* ADRs nur für echte Trade-offs.
* Worklog immer kurz.
* Prompts sind versioniert.

---

# Ende

Der Loop ist kein Dogma.

Er ist eine Leitplanke,
damit Geschwindigkeit nicht in Beliebigkeit kippt.