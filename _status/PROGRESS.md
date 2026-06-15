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
| 1 | Customer Management | business | done | done | done | done | done |
| 2 | Payments | business | done | done | done | done | done |
| 3 | Lending & Credit | business | done | done | done | done | done |
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

- Domain: Lending & Credit (DONE) — 3 of 15 domains deep-dived (Payments, Customer Management, Lending & Credit)
- Phase: DONE — all 5 eval gates 0 FAIL; LLM-judge PASS first pass (evals/judge-lending-and-credit.md); baseline refreshed (562 files)

## Next actions (ordered — keep specific enough to resume cold)

- [ ] Deepen the next domain: run _status/DEEP-DIVE-PROMPT.md with DOMAIN = "next"
      (first not-done row = Deposits & Accounts). Same eval-gated pipeline;
      instruct capability authors to write source-anchored Details up front
      (proven to clear the Groundedness gate on the first judge pass).

## Decisions log

- (2026-06-15, Phase 2 Steward, Lending & Credit) Reconciled the three Lending &
  Credit proposals (bian, flows, tech) into glossary/_canonical-names.md. Counts
  added per section: Business capabilities +40 (19 L3, 21 L4, all Domain=Lending &
  Credit); Technology sub-capabilities +13 (10 L2 under Loan Origination Platform /
  Credit Decisioning Engine, 3 L3, all Domain=Core Processing); Process
  sub-processes +12 (3 Loan Origination Workflow, 2 Credit Underwriting, 3 Mortgage
  Origination, 2 Loan Collections, 2 Trade Finance Processing); Process flow steps
  +32 (7 Loan Origination Workflow, 6 Credit Underwriting, 7 Mortgage Origination,
  6 Loan Collections, 6 Trade Finance Processing); Supporting concepts +19 (8 role,
  5 event, 6 artifact); Legacy systems +4 (Ellie Mae Encompass, Finastra LaserPro,
  FICO Origination Manager, Experian PowerCurve); Modern systems +3 (Temenos
  Origination, MeridianLink, Provenir). Total +123 rows. Renames (all of colliding
  proposed ALIASES, not canonical names — no canonical-name collisions existed):
  (1) sub-process "Application Origination & Pre-Qualification" alias "Origination
  Intake" -> "Origination Pre-Qualification" (Origination Intake is an existing
  alias of Application Processing). (2) sub-process "Late-Stage Recovery" alias
  "Recoveries" -> "Late Collections" (Recoveries is an existing alias of Collections
  & Recovery). (3) supporting artifact "Credit Decision" alias "Underwriting
  Decision" -> "Underwriting Outcome" (Underwriting Decision is an existing alias of
  Credit Decisioning). Coverage: every new legacy has a modern successor — Ellie Mae
  Encompass <- Temenos Origination, MeridianLink; Finastra LaserPro <- Temenos
  Origination; FICO Origination Manager <- Provenir; Experian PowerCurve <- Provenir.
  No "no successor" WARNs. Steward gate: 0 FAIL, 0 WARN.
- (2026-06-15, Phase 2 Steward, Customer Management) Reconciled the three
  Customer Management proposals (bian, flows, tech) into
  glossary/_canonical-names.md. Counts added per section: Business capabilities
  +34 (14 L3, 20 L4); Technology sub-capabilities +16 (12 L2, 4 L3); Process
  sub-processes +8; Process flow steps +24 (9 Customer Onboarding, 8 Complaint
  Handling, 7 Service Request Handling); Supporting concepts +17 (5 role, 5
  event, 7 artifact); Legacy systems +2 (SAP CRM, Informatica MDM); Modern
  systems +4 (Microsoft Dynamics 365, Pega Customer Service, Reltio, Amazon Lex).
  Total +105 rows. Renames: (1) the tech proposal's L2 "Virtual Assistant" was
  renamed to **Self-Service Virtual Assistant** because "Virtual Assistant" is an
  existing alias of the Conversational AI technology capability — the
  "Virtual Assistant" alias was dropped (kept Digital Assistant, Customer
  Chatbot). (2) The tech sub-capability "Consent Management Service" had its
  proposed alias "Consent & Preference Management" dropped (replaced with Consent
  Service) because that string is now the canonical name of the new L3 business
  capability Consent & Preference Management; alias-equals-canonical would FAIL
  the gate. Coverage: SAP CRM ← Microsoft Dynamics 365; Siebel CRM ← Pega
  Customer Service (in addition to existing Salesforce FSC); Informatica MDM ←
  Reltio; Legacy IVR System ← Amazon Lex (in addition to existing Kasisto). Both
  new legacy systems received successors, so no new "no successor" WARNs.
  Steward gate: 0 FAIL, 0 WARN.
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
