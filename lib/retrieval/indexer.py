import os
from pathlib import Path
from .db import connect

KB_DIR = os.environ.get("PDD_KB_DIR", "knowledge_base")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS kb_docs (
    id INTEGER PRIMARY KEY,
    source TEXT NOT NULL,
    body TEXT NOT NULL
);

-- FTS5 virtual table (contentless for simplicity)
CREATE VIRTUAL TABLE IF NOT EXISTS kb_fts USING fts5(
    source,
    body,
    content='kb_docs',
    content_rowid='id'
);

-- Triggers to keep fts in sync
CREATE TRIGGER IF NOT EXISTS kb_docs_ai AFTER INSERT ON kb_docs BEGIN
    INSERT INTO kb_fts(rowid, source, body) VALUES (new.id, new.source, new.body);
END;

CREATE TRIGGER IF NOT EXISTS kb_docs_ad AFTER DELETE ON kb_docs BEGIN
    INSERT INTO kb_fts(kb_fts, rowid, source, body) VALUES('delete', old.id, old.source, old.body);
END;

CREATE TRIGGER IF NOT EXISTS kb_docs_au AFTER UPDATE ON kb_docs BEGIN
    INSERT INTO kb_fts(kb_fts, rowid, source, body) VALUES('delete', old.id, old.source, old.body);
    INSERT INTO kb_fts(rowid, source, body) VALUES (new.id, new.source, new.body);
END;
"""

def init_retrieval_schema():
    con = connect()
    try:
        con.executescript(SCHEMA_SQL)
        con.commit()
    finally:
        con.close()

def read_markdown_files() -> list[tuple[str, str]]:
    kb = Path(KB_DIR)
    docs = []
    if not kb.exists():
        return docs
    for p in kb.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = p.read_text(encoding="utf-8", errors="ignore")
        rel = str(p.as_posix())
        docs.append((rel, text))
    return docs

def rebuild_index():
    init_retrieval_schema()
    con = connect()
    try:
        con.execute("DELETE FROM kb_docs;")
        for source, body in read_markdown_files():
            con.execute("INSERT INTO kb_docs(source, body) VALUES (?, ?)", (source, body))
        con.commit()
    finally:
        con.close()
