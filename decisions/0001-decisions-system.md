# 0001 — Decisions-System (ADR) einführen

**Status:** accepted  
**Date:** 2026-03-04

## Context

Das Repository ist docs-first und soll Entscheidungen nachvollziehbar machen.

Der Worklog bildet die Chronologie ab, ist aber nicht optimal, um später schnell zu verstehen:
- welche Architekturentscheidungen gelten
- welche verworfen wurden
- welche Konsequenzen sie haben

## Decision

Wir führen ein `/decisions/` Verzeichnis mit ADRs ein.

Jede relevante Architektur- oder Workflow-Entscheidung bekommt eine eigene Datei:
- nummeriert
- kurz
- mit Status
- mit Konsequenzen

## Consequences

**Positive:**
- Entscheidungen sind auffindbar und stabil referenzierbar (z. B. aus Kapiteln, Issues, PRs).
- “Warum ist das so?” ist dokumentiert, ohne den Worklog durchsuchen zu müssen.
- Ersetzt Meinung durch nachvollziehbare Begründung.

**Negative / Trade-offs:**
- Zusatzaufwand: Entscheidungen müssen aktiv gepflegt werden.
- Gefahr von Overhead → ADRs nur für echte Entscheidungen, nicht für Kleinkram.

## Alternatives considered

- Nur Worklog: zu unstrukturiert für spätere Referenz.
- Wiki/Confluence: nicht versioniert im selben Flow, weniger “code-adjacent”.

## Notes / Links

- Worklog: `../worklog/2026-03-04.md`