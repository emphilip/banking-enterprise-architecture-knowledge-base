# Deep-Dive Progress Ledger

Resumable source of truth for the iterative domain deep-dive (L2/L3/L4 business
and technology capabilities + multi-granularity process flows). Every sub-agent
updates this file at the end of each phase and before stopping for any reason.
A fresh session reads this file to resume with zero extra context.

Legend for cells: `todo` | `in-progress` | `done` | `n/a`.
Run one domain per invocation (DOMAIN = a name below, or "next" to auto-pick the
first row whose Status is not `done`).

## Domain status

| # | Domain | Kind | Caps L3/L4 | Tech L2/L3 | Flows | Validated | Status |
|---|---|---|---|---|---|---|---|
| 1 | Customer Management | business | todo | todo | todo | todo | todo |
| 2 | Payments | business | done | done | done | done | done |
| 3 | Lending & Credit | business | todo | todo | todo | todo | todo |
| 4 | Deposits & Accounts | business | todo | todo | todo | todo | todo |
| 5 | Cards | business | todo | todo | todo | todo | todo |
| 6 | Wealth & Investments | business | todo | todo | todo | todo | todo |
| 7 | Risk Management | business | todo | todo | todo | todo | todo |
| 8 | Compliance & Financial Crime | business | todo | todo | todo | todo | todo |
| 9 | Channels & Engagement | business | todo | todo | todo | todo | todo |
| 10 | Finance & Treasury | business | todo | todo | todo | todo | todo |
| 11 | Core Processing | technology | n/a | todo | n/a | todo | todo |
| 12 | Data & Analytics | technology | n/a | todo | n/a | todo | todo |
| 13 | Integration & APIs | technology | n/a | todo | n/a | todo | todo |
| 14 | Security & Identity | technology | n/a | todo | n/a | todo | todo |
| 15 | AI & Automation | technology | n/a | todo | n/a | todo | todo |

Recommended order: deepen the 10 business domains first (1→10), then the 5
technology domains (11→15), since business L4 capabilities pull the technology
decomposition into sharper focus.

## Active run

- Domain: Payments (DONE) — next: run DEEP-DIVE-PROMPT with DOMAIN="next" (picks Customer Management)
- Phase: DONE — Payments deep-dive complete. All 5 eval gates 0 FAIL; LLM-judge PASS (evals/judge-payments.md); baseline refreshed (334 files).
- Started: 2026-06-15
- Resume note: proceed to Phase 3 author — author the new L3/L4 capability, tech
  sub-capability, sub-process, process-flow step, and supporting-concept notes per
  the registry, then run `python evals/checks.py --phase author` (0 FAIL).

## Next actions (ordered — keep specific enough to resume cold)

- [ ] Deepen the next domain: run _status/DEEP-DIVE-PROMPT.md with DOMAIN = "next"
      (first not-done row = Customer Management). Same eval-gated pipeline:
      research -> steward gate -> author -> weave -> validate (+ LLM-judge) ->
      mark row done + refresh baseline.

## Decisions log

- (2026-06-15, Phase 2 Steward, Payments) Reconciled the three Payments proposals
  into glossary/_canonical-names.md. Counts added per section: Business
  capabilities +33 (16 L3, 17 L4); Legacy systems +3; Modern systems +3;
  Technology sub-capabilities +11 (8 L2, 3 L3); Process sub-processes +9; Process
  flow steps +22 (8 Payment Processing, 7 Reconciliation & Settlement, 7 Cash
  Management); Supporting concepts +16 (6 role, 4 event, 6 artifact). Total +97
  rows. Renames: none — all proposed names were globally unique against the
  registry and across proposals (no collisions, no alias-vs-canonical clashes), so
  no disambiguating words were appended. Steward decision: the six new payment-hub
  systems realize the parent technology capability **Payment Orchestration** (a
  real `## Technology capabilities` entry under which all proposed L2 sub-caps
  sit), rather than naming a sub-capability in the Realizes column, because the
  steward gate validates system "realizes" targets only against the top-level
  Technology capabilities table. Steward gate: 0 FAIL, 3 WARN (all benign
  "legacy has no modern successor" for the three new payment-hub legacy systems).
- (initialized) Ledger created with all 15 domains pending. v1 base = 237 concept
  files already merged (15 domains, 67 capabilities, 22 processes, 30 tech
  capabilities, 43 legacy + 50 modern systems, 10 glossary terms). Deep-dive adds
  L4 capabilities, tech L2/L3, and multi-granularity process flows on top.
