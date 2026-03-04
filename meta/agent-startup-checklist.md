# Agent Startup Checklist

Dieses Dokument beschreibt die Schritte, die ein KI-Agent ausführen soll,
bevor er Änderungen am Repository vornimmt.

Der Zweck dieser Checkliste ist Alignment.

Ein Agent soll zuerst verstehen:

- was dieses Repository ist
- wie hier gearbeitet wird
- welche Regeln gelten

Erst danach darf implementiert werden.

---

# Step 1 — Projekt verstehen

Lies folgende Dokumente vollständig:

```

/meta/project-intent.md
/meta/workflow.md
/meta/pdd-loop.md
/meta/agent-contract.md
/meta/agent-roles.md

```

Ziel:

Verstehen

- was das Projekt erreichen will
- wie gearbeitet wird
- welche Prinzipien gelten

Wenn etwas unklar ist → zuerst analysieren, nicht implementieren.

---

# Step 2 — Repository-Struktur analysieren

Untersuche die Hauptverzeichnisse:

```

/meta
/worklog
/decisions
/prompts
/docs
/scripts
/templates

```

Verstehe die Rolle jedes Bereichs.

Der Agent soll erkennen:

- welche Artefakte existieren
- welche Artefakte fehlen
- welche Artefakte aktualisiert werden müssen

---

# Step 3 — Aktuellen Stand ermitteln

Der Agent soll prüfen:

- letzten Worklog-Eintrag
- vorhandene ADRs
- letzte Prompts

Fragen:

- Was wurde zuletzt entschieden?
- Was ist der nächste Schritt?
- Gibt es offene Fragen?

---

# Step 4 — Rolle definieren

Der Agent muss entscheiden, in welcher Rolle er arbeitet.

Beispiele:

```

Analyst
Architect
Generator
Reviewer
Archivist

```

Die Rolle bestimmt:

- welche Aufgaben erlaubt sind
- welche Aufgaben nicht erlaubt sind

---

# Step 5 — Aufgabe verstehen

Der Agent soll sicherstellen:

- die Aufgabe ist klar
- die Aufgabe ist klein genug (1–2 Stunden)
- die Aufgabe passt zum Projekt-Intent

Wenn eine Aufgabe zu groß ist:

→ in kleinere Schritte zerlegen.

---

# Step 6 — Workflow prüfen

Vor jeder Implementierung prüfen:

```

Intent → Context → Plan → Build → Review → Log

```

Der Agent darf keine Schritte überspringen.

---

# Step 7 — Artefakte vorbereiten

Vor Änderungen prüfen:

- Muss der Worklog aktualisiert werden?
- Wird eine Decision (ADR) benötigt?
- Muss ein Prompt archiviert werden?

Wenn ja → vorbereiten.

---

# Step 8 — Implementierung

Jetzt erst darf implementiert werden.

Implementierung soll:

- minimal sein
- reproduzierbar sein
- verständlich sein

Keine unnötige Komplexität.

---

# Step 9 — Review

Nach der Implementierung prüfen:

- passt das zum Intent des Projekts?
- verletzt es KISS oder YAGNI?
- fehlt Dokumentation?

---

# Step 10 — Log

Zum Abschluss:

- Worklog aktualisieren
- ggf. Decision erstellen
- Prompt archivieren

Der Prozess muss nachvollziehbar bleiben.

---

# Abbruchbedingungen

Der Agent soll stoppen wenn:

- Kontext unklar ist
- Entscheidungen fehlen
- Aufgabe zu groß ist
- Workflow verletzt würde

In diesem Fall:

Analyse liefern statt Implementation.

---

# Kurzfassung

Der Agent soll zuerst verstehen,
dann planen,
dann bauen,
und zuletzt dokumentieren.

Nicht umgekehrt.
