# SRI — Skill-based Reasoning Intelligence

> *AI orchestration beyond the mathematical complexity ceiling.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/SRIKARNANDAGIRI/sri?style=social)](https://github.com/SRIKARNANDAGIRI/sri)
[![Status](https://img.shields.io/badge/status-building-orange)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## The Problem Nobody Is Solving

In 2025, Vishal Sikka — former CTO of SAP, CEO of Infosys, Stanford PhD who studied under John McCarthy (the man who coined "Artificial Intelligence") — published a paper with his son titled **"Hallucination Stations: On Some Basic Limitations of Transformer-Based Language Models."**

Their finding, grounded in 60-year-old complexity theory:

> *"For any prompt of length N encoding a task of complexity O(nᵏ) or higher, an LLM will necessarily hallucinate."*

In plain English: **every LLM has a fixed computation budget per token. Simple tasks fit inside it. Complex tasks don't. Beyond a certain complexity threshold, the model doesn't struggle — it collapses.**

This is not a prompt engineering problem. It is not a model size problem. It is a mathematical property of transformer architecture itself.

Apple's research team independently confirmed this in their paper **"The Illusion of Thinking"** — showing that frontier reasoning models like o3 and DeepSeek-R1 don't just perform worse at high complexity. Their accuracy drops to **zero**. Completely. And — most strangely — they reduce their own reasoning effort right when the problem gets hardest.

**This is why autonomous AI businesses keep failing. This is why AI agents hallucinate at the worst possible moment. This is the ceiling everyone is pretending doesn't exist.**

SRI is the first open-source framework built explicitly to work around it.

---

## The SRI Approach

The ceiling exists because we hand complex tasks to AI in one shot. SRI never does that.

Instead, every goal flows through four stages — each one staying below the complexity threshold:

```
COMPLEX GOAL
     │
     ▼
┌─────────────────────────────────┐
│  DECOMPOSE                      │
│  Break goal into atomic steps   │
│  Each step fits below ceiling   │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│  SIMULATE  (powered by MiroFish)│
│  Before acting, simulate the    │
│  consequence with swarm agents  │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│  VERIFY                         │
│  Deterministic checks on output │
│  Human gate before high-stakes  │
│  actions                        │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│  LEARN  (powered by Hermes)     │
│  Every approved workflow saved  │
│  as a reusable skill forever    │
└─────────────────────────────────┘
     │
     ▼
MEASURABLE OUTCOME
```

**No single step ever hits the ceiling. The system gets smarter every time it succeeds. Humans stay in control of what matters.**

---

## Why This Stack

### MiroFish — Simulate before you act
MiroFish is a swarm intelligence engine that spawns thousands of AI agents with independent personalities, memory, and behaviour — then drops them into a simulated world to predict what happens next.

Everyone else uses MiroFish to predict markets and politics. SRI uses it differently: **simulate the consequence of a single AI decision before taking it.** Before sending a client email, simulate how 500 agents react. Before executing a business workflow, run it in a digital sandbox first.

### Hermes Agent — Skills that never die
Hermes (by Nous Research, 100k+ GitHub stars) is a persistent AI agent that converts successful workflows into reusable skill documents. Every problem it solves, it remembers how — forever.

In SRI, every workflow that passes human verification is automatically written as a Hermes skill. **The system compounds. It never re-learns what it already knows.**

### Human Verification Gate — The thing everyone else removed
Every major AI framework is racing toward zero human involvement. SRI goes the opposite direction — and that's exactly what the Sikka math requires.

The human gate is not a limitation. It is the feature that makes SRI safe to run on real business operations.

---

## Architecture

```
                    ┌──────────────────┐
                    │   Complex Goal   │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  Task Decomposer │  ◄── Keeps each step
                    │                  │       below complexity
                    └────────┬─────────┘       ceiling
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
 ┌────────▼───────┐ ┌────────▼───────┐ ┌────────▼───────┐
 │   MiroFish     │ │ Hermes Agent   │ │ Verifier Layer │
 │                │ │                │ │                │
 │ Simulate       │ │ Execute using  │ │ Schema checks  │
 │ outcome with   │ │ persistent     │ │ Deterministic  │
 │ swarm agents   │ │ skill memory   │ │ validation     │
 └────────┬───────┘ └────────┬───────┘ └────────┬───────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                    ┌────────▼─────────┐
                    │ Output Aggregator│
                    │ Merges results   │
                    │ Flags failures   │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  Human Gate      │  ◄── Approve / Reject
                    │                  │       / Refine
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  Skill Written   │  ◄── Hermes saves
                    │  to Hermes       │       forever
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │ Measurable       │
                    │ Outcome          │
                    └──────────────────┘
```

---

## Target Use Case (v1)

**Autonomous operations for freelancers and small agencies.**

The first working demo: a freelancer inputs a project status update goal. SRI decomposes it, drafts the client communication, simulates client reaction via MiroFish, waits for human approval, sends — and saves the entire workflow as a reusable skill.

Why this use case:
- Output is concrete and measurable
- MiroFish adds genuine value (simulate client reaction before sending)
- Hermes adds genuine value (remember this client's communication style forever)
- Narrow enough to ship in 6 weeks
- Affects millions of freelancers globally

---

## Roadmap

### Phase 1 — Core Framework (Weeks 1–2)
- [ ] Task decomposer: goal → atomic steps with complexity budget per step
- [ ] Verifier layer: schema validation on each step output
- [ ] Human gate: CLI approve / reject / refine flow
- [ ] Basic orchestration loop

### Phase 2 — Integrations (Weeks 3–4)
- [ ] Hermes Agent integration: approved workflows → saved skills
- [ ] MiroFish integration: pre-action simulation for communication steps
- [ ] Complexity budget estimator: warn before a step approaches the ceiling

### Phase 3 — Freelancer Use Case (Weeks 5–6)
- [ ] End-to-end demo: project update → simulate → approve → send
- [ ] Skill marketplace: share and reuse workflows
- [ ] Web UI for non-technical users

### Phase 4 — Open (Community-driven)
- [ ] Plugin system for custom verifiers
- [ ] Multi-agent coordination
- [ ] Enterprise audit logs

---

## The Math Behind SRI (Plain English)

Sikka's paper applies the **Time Hierarchy Theorem** (Hartmanis & Stearns, 1965 — Turing Award 1993) to transformers:

- Some problems have a minimum computational floor
- You cannot solve them in fewer steps than that floor requires, no matter how clever your approach
- A transformer's forward pass has a fixed depth
- If a task's verification complexity exceeds what one forward pass can compute — the model **cannot tell good outputs from bad ones**
- This is not a bug. It is an architectural property.

SRI's answer: **never give a task to one forward pass if it exceeds the ceiling. Decompose until every piece fits.**

---

## Getting Started

> ⚠️ SRI is under active development. APIs will change. Watch the repo for updates.

```bash
# Clone the repo
git clone https://github.com/SRIKARNANDAGIRI/sri.git
cd sri

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Add your API keys to .env

# Run the demo
python sri/demo.py
```

### Prerequisites
- Python 3.11+
- Node.js 18+ (for MiroFish)
- Anthropic or OpenAI API key
- Zep Cloud key (free tier works)

---

## Contributing

SRI is being built in public from day one. Every issue, PR, and discussion shapes the direction.

**Best ways to contribute right now:**
- ⭐ Star the repo — it helps more than you think
- 🐛 Open issues for use cases you want SRI to handle
- 💬 Discuss architecture in the Discussions tab
- 🔧 Pick up any open issue tagged `good first issue`

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## References

- Sikka, V. & Sikka, V. (2025). [*Hallucination Stations: On Some Basic Limitations 
of Transformer-Based Language Models.*](https://arxiv.org/abs/2507.07505) arXiv:2507.07505
- Shojaee et al. (2025). *The Illusion of Thinking.* Apple Machine Learning Research
- Hartmanis, J. & Stearns, R. E. (1965). *On the Computational Complexity of Algorithms.* Transactions of the American Mathematical Society
- [MiroFish](https://github.com/666ghj/MiroFish) — Swarm Intelligence Prediction Engine
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — Persistent Skill-based AI Agent by Nous Research

---

## License

MIT — free to use, modify, and build on.

---

<div align="center">

**SRI** — श्री

*Built by a student who read the paper and refused to accept the ceiling.*

[GitHub](https://github.com/SRIKARNANDAGIRI/sri) · [Discussions](https://github.com/SRIKARNANDAGIRI/sri/discussions) · [Issues](https://github.com/SRIKARNANDAGIRI/sri/issues)

</div>
