# CLAUDE.md — Bladerunner Runner

This file orients Claude (in any form — Code, Cowork, chat) to the Bladerunner codebase. Read it before doing substantive work in this repository.

## What Bladerunner is

Bladerunner is PnyxLabs' empirical research platform for measuring AI personality. It administers validated psychological instruments to large language models that have been programmed with specified OCEAN personality profiles, then measures cross-model reliability as the primary metric of personality implementation quality.

The platform underpins a research programme investigating whether LLMs exhibit stable personality attractors — coherent regions in model parameter space that resist perturbation. It also underpins commercial IP: notably the Psyche patent on prompt choice architecture as attractor engineering, and the Lachesis runtime drift-control system.

The codebase is the *measurement apparatus*. The data it produces, the SA-reports it informs, and the papers it supports are the *research output*. These are kept conceptually distinct.

## Repository structure

```
Bladerunner/                          # this repo
├── bladerunner_runner/               # main Python package
│   ├── cli.py                        # CLI entry point: quick-test, create, status, run
│   ├── runner.py                     # ExperimentRunner — core execution engine
│   ├── models.py                     # Dataclasses: OceanProfile, TestCase, Response, etc.
│   ├── db.py                         # Thin pyodbc wrapper. Raw SQL, no ORM.
│   ├── instruments/                  # WHAT we measure (BFI, PHQ-9, GAD-7, Levenson, Dark Triad, ...)
│   │   └── base.py                   # BaseInstrument abstract class
│   ├── input_systems/                # HOW we program personality (ocean_direct, narrative, behavioral, exemplar, scenario, hexaco)
│   │   └── base.py                   # BaseInputSystem abstract class
│   ├── clients/                      # LLM provider adapters (claude, openai, deepseek, gemini, xai)
│   │   └── base.py                   # BaseClient + RateLimiter
│   ├── analysis/                     # Post-experiment analytics, item reliability
│   ├── Initiators/                   # Per-experiment setup scripts (create_experiment_7.py, etc.)
│   └── probes/                       # (currently empty — reserved for future synthetic probe instruments)
├── experiments/                      # Per-experiment output folders (CSVs, reports)
├── reports/                          # CANONICAL reports (committed to git)
├── papers/                           # CANONICAL papers (PDFs, committed to git)
├── secondary_analysis/               # SA-NNN analysis artefacts (item taggings, reliability tables, scratch analyses)
├── scripts/                          # SQL schema, ad-hoc utility scripts
└── _env / .env                       # Local secrets (NOT committed) — API keys, DB connection
```

Working drafts and active research documents live OUTSIDE this repo, in the workspace folder one level up. Only canonical, citation-worthy artefacts belong in `papers/` and `reports/`.

## Core architecture

The system is organised around four orthogonal axes that combine to produce test cases:

1. **Instrument** — what psychological construct is being measured (e.g. BFI, PHQ-9)
2. **Input system** — how the OCEAN profile is rendered into a system prompt (e.g. `ocean_direct` gives raw scores; `narrative` writes a character description; `exemplar` references a named figure)
3. **Profile** — the OCEAN values being programmed (5 integers 0–100)
4. **Provider** — which LLM is the subject (Claude, OpenAI, DeepSeek, Gemini, xAI)

A single test case is the cross-product of these four. An experiment is a configured set of test cases. The runner consumes pending test cases from the database and writes results back.

The database is the source of truth for experiment state. Python is the source of truth for instrument and input-system *definitions* — the schema is deliberately thin and references things by short name (`'levenson'`, `'ocean_direct'`) which must match the Python class identifiers exactly.

Longitudinal mode (`--longitudinal` flag, `is_longitudinal=True`) accumulates conversation history across questions within a test case. Cross-sectional mode treats each question independently. The longitudinal/cross-sectional contrast is one of the platform's primary methodological tools.

## Key conventions

- **Async throughout.** All client code, all runner code is `async`. Rate limiting is per-provider via the `RateLimiter` in `clients/base.py`. Don't introduce synchronous network calls.
- **Raw SQL, no ORM.** `db.py` is a thin pyodbc wrapper. Schema lives in `scripts/schema.sql`. New tables go there.
- **Dataclasses for models.** No SQLAlchemy, no Pydantic. See `models.py`.
- **Short names are identifiers.** `'levenson'`, `'bfi'`, `'ocean_direct'` etc. appear as class identifiers, database keys, CLI arguments, and filename roots. They must stay consistent across all four.
- **Reverse scoring is per-question, computed at parse time.** See `Question.is_reversed` and the `score_after_reverse` field on `Response`.
- **Profiles are 0–100 integers per OCEAN factor.** Not floats. Not 1–5 Likert.

## Adding things

- **New instrument:** subclass `BaseInstrument` in `bladerunner_runner/instruments/`, register it in `instruments/__init__.py`, add the short name to the `instruments` table.
- **New input system:** subclass `BaseInputSystem` in `bladerunner_runner/input_systems/`, register in `input_systems/__init__.py`, add to `input_systems` table.
- **New provider:** subclass `BaseClient` in `bladerunner_runner/clients/`, add API key to `_env`, register in `clients/__init__.py`, add to `providers` table.
- **New experiment:** create a setup script in `bladerunner_runner/Initiators/` following the pattern of `create_experiment_9.py`. Then `python -m bladerunner_runner.cli create --name ...` (or run the initiator directly).

## What this codebase is *not*

- **Not an agent framework.** The runner executes deterministic experiment configurations. It does not reason about what to do next.
- **Not a personality classifier.** It administers instruments and records responses. Interpretation is downstream, in the analytics modules and SA-reports.
- **Not a production service.** It's a research platform. No HTTP API, no auth, no SLA. Crashes are recoverable because the database holds state.

## Current research context (April 2026)

The most recent significant finding is **affect instability** — affect content in psychological items predicts longitudinal reliability degradation at r ≈ -0.86 (see `reports/longitudinal_degradation_finding.md` and the corresponding write-up in the workspace folder). A confirmatory experiment using three matched synthetic instruments (NE-A, NE-T, NE-B — affect / attitude / behavioural framings of the same construct) is **designed but not yet run**. Picking this up is the natural next experiment.

Also planned: a performative-vs-directive experiment to back Claim 9 of the Psyche patent (substituting directive constructions for performative ones in an otherwise stable prompt should measurably degrade attractor depth).

Before designing new experiments, read the latest reports and SA-NNN files in `secondary_analysis/`. The research has moved beyond simple reliability measurement into attractor topology and the state/trait distinction.

## Working with the database

Connection is via `_env`:
```
DB_SERVER=...
DB_NAME=BladerunnerDev
DB_TRUSTED_CONNECTION=yes  # or no, with DB_USER and DB_PASSWORD
```
Default driver is `ODBC Driver 17 for SQL Server`. Schema is `scripts/schema.sql`.

## Don'ts

- Do not commit `_env`, `.env`, or anything containing API keys.
- Do not modify the runner, scoring, or client code mid-experiment. Reliability claims depend on a frozen apparatus during data collection.
- Do not add dependencies casually. The stack is small on purpose: pyodbc, dotenv, asyncio, the provider SDKs. New dependencies need a reason.
- Do not rename short identifiers (`'levenson'`, `'bfi'`, etc.) without coordinated changes in Python, the database, and any open experiments.
- Do not introduce ORMs, web frameworks, or "make it production-ready" refactors. This is a research instrument, not a product.

## Brand and naming

The company is **PnyxLabs**. The previous name "SneakyLabs" may still appear in older comments — leave those alone unless explicitly cleaning up. The research programme retains the name **Bladerunner** (no copyright issue with a research homage). The Replicants product suite has been renamed to Greek mythological figures (Lachesis, Clotho, Atropos, plus Mneme, Psyche, Hermes), but those products live in their own repositories — not here.
