# ADR-0001 Retrieval via SQLite FTS5

## Kontext
Ziel ist low-resource (8 GB RAM), nachvollziehbar, ohne Embeddings als Pflicht.

## Entscheidung
Retrieval über SQLite FTS5 (`kb_fts`) auf Markdown-Dokumenten.

## Konsequenzen
✅ leichtgewichtig, keine Embedding-Modelle  
✅ transparent (SQL)  
✅ gut genug für „Kontext-Schnipsel“  

⚠️ Match-Syntax kann bei Sonderzeichen zicken → Fallback nötig  
⚠️ Semantik ist begrenzt (kein Vektorraum)  

## Alternativen
- Whoosh (Python-only Index)  
- grep + manuelle Relevanz  
- ChromaDB + Embeddings (verworfen: RAM/Komplexität)
