# Contributing to SRI

First off — thank you. SRI is being built in public from day one, and every contribution shapes what it becomes.

---

## The Spirit of SRI

SRI exists because one student read about a mathematical ceiling on AI and refused to accept it. If you're here, you probably feel the same way. That's the only prerequisite.

---

## Ways to Contribute Right Now

### 1. Star the repo
Sounds small. It isn't. Stars trigger GitHub's trending algorithm. If you believe in what SRI is building, starring takes 2 seconds and genuinely helps.

### 2. Open an issue
Tell us:
- A use case you want SRI to handle
- A gap you see in the architecture
- A tool you think should be integrated

### 3. Join the discussion
Go to the **Discussions** tab. Introduce yourself. Tell us what problem you're trying to solve with AI agents.

### 4. Pick up a `good first issue`
We tag beginner-friendly issues clearly. No contribution is too small.

### 5. Write docs
The `docs/` folder needs love. If you understand the Sikka ceiling problem and can explain it clearly, open a PR.

---

## Development Setup

```bash
# Fork the repo, then clone your fork
git clone https://github.com/YOUR_USERNAME/sri.git
cd sri

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
# Fill in your API keys
```

---

## Pull Request Guidelines

- Keep PRs focused — one thing at a time
- Write a clear description of what you changed and why
- If your PR fixes an issue, reference it: `Fixes #123`
- Don't worry about perfection — we review and iterate together

---

## Code Style

- Python: follow PEP 8, use Black for formatting
- Docstrings on all public functions
- Comments explaining *why*, not just *what*

---

## Questions?

Open a Discussion. No question is too basic. We're all figuring this out together.

---

*SRI — श्री — Built in public, built together.*
