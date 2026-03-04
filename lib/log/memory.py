from __future__ import annotations
import json
from typing import List, Dict
from lib.retrieval.db import connect as connect_db
from lib.log.evolution import init_db

def fetch_similar_runs(user_prompt: str, limit: int = 3) -> List[Dict]:
    """Naive similarity: keyword overlap via SQL LIKE on user_prompt. Low-resource and transparent."""
    init_db()
    tokens = [t for t in user_prompt.replace(":", " ").replace("-", " ").split() if len(t) >= 4][:5]
    if not tokens:
        return []

    con = connect_db()
    try:
        # Build OR LIKE query
        wheres = " OR ".join(["user_prompt LIKE ?"] * len(tokens))
        params = [f"%{t}%" for t in tokens]
        rows = con.execute(
            f"""
            SELECT timestamp, user_prompt, valid, iterations, metrics_json
            FROM evolution
            WHERE {wheres}
            ORDER BY id DESC
            LIMIT ?
            """,
            (*params, limit),
        ).fetchall()

        out = []
        for r in rows:
            metrics = {}
            try:
                metrics = json.loads(r["metrics_json"])
            except Exception:
                metrics = {}
            out.append({
                "timestamp": r["timestamp"],
                "user_prompt": r["user_prompt"],
                "valid": bool(r["valid"]),
                "iterations": int(r["iterations"]),
                "metrics": metrics,
            })
        return out
    finally:
        con.close()

def format_memory(runs: List[Dict]) -> str:
    if not runs:
        return ""
    lines = []
    for r in runs:
        m = r.get("metrics", {})
        lines.append(
            f"- {r['timestamp']} | valid={r['valid']} | iters={r['iterations']} | "
            f"retrieval_ms={m.get('retrieval_time_ms')} gen_ms={m.get('generation_time_ms')} review_ms={m.get('review_time_ms')}"
        )
        lines.append(f"  prompt: {r['user_prompt'][:180]}")
    return "\n".join(lines)
