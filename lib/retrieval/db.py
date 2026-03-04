import os
import sqlite3
from pathlib import Path

DB_PATH = os.environ.get("PDD_DB_PATH", "data/pdd.sqlite3")

def ensure_db_dir():
    Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)

def connect() -> sqlite3.Connection:
    ensure_db_dir()
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con
