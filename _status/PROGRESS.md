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
| 4 | Deposits & Accounts | business | done | done | done | done | done |
| 5 | Cards | business | done | done | done | done | done |
| 6 | Wealth & Investments | business | todo | todo | todo | todo | in-progress |
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

- Domain: Wealth & Investments
- Phase: 1 Research (in-progress) — 3 sub-agents writing _status/proposed-wealth-and-investments-{bian,flows,tech}.md. NOTE: domain has no top-level tech capability yet; tech agent proposes NEW top-level wealth tech caps + decomposition + first wealth systems.
- Done so far: Payments, Customer Management, Lending & Credit, Deposits & Accounts, Cards (5 of 15)

## Next actions (ordered — keep specific enough to resume cold)

- [ ] Deepen the next domain: run _status/DEEP-DIVE-PROMPT.md with DOMAIN = "next"
      (first not-done row = Wealth & Investments). Same eval-gated pipeline;
      capability authors must write source-anchored Details up front. Wealth has
      L1 Wealth Management + L2 Portfolio Management / Investment Advisory /
      Brokerage & Trading and 1 process (Wealth Onboarding) — propose 2-3 new
      processes (e.g. Portfolio Rebalancing, Trade Execution, Suitability
      Assessment) for flow coverage. Watch supersedes: ensure same-capability
      (issuer vs acquirer, etc.) to avoid the relationship-sensibility floor.

## Decisions log

- (2026-06-15, Phase 2 Steward, Cards) Reconciled the three Cards proposals (bian,
  flows, tech) into glossary/_canonical-names.md. Most capability/process/tech-subcap/
  sub-process rows from the proposals were already present in the registry from an
  earlier reconciliation pass; this run completed the remaining deep-dive sections.
  Counts added per section: Business capabilities +0 (all 31 proposed Cards L3/L4
  already present, lines 267-297); Business processes +0 (3 new processes Card
  Transaction Authorization, Chargeback Processing, Card Fraud Handling already in
  table with Domain=Cards and 1-3 existing-capability dependencies); Technology
  sub-capabilities +0 (11 already present under Card Processing / Card Authorization
  Engine / Card Tokenization Service, Domain=Core Processing); Process sub-processes
  +0 (14 already present); Process flow steps +32 (7 Card Issuance + 6 Dispute
  Resolution + 7 Card Transaction Authorization + 6 Chargeback Processing + 6 Card
  Fraud Handling, each with Order integer per process and a real Depends-On tech cap);
  Supporting concepts +15 (4 role, 5 event, 6 artifact); Legacy systems +3 (FIS Card
  Management, Fiserv OmniPay, Fiserv Optis — all realize Card Processing); Modern
  systems +5 (Thredd, Lithic, i2c, Pismo, Episode Six — all realize Card Processing).
  Total +55 rows this run. Renames / collision resolutions: none required this run —
  the previously-reconciled rows already carried the earlier disambiguations
  (capability "Chargeback Handling" distinct from process "Chargeback Processing";
  capability "Card Application" distinct from artifact "Card Account Application";
  sub-process "Authorization Validation & Decisioning" disambiguated from capability
  "Authorization Decisioning"; sub-process "Dispute Intake & Investigation" alias
  trimmed to "Dispute Intake" because "Dispute Investigation"/"Claim Investigation"
  are a canonical cap and its alias). The 32 step names are verb-form and globally
  unique; no step name or step alias equals any other concept's canonical name.
  Coverage — every new legacy has a modern successor, with the 3 new legacies covered
  by appending via "; " to suitable moderns: FIS Card Management <- Pismo (supersedes
  "TSYS TS2; FIS Card Management"); Fiserv OmniPay <- Thredd (supersedes "First Data
  Cards; Fiserv OmniPay"); Fiserv Optis <- i2c (supersedes "TSYS TS2; Fiserv Optis").
  Existing legacy targets TSYS TS2 / First Data Cards retained (also covered by
  Lithic and Episode Six -> First Data Cards). No new legacy left without a successor;
  every supersedes target is a real legacy system. Steward gate: 0 FAIL, 0 WARN.
- (2026-06-15, Phase 2 Steward, Deposits & Accounts) Reconciled the three Deposits
  & Accounts proposals (bian, flows, tech) into glossary/_canonical-names.md. Counts
  added per section: Business capabilities +45 (23 L3, 22 L4, all Domain=Deposits &
  Accounts; 5 L3 under Account Opening, 10 under Account Servicing, 5 under Interest
  Calculation, 3 under Overdraft Management); Business processes +3 (Account
  Maintenance, Account Closure, Overdraft Servicing — Domain=Deposits & Accounts,
  Depends on existing caps Account Servicing / Overdraft Management); Technology
  sub-capabilities +11 (8 L2 under Core Banking Processing, 3 L3, all Domain=Core
  Processing); Process sub-processes +11 (2 Deposit Account Opening, 2 Statement
  Generation, 2 Account Maintenance, 3 Account Closure, 2 Overdraft Servicing);
  Process flow steps +32 (7 Deposit Account Opening, 7 Statement Generation, 6
  Account Maintenance, 7 Account Closure, 6 Overdraft Servicing); Supporting concepts
  +18 (4 role, 5 event, 9 artifact); Legacy systems +3 (Fiserv Premier, Jack Henry
  Core Director, FIS Horizon); Modern systems +3 (SAP Deposits Management, Tuum,
  SaaScada). Total +126 rows. Renames (no canonical-name vs canonical-name collisions
  existed; these resolve a proposed-canonical-vs-existing-alias clash and a
  proposed-vs-proposed clash): (1) BIAN L4 capability "Statement Production" ->
  **Deposit Statement Production**, because "Statement Production" is already the
  alias of the existing process "Statement Generation". (2) BIAN L4 capability
  "Statement Delivery" -> **Deposit Statement Delivery**, because the flows proposal
  introduces a sub-process also named "Statement Delivery" (proposed-vs-proposed
  duplicate); the sub-process keeps the plain name. Alias adjustment: the new process
  "Account Closure" alias "Account Termination" was changed to **Deposit Account
  Closure** to avoid duplicating the alias "Account Termination" already carried by
  the new L3 cap "Account Closure Servicing". Coverage: every new legacy has a modern
  successor — Fiserv Premier <- Tuum; Jack Henry Core Director <- SaaScada; FIS
  Horizon <- SAP Deposits Management (added via "; " to SAP Deposits Management's
  supersedes alongside Legacy Mainframe Core; SAP Deposits Management chosen over
  Thought Machine Vault as the better capability-level fit since FIS Horizon is a
  deposit/loan community-bank core and SAP Deposits Management is a deposit-specific
  banking core). No "no successor" WARNs. Steward gate: 0 FAIL, 0 WARN.
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
