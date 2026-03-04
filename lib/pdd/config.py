from __future__ import annotations
import os
from pathlib import Path
import yaml

PDD_DIR = Path(os.environ.get("PDD_DIR", "pdd"))

def _load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

def load_actors() -> dict:
    return _load_yaml(PDD_DIR / "actors.yaml")

def load_constraints() -> dict:
    return _load_yaml(PDD_DIR / "constraints.yaml")

def load_template() -> str:
    tpl = PDD_DIR / "prompt_template.md"
    if not tpl.exists():
        return ""
    return tpl.read_text(encoding="utf-8")
