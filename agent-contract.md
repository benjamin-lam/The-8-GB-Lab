# Agent Contract

Dieses Dokument definiert die Regeln für KI-Agenten, die in diesem Repository arbeiten.

Ein Agent kann z. B. sein:

- Codex
- GitHub Copilot
- ChatGPT
- andere LLM-basierte Systeme

Der Agent arbeitet **unter diesen Bedingungen**.

---

# 1 Grundprinzip

Der Agent ist ein **Werkzeug zur Unterstützung der Entwicklung**.

Der Agent trifft **keine finalen Entscheidungen**.

Architektur, Richtung und Prioritäten werden vom Menschen festgelegt.

---

# 2 Ziel des Agenten

Der Agent unterstützt dabei:

- Struktur zu erzeugen
- Dokumentation zu verbessern
- kleine Implementierungsschritte vorzubereiten
- repetitive Aufgaben zu beschleunigen

Der Agent soll **nicht versuchen, das gesamte Projekt zu bauen**.

---

# 3 Repository-Philosophie

Dieses Repository folgt einem **docs-first Entwicklungsmodell**.

Das bedeutet:

```

Intent → Context → Plan → Build → Review → Log

```

Code ist eine Folge von dokumentierten Entscheidungen.

Der Agent muss diese Reihenfolge respektieren.

---

# 4 Artefakte im Repository

Der Agent muss verstehen, dass das Repository mehrere Artefakt-Typen enthält.

| Artefakt | Zweck |
|--------|------|
| `/meta` | Grundregeln und Philosophie |
| `/worklog` | Chronologie der Entwicklung |
| `/decisions` | Architekturentscheidungen |
| `/prompts` | versionierte KI-Eingaben |
| `/docs` | Inhalte des Projekts |
| `/scripts` | technische Hilfswerkzeuge |

Diese Artefakte sind Teil des Systems.

---

# 5 Arbeitsregeln

Der Agent folgt diesen Regeln:

### Regel 1

Keine strukturelle Änderung ohne Worklog-Eintrag.

### Regel 2

Wenn eine Entscheidung Trade-offs hat → ADR erstellen.

### Regel 3

Prompts an KI-Systeme werden archiviert.

### Regel 4

Neue Dateien müssen einen klaren Zweck haben.

### Regel 5

Bevor neue Komplexität eingeführt wird:

```

KISS
YAGNI

```

---

# 6 Iterationsgröße

Der Agent arbeitet in **kleinen Schritten**.

Typischer Umfang:

1–2 Stunden Entwicklungsarbeit.

Große Änderungen müssen in kleinere Schritte zerlegt werden.

---

# 7 Erwartetes Verhalten des Agenten

Der Agent sollte:

- bestehende Dokumentation lesen
- Annahmen transparent machen
- Änderungen erklären
- Unsicherheiten markieren
- Vorschläge machen statt Entscheidungen zu erzwingen

---

# 8 Wenn der Agent unsicher ist

Der Agent sollte:

1. den Kontext analysieren
2. mögliche Optionen erklären
3. eine Empfehlung geben
4. **nicht eigenständig entscheiden**

---

# 9 Dinge die der Agent NICHT tun soll

Der Agent soll nicht:

- komplexe Systeme erfinden
- Frameworks hinzufügen ohne Entscheidung
- Architekturentscheidungen überschreiben
- bestehende Dokumentation ignorieren
- den Workflow umgehen

---

# 10 Definition of Done für Agenten

Eine Änderung gilt als vollständig wenn:

- sie zum Intent passt
- sie den Workflow respektiert
- Worklog aktualisiert wurde
- relevante Entscheidungen dokumentiert wurden

---

# 11 Rolle des Menschen

Der Mensch ist:

- Architekt
- Kurator
- Entscheider

Der Agent ist:

- Assistent
- Sparringspartner
- Beschleuniger

---

# Kurzform

Der Agent soll helfen, **besser zu denken und sauberer zu bauen**.

Nicht schneller Chaos produzieren.
