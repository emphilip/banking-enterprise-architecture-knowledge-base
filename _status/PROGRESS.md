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
| 6 | Wealth & Investments | business | done | done | done | done | done |
| 7 | Risk Management | business | done | done | done | done | done |
| 8 | Compliance & Financial Crime | business | done | done | done | done | done |
| 9 | Channels & Engagement | business | done | done | done | done | done |
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

- Domain: Channels & Engagement (DONE) — 9 of 15 domains deep-dived
- Phase: DONE — all 5 eval gates 0 FAIL (1 advisory WARN: pre-existing Cards OmniPay); LLM-judge PASS after fixes incl. removing a fabricated BIAN domain (evals/judge-channels-and-engagement.md); baseline refreshed (1352 files)
- Done so far: Payments, Customer Management, Lending & Credit, Deposits & Accounts, Cards, Wealth & Investments, Risk Management, Compliance & Financial Crime, Channels & Engagement

## Next actions (ordered — keep specific enough to resume cold)

- [ ] Deepen the next domain: run _status/DEEP-DIVE-PROMPT.md with DOMAIN = "next"
      (first not-done row = Finance & Treasury — the LAST business domain). Same
      eval-gated pipeline; source-anchored Details up front; same-capability
      supersedes. Finance & Treasury has L1 Finance Management + Treasury
      Management, L2 General Ledger Accounting / Financial Reporting / Regulatory
      Capital Management / Liquidity Management / Asset Liability Management, and
      no dedicated process yet; relevant tech = General Ledger Engine, Regulatory
      Reporting Engine, Analytics Platform, Data Warehousing. Propose new processes
      (Financial Close, Management Reporting, Funds Transfer Pricing, Cash & Liquidity
      Management, Regulatory Capital Reporting). Likely needs new top-level treasury
      tech caps (e.g. Treasury Management System / ALM Engine). After Finance &
      Treasury, the 5 technology domains (11-15) remain for tech-only deepening.

## Decisions log

- (2026-06-17, Phase 2 Steward, Channels & Engagement) Reconciled the three Channels &
  Engagement proposals (bian, flows, tech) into glossary/_canonical-names.md after a
  full-registry dedupe (against every existing canonical name + every existing alias
  and across the three proposals). Counts added per section: Business capabilities +44
  (Domain=Channels & Engagement: 22 L3 + 22 L4 — 7 L3 under Digital Banking, 5 under
  Branch Banking, 6 under Contact Center, 4 under ATM Management; L4s parent to those
  L3s); Business processes +4 (Digital Onboarding Journey, Channel Servicing, ATM Cash
  Servicing [renamed], Contact Centre Interaction — Domain=Channels & Engagement);
  Technology sub-capabilities +25 (17 L2 + 8 L3 — Digital Channel Platform 9 L2 + 3 L3,
  Contact Center Platform 8 L2 + 4 L3, CRM Platform 1 L2; Domain=Channels & Engagement;
  no new top-level tech caps); Process sub-processes +10 (2 per process across Branch
  Operations + the 4 new processes — Branch Operations is now decomposed); Process flow
  steps +32 (Branch Operations 7; Digital Onboarding Journey 6; Channel Servicing 7;
  ATM Cash Servicing 6; Contact Centre Interaction 6 — Order integer contiguous per
  process); Supporting concepts +16 (6 role, 5 event, 5 artifact); Legacy systems +2
  (Kony DBX [Digital Channel Platform], Verint WFM [Contact Center Platform]); Modern
  systems +7 (Temenos Infinity, Alkami, NICE CXone, Five9, Twilio Flex, Glia, Verint
  WFM Cloud — all Digital Channel Platform or Contact Center Platform). Total +130 rows.
  Collision resolutions (the gate keeps all sections in one namespace):
  (1) "Digital Onboarding Journey" was proposed BOTH as a PROCESS (flows) and a
  TECHNOLOGY sub-capability (tech, under Digital Channel Platform). The PROCESS keeps
  the canonical "Digital Onboarding Journey"; the TECH sub-capability was renamed to
  **Onboarding Journey Orchestrator** (aliases Onboarding Journey Engine, Origination
  Front-End, Digital Onboarding Module). Its proposed alias "Digital Account Opening"
  was dropped (kept on the L3 capability "Digital Onboarding").
  (2) "ATM Cash Management" was proposed BOTH as an L3 CAPABILITY (bian, under ATM
  Management) and a PROCESS (flows). The CAPABILITY keeps the canonical "ATM Cash
  Management"; the PROCESS was renamed to **ATM Cash Servicing** (aliases ATM Cash
  Cycle, ATM Replenishment Process). All its sub-processes (ATM Cash Forecasting &
  Ordering, ATM Replenishment & Reconciliation) and steps (Forecast ATM Demand … Resolve
  Cash Discrepancy) re-parent to "ATM Cash Servicing".
  Other renames / alias fixes (avoid alias==another concept's canonical, and avoid two
  concepts sharing an alias):
  (a) Existing L4 cap "Contact Routing Management" alias "Skills-Based Routing" dropped
  (-> "Contact Skills Routing"), because the tech proposal introduces a sub-capability
  whose canonical name is "Skills-Based Routing" (under Omnichannel Routing Engine).
  (b) L3 cap "Channel Interaction Routing" alias "Skills-Based Routing" dropped (->
  "Channel Routing Capability") for the same reason.
  (c) Step "Route Interaction" (Contact Centre Interaction) aliases "Skills-Based
  Routing" / "Interaction Routing" dropped (-> "Distribute Interaction, Skills Routing
  Step"); "Interaction Routing" is an existing alias of Contact Routing Management.
  (d) L3 cap "Self-Service IVR" alias "Interactive Voice Response" dropped (-> "IVR
  Self-Service"), because the tech proposal makes "Interactive Voice Response" a
  sub-capability canonical (under Contact Center Platform).
  (e) L3 cap "ATM Cash Management" alias "ATM Cash Forecasting" dropped (-> "ATM Estate
  Cash Forecasting"), because the bian proposal also makes "ATM Cash Forecasting" an L4
  capability canonical (under ATM Cash Management).
  (f) L4 cap "Interaction Recording & Quality" alias "Quality Monitoring" dropped (->
  "Contact Quality Monitoring") — shared with tech sub-cap "Data Quality Engine".
  (g) L4 cap "Agent Desktop Servicing" alias "Unified Agent Desktop" dropped (->
  "Servicing Agent Desktop") — kept on tech sub-cap "Agent Desktop".
  (h) Tech sub-cap "Automatic Call Distribution" alias "Queue Management" dropped (->
  "ACD Engine, Call Distribution Engine") — shared with L3 cap "Branch Appointment &
  Queue".
  (i) Step "Fund Digital Account" alias "Initial Funding" dropped (-> "Fund Online
  Account, First Deposit Capture") — shared with cap "First Deposit Funding".
  (j) Step "Orchestrate Channel Journey" alias "Journey Orchestration" dropped (->
  "Channel Routing, Cross-Channel Orchestration") — shared with tech sub-cap "Campaign
  Automation".
  (k) Step "Forecast ATM Demand" alias "ATM Demand Forecast" dropped (-> "Cash
  Forecasting (ATM), Per-Terminal Forecast") — kept on artifact "ATM Cash Forecast".
  (l) Proposed-vs-proposed alias splits: sub-process "Branch Counter Servicing" ("Teller
  Servicing, Branch Counter Operations"; "Counter Operations" kept on cap "Teller
  Operations"); sub-process "Branch Cash Control" ("Vault & Drawer Control, Branch Cash
  Balancing"; "Branch Balancing" kept on step "Reconcile Branch Cash"); sub-process
  "Digital Application Intake" ("DAO Intake, Digital Intake"; "Online Application
  Capture" kept on cap "Digital Application Capture"); sub-process "Self-Service
  Resolution" ("Self-Service Handling, In-Channel Servicing"; "In-Channel Resolution"
  kept on step "Resolve Self-Service Request").
  Legacy coverage (same-capability discipline only; digital->digital, CCaaS->CCaaS):
  every new legacy has a same-capability successor — Kony DBX (Digital Channel Platform)
  <- Temenos Infinity (supersedes "Legacy Online Banking; Kony DBX"); Verint WFM
  (Contact Center Platform) <- Verint WFM Cloud. Modern CCaaS systems with no legacy peer
  carry only existing legacy targets (NICE CXone / Twilio Flex -> Avaya Aura; Five9 /
  Glia -> Cisco UCCE; Alkami -> Legacy Online Banking). Every supersedes target is a
  real legacy system. Steward gate: 0 FAIL, 1 WARN — the lone WARN ("legacy 'Fiserv
  OmniPay' has no modern successor") is the pre-existing Cards-domain legacy unrelated to
  this run; no new "no successor" WARN introduced.
- (2026-06-17, Phase 2 Steward, Compliance & Financial Crime) Reconciled the three
  Compliance & Financial Crime proposals (bian, flows, tech) into
  glossary/_canonical-names.md after a full-registry dedupe (against every existing
  canonical name + every existing alias and across the three proposals).
  Counts added per section: Business capabilities +43 (Domain=Compliance & Financial
  Crime: 1 new L2 [Financial Crime Risk Compliance, parent L1 Financial Crime
  Compliance] + 23 L3 + 19 L4 — L3s parent to KYC Management / AML Monitoring /
  Regulatory Compliance / the new Financial Crime Risk Compliance; L4s parent to those
  L3s); Business processes +3 (Customer Due Diligence Onboarding, Sanctions Screening
  Operations, Regulatory Change Management — Domain=Compliance & Financial Crime);
  Technology capabilities +1 (KYC Onboarding Platform, Domain=AI & Automation, Enables
  KYC Management / Customer Due Diligence / Customer Acquisition); Technology
  sub-capabilities +20 (16 L2 + 4 L3 [Detection Scenario Library, Watchlist Data
  Management, SAR Filing Service, Business Glossary Manager], parented to Transaction
  Monitoring Platform / Regulatory Reporting Engine / Data Governance and their L2s;
  Domain = same as parent: AI & Automation under TMP, Data & Analytics under the reg/
  data-gov caps); Process sub-processes +13 (3 KYC Verification, 2 Customer Due
  Diligence Onboarding, 2 Suspicious Activity Reporting, 2 Sanctions Screening
  Operations, 2 Regulatory Filing, 2 Regulatory Change Management; Domain=Compliance &
  Financial Crime); Process flow steps +37 (6 KYC Verification + 6 Suspicious Activity
  Reporting + 6 Regulatory Filing + 7 Customer Due Diligence Onboarding + 6 Sanctions
  Screening Operations + 6 Regulatory Change Management — Order integer contiguous per
  process; the existing KYC Verification / Suspicious Activity Reporting / Regulatory
  Filing processes are now decomposed); Supporting concepts +16 (5 role, 6 event, 5
  artifact); Legacy systems +2 (SAS Anti-Money Laundering, LexisNexis Bridger Insight —
  both realize Transaction Monitoring Platform); Modern systems +2 (Napier AI, Fenergo).
  Total +137 rows.
  Renames / collision resolutions (the gate keeps all sections in one name space):
  (1) BIAN L3 capability "Regulatory Change Management" -> **Regulatory Change
  Compliance**, because the flows proposal introduces a PROCESS named "Regulatory
  Change Management" (capability-vs-process collision); the process keeps the plain
  name, and the L4 child "Obligation Mapping" parents to "Regulatory Change Compliance".
  The capability's alias "Horizon Scanning" was dropped (kept on the flows sub-process
  "Horizon Scanning & Impact") and replaced with "Regulatory Change Interpretation".
  (2) Existing process "Suspicious Activity Reporting" alias "SAR Filing" -> **SAR
  Process**, so the new flows ARTIFACT "SAR Filing" can take that canonical name
  (alias-vs-canonical clash; the artifact is the load-bearing deliverable referenced by
  step outputs).
  (3) New flows step "Assess Change Impact" (Regulatory Change Management, order 3) ->
  **Assess Regulatory Impact**, because an existing step "Assess Change Impact"
  (Account Maintenance, order 3) already carries that canonical name and the alias
  "Impact Assessment Step"; the new step's alias became "Regulatory Impact Assessment
  Step".
  Alias-only fixes (avoid alias==another concept's canonical, and avoid two concepts
  sharing an alias):
  (a) tech sub-cap "Detection Scenario Library" dropped alias "Scenario Catalogue"
  (== alias of cap "Scenario Library Management").
  (b) tech sub-cap "Network Entity Resolution" dropped alias "Contextual Decision
  Intelligence" (== alias of system "Quantexa").
  (c) tech sub-cap "Report Validation Service" dropped alias "Validation Engine"
  (== alias of tech sub-cap "Payment Validation Engine").
  (d) sub-process "Identity Proofing & Verification" dropped alias "Identity
  Verification" (== capability canonical) -> "CIP Verification".
  (e) sub-process "SAR Decision & Filing" dropped alias "SAR Filing" (== artifact
  canonical / process alias) -> kept "STR Decision".
  (f) steps "Validate Customer Identity" / "Screen Against Watchlists" / "Open
  Investigation Case" dropped aliases "Identity Proofing Step" / "Watchlist Screening
  Step" / "Case Opening Step" respectively (each an existing step alias).
  (g) artifact "Customer Risk Score" dropped alias "Customer Risk Rating" (== new
  capability canonical) -> "CDD Risk Score, Customer Risk Tier".
  (h) artifact "SAR Filing" dropped alias "STR Filing" (shared with cap "SAR Filing &
  Tracking", which keeps it) -> "Suspicious Activity Report, FinCEN Form 111".
  (i) sub-process "Ongoing KYC Monitoring" dropped aliases "Periodic Review" /
  "Perpetual KYC" (shared with cap "KYC Refresh Management", which keeps them) ->
  "Ongoing Monitoring, KYC Refresh".
  Reuse handling (NOT re-added — flows steps/sub-processes reference the existing rows):
  artifact **KYC Profile** (Customer Management; alias "CDD Profile") reused across KYC
  Verification / Customer Due Diligence Onboarding; roles **Compliance Screening
  Officer** (Sanctions Screening Operations) and **KYC Analyst** (KYC Verification / CDD
  Onboarding) reused. So supporting concepts added 16, not the 17 declared in the flows
  proposal.
  Systems classification & legacy coverage (same-capability discipline only):
  Legacy = SAS Anti-Money Laundering and LexisNexis Bridger Insight (both realize
  Transaction Monitoring Platform). Modern = Napier AI (Transaction Monitoring Platform)
  supersedes "SAS Anti-Money Laundering; LexisNexis Bridger Insight" — the watchlist-
  screening legacy LexisNexis Bridger Insight was given its same-capability successor by
  appending it to Napier AI's supersedes (both TMP), so both new legacies are covered;
  Fenergo (KYC Onboarding Platform) is greenfield realizing the brand-new tech cap and
  correctly carries NO supersedes (blank cell). Every supersedes target is a real
  legacy system; no new "no successor" WARN introduced. Steward gate: 0 FAIL, 1 WARN —
  the lone WARN ("legacy 'Fiserv OmniPay' has no modern successor") is the pre-existing
  Cards-domain legacy unrelated to this run.
- (2026-06-16, Phase 2 Steward, Risk Management) Reconciled the three Risk Management
  proposals (bian, flows, tech) into glossary/_canonical-names.md after a full-registry
  dedupe pass (against all existing canonical names + all ~1,739 existing aliases and
  across the three proposals). Counts added per section: Technology capabilities +4
  (Risk Analytics Engine [AI & Automation], Model Risk Management Platform [AI &
  Automation], Risk Data Aggregation [Data & Analytics], Governance Risk & Compliance
  Platform [Data & Analytics]); Business capabilities +40 (Domain=Risk Management:
  6 L2 + 22 L3 + 12 L4 — the 6 cross-cutting capabilities parent to L1 Enterprise Risk
  Management, the per-risk-type L3/L4s parent to the existing L2s Credit/Market/
  Operational/Liquidity Risk Management and Fraud Management); Business processes +4
  (Risk Appetite Setting, Risk Identification & Assessment, Stress Testing, Risk
  Reporting — Domain=Risk Management); Technology sub-capabilities +13 (12 L2 + 1 L3
  [Counterparty Risk & XVA Service under Market Risk Engine], parented to the 4 new
  top-level risk tech caps, Domain AI & Automation or Data & Analytics per proposal);
  Process sub-processes +14 (2 Fraud Detection, 2 Fraud Investigation, 2 Risk Appetite
  Setting, 3 Risk Identification & Assessment, 2 Stress Testing, 3 Risk Reporting,
  Domain=Risk Management); Process flow steps +34 (5 Fraud Detection, 6 Fraud
  Investigation, 5 Risk Appetite Setting, 6 Risk Identification & Assessment, 6 Stress
  Testing, 6 Risk Reporting — Order integer contiguous per process; the existing Fraud
  Detection / Fraud Investigation processes are now decomposed); Supporting concepts +18
  (6 role, 6 event, 6 artifact); Legacy systems +8; Modern systems +8. Total +143 rows.
  Renames / collision resolutions (the gate stores all sections in one name space, so a
  capability and a process sharing a canonical name FAILs):
  (1) BIAN L3 capability "Stress Testing" -> **Stress Testing Management**, because the
  flows proposal introduces a process named "Stress Testing" (capability-vs-process
  collision); the process keeps the plain name, and the L4-child "Scenario Library
  Management" re-parents to "Stress Testing Management". Aliases: Scenario Stress
  Testing, Reverse Stress Testing, CCAR Stress Testing.
  (2) Flows sub-process "Risk Identification" -> **Risk Capture & Registration**,
  because the BIAN proposal introduces an L2 capability "Risk Identification"; the
  capability keeps the plain name (it is the more permanent concept and a system/sub-cap
  anchor).
  (3) Flows sub-process "Risk Data Aggregation" -> **Reporting Data Aggregation**,
  because the tech proposal introduces a top-level tech capability "Risk Data
  Aggregation" (systems realize it, sub-caps derive from it); the tech cap keeps the
  plain name.
  Level adjustment for gate monotonicity (parent must be exactly one level above):
  the 6 enterprise-wide capabilities the BIAN proposal authored as L3 under L1
  Enterprise Risk Management (Risk Appetite Management, Risk Identification, Stress
  Testing Management, Model Risk Management, Regulatory Capital Adequacy, Risk Reporting
  & Governance) were set to **L2** (direct children of the L1, siblings of the existing
  risk L2s), and their three L4 children (Risk Capital Calculation, Scenario Library
  Management, Model Inventory Management) were promoted to **L3** — preserving the
  proposed hierarchy intent while satisfying L<n>->L<n-1> monotonicity.
  Alias-only fixes (avoid alias==another concept's canonical name and avoid two
  concepts sharing an alias):
  (a) cap "Risk Capital Calculation" alias "Economic Capital Engine" (== tech sub-cap
  canonical) -> "Capital Charge Engine".
  (b) cap "Risk Reporting & Governance" alias "Risk Data Aggregation" (== tech cap
  canonical) -> "Risk Data Aggregation & Governance"; dropped shared alias "Board Risk
  Reporting" (kept on process "Risk Reporting").
  (c) process "Risk Identification & Assessment" dropped aliases "Risk Identification"
  (== cap canonical) and "RCSA" (shared w/ cap "Risk & Control Self-Assessment") ->
  "Risk Assessment, Risk ID & Assessment".
  (d) process "Risk Appetite Setting" dropped shared alias "Risk Appetite Framework"
  (kept on cap "Risk Appetite Management") -> "RAF Process, Appetite Setting".
  (e) cap "Value-at-Risk Calculation" dropped alias "VaR Engine" (kept on tech sub-cap
  "Market Risk Engine") -> "Expected Shortfall Calculation, VaR/ES".
  (f) sub-process "Scenario Design & Governance" dropped aliases "Scenario Design"
  (kept on cap "Scenario Library Management") and "Model Governance" (kept on cap
  "Model Risk Management") -> "Scenario Build & Governance, Stress Scenario Design".
  (g) sub-process "Limit Monitoring & Escalation" dropped alias "Limit Monitoring"
  (kept on cap "Limit & Exposure Management") -> "Limit Tracking, Breach Escalation".
  (h) sub-process "Disposition & Recovery" dropped alias "Resolution & Recovery"
  (== existing alias of Cards sub-process "Dispute Resolution & Recovery") ->
  "Disposition & SAR, Fraud Resolution & Recovery".
  Fraud Alert reuse: the existing Cards artifact **Fraud Alert** was NOT re-added; the
  flows steps/sub-processes that mention it (Generate/Route Fraud Alert, Adjudicate
  Fraud Alert, Real-Time Risk Scoring, etc.) reference the single existing Supporting-
  concepts row. Supporting concepts therefore added 18, not 19.
  Systems classification & legacy coverage (same-capability discipline only):
  Legacy +8 — Risk Analytics Engine: SAS Risk Management for Banking, Oracle OFSAA,
  Moody's RiskFrontier, IBM Algorithmics, FIS Adaptiv; Risk Data Aggregation: Moody's
  RiskAuthority; GRC Platform: IBM OpenPages, Archer IRM. Modern +8 — Murex MX.3 Risk
  (Risk Analytics Engine) supersedes FIS Adaptiv; Oracle OFSAA; MSCI RiskMetrics (Risk
  Analytics Engine) supersedes IBM Algorithmics; SAS Risk Management for Banking;
  Numerix Oneview (Risk Analytics Engine) supersedes Moody's RiskFrontier; Quantexa
  (Risk Data Aggregation) supersedes Moody's RiskAuthority; ServiceNow IRM (GRC)
  supersedes Archer IRM; MetricStream (GRC) supersedes IBM OpenPages; ValidMind and
  ModelOp (Model Risk Management Platform) are greenfield model-risk tooling with NO
  same-capability legacy in the registry, so they correctly carry NO supersedes (blank
  cell). SAS RMfB and Oracle OFSAA had no 1:1 modern in the proposal; rather than leave
  benign WARNs, they were paired same-capability to MSCI RiskMetrics / Murex MX.3 Risk
  (both broad Risk Analytics Engine suites) via "; " — no cross-capability supersede was
  forced. Every supersedes target is a real legacy system; all 8 new risk legacies now
  have a same-capability modern successor. Steward gate: 0 FAIL, 1 WARN — the lone WARN
  ("legacy 'Fiserv OmniPay' has no modern successor") is the pre-existing Cards-domain
  legacy unrelated to this run; no new "no successor" WARNs introduced.
- (2026-06-16, Phase 2 Steward, Wealth & Investments) Reconciled the three Wealth &
  Investments proposals (bian, flows, tech) into glossary/_canonical-names.md.
  Counts added per section: Technology capabilities +3 (Portfolio Management System,
  Order Management System, Investment Advisory Platform — all Domain=Core Processing,
  Enables = Portfolio Management / Brokerage & Trading / Investment Advisory
  respectively); Business capabilities +37 (18 L3 + 19 L4, all Domain=Wealth &
  Investments — 6 L3 under Portfolio Management, 6 under Investment Advisory, 6 under
  Brokerage & Trading; L4s parented to those L3s); Business processes +4 (Financial
  Planning, Portfolio Rebalancing, Trade Order Management, Performance Reporting,
  Domain=Wealth & Investments); Technology sub-capabilities +14 (11 L2 under the 3 new
  top-level wealth tech caps + 3 L3 under Rebalancing Engine / Order Routing Engine /
  Risk Profiling Engine, all Domain=Core Processing); Process sub-processes +12 (2
  Wealth Onboarding, 3 Financial Planning, 2 Portfolio Rebalancing, 3 Trade Order
  Management, 2 Performance Reporting); Process flow steps +31 (6 Wealth Onboarding,
  6 Financial Planning, 6 Portfolio Rebalancing, 7 Trade Order Management, 6
  Performance Reporting — Order integer contiguous per process); Supporting concepts
  +16 (6 role, 5 event, 5 artifact); Legacy systems +6; Modern systems +7. Total +130
  rows.
  Renames / collision resolutions:
  (1) BIAN L3 capability "Portfolio Rebalancing" -> **Portfolio Rebalancing
  Management**, because the flows proposal introduces a process also named "Portfolio
  Rebalancing" (capability-vs-process collision, per the registry naming rule). The
  process keeps the plain name "Portfolio Rebalancing"; the two L4 children
  (Tolerance Band Monitoring, Tax-Loss Harvesting) were re-parented to "Portfolio
  Rebalancing Management". Its aliases were set to "Rebalancing Capability, Drift
  Management Capability" to avoid sharing "Rebalancing"/"Drift Management" with the
  process.
  (2) BIAN L3 capability "Financial Planning" -> **Financial Planning Advisory**,
  because the flows proposal introduces a process named "Financial Planning". The
  process keeps the plain name; the capability's aliases became "Wealth Planning
  Capability, Comprehensive Planning" (process keeps "Wealth Planning, Advice
  Process"). No L4 children parent to this capability, so no re-parenting needed.
  Alias-only adjustments (avoid alias==other-concept canonical, and avoid two
  concepts sharing an alias):
  (a) tech cap "Order Management System" dropped alias "Trade Order Management"
  (equals the new process canonical name).
  (b) BIAN cap "Portfolio Accounting" dropped aliases "Investment Book of Record" /
  "IBOR" (kept on tech cap "Portfolio Management System"); replaced with "Investment
  Bookkeeping, Investment Book of Record Capability".
  (c) tech sub-cap "Order Routing Engine" dropped alias "Smart Order Routing" (kept on
  BIAN L4 cap "Order Routing").
  (d) sub-process "Investor Profiling & Suitability" dropped alias "Investor Profiling"
  (kept on cap "Suitability Assessment") -> "Investor Profiling Sub-Process".
  (e) sub-process "Routing & Execution" dropped alias "Best Execution" (kept on cap
  "Trade Execution") -> "Order Execution Sub-Process".
  (f) sub-process "Rebalance Compliance & Approval" dropped alias "Pre-Trade
  Compliance" (kept on tech sub-cap "Pre-Trade Compliance Engine") -> "Rebalance
  Pre-Trade Compliance".
  (g) support event "Rebalance Triggered Event" alias "Rebalance Trigger" ->
  "Rebalance Trigger Event" (kept "Rebalance Trigger" on cap "Tolerance Band
  Monitoring").
  (h) step "Settle Trade" alias "Trade Settlement Step" -> "Settle Securities Trade
  Step" (the string "Trade Settlement Step" is an existing alias of the Trade Finance
  step "Settle Trade Payment").
  Temenos WealthSuite classification: classified as a **LEGACY** Investment Advisory
  Platform system (advisory incumbent), since InvestCloud and Envestnet supersede it.
  Legacy coverage (same-capability successors only): FIS Global Plus (PMS) <- SimCorp
  One; SunGard Asset Arena (PMS) <- BlackRock Aladdin, SimCorp One; SS&C Advent Geneva
  (PMS) <- BlackRock Aladdin, Addepar; Broadridge Portfolio Master (PMS,
  generic/representative — vendor marked "Broadridge (representative)") <- Addepar;
  SS&C Advent Moxy (OMS) <- Charles River IMS, Bloomberg AIM; Temenos WealthSuite
  (advisory) <- InvestCloud, Envestnet. Every new legacy has at least one
  same-capability modern successor; every supersedes target is a real legacy system;
  no cross-capability pairing. Steward gate: 0 FAIL, 1 WARN — the lone WARN ("legacy
  'Fiserv OmniPay' has no modern successor") is a pre-existing Cards-domain legacy
  unrelated to this run; no new "no successor" WARNs introduced.
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
