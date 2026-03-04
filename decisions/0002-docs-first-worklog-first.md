# 0002 — Docs-first & Worklog-first als Kernprinzip

**Status:** accepted  
**Date:** 2026-03-04

## Context

Dieses Repository soll nicht nur Code produzieren, sondern den Denk- und Entscheidungsprozess nachvollziehbar machen.

Klassische Doku entsteht oft nachträglich.
Dadurch gehen Annahmen, Trade-offs und Iterationen verloren.

## Decision

Wir arbeiten docs-first.

- Jede Implementierung hat eine dokumentierte Grundlage (Blueprint oder Decision).
- Jede nennenswerte Änderung wird im Worklog protokolliert.
- Code ist eine Folge von dokumentierten Entscheidungen, nicht umgekehrt.

## Consequences

**Positive:**
- Nachvollziehbarkeit: Warum ist das so? → beantwortbar.
- Wiederholbarkeit: Iterationen sind sichtbar.
- Reviewbarkeit: Änderungen lassen sich gegen Absicht und Kontext prüfen.

**Negative / Trade-offs:**
- Mehr Disziplin nötig.
- Gefahr von Overhead → wir dokumentieren nur das Nötigste:
    - Worklog kurz
    - Decisions nur bei echten Trade-offs

## Alternatives considered

- Code-first + “später Doku”: erzeugt Wissenslücken und Legendenbildung.
- Nur Decisions ohne Worklog: verliert Chronologie und Lernkurve.

## Notes / Links

- Worklog: `../worklog/2026-03-04.md`
- Related: `./0001-decisions-system.md`