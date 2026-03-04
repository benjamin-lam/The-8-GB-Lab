from __future__ import annotations
import json
from typing import Any
from lib.pdd.config import load_actors, load_constraints, load_template

def _fmt_constraints(obj: Any) -> str:
    if obj is None:
        return ""
    if isinstance(obj, str):
        return obj
    if isinstance(obj, list):
        return "\n".join([f"- {x}" for x in obj])
    if isinstance(obj, dict):
        lines = []
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{k}:")
                lines.append(_fmt_constraints(v))
            else:
                lines.append(f"- {k}: {v}")
        return "\n".join(lines)
    return str(obj)

def compile_prompt(
    *,
    actor_name: str,
    artifact_type: str,
    user_task: str,
    retrieved_context: str,
    memory_context: str,
) -> str:
    actors = load_actors()
    constraints = load_constraints()
    template = load_template()

    actor = actors.get(actor_name, {})
    actor_purpose = actor.get("purpose", "")
    actor_role = actor.get("role", "")

    global_c = _fmt_constraints(constraints.get("global", {}))
    artifact_c = _fmt_constraints(constraints.get(artifact_type, {}))

    if not template:
        # Fallback: minimal composed prompt
        return (
            f"Actor: {actor_name}\nPurpose: {actor_purpose}\nRole: {actor_role}\n\n"
            f"Constraints (global):\n{global_c}\n\n"
            f"Constraints ({artifact_type}):\n{artifact_c}\n\n"
            f"Context:\n{retrieved_context}\n\n"
            f"Memory:\n{memory_context}\n\n"
            f"Task:\n{user_task}\n"
        )

    return template.format(
        actor_name=actor_name,
        actor_purpose=actor_purpose,
        actor_role=actor_role,
        constraints_global=global_c,
        constraints_artifact=artifact_c,
        retrieved_context=retrieved_context or "(none)",
        memory_context=memory_context or "(none)",
        user_task=user_task,
    )
