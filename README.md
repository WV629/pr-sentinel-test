# pr-sentinel-test

Fixture target repo for testing **PR Sentinel** (Agentware hackathon, T5 developer workflows).

This repo is a small, real Python project that the agent runs against during
development. It is **not** the agent itself — the agent lives in `WV629/pr-sentinel`
(created when the competition starts).

## What is in here

- `calc.py` — a tiny arithmetic module used to recieve test inputs.
- `test_calc.py` — pytest tests for `calc.py`.
- Fixture PRs (open against `main`):
  1. a planted bug that breaks a test,
  2. a typo-only docs fix,
  3. a deliberately high-risk change the agent should flag.

## Running the tests

```sh
python -m pytest -q
```

## Layout

The module and its tests are kept seperate so the agent can run pytest and
ruff in a sandbox without touching anything else.
