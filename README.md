# 🔬 The 8‑GB Lab  
### Prompt Driven Development (PDD) auf minimalen Ressourcen  

> „The documentation is the product. The code is only the proof."  

Dieses Repository ist ein Experiment: Wie weit kommt man mit **Vibe Coding** und **Prompt Driven Development**, wenn man Hardware‑Constraints (8 GB RAM) als kreative Leitplanken nutzt – und systematisches Denken über schnelles Hacken stellt?

Hier entsteht kein weiteres High‑End‑Tool für eine kleine Elite. Hier entsteht ein **Denkmuster**: eine lokal lauffähige, nachvollziehbare Alternative zu Vendor‑Lock‑In, monatlichen API‑Kosten und KI‑Abhängigkeit.

---

## 🧠 Core Philosophy: Alignment First  

Bevor eine Zeile Code generiert wird, muss die KI beweisen, dass sie das System **verstanden** hat. Wir nutzen ein striktes **Alignment‑Protokoll**, um sicherzustellen, dass die KI nicht „einfach drauflos generiert", sondern die Rollen, Constraints und das Low‑Resource‑Mindset verinnerlicht hat.

### Der Workflow  

1. **Context Ingestion**  
   Die KI liest die Ordner `/meta` (die „Verfassung" des Projekts) und `/pdd` (Definitionen von Rollen, Constraints und Prompt‑Templates).  

2. **Alignment Check**  
   Die KI erklärt das System in eigenen Worten (siehe `prompts/alignment`). Dabei muss sie zeigen, dass sie Rollen, Ziele und die Low‑Resource‑Philosophie verinnerlicht hat.  

3. **Reality Check**  
   Validierung gegen **KISS** (Keep It Simple, Stupid) und **YAGNI** (You Ain't Gonna Need It). Nur wenn der Plan diesen Prinzipien standhält, wird er freigegeben.  

4. **Execution**  
   Erst jetzt erfolgt die Code‑Generierung – und zwar streng nach dem freigegebenen Plan.  

Jeder Schritt wird dokumentiert. Die **Dokumentation ist das eigentliche Produkt**; der Code ist nur der Beleg, dass die Idee funktioniert.  

---

## 🏗️ System‑Architektur (Baseline)  

Wir bauen einen ressourcenschonenden **Meta‑Workflow**, der selbst auf einem Rechner mit 8 GB RAM flüssig läuft. Dieser Workflow orchestriert die Entwicklung des eigentlichen Zielsystems (des „Produkts").

| Komponente               | Low‑Resource‑Entscheidung                                                                 | Warum?                                                                                                    |
|--------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Orchestrator**         | [FastAPI](https://fastapi.tiangolo.com/) – asynchron, leichtgewichtig                      | Minimaler RAM‑Footprint, perfekt für den zentralen Steuerungsdienst.                                     |
| **Retriever**            | **SQLite FTS5** über Markdown‑Dateien in `knowledge_base/`                                | Keine Vektordatenbank, keine Embedding‑Modelle – nur Volltextsuche. Spart Gigabytes an RAM.             |
| **Generator**            | [Ollama](https://ollama.com/) mit `phi3:mini` (3,8 B Parameter)                           | Läuft erfahrungsgemäß in 8 GB RAM, liefert gute Reasoning‑Qualität. Wechsel zu größeren Modellen möglich.|
| **Reviewer**             | **Regelbasiert** (Python‑Syntax, verbotene Muster, Pflichtfunktionen)                     | Kein zweites LLM nötig – spart RAM und macht das Verhalten transparent. Kann später erweitert werden.    |
| **Evolution‑Log**        | SQLite‑Datenbank mit Metriken (Latenzen, Iterationen, RAM‑Verbrauch)                      | Ermöglicht fundierte Entscheidungen: Wann lohnt sich ein Upgrade? Wo sind Flaschenhälse?                 |

Der Ablauf im Überblick:  

1. User sendet Prompt an `/orchestrate`.  
2. Orchestrator holt per Volltextsuche relevanten Kontext aus `knowledge_base/`.  
3. Er baut einen finalen Prompt (User‑Prompt + Kontext + Guidelines).  
4. Generator (Ollama) erzeugt einen Entwurf.  
5. Regelbasierter Reviewer prüft den Entwurf.  
6. Bei negativem Review folgt eine Iteration (max. 3) mit verbessertem Prompt.  
7. Metriken werden in SQLite geloggt.  
8. Antwort wird an User zurückgegeben.  

---

## 📂 Repository‑Struktur  

Die Struktur spiegelt die Philosophie wider: Ordnung, Transparenz und klare Trennung von Konzept und Implementierung.  

```
📦 The-8GB-Lab
│
├── /meta                   # 🧭 Die "Verfassung" des Projekts
│   ��── agent-startup-checklist.md    # Checkliste für KI-Agents beim Start
│   ├── pdd-loop.md                   # Der iterative PDD-Entwicklungszyklus
│   ├── pdd-map.md                    # Übersicht: Was ist PDD?
│   ├── project-intent.md             # Warum existiert dieses Projekt?
│   └── workflow.md                   # Der strukturierte Arbeitsablauf
│
├── /pdd                    # 📋 PDD-Konfiguration (Actors, Constraints, Templates)
│   ├── actors.yaml                   # Definition der Agent-Rollen
│   ├── constraints.yaml              # Globale und artefakt-spezifische Regeln
│   └── prompt_template.md            # Strukturiertes Prompt-Template
│
├── /app                    # 🚀 FastAPI-Anwendungslogik (Orchestrator-Endpunkte)
│   ├── __init__.py
│   ├── main.py                       # FastAPI Entry Point
│   └── routes.py                     # API-Endpunkte (/orchestrate, /health, etc.)
│
├── /lib                    # ⚙️ Core-Module (die Kern-Logik des Systems)
│   ├── /generator
│   │   ├── dummy.py                  # Baseline-Generator (deterministisch)
│   │   └── ollama.py                 # Ollama-Adapter (LLM-Integration)
│   ├── /retrieval
│   │   ├── db.py                     # SQLite-Verbindungslogik
│   │   ├── indexer.py                # FTS5-Indexierung der Knowledge Base
│   │   └── retriever.py              # Volltextsuche mit BM25-Ranking
│   ├── /review
│   │   └── rules.py                  # Regelbasierte Code-Validierung
│   ├── /metrics
│   │   └── runtime.py                # Performance-Metriken (Zeit, RAM)
│   ├── /log
│   │   ├── evolution.py              # Evolution-Log (SQLite-Persistenz)
│   │   └── memory.py                 # Ähnliche frühere Runs finden
│   └── /pdd
│       ├── config.py                 # Laden von actors.yaml, constraints.yaml
│       └── prompt_compiler.py        # Zusammenstellung finaler Prompts
│
├── /knowledge_base         # 📚 Kontext-Dokumente für RAG (als Markdown)
│   ├── README.md                     # Anleitung zur Knowledge Base
│   └── pdd_principles.md             # PDD-Grundprinzipien (Kurz)
│
├── /scripts                # 🛠️ Utilities (Indexierung, Setup-Helfer)
│   └── index_kb.py                   # Indexiert Markdown-Dateien in SQLite FTS5
│
├── /worklog                # 📓 Laufendes Log aller Entscheidungen – das eigentliche Produkt
│   ├── README.md                     # Was ist der Worklog?
│   └── 2026-03-04.md                 # Beispiel-Eintrag (täglich oder pro Feature)
│
├── /decisions              # 🎯 Architecture Decision Records (ADRs)
│   └── TEMPLATE.md                   # ADR-Template (Kontext, Entscheidung, Konsequenzen)
│
├── /docs                   # 📖 Erweiterte Projekt-Dokumentation
│   └── (zukünftig: Architektur, Tutorials, Analysen)
│
├── /prompts                # 💬 Versionierte KI-Prompts (für Reproduzierbarkeit)
│   └── (zukünftig: alignment/, generation/, review/)
│
├── /tests                  # ✅ Test-Suite (Smoke-Tests, Unit-Tests)
│   └── (zukünftig: test_orchestrator.py, test_retriever.py, etc.)
│
├── /data                   # 🗄️ SQLite-Datenbanken (automatisch generiert)
│   └── pdd.sqlite3                   # Knowledge Base + Evolution Log
│
├── agent-contract.md       # 🤝 Vertrag zwischen Mensch und KI-Agent
├── agent-roles.md          # 🎭 Definition der Agent-Rollen (Architect, Generator, Reviewer, etc.)
├── DOD.md                  # ✔️ Definition of Done (Doc-first Mindset)
├── TEMPLATE.md             # 📄 Prompt-Template (für versionierte KI-Eingaben)
├── Makefile                # ⚡ Shortcuts (venv, install, index, run, test)
├── pyproject.toml          # 🐍 Python-Projektkonfiguration (pytest)
├── requirements.txt        # 📦 Nur essenzielle, schlanke Abhängigkeiten
└── README.md               # 📘 Du liest gerade
```

### 📂 Ordner-Übersicht

| Ordner           | Zweck                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------|
| `/meta`          | **Projektverfassung**: Intent, Workflow, PDD-Philosophie – das „Warum" und „Wie"               |
| `/pdd`           | **PDD-Konfiguration**: Actors, Constraints, Prompt-Templates (die Regeln des Systems)          |
| `/app`           | **API-Schicht**: FastAPI-Endpunkte für den Orchestrator                                        |
| `/lib`           | **Core-Logik**: Generator, Retriever, Reviewer, Metrics, Logging                               |
| `/knowledge_base`| **RAG-Kontext**: Markdown-Dateien für Retrieval (Architektur, Guidelines, Prinzipien)          |
| `/scripts`       | **Utilities**: Indexierung, Setup-Skripte                                                       |
| `/worklog`       | **Entwicklungs-Chronik**: Das „Tagebuch" des Projekts – wichtiger als der Code                 |
| `/decisions`     | **ADRs**: Architekturentscheidungen mit Trade-offs (schwer reversible Entscheidungen)          |
| `/docs`          | **Erweiterte Doku**: Tutorials, Analysen, Experimente                                           |
| `/prompts`       | **Versionierte KI-Eingaben**: Reproduzierbare Prompts für verschiedene Aufgaben                |
| `/tests`         | **Test-Suite**: Automatisierte Tests für die Core-Module                                        |
| `/data`          | **SQLite-Datenbanken**: Automatisch generiert (Knowledge Base + Evolution Log)                 |

### 📄 Root-Level-Dateien

| Datei                  | Zweck                                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------|
| `agent-contract.md`    | **Vertrag zwischen Mensch und KI**: Welche Regeln gelten für KI-Agents in diesem Repo?         |
| `agent-roles.md`       | **Agent-Rollen**: Architect, Generator, Reviewer, Archivist, Analyst – wer macht was?          |
| `DOD.md`               | **Definition of Done**: Checkliste für jede Änderung (Doku ist das Produkt)                    |
| `TEMPLATE.md`          | **Prompt-Template**: Struktur für versionierte KI-Eingaben (Tool, Status, Purpose, Task, etc.) |
| `Makefile`             | **Shortcuts**: `make venv`, `make install`, `make index`, `make run`, `make test`              |
| `pyproject.toml`       | **Python-Konfiguration**: pytest-Einstellungen                                                  |
| `requirements.txt`     | **Abhängigkeiten**: FastAPI, uvicorn, psutil, httpx, PyYAML, pytest                            |

**Wichtig:** Der Ordner `worklog` ist das Herzstück. Hier werden alle Architektur‑Entscheidungen, Prompt‑Iterationen und gewonnenen Erkenntnisse festgehalten. Wer das Projekt verstehen will, liest hier.

---

## 🚀 Quickstart  

So startest du den Meta‑Workflow auf deinem eigenen Rechner (vorzugsweise mit ≥ 8 GB RAM).  

### Variante A: Mit `make` (empfohlen)

```bash
# 1. Repository klonen
git clone https://github.com/benjamin-lam/The-8-GB-Lab.git
cd The-8-GB-Lab

# 2. Virtual Environment erstellen
make venv

# 3. Abhängigkeiten installieren
make install

# 4. Knowledge Base indexieren
make index

# 5. FastAPI-Server starten
make run
```

### Variante B: Manuell

```bash
# 1. Repository klonen
git clone https://github.com/benjamin-lam/The-8-GB-Lab.git
cd The-8-GB-Lab

# 2. Virtual Environment erstellen
python -m venv .venv
source .venv/bin/activate   # (Linux/macOS)  
# .venv\Scripts\activate    # (Windows)

# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. Knowledge Base indexieren
python scripts/index_kb.py

# 5. FastAPI-Server starten
uvicorn app.main:app --reload
```

### 4. Ollama starten und Modell bereitstellen  

Stelle sicher, dass [Ollama](https://ollama.com/) installiert ist und das Modell `phi3:mini` geladen wurde:  

```bash
ollama pull phi3:mini
ollama serve   # startet den Server (falls nicht schon als Service läuft)
```

### 5. Erste Anfrage senden  

Der Orchestrator ist nun unter `http://localhost:8000` erreichbar. Die interaktive API‑Dokumentation findest du unter `http://localhost:8000/docs`.  

```bash
curl -X POST http://localhost:8000/orchestrate \
  -H "Content-Type: application/json" \
  -d '{"user_prompt": "Erstelle ein Python-Skript, das die Anzahl der Commits der letzten 7 Tage in einem Git-Repository zählt."}'
```

Die Antwort enthält den generierten Code, die Anzahl der Iterationen, das Validierungsergebnis und die gesammelten Metriken (Latenzen, RAM‑Verbrauch).  

### 6. Tests ausführen (optional)

```bash
make test
# oder:
pytest
```

---

## 📊 Metriken & Entscheidungsgrundlage  

Das Evolution‑Log speichert für jede Anfrage:  

- **Timestamp**  
- **User‑Prompt** und final verwendeter Prompt  
- **Generierter Code**  
- **Valid** (bool)  
- **Iterationen**  
- **Retrieval‑Zeit, Generierungs‑Zeit, Review‑Zeit** (jeweils in ms)  
- **RAM‑Verbrauch** (während der Generierung)  

Diese Daten helfen später, gezielt Komponenten auszutauschen:  

- Wann wird die Volltextsuche zum Flaschenhals?  
- Reicht `phi3:mini` noch aus, oder brauchen wir ein größeres Modell?  
- Ab welcher Auslastung lohnt sich ein separater, LLM‑basierter Reviewer?  

So wird das System nicht nur ein Werkzeug, sondern auch ein **Forschungsinstrument** – ganz im Sinne von Aufklärung und Verständnis.  

---

## 🤝 Agent-Driven Development

Dieses Projekt nutzt **strukturierte KI-Zusammenarbeit**:

- **`agent-contract.md`**: Definiert Regeln für KI-Agents (KISS, YAGNI, Docs-first)
- **`agent-roles.md`**: Definiert Rollen (Architect, Generator, Reviewer, Archivist, Analyst)
- **`DOD.md`**: Definition of Done für jede Änderung

**Typischer Workflow:**

```
Analyst → Architect → Generator → Reviewer → Archivist
```

1. **Analyst** erklärt den aktuellen Zustand
2. **Architect** schlägt eine Entscheidung vor
3. **Generator** implementiert einen kleinen Schritt
4. **Reviewer** prüft das Ergebnis
5. **Archivist** aktualisiert Worklog/Decisions/Prompts

Siehe `agent-contract.md` und `agent-roles.md` für Details.

---

## 🎧 The Soundtrack  

Vibe Coding braucht Fokus. Dieses Projekt wurde (und wird) mit folgender Playlist entwickelt:  

- **Trent Reznor & Atticus Ross** – *Hand Covers Bruise*  
- **Nils Frahm** – *Says*  
- **Jon Hopkins** – *Emerald Rush*  

Kopfhörer auf, Ablenkung aus – eintauchen.

---

## 📝 Nächste Schritte

- [ ] `/prompts` mit Alignment-Checks befüllen
- [ ] `/docs` mit Architektur-Diagrammen erweitern
- [ ] `/tests` mit Unit-Tests für alle Core-Module ausbauen
- [ ] Evolution-Log-Auswertungs-Dashboard bauen (optional)
- [ ] Alternative Generatoren testen (z.B. `llama3.2:3b`, `deepseek-coder`)

---

## 🌟 Philosophie

> „The documentation is the product. The code is only the proof."

Dieses Projekt ist kein Tool. Es ist ein **Denkmuster** für:

- **Low-Resource Development**: Was geht mit 8 GB RAM?
- **Docs-First Thinking**: Ideen vor Code
- **Prompt-Driven Development**: KI als strukturierter Werkzeugkasten
- **Transparenz**: Jede Entscheidung ist nachvollziehbar

**Das Ziel:** Eine lokal lauffähige, nachvollziehbare Alternative zu Vendor‑Lock‑In und monatlichen API‑Kosten.
