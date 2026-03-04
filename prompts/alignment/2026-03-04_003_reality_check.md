You are performing a reality check before implementation continues.

The goal of this step is to prevent unnecessary complexity and ensure
that the repository remains aligned with its core philosophy.

This repository intentionally follows a minimal, docs-first development model.

Implementation must remain small, understandable and reproducible.

Read the repository documentation again, especially:

/meta/project-intent.md
/meta/workflow.md
/meta/pdd-loop.md
/meta/pdd-map.md
/meta/agent-contract.md
/meta/agent-roles.md

---

TASK

Evaluate the current direction of the repository and the proposed next steps.

---

STEP 1 — Identify potential overengineering

Analyze whether the proposed work might introduce unnecessary complexity.

Examples:

- unnecessary frameworks
- large build systems
- excessive abstraction
- premature architecture decisions

Explain where complexity might appear.

---

STEP 2 — Apply KISS and YAGNI

For each proposed implementation step ask:

1. Is this the simplest possible approach?
2. Is this needed now, or only potentially useful later?
3. Can the same outcome be achieved with less structure or tooling?

Explain your reasoning.

---

STEP 3 — Validate alignment with project intent

Compare the proposed work with the project intent.

Does the work support the goal of:

- documenting the development process
- demonstrating Prompt Driven Development
- keeping the system minimal and understandable

If something deviates from that goal, explain why.

---

STEP 4 — Recommend simplifications

Suggest ways to reduce complexity.

Examples:

- reduce tooling
- split work into smaller steps
- delay features
- simplify architecture

---

STEP 5 — Final recommendation

Provide a short summary:

- Is the project still aligned with its intent?
- What is the safest next step?
- What should definitely NOT be built yet?

---

OUTPUT FORMAT

Provide a structured analysis.

Do not generate code.

Do not modify the repository.

This step is purely a reality check to keep the system simple and aligned.