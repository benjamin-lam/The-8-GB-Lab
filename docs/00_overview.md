# Overview

## Ziel
Dieses Projekt baut einen **PDD-orientierten Meta-Workflow** (Orchestrator → Retrieval → Generation → Review → Evolution-Log),
der auf **low-resource Hardware** lauffähig bleibt (z. B. 8 GB RAM) und vor allem eines liefert:
**Nachvollziehbarkeit**.

## Kernthese
Prompts sind **Interface**. Das System ist:
- Rollen
- Constraints
- Kontext
- Review-Schleifen
- Metriken
- dokumentierte Entscheidungen

## Nicht-Ziele
- Keine „magische“ Autonomie (kein Agent der ungefragt Dinge tut)
- Keine Vector-DB / Embeddings als Voraussetzung
- Keine parallelen Modelle / kein GPU-Zwang
- Kein perfekter Prompt als Ziel

## Erfolgskriterien (Messbar)
- System startet lokal und beantwortet `/orchestrate`
- jede Iteration schreibt Log + Metriken
- jede wichtige Entscheidung hat eine ADR
- Doku erklärt das **Warum** besser als der Code das **Wie**
