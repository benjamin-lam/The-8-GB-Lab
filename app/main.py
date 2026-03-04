from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="PDD Low-Resource Orchestrator", version="0.1.0")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}
