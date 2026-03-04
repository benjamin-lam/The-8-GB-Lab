# Agent Roles

Dieses Dokument beschreibt die Rollen, die ein KI-Agent in diesem Repository übernehmen kann.

Ein Agent arbeitet immer **in genau einer Rolle zurzeit**.

Rollen definieren:
- Verantwortlichkeiten
- Grenzen
- erwartete Ergebnisse

Sie helfen dabei, Denkprozesse zu strukturieren.

---

# Überblick

| Rolle     | Zweck                                             |
|-----------|---------------------------------------------------|
| Architect | Kontext verstehen und Entscheidungen vorbereiten  |
| Generator | Inhalte oder Code erzeugen                        |
| Reviewer  | Qualität prüfen                                   |
| Archivist | Dokumentation und Artefakte pflegen               |
| Analyst   | Repository analysieren und Zusammenhänge erklären |

Diese Rollen können von Menschen oder KI übernommen werden.

---

# Architect

Der Architect arbeitet auf der **Konzept- und Entscheidungsebene**.

Aufgaben:

- Kontext analysieren
- Trade-offs sichtbar machen
- Entscheidungen vorbereiten
- Architektur erklären

Der Architect schreibt normalerweise **keinen Code**.

Typische Outputs:

- ADR-Vorschläge
- Architekturübersichten
- Systemerklärungen

---

# Generator

Der Generator erzeugt konkrete Artefakte.

Das können sein:

- Code
- Markdown Inhalte
- Templates
- kleine Skripte

Der Generator arbeitet immer auf Basis von:

- vorhandenen Decisions
- Worklog Kontext
- klaren Aufgaben

Der Generator soll **keine Architekturentscheidungen treffen**.

---

# Reviewer

Der Reviewer prüft Ergebnisse.

Aufgaben:

- Qualität prüfen
- Inkonsistenzen finden
- unnötige Komplexität erkennen
- Alignment mit Workflow sicherstellen

Typische Fragen eines Reviewers:

- Passt das zum Intent des Projekts?
- Verstößt es gegen KISS oder YAGNI?
- Fehlt Dokumentation?

Der Reviewer erzeugt **keinen neuen Code**.

---

# Archivist

Der Archivist kümmert sich um **Ordnung und Nachvollziehbarkeit**.

Aufgaben:

- Worklog aktualisieren
- Prompts archivieren
- Decisions referenzieren
- Dokumentation strukturieren

Der Archivist verändert **keine Architektur oder Funktionalität**.

---

# Analyst

Der Analyst betrachtet das Repository als Ganzes.

Aufgaben:

- Struktur erklären
- Zusammenhänge sichtbar machen
- Risiken identifizieren
- Verbesserungen vorschlagen

Der Analyst implementiert **nichts**.

---

# Typischer Arbeitsfluss

Ein sinnvoller Ablauf kann so aussehen:

```

Analyst → Architect → Generator → Reviewer → Archivist

```

Beispiel:

1. Analyst erklärt aktuellen Zustand des Repositories
2. Architect schlägt eine Entscheidung vor
3. Generator implementiert einen kleinen Schritt
4. Reviewer prüft Ergebnis
5. Archivist aktualisiert Worklog / Prompts / Decisions

---

# Rollenwechsel

Ein Agent kann Rollen wechseln.

Der Wechsel sollte **explizit passieren**.

Beispiel:

```

Act as Reviewer

```

oder

```

Switch role to Architect

```

---

# Warum Rollen wichtig sind

Ohne Rollen versuchen KI-Systeme oft:

- gleichzeitig zu analysieren
- zu entscheiden
- zu implementieren
- zu dokumentieren

Das führt zu unklaren Ergebnissen.

Rollen trennen diese Aufgaben.

---

# Kurzfassung

Rollen helfen dabei:

- Denken zu strukturieren
- Verantwortung zu trennen
- KI gezielter einzusetzen

