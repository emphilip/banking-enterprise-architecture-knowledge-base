---
id: proposed-compliance-and-financial-crime-tech
title: Proposed Compliance & Financial Crime Technology Decomposition
type: proposal
status: draft
author: tech-decomposition sub-agent
date: 2026-06-17
---

# Proposed Compliance & Financial Crime Technology Decomposition

Scope: the enabling **technology capabilities** for the Compliance & Financial
Crime business domain. Three top-level tech caps already exist in the registry:

- **Transaction Monitoring Platform** (domain: AI & Automation) — realized by
  Oracle Mantas / NICE Actimize (legacy); Hawk AI / ComplyAdvantage (modern).
- **Regulatory Reporting Engine** (domain: Data & Analytics) — realized by
  AxiomSL / Wolters Kluwer OneSumX (legacy); Regnology / Suade (modern).
- **Data Governance** (domain: Data & Analytics) — supports Regulatory Compliance.

This proposal (1) decomposes those three to **L2/L3 sub-capabilities** (each
`defined_in` the SAME domain as its parent), (2) proposes **1 NEW top-level tech
capability** — a KYC onboarding / customer-screening platform that does not fit
under the transaction-centric Transaction Monitoring Platform — and (3) refreshes
the **systems** list with genuinely new FinCrime/RegTech products.

Grounded in financial-crime / RegTech reference architectures and vendor docs:
NICE Actimize (SAM, Watchlist Filtering, X-Sight, ActOne case management), Oracle
FCCM / Mantas Behavior Detection + Enterprise Case Management, SAS Anti-Money
Laundering, ComplyAdvantage, Hawk AI, Quantexa (entity resolution / network
analytics), Napier AI Continuum, LexisNexis / Fircosoft (Bridger Insight XG,
WorldCompliance, Firco Continuity / Compliance Link) screening, AxiomSL /
Adenza, Wolters Kluwer OneSumX, Regnology (Abacus data model + calculation
engine, validation engine, reporting APIs), Suade, Collibra-class data-governance
platforms (catalog / quality / lineage / stewardship), Fenergo client lifecycle
management, FATF/Wolfsberg technology guidance, and CNCF cloud-native patterns.

Naming note: all canonical names were checked against
`glossary/_canonical-names.md` for global uniqueness and kept distinct from
existing **business** capabilities (e.g. tech **Watchlist Screening Engine** vs
business *Sanctions Screening*; tech **Financial Crime Case Manager** vs business
*Case Management*; tech **Alert Scoring Service** vs business *Alert Management* /
*AML Monitoring*; tech **Regulatory Report Calculation Engine** vs business
*Regulatory Reporting*; tech **KYC Onboarding Platform** vs business *KYC
Management*). They are also kept distinct from existing tech sub-caps such as
*Payment Sanctions Filter* / *Inline Sanctions Filter* (Payments domain, inline
in-flight payment screening) — the Watchlist Screening Engine here is the
batch/customer/list-management screening capability of the FinCrime stack.
Relationships use only the 7 verbs: `depends_on`, `derived_from`, `supersedes`,
`defined_in`, `related_to`, `causes`, `mentions`.

---

## 1) Technology sub-capabilities

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Scenario Detection Engine | technology-subcapability | L2 | Transaction Monitoring Platform | AI & Automation | Configurable behavior-detection engine that runs typology scenarios, thresholds and segmented rules over transactions and account behaviour to detect suspicious activity. | Behavior Detection Engine, Scenario Engine, AML Detection Engine, Typology Engine | derived_from Transaction Monitoring Platform; defined_in AI & Automation; depends_on Data Warehousing; related_to AML Monitoring | https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/behavior-detection/8.1.2.9.0/smubd/overview-fccm.html ; https://www.niceactimize.com/Documents/SAM10_Brochure.pdf |
| Detection Scenario Library | technology-subcapability | L3 | Scenario Detection Engine | AI & Automation | Managed catalogue of out-of-the-box and custom AML/CTF scenarios, parameters and segmentation logic, with versioning and tuning of thresholds. | Scenario Library, Scenario Catalogue, Scenario Manager, Rule Library | derived_from Scenario Detection Engine; defined_in AI & Automation; related_to Model Risk Management Platform | https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/behavior-detection/8.1.2.9.0/smubd/overview-fccm.html ; https://www.niceactimize.com/glossary/transaction-monitoring-software |
| Behavioural Risk Analytics | technology-subcapability | L2 | Transaction Monitoring Platform | AI & Automation | Machine-learning and anomaly-detection layer that profiles customer/peer behaviour and scores deviations to surface money-laundering risk beyond static rules. | AML Machine Learning, Anomaly Detection Service, Behavioural Profiling, Unsupervised Detection | derived_from Transaction Monitoring Platform; defined_in AI & Automation; depends_on Machine Learning Platform; related_to Behavioural Analytics | https://www.napier.ai/transaction-monitoring ; https://www.sas.com/en_us/software/anti-money-laundering.html |
| Watchlist Screening Engine | technology-subcapability | L2 | Transaction Monitoring Platform | AI & Automation | Name/entity matching engine that screens customers, counterparties and payments against sanctions, PEP, adverse-media and internal watchlists with fuzzy matching and hit disposition. | Name Screening Engine, Sanctions Matching Engine, List Screening Engine, Filter Engine | derived_from Transaction Monitoring Platform; defined_in AI & Automation; related_to Sanctions Screening; depends_on Watchlist Data Management | https://risk.lexisnexis.com/products/bridger-insight-xg ; https://www.niceactimize.com/glossary/transaction-monitoring-software |
| Watchlist Data Management | technology-subcapability | L3 | Watchlist Screening Engine | AI & Automation | Ingestion, normalisation, deduplication and refresh of sanctions/PEP/adverse-media reference lists used by the screening engine. | List Management Service, Reference List Manager, Sanctions List Loader, WorldCompliance Data | derived_from Watchlist Screening Engine; defined_in AI & Automation; depends_on Data Governance | https://risk.lexisnexis.com/global/en/products/worldcompliance-data ; https://risk.lexisnexis.com/global/en/financial-services/financial-crime-compliance/watchlist-screening |
| Alert Scoring Service | technology-subcapability | L2 | Transaction Monitoring Platform | AI & Automation | Consolidates, deduplicates, prioritises and risk-scores alerts from detection, analytics and screening, routing them for investigation and reducing false positives. | Alert Prioritisation Service, Alert Correlation Service, Alert Triage Engine, Alert Generation Engine | derived_from Transaction Monitoring Platform; defined_in AI & Automation; depends_on Scenario Detection Engine; causes Financial Crime Case Manager | https://docs.oracle.com/cd/E91253_01/PDF/8.0.7.0.0/OFS%20BD%208.0.7.0.0%20Release%20Notes.pdf ; https://www.niceactimize.com/glossary/transaction-monitoring-software |
| Financial Crime Case Manager | technology-subcapability | L2 | Transaction Monitoring Platform | AI & Automation | Investigation workspace that consolidates alerts and entity data into cases, manages workflow, audit trail, narrative and disposition for AML/financial-crime investigations. | FinCrime Case Management, Investigation Workbench, Enterprise Case Management, ActOne | derived_from Transaction Monitoring Platform; defined_in AI & Automation; depends_on Alert Scoring Service; related_to Suspicious Activity Reporting | https://docs.oracle.com/cd/E91253_01/PDF/8.0.7.0.0/OFS%20BD%208.0.7.0.0%20Release%20Notes.pdf ; https://www.niceactimize.com/glossary/transaction-monitoring-software |
| SAR Filing Service | technology-subcapability | L3 | Financial Crime Case Manager | AI & Automation | Generation, e-filing and tracking of suspicious activity / transaction reports (SAR/STR) to FIUs from investigated cases. | STR Filing Service, Regulatory Report Filing (AML), goAML Connector, SAR Generator | derived_from Financial Crime Case Manager; defined_in AI & Automation; related_to Suspicious Activity Reporting | https://www.sas.com/en_us/solutions/fraud-security-intelligence/solutions/aml-cft-compliance.html ; https://www.niceactimize.com/glossary/transaction-monitoring-software |
| Network Entity Resolution | technology-subcapability | L2 | Transaction Monitoring Platform | AI & Automation | Resolves disparate records into single entities and builds relationship networks to provide context, uncover hidden links and prioritise financial-crime risk. | Entity Resolution Engine, Network Analytics, Contextual Decision Intelligence, Link Analysis | derived_from Transaction Monitoring Platform; defined_in AI & Automation; related_to Network Analytics; depends_on Machine Learning Platform | https://www.quantexa.com/solutions/aml/ ; https://www.quantexa.com/resources/holistic-view-of-financial-crime/ |
| Regulatory Report Calculation Engine | technology-subcapability | L2 | Regulatory Reporting Engine | Data & Analytics | Rules/calculation engine that applies regulatory logic to a harmonised data model to compute report figures across jurisdictions and reporting areas. | Report Calculation Engine, Reporting Computation Engine, Abacus Calculation Engine, Reg Calc Engine | derived_from Regulatory Reporting Engine; defined_in Data & Analytics; depends_on Regulatory Data Model | https://www.regnology.net/en/solutions/for-the-regulated/regnology-reporting-hub/abacus-data-and-calculation-engine/ ; https://www.risk.net/awards/7960489/regulatory-reporting-product-of-the-year-regnology |
| Regulatory Data Model | technology-subcapability | L2 | Regulatory Reporting Engine | Data & Analytics | Standardised, harmonised regulatory data model that ingests and maps source data for consistent, granular reporting across jurisdictions. | Harmonised Data Model, Granular Data Layer, Reporting Data Model, Reg Data Layer | derived_from Regulatory Reporting Engine; defined_in Data & Analytics; depends_on Data Governance | https://www.regnology.net/en/solutions/for-the-regulated/regnology-reporting-hub/abacus-data-and-calculation-engine/ ; https://a-teaminsight.com/blog/api-driven-and-template-free-the-rise-of-granular-data-reporting/?brand=ati |
| Regulatory Taxonomy Manager | technology-subcapability | L2 | Regulatory Reporting Engine | Data & Analytics | Manages regulator taxonomies, templates and report definitions (e.g. XBRL/DPM) and keeps them current with changing rules across regimes. | Taxonomy Manager, Reporting Template Manager, XBRL Taxonomy Service, Regulatory Rules Library | derived_from Regulatory Reporting Engine; defined_in Data & Analytics; related_to Regulatory Reporting | https://www.regnology.net/en/solutions/for-the-regulated/regnology-reporting-hub/ ; https://medium.com/@pratikchavan977/how-regtech-platforms-like-suade-are-transforming-regulatory-reporting-in-modern-banks-bfaa53363b0d |
| Report Validation Service | technology-subcapability | L2 | Regulatory Reporting Engine | Data & Analytics | Applies regulator validation rules, plausibility/quality checks and cross-report consistency checks before report generation and submission. | Validation Engine, Reporting Validation Service, Plausibility Check Service, Quality Rule Engine | derived_from Regulatory Reporting Engine; defined_in Data & Analytics; depends_on Regulatory Taxonomy Manager | https://www.regnology.net/en/solutions/for-the-regulated/regnology-reporting-hub/ ; https://sourceforge.net/software/product/Regnology/ |
| Reporting Reconciliation Workbench | technology-subcapability | L2 | Regulatory Reporting Engine | Data & Analytics | Reconciles reported figures back to source ledgers/risk data, manages adjustments and provides an audit trail for sign-off of regulatory returns. | Reconciliation Workbench, Reg Reconciliation Service, Figure Reconciliation, Reporting Sign-Off | derived_from Regulatory Reporting Engine; defined_in Data & Analytics; depends_on Regulatory Report Calculation Engine; related_to Data Lineage Tracker | https://www.regnology.net/en/solutions/for-the-regulated/regnology-reporting-hub/abacus-data-and-calculation-engine/ ; https://sourceforge.net/software/product/Regnology/ |
| Regulatory Submission Gateway | technology-subcapability | L2 | Regulatory Reporting Engine | Data & Analytics | Connectivity layer that submits returns to regulators and ingests feedback/acknowledgements via APIs and regulator portals. | Submission Gateway, Regulator Connectivity, Filing Gateway, Reporting API Gateway | derived_from Regulatory Reporting Engine; defined_in Data & Analytics; depends_on Report Validation Service | https://www.regnology.net/en/solutions/for-the-regulated/reporting-apis/ ; https://a-teaminsight.com/blog/api-driven-and-template-free-the-rise-of-granular-data-reporting/?brand=ati |
| Data Quality Engine | technology-subcapability | L2 | Data Governance | Data & Analytics | Profiles, monitors and remediates data quality, detecting anomalies against statistical baselines and raising issues for stewards. | Data Quality Service, DQ Engine, Data Profiling Service, Quality Monitoring | derived_from Data Governance; defined_in Data & Analytics; related_to Party Data Quality | https://erstudio.com/blog/collibra-data-governance/ ; https://thedatagovernor.com/what-is-collibra/ |
| Data Lineage Tracker | technology-subcapability | L2 | Data Governance | Data & Analytics | Captures and visualises end-to-end data lineage across systems, reports and transformations to support impact analysis and regulatory traceability (e.g. BCBS 239). | Lineage Service, Data Lineage Engine, Provenance Tracker, End-to-End Lineage | derived_from Data Governance; defined_in Data & Analytics; related_to Risk Data Lineage | https://thedatagovernor.com/what-is-collibra/ ; https://moderntechnologist.com/collibra-overview/ |
| Metadata Catalog | technology-subcapability | L2 | Data Governance | Data & Analytics | Searchable catalogue of technical and business metadata that organises data assets, enables discovery and surfaces trusted, classified information. | Data Catalog Service, Metadata Repository, Asset Catalog, Data Discovery | derived_from Data Governance; defined_in Data & Analytics; related_to Master Data Management | https://murdio.com/insights/collibra-data-catalog/ ; https://moderntechnologist.com/collibra-overview/ |
| Business Glossary Manager | technology-subcapability | L3 | Metadata Catalog | Data & Analytics | Manages business terms, definitions, classifications and their links to data assets so data is interpreted consistently across the enterprise. | Business Glossary, Term Management, Semantic Glossary, Data Dictionary | derived_from Metadata Catalog; defined_in Data & Analytics; related_to Metadata Catalog | https://erstudio.com/blog/collibra-data-governance/ ; https://maniksonituts.medium.com/what-is-data-governance-and-how-can-it-be-implemented-in-collibra-0e72c4f75871 |
| Data Policy & Stewardship Service | technology-subcapability | L2 | Data Governance | Data & Analytics | Manages data policies, ownership models, stewardship workflows and audit-ready controls that operationalise governance across the enterprise. | Stewardship Workflow, Policy Management (Data), Data Governance Workflow, Data Ownership Service | derived_from Data Governance; defined_in Data & Analytics; related_to Data Quality Engine | https://thedatagovernor.com/what-is-collibra/ ; https://erstudio.com/blog/collibra-data-governance/ |

## 2) New top-level technology capability

| Canonical Name | type | level | domain | enables (business caps) | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| KYC Onboarding Platform | technology-capability | L1 | AI & Automation | KYC Management, Customer Due Diligence, Customer Acquisition | Client lifecycle / KYC platform that orchestrates customer due diligence, identity and document verification, risk rating, screening and periodic review across onboarding and the ongoing client lifecycle. | Client Lifecycle Management Platform, KYC Platform, CLM Platform, Perpetual KYC Platform | defined_in AI & Automation; related_to Transaction Monitoring Platform; depends_on Watchlist Screening Engine; depends_on Intelligent Document Processing | https://www.fenergo.com/client-lifecycle-management ; https://www.fenergo.com/know-your-customer-kyc-solution ; https://www.sas.com/en_us/software/anti-money-laundering.html |

Rationale: the registry has tech caps for transaction monitoring and reg
reporting but **no platform enabling KYC Management / Customer Due Diligence**.
KYC/CLM (Fenergo, NICE Actimize CDD, SAS CDD) is a distinct system class —
onboarding, policy-driven due diligence, perpetual KYC review — that is not
transaction-centric and therefore does not fit under Transaction Monitoring
Platform. One new top-level cap added; kept minimal.

## 3) Systems refresh

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only — SAME capability) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| SAS Anti-Money Laundering | legacy-system | Transaction Monitoring Platform | — | SAS | Integrated AML platform covering transaction monitoring, scenario detection, watchlist screening, case management and regulatory reporting on the SAS analytics stack. | SAS AML, SAS Anti Money Laundering | https://www.sas.com/en_us/software/anti-money-laundering.html ; https://www.sas.com/en_us/solutions/fraud-security-intelligence/solutions/aml-cft-compliance.html |
| LexisNexis Bridger Insight | legacy-system | Transaction Monitoring Platform | — | LexisNexis Risk Solutions (Fircosoft) | Watchlist and sanctions screening platform (Bridger Insight XG, Firco Compliance Link / Continuity) for customer and payment screening against sanctions, PEP and adverse-media data. | Bridger Insight XG, Fircosoft, Firco, Firco Continuity | https://risk.lexisnexis.com/products/bridger-insight-xg ; https://www.finastra.com/partners/fircosoft |
| Napier AI | modern-system | Transaction Monitoring Platform | SAS Anti-Money Laundering | Napier AI | AI-enhanced financial-crime platform (Continuum) unifying transaction monitoring, transaction and client screening, and case management with explainable AI. | Napier, Napier Continuum, Continuum, NapierAI | https://www.napier.ai/continuum ; https://www.napier.ai/transaction-monitoring |
| Fenergo | modern-system | KYC Onboarding Platform | — | Fenergo | API-first SaaS client lifecycle management / KYC platform covering onboarding, policy-driven due diligence, document AI, screening orchestration and perpetual KYC across jurisdictions. | Fenergo CLM, Fenergo KYC, Fenergo Client Lifecycle Management | https://www.fenergo.com/client-lifecycle-management ; https://www.fenergo.com/know-your-customer-kyc-solution |

Notes on systems:
- **No supersedes** for SAS AML, LexisNexis Bridger Insight (legacy entries) or
  Fenergo (it realizes the brand-new KYC Onboarding Platform, so there is no
  same-capability legacy predecessor already in the registry).
- Napier AI is the only new modern system with a same-capability `supersedes`
  pair (→ SAS Anti-Money Laundering, both realize Transaction Monitoring
  Platform). Oracle Mantas and NICE Actimize already carry Hawk AI /
  ComplyAdvantage as their modern successors.
- **Deliberately NOT re-added** (already in registry from other domains):
  Quantexa (Risk — Risk Data Aggregation), Feedzai & Featurespace (Fraud
  Analytics). SAS already appears as SAS Platform / SAS Fraud Management / SAS
  Risk Management for Banking, but **SAS Anti-Money Laundering is a distinct AML
  product** realizing Transaction Monitoring Platform and is genuinely new.
