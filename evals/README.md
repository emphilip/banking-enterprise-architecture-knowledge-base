# Evals

Quality gates for the knowledge base. Two layers:

1. **Deterministic** — `checks.py` (Python stdlib only). Phase-scoped, scriptable,
   runs in CI. Fails the build on any `FAIL`-severity finding; `WARN`/`INFO` are
   advisory.
2. **Semantic** — `rubric.md`, applied by an LLM `judge` sub-agent on a sample of
   notes (accuracy, groundedness/anti-hallucination, relationship sensibility,
   naming fidelity, granularity). Run during a deep-dive's validate phase.

## Run it

```bash
python evals/checks.py --phase all            # everything + regression
python evals/checks.py --phase steward        # registry integrity
python evals/checks.py --phase author         # per-file note checks
python evals/checks.py --phase weave          # indexes, maps, flows, links
python evals/checks.py --phase research       # research staging files
python evals/checks.py --phase all --update-baseline   # refresh regression snapshot
```

Outputs `evals/report.json` and `evals/REPORT.md`. Exit code is non-zero if any
`FAIL` is present.

## What each phase checks

- **steward** — no duplicate canonical names; no alias colliding with another
  canonical name; every capability parent exists; L1→L4 level monotonicity;
  domains referenced exist; legacy/modern `realizes` + `supersedes` targets
  resolve; no kebab/path collisions.
- **author** — registry⇄file parity (no missing/extra files); H1 == title;
  `## Relationships` present and within ~1800 chars; **each relationship's object
  is a registry name** (not just the subject); only the 7 verbs; ≥1 relationship;
  definition starts with the canonical name; "Also known as" present; <6 KB;
  system notes carry sources + a reference link; pronoun heuristic.
- **weave** — every `_index.md` links every file in its folder; no dangling
  `[[wikilinks]]`; process-flow step numbering contiguous with `causes` chains;
  maps present.
- **research** — `_status/proposed-*.md` staging files include source URLs.
- **all** — runs the above plus **regression** vs `evals/baseline.json` (concept
  counts must not drop; edge-count drops warn).

## Regression baseline

`evals/baseline.json` is the last-known-good snapshot (per-pillar counts + edge
tallies). Refresh it only after a run is fully green, with `--update-baseline`.

## CI

`.github/workflows/evals.yml` runs `--phase all` on every push and PR (no
secrets, no LLM). The LLM-judge is run interactively during deep-dives, not in
CI.
