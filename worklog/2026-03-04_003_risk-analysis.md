# Worklog 2026-03-04_003 — Risk Analysis: AI Misunderstandings

## Context

Dritter Alignment-Prompt ausgeführt.
Aufgabe: Potenzielle Missverständnisse analysieren, die ein AI Coding Assistant über dieses Repository haben könnte.

Ziel: Risiken identifizieren und Präventionsmaßnahmen definieren.

## Decision

Risikoanalyse durchgeführt.
Keine Implementierung.

Vier Kategorien von Missverständnissen untersucht:
1. Was könnte missverstanden werden?
2. Was könnte als Framework fehlinterpretiert werden?
3. Welche Workflow-Schritte könnten übersprungen werden?
4. Welche Arten von Overengineering sind wahrscheinlich?

## Why

Gemäß Agent-Startup-Checklist:
- Abbruchbedingungen verstehen
- "Analyse liefern statt Implementation" wenn unklar

Präventiv: Bevor erste produktive Aufgabe, mögliche Fehlerquellen identifizieren.

## Result

### 1. Typische Missverständnisse eines AI Coding Assistant

#### Missverständnis 1: "Das ist ein Software-Projekt"
**Was AI denkt**: "Ich soll hier Software bauen."
**Realität**: Dies ist ein dokumentationsgetriebenes Projekt, das ein System ERKLÄRT.

**Symptome**:
- AI schlägt komplexe Architekturen vor
- AI will Tests, CI/CD, Package-Management einführen
- AI fokussiert auf Code statt auf Dokumentation

**Prävention**:
- Immer `/meta/project-intent.md` lesen vor erstem Task
- Bei jedem Prompt explizit: "Kein Framework, nur Erklärung"
- Code nur als Werkzeug, nicht als Ziel

#### Missverständnis 2: "Schnelligkeit ist wichtig"
**Was AI denkt**: "Ich muss schnell Output liefern."
**Realität**: Nachvollziehbarkeit > Geschwindigkeit

**Symptome**:
- AI überspringt Worklog-Updates
- AI erstellt keine ADRs bei Trade-offs
- AI liefert Code ohne Context/Why/Next

**Prävention**:
- PDD Loop ist NICHT optional
- Jeder Output MUSS im Worklog dokumentiert werden
- Langsam und nachvollziehbar > schnell und opak

#### Missverständnis 3: "Ich soll optimieren"
**Was AI denkt**: "Ich verbessere existierenden Code."
**Realität**: YAGNI - Nur was JETZT gebraucht wird.

**Symptome**:
- AI refactored ohne Intent
- AI fügt "best practices" hinzu, die niemand verlangt hat
- AI schlägt Features vor, die "später nützlich sein könnten"

**Prävention**:
- Immer fragen: "Was ist das absolut Nötigste?"
- KISS/YAGNI Quality Gates explizit prüfen
- Keine Änderung ohne Intent

#### Missverständnis 4: "Worklog ist optional"
**Was AI denkt**: "Dokumentation kann ich später machen."
**Realität**: Worklog ist der KERN des Projekts.

**Symptome**:
- AI macht Commits ohne Worklog-Update
- AI sagt "Das kann später dokumentiert werden"
- AI überspringt den "Log"-Schritt im Loop

**Prävention**:
- Definition of Done IMMER prüfen:
  - Code funktioniert ✓
  - **Worklog aktualisiert** ✓
  - Relevante Entscheidungen dokumentiert ✓
  - Dateien verständlich ✓

---

### 2. Was könnte als Framework fehlinterpretiert werden?

#### Risiko-Zone 1: `/scripts/` Verzeichnis
**Fehlinterpretation**: "Das ist ein Tool-Projekt, ich baue Frameworks."
**Realität**: Scripts sind Hilfsmittel, keine Produkte.

**Wie es passiert**:
- AI sieht `build.py` und denkt "Ich baue ein Build-System"
- AI fügt Features hinzu: Plugins, Config-Files, CLI-Framework
- AI schlägt vor: "Lass uns das auf PyPI publishen"

**Wie man es vermeidet**:
- Scripts bleiben BORING
- Keine Abstraktion ohne konkreten Bedarf
- Skripte dürfen "bad code" sein, wenn sie funktionieren
- Kein "Framework-Denken"

#### Risiko-Zone 2: `/templates/` Verzeichnis
**Fehlinterpretation**: "Das ist ein Template-Engine-Projekt."
**Realität**: Templates sind Beispiele, keine Spezifikation.

**Wie es passiert**:
- AI sieht Templates und denkt "Ich brauche Jinja2/Mustache/etc."
- AI baut Templating-System mit Variablen, Conditionals, Loops
- AI schlägt vor: "Lass uns das generisch machen"

**Wie man es vermeidet**:
- Templates bleiben einfache Markdown-Dateien
- Keine Template-Language
- Copy-Paste ist OK

#### Risiko-Zone 3: `/meta/` Verzeichnis
**Fehlinterpretation**: "Das sind Spezifikationen für ein Framework."
**Realität**: Das sind Arbeitsregeln für DIESES Repository.

**Wie es passiert**:
- AI denkt: "/meta/ = Metaprogramming"
- AI schlägt vor: "Lass uns daraus ein Tool machen"
- AI will `/meta/` in Code transformieren

**Wie man es vermeidet**:
- `/meta/` ist Prosa für Menschen (und AI-Agents)
- Nicht in Code transformieren
- Nicht "formal" machen

---

### 3. Workflow-Schritte, die übersprungen werden könnten

#### Übersprungener Schritt 1: CONTEXT
**Was passiert**: AI springt direkt zu Plan/Build.
**Warum gefährlich**: Decisions werden ignoriert, Doppelarbeit, Inkonsistenz.

**Symptome**:
- "Ich implementiere Feature X" ohne zu prüfen, ob es bereits existiert
- "Ich erstelle ADR Y" ohne vorhandene ADRs zu lesen
- "Ich baue Tool Z" ohne zu prüfen, ob es dem Intent widerspricht

**Prävention**:
```
Vor jedem Build:
1. Lies /meta/
2. Lies relevante /decisions/
3. Lies letzten /worklog/ Eintrag
4. Frage: "Was ist der Stand?"
```

#### Übersprungener Schritt 2: REVIEW
**Was passiert**: AI baut, dann direkt Log.
**Warum gefährlich**: Keine Quality Gates, Komplexität schleicht sich ein.

**Symptome**:
- Code funktioniert, aber verletzt KISS/YAGNI
- Keine Frage: "Braucht es eine Decision?"
- Keine Frage: "Passt das zum Intent?"

**Prävention**:
```
Nach jedem Build:
1. Passt das zum Intent? ✓
2. Unbeabsichtigte Komplexität? ✓
3. Verständlich? ✓
4. Braucht es ADR? ✓
5. Fehlt Dokumentation? ✓
```

#### Übersprungener Schritt 3: DECIDE
**Was passiert**: AI macht Build, aber dokumentiert Trade-offs nicht.
**Warum gefährlich**: Spätere Frage "Warum ist das so?" hat keine Antwort.

**Symptome**:
- Technologie-Wahl ohne ADR
- Architektur-Änderung nur im Worklog
- Trade-offs werden nicht explizit gemacht

**Prävention**:
```
Wenn Trade-offs existieren:
→ ADR erstellen (nicht optional)
→ Im Worklog referenzieren
→ Status setzen (proposed/accepted/etc.)
```

#### Übersprungener Schritt 4: LOG
**Was passiert**: AI denkt "Git Commit = genug Dokumentation".
**Warum gefährlich**: Repository verliert Nachvollziehbarkeit.

**Symptome**:
- Commit ohne Worklog-Update
- "Ich update das später"
- Nur technische Änderungen, kein Context/Why/Next

**Prävention**:
```
Definition of Done ist HARD:
- Worklog aktualisiert (nicht optional)
- Context/Decision/Why/Result/Next ausgefüllt
- Prompts archiviert wenn AI involviert
```

---

### 4. Arten von Overengineering, die AI einführen könnte

#### Overengineering 1: Premature Abstraction
**Was AI macht**: "Ich mache das generisch für zukünftige Use Cases."

**Beispiele**:
- Build-Script mit Plugin-System (obwohl nur ein Use Case existiert)
- Template-Engine mit Variablen (obwohl nur 3 Dateien existieren)
- Config-System mit YAML/JSON (obwohl Hardcoding reicht)

**Warum gefährlich**:
- Komplexität steigt exponentiell
- Niemand versteht es in 6 Monaten
- Widerspricht YAGNI

**Prävention**:
- Quality Gate 2: "Welche Features können weg und später rein?"
- Regel: Erst 3 konkrete Use Cases, DANN abstrahieren
- Boring code is good code

#### Overengineering 2: Framework-Thinking
**Was AI macht**: "Ich baue das so, dass andere es auch nutzen können."

**Beispiele**:
- Versioned API für internes Script
- Dependency Injection für 2 Funktionen
- "Separation of Concerns" obwohl 100 LOC
- Tests für Scripts, die einmal laufen

**Warum gefährlich**:
- Repository wird kompliziert statt verständlich
- Fokus verschiebt sich von "Erklären" zu "Bauen"
- Widerspricht Project Intent

**Prävention**:
- Frage: "Wer ist der User?" → Antwort: "Dieses Repository"
- Frage: "Wird das publiziert?" → Antwort: "Nein"
- Frage: "Braucht das eine API?" → Antwort: "Nein"

#### Overengineering 3: Best-Practice Overkill
**Was AI macht**: "Ich implementiere alle Best Practices."

**Beispiele**:
- Linting, Formatting, Pre-Commit Hooks
- CI/CD Pipeline für statische Website
- Docker für Markdown-zu-HTML Conversion
- Type Hints für 50 LOC Script
- Unit Tests für Glue Code

**Warum gefährlich**:
- Setup-Overhead > Nutzen
- Komplexität schreckt ab
- "Best Practices" sind kontextabhängig

**Prävention**:
- Quality Gate 4: "Wofür investiere ich gerade zu viel Zeit?"
- Regel: Erst Problem haben, DANN Best Practice
- Einfachheit > Perfektion

#### Overengineering 4: Tooling Proliferation
**Was AI macht**: "Ich integriere moderne Tools."

**Beispiele**:
- 15 NPM Dependencies für statische Website
- Poetry + Pipenv + Virtualenv gleichzeitig
- Make + Invoke + Taskfile gleichzeitig
- GitHub Actions + GitLab CI + Travis gleichzeitig

**Warum gefährlich**:
- Dependency Hell
- Niemand kann das Projekt mehr klonen und starten
- Wartungsaufwand explodiert

**Prävention**:
- Regel: Minimale Dependencies
- Regel: Standard Library > externe Library
- Regel: Boring Technology Wins

---

### 5. Wie man diese Fehler VERMEIDET

#### Strategie 1: Loop als Hard Gate
```
BEFORE Build:
❌ Context gelesen?
❌ Intent formuliert?
❌ Plan klein genug (1-2h)?

→ Wenn NEIN, zurück zu Context

AFTER Build:
❌ Review durchgeführt?
❌ Trade-offs dokumentiert?
❌ Worklog updated?

→ Wenn NEIN, Build ist NICHT fertig
```

#### Strategie 2: Explizite Checkfragen
```
Vor jedem Commit:
1. Warum mache ich das? (Intent)
2. Was ist der Stand? (Context)
3. Ist das der kleinste Schritt? (Plan)
4. Ist das minimal? (Build)
5. Verletzt das KISS/YAGNI? (Review)
6. Gibt es Trade-offs? (Decide)
7. Ist das im Worklog? (Log)
```

#### Strategie 3: Anti-Pattern Detection
```
Wenn AI sagt:
"Lass uns das generisch machen" → STOP
"Das könnte später nützlich sein" → STOP
"Best Practice wäre..." → STOP
"Ich füge das schnell hinzu" → STOP
"Das dokumentieren wir später" → STOP

→ Zurück zu Quality Gates
```

#### Strategie 4: Worklog-First Development
```
Workflow:
1. Worklog Eintrag STARTEN (Context/Decision/Why)
2. Build machen
3. Worklog Eintrag BEENDEN (Result/Next)
4. Commit

NICHT:
1. Build machen
2. Commit
3. Worklog "wenn Zeit ist"
```

#### Strategie 5: Pair mit Mensch
```
Bei Unsicherheit:
→ STOP
→ Analyse liefern statt Implementation
→ Mensch entscheidet

Abbruchbedingungen:
- Kontext unklar
- Entscheidungen fehlen
- Aufgabe zu groß
- Workflow würde verletzt

→ In diesem Fall: Lieber fragen als raten
```

---

### 6. Checkliste: Bin ich auf dem richtigen Weg?

✅ **Gute Zeichen**:
- Ich habe Context gelesen
- Mein Plan ist klein (1-2h)
- Ich frage: "Was ist das Nötigste?"
- Ich dokumentiere BEVOR ich committe
- Ich erstelle ADR bei Trade-offs
- Ich kann erklären: Warum mache ich das?

❌ **Schlechte Zeichen**:
- Ich "verbessere" ohne Intent
- Ich denke: "Das könnte später nützlich sein"
- Ich überspringe Worklog-Update
- Ich baue Framework statt Tool
- Ich füge Dependencies hinzu ohne Grund
- Ich kann nicht erklären: Warum mache ich das?

---

### 7. TL;DR — Die wichtigsten Faustregeln

1. **Dies ist KEIN Software-Projekt**
   → Dokumentation > Code

2. **Nachvollziehbarkeit > Geschwindigkeit**
   → Langsam und dokumentiert > schnell und opak

3. **YAGNI ist LAW**
   → Nur bauen was JETZT gebraucht wird

4. **Worklog ist NICHT optional**
   → Kein Commit ohne Worklog

5. **Loop ist HARD GATE**
   → Keine Schritte überspringen

6. **Boring > Clever**
   → Einfacher schlechter Code > komplexer guter Code

7. **Frag im Zweifel**
   → Analyse liefern statt raten

---

## Next

Risk Analysis abgeschlossen.

Agent ist sich jetzt bewusst:
- Welche Fehler typischerweise passieren
- Wie man sie erkennt
- Wie man sie vermeidet

Bereit für produktive Arbeit mit:
- Verstärktem Fokus auf Loop-Compliance
- Expliziter Prüfung von Quality Gates
- Worklog-First Mindset
- Anti-Pattern Detection aktiviert

Bei nächster Aufgabe:
- Checkfragen vor Build
- Checkfragen nach Build
- Im Zweifel: STOP und fragen

---

**Agent**: GitHub Copilot
**Datum**: 2026-03-04
**Phase**: Alignment — Risk Analysis
**Prompt**: `prompts/alignment/2026-03-04_002_risk-analysis.md`