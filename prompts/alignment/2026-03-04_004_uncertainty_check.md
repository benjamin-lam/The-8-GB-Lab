You are performing an uncertainty check.

The goal of this step is to explicitly identify areas where the
repository or its intentions are unclear.

Large Language Models often produce confident answers even when
the underlying understanding is incomplete.

This step exists to surface those uncertainties before implementation begins.

---

STEP 1 — Identify unclear areas

List parts of the repository that may still be ambiguous.

Examples:

- unclear goals
- missing constraints
- undefined interfaces
- missing documentation
- assumptions about the implementation

---

STEP 2 — Identify assumptions

List all assumptions you made while analyzing the repository.

For each assumption explain:

- why the assumption was made
- what information would confirm or reject it

---

STEP 3 — Risk of misinterpretation

Identify areas where a misunderstanding could lead to incorrect
implementation decisions.

Explain the potential consequences.

---

STEP 4 — Questions for the repository owner

List questions that would reduce uncertainty.

These questions should help clarify:

- scope
- architecture
- implementation priorities

---

STEP 5 — Confidence level

Estimate your confidence in your understanding of the repository.

Provide a short explanation.

Example scale:

0–30% → very uncertain  
30–60% → partial understanding  
60–80% → mostly understood  
80–100% → confident understanding

---

OUTPUT

Provide a structured uncertainty report.

Do not implement anything.

This step exists to reduce hallucination risk before development begins.
