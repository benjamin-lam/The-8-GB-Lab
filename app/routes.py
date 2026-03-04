from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from lib.retrieval.retriever import retrieve_snippets
from lib.generator.dummy import generate
from lib.review.rules import review_pythonish_output
from lib.log.evolution import init_db, log_run
from lib.metrics.runtime import measure_ram_mb, now_ms

router = APIRouter()

class OrchestrateRequest(BaseModel):
    user_prompt: str = Field(..., min_length=1, max_length=20_000)

class OrchestrateResponse(BaseModel):
    result: str
    iterations: int
    valid: bool
    metrics: dict

@router.on_event("startup")
def _startup():
    init_db()

@router.post("/orchestrate", response_model=OrchestrateResponse)
def orchestrate(payload: OrchestrateRequest):
    # 1) Retrieval
    t0 = now_ms()
    snippets = retrieve_snippets(payload.user_prompt, top_k=3)
    retrieval_ms = now_ms() - t0

    # 2) Prompt synthesis (PDD = Artefakte -> Prompt)
context = "

".join([f"---
{snip['source']}
{snip['text']}" for snip in snippets])

# Memory: fetch similar recent runs (transparent, low-resource)
from lib.log.memory import fetch_similar_runs, format_memory
similar = fetch_similar_runs(payload.user_prompt, limit=3)
memory = format_memory(similar)

# Compile prompts from explicit actors + constraints + template
from lib.pdd.prompt_compiler import compile_prompt

final_prompt = compile_prompt(
    actor_name="generator",
    artifact_type="python",
    user_task=payload.user_prompt,
    retrieved_context=context,
    memory_context=memory,
)

# 3) Iterate (baseline uses dummy generator; replace later with Ollama adapter)
 (baseline uses dummy generator; replace later with Ollama adapter)
    max_iters = 3
    iterations = 0
    valid = False
    final = ""
    review_feedback = ""

    gen_total_ms = 0.0
    review_total_ms = 0.0
    ram_mb = measure_ram_mb()

    for i in range(max_iters):
        iterations += 1

        t1 = now_ms()
        # Re-compile prompt with reviewer feedback as additional "memory" line (keeps prompt as artefact output)
if review_feedback:
    mem_plus = (memory + "\n\n" if memory else "") + f"Reviewer feedback: {review_feedback}"
else:
    mem_plus = memory

iter_prompt = compile_prompt(
    actor_name="generator",
    artifact_type="python",
    user_task=payload.user_prompt,
    retrieved_context=context,
    memory_context=mem_plus,
)
final = generate(iter_prompt, feedback=review_feedback)
        gen_total_ms += (now_ms() - t1)

        t2 = now_ms()
        verdict = review_pythonish_output(final)
        review_total_ms += (now_ms() - t2)

        if verdict["valid"]:
            valid = True
            break
        review_feedback = verdict["feedback"]

    metrics = {
        "retrieval_time_ms": retrieval_ms,
        "generation_time_ms": gen_total_ms,
        "review_time_ms": review_total_ms,
        "ram_usage_mb": ram_mb,
        "snippets": snippets,
    }

    # 4) Log
    try:
        log_run(
            user_prompt=payload.user_prompt,
            final_prompt=final_prompt,
            generated=final,
            valid=valid,
            iterations=iterations,
            metrics=metrics,
        )
    except Exception as e:
        # Don't fail the user request if logging fails
        raise HTTPException(status_code=500, detail=f"Logging failed: {e}")

    return OrchestrateResponse(result=final, iterations=iterations, valid=valid, metrics=metrics)
