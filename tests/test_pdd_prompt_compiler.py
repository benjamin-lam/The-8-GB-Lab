from lib.pdd.prompt_compiler import compile_prompt

def test_compile_prompt_contains_actor_and_task():
    p = compile_prompt(
        actor_name="generator",
        artifact_type="python",
        user_task="Schreibe Hello World",
        retrieved_context="CTX",
        memory_context="MEM",
    )
    assert "Actor" in p
    assert "Task" in p
    assert "Hello World" in p
