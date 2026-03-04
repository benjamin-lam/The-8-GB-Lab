.PHONY: venv install index run test

venv:
	python -m venv .venv

install:
	. .venv/bin/activate && pip install -r requirements.txt

index:
	. .venv/bin/activate && python scripts/index_kb.py

run:
	. .venv/bin/activate && uvicorn app.main:app --reload

test:
	. .venv/bin/activate && pytest
