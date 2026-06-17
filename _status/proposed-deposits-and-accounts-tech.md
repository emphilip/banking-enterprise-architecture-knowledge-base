---
title: Proposed Deposits & Accounts Technology Decomposition
type: proposal
status: draft
author: tech-decomposition sub-agent
date: 2026-06-15
---

# Proposed Deposits & Accounts Technology Decomposition

Scope: enabling technology-capability decomposition for the Deposits & Accounts
domain's core enabling technology capability, **Core Banking Processing** (the
EXISTING parent in the Core Processing technology domain), plus a systems
refresh of notable deposit/core platforms not already covered.

Grounding: core-banking / deposit-system reference architectures and vendor docs
(Thought Machine Vault Core's Universal Product Engine, smart contracts and
Postings/Streaming APIs; Finxact's multi-position, event-driven, batch-free
core; Mambu deposit account lifecycle, interest application and withholding;
SAP Deposits Management contract lifecycle for current/savings/term accounts),
plus general core-banking component models (transaction posting, interest
accrual & capitalisation, service-charge calculation, tiered pricing, zero/
target-balance cash management, sub-ledger-to-GL reconciliation) and
cloud-native patterns (real-time posting, CQRS/event-sourcing ledgers).

Naming verified globally unique against `glossary/_canonical-names.md`. Tech
names are deliberately kept distinct from the Deposits & Accounts business
capabilities and processes, e.g.:
- tech "Deposit Account Management" vs business cap "Account Servicing" / domain "Deposits"
- tech "Interest & Charges Engine" vs business cap "Interest Calculation"
- tech "Account Statement Generator" vs process "Statement Generation"
- tech "Account Lifecycle Manager" vs business cap "Account Opening" / "Account Servicing"
- tech "General Ledger Posting" (sub-cap of Core Banking Processing) vs tech cap "General Ledger Engine" and business cap "General Ledger Accounting"
- tech "Standing Order & Sweep Engine" vs business cap "Standing Order Management" (Payments) and process "Funding & Concentration"

Also checked against payments and lending tech sub-caps already added (e.g.
"Settlement Instruction Engine", "Disbursement Engine", "Offer & Pricing
Engine") — no clashes.

Relationship verbs used (of the allowed 7): `derived_from`, `defined_in`,
`depends_on`, `related_to`.

## 1) Technology sub-capabilities

All `type = technology-capability`, `domain = Core Processing`,
`parent = Core Banking Processing` (L2 rows) and the named L2 (L3 rows).

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Deposit Account Management | technology-capability | L2 | Core Banking Processing | Core Processing | Maintains the system-of-record for deposit accounts (current, savings, term/fixed deposits): account master data, balances, holds, multi-currency positions and account-level configuration as the authoritative core record. | Account Master Service, Deposit Account Service, Account System of Record | derived_from Core Banking Processing; defined_in Core Processing; related_to Account Servicing | https://www.thoughtmachine.net/vault-core ; https://help.sap.com/docs/SAP_FOR_BANKING/b0c17eb728054c5e92d73923f704edd7/53ffbdb976794b099a360da5b4ec88b6.html |
| Transaction Posting Engine | technology-capability | L2 | Core Banking Processing | Core Processing | Posts debits and credits to deposit accounts and the core ledger, applying value dating, balance updates, funds availability and double-entry integrity for both real-time and batch transaction streams. | Posting Engine, Core Ledger Posting, Postings Service | derived_from Core Banking Processing; defined_in Core Processing; related_to Account Servicing | https://www.thoughtmachine.net/blog/product-development ; https://aws.amazon.com/blogs/apn/meeting-bank-grade-requirements-for-real-time-and-resilient-core-banking-with-finxact-on-aws/ |
| Product & Pricing Engine | technology-capability | L2 | Core Banking Processing | Core Processing | Configures deposit products and their terms, tiers, fee schedules and pricing rules without code, enabling rapid product manufacture and parameter-driven product behaviour. | Deposit Product Engine, Product Configurator (Deposits), Universal Product Engine | derived_from Core Banking Processing; defined_in Core Processing; related_to Deposits | https://www.thoughtmachine.net/vault-core ; https://development.saascada.com/platform/real-time-data/ |
| Interest & Charges Engine | technology-capability | L2 | Core Banking Processing | Core Processing | Calculates daily interest accruals, capitalisation/payment, tiered and bonus rates, service charges, fees and withholding tax for interest-bearing and fee-bearing deposit accounts. | Accrual Engine, Interest & Fee Engine, Charges Engine | derived_from Core Banking Processing; defined_in Core Processing; related_to Interest Calculation | https://docs.mambu.com/docs/profit-sharing-deposit-account-life-cycle-and-states/ ; https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products |
| Account Statement Generator | technology-capability | L2 | Core Banking Processing | Core Processing | Produces periodic and on-demand account statements and transaction histories (incl. ISO 20022 camt.05x), assembling balances, postings, interest and fees for delivery to channels and document services. | Statement Engine, Statement Production Service, Statement Generator | derived_from Core Banking Processing; defined_in Core Processing; related_to Statement Generation; depends_on Document Management | https://www.iso20022.org/iso-20022-message-definitions ; https://www.alogent.com/banking-definitions/core-banking-systems |
| Standing Order & Sweep Engine | technology-capability | L2 | Core Banking Processing | Core Processing | Executes scheduled and rule-based account movements: standing orders, recurring internal transfers, zero/target-balance sweeps and cash-concentration/pooling between deposit accounts. | Sweep Engine, Scheduled Transfer Engine, Cash Concentration Engine | derived_from Core Banking Processing; defined_in Core Processing; related_to Standing Order Management | https://www.alogent.com/banking-definitions/core-banking-systems ; https://tuum.com/ |
| General Ledger Posting | technology-capability | L2 | Core Banking Processing | Core Processing | Aggregates core sub-ledger entries into GL postings, maintains the chart-of-accounts mapping and reconciles deposit sub-ledgers upward to the institution-wide general ledger. | Sub-Ledger to GL Posting, GL Interface Service, Core GL Bridge | derived_from Core Banking Processing; defined_in Core Processing; depends_on General Ledger Engine; related_to General Ledger Accounting | https://sdk.finance/blog/what-is-a-general-ledger-core-concepts/ ; https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products |
| Account Lifecycle Manager | technology-capability | L2 | Core Banking Processing | Core Processing | Drives deposit account state transitions through the lifecycle — opening, activation, dormancy, hold/freeze, maturity/rollover for term deposits and closure — enforcing lifecycle rules in the core. | Account State Engine, Deposit Lifecycle Engine, Account Status Manager | derived_from Core Banking Processing; defined_in Core Processing; related_to Account Opening; related_to Account Servicing | https://docs.mambu.com/docs/profit-sharing-deposit-account-life-cycle-and-states/ ; https://help.sap.com/docs/SAP_FOR_BANKING/b0c17eb728054c5e92d73923f704edd7/53ffbdb976794b099a360da5b4ec88b6.html |
| Real-Time Posting Service | technology-capability | L3 | Transaction Posting Engine | Core Processing | Provides low-latency, idempotent real-time posting and instant balance updates (event-driven, replacing overnight batch), exposing a postings API and a streaming event feed of ledger changes. | Real-Time Ledger Service, Instant Posting Service, Streaming Postings | derived_from Transaction Posting Engine; defined_in Core Processing; depends_on Data Streaming | https://www.thoughtmachine.net/blog/product-development ; https://aws.amazon.com/blogs/apn/meeting-bank-grade-requirements-for-real-time-and-resilient-core-banking-with-finxact-on-aws/ |
| Tiered Interest Calculator | technology-capability | L3 | Interest & Charges Engine | Core Processing | Computes interest under tiered, banded and bonus-rate structures, applying balance-tier rules, promotional/bonus conditions and day-count conventions to deposit balances. | Tiered Rate Calculator, Banded Interest Service, Bonus Rate Engine | derived_from Interest & Charges Engine; defined_in Core Processing; related_to Interest Calculation | https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products ; https://www.alogent.com/banking-definitions/core-banking-systems |
| Dormancy & Escheatment Service | technology-capability | L3 | Account Lifecycle Manager | Core Processing | Detects inactive/dormant deposit accounts, applies dormancy rules and charges, and manages unclaimed-property escheatment workflows and reporting within the core. | Dormancy Engine, Unclaimed Property Service, Escheatment Service | derived_from Account Lifecycle Manager; defined_in Core Processing; related_to Account Servicing | https://www.alogent.com/banking-definitions/core-banking-systems ; https://help.sap.com/docs/SAP_FOR_BANKING/b0c17eb728054c5e92d73923f704edd7/53ffbdb976794b099a360da5b4ec88b6.html |

## 2) Systems refresh

Only genuinely new, verifiable deposit/core systems NOT already covered are
listed. Already covered (not repeated): FIS Profile, Fiserv DNA, Jack Henry
SilverLake, Temenos T24, Oracle FLEXCUBE, Infosys Finacle, TCS BaNCS, Legacy
Mainframe Core (legacy); Thought Machine Vault, Mambu, 10x Banking, Finxact,
Temenos Transact (modern). All rows `realizes = Core Banking Processing`.

Legacy additions (the "Big-Three" community/regional deposit cores documented
by the Kansas City Fed market-structure brief and FIS's NA community-bank
report):

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| Fiserv Premier | core-system (legacy) | Core Banking Processing | — | Fiserv | Long-established Fiserv deposit/loan core widely used by US community banks for account servicing, posting and GL integration. | Premier, Premier Core | https://www.kansascityfed.org/research/payments-system-research-briefings/market-structure-of-core-banking-services-providers/ ; https://www.fisglobal.com/-/media/fisglobal/files/pdf/report/retail-banking-core-banking-systems-na-community-bank-edition.pdf |
| Jack Henry Core Director | core-system (legacy) | Core Banking Processing | — | Jack Henry | Jack Henry's in-house community-bank deposit/loan core platform, an alternative to SilverLake for smaller institutions. | Core Director, Jack Henry Core Director System | https://www.kansascityfed.org/research/payments-system-research-briefings/market-structure-of-core-banking-services-providers/ ; https://www.openbankingtracker.com/banktech-providers |
| FIS Horizon | core-system (legacy) | Core Banking Processing | — | FIS | FIS deposit/loan core serving small and midsized banks (alongside FIS IBS), covering account servicing, posting and reporting. | Horizon, FIS Horizon Core | https://www.kansascityfed.org/research/payments-system-research-briefings/market-structure-of-core-banking-services-providers/ ; https://www.fisglobal.com/-/media/fisglobal/files/pdf/report/retail-banking-core-banking-systems-na-community-bank-edition.pdf |

Modern additions (supersede legacy deposit cores per the supersedes rule):

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| SAP Deposits Management | core-system (modern) | Core Banking Processing | Legacy Mainframe Core | SAP / SAP Fioneer | S/4HANA banking module managing current, savings and fixed-term deposit contracts across their lifecycle, with product configuration, pricing and contract operations. | SAP Deposits Management for Banking, SAP Transactional Banking, SAP Fioneer Core | https://help.sap.com/docs/SAP_FOR_BANKING/b0c17eb728054c5e92d73923f704edd7/53ffbdb976794b099a360da5b4ec88b6.html ; https://www.sapfioneer.com/banking/core-banking/ |
| Tuum | core-system (modern) | Core Banking Processing | Fiserv Premier | Tuum | Estonian cloud-native, API-first, microservices core banking platform with a modular accounts engine for current, savings and deposit accounts. | Tuum Core, Modularbank | https://tuum.com/ ; https://ibsintelligence.com/ibsi-verified/best-in-class-core-banking-vendor-tuum/ |
| SaaScada | core-system (modern) | Core Banking Processing | Jack Henry Core Director | SaaScada | Cloud-native, data-driven core banking platform using CQRS/event-sourcing and a Product Sequencer to build multi-ledger, multi-currency current and savings deposit products without code. | SaaScada Core, SaaScada Cloud Core | https://saascada.com/platform/ ; https://www.swisscom.ch/en/business/enterprise/themen/banking/core-banking-radar-saascada.html |

Notes:
- Did NOT add separate rows for Fiserv Precision/Cleartouch, Jack Henry CIF
  20/20/Symitar, or FIS IBS to avoid low-value duplication of the same vendor's
  legacy-core slot; Fiserv Premier, Jack Henry Core Director and FIS Horizon are
  the most distinct, well-documented additions.
- `supersedes` pairs chosen to map cloud-native modern cores onto representative
  legacy community/regional deposit cores; all targets exist in the registry or
  are added above.
