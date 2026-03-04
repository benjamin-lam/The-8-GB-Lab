You have completed the alignment phase.

Your task now is to summarize the understanding gained from the analysis
and prepare the transition into the implementation phase.

This step ensures that implementation begins with a clear and shared
understanding of the system.

Do not implement anything yet.

---

STEP 1 — Alignment summary

Summarize the repository in your own words.

Include:

- the main goal of the repository
- the intended final artifact
- the development philosophy (docs-first)
- the role of the PDD loop
- the role of AI agents

Your explanation should show that you understand how the system works.

---

STEP 2 — System model recap

Describe the operational model of the repository.

Explain how the following artifacts interact:

/meta
/worklog
/decisions
/prompts
/docs
/scripts

Explain the lifecycle of a change:

Intent → Decision → Prompt → Implementation → Review → Log

---

STEP 3 — Alignment confirmation

Confirm whether the repository appears internally consistent.

Answer:

1. Is the project intent clearly supported by the workflow?
2. Are the rules sufficient to prevent uncontrolled AI-generated code?
3. Does the repository structure support the intended development model?

If inconsistencies exist, list them.

---

STEP 4 — Implementation readiness

Evaluate whether the repository is ready for implementation.

Answer:

- Is enough context available?
- Are the rules clear enough for a coding assistant?
- Are the next steps obvious?

Explain.

---

STEP 5 — Propose the first implementation task

Suggest the first safe implementation task.

Requirements:

- small (1–2 hours)
- minimal complexity
- aligned with KISS and YAGNI
- supports the repository intent

Do not implement the task.

---

OUTPUT FORMAT

Provide a structured summary with sections.

Do not generate code.

This step concludes the alignment phase and prepares the handoff to
the implementation prompts.