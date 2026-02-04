# Nanocode v1.0 (Open Source Observation & Orchestration Framework)

Nanocode v1.0 is an open-source local observation and orchestration framework for constraint-aware, model-agnostic AI workflows. It provides a structured way to define constraints, apply recovery strategies, and generate execution traces for AI calls. This repository is an observation tool; governance features are outside its scope and should be contributed separately.

## What this repository includes
- Constraint engine (framework-level): constraint profiles, structured prompt templates, and constraint observation.
- Recovery ("tragedy") strategies: bounded fallback/degrade/retry patterns for predictable behavior.
- Execution traces: run artifacts describing which constraints were applied, waived, or failed.
- Model adapters: OpenAI, Anthropic, and custom HTTP backends to keep workflows portable.
- Local stack: FastAPI backend + model server layer + frontend playground UI + dev scripts.

## What this repository explicitly does NOT include (Non-Goals)
Nanocode v1.0 does **not** provide:
- Governance or enforcement mechanisms
- Persistent internal identity/state beyond explicit external storage you configure
- Self-modifying instruction graphs or autonomous mutation
- Any Cham-Code production components

Governance, policy enforcement, or autonomous control features are intentionally out of scope; they should be contributed as separate modules or forks by those who need them.

## Relationship to Cham-Code / Nanocode v2.0
- **Nanocode v1.0 (this repo):** open-source observation and orchestration framework.
- **Nanocode v2.0 (Cham-Code):** separate proprietary kernel; not distributed or referenced here.

This separation maintains licensing clarity and architectural independence.

## Prerequisites
- Python 3.10+ (or the version used by this project)
- Node.js 20.19+ (for the frontend) and npm
- Git
- (Optional) a Python virtual environment
- An API key for at least one model provider:
  - OpenAI (e.g. gpt-4o)
  - Anthropic
  - Or a compatible custom model server

## Quickstart
```bash
git clone https://github.com/<your-org>/Nanocode-v1.0-main.git
cd Nanocode-v1.0-main

# Backend dependencies
python3 -m pip install -r requirements.txt

# Frontend dependencies
cd frontend && npm install && cd ..
```

Configure providers (from repo root):
```bash
./configure_nanocode.sh
```
The script will create `.env` (from `.env.example`), prompt for OpenAI/Anthropic/Custom, and write credentials and model names.

Start everything locally:
```bash
./dev.sh
```
This starts the model server (port 9000), Nanocode API (port 8000), and frontend dev server (port 5173). Open http://localhost:5173 to experiment with constraints, workflows, and responses. Stop with `CTRL+C`.

Run the frontend only (optional):
```bash
cd frontend
npm install
npm run dev
```

### Optional: manual `.env`
```bash
cp .env.example .env
# edit with your keys/models
```
`.env` is ignored by Git and should never be committed.

### Build frontend for production (optional)
```bash
cd frontend
npm run build
npm run preview -- --host 0.0.0.0 --port 4173
```
Then open http://localhost:4173.

## Architecture at a Glance
- **Orchestration framework**: constraints, recovery strategies, and execution traces for observable agent behavior.
- **Model adapters**: swap between OpenAI, Anthropic, or custom backends without changing workflows.
- **Frontend playground**: experiment with constraints and workflows in-browser.
- **CLI/scripts**: `configure_nanocode.sh` for setup and `dev.sh` for a full local stack.

## Whitepaper
See [WHITEPAPER.md](WHITEPAPER.md) for design goals and the Nanocode v1.0 open source scope.

## License
Nanocode v1.0 is released under the Apache License 2.0. See `LICENSE` for terms and `NOTICE` for attribution details.

## Security Notes
- Never commit `.env` or any API keys to source control.
- Review `configure_nanocode.sh` to understand how your `.env` is written.
- When using remote model providers (OpenAI, Anthropic), ensure your usage complies with their terms.
