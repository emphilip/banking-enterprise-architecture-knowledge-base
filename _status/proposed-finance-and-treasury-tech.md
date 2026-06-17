---
title: Proposed Finance & Treasury Technology Decomposition
type: proposal
status: draft
author: tech-decomposition sub-agent
date: 2026-06-17
---

# Proposed Finance & Treasury Technology Decomposition

Scope: the Finance & Treasury business domain has only ONE directly relevant
existing top-level technology capability (**General Ledger Engine**, Core
Processing) plus the shared **Regulatory Reporting Engine** (already decomposed
under the Risk/Reg work). There is no treasury, ALM or financial-consolidation
technology capability registered. This proposal therefore:

1. Proposes **3 NEW top-level technology capabilities** enabling the F&T business
   capabilities (Treasury Management, Liquidity Management, Asset Liability
   Management, Financial Reporting, Regulatory Capital Management).
2. Decomposes the existing **General Ledger Engine** to L2/L3.
3. Decomposes the 3 new top-level caps to L2 (with a few L3).
4. Refreshes F&T systems with same-capability legacy -> modern `supersedes` pairs.

Grounding: SAP S/4HANA Finance (Universal Journal / ACDOCA, document splitting,
Financial Closing Cockpit, subledger accounting), Oracle Fusion ERP / Workday
Financials; Kyriba Liquidity Performance (cash positioning, 9,900+ bank
connectivity, AI cash forecasting, payments hub), ION Treasury (Wallstreet Suite,
Reval, IT2) and GTreasury (cloud-native cash visibility / forecasting / FX);
Moody's Balance Sheet Management ALM (IRRBB, behavioural models for non-maturity
deposits, FTP, earnings/EVE sensitivity), Oracle OFSAA ALM (IRRBB), QRM and SAS
ALM (legacy), Empyrean Sol ALM (modern cloud ALM + FTP + balance-sheet planning);
OneStream and Oracle EPM Cloud / Anaplan for close, consolidation, planning and
disclosure (legacy Oracle HFM / SAP BPC). CNCF cloud-native event-driven patterns
inform the service granularity.

Naming verified globally unique against `glossary/_canonical-names.md`. Tech names
are deliberately kept distinct from F&T business capabilities and L1s:
- tech **Treasury Management System** vs business L1 **Treasury Management**
- tech **Asset Liability Management Engine** vs business L2 **Asset Liability Management**
- tech **Financial Consolidation Platform** vs (no business cap of that name; distinct from **Financial Reporting**)
- tech **Liquidity Forecasting Engine** (sub-cap) vs business **Liquidity Management** / risk **Liquidity Risk Measurement**
- tech **Chart Of Accounts Service** / **Period Close Manager** vs business **General Ledger Accounting**
- new sub-caps checked against existing **General Ledger Posting** (a Core Banking
  Processing sub-cap that bridges core sub-ledgers to the GL) and existing risk
  **Economic Capital Engine** / **Stress Testing Engine**.

All three new top-level caps sit in **Core Processing**, alongside the existing
General Ledger Engine, Core Banking Processing, Payment Orchestration, etc. (The
shared Regulatory Reporting Engine remains the Data & Analytics home for capital
*reporting*; these caps cover the operational/analytical treasury & finance
engines.) Sub-capabilities are `defined_in` the SAME domain as their parent.

Relationships use only the 7 verbs: `depends_on`, `derived_from`, `supersedes`,
`defined_in`, `related_to`, `causes`, `mentions`.

---

## 1) New top-level technology capabilities

| Canonical Name | type | level | domain | enables (business caps) | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Treasury Management System | technology-capability | L1 | Core Processing | Treasury Management, Liquidity Management | Enterprise platform that gives treasury real-time visibility and control over cash, liquidity, funding and financial-market dealing: multi-bank cash positioning, bank/ERP connectivity, in-house banking, deal capture for money-market/FX/debt instruments, liquidity forecasting and treasury payments. | TMS, Treasury & Risk Management Platform, Treasury Workstation | `defined_in` Core Processing; `related_to` General Ledger Engine; `related_to` Payment Orchestration; `related_to` Asset Liability Management Engine | https://www.kyriba.com/solutions/treasury/ ; https://iongroup.com/products/treasury/wallstreet-suite/ ; https://www.gtreasury.com/ |
| Asset Liability Management Engine | technology-capability | L1 | Core Processing | Asset Liability Management, Liquidity Management, Regulatory Capital Management | Analytical engine that models the bank's balance sheet to measure and manage interest-rate risk in the banking book (IRRBB), funding and liquidity risk: cash-flow generation, repricing/gap analysis, EVE and NII sensitivity, behavioural modelling of non-maturity deposits and prepayment, funds transfer pricing and balance-sheet planning/stress. | ALM Engine, Balance Sheet Management Platform, IRRBB Engine, ALM/FTP Platform | `defined_in` Core Processing; `related_to` General Ledger Engine; `related_to` Treasury Management System; `related_to` Risk Analytics Engine; `related_to` Regulatory Reporting Engine | https://www.moodys.com/web/en/us/solutions/balance-sheet-management/alm.html ; https://empyreansolutions.com/risk-management/sol-alm/ ; https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/analytical-applications-infrastructure/812/almug/interest-rate-risk-banking-book-irrbb.html |
| Financial Consolidation Platform | technology-capability | L1 | Core Processing | Financial Reporting, General Ledger Accounting, Regulatory Capital Management | Corporate performance / financial-close platform that automates the group financial close, multi-entity/multi-GAAP consolidation (intercompany elimination, currency translation, minority interest), planning & budgeting, management & statutory reporting and regulatory disclosure (XBRL/ESEF). | CPM Platform, EPM Platform, Consolidation & Close Platform, Corporate Performance Management | `defined_in` Core Processing; `depends_on` General Ledger Engine; `related_to` Financial Reporting; `related_to` Regulatory Reporting Engine | https://www.onestream.com/solutions/financial-close-and-consolidation-software/ ; https://www.oracle.com/performance-management/ ; https://www.anaplan.com/solutions/finance/ |

---

## 2) Technology sub-capabilities

### General Ledger Engine (existing parent) — L2/L3

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Journal Processing Engine | technology-capability | L2 | General Ledger Engine | Core Processing | Captures, validates, posts and stores journal entries in the GL (manual, recurring, accrual/reversal and high-volume system-generated postings); in modern ERPs the single universal-journal line-item store of financial + management accounting. | Journal Engine, Universal Journal Service, GL Posting Engine, Document Posting Engine | `defined_in` Core Processing; `derived_from` General Ledger Engine | https://blog.sap-press.com/what-is-saps-universal-journal ; https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/523b8a55559ad007e10000000a44538d.html |
| Subledger Accounting | technology-capability | L2 | General Ledger Engine | Core Processing | Centralised rules-based subledger that transforms business transactions (AP/AR/assets/positions) into accounting entries and reconciles them to the GL, providing a detailed audit trail beneath summarised GL balances. | SLA, Subledger Accounting Engine, Accounting Hub, Subledger Service | `defined_in` Core Processing; `derived_from` General Ledger Engine; `related_to` Accounting Rules Engine; `related_to` General Ledger Posting | https://docs.oracle.com/en/cloud/saas/financials/saas-subledger-accounting/ ; https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana |
| Chart Of Accounts Service | technology-capability | L2 | General Ledger Engine | Core Processing | Manages the accounting structures and master data of the ledger: chart of accounts, ledgers (leading/parallel for multi-GAAP), accounting dimensions/segments (cost centre, profit centre, segment), and account hierarchies. | COA Service, Accounting Structure Service, Ledger & Segment Master, Account Master Service | `defined_in` Core Processing; `derived_from` General Ledger Engine | https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana ; https://docs.oracle.com/en/cloud/saas/financials/ |
| Accounting Rules Engine | technology-capability | L2 | General Ledger Engine | Core Processing | Configurable rules that derive accounting treatment from events — account determination, document-splitting / segment derivation, posting validation/substitution and multi-GAAP rule sets — driving consistent, auditable postings. | Account Determination Engine, Posting Rules Engine, Document Splitting Service | `defined_in` Core Processing; `derived_from` General Ledger Engine; `related_to` Subledger Accounting | https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana ; https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/523b8a55559ad007e10000000a44538d.html |
| Allocation Engine | technology-capability | L2 | General Ledger Engine | Core Processing | Periodic and on-demand cost/revenue allocations, distributions, assessments and apportionments across cost centres, profit centres and segments to support management accounting and profitability. | Cost Allocation Engine, Distribution & Assessment Engine, Profitability Allocation Service | `defined_in` Core Processing; `derived_from` General Ledger Engine; `related_to` Chart Of Accounts Service | https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana ; https://www.oracle.com/erp/ |
| Period Close Manager | technology-capability | L2 | General Ledger Engine | Core Processing | Orchestrates the period-end close: scheduling and sequencing of close tasks, accruals/reclassifications, foreign-currency revaluation, balance carryforward and close certification across entities and ledgers. | Financial Close Cockpit, Close Orchestration Service, GL Close Manager | `defined_in` Core Processing; `derived_from` General Ledger Engine; `related_to` Consolidation Engine | https://sapinsider.org/topic/sap-finance/sap-general-ledger/ ; https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana |
| Account Reconciliation Service | technology-capability | L2 | General Ledger Engine | Core Processing | Automated GL-to-subledger and balance-sheet account reconciliation: high-volume transaction matching, reconciliation certification and exception/break management feeding the close. | Reconciliation Engine, Transaction Matching Service, Balance Sheet Reconciliation | `defined_in` Core Processing; `derived_from` General Ledger Engine; `related_to` Period Close Manager | https://www.onestream.com/solutions/financial-close-and-consolidation-software/ ; https://www.oracle.com/performance-management/account-reconciliation/ |
| Multi-Currency Ledger Service | technology-capability | L3 | Journal Processing Engine | Core Processing | Maintains transaction, local and group currencies on every posting and performs foreign-currency valuation/translation, supporting multi-ledger parallel accounting. | Currency Translation Service, FX Revaluation Service, Multi-Currency Posting | `defined_in` Core Processing; `derived_from` Journal Processing Engine | https://blog.sap-press.com/what-is-saps-universal-journal ; https://docs.oracle.com/en/cloud/saas/financials/ |
| Intercompany Accounting Service | technology-capability | L3 | Subledger Accounting | Core Processing | Generates and matches intercompany transactions and balances across legal entities, supporting netting and elimination preparation ahead of consolidation. | Intercompany Engine, ICO Matching Service, Intercompany Reconciliation | `defined_in` Core Processing; `derived_from` Subledger Accounting; `related_to` Consolidation Engine | https://docs.oracle.com/en/cloud/saas/financials/ ; https://www.onestream.com/solutions/financial-close-and-consolidation-software/ |

### Treasury Management System (new parent) — L2/L3

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Cash Positioning Service | technology-capability | L2 | Treasury Management System | Core Processing | Aggregates balances and transactions across all banks, accounts, entities and currencies to give a real-time global cash position and drive same-day funding/concentration decisions. | Cash Visibility Service, Cash Position Engine, Global Cash Management | `defined_in` Core Processing; `derived_from` Treasury Management System; `related_to` Bank Connectivity Hub | https://www.kyriba.com/resource/cash-and-liquidity-management/ ; https://www.gtreasury.com/ |
| Bank Connectivity Hub | technology-capability | L2 | Treasury Management System | Core Processing | Standardised connectivity to banks, ERPs, payment and market systems (SWIFT, host-to-host, APIs, EBICS) with statement (MT940/camt) ingestion and treasury payment dispatch and tracking. | Bank Connectivity Service, SWIFT Service Bureau, Treasury Connectivity Gateway, Multi-Bank Connectivity | `defined_in` Core Processing; `derived_from` Treasury Management System; `related_to` Payment Orchestration | https://www.kyriba.com/products/treasury/ ; https://iongroup.com/products/treasury/wallstreet-suite/ |
| Deal Management | technology-capability | L2 | Treasury Management System | Core Processing | Capture, confirmation, settlement and accounting lifecycle for treasury financial instruments — money-market, FX, debt/investments and derivatives — with position keeping and counterparty/limit control. | Treasury Deal Capture, Front-Office Dealing, Treasury Instrument Management, Trade & Position Management | `defined_in` Core Processing; `derived_from` Treasury Management System; `related_to` Subledger Accounting | https://iongroup.com/products/treasury/wallstreet-suite/ ; https://treasury-management.com/companies/ion-treasury |
| Liquidity Forecasting Engine | technology-capability | L2 | Treasury Management System | Core Processing | Builds short- and medium-term cash-flow forecasts from actuals, scheduled flows, working-capital and AI-driven predictions, with variance analysis and scenario what-ifs to manage liquidity and funding. | Cash Forecasting Engine, AI Cash Forecasting, Liquidity Planning Service | `defined_in` Core Processing; `derived_from` Treasury Management System; `related_to` Cash Positioning Service; `related_to` Asset Liability Management Engine | https://www.kyriba.com/products/treasury/ ; https://www.gtreasury.com/ |
| Treasury Risk Management Service | technology-capability | L2 | Treasury Management System | Core Processing | Measures and manages treasury market exposures — FX, interest-rate and commodity — with exposure capture, hedge management and hedge-accounting support, plus counterparty/limit monitoring. | FX & Risk Management Service, Hedge Management Service, Treasury Exposure Management | `defined_in` Core Processing; `derived_from` Treasury Management System; `related_to` Deal Management; `related_to` Risk Analytics Engine | https://www.kyriba.com/products/treasury/ ; https://iongroup.com/treasury/ |
| In-House Banking Service | technology-capability | L3 | Treasury Management System | Core Processing | Internal bank for the group: intercompany loans/deposits, internal current accounts, payments-on-behalf-of (POBO) / collections-on-behalf-of (COBO) and cash-pooling/interest apportionment. | IHB Service, Payment Factory, POBO/COBO Service, Internal Bank | `defined_in` Core Processing; `derived_from` Treasury Management System; `related_to` Bank Connectivity Hub | https://www.kyriba.com/solutions/treasury/ ; https://iongroup.com/products/treasury/wallstreet-suite/ |

### Asset Liability Management Engine (new parent) — L2/L3

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| IRRBB Analytics Engine | technology-capability | L2 | Asset Liability Management Engine | Core Processing | Measures interest-rate risk in the banking book: cash-flow generation, repricing/gap analysis, economic value of equity (EVE) and net interest income (NII) sensitivity under prescribed and internal rate-shock scenarios. | Interest Rate Risk Engine, EVE/NII Engine, Banking Book Rate Risk Engine | `defined_in` Core Processing; `derived_from` Asset Liability Management Engine; `related_to` Behavioural Modelling Service | https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/analytical-applications-infrastructure/812/almug/interest-rate-risk-banking-book-irrbb.html ; https://www.moodys.com/web/en/us/solutions/balance-sheet-management/alm.html |
| Funds Transfer Pricing Engine | technology-capability | L2 | Asset Liability Management Engine | Core Processing | Allocates the cost/value of funds and liquidity premia across products, business units and the balance sheet to isolate net interest margin and support profitability and ALCO decisions. | FTP Engine, Transfer Pricing Service, Funds Transfer Pricing Service | `defined_in` Core Processing; `derived_from` Asset Liability Management Engine; `related_to` IRRBB Analytics Engine | https://empyreansolutions.com/risk-management/sol-alm/ ; https://www.moodys.com/web/en/us/solutions/balance-sheet-management/alm.html |
| Behavioural Modelling Service | technology-capability | L2 | Asset Liability Management Engine | Core Processing | Models customer behaviour that drives balance-sheet risk — non-maturity deposit decay/rate sensitivity, loan prepayment, pipeline and early-redemption assumptions — including macro-linked behavioural models for stress. | Behavioral Modeling Service, NMD Modelling Service, Prepayment Modelling Engine | `defined_in` Core Processing; `derived_from` Asset Liability Management Engine; `related_to` IRRBB Analytics Engine | https://www.moodys.com/web/en/us/insights/banking/embedding-interest-rate-risk-into-stress-testing.html ; https://www.risk.net/node/7963522 |
| Balance Sheet Planning Engine | technology-capability | L2 | Asset Liability Management Engine | Core Processing | Projects and simulates the future balance sheet and earnings under business and rate scenarios — multi-year NII/EVE forecasting, new-business volume modelling and capital/liquidity what-if planning for ALCO. | Balance Sheet Management Engine, NII Simulation Engine, ALM Scenario Engine | `defined_in` Core Processing; `derived_from` Asset Liability Management Engine; `related_to` Stress Testing Engine; `related_to` Liquidity Forecasting Engine | https://empyreansolutions.com/risk-management/sol-alm/ ; https://www.moodys.com/web/en/us/solutions/balance-sheet-management/alm.html |

### Financial Consolidation Platform (new parent) — L2/L3

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Consolidation Engine | technology-capability | L2 | Financial Consolidation Platform | Core Processing | Performs group consolidation: data collection from entities, currency translation, intercompany elimination, ownership/minority-interest calculation and multi-GAAP/management views to produce consolidated financial statements. | Group Consolidation Engine, Financial Consolidation Service, Consol Engine | `defined_in` Core Processing; `derived_from` Financial Consolidation Platform; `related_to` Intercompany Accounting Service; `related_to` Period Close Manager | https://www.onestream.com/solutions/financial-close-and-consolidation-software/ ; https://www.oracle.com/performance-management/financial-consolidation/ |
| Planning & Budgeting Engine | technology-capability | L2 | Financial Consolidation Platform | Core Processing | Driver-based planning, budgeting, rolling forecasts and scenario modelling (workforce, capex, revenue) integrated with the consolidation model for one source of plan and actual data. | Planning Engine, FP&A Engine, Budgeting & Forecasting Service, EPM Planning | `defined_in` Core Processing; `derived_from` Financial Consolidation Platform; `related_to` Consolidation Engine | https://www.anaplan.com/solutions/finance/ ; https://www.oracle.com/performance-management/planning/ |
| Disclosure Management Service | technology-capability | L2 | Financial Consolidation Platform | Core Processing | Produces narrative/statutory disclosures and board packages from consolidated data with collaborative authoring, audit trail and tagged regulatory output (XBRL/iXBRL, ESEF). | Narrative Reporting Service, Disclosure Management, XBRL Tagging Service, Statutory Reporting Service | `defined_in` Core Processing; `derived_from` Financial Consolidation Platform; `related_to` Consolidation Engine; `related_to` Regulatory Reporting Engine | https://www.onestream.com/solutions/financial-close-and-consolidation-software/ ; https://www.oracle.com/performance-management/narrative-reporting/ |
| Financial Data Quality Service | technology-capability | L3 | Financial Consolidation Platform | Core Processing | Built-in finance data integration and quality layer that loads, validates, maps and certifies source-system data before consolidation/planning, with full drill-back and audit. | Financial Data Quality Management, FDQM, Data Integration & Validation (Finance) | `defined_in` Core Processing; `derived_from` Financial Consolidation Platform; `related_to` Consolidation Engine | https://www.onestream.com/solutions/financial-close-and-consolidation-software/ ; https://www.mindstreamanalytics.com/onestream-software.html |

---

## 3) Systems refresh (legacy -> modern, same-capability supersedes)

Already-registered systems NOT re-added: SAP ECC, Workday Financials, Oracle
Fusion ERP (all General Ledger Engine), AxiomSL, Wolters Kluwer OneSumX,
Regnology, Suade (all Regulatory Reporting Engine). New systems below realize one
of the new top-level caps (or General Ledger Engine for the consolidation/ERP
items), and modern systems `supersedes` a legacy system realizing the SAME
capability.

### Legacy systems

| Canonical Name | type | realizes (tech cap) | supersedes | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| Oracle E-Business Suite | system | General Ledger Engine | — | Oracle | On-premise ERP financials suite (Oracle GL/AP/AR/FA) widely deployed as a legacy corporate general ledger before cloud ERP. | Oracle EBS, Oracle Financials, E-Business Suite | https://www.oracle.com/applications/ebusiness/ |
| Oracle Hyperion HFM | system | Financial Consolidation Platform | — | Oracle | Legacy on-premise Hyperion Financial Management product for group financial consolidation and close, the long-standing incumbent now being migrated to cloud EPM. | HFM, Hyperion Financial Management, Hyperion | https://www.oracle.com/performance-management/ ; https://docs.oracle.com/en/applications/enterprise-performance-management/ |
| SAP BPC | system | Financial Consolidation Platform | — | SAP | Legacy SAP Business Planning and Consolidation product for planning, budgeting and legal/management consolidation on BW/NetWeaver. | Business Planning and Consolidation, SAP BPC, SEM-BCS | https://www.sap.com/products/financial-management/planning-consolidation.html |
| SunGard AvantGard | system | Treasury Management System | — | FIS (SunGard) | Legacy SunGard AvantGard treasury / receivables suite (incl. Integrity and Quantum TMS) for cash, payments and treasury management. | AvantGard, AvantGard Integrity, AvantGard Quantum | http://www.neilainger.com/pdf/gtnews_TMS%20Buyers%20Guide%202013_Corrected_withCovers.pdf ; https://treasury-management.com/companies/ion-treasury |
| SAP Treasury And Risk Management | system | Treasury Management System | — | SAP | Legacy ERP-embedded treasury module (SAP TRM / Cash Management classic) for cash management, transaction management and treasury risk. | SAP TRM, SAP Treasury, FSCM Treasury | https://www.sap.com/products/financial-management/treasury-management.html |
| QRM Balance Sheet Management | system | Asset Liability Management Engine | — | Quantitative Risk Management | Long-established on-premise ALM/IRRBB and balance-sheet-management system used by large, highly-regulated banks for rate-risk, FTP and capital modelling. | QRM, Quantitative Risk Management, QRM ALM | https://www.qrm.com/ ; https://www.finalyse.com/blog/banking/implementation-and-change-management-associated-with-sophisticated-tools-a-glimpse-at-qrm |
| SAS Asset And Liability Management | system | Asset Liability Management Engine | — | SAS | Legacy SAS ALM / Risk Management for Banking module for interest-rate-risk, liquidity and balance-sheet analytics. | SAS ALM, SAS Risk Management for Banking ALM | https://www.sas.com/en_us/software/asset-liability-management.html |

### Modern systems

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, same capability) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| SAP S/4HANA Finance | system | General Ledger Engine | SAP ECC; Oracle E-Business Suite | SAP | Modern in-memory ERP finance built on the Universal Journal (ACDOCA), unifying financial and management accounting with real-time GL, subledgers, allocations and the Financial Closing Cockpit. | S/4HANA Finance, Simple Finance, S/4HANA Central Finance | https://blog.sap-press.com/what-is-saps-universal-journal ; https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/523b8a55559ad007e10000000a44538d.html |
| OneStream | system | Financial Consolidation Platform | Oracle Hyperion HFM; SAP BPC | OneStream Software | Unified cloud CPM platform combining financial close, consolidation, planning, reporting and disclosure on a single Extensible-Dimensionality model with built-in financial data quality. | OneStream Software, OneStream Platform, OneStream XF | https://www.onestream.com/solutions/financial-close-and-consolidation-software/ ; https://barc.com/review/onestream/ |
| Oracle EPM Cloud | system | Financial Consolidation Platform | Oracle Hyperion HFM | Oracle | Cloud enterprise performance management suite (Financial Consolidation and Close, Planning, Narrative Reporting) succeeding on-premise Hyperion. | Oracle EPM, Oracle Fusion EPM, FCCS, EPM Cloud | https://www.oracle.com/performance-management/ ; https://docs.oracle.com/en/applications/enterprise-performance-management/ |
| Anaplan | system | Financial Consolidation Platform | SAP BPC | Anaplan | Cloud connected-planning platform for financial planning, budgeting, forecasting and scenario modelling across finance and operations. | Anaplan Platform, Connected Planning | https://www.anaplan.com/solutions/finance/ |
| Kyriba | system | Treasury Management System | SunGard AvantGard | Kyriba | Cloud Liquidity Performance / treasury management platform: multi-bank cash positioning, 9,900+ bank/ERP connectivity, AI cash forecasting, payments and FX/risk management. | Kyriba Liquidity Performance, Kyriba TMS | https://www.kyriba.com/solutions/treasury/ ; https://www.kyriba.com/products/treasury/ |
| ION Treasury | system | Treasury Management System | SAP Treasury And Risk Management | ION Group | Treasury & risk management portfolio (Wallstreet Suite, Reval, IT2, Treasura) spanning on-prem to cloud, with cash, dealing, payments and risk for corporates and banks. | ION Wallstreet Suite, Reval, IT2, Wallstreet Suite | https://iongroup.com/products/treasury/wallstreet-suite/ ; https://treasury-management.com/companies/ion-treasury |
| GTreasury | system | Treasury Management System | SunGard AvantGard | GTreasury | Cloud-native treasury and risk management platform focused on cash visibility, cash-flow forecasting, bank connectivity, payments and FX risk for mid- to large-market organisations. | GTreasury Platform, GTreasury TRMS | https://www.gtreasury.com/ ; https://www.viewpointanalysis.com/post/treasury-management-software-options-2026 |
| Empyrean Sol ALM | system | Asset Liability Management Engine | QRM Balance Sheet Management; SAS Asset And Liability Management | Empyrean Solutions | Modern cloud ALM platform (Sol ALM) for IRRBB, liquidity stress testing, deposit/behavioural analytics, funds transfer pricing and balance-sheet planning. | Sol ALM, Empyrean ALM, Empyrean Solutions | https://empyreansolutions.com/risk-management/sol-alm/ ; https://prnewswire.com/news-releases/empyrean-solutions-wins-financial-planning-and-budgeting-category-in-the-2025-risktech100-302291573.html |
| Moody's Balance Sheet Management | system | Asset Liability Management Engine | QRM Balance Sheet Management | Moody's Analytics | Moody's cloud-enabled ALM / balance-sheet-management suite for IRRBB, FTP, behavioural modelling and earnings/EVE sensitivity, aligned to evolving regulatory standards. | Moody's ALM, Moody's Balance Sheet Management, RiskConfidence | https://www.moodys.com/web/en/us/solutions/balance-sheet-management/alm.html ; https://www.moodys.com/web/en/us/insights/banking/embedding-interest-rate-risk-into-stress-testing.html |

---

## Notes for the integrator

- All sub-capabilities are `defined_in` Core Processing (same domain as their
  parent), consistent with the existing General Ledger Engine home.
- The new top-level caps are placed in **Core Processing**. If the integrator
  prefers the analytical ALM engine in **Data & Analytics** (alongside Risk Data
  Aggregation / Regulatory Reporting Engine), Asset Liability Management Engine is
  the only candidate for relocation; it is grounded equally in both. Recommended
  to keep all three in Core Processing for cohesion with General Ledger Engine.
- `Financial Data Quality Service` (FCP L3) is named to avoid clash with the
  existing `Data Quality Engine` sub-cap of Data Governance.
- `Liquidity Forecasting Engine` (TMS L2) is distinct from the risk-domain
  `Liquidity Risk Measurement` / `Intraday Liquidity Monitoring` business caps and
  from the `Risk Analytics Engine`; cross-linked via `related_to`.
- `Account Reconciliation Service` (GL L2) is distinct from the deposits business
  cap `Account Reconciliation Servicing` and the Reg `Reporting Reconciliation
  Workbench`.
