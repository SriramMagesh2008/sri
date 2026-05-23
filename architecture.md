# SRI Architecture

*How SRI is structured and why each piece exists.*

---

## Overview

SRI is built around one constraint: **no single AI call should ever handle a task that exceeds the complexity ceiling.**

Everything else in the architecture follows from that constraint.

---

## The Four Layers

### 1. Decomposer
**What it does:** Takes a complex goal and breaks it into atomic, verifiable steps.

**Why it exists:** The Sikka ceiling applies per AI call. If each step is simple enough, each call stays below the ceiling. Complexity that would cause one big call to hallucinate is distributed across many small calls that each succeed reliably.

**Key principle:** Each step must have a clear input, a clear expected output, and a way to verify whether it succeeded.

---

### 2. Simulator (MiroFish)
**What it does:** Before any step that touches the outside world (sending an email, making an API call, publishing content), MiroFish spawns thousands of simulated agents to predict how the action plays out.

**Why it exists:** Verification catches bad outputs. Simulation catches bad decisions. An output can be technically correct but strategically wrong. Simulation is the layer that catches strategic errors before they happen.

**Key principle:** Simulate before you act. Never fire and forget.

---

### 3. Verifier
**What it does:** Runs deterministic checks on every step output before the next step runs.

**Why it exists:** AI outputs can be syntactically correct but semantically wrong. The verifier enforces schema, checks for required fields, validates formats, and flags anything that doesn't match the expected output spec.

**Key principle:** Every step output is a contract. The verifier enforces it.

---

### 4. Human Gate
**What it does:** On high-stakes steps, pauses the workflow and presents the output to a human for approval, rejection, or refinement.

**Why it exists:** There are decisions that should not be delegated to any automated system — not because AI can't handle them, but because accountability matters. The human gate is not a limitation. It is the feature that makes SRI safe to deploy on real business operations.

**Key principle:** Automate the routine. Escalate the important.

---

### 5. Skill Store (Hermes)
**What it does:** Every workflow that passes human verification is automatically written as a reusable skill via Hermes. The next time a similar goal appears, SRI loads the skill instead of re-learning.

**Why it exists:** Intelligence should compound. A system that re-learns the same workflows is not getting smarter — it's just running faster. Hermes makes SRI genuinely learn over time.

**Key principle:** Every success is a skill. Every skill is permanent.

---

## The Flow

```
GOAL
 │
 ▼
DECOMPOSER ──────────────────────────────────────┐
 │                                               │
 │  Is there a saved skill for this step?        │
 │  YES → load from Hermes, skip to Verifier     │
 │  NO  → continue                               │
 │                                               ▼
 ▼                                         SKILL STORE
SIMULATOR (MiroFish)                       (Hermes)
 │                                               ▲
 │  Simulate outcome                             │
 │  Flag high-risk actions                       │
 ▼                                               │
EXECUTOR (Hermes Agent)                          │
 │                                               │
 │  Execute the step                             │
 ▼                                               │
VERIFIER                                         │
 │                                               │
 │  FAIL → return to Decomposer with error       │
 │  PASS → continue                              │
 ▼                                               │
HUMAN GATE (if high-stakes)                      │
 │                                               │
 │  REJECT → refine loop                         │
 │  APPROVE → write skill to Hermes ────────────►┘
 ▼
OUTCOME
```

---

## Design Principles

1. **No step should exceed complexity budget** — the Decomposer enforces this
2. **Every output is a contract** — the Verifier enforces this
3. **Simulate before acting** — MiroFish enforces this
4. **Humans control what matters** — the Human Gate enforces this
5. **Intelligence compounds** — Hermes enforces this

---

## Technology Stack

| Layer | Technology |
|---|---|
| Decomposer | Claude / GPT-4 via API |
| Simulator | MiroFish (swarm intelligence) |
| Executor | Hermes Agent (Nous Research) |
| Verifier | Deterministic Python validation |
| Human Gate | CLI (v1) → Web UI (v2) → Slack (v3) |
| Skill Store | Hermes + Zep Cloud |

---

*Part of the [SRI Framework](https://github.com/SRIKARNANDAGIRI/sri)*
