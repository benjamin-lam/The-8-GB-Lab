# Repository Workflow

Dieses Repository folgt einem **docs-first Entwicklungsmodell**.

Ziel ist nicht nur Software zu bauen, sondern Entscheidungen, Annahmen und Iterationen nachvollziehbar zu dokumentieren.

Code ist ein Ergebnis dieses Prozesses – nicht sein Ausgangspunkt.

---

# Core Prinzipien

1. **Docs first**
2. **Decisions before complexity**
3. **Small iterations**
4. **Reproducible steps**
5. **No change without trace**

---

# Die vier Artefakte des Projekts

Das Repository kennt vier zentrale Artefakt-Typen.

| Artefakt        | Zweck                       |
|-----------------|-----------------------------|
| Worklog         | Chronologie der Entwicklung |
| Decisions (ADR) | Architekturentscheidungen   |
| Prompts         | Eingaben an KI-Systeme      |
| Code / Docs     | Umsetzung und Inhalte       |

Diese Artefakte ergänzen sich.

---

# 1 Worklog

Ort: `/worklog/`

Der Worklog dokumentiert den Verlauf der Entwicklung.

Eine Datei pro Tag.

Format:

```

Context
Decision
Why
Result
Next

```

Der Worklog ist **kurz und ehrlich**.

Er beantwortet:
- Was ist passiert?
- Warum wurde etwas entschieden?
- Was kommt als nächstes?

---

# 2 Decisions (ADR)

Ort: `/decisions/`

Architecture Decision Records dokumentieren **dauerhafte Entscheidungen**.

Beispiele:

- Wahl der Architektur
- Workflow-Regeln
- Build-System
- Technologieentscheidungen

ADRs werden erstellt wenn:

- eine Entscheidung Trade-offs hat
- eine Entscheidung langfristig relevant ist
- jemand später fragen könnte: „Warum ist das so?“

---

# 3 Prompts

Ort: `/prompts/`

Prompts sind **Input-Artefakte**.

Sie dokumentieren:

- welche Aufgaben an KI-Systeme gegeben wurden
- welche Annahmen im Prompt steckten
- welche Ergebnisse erwartet wurden

Dateiname:

```

YYYY-MM-DD_NNN_topic.md

```

---

# 4 Code und Inhalte

Ort: `/docs`, `/scripts`, `/templates` usw.

Code entsteht als Folge von:

- Decisions
- Worklog
- Prompts

Nicht umgekehrt.

---

# Standard Entwicklungszyklus

Jede Änderung folgt idealerweise diesem Ablauf:

```

Idea
↓
Decision (falls nötig)
↓
Prompt / Task
↓
Implementation
↓
Worklog Update

```

Oder als Kurzform:

```

Think → Decide → Build → Log

```

---

# Regeln für Menschen und KI

Diese Regeln gelten für alle Mitwirkenden – auch für KI-Systeme.

### Rule 1

Keine strukturelle Änderung ohne Worklog-Eintrag.

### Rule 2

Wenn eine Entscheidung Trade-offs hat → ADR erstellen.

### Rule 3

Prompts an KI-Systeme werden archiviert.

### Rule 4

Neue Dateien brauchen eine kurze Erklärung ihres Zwecks.

### Rule 5

Bevor Komplexität hinzugefügt wird, prüfen:

```

KISS
YAGNI

```

---

# Definition of Done

Eine Änderung gilt als abgeschlossen wenn:

- Code funktioniert
- Worklog aktualisiert wurde
- relevante Entscheidungen dokumentiert sind
- Dateien verständlich sind

---

# Ziel dieses Systems

Dieses Repository soll zeigen:

Softwareentwicklung ist kein Blackbox-Prozess.

Sie ist eine Folge von:

- Entscheidungen
- Experimenten
- Iterationen

Der Code ist nur der sichtbare Teil davon.