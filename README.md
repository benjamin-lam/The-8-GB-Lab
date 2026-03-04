# 🔬 The 8‑GB Lab  
### Prompt Driven Development (PDD) auf minimalen Ressourcen  

> „The documentation is the product. The code is only the proof.“  

Dieses Repository ist ein Experiment: Wie weit kommt man mit **Vibe Coding** und **Prompt Driven Development**, wenn man Hardware‑Constraints (8 GB RAM) als kreative Leitplanken nutzt – und System‑Design über rohe Rechenpower stellt?  

Hier entsteht kein weiteres High‑End‑Tool für eine kleine Elite. Hier entsteht ein **Denkmuster**: eine lokal lauffähige, nachvollziehbare Alternative zu Vendor‑Lock‑In, monatlichen API‑Kosten und undurchsichtigen Clouds.  

---

## 🧠 Core Philosophy: Alignment First  

Bevor eine Zeile Code generiert wird, muss die KI beweisen, dass sie das System **verstanden** hat. Wir nutzen ein striktes **Alignment‑Protokoll**, um sicherzustellen, dass die KI nicht „einfach nur rät“, sondern innerhalb unserer Architektur‑Leitplanken agiert.  

### Der Workflow  

1. **Context Ingestion**  
   Die KI liest die Ordner `/meta` (die „Verfassung“ des Projekts) und `/pdd` (Definitionen von Rollen, Constraints und Prompt‑Templates).  

2. **Alignment Check**  
   Die KI erklärt das System in eigenen Worten (siehe `prompts/alignment`). Dabei muss sie zeigen, dass sie Rollen, Ziele und die Low‑Resource‑Philosophie verinnerlicht hat.  

3. **Reality Check**  
   Validierung gegen **KISS** (Keep It Simple, Stupid) und **YAGNI** (You Ain’t Gonna Need It). Nur wenn der Plan diesen Prinzipien standhält, wird er freigegeben.  

4. **Execution**  
   Erst jetzt erfolgt die Code‑Generierung – und zwar streng nach dem freigegebenen Plan.  

Jeder Schritt wird dokumentiert. Die **Dokumentation ist das eigentliche Produkt**; der Code ist nur der Beleg, dass die Idee funktioniert.  

---

## 🏗️ System‑Architektur (Baseline)  

Wir bauen einen ressourcenschonenden **Meta‑Workflow**, der selbst auf einem Rechner mit 8 GB RAM flüssig läuft. Dieser Workflow orchestriert die Entwicklung des eigentlichen Zielsystems (des „Oracle Dashboards“) und sammelt dabei wertvolle Metriken.  

| Komponente               | Low‑Resource‑Entscheidung                                                                 | Warum?                                                                                                                                         |
|--------------------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Orchestrator**         | [FastAPI](https://fastapi.tiangolo.com/) – asynchron, leichtgewichtig                      | Minimaler RAM‑Footprint, perfekt für den zentralen Steuerungsdienst.                                                                          |
| **Retriever**            | **SQLite FTS5** über Markdown‑Dateien in `knowledge_base/`                                | Keine Vektordatenbank, keine Embedding‑Modelle – nur Volltextsuche. Spart RAM und ist sofort nachvollziehbar.                                 |
| **Generator**            | [Ollama](https://ollama.com/) mit `phi3:mini` (3,8 B Parameter)                           | Läuft erfahrungsgemäß in 8 GB RAM, liefert gute Reasoning‑Qualität. Wartezeiten sind akzeptabel und werden gemessen.                         |
| **Reviewer**             | **Regelbasiert** (Python‑Syntax, verbotene Muster, Pflichtfunktionen)                     | Kein zweites LLM nötig – spart RAM und macht das Verhalten transparent. Kann später bei Bedarf durch ein zweites Modell ersetzt werden.      |
| **Evolution‑Log**        | SQLite‑Datenbank mit Metriken (Latenzen, Iterationen, RAM‑Verbrauch)                      | Ermöglicht fundierte Entscheidungen: Wann lohnt sich ein Upgrade? Wo sind die Engpässe?                                                       |

Der Ablauf im Überblick:  

1. User sendet Prompt an `/orchestrate`.  
2. Orchestrator holt per Volltextsuche relevanten Kontext aus `knowledge_base/`.  
3. Er baut einen finalen Prompt (User‑Prompt + Kontext + Guidelines).  
4. Generator (Ollama) erzeugt einen Entwurf.  
5. Regelbasierter Reviewer prüft den Entwurf.  
6. Bei negativem Review folgt eine Iteration (max. 3) mit verbessertem Prompt.  
7. Metriken werden in SQLite geloggt.  
8. Antwort wird an User zurückgegeben.  

---

## 📂 Repository‑Struktur  

Die Struktur spiegelt die Philosophie wider: Ordnung, Transparenz und klare Trennung von Konzept und Implementierung.  

```
📦 The-8GB-Lab
├── /meta                  # Die "Verfassung" des Projekts (Rollen, Intent, Workflow)
├── /pdd                   # Definition von Actors, Constraints und Prompt‑Templates
├── /app                   # FastAPI‑Anwendungslogik (Orchestrator‑Endpunkte)
├── /lib                   # Core‑Module (Retrieval, Generator, Review, Metrics)
├── /knowledge_base        # Kontext‑Dokumente für den RAG‑Prozess (als Markdown)
├── /scripts               # Utilities (z.B. Indexierung der Knowledge Base mit SQLite FTS)
├── /worklog               # Laufendes Log aller Entscheidungen – **das eigentliche Produkt**
├── requirements.txt       # Nur essenzielle, schlanke Abhängigkeiten
└── README.md              # Du liest gerade
```

**Wichtig:** Der Ordner `worklog` ist das Herzstück. Hier werden alle Architektur‑Entscheidungen, Prompt‑Iterationen und gewonnenen Erkenntnisse festgehalten. Wer das Projekt verstehen will, liest das Worklog. Der Code ist nur Beiwerk.  

---

## 🚀 Quickstart  

So startest du den Meta‑Workflow auf deinem eigenen Rechner (vorzugsweise mit ≥ 8 GB RAM).  

### 1. Repository klonen  

```bash
git clone https://github.com/deinname/The-8GB-Lab.git
cd The-8GB-Lab
```

### 2. Virtuelle Umgebung anlegen & Abhängigkeiten installieren  

```bash
python -m venv .venv
source .venv/bin/activate   # (Linux/macOS)  
# .venv\Scripts\activate    # (Windows)
pip install -r requirements.txt
```

### 3. Knowledge Base indexieren  

```bash
python scripts/index_kb.py
```
Dieser Befehl durchsucht `knowledge_base/` nach Markdown‑Dateien und erstellt eine SQLite‑Datenbank mit Volltextsuche (FTS5).  

### 4. Ollama starten und Modell bereitstellen  

Stelle sicher, dass [Ollama](https://ollama.com/) installiert ist und das Modell `phi3:mini` geladen wurde:  

```bash
ollama pull phi3:mini
ollama serve   # startet den Server (falls nicht schon als Service läuft)
```

### 5. FastAPI‑Server starten  

```bash
uvicorn app.main:app --reload
```

Der Orchestrator ist nun unter `http://localhost:8000` erreichbar. Die interaktive API‑Dokumentation findest du unter `http://localhost:8000/docs`.  

### 6. Erste Anfrage senden  

```bash
curl -X POST http://localhost:8000/orchestrate \
  -H "Content-Type: application/json" \
  -d '{"user_prompt": "Erstelle ein Python-Skript, das die Anzahl der Commits der letzten 7 Tage in einem Git-Repository zählt."}'
```

Die Antwort enthält den generierten Code, die Anzahl der Iterationen, das Validierungsergebnis und die gesammelten Metriken (Latenzen, RAM‑Verbrauch).  

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

## 🎧 The Soundtrack  

Vibe Coding braucht Fokus. Dieses Projekt wurde (und wird) mit folgender Playlist entwickelt:  

- **Trent Reznor & Atticus Ross** – *Hand Covers Bruise*  
- **Nils Frahm** – *Says*  
- **Jon Hopkins** – *Emerald Rush*  

Kopfhörer auf, Ablenkung aus – eintauchen.
