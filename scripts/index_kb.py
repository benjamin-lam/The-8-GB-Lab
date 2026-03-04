"""Index knowledge_base into SQLite FTS5.

Usage:
  python scripts/index_kb.py
"""
from lib.retrieval.indexer import rebuild_index

if __name__ == "__main__":
    rebuild_index()
    print("OK: knowledge_base indexed into SQLite FTS5.")
