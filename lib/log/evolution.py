import os
import json
import sqlite3
from pathlib import Path
from datetime import datetime
from lib.retrieval.db import DB_PATH, ensure_db_dir, connect as connect_db

SCHEMA = """
CREATE TABLE IF NOT EXISTS evolution (
  id INTEGER PRIMARY KEY,
  timestamp TEXT NOT NULL,
  user_prompt TEXT NOT NULL,
  final_prompt TEXT NOT NULL,
  generated TEXT NOT NULL,
  valid INTEGER NOT NULL,
  iterations INTEGER NOT NULL,
  metrics_json TEXT NOT NULL
);
"""

def init_db():
    ensure_db_dir()
    con = connect_db()
    try:
        con.executescript(SCHEMA)
        con.commit()
    finally:
        con.close()

def log_run(user_prompt: str, final_prompt: str, generated: str, valid: bool, iterations: int, metrics: dict):
    init_db()
    con = connect_db()
    try:
        con.execute(
            """
            INSERT INTO evolution(timestamp, user_prompt, final_prompt, generated, valid, iterations, metrics_json)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.utcnow().isoformat(timespec="seconds") + "Z",
                user_prompt,
                final_prompt,
                generated,
                1 if valid else 0,
                iterations,
                json.dumps(metrics, ensure_ascii=False),
            ),
        )
        con.commit()
    finally:
        con.close()
