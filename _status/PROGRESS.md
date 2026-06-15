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
| 2 | Payments | business | todo | todo | todo | todo | todo |
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

- Domain: (none yet)
- Phase: (none) — phases are 1 Research · 2 Steward gate · 3 Author · 4 Weave · 5 Validate
- Started: (n/a)

## Next actions (ordered — keep specific enough to resume cold)

- [ ] Start the first domain: run the deep-dive prompt with DOMAIN = "Payments"
      (or any business domain). The run will: create _status/proposed-<domain>.md
      from research, pass the ontology-steward gate, author L3/L4 + tech L2/L3 +
      process-flow step notes, weave maps/indexes, validate, then set this
      domain's row to `done` and repoint these Next actions at the next domain.

## Decisions log

- (initialized) Ledger created with all 15 domains pending. v1 base = 237 concept
  files already merged (15 domains, 67 capabilities, 22 processes, 30 tech
  capabilities, 43 legacy + 50 modern systems, 10 glossary terms). Deep-dive adds
  L4 capabilities, tech L2/L3, and multi-granularity process flows on top.
