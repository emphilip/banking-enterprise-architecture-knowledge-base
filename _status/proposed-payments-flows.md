---
id: proposed-payments-flows
title: Proposed Payments Process-Flow Decomposition
type: proposal
status: draft
author: apqc-process research sub-agent
date: 2026-06-15
---

# Proposed Payments Process-Flow Decomposition

Multi-granularity process-flow decomposition for the three existing Payments-domain
processes: **Payment Processing**, **Reconciliation & Settlement**, and **Cash Management**.

Grounded in APQC PCF (Banking / Cross-Industry), Nacha ACH Rules, ISO 20022
(pain/pacs/camt), Fedwire Funds Service, TCH RTP / FedNow, and SWIFT market practice.

Relationship verbs used: `defined_in`, `derived_from`, `supersedes`, `related_to`,
`depends_on`, `causes`, `mentions`. Steps are filed as
`process-flows/<kebab-process>/NN-<kebab-step>.md`.

All canonical names below are checked against `glossary/_canonical-names.md` and are new
(no collisions with existing domains, capabilities, processes, technology capabilities,
or system names).

---

## 1. Sub-Processes

Type: `business-process`, level: `sub-process`. Each `derived_from` its parent process.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Payment Capture & Validation | business-process | sub-process | Payment Processing | Receiving, enriching and validating inbound payment instructions before they enter execution. | Payment Operations Analyst | Payment Instruction | Validated Payment Order | depends_on Payment Orchestration | — | Schema/format validation, duplicate check | Payment Intake, Capture & Validation | https://achdevguide.nacha.org/how-ach-works ; https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/ |
| Payment Authorization & Routing | business-process | sub-process | Payment Processing | Screening, authorizing and routing each payment to the correct clearing rail. | Payment Operations Analyst | Validated Payment Order | Routed Payment | depends_on Payment Orchestration | — | Sanctions screening, fraud, limit checks | Authorization & Routing, Payment Routing | https://www.iso20022payments.com/cbpr/pacs-008-serial-method/ ; https://fedwireservice.org/ |
| Clearing Submission | business-process | sub-process | Payment Processing | Formatting and transmitting cleared payments to ACH operator, Fedwire, or RTP/FedNow. | Clearing Operations Specialist | Routed Payment | Clearing Message | depends_on Payment Orchestration | — | Cut-off enforcement, message integrity | Rail Submission, Clearing Dispatch | https://achdevguide.nacha.org/how-ach-works ; https://www.frbservices.org/financial-services/ach |
| Settlement Confirmation | business-process | sub-process | Reconciliation & Settlement | Capturing settlement advices and confirming interbank money movement. | Settlement Officer | Settlement File | Confirmed Settlement | depends_on Payment Orchestration | — | Settlement finality check, dual control | Settlement Capture | https://fedwireservice.org/ ; https://www.swift.com/sites/default/files/files/pmpg-interbank-statement-creation-market-practice-final-version.pdf |
| Account Reconciliation | business-process | sub-process | Reconciliation & Settlement | Matching internal ledger entries to nostro/clearing statements and surfacing breaks. | Reconciliation Analyst | Bank Statement Message | Reconciliation Result | depends_on Core Banking Processing | — | Matching tolerance rules, segregation of duties | Statement Matching, Nostro Recon | https://www.skydo.com/blog/nostro-reconciliation ; https://corporates.dzbank.com/content/firmenkunden/en/homepage/products/transaction-banking/national-international_payments/iso-20022/camt-053-52.html |
| Exception Investigation | business-process | sub-process | Reconciliation & Settlement | Investigating, classifying and resolving reconciliation breaks and settlement failures. | Reconciliation Analyst | Reconciliation Break | Resolved Break | depends_on Workflow Orchestration | — | Break ageing, escalation workflow | Break Resolution, Investigations | https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/ |
| Cash Positioning | business-process | sub-process | Cash Management | Establishing the intraday/end-of-day cash position across accounts and currencies. | Treasury Cash Manager | Bank Statement Message | Cash Position | depends_on Core Banking Processing | — | Position sign-off, intraday limits | Position Keeping, Cash Visibility | https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/ ; https://www.jpmorgan.com/payments/solutions/treasury/liquidity |
| Liquidity Forecasting | business-process | sub-process | Cash Management | Projecting future cash needs and surpluses from positions, flows and obligations. | Treasury Cash Manager | Cash Position | Cash Forecast | depends_on Analytics Platform | — | Forecast variance review | Cash Forecasting, Liquidity Planning | https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/ |
| Funding & Concentration | business-process | sub-process | Cash Management | Executing sweeps, pooling and funding transfers to balance accounts to target. | Treasury Cash Manager | Cash Forecast | Funding Instruction | depends_on Payment Orchestration | — | Sweep parameters, approval limits | Cash Concentration, Sweeping & Pooling | https://www.nilus.com/glossary/cash-concentration ; https://www.atlar.com/guides/how-to-enable-growth-with-cash-pooling |

---

## 2. Steps — Payment Processing

Type: `process-step`, parent process: **Payment Processing**.
Files: `process-flows/payment-processing/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Receive Payment Instruction | process-step | 01 | Payment Processing | Capture an inbound payment instruction (e.g. ISO 20022 pain.001, file, or API call) from a channel or corporate. | Payment Operations Analyst | Payment Instruction | Raw Payment Order | depends_on Payment Orchestration | causes Validate Payment | Channel authentication, intake logging | Capture Instruction, Intake Payment | https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/ ; https://achdevguide.nacha.org/how-ach-works |
| Validate Payment | process-step | 02 | Payment Processing | Validate format/schema, mandatory fields, account validity and duplicates; reject or request repair on failure. | Payment Operations Analyst | Raw Payment Order | Validated Payment Order | depends_on Payment Orchestration | causes Screen Sanctions | Schema validation, duplicate/dedupe check (branch: reject vs accept) | Payment Validation, Field Validation | https://www.iso20022payments.com/cbpr/pacs-008-serial-method/ ; https://achdevguide.nacha.org/how-ach-works |
| Screen Sanctions | process-step | 03 | Payment Processing | Screen debtor, creditor and message data against sanctions/watchlists; hold and escalate hits. | Compliance Screening Officer | Validated Payment Order | Screened Payment Order | depends_on Transaction Monitoring Platform | causes Authorize Payment | Sanctions screening control (branch: hit -> hold/escalate vs clear) | Watchlist Screening Step, OFAC Screening | https://www.statestreet.com/web/insights/articles/documents/state-street-client-guide-to-iso-20022-2025.pdf ; https://www.iso20022payments.com/cbpr/pacs-008-serial-method/ |
| Authorize Payment | process-step | 04 | Payment Processing | Apply fraud scoring, limit checks and funds/credit availability; approve, hold or decline the payment. | Payment Operations Analyst | Screened Payment Order | Authorized Payment | depends_on Fraud Analytics | causes Route Payment | Fraud check, exposure/limit check, funds availability (branch: approve/hold/decline) | Payment Authorization Step, Approve Payment | https://achdevguide.nacha.org/how-ach-works ; https://fedwireservice.org/ |
| Route Payment | process-step | 05 | Payment Processing | Select the clearing rail (ACH, Fedwire, RTP/FedNow, SWIFT) based on amount, speed and destination. | Payment Operations Analyst | Authorized Payment | Routed Payment | depends_on Payment Orchestration | causes Format Clearing Message | Rail eligibility rules (branch: ACH vs wire vs instant) | Rail Selection, Payment Routing Step | https://fedwireservice.org/ ; https://www.moderntreasury.com/journal/interoperability-between-rtp-and-fednow |
| Format Clearing Message | process-step | 06 | Payment Processing | Transform the routed payment into the rail-specific message (Nacha entry, pacs.008, Fedwire format). | Clearing Operations Specialist | Routed Payment | Clearing Message | depends_on Payment Orchestration | causes Submit To Clearing | Message integrity/format control | Build Clearing Message, Message Formatting | https://www.iso20022payments.com/cbpr/pacs-008-serial-method/ ; https://achdevguide.nacha.org/how-ach-works |
| Submit To Clearing | process-step | 07 | Payment Processing | Transmit the clearing message/batch to the ACH operator, Fedwire, or RTP/FedNow within cut-off windows. | Clearing Operations Specialist | Clearing Message | Submitted Clearing Batch | depends_on Payment Orchestration | causes Capture Clearing Response | Cut-off enforcement, transmission ACK | Dispatch To Operator, Rail Submission Step | https://achdevguide.nacha.org/how-ach-works ; https://fedwireservice.org/ |
| Capture Clearing Response | process-step | 08 | Payment Processing | Ingest acknowledgements, status (pacs.002 / pain.002) and returns; update payment status and trigger repair on returns. | Payment Operations Analyst | Submitted Clearing Batch | Cleared Payment | depends_on Payment Orchestration | causes Confirm Settlement | Status reconciliation, return handling (branch: accepted vs returned) | Process Clearing Status, Return Handling | https://www.cpg.de/en/glossary/pain-002-iso-20022-message/ ; https://achdevguide.nacha.org/how-ach-works |

---

## 3. Steps — Reconciliation & Settlement

Type: `process-step`, parent process: **Reconciliation & Settlement**.
Files: `process-flows/reconciliation-and-settlement/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Confirm Settlement | process-step | 01 | Reconciliation & Settlement | Capture settlement advices from operators/correspondents and confirm interbank money movement finality. | Settlement Officer | Settlement File | Confirmed Settlement | depends_on Payment Orchestration | causes Ingest Bank Statement | Settlement finality check, dual control | Settlement Confirmation Step, Capture Settlement | https://fedwireservice.org/ ; https://bankersbank.com/solutions/fednow-rtp-settlement-solutions/ |
| Ingest Bank Statement | process-step | 02 | Reconciliation & Settlement | Load end-of-day / intraday statements (camt.053, camt.052, MT940) from nostro and clearing accounts. | Reconciliation Analyst | Bank Statement Message | Loaded Statement Data | depends_on Integration Platform | causes Match Transactions | Completeness/sequence check | Load Statement, Statement Ingestion | https://corporates.dzbank.com/content/firmenkunden/en/homepage/products/transaction-banking/national-international_payments/iso-20022/camt-053-52.html ; https://validatefin.com/en/blog/camt053-bank-statement |
| Match Transactions | process-step | 03 | Reconciliation & Settlement | Auto-match statement entries to internal ledger/payment records using references and tolerances. | Reconciliation Analyst | Loaded Statement Data | Reconciliation Result | depends_on Core Banking Processing | causes Identify Breaks | Matching tolerance rules, structured reference check | Auto Matching, Transaction Matching | https://www.skydo.com/blog/nostro-reconciliation ; https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/ |
| Identify Breaks | process-step | 04 | Reconciliation & Settlement | Surface unmatched items and discrepancies as reconciliation breaks and classify by type. | Reconciliation Analyst | Reconciliation Result | Reconciliation Break | depends_on Workflow Orchestration | causes Investigate Break | Break classification, ageing thresholds (branch: matched vs break) | Break Detection, Exception Identification | https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/ ; https://www.skydo.com/blog/nostro-reconciliation |
| Investigate Break | process-step | 05 | Reconciliation & Settlement | Investigate each break, raise investigation messages/recalls, and route to owners for resolution. | Reconciliation Analyst | Reconciliation Break | Resolved Break | depends_on Workflow Orchestration | causes Post Adjustment | Segregation of duties, escalation workflow (branch: resolve vs escalate) | Break Investigation, Exception Handling | https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/ |
| Post Adjustment | process-step | 06 | Reconciliation & Settlement | Post correcting/clearing ledger entries for resolved breaks under maker-checker control. | Settlement Officer | Resolved Break | Ledger Adjustment | depends_on General Ledger Engine | causes Sign Off Reconciliation | Maker-checker, journal authorization | Adjustment Posting, Correcting Entry | https://www.skydo.com/blog/nostro-reconciliation ; https://www.swift.com/sites/default/files/files/pmpg-interbank-statement-creation-market-practice-final-version.pdf |
| Sign Off Reconciliation | process-step | 07 | Reconciliation & Settlement | Review residual items, certify the reconciliation and produce the recon report for control/audit. | Settlement Officer | Ledger Adjustment | Reconciliation Report | depends_on Workflow Orchestration | — | Certification sign-off, audit trail | Recon Certification, Reconciliation Sign-Off | https://www.swift.com/sites/default/files/files/pmpg-interbank-statement-creation-market-practice-final-version.pdf ; https://www.skydo.com/blog/nostro-reconciliation |

---

## 4. Steps — Cash Management

Type: `process-step`, parent process: **Cash Management**.
Files: `process-flows/cash-management/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aggregate Balances | process-step | 01 | Cash Management | Collect intraday and prior-day balances across all bank accounts, entities and currencies. | Treasury Cash Manager | Bank Statement Message | Aggregated Balances | depends_on Integration Platform | causes Determine Cash Position | Balance completeness check, account coverage | Balance Aggregation, Gather Balances | https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/ ; https://www.coupa.com/products/treasury-cash-management/ |
| Determine Cash Position | process-step | 02 | Cash Management | Compute the consolidated cash position by account, currency and value date. | Treasury Cash Manager | Aggregated Balances | Cash Position | depends_on Core Banking Processing | causes Forecast Cash Flow | Position sign-off, intraday limit check | Position Calculation, Cash Positioning Step | https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/ ; https://www.jpmorgan.com/payments/solutions/treasury/liquidity |
| Forecast Cash Flow | process-step | 03 | Cash Management | Project future inflows/outflows and surpluses/shortfalls from position, schedules and history. | Treasury Cash Manager | Cash Position | Cash Forecast | depends_on Analytics Platform | causes Decide Funding Actions | Forecast variance review, scenario assumptions | Cash Forecasting Step, Liquidity Forecast | https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/ |
| Decide Funding Actions | process-step | 04 | Cash Management | Decide sweeps, concentration, investment of surplus or borrowing to cover shortfalls against targets. | Treasury Cash Manager | Cash Forecast | Funding Decision | depends_on Analytics Platform | causes Execute Funding Transfer | Target/threshold rules, approval limits (branch: invest surplus vs fund shortfall) | Funding Decisioning, Liquidity Decision | https://www.nilus.com/glossary/cash-concentration ; https://www.atlar.com/guides/how-to-enable-growth-with-cash-pooling |
| Execute Funding Transfer | process-step | 05 | Cash Management | Generate and release sweep/pooling/funding payment instructions to move cash to target balances. | Treasury Cash Manager | Funding Decision | Funding Instruction | depends_on Payment Orchestration | causes Monitor Liquidity Position | Sweep parameters, dual authorization | Sweep Execution, Funding Execution | https://www.nilus.com/glossary/cash-concentration ; https://www.atlar.com/guides/how-to-enable-growth-with-cash-pooling |
| Monitor Liquidity Position | process-step | 06 | Cash Management | Track post-funding balances and intraday liquidity against limits; alert on breaches. | Treasury Cash Manager | Funding Instruction | Liquidity Status | depends_on Analytics Platform | causes Report Cash Status | Intraday liquidity limit monitoring (branch: within limit vs breach alert) | Liquidity Monitoring, Position Monitoring | https://www.jpmorgan.com/payments/solutions/treasury/liquidity ; https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/ |
| Report Cash Status | process-step | 07 | Cash Management | Produce cash position, forecast and liquidity reports for treasury, finance and regulators. | Treasury Cash Manager | Liquidity Status | Cash Management Report | depends_on Analytics Platform | — | Reporting review, data lineage | Cash Reporting, Treasury Reporting | https://www.coupa.com/products/treasury-cash-management/ ; https://ramp.com/blog/business-banking/treasury-operations |

---

## 5. Supporting Concepts (deduped across all three flows)

Actors (`role`), business/trigger events (`event`), and artifacts/data objects (`artifact`).
For these rows the flow-specific columns (actor/inputs/outputs/depends_on/causes/controls)
are intentionally blank; definition states which flows `mention` them.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Payment Operations Analyst | role | — | — | Operations staff who capture, validate, authorize and route payments. Mentioned by Payment Processing. | | | | | | | Payment Ops Analyst, Payments Operator | https://achdevguide.nacha.org/how-ach-works |
| Clearing Operations Specialist | role | — | — | Specialist who formats and submits payments to clearing rails and handles operator dialogue. Mentioned by Payment Processing. | | | | | | | Clearing Operator, Rail Operations Specialist | https://fedwireservice.org/ |
| Compliance Screening Officer | role | — | — | Compliance role that adjudicates sanctions/watchlist hits on payments. Mentioned by Payment Processing. | | | | | | | Sanctions Officer, Screening Analyst | https://www.statestreet.com/web/insights/articles/documents/state-street-client-guide-to-iso-20022-2025.pdf |
| Settlement Officer | role | — | — | Officer who confirms settlement finality and posts settlement/adjustment entries. Mentioned by Reconciliation & Settlement. | | | | | | | Settlements Officer, Settlement Clerk | https://fedwireservice.org/ |
| Reconciliation Analyst | role | — | — | Analyst who matches statements to ledgers and investigates breaks. Mentioned by Reconciliation & Settlement. | | | | | | | Recon Analyst, Reconciliations Specialist | https://www.skydo.com/blog/nostro-reconciliation |
| Treasury Cash Manager | role | — | — | Treasury role responsible for positioning, forecasting and funding cash. Mentioned by Cash Management. | | | | | | | Cash Manager, Liquidity Manager | https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/ |
| Payment Initiated Event | event | — | — | Trigger event raised when a payment instruction is received and accepted for processing. Mentioned by Payment Processing. | | | | | | | Payment Received Event, Instruction Received | https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/ |
| Settlement Received Event | event | — | — | Event raised when a settlement advice/file is received from an operator or correspondent. Mentioned by Reconciliation & Settlement. | | | | | | | Settlement Advice Event, Settlement Notified | https://fedwireservice.org/ |
| Reconciliation Break Event | event | — | — | Event raised when an unmatched item is detected during reconciliation. Mentioned by Reconciliation & Settlement. | | | | | | | Break Raised Event, Exception Raised | https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/ |
| Cut-Off Reached Event | event | — | — | Time-based event marking a clearing-rail or value-date cut-off, triggering submission or positioning. Mentioned by Payment Processing and Cash Management. | | | | | | | Cut-Off Event, Window Closed Event | https://achdevguide.nacha.org/how-ach-works |
| Payment Instruction | artifact | — | — | Customer/channel request to move funds (e.g. ISO 20022 pain.001, file or API payload). Mentioned by Payment Processing. | | | | | | | Payment Order Request, Pain.001 Message | https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/ |
| Clearing Message | artifact | — | — | Rail-specific interbank payment message (Nacha entry, ISO 20022 pacs.008, Fedwire format). Mentioned by Payment Processing. | | | | | | | Pacs.008 Message, ACH Entry | https://www.iso20022payments.com/cbpr/pacs-008-serial-method/ |
| Settlement File | artifact | — | — | Operator/correspondent file or advice evidencing interbank settlement. Mentioned by Payment Processing and Reconciliation & Settlement. | | | | | | | Settlement Advice, Settlement Report | https://fedwireservice.org/ |
| Bank Statement Message | artifact | — | — | Account statement/reporting message used for reconciliation and positioning (camt.053/camt.052, MT940). Mentioned by Reconciliation & Settlement and Cash Management. | | | | | | | Camt.053 Statement, Account Statement | https://corporates.dzbank.com/content/firmenkunden/en/homepage/products/transaction-banking/national-international_payments/iso-20022/camt-053-52.html |
| Cash Forecast | artifact | — | — | Projection of future cash inflows, outflows and net position by value date. Mentioned by Cash Management. | | | | | | | Liquidity Forecast Report, Cash Flow Forecast | https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/ |
| Reconciliation Report | artifact | — | — | Certified output evidencing reconciliation status, breaks and adjustments for control/audit. Mentioned by Reconciliation & Settlement. | | | | | | | Recon Report, Reconciliation Certificate | https://www.swift.com/sites/default/files/files/pmpg-interbank-statement-creation-market-practice-final-version.pdf |

---

## Notes for downstream synthesis

- Granularity ladder: **Process** (existing) -> **Sub-Process** (Section 1) -> **Step**
  (Sections 2-4). Sub-processes group the ordered steps so flows can be rendered at
  either altitude.
- Steps `depends_on` existing technology capabilities (Payment Orchestration, Core
  Banking Processing, Transaction Monitoring Platform, Fraud Analytics, Workflow
  Orchestration, Integration Platform, Analytics Platform, General Ledger Engine) — all
  verbatim from `_canonical-names.md`. No new systems/capabilities were introduced.
- Controls embedded per APQC/regulatory practice: sanctions screening (step 03 Payment
  Processing), fraud + limit/exposure checks (step 04), cut-off enforcement, maker-checker
  on adjustments, segregation of duties on breaks, intraday liquidity limits.
- Hand-off chain across processes: `Capture Clearing Response` (Payment Processing)
  causes `Confirm Settlement` (Reconciliation & Settlement); `Confirm Settlement`
  produces statements consumed by `Aggregate Balances` (Cash Management). Cross-process
  `causes` links are noted in definitions, not in the in-table `causes` column, which is
  scoped to the next step within the same flow.
