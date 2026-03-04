You are executing the alignment phase of this repository.

Your goal is to iteratively execute all prompts located in:

/prompts/alignment/

This phase is analysis only.  
No implementation work is allowed.

---

CONTEXT

This repository follows a docs-first development model.

Key rules:

- Implementation follows documented decisions.
- All significant actions must be traceable.
- Alignment must happen before implementation.

The alignment prompts exist to verify that the AI agent has correctly
understood the repository.

---

WORKFLOW

Process the alignment prompts one by one.

The order is determined by the filename numbering:

000_*
001_*
002_*
003_*
004_*

For each prompt:

1. Read the prompt.
2. Execute the analysis requested in that prompt.
3. Produce the analysis output.

After completing each prompt:

Create a corresponding worklog entry.

---

WORKLOG REQUIREMENTS

Worklog entries must follow the structure defined in:

/worklog/README.md

Structure:

Context  
Decision  
Why  
Result  
Next

Language requirement:

All worklog entries must be written in **German**.

---

WORKLOG CONTENT

For each iteration the worklog entry must include:

Context  
- Which alignment prompt is being executed  
- What the purpose of that prompt is

Decision  
- That the repository enters an alignment analysis step

Why  
- Why this analysis step is necessary before implementation

Result  
- Summary of the findings of the prompt execution

Next  
- Which alignment prompt will be executed next

---

FILE LOCATION

Append the worklog entry to the current worklog file:

/worklog/YYYY-MM-DD.md

If the file does not exist yet, create it.

---

ITERATION RULE

Execute exactly one prompt at a time.

After finishing one prompt:

- update the worklog
- clearly mark the iteration
- continue with the next prompt

---

OUTPUT FORMAT

For each iteration produce:

1. The analysis output of the prompt
2. The corresponding worklog entry

---

IMPORTANT CONSTRAINTS

Do NOT:

- implement code
- modify repository structure
- introduce tooling
- skip alignment prompts

This phase is strictly for repository understanding.

Only proceed to implementation prompts once the alignment sequence
has been completed.
