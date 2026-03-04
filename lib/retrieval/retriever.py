from .db import connect
from .indexer import init_retrieval_schema

def retrieve_snippets(query: str, top_k: int = 3) -> list[dict]:
    """Return top-k snippets using SQLite FTS5 BM25 ranking."""
    init_retrieval_schema()
    con = connect()
    try:
        # bm25() is available for FTS5
        rows = con.execute(
            """
            SELECT source, snippet(kb_fts, 1, '', '', ' … ', 12) AS snippet,
                   bm25(kb_fts) AS score
            FROM kb_fts
            WHERE kb_fts MATCH ?
            ORDER BY score
            LIMIT ?;
            """,
            (query, top_k),
        ).fetchall()

        out = []
        for r in rows:
            out.append({
                "source": r["source"],
                "text": r["snippet"],
                "score": float(r["score"]) if r["score"] is not None else None,
            })
        return out
    except Exception:
        # FTS MATCH can throw on special chars; fallback to a safe query
        safe = " ".join([w for w in query.replace(":", " ").replace("-", " ").split() if w])
        if not safe:
            return []
        rows = con.execute(
            """
            SELECT source, substr(body, 1, 500) AS snippet,
                   bm25(kb_fts) AS score
            FROM kb_fts
            WHERE kb_fts MATCH ?
            ORDER BY score
            LIMIT ?;
            """,
            (safe, top_k),
        ).fetchall()
        return [{"source": r["source"], "text": r["snippet"], "score": float(r["score"]) if r["score"] is not None else None} for r in rows]
    finally:
        con.close()
