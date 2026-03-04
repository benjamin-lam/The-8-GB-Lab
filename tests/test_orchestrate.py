from fastapi.testclient import TestClient
from app.main import app

def test_orchestrate_baseline():
    c = TestClient(app)
    r = c.post("/orchestrate", json={"user_prompt": "Erzeuge ein kurzes Python-Beispiel für Hello World"})
    assert r.status_code == 200
    data = r.json()
    assert "result" in data
    assert "metrics" in data
    assert "iterations" in data
    assert isinstance(data["metrics"].get("ram_usage_mb"), (int, float))
