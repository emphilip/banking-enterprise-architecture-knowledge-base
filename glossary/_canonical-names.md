---
id: canonical-names
title: Canonical Names Registry
type: glossary-term
status: draft
---

# Canonical Names Registry

This file is the single source of truth for every concept name and its aliases.
Every other file MUST use these exact spellings (dedupe is
case/whitespace-insensitive but otherwise literal). When adding a concept, add it
here first. The 7 relationship verbs are: `depends_on`, `derived_from`,
`supersedes`, `defined_in`, `related_to`, `causes`, `mentions`.

Naming rule applied here to avoid graph collisions: a **capability** and a
**process** covering similar ground are given distinct names (e.g. capability
"Customer Acquisition" vs process "Customer Onboarding"; tech capability
"Transaction Monitoring Platform" vs business capability "Transaction
Monitoring").

## Domains (value streams & technology domains)

| Canonical Name | Kind | Aliases |
|---|---|---|
| Customer Management | business-domain | Party Management, Customer Domain |
| Payments | business-domain | Payments Domain |
| Lending & Credit | business-domain | Lending Domain, Credit Domain |
| Deposits & Accounts | business-domain | Deposits Domain, Accounts Domain |
| Cards | business-domain | Cards Domain, Card Services |
| Wealth & Investments | business-domain | Wealth Domain, Investments Domain |
| Risk Management | business-domain | Risk Domain |
| Compliance & Financial Crime | business-domain | Financial Crime Domain, Compliance Domain |
| Channels & Engagement | business-domain | Channels Domain, Engagement Domain |
| Finance & Treasury | business-domain | Finance Domain, Treasury Domain |
| Core Processing | technology-domain | Core Systems Domain |
| Data & Analytics | technology-domain | Data Domain, Analytics Domain |
| Integration & APIs | technology-domain | Integration Domain, API Domain |
| Security & Identity | technology-domain | Security Domain, Identity Domain |
| AI & Automation | technology-domain | AI Domain, Automation Domain |

## Business capabilities

Format: Canonical Name | Level | Domain (defined_in) | Parent (derived_from) | Aliases

| Canonical Name | Level | Domain | Parent | Aliases |
|---|---|---|---|---|
| Customer Lifecycle Management | L1 | Customer Management | — | Customer Lifecycle |
| Customer Acquisition | L2 | Customer Management | Customer Lifecycle Management | Onboarding Capability |
| Identity Verification | L3 | Customer Management | Customer Acquisition | ID&V, Identity Proofing |
| Customer Due Diligence | L3 | Customer Management | Customer Acquisition | CDD, EDD |
| Party Data Management | L2 | Customer Management | Customer Lifecycle Management | Customer Information Management |
| Customer Profile Management | L3 | Customer Management | Party Data Management | Profile Management |
| Customer Servicing | L2 | Customer Management | Customer Lifecycle Management | Customer Service |
| Case Management | L3 | Customer Management | Customer Servicing | Service Case Management |
| Relationship Management | L2 | Customer Management | Customer Lifecycle Management | RM, Client Relationship |
| Marketing Management | L1 | Customer Management | — | Marketing |
| Campaign Management | L2 | Customer Management | Marketing Management | Campaigns |
| Customer Segmentation | L2 | Customer Management | Marketing Management | Segmentation |
| Payment Services | L1 | Payments | — | Payments Capability |
| Payment Execution | L2 | Payments | Payment Services | Payment Processing Capability |
| Domestic Payments | L3 | Payments | Payment Execution | ACH, Faster Payments |
| Cross-Border Payments | L3 | Payments | Payment Execution | International Payments, SWIFT Payments |
| Real-Time Payments | L3 | Payments | Payment Execution | RTP, Instant Payments |
| Payment Clearing & Settlement | L2 | Payments | Payment Services | Clearing and Settlement |
| Payment Initiation | L2 | Payments | Payment Services | Payment Origination |
| Direct Debit Management | L2 | Payments | Payment Services | Direct Debits |
| Lending | L1 | Lending & Credit | — | Credit Services |
| Loan Origination | L2 | Lending & Credit | Lending | Loan Onboarding |
| Credit Decisioning | L3 | Lending & Credit | Loan Origination | Credit Assessment, Underwriting Decision |
| Loan Servicing | L2 | Lending & Credit | Lending | Loan Administration |
| Collateral Management | L2 | Lending & Credit | Lending | Collateral & Security |
| Collections & Recovery | L2 | Lending & Credit | Lending | Collections, Recoveries |
| Deposits | L1 | Deposits & Accounts | — | Deposit Services |
| Account Opening | L2 | Deposits & Accounts | Deposits | Account Origination |
| Account Servicing | L2 | Deposits & Accounts | Deposits | Account Administration |
| Interest Calculation | L2 | Deposits & Accounts | Deposits | Interest Processing |
| Overdraft Management | L2 | Deposits & Accounts | Deposits | Overdrafts |
| Cards Management | L1 | Cards | — | Card Services Capability |
| Card Issuing | L2 | Cards | Cards Management | Card Issuance Capability |
| Card Authorization | L2 | Cards | Cards Management | Authorization |
| Dispute Management | L2 | Cards | Cards Management | Chargeback Management |
| Card Lifecycle Management | L2 | Cards | Cards Management | Card Lifecycle |
| Wealth Management | L1 | Wealth & Investments | — | Private Banking |
| Portfolio Management | L2 | Wealth & Investments | Wealth Management | Portfolio Administration |
| Investment Advisory | L2 | Wealth & Investments | Wealth Management | Advisory Services |
| Brokerage & Trading | L2 | Wealth & Investments | Wealth Management | Trading, Brokerage |
| Enterprise Risk Management | L1 | Risk Management | — | Enterprise Risk |
| Credit Risk Management | L2 | Risk Management | Enterprise Risk Management | Credit Risk |
| Market Risk Management | L2 | Risk Management | Enterprise Risk Management | Market Risk |
| Operational Risk Management | L2 | Risk Management | Enterprise Risk Management | Operational Risk |
| Liquidity Risk Management | L2 | Risk Management | Enterprise Risk Management | Liquidity Risk |
| Fraud Management | L2 | Risk Management | Enterprise Risk Management | Fraud Risk Management |
| Financial Crime Compliance | L1 | Compliance & Financial Crime | — | FinCrime, Compliance |
| KYC Management | L2 | Compliance & Financial Crime | Financial Crime Compliance | Know Your Customer |
| AML Monitoring | L2 | Compliance & Financial Crime | Financial Crime Compliance | Anti-Money Laundering |
| Transaction Monitoring | L3 | Compliance & Financial Crime | AML Monitoring | Transaction Surveillance |
| Sanctions Screening | L3 | Compliance & Financial Crime | AML Monitoring | Watchlist Screening |
| Regulatory Compliance | L2 | Compliance & Financial Crime | Financial Crime Compliance | Compliance Management |
| Regulatory Reporting | L3 | Compliance & Financial Crime | Regulatory Compliance | Reg Reporting |
| Channel Management | L1 | Channels & Engagement | — | Channels |
| Digital Banking | L2 | Channels & Engagement | Channel Management | Digital Channels |
| Mobile Banking | L3 | Channels & Engagement | Digital Banking | Mobile App Banking |
| Online Banking | L3 | Channels & Engagement | Digital Banking | Internet Banking |
| Branch Banking | L2 | Channels & Engagement | Channel Management | Branch Network |
| Contact Center | L2 | Channels & Engagement | Channel Management | Call Center |
| ATM Management | L2 | Channels & Engagement | Channel Management | ATM Network |
| Finance Management | L1 | Finance & Treasury | — | Finance |
| General Ledger Accounting | L2 | Finance & Treasury | Finance Management | GL Accounting |
| Financial Reporting | L2 | Finance & Treasury | Finance Management | Internal Reporting |
| Regulatory Capital Management | L2 | Finance & Treasury | Finance Management | Capital Management |
| Treasury Management | L1 | Finance & Treasury | — | Treasury |
| Liquidity Management | L2 | Finance & Treasury | Treasury Management | Cash & Liquidity |
| Asset Liability Management | L2 | Finance & Treasury | Treasury Management | ALM |
| Journal Management | L3 | Finance & Treasury | General Ledger Accounting | Journal Entry Management, GL Posting Management, Manual Journals |
| Chart Of Accounts Management | L3 | Finance & Treasury | General Ledger Accounting | COA Management, Account Structure Governance, Ledger Hierarchy Management |
| Intercompany Accounting | L3 | Finance & Treasury | General Ledger Accounting | Intercompany Transactions, IC Accounting, Inter-Entity Accounting |
| Reconciliation & Close | L3 | Finance & Treasury | General Ledger Accounting | Period-End Close, GL Reconciliation |
| Fixed Asset Accounting | L3 | Finance & Treasury | General Ledger Accounting | Asset Register Management, Depreciation Accounting, Capital Asset Accounting |
| Financial Consolidation | L3 | Finance & Treasury | Financial Reporting | Group Consolidation, Consolidation & Eliminations, IFRS 10 Consolidation |
| Statutory Reporting | L3 | Finance & Treasury | Financial Reporting | External Financial Reporting, Statutory Accounts, IAS 1 Reporting |
| Internal Management Reporting | L3 | Finance & Treasury | Financial Reporting | MI Reporting, Performance Reporting (Finance) |
| Disclosure Management | L3 | Finance & Treasury | Financial Reporting | Notes & Disclosures, Disclosure Reporting, XBRL Disclosure |
| RWA Calculation | L3 | Finance & Treasury | Regulatory Capital Management | Risk-Weighted Assets Calculation, RWA Computation, Basel RWA |
| Capital Planning | L3 | Finance & Treasury | Regulatory Capital Management | Capital Forecasting, Capital Plan Management, Capital Strategy |
| Capital Adequacy Reporting | L3 | Finance & Treasury | Regulatory Capital Management | Capital Reporting, COREP Reporting, Own Funds Reporting |
| Treasury Cash Positioning | L3 | Finance & Treasury | Liquidity Management | Cash Position Keeping, Nostro Positioning |
| Funding Management | L3 | Finance & Treasury | Liquidity Management | Funding Execution, Wholesale Funding Management, Treasury Funding |
| Collateral & Reserve Management | L3 | Finance & Treasury | Liquidity Management | Treasury Collateral Management, Reserve Management, Liquidity Collateral Management |
| Intraday Liquidity Management | L3 | Finance & Treasury | Liquidity Management | Intraday Funding Management, Intraday Cash Management, Throughput Management |
| Interest Rate Risk In The Banking Book | L3 | Finance & Treasury | Asset Liability Management | IRRBB Management, Banking Book Rate Risk, EVE & NII Management |
| Funds Transfer Pricing Management | L3 | Finance & Treasury | Asset Liability Management | FTP Management, Internal Funds Pricing Capability, Matched-Maturity FTP |
| Balance Sheet Management | L3 | Finance & Treasury | Asset Liability Management | Structural Balance Sheet Management, ALCO Management, Balance Sheet Optimisation |
| Hedge Management | L3 | Finance & Treasury | Asset Liability Management | Hedge Accounting Management, Treasury Hedging, Macro Hedge Management |
| Journal Validation & Control | L4 | Finance & Treasury | Journal Management | Journal Approval Control, Posting Validation, Journal SoD Control |
| Accruals & Provisions Posting | L4 | Finance & Treasury | Journal Management | Accrual Posting, Provision Posting, Period-End Accruals |
| Ledger Account Mapping | L4 | Finance & Treasury | Chart Of Accounts Management | Account Mapping, GL Mapping Rules, Sub-Ledger Mapping |
| Intercompany Elimination | L4 | Finance & Treasury | Intercompany Accounting | IC Elimination, Intra-Group Elimination, Reciprocal Elimination |
| Close Task Orchestration | L4 | Finance & Treasury | Reconciliation & Close | Close Calendar Management, Close Checklist Orchestration, Close Certification |
| Account Substantiation | L4 | Finance & Treasury | Reconciliation & Close | Balance Sheet Substantiation, Account Certification, Recon Substantiation |
| Consolidation Eliminations | L4 | Finance & Treasury | Financial Consolidation | Consolidation Adjustments, Group Eliminations, NCI Adjustments |
| Currency Translation | L4 | Finance & Treasury | Financial Consolidation | FX Translation, Foreign Currency Translation, CTA Management |
| Primary Statement Production | L4 | Finance & Treasury | Statutory Reporting | Financial Statement Production, Primary Statements, IAS 1 Statements |
| Profitability Analytics | L4 | Finance & Treasury | Internal Management Reporting | Cost & Profitability Analysis, Product Profitability, Customer Profitability |
| Budgeting & Forecasting | L4 | Finance & Treasury | Internal Management Reporting | Planning & Forecasting, Budget Management, Variance Analysis |
| Credit Risk RWA | L4 | Finance & Treasury | RWA Calculation | Credit RWA, SA-CR RWA, IRB RWA |
| Leverage Ratio Calculation | L4 | Finance & Treasury | Capital Adequacy Reporting | Leverage Exposure Measure, LR Calculation, Leverage Ratio |
| Capital Stress Forecasting | L4 | Finance & Treasury | Capital Planning | Capital Projection, Stressed Capital Forecast, Capital Scenario Forecasting |
| Cash Flow Forecasting | L4 | Finance & Treasury | Treasury Cash Positioning | Treasury Cash Forecasting, Liquidity Cash Forecasting, Cash Projection |
| Wholesale Funding Execution | L4 | Finance & Treasury | Funding Management | Money Market Funding, Repo Funding, Debt Issuance Funding |
| Collateral Optimisation | L4 | Finance & Treasury | Collateral & Reserve Management | Collateral Allocation, Collateral Substitution, Treasury Collateral Optimisation |
| EVE Sensitivity Analysis | L4 | Finance & Treasury | Interest Rate Risk In The Banking Book | Economic Value Of Equity Analysis, EVE Shock Analysis, EVE Measurement |
| NII Sensitivity Analysis | L4 | Finance & Treasury | Interest Rate Risk In The Banking Book | Net Interest Income Sensitivity, Earnings-at-Risk, NII Simulation |
| Behavioural Modelling | L4 | Finance & Treasury | Interest Rate Risk In The Banking Book | NMD Modelling, Prepayment Modelling, Behavioural Assumptions |
| FTP Rate Curve Management | L4 | Finance & Treasury | Funds Transfer Pricing Management | Transfer Curve Management, FTP Curve Construction, Liquidity Premium Curves |
| Hedge Effectiveness Testing | L4 | Finance & Treasury | Hedge Management | Effectiveness Testing, Hedge Qualification Testing, IFRS 9 Effectiveness |
| Payment Order Capture | L3 | Payments | Payment Initiation | Payment Order Management, Order Capture |
| Request To Pay | L3 | Payments | Payment Initiation | Request for Payment, RfP, RTP Request |
| Payment Pre-Validation | L3 | Payments | Payment Initiation | Beneficiary Validation, Account Verification, Confirmation of Payee |
| Standing Order Management | L3 | Payments | Payment Initiation | Recurring Payments, Standing Instructions |
| Bulk Payment Origination | L3 | Payments | Payment Initiation | Batch Payments, File-Based Payments, Bulk Disbursement |
| Payment Screening | L3 | Payments | Payment Initiation | Payment Compliance Check, Watchlist Filtering |
| Payment Rail Connectivity | L3 | Payments | Payment Execution | Rail Integration, Scheme Connectivity, Gateway Management |
| Correspondent Banking | L3 | Payments | Payment Execution | Nostro Vostro Management, Correspondent Bank Operations |
| Payment Status Tracking | L3 | Payments | Payment Execution | Payment Tracking, Status Reporting, gpi Tracking |
| Interbank Clearing | L3 | Payments | Payment Clearing & Settlement | Clearing Operations, Net Position Calculation |
| Interbank Settlement | L3 | Payments | Payment Clearing & Settlement | Settlement Operations, RTGS Settlement |
| Settlement Liquidity Management | L3 | Payments | Payment Clearing & Settlement | Settlement Funding, Liquidity Positioning, LMT |
| Payment Exceptions & Investigations | L3 | Payments | Payment Clearing & Settlement | Payment Investigations, Exception Handling, Recalls |
| Direct Debit Mandate Management | L3 | Payments | Direct Debit Management | Mandate Management, DDI Setup |
| Direct Debit Collection | L3 | Payments | Direct Debit Management | Direct Debit Processing, Creditor Collection |
| Direct Debit Returns | L3 | Payments | Direct Debit Management | DD Returns, Unpaids, Indemnity Claims |
| Credit Transfer Execution | L4 | Payments | Domestic Payments | ACH Credit, Direct Credit, Push Payment |
| Debit Transfer Execution | L4 | Payments | Domestic Payments | ACH Debit, Pull Payment |
| Same Day ACH Processing | L4 | Payments | Domestic Payments | SDA, Same-Day ACH |
| ACH Return Handling | L4 | Payments | Domestic Payments | ACH Returns, Return Codes, R-codes |
| SWIFT Message Processing | L4 | Payments | Cross-Border Payments | SWIFT Messaging, CBPR+, MT/MX |
| FX Conversion For Payments | L4 | Payments | Cross-Border Payments | Payment FX, Currency Conversion |
| Cross-Border Fee Calculation | L4 | Payments | Cross-Border Payments | Charge Bearer Handling, Correspondent Fees |
| Instant Payment Clearing | L4 | Payments | Real-Time Payments | RTP Clearing, FedNow Clearing |
| Instant Payment Confirmation | L4 | Payments | Real-Time Payments | Real-Time Confirmation, Positive Acknowledgement |
| Alias Resolution | L4 | Payments | Real-Time Payments | Proxy Lookup, Directory Resolution |
| File Validation & Enrichment | L4 | Payments | Bulk Payment Origination | Bulk File Validation, File Ingestion |
| Payment Authorization Capture | L4 | Payments | Payment Order Capture | Order Authorization, Payment Approval |
| Payment Limit Checking | L4 | Payments | Payment Order Capture | Limit Validation, Threshold Checks |
| Mandate Verification | L4 | Payments | Direct Debit Collection | Mandate Check, Authorisation Check |
| Collection Scheduling | L4 | Payments | Direct Debit Collection | DD Scheduling, Collection Runs |
| Settlement Reconciliation | L4 | Payments | Interbank Settlement | Settlement Matching, Position Reconciliation |
| Nostro Reconciliation | L4 | Payments | Correspondent Banking | Nostro Matching, Vostro Reconciliation |
| Lead Management | L3 | Customer Management | Customer Acquisition | Lead and Opportunity Management, Prospect Management, Opportunity Management |
| Application Processing | L3 | Customer Management | Customer Acquisition | Application Management, Account Application Handling, Origination Intake |
| Onboarding Orchestration | L3 | Customer Management | Customer Acquisition | Onboarding Coordination, Origination Orchestration |
| Party Reference Data | L3 | Customer Management | Party Data Management | Party Master Data, Customer Reference Data, Golden Record |
| Party Data Quality | L3 | Customer Management | Party Data Management | Customer Data Quality, Data Cleansing, Deduplication Management |
| Consent & Preference Management | L3 | Customer Management | Party Data Management | Consent Management, Preference Management, Permissions Management |
| Contact Dialogue Management | L3 | Customer Management | Customer Servicing | Contact Management, Interaction Management, Dialogue Handling |
| Complaint Management | L3 | Customer Management | Customer Servicing | Complaints Management, Grievance Management |
| Service Fulfilment | L3 | Customer Management | Customer Servicing | Service Order Fulfilment, Servicing Order Management, Request Fulfilment |
| Relationship Planning | L3 | Customer Management | Relationship Management | Customer Planning, Account Planning, Relationship Strategy |
| Next-Best-Action | L3 | Customer Management | Relationship Management | NBA, Next Best Offer, Recommendation Management |
| Campaign Execution | L3 | Customer Management | Campaign Management | Campaign Operations, Campaign Delivery, Marketing Execution |
| Customer Insight | L3 | Customer Management | Customer Segmentation | Customer Analytics, Customer Intelligence, Customer Value Analytics |
| Behavioural Analytics | L3 | Customer Management | Customer Segmentation | Behavioral Analytics, Customer Event Analytics, Behavioural Pattern Modelling |
| Lead Capture | L4 | Customer Management | Lead Management | Lead Intake, Inquiry Capture |
| Lead Qualification | L4 | Customer Management | Lead Management | Lead Scoring, Lead Routing |
| Application Decisioning | L4 | Customer Management | Application Processing | Application Adjudication, Eligibility Decisioning |
| Application Tracking | L4 | Customer Management | Application Processing | Application Status Management, Application Monitoring |
| Agreement Activation | L4 | Customer Management | Onboarding Orchestration | Account Activation, Agreement Setup |
| Welcome Servicing | L4 | Customer Management | Onboarding Orchestration | Welcome Journey, First-Use Enablement |
| Party Identifier Management | L4 | Customer Management | Party Reference Data | Party ID Management, Identifier Cross-Referencing |
| Party Relationship Mapping | L4 | Customer Management | Party Reference Data | Relationship Hierarchy Management, Household Linking, Beneficial Ownership Mapping |
| Data Survivorship | L4 | Customer Management | Party Data Quality | Survivorship Rules, Record Merge, Golden Record Resolution |
| Consent Lifecycle | L4 | Customer Management | Consent & Preference Management | Consent Tracking, Consent Versioning |
| Communication Preference Management | L4 | Customer Management | Consent & Preference Management | Channel Preferences, Marketing Permissions, Contact Preferences |
| Contact Routing Management | L4 | Customer Management | Contact Dialogue Management | Interaction Routing, Contact Skills Routing |
| Interaction History | L4 | Customer Management | Contact Dialogue Management | Contact History, Channel Activity History |
| Complaint Resolution | L4 | Customer Management | Complaint Management | Complaint Investigation, Redress Management |
| Complaint Root-Cause Analysis | L4 | Customer Management | Complaint Management | Complaint Analytics, Root Cause Feedback |
| Servicing Order Orchestration | L4 | Customer Management | Service Fulfilment | Order Orchestration, Servicing Workflow |
| Customer Survey Management | L4 | Customer Management | Customer Insight | Voice of Customer, Survey Management, Feedback Management |
| Customer Value Modelling | L4 | Customer Management | Customer Insight | Lifetime Value Modelling, CLV Analytics, Propensity Modelling |
| Customer Event Detection | L4 | Customer Management | Behavioural Analytics | Trigger Detection, Life Event Detection |
| Churn Prediction | L4 | Customer Management | Behavioural Analytics | Attrition Modelling, Retention Analytics |
| Loan Application Management | L3 | Lending & Credit | Loan Origination | Application Intake (Lending), Credit Application Handling |
| Affordability Assessment | L3 | Lending & Credit | Loan Origination | Serviceability Assessment, Affordability Check |
| Loan Pricing | L3 | Lending & Credit | Loan Origination | Risk-Based Pricing, Rate Setting |
| Loan Approval | L3 | Lending & Credit | Loan Origination | Credit Sanctioning, Offer Issuance |
| Loan Disbursement | L3 | Lending & Credit | Loan Origination | Fund Disbursement, Loan Drawdown |
| Loan Documentation Management | L3 | Lending & Credit | Loan Origination | Credit Agreement Management, Loan Doc Preparation |
| Repayment Processing | L3 | Lending & Credit | Loan Servicing | Loan Repayment Handling, Installment Processing |
| Loan Account Maintenance | L3 | Lending & Credit | Loan Servicing | Loan Account Administration, Facility Maintenance |
| Statement & Notices | L3 | Lending & Credit | Loan Servicing | Loan Statements, Borrower Notices |
| Loan Modification | L3 | Lending & Credit | Loan Servicing | Loan Restructuring, Variation Management |
| Payoff & Closure | L3 | Lending & Credit | Loan Servicing | Loan Settlement, Loan Closure |
| Syndicated Loan Administration | L3 | Lending & Credit | Loan Servicing | Syndication Servicing, Participation Management |
| Collateral Valuation | L3 | Lending & Credit | Collateral Management | Asset Valuation (Lending), Security Valuation |
| Collateral Perfection | L3 | Lending & Credit | Collateral Management | Lien Perfection, Charge Registration |
| Collateral Release | L3 | Lending & Credit | Collateral Management | Security Discharge, Lien Release |
| Guarantee Administration | L3 | Lending & Credit | Collateral Management | Surety Management, Guarantee Servicing |
| Delinquency Management | L3 | Lending & Credit | Collections & Recovery | Arrears Management, Early Collections |
| Hardship & Forbearance | L3 | Lending & Credit | Collections & Recovery | Financial Hardship Handling, Forbearance Management |
| Recovery & Write-Off | L3 | Lending & Credit | Collections & Recovery | Debt Recovery, Charge-Off Management |
| Application Eligibility Screening | L4 | Lending & Credit | Loan Application Management | Pre-Qualification, Eligibility Pre-Screen |
| Application Data Capture | L4 | Lending & Credit | Loan Application Management | Loan Data Intake, Applicant Data Capture |
| Credit Bureau Retrieval | L4 | Lending & Credit | Affordability Assessment | Bureau Pull, Credit Reference Retrieval |
| Income Verification | L4 | Lending & Credit | Affordability Assessment | Income & Expense Verification, Earnings Verification |
| Risk-Grade Assignment | L4 | Lending & Credit | Affordability Assessment | Credit Grading, Rating Assignment |
| Pricing Exception Handling | L4 | Lending & Credit | Loan Pricing | Rate Override Management, Pricing Override |
| Approval Authority Routing | L4 | Lending & Credit | Loan Approval | Delegated Authority Routing, Mandate Routing |
| Condition Precedent Tracking | L4 | Lending & Credit | Loan Approval | CP Tracking, Covenant Pre-Disbursement Tracking |
| Disbursement Authorization | L4 | Lending & Credit | Loan Disbursement | Drawdown Authorization, Release Authorization |
| Repayment Schedule Management | L4 | Lending & Credit | Repayment Processing | Amortization Scheduling, Schedule Recalculation |
| Payment Allocation | L4 | Lending & Credit | Repayment Processing | Repayment Allocation, Waterfall Allocation |
| Prepayment Handling | L4 | Lending & Credit | Repayment Processing | Overpayment Handling, Partial Prepayment |
| Escrow Administration | L4 | Lending & Credit | Loan Account Maintenance | Impound Account Management, Tax & Insurance Escrow |
| Interest Accrual Management | L4 | Lending & Credit | Loan Account Maintenance | Loan Interest Accrual, Accrual Posting |
| Settlement Quotation | L4 | Lending & Credit | Payoff & Closure | Payoff Quote, Redemption Statement |
| Revaluation Scheduling | L4 | Lending & Credit | Collateral Valuation | Collateral Revaluation, Valuation Refresh |
| Lien Registration | L4 | Lending & Credit | Collateral Perfection | Charge Filing, Security Registration |
| Treatment Strategy Management | L4 | Lending & Credit | Delinquency Management | Collections Strategy, Treatment Path Management |
| Promise-To-Pay Management | L4 | Lending & Credit | Delinquency Management | PTP Management, Repayment Promise Tracking |
| Repossession Management | L4 | Lending & Credit | Recovery & Write-Off | Asset Repossession, Collateral Liquidation |
| Debt Sale Management | L4 | Lending & Credit | Recovery & Write-Off | Portfolio Debt Sale, NPL Sale |
| Deposit Account Origination | L3 | Deposits & Accounts | Account Opening | Account Origination Capability, New Account Establishment |
| Deposit Product Selection | L3 | Deposits & Accounts | Account Opening | Product Matching, Deposit Product Fit |
| First Deposit Funding | L3 | Deposits & Accounts | Account Opening | Initial Funding, Account Funding |
| Account Activation Control | L3 | Deposits & Accounts | Account Opening | Deposit Activation, Go-Live Control |
| Eligibility & Suitability Screening | L3 | Deposits & Accounts | Account Opening | Account Eligibility Check, Opening Suitability |
| Transaction Posting | L3 | Deposits & Accounts | Account Servicing | Ledger Posting, Account Posting |
| Account Balance Management | L3 | Deposits & Accounts | Account Servicing | Balance Keeping, Available Balance Control |
| Account Maintenance Servicing | L3 | Deposits & Accounts | Account Servicing | Account Amendments, Account Care |
| Deposit Statement & Reporting | L3 | Deposits & Accounts | Account Servicing | Account Statement Capability, Deposit Reporting |
| Standing Orders & Sweeps | L3 | Deposits & Accounts | Account Servicing | Sweep Management, Account Standing Instructions |
| Deposit Direct Debit Authorisation | L3 | Deposits & Accounts | Account Servicing | Debtor Mandate Management, Account DD Authorisation |
| Account Closure Servicing | L3 | Deposits & Accounts | Account Servicing | Deposit Closure, Account Termination |
| Dormancy Management | L3 | Deposits & Accounts | Account Servicing | Inactive Account Management, Unclaimed Balance Handling |
| Distressed Account Recovery | L3 | Deposits & Accounts | Account Servicing | Account Recovery Capability, Distressed Deposit Handling |
| Account Reconciliation Servicing | L3 | Deposits & Accounts | Account Servicing | Deposit Recon, Account Matching |
| Deposit Interest Accrual | L3 | Deposits & Accounts | Interest Calculation | Credit Interest Accrual, Savings Interest Accrual |
| Deposit Interest Posting | L3 | Deposits & Accounts | Interest Calculation | Interest Capitalisation, Interest Credit |
| Deposit Tax Withholding | L3 | Deposits & Accounts | Interest Calculation | Withholding Tax Handling, Interest Tax Reporting |
| Deposit Rate Management | L3 | Deposits & Accounts | Interest Calculation | Interest Rate Management, Rate Table Management |
| Term Deposit Lifecycle | L3 | Deposits & Accounts | Interest Calculation | Fixed Deposit Management, Time Deposit Lifecycle |
| Overdraft Facility Setup | L3 | Deposits & Accounts | Overdraft Management | Overdraft Arrangement, Limit Setup |
| Overdraft Limit Monitoring | L3 | Deposits & Accounts | Overdraft Management | Overdraft Monitoring, Utilisation Monitoring |
| Unauthorised Overdraft Handling | L3 | Deposits & Accounts | Overdraft Management | Unarranged Overdraft Handling, Excess Management |
| Application Capture & Validation | L4 | Deposits & Accounts | Deposit Account Origination | Account Application Capture, Opening Data Validation |
| Account Instantiation | L4 | Deposits & Accounts | Deposit Account Origination | Account Record Creation, Account Provisioning |
| Beneficial Ownership Capture | L4 | Deposits & Accounts | Deposit Account Origination | Signatory Capture, Joint Holder Setup |
| Value-Dated Posting | L4 | Deposits & Accounts | Transaction Posting | Value Dating, Effective-Date Posting |
| Transaction Reversal Handling | L4 | Deposits & Accounts | Transaction Posting | Entry Reversal, Posting Correction |
| Account Hold & Block Management | L4 | Deposits & Accounts | Account Balance Management | Funds Hold Management, Earmark Management |
| Account Detail Amendment | L4 | Deposits & Accounts | Account Maintenance Servicing | Attribute Amendment, Account Update |
| Mandate & Signatory Maintenance | L4 | Deposits & Accounts | Account Maintenance Servicing | Signatory Maintenance, Operating Mandate Update |
| Deposit Statement Production | L4 | Deposits & Accounts | Deposit Statement & Reporting | Statement Rendering, Statement Generation Engine |
| Deposit Statement Delivery | L4 | Deposits & Accounts | Deposit Statement & Reporting | Statement Dispatch, Advice Delivery |
| Sweep Rule Execution | L4 | Deposits & Accounts | Standing Orders & Sweeps | Sweep Execution, Balance Sweep Run |
| Dormancy Detection | L4 | Deposits & Accounts | Dormancy Management | Inactivity Detection, Dormant Flagging |
| Escheatment Processing | L4 | Deposits & Accounts | Dormancy Management | Unclaimed Property Remittance, Escheat Handling |
| Closure Settlement | L4 | Deposits & Accounts | Account Closure Servicing | Final Balance Settlement, Closure Payout |
| Interest Accrual Calculation | L4 | Deposits & Accounts | Deposit Interest Accrual | Daily Accrual Calculation, Accrual Engine |
| Tiered Interest Determination | L4 | Deposits & Accounts | Deposit Interest Accrual | Tier Rate Selection, Bonus Interest Determination |
| Withholding Tax Calculation | L4 | Deposits & Accounts | Deposit Tax Withholding | WHT Calculation, Interest Tax Deduction |
| Tax Reporting Consolidation | L4 | Deposits & Accounts | Deposit Tax Withholding | Year-End Tax Reporting, Tax Statement Consolidation |
| Maturity & Rollover Processing | L4 | Deposits & Accounts | Term Deposit Lifecycle | Rollover Processing, Renewal Handling |
| Early Withdrawal Handling | L4 | Deposits & Accounts | Term Deposit Lifecycle | Break Handling, Pre-Maturity Withdrawal |
| Overdraft Limit Assessment | L4 | Deposits & Accounts | Overdraft Facility Setup | Limit Sizing, Overdraft Eligibility |
| Overdraft Interest & Fee Charging | L4 | Deposits & Accounts | Unauthorised Overdraft Handling | Debit Interest Charging, Overdraft Fee Application |
| Card Application | L3 | Cards | Card Issuing | Card Onboarding, New Card Application |
| Credit Limit Assignment | L3 | Cards | Card Issuing | Credit Line Setting, Limit Assignment |
| Card Production & Fulfilment | L3 | Cards | Card Issuing | Card Manufacturing, Card Production |
| Card Personalisation | L4 | Cards | Card Production & Fulfilment | Card Encoding, EMV Personalisation |
| Card Dispatch & Delivery | L4 | Cards | Card Production & Fulfilment | Card Distribution, Card Mailing |
| Card Activation | L3 | Cards | Card Issuing | Card Enablement, First Use Activation |
| Card Tokenisation | L3 | Cards | Card Issuing | Network Tokenisation, Wallet Provisioning, Token Provisioning |
| Authorization Decisioning | L3 | Cards | Card Authorization | Authorization Approval, Auth Decisioning |
| Balance & Funds Verification | L4 | Cards | Authorization Decisioning | Available Balance Check, Open-to-Buy Check |
| Card Fraud Authorization Screening | L4 | Cards | Authorization Decisioning | Auth Fraud Screening, Real-Time Fraud Scoring (Cards) |
| Stand-In Authorization | L3 | Cards | Card Authorization | STIP, Stand-In Processing, Fallback Authorization |
| Authorization Controls | L3 | Cards | Card Authorization | Spending Controls, Velocity Controls, Card Controls |
| Card Clearing & Settlement | L3 | Cards | Card Authorization | Card Clearing, Card Settlement, Interchange Settlement |
| Card Billing & Statements | L3 | Cards | Card Authorization | Card Billing, Statement Cycle Processing |
| Chargeback Handling | L3 | Cards | Dispute Management | Chargeback Initiation, Issuer Chargeback Management |
| Chargeback Filing | L4 | Cards | Chargeback Handling | Reason Code Assignment, Chargeback Submission |
| Provisional Credit Management | L4 | Cards | Chargeback Handling | Temporary Credit Handling, Dispute Credit |
| Representment Handling | L3 | Cards | Dispute Management | Second Presentment Handling, Re-presentment |
| Dispute Investigation | L3 | Cards | Dispute Management | Dispute Case Investigation, Claim Investigation |
| Dispute Evidence Management | L4 | Cards | Dispute Investigation | Evidence Collation, Compelling Evidence Management |
| Pre-Arbitration & Arbitration | L3 | Cards | Dispute Management | Arbitration, Pre-Arbitration Handling, Dispute Escalation |
| Card Renewal | L3 | Cards | Card Lifecycle Management | Card Reissuance, Expiry Renewal |
| Card Replacement | L3 | Cards | Card Lifecycle Management | Lost/Stolen Replacement, Emergency Card Replacement |
| Card Blocking | L3 | Cards | Card Lifecycle Management | Card Hotlisting, Card Suspension, Block/Unblock |
| PIN Management | L3 | Cards | Card Lifecycle Management | PIN Services, PIN Reset, PIN Change |
| Card Closure | L3 | Cards | Card Lifecycle Management | Card Cancellation, Card Account Closure |
| Rewards Management | L3 | Cards | Card Lifecycle Management | Loyalty Management, Rewards & Points, Cashback Management |
| Reward Points Accrual | L4 | Cards | Rewards Management | Points Earning, Loyalty Accrual |
| Reward Points Redemption | L4 | Cards | Rewards Management | Points Redemption, Loyalty Redemption |
| Card Collections | L3 | Cards | Card Lifecycle Management | Card Dunning, Card Arrears Management |
| Cardholder Notifications | L3 | Cards | Card Lifecycle Management | Card Alerts, Transaction Alerts |
| Portfolio Construction | L3 | Wealth & Investments | Portfolio Management | Portfolio Build, Portfolio Modelling |
| Asset Allocation | L3 | Wealth & Investments | Portfolio Management | Strategic Asset Allocation, SAA/TAA |
| Portfolio Rebalancing Management | L3 | Wealth & Investments | Portfolio Management | Rebalancing Capability, Drift Management Capability |
| Performance Measurement | L3 | Wealth & Investments | Portfolio Management | Performance & Attribution, GIPS Reporting |
| Portfolio Accounting | L3 | Wealth & Investments | Portfolio Management | Investment Bookkeeping, Investment Book of Record Capability |
| Investment Mandate Management | L3 | Wealth & Investments | Portfolio Management | Mandate Compliance, IPS Management |
| Financial Planning Advisory | L3 | Wealth & Investments | Investment Advisory | Wealth Planning Capability, Comprehensive Planning |
| Suitability Assessment | L3 | Wealth & Investments | Investment Advisory | Suitability & Appropriateness, Investor Profiling |
| Investment Research | L3 | Wealth & Investments | Investment Advisory | Securities Research, Market Research (Investments) |
| Advice Generation | L3 | Wealth & Investments | Investment Advisory | Advisory Recommendation, Robo-Advice |
| Goal Planning | L3 | Wealth & Investments | Investment Advisory | Goal-Based Investing, Goal Tracking |
| Best Interest Compliance | L3 | Wealth & Investments | Investment Advisory | Reg BI Compliance, Care Obligation Management |
| Order Management | L3 | Wealth & Investments | Brokerage & Trading | Order Lifecycle Management, OMS Capability |
| Trade Execution | L3 | Wealth & Investments | Brokerage & Trading | Execution Management, Best Execution |
| Trade Settlement | L3 | Wealth & Investments | Brokerage & Trading | Securities Settlement, Clearing & Settlement (Securities) |
| Custody & Safekeeping | L3 | Wealth & Investments | Brokerage & Trading | Custody Administration, Asset Servicing |
| Corporate Actions Processing | L3 | Wealth & Investments | Brokerage & Trading | Corporate Action Handling, Asset Servicing Events |
| Securities Position Keeping | L3 | Wealth & Investments | Brokerage & Trading | Position Management (Securities), Holdings Keeping |
| Allocation Optimisation | L4 | Wealth & Investments | Asset Allocation | Mean-Variance Optimisation, Efficient Frontier |
| Capital Market Assumptions | L4 | Wealth & Investments | Asset Allocation | CMA Modelling, Return Forecasting |
| Tolerance Band Monitoring | L4 | Wealth & Investments | Portfolio Rebalancing Management | Drift Monitoring, Rebalance Trigger |
| Tax-Loss Harvesting | L4 | Wealth & Investments | Portfolio Rebalancing Management | Tax Optimisation (Investments), TLH |
| Return Attribution | L4 | Wealth & Investments | Performance Measurement | Performance Attribution, Brinson Attribution |
| Benchmark Management | L4 | Wealth & Investments | Performance Measurement | Composite Management, Benchmark Administration |
| Investment Valuation | L4 | Wealth & Investments | Portfolio Accounting | Pricing & Valuation (Investments), NAV Calculation |
| Cost Basis Tracking | L4 | Wealth & Investments | Portfolio Accounting | Tax Lot Accounting, Basis Reporting |
| Risk Tolerance Profiling | L4 | Wealth & Investments | Suitability Assessment | Risk Profiling, Risk Capacity Assessment |
| Suitability Report Production | L4 | Wealth & Investments | Suitability Assessment | Suitability Statement, Advice Disclosure |
| Product Recommendation | L4 | Wealth & Investments | Advice Generation | Investment Recommendation, Model Portfolio Matching |
| Retirement Projection | L4 | Wealth & Investments | Goal Planning | Retirement Modelling, Decumulation Planning |
| Order Routing | L4 | Wealth & Investments | Order Management | Smart Order Routing, Venue Selection |
| Order Allocation | L4 | Wealth & Investments | Order Management | Block Allocation, Fill Allocation |
| Trade Affirmation | L4 | Wealth & Investments | Trade Settlement | Affirmation & Confirmation, Trade Matching |
| Settlement Instruction Management | L4 | Wealth & Investments | Trade Settlement | SSI Management, Settlement Messaging |
| Trade Fail Management | L4 | Wealth & Investments | Trade Settlement | Fails Management, Settlement Exceptions |
| Asset Safekeeping | L4 | Wealth & Investments | Custody & Safekeeping | Safekeeping Records, Depository Reconciliation |
| Income Collection | L4 | Wealth & Investments | Custody & Safekeeping | Dividend Collection, Coupon Processing |
| Corporate Action Election | L4 | Wealth & Investments | Corporate Actions Processing | Voluntary Election Handling, Proxy Voting |
| Risk Appetite Management | L2 | Risk Management | Enterprise Risk Management | Risk Appetite Framework, Tolerance Setting, RAS Management |
| Risk Identification | L2 | Risk Management | Enterprise Risk Management | Risk Taxonomy Management, Emerging Risk Scanning, Risk Register Management |
| Stress Testing Management | L2 | Risk Management | Enterprise Risk Management | Scenario Stress Testing, Reverse Stress Testing, CCAR Stress Testing |
| Model Risk Management | L2 | Risk Management | Enterprise Risk Management | Model Governance, Model Validation, MRM |
| Regulatory Capital Adequacy | L2 | Risk Management | Enterprise Risk Management | ICAAP, Economic Capital Management, Capital Adequacy Assessment |
| Risk Reporting & Governance | L2 | Risk Management | Enterprise Risk Management | Risk Data Aggregation & Governance, BCBS 239 Compliance |
| Risk Capital Calculation | L3 | Risk Management | Regulatory Capital Adequacy | RWA Charge Calculation, Capital Charge Computation, Capital Charge Engine |
| Scenario Library Management | L3 | Risk Management | Stress Testing Management | Scenario Design, Scenario Catalogue, Macro Scenario Management |
| Model Inventory Management | L3 | Risk Management | Model Risk Management | Model Register, Model Tiering, Model Catalogue |
| Credit Risk Assessment | L3 | Risk Management | Credit Risk Management | Counterparty Credit Assessment, Credit Risk Analysis |
| Credit Risk Rating | L3 | Risk Management | Credit Risk Management | Internal Ratings, Rating Model Management, IRB Rating |
| Credit Exposure Management | L3 | Risk Management | Credit Risk Management | Counterparty Exposure Management, EAD Measurement |
| Credit Risk Mitigation | L3 | Risk Management | Credit Risk Management | CRM Techniques, Collateral Risk Mitigation, Netting Recognition |
| Provisioning & ECL | L3 | Risk Management | Credit Risk Management | Expected Credit Loss, Impairment Provisioning, IFRS 9 Staging |
| Limit & Exposure Management | L4 | Risk Management | Credit Exposure Management | Credit Limit Management, Limit Monitoring, Concentration Limit Control |
| PD LGD EAD Estimation | L4 | Risk Management | Credit Risk Rating | Risk Parameter Estimation, Default Parameter Modelling |
| Concentration Risk Analysis | L4 | Risk Management | Credit Exposure Management | Single-Name Concentration, Portfolio Concentration Analysis |
| Market Risk Measurement | L3 | Risk Management | Market Risk Management | Market Risk Metrics, Sensitivity Measurement |
| Value-at-Risk Calculation | L3 | Risk Management | Market Risk Management | Expected Shortfall Calculation, VaR/ES |
| Trading Book Risk | L3 | Risk Management | Market Risk Management | Trading Book Capital, FRTB Boundary Management |
| Counterparty Credit Risk | L3 | Risk Management | Market Risk Management | CCR Management, CVA Risk, SA-CCR Exposure |
| Sensitivities Calculation | L4 | Risk Management | Market Risk Measurement | Greeks Calculation, SBM Sensitivities, Risk Factor Sensitivities |
| Mark-to-Market Valuation | L4 | Risk Management | Market Risk Measurement | Independent Price Verification, Position Revaluation, IPV |
| Backtesting & P&L Attribution | L4 | Risk Management | Value-at-Risk Calculation | PLA Test, VaR Backtesting, Model Performance Testing |
| Risk & Control Self-Assessment | L3 | Risk Management | Operational Risk Management | RCSA, Control Self-Assessment |
| Loss Data Management | L3 | Risk Management | Operational Risk Management | Internal Loss Data, Loss Event Management, External Loss Data |
| Op Risk Scenario Analysis | L3 | Risk Management | Operational Risk Management | Operational Scenario Analysis, Tail-Risk Scenarios |
| Business Continuity Management | L3 | Risk Management | Operational Risk Management | BCM, Operational Resilience, Disaster Recovery Planning |
| Key Risk Indicator Monitoring | L4 | Risk Management | Risk & Control Self-Assessment | KRI Monitoring, Risk Indicator Tracking |
| Operational Risk Capital Modelling | L4 | Risk Management | Op Risk Scenario Analysis | Op Risk Capital, SMA Modelling, Loss Distribution Approach |
| Liquidity Risk Measurement | L3 | Risk Management | Liquidity Risk Management | Liquidity Gap Analysis, Survival Horizon Measurement |
| LCR & NSFR Management | L3 | Risk Management | Liquidity Risk Management | Liquidity Ratio Management, HQLA Management |
| Funding Risk Management | L3 | Risk Management | Liquidity Risk Management | Contingency Funding, ILAAP, Funding Concentration Management |
| Intraday Liquidity Monitoring | L4 | Risk Management | Liquidity Risk Measurement | Intraday Liquidity Oversight, Intraday Position Monitoring |
| HQLA Buffer Management | L4 | Risk Management | LCR & NSFR Management | Liquid Asset Buffer, HQLA Eligibility Management |
| Fraud Risk Assessment | L3 | Risk Management | Fraud Management | Fraud Risk Evaluation, Fraud Exposure Assessment |
| Fraud Monitoring | L3 | Risk Management | Fraud Management | Fraud Surveillance, Fraud Screening Capability |
| Fraud Loss Recovery | L3 | Risk Management | Fraud Management | Fraud Recovery, Fraud Reimbursement |
| Fraud Scoring Models | L4 | Risk Management | Fraud Monitoring | Fraud Risk Scoring, Fraud Model Development |
| Synthetic Identity Detection | L4 | Risk Management | Fraud Risk Assessment | Synthetic Fraud Detection, Identity Fraud Detection |
| Financial Crime Risk Compliance | L2 | Compliance & Financial Crime | Financial Crime Compliance | FinCrime Risk Compliance, Wider Financial Crime |
| AML Customer Due Diligence | L3 | Compliance & Financial Crime | KYC Management | CDD Management, AML CDD, Standard Due Diligence |
| Enhanced Due Diligence Management | L3 | Compliance & Financial Crime | KYC Management | EDD Management, High-Risk Diligence |
| Beneficial Ownership Identification | L3 | Compliance & Financial Crime | KYC Management | UBO Identification, Ownership Verification |
| Customer Risk Rating | L3 | Compliance & Financial Crime | KYC Management | AML Risk Scoring, Customer Risk Profiling |
| PEP Screening | L3 | Compliance & Financial Crime | KYC Management | Politically Exposed Person Screening, PEP Identification |
| KYC Refresh Management | L3 | Compliance & Financial Crime | KYC Management | Perpetual KYC, Periodic Review, KYC Remediation |
| Correspondent Banking Due Diligence | L3 | Compliance & Financial Crime | KYC Management | CBDDQ Management, Respondent Bank Diligence |
| Suspicious Activity Detection | L3 | Compliance & Financial Crime | AML Monitoring | Suspicious Behaviour Detection, AML Detection |
| Alert Management | L3 | Compliance & Financial Crime | AML Monitoring | AML Alert Triage, Alert Disposition |
| AML Case Investigation | L3 | Compliance & Financial Crime | AML Monitoring | Financial Crime Investigation, AML Case Handling |
| SAR Management | L3 | Compliance & Financial Crime | AML Monitoring | STR Management, Suspicious Activity Reporting Management |
| Watchlist Management | L3 | Compliance & Financial Crime | AML Monitoring | List Management, Sanctions List Management |
| Adverse Media Screening | L3 | Compliance & Financial Crime | AML Monitoring | Negative News Screening, Media Monitoring |
| Currency Transaction Reporting | L3 | Compliance & Financial Crime | AML Monitoring | CTR Management, Cash Transaction Reporting |
| Regulatory Change Compliance | L3 | Compliance & Financial Crime | Regulatory Compliance | Reg Change Tracking, Regulatory Change Interpretation |
| Compliance Risk Assessment | L3 | Compliance & Financial Crime | Regulatory Compliance | Financial Crime Risk Assessment, AML Risk Assessment |
| Compliance Policy Management | L3 | Compliance & Financial Crime | Regulatory Compliance | Policy & Standards Management, Compliance Procedures Management |
| Compliance Monitoring & Testing | L3 | Compliance & Financial Crime | Regulatory Compliance | Compliance Assurance, Independent Testing |
| Conduct Risk Management | L3 | Compliance & Financial Crime | Regulatory Compliance | Conduct Compliance, Market Conduct Management |
| Regulatory Examination Management | L3 | Compliance & Financial Crime | Regulatory Compliance | Exam Management, Regulator Relations |
| Anti-Bribery & Corruption | L3 | Compliance & Financial Crime | Financial Crime Risk Compliance | ABC Compliance, Bribery Prevention |
| Tax Evasion Compliance | L3 | Compliance & Financial Crime | Financial Crime Risk Compliance | Customer Tax Compliance, FATCA CRS Compliance |
| Bribery & Corruption Risk Assessment | L4 | Compliance & Financial Crime | Anti-Bribery & Corruption | ABC Risk Assessment, Corruption Risk Scoring |
| Third-Party Integrity Due Diligence | L4 | Compliance & Financial Crime | Anti-Bribery & Corruption | Intermediary Due Diligence, Vendor Integrity Screening |
| Source Of Wealth Verification | L4 | Compliance & Financial Crime | Enhanced Due Diligence Management | SoW Verification, Source Of Funds Verification |
| Senior Management Approval | L4 | Compliance & Financial Crime | Enhanced Due Diligence Management | EDD Approval, High-Risk Sign-Off |
| Ownership Structure Unwrapping | L4 | Compliance & Financial Crime | Beneficial Ownership Identification | Layered Ownership Analysis, UBO Unwrapping |
| Control Person Identification | L4 | Compliance & Financial Crime | Beneficial Ownership Identification | Controlling Party Identification, Control Prong |
| Risk Model Calibration | L4 | Compliance & Financial Crime | Customer Risk Rating | Rating Model Tuning, Risk Factor Weighting |
| Scenario Threshold Tuning | L4 | Compliance & Financial Crime | Suspicious Activity Detection | Detection Tuning, Rule Optimisation |
| Typology Modelling | L4 | Compliance & Financial Crime | Suspicious Activity Detection | ML Typology Modelling, Risk Typology Library |
| Alert Prioritisation Scoring | L4 | Compliance & Financial Crime | Alert Management | Alert Risk Scoring, Alert Ranking |
| Network Link Analysis | L4 | Compliance & Financial Crime | AML Case Investigation | Entity Network Analysis, Link Analytics |
| SAR Filing & Tracking | L4 | Compliance & Financial Crime | SAR Management | STR Filing, SAR Submission |
| SAR Confidentiality Control | L4 | Compliance & Financial Crime | SAR Management | Tipping-Off Prevention, SAR Access Control |
| Sanctions List Ingestion | L4 | Compliance & Financial Crime | Watchlist Management | List Ingestion, SDN Loading |
| Sanctions List Curation | L4 | Compliance & Financial Crime | Watchlist Management | List Quality Management, Whitelist Management |
| Obligation Mapping | L4 | Compliance & Financial Crime | Regulatory Change Compliance | Requirement Mapping, Control Mapping |
| Control Testing Execution | L4 | Compliance & Financial Crime | Compliance Monitoring & Testing | Compliance Control Testing, Assurance Testing |
| Issue & Remediation Tracking | L4 | Compliance & Financial Crime | Compliance Monitoring & Testing | Findings Management, Remediation Tracking |
| Compliance Training Management | L4 | Compliance & Financial Crime | Compliance Policy Management | AML Training, Awareness Management |
| Digital Onboarding | L3 | Channels & Engagement | Digital Banking | Digital Account Opening, Self-Service Onboarding |
| Digital Self-Service | L3 | Channels & Engagement | Digital Banking | Self-Service Banking, Digital Self Service |
| Digital Servicing | L3 | Channels & Engagement | Digital Banking | In-App Servicing, Digital Service Requests |
| Digital Engagement & Personalisation | L3 | Channels & Engagement | Digital Banking | Digital Personalisation, In-Channel Engagement |
| Conversational Banking | L3 | Channels & Engagement | Digital Banking | Chat Banking, Messaging Banking |
| Channel Accessibility | L3 | Channels & Engagement | Digital Banking | Digital Accessibility, Inclusive Design |
| Open Banking Channel | L3 | Channels & Engagement | Digital Banking | Third-Party Channel, Embedded Banking Channel |
| Teller Operations | L3 | Channels & Engagement | Branch Banking | Counter Operations, Cashier Operations |
| Branch Servicing | L3 | Channels & Engagement | Branch Banking | In-Branch Servicing, Assisted Servicing |
| Cash & Vault Management | L3 | Channels & Engagement | Branch Banking | Branch Cash Management, Vault Management |
| Branch Appointment & Queue | L3 | Channels & Engagement | Branch Banking | Appointment Booking, Queue Management |
| Branch Sales | L3 | Channels & Engagement | Branch Banking | In-Branch Sales, Counter Sales |
| Inbound Contact Servicing | L3 | Channels & Engagement | Contact Center | Inbound Servicing, Inbound Voice Servicing |
| Outbound Engagement | L3 | Channels & Engagement | Contact Center | Outbound Calling, Outbound Contact |
| Channel Interaction Routing | L3 | Channels & Engagement | Contact Center | Intent Routing, Channel Routing Capability |
| Self-Service IVR | L3 | Channels & Engagement | Contact Center | Voice Self-Service, IVR Self-Service |
| Contact Complaint Intake | L3 | Channels & Engagement | Contact Center | Complaint Capture, Complaint Logging (Channel) |
| Servicing Resource Management | L3 | Channels & Engagement | Contact Center | Agent Scheduling, Position Management |
| ATM Transaction Processing | L3 | Channels & Engagement | ATM Management | ATM Transactions, Self-Service Terminal Processing |
| ATM Cash Management | L3 | Channels & Engagement | ATM Management | ATM Cash Replenishment, ATM Estate Cash Forecasting |
| ATM Monitoring & Servicing | L3 | Channels & Engagement | ATM Management | ATM Device Monitoring, ATM Maintenance |
| ATM Network Management | L3 | Channels & Engagement | ATM Management | ATM Estate Management, ATM Fleet Management |
| Digital Identity Verification | L4 | Channels & Engagement | Digital Onboarding | Remote ID Verification, eKYC Capture |
| Digital Application Capture | L4 | Channels & Engagement | Digital Onboarding | Online Application Capture, Digital Form Capture |
| Digital Consent Capture | L4 | Channels & Engagement | Digital Onboarding | E-Consent Capture, Terms Acceptance |
| Funds Transfer Self-Service | L4 | Channels & Engagement | Digital Self-Service | Self-Service Transfers, Move Money |
| Card & Account Controls | L4 | Channels & Engagement | Digital Self-Service | Self-Service Controls, Card Management Self-Service |
| Digital Statements & Documents | L4 | Channels & Engagement | Digital Self-Service | E-Statements, Secure Document Inbox |
| Chatbot Servicing | L4 | Channels & Engagement | Conversational Banking | Virtual Assistant Banking, Chatbot Banking |
| Voice Assistant Banking | L4 | Channels & Engagement | Conversational Banking | Voice Banking, Smart Speaker Banking |
| Wearable Banking | L4 | Channels & Engagement | Digital Engagement & Personalisation | Smartwatch Banking, Wearable Channel |
| Channel Experience Management | L4 | Channels & Engagement | Digital Engagement & Personalisation | CX Management, Journey Optimisation |
| Cash Handling | L4 | Channels & Engagement | Teller Operations | Till Operations, Counter Cash Handling |
| Negotiable Instrument Processing | L4 | Channels & Engagement | Teller Operations | Cheque Processing (Branch), Draft Handling |
| Vault Float Control | L4 | Channels & Engagement | Cash & Vault Management | Float Management, Currency Float Control |
| Cash-in-Transit Coordination | L4 | Channels & Engagement | Cash & Vault Management | CIT Coordination, Armoured Carrier Management |
| Interaction Recording & Quality | L4 | Channels & Engagement | Inbound Contact Servicing | Call Recording, Contact Quality Monitoring |
| Agent Desktop Servicing | L4 | Channels & Engagement | Inbound Contact Servicing | Agent Workbench, Servicing Agent Desktop |
| Outbound Dialer Management | L4 | Channels & Engagement | Outbound Engagement | Dialer Operations, Predictive Dialing |
| Self-Service IVR Authentication | L4 | Channels & Engagement | Self-Service IVR | Voice Authentication, IVR Caller Verification |
| ATM Authorization Handling | L4 | Channels & Engagement | ATM Transaction Processing | ATM Auth Handling, Terminal Authorization |
| ATM Deposit Handling | L4 | Channels & Engagement | ATM Transaction Processing | ATM Cash Deposit, Deposit Automation |
| ATM Cash Forecasting | L4 | Channels & Engagement | ATM Cash Management | Cash Demand Forecasting, Replenishment Optimisation |
| ATM Fault Detection | L4 | Channels & Engagement | ATM Monitoring & Servicing | Device Alert Detection, ATM Alarm Handling |

## Business processes

Format: Canonical Name | Domain (defined_in) | Capabilities it depends_on | Aliases

| Canonical Name | Domain | Depends on (capabilities) | Aliases |
|---|---|---|---|
| Customer Onboarding | Customer Management | Customer Acquisition, Identity Verification, KYC Management | Client Onboarding |
| KYC Verification | Compliance & Financial Crime | KYC Management, Identity Verification | KYC Process |
| Deposit Account Opening | Deposits & Accounts | Account Opening | New Account Process |
| Loan Origination Workflow | Lending & Credit | Loan Origination, Credit Decisioning | Loan Application Process |
| Credit Underwriting | Lending & Credit | Credit Decisioning | Underwriting |
| Mortgage Origination | Lending & Credit | Loan Origination, Collateral Management | Mortgage Process |
| Loan Collections | Lending & Credit | Collections & Recovery | Collections Process |
| Payment Processing | Payments | Payment Execution | Payment Run |
| Card Issuance | Cards | Card Issuing | Card Issuance Process |
| Dispute Resolution | Cards | Dispute Management | Chargeback Process |
| Fraud Detection | Risk Management | Fraud Management | Fraud Screening |
| Fraud Investigation | Risk Management | Fraud Management, Case Management | Fraud Case Handling |
| Suspicious Activity Reporting | Compliance & Financial Crime | Transaction Monitoring | SAR Process |
| Regulatory Filing | Compliance & Financial Crime | Regulatory Reporting | Regulatory Submission |
| Statement Generation | Deposits & Accounts | Account Servicing | Statement Production |
| Reconciliation & Settlement | Payments | Payment Clearing & Settlement | Recon & Settlement |
| Complaint Handling | Customer Management | Customer Servicing, Case Management | Complaints Process |
| Service Request Handling | Customer Management | Customer Servicing, Case Management | Service Requests |
| Branch Operations | Channels & Engagement | Branch Banking | Branch Process |
| Trade Finance Processing | Lending & Credit | Collateral Management | Trade Finance |
| Cash Management | Payments | Payment Execution, Liquidity Management | Corporate Cash Management |
| Wealth Onboarding | Wealth & Investments | Portfolio Management, Customer Acquisition | Investor Onboarding |
| Account Maintenance | Deposits & Accounts | Account Servicing | Account Servicing Process, Account Detail Maintenance |
| Account Closure | Deposits & Accounts | Account Servicing | Account Offboarding, Deposit Account Closure |
| Overdraft Servicing | Deposits & Accounts | Overdraft Management, Account Servicing | Overdraft Handling, NSF Processing |
| Card Transaction Authorization | Cards | Card Authorization | Authorization Process, Card Auth |
| Chargeback Processing | Cards | Dispute Management | Chargeback Lifecycle, Dispute Chargeback |
| Card Fraud Handling | Cards | Fraud Management | Card Fraud Management, Card Fraud Operations |
| Financial Planning | Wealth & Investments | Investment Advisory | Wealth Planning, Advice Process |
| Portfolio Rebalancing | Wealth & Investments | Portfolio Management | Rebalancing, Drift Management |
| Trade Order Management | Wealth & Investments | Brokerage & Trading | Trade Order Lifecycle, OMS Workflow |
| Performance Reporting | Wealth & Investments | Portfolio Management | Investment Reporting, Client Reporting |
| Risk Appetite Setting | Risk Management | Enterprise Risk Management | RAF Process, Appetite Setting |
| Risk Identification & Assessment | Risk Management | Operational Risk Management | Risk Assessment, Risk ID & Assessment |
| Stress Testing | Risk Management | Market Risk Management | Capital Stress Testing, CCAR Process, Scenario Analysis |
| Risk Reporting | Risk Management | Enterprise Risk Management | Risk Data Aggregation & Reporting, RDARR, Board Risk Reporting |
| Customer Due Diligence Onboarding | Compliance & Financial Crime | Customer Due Diligence, Sanctions Screening | CDD Onboarding, Diligence Onboarding, AML Onboarding |
| Sanctions Screening Operations | Compliance & Financial Crime | Sanctions Screening | Sanctions Operations, Watchlist Screening Operations, Screening Ops |
| Regulatory Change Management | Compliance & Financial Crime | Regulatory Compliance | Reg Change Management, RCM, Regulatory Change Tracking |
| Digital Onboarding Journey | Channels & Engagement | Digital Banking, Digital Onboarding | Digital Account Opening Journey, Online Onboarding Flow |
| Channel Servicing | Channels & Engagement | Channel Management, Digital Self-Service | Omnichannel Servicing, Self-Service Channel Process |
| ATM Cash Servicing | Channels & Engagement | ATM Management, ATM Cash Management | ATM Cash Cycle, ATM Replenishment Process |
| Contact Centre Interaction | Channels & Engagement | Contact Center, Inbound Contact Servicing | Call Centre Interaction Handling, Contact Handling Process |
| Financial Close | Finance & Treasury | General Ledger Accounting, Financial Reporting | Record to Report, R2R, Month-End Close, Period Close |
| Management Reporting | Finance & Treasury | Financial Reporting | FP&A Process, Performance Management Reporting, Management Accounting, Board Reporting |
| Regulatory Capital Reporting | Finance & Treasury | Regulatory Capital Management | Prudential Reporting, COREP Reporting, CCAR Reporting |
| Cash & Liquidity Management | Finance & Treasury | Liquidity Management | Liquidity Operations, Treasury Cash Operations |
| Funds Transfer Pricing | Finance & Treasury | Asset Liability Management | FTP, Liquidity Transfer Pricing, Internal Funds Pricing, Transfer Pricing (Treasury) |

## Technology capabilities

Format: Canonical Name | Tech Domain (defined_in) | Business capabilities that depend_on it | Aliases

| Canonical Name | Domain | Enables (business caps depend_on) | Aliases |
|---|---|---|---|
| Core Banking Processing | Core Processing | Deposits, Account Servicing, Loan Servicing | Core Banking System, Core Ledger |
| Payment Orchestration | Core Processing | Payment Execution, Payment Initiation | Payment Hub |
| Card Processing | Core Processing | Card Issuing, Card Authorization | Card Management System |
| Loan Origination Platform | Core Processing | Loan Origination | LOS |
| General Ledger Engine | Core Processing | General Ledger Accounting, Financial Reporting | GL System |
| Credit Decisioning Engine | Core Processing | Credit Decisioning, Credit Risk Management | Decision Engine |
| Data Warehousing | Data & Analytics | Financial Reporting, Enterprise Risk Management | Data Warehouse, Lakehouse |
| Data Streaming | Data & Analytics | Real-Time Payments, Fraud Management | Event Streaming |
| Analytics Platform | Data & Analytics | Customer Segmentation, Market Risk Management | BI Platform, Analytics & BI |
| Data Governance | Data & Analytics | Regulatory Compliance | Data Catalog, Data Governance & Catalog |
| Master Data Management | Data & Analytics | Party Data Management | MDM |
| Document Management | Data & Analytics | KYC Management, Loan Origination | ECM, Content Services |
| Regulatory Reporting Engine | Data & Analytics | Regulatory Reporting, Regulatory Capital Management | RegTech Reporting |
| API Management | Integration & APIs | Digital Banking, Payment Initiation | API Gateway |
| Integration Platform | Integration & APIs | Channel Management | ESB, iPaaS |
| Workflow Orchestration | Integration & APIs | Customer Servicing, Loan Origination | BPM, Process Orchestration |
| Notification Services | Integration & APIs | Account Servicing, Customer Servicing | Messaging, Notifications |
| Identity Access Management | Security & Identity | Channel Management | IAM |
| Customer Identity | Security & Identity | Digital Banking, Online Banking | CIAM |
| Threat Detection | Security & Identity | Operational Risk Management | SIEM, Cybersecurity |
| Machine Learning Platform | AI & Automation | Credit Decisioning, Fraud Management | MLOps, ML Platform |
| Fraud Analytics | AI & Automation | Fraud Management | Fraud Detection Platform |
| Transaction Monitoring Platform | AI & Automation | Transaction Monitoring, AML Monitoring | AML Platform |
| Conversational AI | AI & Automation | Contact Center, Customer Servicing | Chatbot, Virtual Assistant |
| Intelligent Document Processing | AI & Automation | KYC Management, Loan Origination | IDP |
| Robotic Process Automation | AI & Automation | Account Servicing, Operational Risk Management | RPA |
| Generative AI Platform | AI & Automation | Customer Servicing, Investment Advisory | GenAI, LLM Platform |
| Digital Channel Platform | Channels & Engagement | Digital Banking, Mobile Banking | Digital Banking Platform |
| Contact Center Platform | Channels & Engagement | Contact Center | CCaaS |
| CRM Platform | Channels & Engagement | Relationship Management, Campaign Management | Customer Relationship Management |
| Portfolio Management System | Core Processing | Portfolio Management | PMS, Investment Book of Record, IBOR, Portfolio & Investment Management Platform |
| Order Management System | Core Processing | Brokerage & Trading | OMS, Order & Execution Management Platform |
| Investment Advisory Platform | Core Processing | Investment Advisory | Digital Advice Platform, Financial Planning Platform, Wealth Advisory Suite |
| Risk Analytics Engine | AI & Automation | Enterprise Risk Management, Credit Risk Management, Market Risk Management, Liquidity Risk Management | Risk Engine, Risk Computation Platform, Quant Risk Engine |
| Risk Data Aggregation | Data & Analytics | Enterprise Risk Management, Credit Risk Management, Market Risk Management, Liquidity Risk Management | Risk Data Platform, BCBS 239 Platform, Risk Data Aggregation and Reporting |
| Model Risk Management Platform | AI & Automation | Enterprise Risk Management, Credit Risk Management, Market Risk Management | MRM Platform, Model Governance Platform, Model Inventory & Validation Platform |
| Governance Risk & Compliance Platform | Data & Analytics | Operational Risk Management, Enterprise Risk Management, Regulatory Compliance | GRC Platform, Integrated Risk Management Platform, IRM Platform |
| KYC Onboarding Platform | AI & Automation | KYC Management, Customer Due Diligence, Customer Acquisition | Client Lifecycle Management Platform, KYC Platform, CLM Platform, Perpetual KYC Platform |
| Treasury Management System | Core Processing | Treasury Management, Liquidity Management | TMS, Treasury & Risk Management Platform, Treasury Workstation |
| Asset Liability Management Engine | Core Processing | Asset Liability Management, Liquidity Management, Regulatory Capital Management | ALM Engine, Balance Sheet Management Platform, IRRBB Engine, ALM/FTP Platform |
| Financial Consolidation Platform | Core Processing | Financial Reporting, General Ledger Accounting, Regulatory Capital Management | CPM Platform, EPM Platform, Consolidation & Close Platform, Corporate Performance Management |

## Legacy systems

Format: Canonical Name | Realizes (tech capability depends_on it) | Vendor | Aliases

| Canonical Name | Realizes (tech cap) | Vendor | Aliases |
|---|---|---|---|
| FIS Profile | Core Banking Processing | FIS | Profile |
| Fiserv DNA | Core Banking Processing | Fiserv | DNA |
| Jack Henry SilverLake | Core Banking Processing | Jack Henry | SilverLake System |
| Temenos T24 | Core Banking Processing | Temenos | T24, Globus |
| Oracle FLEXCUBE | Core Banking Processing | Oracle | FLEXCUBE |
| Infosys Finacle | Core Banking Processing | Infosys | Finacle |
| TCS BaNCS | Core Banking Processing | TCS | BaNCS |
| Legacy Mainframe Core | Core Banking Processing | (generic) | COBOL Core, Mainframe Core |
| ACI BASE24 | Payment Orchestration | ACI Worldwide | BASE24, BASE24-eps |
| Legacy Payment Hub | Payment Orchestration | (generic) | On-Prem Payment Hub |
| ACH Batch Processor | Payment Orchestration | (generic) | Batch ACH System |
| TSYS TS2 | Card Processing | Global Payments (TSYS) | TS2, TSYS |
| First Data Cards | Card Processing | Fiserv (First Data) | First Data, VisionPLUS |
| Teradata | Data Warehousing | Teradata | Teradata EDW |
| Oracle Exadata | Data Warehousing | Oracle | Exadata |
| IBM Db2 | Data Warehousing | IBM | Db2, DB2 |
| IBM Cognos | Analytics Platform | IBM | Cognos |
| SAS Platform | Analytics Platform | SAS | SAS 9, Base SAS |
| IBM MQ | Data Streaming | IBM | WebSphere MQ, MQSeries |
| TIBCO BusinessWorks | Integration Platform | TIBCO | BusinessWorks, TIBCO EMS |
| webMethods | Integration Platform | Software AG | Software AG webMethods |
| Oracle SOA Suite | Integration Platform | Oracle | SOA Suite |
| CA API Gateway | API Management | Broadcom | Layer7, CA Layer7 |
| CA SiteMinder | Identity Access Management | Broadcom | SiteMinder |
| Oracle Identity Manager | Identity Access Management | Oracle | OIM |
| IBM Tivoli Identity Manager | Customer Identity | IBM | Tivoli Identity Manager, ISIM |
| Siebel CRM | CRM Platform | Oracle | Siebel |
| IBM FileNet | Document Management | IBM | FileNet |
| OpenText Documentum | Document Management | OpenText | Documentum |
| Pega BPM | Workflow Orchestration | Pegasystems | Pega, PegaRULES |
| FICO Falcon | Fraud Analytics | FICO | Falcon, Falcon Fraud Manager |
| SAS Fraud Management | Fraud Analytics | SAS | SAS Fraud |
| Oracle Mantas | Transaction Monitoring Platform | Oracle | Mantas, Oracle FCCM |
| NICE Actimize | Transaction Monitoring Platform | NICE | Actimize |
| AxiomSL | Regulatory Reporting Engine | Adenza | ControllerView |
| Wolters Kluwer OneSumX | Regulatory Reporting Engine | Wolters Kluwer | OneSumX |
| SAP ECC | General Ledger Engine | SAP | SAP ERP, SAP R/3 |
| Black Knight Empower | Loan Origination Platform | Black Knight | Empower LOS |
| Legacy Credit Scoring | Credit Decisioning Engine | (generic) | Legacy Scorecard Engine |
| Avaya Aura | Contact Center Platform | Avaya | Aura |
| Cisco UCCE | Contact Center Platform | Cisco | Unified Contact Center Enterprise |
| Legacy Online Banking | Digital Channel Platform | (generic) | Legacy Internet Banking |
| Legacy IVR System | Conversational AI | (generic) | IVR |
| FIS Open Payment Framework | Payment Orchestration | FIS | OPF, FIS OPF |
| Finastra Global PAYplus | Payment Orchestration | Finastra | GPP, Global PAYplus |
| ACI Enterprise Payments Platform | Payment Orchestration | ACI Worldwide | ACI EPP, UP Real-Time Payments |
| SAP CRM | CRM Platform | SAP | SAP CRM 7.0, mySAP CRM |
| Informatica MDM | Master Data Management | Informatica | Informatica MDM Hub, Siperian |
| Ellie Mae Encompass | Loan Origination Platform | ICE Mortgage Technology | Encompass, ICE Encompass, Ellie Mae |
| Finastra LaserPro | Loan Origination Platform | Finastra | LaserPro |
| FICO Origination Manager | Credit Decisioning Engine | FICO | Origination Manager |
| Experian PowerCurve | Credit Decisioning Engine | Experian | PowerCurve, PowerCurve Strategy Management, PowerCurve Originations |
| Fiserv Premier | Core Banking Processing | Fiserv | Premier, Premier Core |
| Jack Henry Core Director | Core Banking Processing | Jack Henry | Core Director, Jack Henry Core Director System |
| FIS Horizon | Core Banking Processing | FIS | Horizon, FIS Horizon Core |
| FIS Card Management | Card Processing | FIS | FIS CMS, FIS Payments One, FIS Card Processing |
| Fiserv OmniPay | Card Processing | Fiserv | OmniPay, Fiserv OmniPay Platform |
| Fiserv Optis | Card Processing | Fiserv | Optis, Fiserv Optis Platform |
| FIS Global Plus | Portfolio Management System | FIS | Global Plus, Unity Powered by Global Plus |
| SunGard Asset Arena | Portfolio Management System | FIS (SunGard) | Asset Arena, FIS Asset Arena |
| SS&C Advent Geneva | Portfolio Management System | SS&C Advent | Geneva, Advent Geneva, APX |
| SS&C Advent Moxy | Order Management System | SS&C Advent | Moxy, Advent Moxy |
| Broadridge Portfolio Master | Portfolio Management System | Broadridge (representative) | Broadridge Recordkeeping, Broadridge IBOR, Portfolio Master |
| Temenos WealthSuite | Investment Advisory Platform | Temenos | WealthSuite, Temenos Wealth, Temenos Robo-Advisor |
| SAS Risk Management for Banking | Risk Analytics Engine | SAS | SAS Risk, SAS RMfB |
| Oracle OFSAA | Risk Analytics Engine | Oracle | OFSAA, Oracle Financial Services Analytical Applications |
| Moody's RiskFrontier | Risk Analytics Engine | Moody's Analytics | RiskFrontier |
| IBM Algorithmics | Risk Analytics Engine | IBM | Algorithmics, Algo Risk, Algo One |
| FIS Adaptiv | Risk Analytics Engine | FIS | Adaptiv, FIS Enterprise Risk Suite |
| Moody's RiskAuthority | Risk Data Aggregation | Moody's Analytics | RiskAuthority, Fermat |
| IBM OpenPages | Governance Risk & Compliance Platform | IBM | OpenPages, OpenPages with Watson |
| Archer IRM | Governance Risk & Compliance Platform | Archer | RSA Archer, Archer GRC |
| SAS Anti-Money Laundering | Transaction Monitoring Platform | SAS | SAS AML, SAS Anti Money Laundering |
| LexisNexis Bridger Insight | Transaction Monitoring Platform | LexisNexis Risk Solutions (Fircosoft) | Bridger Insight XG, Fircosoft, Firco, Firco Continuity |
| Kony DBX | Digital Channel Platform | Temenos (Kony) | Kony Digital Banking, DBX |
| Verint WFM | Contact Center Platform | Verint | Verint Workforce Management, Verint WFO, Verint Impact 360 |
| Oracle E-Business Suite | General Ledger Engine | Oracle | Oracle EBS, Oracle Financials, E-Business Suite |
| Oracle Hyperion HFM | Financial Consolidation Platform | Oracle | HFM, Hyperion Financial Management, Hyperion |
| SAP BPC | Financial Consolidation Platform | SAP | Business Planning and Consolidation, SEM-BCS |
| SunGard AvantGard | Treasury Management System | FIS (SunGard) | AvantGard, AvantGard Integrity, AvantGard Quantum |
| SAP Treasury And Risk Management | Treasury Management System | SAP | SAP TRM, SAP Treasury, FSCM Treasury |
| QRM Balance Sheet Management | Asset Liability Management Engine | Quantitative Risk Management | QRM, Quantitative Risk Management, QRM ALM |
| SAS Asset And Liability Management | Asset Liability Management Engine | SAS | SAS ALM, SAS Risk Management for Banking ALM |
| Avaloq Banking Suite | Core Banking Processing | Avaloq (NEC) | Avaloq, Avaloq Core, Avaloq Wealth |
| Sopra Amplitude | Core Banking Processing | Sopra Banking Software (Sopra Steria) | Amplitude, Sopra Banking Amplitude, Amplitude Up, SBP Core Amplitude |
| Infor SunSystems | General Ledger Engine | Infor | SunSystems, Infor SunSystems Financials, Infor FSM |
| Fidessa | Order Management System | ION Group | Fidessa OMS, Fidessa Trading Platform, ION Fidessa |
| Linedata Longview | Order Management System | Linedata | Longview, Linedata Longview OMS, Longview Trading |
| Nasdaq Calypso | Order Management System | Nasdaq (formerly Calypso/Adenza) | Calypso, Adenza Calypso, Calypso Technology |
| Objectway | Investment Advisory Platform | Objectway | Objectway Platform, Objectway Digital Wealth |
| SAP BusinessObjects | Analytics Platform | SAP | BOBJ, BusinessObjects BI, Web Intelligence, Crystal Reports |
| Informatica Axon | Data Governance | Informatica | Axon Data Governance, Informatica Axon Data Governance |
| Informatica PowerCenter | Data Warehousing | Informatica | PowerCenter, Informatica ETL |

## Modern systems

Format: Canonical Name | Realizes (tech cap depends_on it) | Supersedes (legacy) | Vendor | Aliases

| Canonical Name | Realizes (tech cap) | Supersedes | Vendor | Aliases |
|---|---|---|---|---|
| Thought Machine Vault | Core Banking Processing | Temenos T24; Oracle FLEXCUBE; Avaloq Banking Suite | Thought Machine | Vault, Vault Core |
| Mambu | Core Banking Processing | Fiserv DNA; Jack Henry SilverLake; Sopra Amplitude | Mambu | Mambu Core |
| 10x Banking | Core Banking Processing | Legacy Mainframe Core; TCS BaNCS | 10x Banking | 10x, SuperCore |
| Finxact | Core Banking Processing | FIS Profile; Infosys Finacle | Fiserv | Finxact Core |
| Temenos Transact | Core Banking Processing | Temenos T24 | Temenos | Transact |
| Stripe | Payment Orchestration | ACH Batch Processor | Stripe | Stripe Payments |
| Adyen | Payment Orchestration | Legacy Payment Hub | Adyen | — |
| Modern Treasury | Payment Orchestration | ACH Batch Processor | Modern Treasury | — |
| Volante Payments | Payment Orchestration | ACI BASE24 | Volante Technologies | Volante, VolPay |
| Marqeta | Card Processing | TSYS TS2 | Marqeta | — |
| Galileo | Card Processing | First Data Cards | Galileo Financial Technologies | Galileo FT |
| Snowflake | Data Warehousing | Teradata | Snowflake | Snowflake Data Cloud |
| Databricks | Data Warehousing | Oracle Exadata | Databricks | Databricks Lakehouse |
| Google BigQuery | Data Warehousing | IBM Db2 | Google Cloud | BigQuery |
| Confluent Platform | Data Streaming | IBM MQ | Confluent | Confluent, Kafka |
| MuleSoft | Integration Platform | Oracle SOA Suite; TIBCO BusinessWorks | Salesforce | Anypoint Platform |
| Boomi | Integration Platform | webMethods | Boomi | Dell Boomi |
| Kong | API Management | CA API Gateway | Kong Inc | Kong Gateway |
| Apigee | API Management | CA API Gateway | Google Cloud | Apigee Edge |
| Okta | Identity Access Management | CA SiteMinder | Okta | Okta Identity Cloud |
| ForgeRock | Identity Access Management | Oracle Identity Manager | Ping Identity | ForgeRock Platform |
| Ping Identity | Customer Identity | IBM Tivoli Identity Manager | Ping Identity | PingOne |
| Auth0 | Customer Identity | IBM Tivoli Identity Manager | Okta | Auth0 by Okta |
| Salesforce Financial Services Cloud | CRM Platform | Siebel CRM | Salesforce | FSC, Salesforce FSC |
| Hyperscience | Intelligent Document Processing | IBM FileNet | Hyperscience | — |
| AWS Textract | Intelligent Document Processing | OpenText Documentum | Amazon Web Services | Textract |
| Camunda | Workflow Orchestration | Pega BPM | Camunda | Camunda Platform |
| Temporal | Workflow Orchestration | Pega BPM | Temporal Technologies | Temporal.io |
| Feedzai | Fraud Analytics | FICO Falcon | Feedzai | — |
| Featurespace | Fraud Analytics | SAS Fraud Management | Visa (Featurespace) | ARIC |
| Hawk AI | Transaction Monitoring Platform | Oracle Mantas | Hawk | Hawk:AI |
| ComplyAdvantage | Transaction Monitoring Platform | NICE Actimize | ComplyAdvantage | — |
| Regnology | Regulatory Reporting Engine | AxiomSL | Regnology | Regnology Reporting |
| Suade | Regulatory Reporting Engine | Wolters Kluwer OneSumX | Suade Labs | Suade Platform |
| Workday Financials | General Ledger Engine | SAP ECC | Workday | Workday Financial Management |
| Oracle Fusion ERP | General Ledger Engine | SAP ECC | Oracle | Fusion Cloud ERP |
| Zest AI | Credit Decisioning Engine | Legacy Credit Scoring | Zest AI | ZAML |
| Upstart | Credit Decisioning Engine | Legacy Credit Scoring | Upstart | — |
| Blend | Loan Origination Platform | Black Knight Empower | Blend Labs | Blend Platform |
| nCino | Loan Origination Platform | Black Knight Empower | nCino | nCino Cloud Banking |
| Amazon Connect | Contact Center Platform | Avaya Aura | Amazon Web Services | Connect |
| Genesys Cloud | Contact Center Platform | Cisco UCCE | Genesys | Genesys Cloud CX |
| Backbase | Digital Channel Platform | Legacy Online Banking | Backbase | Engagement Banking |
| Q2 | Digital Channel Platform | Legacy Online Banking | Q2 Holdings | Q2 Digital |
| Amazon SageMaker | Machine Learning Platform | SAS Platform | Amazon Web Services | SageMaker |
| Google Vertex AI | Machine Learning Platform | SAS Platform | Google Cloud | Vertex AI |
| DataRobot | Machine Learning Platform | SAS Platform | DataRobot | — |
| Microsoft Power BI | Analytics Platform | IBM Cognos | Microsoft | Power BI |
| Kasisto | Conversational AI | Legacy IVR System | Kasisto | KAI |
| Anthropic Claude | Generative AI Platform | Legacy IVR System | Anthropic | Claude |
| Form3 | Payment Orchestration | Legacy Payment Hub; Finastra Global PAYplus | Form3 | Form3 Financial Cloud, Form3 PaaS |
| ACI Connetic | Payment Orchestration | ACI BASE24; ACI Enterprise Payments Platform | ACI Worldwide | Connetic |
| Bottomline Payments | Payment Orchestration | ACH Batch Processor; FIS Open Payment Framework | Bottomline Technologies | Bottomline, PTX |
| Microsoft Dynamics 365 | CRM Platform | SAP CRM | Microsoft | Dynamics 365 Customer Service, D365 |
| Pega Customer Service | CRM Platform | Siebel CRM | Pegasystems | Pega CRM, Pega CS |
| Reltio | Master Data Management | Informatica MDM | Reltio | Reltio Data Cloud, Reltio MDM |
| Amazon Lex | Conversational AI | Legacy IVR System | Amazon Web Services | AWS Lex, Lex V2 |
| Temenos Origination | Loan Origination Platform | Ellie Mae Encompass; Finastra LaserPro | Temenos | Temenos Infinity Origination, Infinity Origination |
| MeridianLink | Loan Origination Platform | Finastra LaserPro | MeridianLink | MeridianLink Consumer, MeridianLink Opening |
| Provenir | Credit Decisioning Engine | FICO Origination Manager; Experian PowerCurve | Provenir | Provenir AI, Provenir Decisioning |
| SAP Deposits Management | Core Banking Processing | Legacy Mainframe Core; FIS Horizon | SAP / SAP Fioneer | SAP Deposits Management for Banking, SAP Transactional Banking, SAP Fioneer Core |
| Tuum | Core Banking Processing | Fiserv Premier | Tuum | Tuum Core, Modularbank |
| SaaScada | Core Banking Processing | Jack Henry Core Director | SaaScada | SaaScada Core, SaaScada Cloud Core |
| Thredd | Card Processing | First Data Cards | Thredd | GPS, Global Processing Services, GPS Apex |
| Lithic | Card Processing | First Data Cards | Lithic | Lithic Issuer Processing, Privacy.com |
| i2c | Card Processing | TSYS TS2; Fiserv Optis | i2c Inc | i2c Issuer Processing |
| Pismo | Card Processing | TSYS TS2; FIS Card Management | Visa (Pismo) | Pismo Platform, Visa Global Issuer Processing |
| Episode Six | Card Processing | First Data Cards | Episode Six | Episode Six TRITIUM, E6 |
| BlackRock Aladdin | Portfolio Management System | SS&C Advent Geneva; SunGard Asset Arena | BlackRock | Aladdin, Aladdin Wealth |
| SimCorp One | Portfolio Management System | FIS Global Plus; SunGard Asset Arena | SimCorp | SimCorp Dimension, SimCorp |
| Addepar | Portfolio Management System | Broadridge Portfolio Master | Addepar | Addepar Platform |
| Charles River IMS | Order Management System | SS&C Advent Moxy | State Street (Charles River Development) | Charles River, CRD IMS, Charles River Development |
| Bloomberg AIM | Order Management System | SS&C Advent Moxy | Bloomberg | AIM, Bloomberg Asset and Investment Manager |
| InvestCloud | Investment Advisory Platform | Temenos WealthSuite | InvestCloud | InvestCloud X, NaviPlan |
| Envestnet | Investment Advisory Platform | Temenos WealthSuite | Envestnet | Envestnet Platform, Envestnet Wealth Management |
| Murex MX.3 Risk | Risk Analytics Engine | FIS Adaptiv; Oracle OFSAA | Murex | MX.3 Enterprise Risk, Murex Enterprise Risk |
| MSCI RiskMetrics | Risk Analytics Engine | IBM Algorithmics; SAS Risk Management for Banking | MSCI | RiskMetrics RiskManager, RiskManager |
| Numerix Oneview | Risk Analytics Engine | Moody's RiskFrontier | Numerix | Oneview, Numerix Oneview for Market Risk |
| ServiceNow IRM | Governance Risk & Compliance Platform | Archer IRM | ServiceNow | ServiceNow GRC, ServiceNow Integrated Risk Management |
| MetricStream | Governance Risk & Compliance Platform | IBM OpenPages | MetricStream | MetricStream Enterprise GRC, Connected GRC |
| Quantexa | Risk Data Aggregation | Moody's RiskAuthority | Quantexa | Quantexa DI Platform, Contextual Decision Intelligence |
| ValidMind | Model Risk Management Platform |  | ValidMind | ValidMind MRM, ValidMind AI Governance |
| ModelOp | Model Risk Management Platform |  | ModelOp | ModelOp Center |
| Napier AI | Transaction Monitoring Platform | SAS Anti-Money Laundering; LexisNexis Bridger Insight | Napier AI | Napier, Napier Continuum, Continuum, NapierAI |
| Fenergo | KYC Onboarding Platform |  | Fenergo | Fenergo CLM, Fenergo KYC, Fenergo Client Lifecycle Management |
| Temenos Infinity | Digital Channel Platform | Legacy Online Banking; Kony DBX | Temenos | Infinity, Temenos Digital, Infinity Engage |
| Alkami | Digital Channel Platform | Legacy Online Banking | Alkami Technology | Alkami Platform, Alkami Digital Banking, ORB |
| NICE CXone | Contact Center Platform | Avaya Aura | NICE | CXone, NICE CXone Mpower, inContact |
| Five9 | Contact Center Platform | Cisco UCCE | Five9 | Five9 Intelligent CX Platform |
| Twilio Flex | Contact Center Platform | Avaya Aura | Twilio | Flex, Twilio Flex CCaaS |
| Glia | Contact Center Platform | Cisco UCCE | Glia | Glia Interaction Platform, Digital Customer Service, DCS |
| Verint WFM Cloud | Contact Center Platform | Verint WFM | Verint | Verint Workforce Management Cloud, Verint WEM, Verint Open Platform WFM |
| SAP S/4HANA Finance | General Ledger Engine | SAP ECC; Oracle E-Business Suite | SAP | S/4HANA Finance, Simple Finance, S/4HANA Central Finance |
| OneStream | Financial Consolidation Platform | Oracle Hyperion HFM; SAP BPC | OneStream Software | OneStream Software, OneStream Platform, OneStream XF |
| Oracle EPM Cloud | Financial Consolidation Platform | Oracle Hyperion HFM | Oracle | Oracle EPM, Oracle Fusion EPM, FCCS, EPM Cloud |
| Anaplan | Financial Consolidation Platform | SAP BPC | Anaplan | Anaplan Platform, Connected Planning |
| Kyriba | Treasury Management System | SunGard AvantGard | Kyriba | Kyriba Liquidity Performance, Kyriba TMS |
| ION Treasury | Treasury Management System | SAP Treasury And Risk Management | ION Group | ION Wallstreet Suite, Reval, IT2, Wallstreet Suite |
| GTreasury | Treasury Management System | SunGard AvantGard | GTreasury | GTreasury Platform, GTreasury TRMS |
| Empyrean Sol ALM | Asset Liability Management Engine | QRM Balance Sheet Management; SAS Asset And Liability Management | Empyrean Solutions | Sol ALM, Empyrean ALM, Empyrean Solutions |
| Moody's Balance Sheet Management | Asset Liability Management Engine | QRM Balance Sheet Management | Moody's Analytics | Moody's ALM, RiskConfidence |
| FIS Modern Banking Platform | Core Banking Processing | FIS Profile; FIS Horizon | FIS | MBP, FIS MBP, Modern Banking Platform |
| Sage Intacct | General Ledger Engine | Infor SunSystems | Sage | Intacct, Sage Business Cloud Intacct |
| FlexONE | Order Management System | Linedata Longview | FlexTrade Systems | FlexTrade FlexONE, FlexONE OEMS, FlexOMS |
| Orion | Investment Advisory Platform | Objectway | Orion Advisor Solutions | Orion Advisor Tech, Orion Advisor Solutions, Orion Wealth |
| Coupa Treasury | Treasury Management System | SunGard AvantGard | Coupa (formerly BELLIN) | Bellin, BELLIN tm5, Coupa Treasury Management |
| Tableau | Analytics Platform | SAP BusinessObjects | Salesforce | Tableau Desktop, Tableau Cloud, Tableau Server |
| Qlik | Analytics Platform | SAP BusinessObjects | Qlik | Qlik Sense, QlikView, Qlik Cloud |
| ThoughtSpot | Analytics Platform | SAP BusinessObjects | ThoughtSpot | ThoughtSpot Analytics, ThoughtSpot Sage |
| Collibra | Data Governance | Informatica Axon | Collibra | Collibra Data Intelligence Platform, Collibra Data Catalog, Collibra Data Governance |
| Alation | Data Governance | Informatica Axon | Alation | Alation Data Catalog, Alation Data Governance |
| dbt | Data Warehousing | Informatica PowerCenter | dbt Labs | dbt Core, dbt Cloud, data build tool |
| Fivetran | Data Warehousing | Informatica PowerCenter | Fivetran | Fivetran ELT, Fivetran connectors |
| Apache Kafka | Data Streaming |  | Apache Software Foundation | Apache Kafka Streaming |
| Apache Flink | Data Streaming |  | Apache Software Foundation | Flink, Managed Service for Apache Flink |
| Microsoft SharePoint | Document Management | IBM FileNet | Microsoft | SharePoint Online, SharePoint Server, M365 SharePoint |
| OpenText Content Suite | Document Management | OpenText Documentum | OpenText | OpenText Content Management, OpenText Extended ECM, Content Suite Platform |

## Glossary terms

| Canonical Name | Aliases |
|---|---|
| BIAN | Banking Industry Architecture Network |
| APQC PCF | Process Classification Framework |
| Value Stream | Value Streams |
| Business Capability | Capability |
| Technology Capability | Tech Capability |
| Core Banking | Core Banking System |
| ISO 20022 | ISO20022 |
| Open Banking | Open Banking APIs |
| Cloud-Native | Cloud Native |
| Zettelkasten | Atomic Notes |

## Technology sub-capabilities

| Canonical Name | Parent | Domain | Level | Aliases |
|---|---|---|---|---|
| Payment Routing Engine | Payment Orchestration | Core Processing | L2 | Smart Routing, Least-Cost Routing |
| Scheme Connectivity Gateway | Payment Orchestration | Core Processing | L2 | Rail Connectivity, Network Adapters, Scheme Connectivity |
| Payment Message Transformer | Payment Orchestration | Core Processing | L2 | Message Transformation, ISO 20022 Translation, Payment Message Transformation |
| Payment Validation Engine | Payment Orchestration | Core Processing | L2 | Validation Engine, STP Validation |
| Payment Repair Workbench | Payment Orchestration | Core Processing | L2 | Auto-Repair, Exceptions and Investigations, STP Repair |
| Settlement Instruction Engine | Payment Orchestration | Core Processing | L2 | Settlement Engine, Settlement Instruction |
| Liquidity & Limit Checker | Payment Orchestration | Core Processing | L2 | Limit Check, Funds Control, Liquidity Check |
| Payment Sanctions Filter | Payment Orchestration | Core Processing | L2 | Inline Sanctions Filter, In-Flight Screening |
| ISO 20022 Translation Service | Payment Message Transformer | Core Processing | L3 | MX Translation, MT-MX Mapping |
| Least-Cost Routing Service | Payment Routing Engine | Core Processing | L3 | Cost-Based Routing |
| SWIFT Connectivity Adapter | Scheme Connectivity Gateway | Core Processing | L3 | SWIFT Adapter, SWIFT gpi Connector |
| Contact & Account Management | CRM Platform | Channels & Engagement | L2 | Account & Contact Management, Party Record Management |
| Case Management Workbench | CRM Platform | Channels & Engagement | L2 | Service Case Workbench, Service Console |
| Campaign Automation | CRM Platform | Channels & Engagement | L2 | Marketing Automation, Journey Orchestration |
| Customer 360 View | CRM Platform | Channels & Engagement | L2 | Single Customer View, C360 |
| Party Matching & Merge | Master Data Management | Data & Analytics | L2 | Entity Resolution, Match & Merge |
| Golden Record Management | Master Data Management | Data & Analytics | L2 | Survivorship Engine, Best Record Management |
| Data Stewardship Workflow | Master Data Management | Data & Analytics | L2 | Stewardship Console, Bulk Match Review |
| Customer Authentication | Customer Identity | Security & Identity | L2 | Adaptive Authentication, MFA Service |
| Consent Management Service | Customer Identity | Security & Identity | L2 | Privacy Management, Consent Service |
| Identity Proofing Service | Customer Identity | Security & Identity | L2 | Identity Verification Service, ID Proofing |
| Self-Service Virtual Assistant | Conversational AI | AI & Automation | L2 | Digital Assistant, Customer Chatbot |
| Agent Assist | Conversational AI | AI & Automation | L2 | Agent Copilot, Next Best Action Assist |
| Probabilistic Match Engine | Party Matching & Merge | Data & Analytics | L3 | Fuzzy Match Engine, AI Matching |
| Survivorship Rule Engine | Golden Record Management | Data & Analytics | L3 | Survivorship Rules, Field Survivorship |
| Passwordless Authentication | Customer Authentication | Security & Identity | L3 | Passkey Service, FIDO2 Service |
| Identity Orchestration Engine | Identity Proofing Service | Security & Identity | L3 | Identity Orchestration, Proofing Orchestration |
| Application Intake Engine | Loan Origination Platform | Core Processing | L2 | Application Capture Engine, Origination Intake Service |
| Document Capture & Verification | Loan Origination Platform | Core Processing | L2 | Document Capture Service, Doc Verification Engine |
| Loan Product Configurator | Loan Origination Platform | Core Processing | L2 | Product Configurator, Lending Product Designer |
| Offer & Pricing Engine | Loan Origination Platform | Core Processing | L2 | Loan Pricing Engine, Offer Generation Service |
| Disbursement Engine | Loan Origination Platform | Core Processing | L2 | Loan Booking & Funding, Funding Engine |
| Credit Scoring Service | Credit Decisioning Engine | Core Processing | L2 | Scorecard Service, Credit Score Engine |
| Affordability Assessment Engine | Credit Decisioning Engine | Core Processing | L2 | Affordability Engine, Repayment Capacity Service |
| Decision Rules Engine | Credit Decisioning Engine | Core Processing | L2 | Underwriting Rules Engine, Policy Rules Engine |
| Bureau Data Integration | Credit Decisioning Engine | Core Processing | L2 | Bureau Connectivity Service, Credit Data Aggregation |
| Adverse Action Generator | Credit Decisioning Engine | Core Processing | L2 | Adverse Action Service, Reason Code Generator |
| Income Verification Service | Affordability Assessment Engine | Core Processing | L3 | Income & Employment Verification, Payroll Verification Service |
| Reject Inference Model | Credit Scoring Service | Core Processing | L3 | Reject Inference Engine, Inference Scorecard |
| Strategy Design Studio | Decision Rules Engine | Core Processing | L3 | Strategy Authoring Studio, Champion-Challenger Workbench |
| Deposit Account Management | Core Banking Processing | Core Processing | L2 | Account Master Service, Deposit Account Service, Account System of Record |
| Transaction Posting Engine | Core Banking Processing | Core Processing | L2 | Posting Engine, Core Ledger Posting, Postings Service |
| Product & Pricing Engine | Core Banking Processing | Core Processing | L2 | Deposit Product Engine, Product Configurator (Deposits), Universal Product Engine |
| Interest & Charges Engine | Core Banking Processing | Core Processing | L2 | Accrual Engine, Interest & Fee Engine, Charges Engine |
| Account Statement Generator | Core Banking Processing | Core Processing | L2 | Statement Engine, Statement Production Service, Statement Generator |
| Standing Order & Sweep Engine | Core Banking Processing | Core Processing | L2 | Sweep Engine, Scheduled Transfer Engine, Cash Concentration Engine |
| General Ledger Posting | Core Banking Processing | Core Processing | L2 | Sub-Ledger to GL Posting, GL Interface Service, Core GL Bridge |
| Account Lifecycle Manager | Core Banking Processing | Core Processing | L2 | Account State Engine, Deposit Lifecycle Engine, Account Status Manager |
| Real-Time Posting Service | Transaction Posting Engine | Core Processing | L3 | Real-Time Ledger Service, Instant Posting Service, Streaming Postings |
| Tiered Interest Calculator | Interest & Charges Engine | Core Processing | L3 | Tiered Rate Calculator, Banded Interest Service, Bonus Rate Engine |
| Dormancy & Escheatment Service | Account Lifecycle Manager | Core Processing | L3 | Dormancy Engine, Unclaimed Property Service, Escheatment Service |
| Card Authorization Engine | Card Processing | Core Processing | L2 | Authorization Decisioning Engine, Issuer Auth Engine, Dynamic Authorization |
| Card Transaction Switch | Card Processing | Core Processing | L2 | Issuer Switch, ISO 8583 Switch, Scheme Message Switch |
| Card Issuing & Personalisation | Card Processing | Core Processing | L2 | Card Issuance Engine, Personalisation Service, Card Provisioning |
| Card Tokenization Service | Card Processing | Core Processing | L2 | Token Vault Service, Network Tokenization, Digital Card Tokenisation |
| Card Account Ledger | Card Processing | Core Processing | L2 | Cardholder Ledger, Card Billing Engine, Card Statement Ledger |
| Clearing & Settlement Processor | Card Processing | Core Processing | L2 | Card Clearing Engine, Interchange & Settlement Processor, Presentment Processor |
| Dispute & Chargeback System | Card Processing | Core Processing | L2 | Chargeback Engine, Dispute Management System, Chargeback Processor |
| Card Rewards Engine | Card Processing | Core Processing | L2 | Loyalty & Rewards Engine, Points Engine, Cashback Engine |
| EMV Cryptogram Validation | Card Authorization Engine | Core Processing | L3 | ARQC Validation, Chip Cryptogram Service, EMV Validation Service |
| Stand-In Processing Service | Card Authorization Engine | Core Processing | L3 | STIP Service, On-Behalf-Of Processing, Stand-In Authorization Service |
| 3-D Secure Service | Card Authorization Engine | Core Processing | L3 | 3DS Service, EMV 3DS ACS, Cardholder Authentication Service |
| Portfolio Accounting Engine | Portfolio Management System | Core Processing | L2 | Investment Accounting Engine, Portfolio Bookkeeping, Position & Cash Engine |
| Rebalancing Engine | Portfolio Management System | Core Processing | L2 | Portfolio Rebalancer, Drift Management Engine, Model Rebalancing Service |
| Performance & Attribution Engine | Portfolio Management System | Core Processing | L2 | Performance Measurement Engine, Attribution Analytics, Returns & Attribution Service |
| Model Portfolio Manager | Portfolio Management System | Core Processing | L2 | Model Management Service, Target Allocation Manager, Sleeve & Model Engine |
| Order Routing Engine | Order Management System | Core Processing | L2 | Order Routing Service, FIX Routing Engine |
| Execution Management Service | Order Management System | Core Processing | L2 | EMS, Execution Workbench, Trade Execution Service |
| Trade Allocation Engine | Order Management System | Core Processing | L2 | Allocation Service, Block Allocation Engine, Average Price Allocation |
| Securities Settlement Processor | Order Management System | Core Processing | L2 | Securities Settlement Engine, Post-Trade Processor, SSI & Confirmation Service |
| Risk Profiling Engine | Investment Advisory Platform | Core Processing | L2 | Investor Risk Profiler, Risk Tolerance Engine, Suitability Profiling Service |
| Goal-Based Planning Engine | Investment Advisory Platform | Core Processing | L2 | Financial Planning Engine, Goals-Based Planning Service, Cashflow Planning Engine |
| Robo-Advisory Engine | Investment Advisory Platform | Core Processing | L2 | Robo-Advisor, Automated Advice Engine, Digital Advice Engine |
| Tax-Loss Harvesting Service | Rebalancing Engine | Core Processing | L3 | TLH Service, Tax-Aware Rebalancing, Loss Harvesting Engine |
| Pre-Trade Compliance Engine | Order Routing Engine | Core Processing | L3 | Pre-Trade Compliance, Investment Guideline Monitor, Mandate Compliance Engine |
| Suitability Assessment Service | Risk Profiling Engine | Core Processing | L3 | Suitability Engine, Appropriateness Service, Advice Suitability Check |
| Credit Risk Model Engine | Risk Analytics Engine | AI & Automation | L2 | Credit Risk Engine, ECL Engine, Credit Portfolio Engine |
| Market Risk Engine | Risk Analytics Engine | AI & Automation | L2 | Market Risk VaR Engine, VaR Engine, FRTB Engine |
| Economic Capital Engine | Risk Analytics Engine | AI & Automation | L2 | Capital Engine, Economic Capital Calculator, RAROC Engine |
| Stress Testing Engine | Risk Analytics Engine | AI & Automation | L2 | Scenario Analysis Engine, Enterprise Stress Testing |
| Counterparty Risk & XVA Service | Market Risk Engine | AI & Automation | L3 | XVA Engine, Counterparty Credit Risk Service, PFE Engine |
| Risk Data Warehouse | Risk Data Aggregation | Data & Analytics | L2 | Risk Data Store, Risk Mart, Risk Repository |
| Risk Data Lineage | Risk Data Aggregation | Data & Analytics | L2 | Data Lineage (Risk), Risk Lineage Tracing |
| Exposure Aggregation Service | Risk Data Aggregation | Data & Analytics | L2 | Risk Aggregation Service, Exposure Consolidation |
| Model Inventory Registry | Model Risk Management Platform | AI & Automation | L2 | Model Inventory, Model Catalog, AI Inventory |
| Model Validation Workbench | Model Risk Management Platform | AI & Automation | L2 | Validation Workbench, Model Testing Suite, Independent Validation |
| Risk Control Self-Assessment Engine | Governance Risk & Compliance Platform | Data & Analytics | L2 | RCSA Engine, Risk Register Engine, Control Assessment Service |
| Loss Event Register | Governance Risk & Compliance Platform | Data & Analytics | L2 | Loss Database, Operational Loss Register, Loss Event Capture |
| Policy & Control Management | Governance Risk & Compliance Platform | Data & Analytics | L2 | Policy Management, Control Library, Compliance Management Service |
| Scenario Detection Engine | Transaction Monitoring Platform | AI & Automation | L2 | Behavior Detection Engine, Scenario Engine, AML Detection Engine, Typology Engine |
| Detection Scenario Library | Scenario Detection Engine | AI & Automation | L3 | Scenario Library, Scenario Manager, Rule Library |
| Behavioural Risk Analytics | Transaction Monitoring Platform | AI & Automation | L2 | AML Machine Learning, Anomaly Detection Service, Behavioural Profiling, Unsupervised Detection |
| Watchlist Screening Engine | Transaction Monitoring Platform | AI & Automation | L2 | Name Screening Engine, Sanctions Matching Engine, List Screening Engine, Filter Engine |
| Watchlist Data Management | Watchlist Screening Engine | AI & Automation | L3 | List Management Service, Reference List Manager, Sanctions List Loader, WorldCompliance Data |
| Alert Scoring Service | Transaction Monitoring Platform | AI & Automation | L2 | Alert Prioritisation Service, Alert Correlation Service, Alert Triage Engine, Alert Generation Engine |
| Financial Crime Case Manager | Transaction Monitoring Platform | AI & Automation | L2 | FinCrime Case Management, Investigation Workbench, Enterprise Case Management, ActOne |
| SAR Filing Service | Financial Crime Case Manager | AI & Automation | L3 | STR Filing Service, Regulatory Report Filing (AML), goAML Connector, SAR Generator |
| Network Entity Resolution | Transaction Monitoring Platform | AI & Automation | L2 | Entity Resolution Engine, Network Analytics, Link Analysis |
| Regulatory Report Calculation Engine | Regulatory Reporting Engine | Data & Analytics | L2 | Report Calculation Engine, Reporting Computation Engine, Abacus Calculation Engine, Reg Calc Engine |
| Regulatory Data Model | Regulatory Reporting Engine | Data & Analytics | L2 | Harmonised Data Model, Granular Data Layer, Reporting Data Model, Reg Data Layer |
| Regulatory Taxonomy Manager | Regulatory Reporting Engine | Data & Analytics | L2 | Taxonomy Manager, Reporting Template Manager, XBRL Taxonomy Service, Regulatory Rules Library |
| Report Validation Service | Regulatory Reporting Engine | Data & Analytics | L2 | Reporting Validation Service, Plausibility Check Service, Quality Rule Engine |
| Reporting Reconciliation Workbench | Regulatory Reporting Engine | Data & Analytics | L2 | Reconciliation Workbench, Reg Reconciliation Service, Figure Reconciliation, Reporting Sign-Off |
| Regulatory Submission Gateway | Regulatory Reporting Engine | Data & Analytics | L2 | Submission Gateway, Regulator Connectivity, Filing Gateway, Reporting API Gateway |
| Data Quality Engine | Data Governance | Data & Analytics | L2 | Data Quality Service, DQ Engine, Data Profiling Service, Quality Monitoring |
| Data Lineage Tracker | Data Governance | Data & Analytics | L2 | Lineage Service, Data Lineage Engine, Provenance Tracker, End-to-End Lineage |
| Metadata Catalog | Data Governance | Data & Analytics | L2 | Data Catalog Service, Metadata Repository, Asset Catalog, Data Discovery |
| Business Glossary Manager | Metadata Catalog | Data & Analytics | L3 | Business Glossary, Term Management, Semantic Glossary, Data Dictionary |
| Data Policy & Stewardship Service | Data Governance | Data & Analytics | L2 | Stewardship Workflow, Policy Management (Data), Data Governance Workflow, Data Ownership Service |
| Mobile App Framework | Digital Channel Platform | Channels & Engagement | L2 | Mobile SDK Platform, Mobile Banking Framework, Multi-Experience Framework |
| Web Banking Portal | Digital Channel Platform | Channels & Engagement | L2 | Internet Banking Portal, Web Channel, Online Banking Portal |
| Channel Orchestration Layer | Digital Channel Platform | Channels & Engagement | L2 | Experience Orchestration, Backend-for-Frontend, Journey Orchestration Mid-Tier |
| Onboarding Journey Orchestrator | Digital Channel Platform | Channels & Engagement | L2 | Onboarding Journey Engine, Origination Front-End, Digital Onboarding Module |
| Digital SCA Service | Digital Channel Platform | Channels & Engagement | L2 | Step-Up Authentication Service, In-App SCA, Dynamic Linking Service |
| In-App Messaging | Digital Channel Platform | Channels & Engagement | L2 | In-Session Messaging, Secure Inbox, Contextual Messaging |
| Personalisation Engine | Digital Channel Platform | Channels & Engagement | L2 | Personalization Engine, Offer Targeting Engine, Next-Best-Experience Engine |
| Digital Analytics | Digital Channel Platform | Channels & Engagement | L2 | Digital Behavioural Analytics, Journey Analytics, Product Analytics |
| Feature Flag Service | Digital Channel Platform | Channels & Engagement | L2 | Feature Toggle Service, Release Flagging, Progressive Delivery Service |
| Native Mobile SDK | Mobile App Framework | Channels & Engagement | L3 | Mobile Banking SDK, Embeddable Mobile SDK |
| Progressive Web App Runtime | Web Banking Portal | Channels & Engagement | L3 | PWA Runtime, Responsive Web Runtime |
| A/B Testing Service | Feature Flag Service | Channels & Engagement | L3 | Experimentation Service, Multivariate Testing |
| Interactive Voice Response | Contact Center Platform | Channels & Engagement | L2 | IVR Engine, Voice Self-Service Engine, Conversational IVR |
| Automatic Call Distribution | Contact Center Platform | Channels & Engagement | L2 | ACD Engine, Call Distribution Engine |
| Omnichannel Routing Engine | Contact Center Platform | Channels & Engagement | L2 | Omnichannel Routing, Interaction Routing Engine, Universal Queue |
| Agent Desktop | Contact Center Platform | Channels & Engagement | L2 | Agent Workspace, Unified Agent Desktop, Contact Centre Desktop |
| Interaction Analytics | Contact Center Platform | Channels & Engagement | L2 | Speech Analytics, Conversation Analytics, Interaction Insights |
| Workforce Engagement Management | Contact Center Platform | Channels & Engagement | L2 | WEM, Workforce Optimization, WFO |
| Computer Telephony Integration | Contact Center Platform | Channels & Engagement | L2 | CTI, Telephony Integration, Call Control Service |
| Outbound Dialer | Contact Center Platform | Channels & Engagement | L2 | Predictive Dialer, Campaign Dialer, Proactive Outbound |
| Skills-Based Routing | Omnichannel Routing Engine | Channels & Engagement | L3 | Skill Routing, Proficiency Routing |
| Real-Time Transcription | Interaction Analytics | Channels & Engagement | L3 | Live Transcription, Real-Time Speech-to-Text |
| Quality Management Service | Workforce Engagement Management | Channels & Engagement | L3 | Quality Management, QM, Automated QA |
| Screen Pop Service | Computer Telephony Integration | Channels & Engagement | L3 | Screen Pop, Contextual Pop |
| Knowledge Base Service | CRM Platform | Channels & Engagement | L2 | Knowledge Management, Service Knowledge Base, Answer Library |
| Journal Processing Engine | General Ledger Engine | Core Processing | L2 | Journal Engine, Universal Journal Service, GL Posting Engine, Document Posting Engine |
| Subledger Accounting | General Ledger Engine | Core Processing | L2 | SLA, Subledger Accounting Engine, Accounting Hub, Subledger Service |
| Chart Of Accounts Service | General Ledger Engine | Core Processing | L2 | COA Service, Accounting Structure Service, Ledger & Segment Master, Account Master Service |
| Accounting Rules Engine | General Ledger Engine | Core Processing | L2 | Account Determination Engine, Posting Rules Engine, Document Splitting Service |
| Allocation Engine | General Ledger Engine | Core Processing | L2 | Cost Allocation Engine, Distribution & Assessment Engine, Profitability Allocation Service |
| Period Close Manager | General Ledger Engine | Core Processing | L2 | Financial Close Cockpit, Close Orchestration Service, GL Close Manager |
| Account Reconciliation Service | General Ledger Engine | Core Processing | L2 | Reconciliation Engine, Transaction Matching Service, Balance Sheet Reconciliation |
| Multi-Currency Ledger Service | Journal Processing Engine | Core Processing | L3 | Currency Translation Service, FX Revaluation Service, Multi-Currency Posting |
| Intercompany Accounting Service | Subledger Accounting | Core Processing | L3 | Intercompany Engine, ICO Matching Service, Intercompany Reconciliation |
| Cash Positioning Service | Treasury Management System | Core Processing | L2 | Cash Visibility Service, Cash Position Engine, Global Cash Management |
| Bank Connectivity Hub | Treasury Management System | Core Processing | L2 | Bank Connectivity Service, SWIFT Service Bureau, Treasury Connectivity Gateway, Multi-Bank Connectivity |
| Deal Management | Treasury Management System | Core Processing | L2 | Treasury Deal Capture, Front-Office Dealing, Treasury Instrument Management, Trade & Position Management |
| Liquidity Forecasting Engine | Treasury Management System | Core Processing | L2 | Cash Forecasting Engine, AI Cash Forecasting, Liquidity Planning Service |
| Treasury Risk Management Service | Treasury Management System | Core Processing | L2 | FX & Risk Management Service, Hedge Management Service, Treasury Exposure Management |
| In-House Banking Service | Treasury Management System | Core Processing | L3 | IHB Service, Payment Factory, POBO/COBO Service, Internal Bank |
| IRRBB Analytics Engine | Asset Liability Management Engine | Core Processing | L2 | Interest Rate Risk Engine, EVE/NII Engine, Banking Book Rate Risk Engine |
| Funds Transfer Pricing Engine | Asset Liability Management Engine | Core Processing | L2 | FTP Engine, Transfer Pricing Service, Funds Transfer Pricing Service |
| Behavioural Modelling Service | Asset Liability Management Engine | Core Processing | L2 | Behavioral Modeling Service, NMD Modelling Service, Prepayment Modelling Engine |
| Balance Sheet Planning Engine | Asset Liability Management Engine | Core Processing | L2 | Balance Sheet Management Engine, NII Simulation Engine, ALM Scenario Engine |
| Consolidation Engine | Financial Consolidation Platform | Core Processing | L2 | Group Consolidation Engine, Financial Consolidation Service, Consol Engine |
| Planning & Budgeting Engine | Financial Consolidation Platform | Core Processing | L2 | Planning Engine, FP&A Engine, Budgeting & Forecasting Service, EPM Planning |
| Disclosure Management Service | Financial Consolidation Platform | Core Processing | L2 | Narrative Reporting Service, XBRL Tagging Service, Statutory Reporting Service |
| Financial Data Quality Service | Financial Consolidation Platform | Core Processing | L3 | Financial Data Quality Management, FDQM, Data Integration & Validation (Finance) |
| Product Catalog Service | Product & Pricing Engine | Core Processing | L3 | Product Catalogue Service, Product Definition Service, Universal Product Catalog |
| Fee & Charge Calculator | Product & Pricing Engine | Core Processing | L3 | Fee Calculation Service, Charge Computation Engine, Relationship Pricing Service |
| Posting Determination Service | Transaction Posting Engine | Core Processing | L3 | Posting Rule Resolver, Ledger Entry Determination, Entry Generation Service |
| Accrual Calculation Service | Interest & Charges Engine | Core Processing | L3 | Daily Accrual Service, Interest Accrual Calculator, Accrual Engine Service |
| ISO 8583 Message Switch | Card Transaction Switch | Core Processing | L3 | 8583 Switch Service, Card Scheme Message Switch, Authorization Message Switch |
| Network Token Service | Card Tokenization Service | Core Processing | L3 | Scheme Token Connector, EMVCo Token Service, VTS MDES Connector |
| Token Vault Manager | Card Tokenization Service | Core Processing | L3 | Issuer Token Vault Service, PAN Token Vault, Token Mapping Store |
| Document Splitting Engine | Accounting Rules Engine | Core Processing | L3 | Document Split Service, Segment Splitting Engine, Line-Item Splitting Service |
| Assessment Cycle Engine | Allocation Engine | Core Processing | L3 | Assessment & Distribution Engine, Cost Cycle Engine, Allocation Cycle Service |
| Bank Statement Ingestion Service | Cash Positioning Service | Core Processing | L3 | Statement Parsing Service, BAI2 MT940 Parser, Electronic Bank Statement Loader |
| FX Exposure Aggregation Service | Treasury Risk Management Service | Core Processing | L3 | FX Exposure Engine, Currency Exposure Aggregator, Net FX Position Service |
| Hedge Accounting Service | Treasury Risk Management Service | Core Processing | L3 | Hedge Accounting Engine, Hedge Designation Service, IFRS 9 Hedge Service |
| Repricing Gap Engine | IRRBB Analytics Engine | Core Processing | L3 | Gap Analysis Engine, Repricing Bucket Engine, Maturity Gap Service |
| Transfer Curve Engine | Funds Transfer Pricing Engine | Core Processing | L3 | FTP Curve Engine, Matched-Maturity Curve Service, Transfer Rate Curve Builder |
| Brinson Attribution Service | Performance & Attribution Engine | Core Processing | L3 | Brinson-Fachler Service, Return Attribution Engine, Active Return Decomposition |
| GIPS Composite Service | Performance & Attribution Engine | Core Processing | L3 | GIPS Reporting Service, Composite Management Service, Performance Composite Engine |
| Drift Monitoring Service | Model Portfolio Manager | Core Processing | L3 | Model Drift Monitor, Tolerance Band Service, Rebalance Trigger Service |
| FIX Order Gateway | Execution Management Service | Core Processing | L3 | FIX Connectivity Gateway, FIX Session Manager, Execution FIX Gateway |
| Average Price Book Service | Trade Allocation Engine | Core Processing | L3 | Average Pricing Service, Block Average Price Engine, Fill Aggregation Service |
| Adverse Action Reason Service | Adverse Action Generator | Core Processing | L3 | Reason Code Derivation Service, Principal Reason Service, ECOA Reason Service |
| Bureau Response Normalizer | Bureau Data Integration | Core Processing | L3 | Bureau Data Normaliser, Credit Report Parser, Bureau Attribute Mapper |
| Document Classification Service | Document Capture & Verification | Core Processing | L3 | Document Type Classifier, Page Classification Service, Doc Sorting Service |
| Data Extraction Service | Document Capture & Verification | Core Processing | L3 | OCR Extraction Service, Field Extraction Engine, Document Data Extractor |
| Beneficiary Verification Service | Payment Validation Engine | Core Processing | L3 | Confirmation of Payee Service, Payee Validation Service, Account Verification Service |
| Sanctions Hit Disposition Service | Payment Sanctions Filter | Core Processing | L3 | Hit Disposition Workbench, Sanctions Alert Disposition, Screening Hit Workflow |
| Intercompany Matching Service | Consolidation Engine | Core Processing | L3 | IC Matching Service, Intercompany Reconciliation (Consolidation), Group Matching Service |
| Data Lakehouse Platform | Data Warehousing | Data & Analytics | L2 | Lakehouse Platform, Open Lakehouse, Delta/Iceberg Lakehouse |
| Cloud Data Warehouse | Data Warehousing | Data & Analytics | L2 | Cloud DW, MPP Warehouse, Analytical Data Store |
| ELT Pipeline Engine | Data Warehousing | Data & Analytics | L2 | ETL/ELT Pipeline Engine, Data Pipeline Orchestrator, Ingestion & Load Engine |
| Data Transformation Framework | Data Warehousing | Data & Analytics | L2 | dbt Framework, In-Warehouse Transformation, Analytics Engineering Framework |
| Semantic Layer Service | Data Warehousing | Data & Analytics | L2 | Semantic Layer, Metrics Layer, Universal Semantic Model |
| Data Mart Service | Data Warehousing | Data & Analytics | L2 | Data Mart Management, Subject-Area Mart, Marts Layer |
| Distributed Query Engine | Data Warehousing | Data & Analytics | L2 | Query Engine, Federated Query Engine, MPP Query Engine |
| Medallion Storage Layer | Data Lakehouse Platform | Data & Analytics | L3 | Medallion Architecture, Bronze-Silver-Gold Layers, Curated Storage Zones |
| Event Streaming Bus | Data Streaming | Data & Analytics | L2 | Streaming Backbone, Kafka Bus, Event Log |
| Stream Processing Engine | Data Streaming | Data & Analytics | L2 | Stream Compute Engine, Real-Time Processing Engine, Flink Engine |
| Change Data Capture Service | Data Streaming | Data & Analytics | L2 | CDC Service, Debezium Connector, Log-Based CDC |
| Event Schema Registry | Data Streaming | Data & Analytics | L2 | Schema Registry, Stream Schema Service, Message Contract Registry |
| Streaming Connector Framework | Data Streaming | Data & Analytics | L2 | Streaming Connectors, Kafka Connect, Connector Hub |
| Stateful Stream Processor | Stream Processing Engine | Data & Analytics | L3 | Windowed Aggregation Service, Keyed State Processor, Stream Join Engine |
| BI & Reporting Service | Analytics Platform | Data & Analytics | L2 | BI Reporting Service, Reporting Service, Operational Reporting |
| Self-Service Analytics | Analytics Platform | Data & Analytics | L2 | Self-Serve Analytics, Ad-Hoc Exploration, Citizen Analytics |
| OLAP Cube Engine | Analytics Platform | Data & Analytics | L2 | OLAP Engine, Multidimensional Model Engine, Analysis Services Engine |
| Dashboarding Service | Analytics Platform | Data & Analytics | L2 | Dashboard Service, Interactive Dashboards, KPI Dashboards |
| Embedded Analytics Service | Analytics Platform | Data & Analytics | L2 | Embedded Analytics, Embedded BI, White-Label Analytics |
| Data Visualisation Library | Analytics Platform | Data & Analytics | L2 | Data Visualization Library, Charting Library, Visualisation Components |
| Natural Language Query Service | Self-Service Analytics | Data & Analytics | L3 | NL Query Service, Search Analytics, AI-Assisted Query |
| Content Repository | Document Management | Data & Analytics | L2 | Content Store, Document Repository, ECM Repository |
| Content Capture Service | Document Management | Data & Analytics | L2 | Capture Service, Document Imaging, Content Capture |
| Records Management Service | Document Management | Data & Analytics | L2 | Records Management, Recordkeeping Service, RM Service |
| Content Workflow Engine | Document Management | Data & Analytics | L2 | Content Workflow, Document Workflow, Process Automation (ECM) |
| E-Signature Integration | Document Management | Data & Analytics | L2 | Electronic Signature Service, E-Sign Integration, Digital Signing Service |
| Archival & Retention Service | Document Management | Data & Analytics | L2 | Archival Service, Retention Management, Preservation Service |
| Intelligent Document Recognition | Content Capture Service | Data & Analytics | L3 | Intelligent Document Recognition Service, OCR & Extraction Service, Document Field Extraction |
| Reference Data Management | Master Data Management | Data & Analytics | L2 | Reference Data Service, Code Table Management, RDM |
| Deterministic Match Engine | Party Matching & Merge | Data & Analytics | L3 | Rule-Based Matching, Exact Match Engine, Identifier Matching |
| Cross-Reference Registry | Golden Record Management | Data & Analytics | L3 | Cross-Reference Service, Key Mapping Registry, XREF Registry |
| Data Classification Service | Metadata Catalog | Data & Analytics | L3 | Data Tagging Service, Sensitivity Classification, Data Categorisation |
| Data Quality Rule Engine | Data Quality Engine | Data & Analytics | L3 | DQ Rule Engine, Validation Rule Service, Quality Rule Manager |
| Risk Data Mart | Risk Data Warehouse | Data & Analytics | L3 | Risk Subject-Area Mart, Risk Reporting Mart |

## Process sub-processes

| Canonical Name | Parent Process | Domain | Aliases |
|---|---|---|---|
| Payment Capture & Validation | Payment Processing | Payments | Payment Intake, Capture & Validation |
| Payment Authorization & Routing | Payment Processing | Payments | Authorization & Routing, Payment Routing |
| Clearing Submission | Payment Processing | Payments | Rail Submission, Clearing Dispatch |
| Settlement Confirmation | Reconciliation & Settlement | Payments | Settlement Capture |
| Account Reconciliation | Reconciliation & Settlement | Payments | Statement Matching, Nostro Recon |
| Exception Investigation | Reconciliation & Settlement | Payments | Break Resolution, Investigations |
| Cash Positioning | Cash Management | Payments | Position Keeping, Cash Visibility |
| Liquidity Forecasting | Cash Management | Payments | Cash Forecasting, Liquidity Planning |
| Funding & Concentration | Cash Management | Payments | Cash Concentration, Sweeping & Pooling |
| Application Intake & Capture | Customer Onboarding | Customer Management | Onboarding Intake, Application Capture |
| Identity & Due Diligence | Customer Onboarding | Customer Management | KYC & CDD, Verification & Diligence |
| Account Setup & Activation | Customer Onboarding | Customer Management | Onboarding Activation, Account Setup Activation |
| Complaint Intake & Triage | Complaint Handling | Customer Management | Complaint Logging, Complaint Intake Triage |
| Complaint Investigation & Redress | Complaint Handling | Customer Management | Investigation & Redress, Resolution & Redress |
| Complaint Closure & Learning | Complaint Handling | Customer Management | Closure & RCA, Learning & Reporting |
| Request Intake & Triage | Service Request Handling | Customer Management | Request Logging, Request Intake Triage |
| Request Fulfilment & Closure | Service Request Handling | Customer Management | Fulfilment & Closure, Resolution & Closure |
| Application Origination & Pre-Qualification | Loan Origination Workflow | Lending & Credit | Origination Pre-Qualification, Pre-Qual |
| Application Processing & Verification | Loan Origination Workflow | Lending & Credit | Loan Processing, File Verification |
| Offer & Disbursement | Loan Origination Workflow | Lending & Credit | Offer & Funding, Disbursement |
| Risk & Affordability Assessment | Credit Underwriting | Lending & Credit | 5 Cs Assessment, Affordability Review |
| Credit Adjudication | Credit Underwriting | Lending & Credit | Adjudication, Credit Decisioning Sub-Process |
| Mortgage Application & Disclosure | Mortgage Origination | Lending & Credit | Mortgage Intake, TRID Disclosure |
| Property & Title Diligence | Mortgage Origination | Lending & Credit | Collateral Diligence, Appraisal & Title |
| Closing & Mortgage Funding | Mortgage Origination | Lending & Credit | Closing & Funding, CTC |
| Early-Stage Collections | Loan Collections | Lending & Credit | Early Collections, Soft Collections |
| Late-Stage Recovery | Loan Collections | Lending & Credit | Late Collections, Hard Collections |
| Documentary Credit Issuance | Trade Finance Processing | Lending & Credit | LC Issuance, Credit Issuance |
| Presentation & Settlement | Trade Finance Processing | Lending & Credit | Document Examination, LC Settlement |
| Application & Identity Capture | Deposit Account Opening | Deposits & Accounts | Opening Intake, CIP Capture |
| Account Setup & Funding | Deposit Account Opening | Deposits & Accounts | Open & Fund, Activation |
| Statement Assembly | Statement Generation | Deposits & Accounts | Statement Build, Cycle Assembly |
| Statement Delivery | Statement Generation | Deposits & Accounts | Statement Distribution, E-Statement Delivery |
| Maintenance Intake & Verification | Account Maintenance | Deposits & Accounts | Maintenance Intake, Mandate Check |
| Account Update Execution | Account Maintenance | Deposits & Accounts | Update Execution, Servicing Action |
| Closure Request Handling | Account Closure | Deposits & Accounts | Closure Intake, Closure Validation |
| Balance Settlement & Deactivation | Account Closure | Deposits & Accounts | Settle & Close, Final Settlement |
| Dormancy & Escheatment | Account Closure | Deposits & Accounts | Escheatment, Abandoned Property Handling |
| Overdraft Decisioning | Overdraft Servicing | Deposits & Accounts | OD Decisioning, Pay/Return Decision |
| Overdraft Fee & Notice | Overdraft Servicing | Deposits & Accounts | Fee Application, OD Notice |
| Card Application & Decisioning | Card Issuance | Cards | Card App & Decision, Issuance Decisioning |
| Card Production & Fulfillment | Card Issuance | Cards | Production & Fulfillment, Card Personalization |
| Card Activation & Provisioning | Card Issuance | Cards | Activation & Wallet Provisioning |
| Ledger Close & Reconciliation | Financial Close | Finance & Treasury | Subledger Close, GL Close, Close & Recon |
| Consolidation & Statements | Financial Close | Finance & Treasury | Group Consolidation, Statement Preparation |
| Period-End Adjustments | Financial Close | Finance & Treasury | Accruals & Adjustments, Period-End Journals |
| Budget & Forecast Preparation | Management Reporting | Finance & Treasury | Budget Build, Operating Budget Preparation |
| Variance & Insight Reporting | Management Reporting | Finance & Treasury | Variance Analysis, MI Reporting |
| Capital Calculation & Aggregation | Regulatory Capital Reporting | Finance & Treasury | RWA & Own Funds, Capital Aggregation |
| Return Assembly & Submission | Regulatory Capital Reporting | Finance & Treasury | COREP Submission, Capital Return Filing |
| Scenario & Capital Planning | Regulatory Capital Reporting | Finance & Treasury | CCAR Planning, Capital Plan Assembly |
| Intraday Liquidity Positioning | Cash & Liquidity Management | Finance & Treasury | Intraday Positioning, Position Projection |
| Funding & Buffer Management | Cash & Liquidity Management | Finance & Treasury | Buffer Management, Funding Execution Sub-Process |
| Curve Construction & Governance | Funds Transfer Pricing | Finance & Treasury | FTP Curve Build, Curve Governance |
| Rate Application & Attribution | Funds Transfer Pricing | Finance & Treasury | FTP Application, Margin Attribution |
| Dispute Intake & Investigation | Dispute Resolution | Cards | Dispute Intake |
| Provisional Credit & Resolution | Dispute Resolution | Cards | Resolution & Credit, Dispute Closure |
| Authorization Validation & Decisioning | Card Transaction Authorization | Cards | Auth Decisioning, Approve/Decline |
| Authorization Response & Hold | Card Transaction Authorization | Cards | Auth Response, Hold Management |
| Clearing & Posting | Card Transaction Authorization | Cards | Presentment Posting, Clearing Match |
| Dispute Intake & Provisional Credit | Chargeback Processing | Cards | Provisional Credit Intake |
| Chargeback Filing & Representment | Chargeback Processing | Cards | Filing & Representment |
| Dispute Resolution & Recovery | Chargeback Processing | Cards | Resolution & Recovery, Case Closure |
| Fraud Detection & Triage | Card Fraud Handling | Cards | Detection & Triage, Alert Triage |
| Card Containment & Reissue | Card Fraud Handling | Cards | Containment & Reissue, Block & Reissue |
| Fraud Adjudication & Reporting | Card Fraud Handling | Cards | Adjudication & Reporting, Fraud Disposition |
| Investor Profiling & Suitability | Wealth Onboarding | Wealth & Investments | Suitability Onboarding, Investor Profiling Sub-Process |
| Investment Account Setup | Wealth Onboarding | Wealth & Investments | Investment Account Opening, Mandate Setup |
| Client Discovery & Profiling | Financial Planning | Wealth & Investments | Discovery, Client Fact Find |
| Plan Construction & Suitability | Financial Planning | Wealth & Investments | Plan Construction, Suitability Determination |
| IPS Agreement & Documentation | Financial Planning | Wealth & Investments | IPS Agreement, Advice Documentation |
| Drift Detection & Proposal | Portfolio Rebalancing | Wealth & Investments | Drift Detection, Rebalance Proposal |
| Rebalance Compliance & Approval | Portfolio Rebalancing | Wealth & Investments | Rebalance Approval, Rebalance Pre-Trade Compliance |
| Order Capture & Compliance | Trade Order Management | Wealth & Investments | Order Intake, Pre-Trade Check |
| Routing & Execution | Trade Order Management | Wealth & Investments | Execution, Order Execution Sub-Process |
| Confirmation, Allocation & Settlement | Trade Order Management | Wealth & Investments | Allocation & Settlement, Post-Trade |
| Valuation & Reconciliation | Performance Reporting | Wealth & Investments | Valuation & Recon, Book Reconciliation |
| Return Measurement & Delivery | Performance Reporting | Wealth & Investments | Return Calc & Delivery, Reporting & Delivery |
| Real-Time Risk Scoring | Fraud Detection | Risk Management | Detection Scoring, Real-Time Fraud Scoring |
| Alert Generation & Routing | Fraud Detection | Risk Management | Alert Routing, Alert Orchestration |
| Case Triage & Investigation | Fraud Investigation | Risk Management | Triage & Investigation, Case Investigation |
| Disposition & Recovery | Fraud Investigation | Risk Management | Disposition & SAR, Fraud Resolution & Recovery |
| Appetite Definition & Limits | Risk Appetite Setting | Risk Management | Appetite & Limits, RAS Drafting |
| Appetite Approval & Cascade | Risk Appetite Setting | Risk Management | Approval & Cascade, RAS Approval |
| Risk Capture & Registration | Risk Identification & Assessment | Risk Management | Risk Capture, RCSA Identification |
| Inherent & Residual Assessment | Risk Identification & Assessment | Risk Management | Risk Scoring, Residual Assessment |
| Risk Treatment & Ownership | Risk Identification & Assessment | Risk Management | Treatment & Ownership, Risk Response |
| Scenario Design & Governance | Stress Testing | Risk Management | Scenario Build & Governance, Stress Scenario Design |
| Projection & Submission | Stress Testing | Risk Management | Projection & Filing, Capital Submission |
| Reporting Data Aggregation | Risk Reporting | Risk Management | Data Aggregation, RDA |
| Limit Monitoring & Escalation | Risk Reporting | Risk Management | Limit Tracking, Breach Escalation |
| Report Production & Distribution | Risk Reporting | Risk Management | Report Production, Reporting & Distribution |
| Identity Proofing & Verification | KYC Verification | Compliance & Financial Crime | CIP Verification |
| Customer Watchlist Screening | KYC Verification | Compliance & Financial Crime | Onboarding Screening, KYC Screening |
| Ongoing KYC Monitoring | KYC Verification | Compliance & Financial Crime | Ongoing Monitoring, KYC Refresh |
| Identification & Beneficial Ownership | Customer Due Diligence Onboarding | Compliance & Financial Crime | CIP & UBO, Onboarding Identification |
| Risk Rating & EDD Decision | Customer Due Diligence Onboarding | Compliance & Financial Crime | EDD Decisioning, Risk Rating & Approval |
| AML Alert Investigation | Suspicious Activity Reporting | Compliance & Financial Crime | Alert Investigation, AML Case Work |
| SAR Decision & Filing | Suspicious Activity Reporting | Compliance & Financial Crime | STR Decision |
| Match Generation & Triage | Sanctions Screening Operations | Compliance & Financial Crime | Alert Generation & Triage, Screening Triage |
| Hit Resolution & Reporting | Sanctions Screening Operations | Compliance & Financial Crime | Hit Disposition, Match Resolution |
| Regulatory Filing Preparation | Regulatory Filing | Compliance & Financial Crime | Return Preparation, Filing Prep |
| Filing Review & Submission | Regulatory Filing | Compliance & Financial Crime | Review & Submit, Filing Submission |
| Horizon Scanning & Impact | Regulatory Change Management | Compliance & Financial Crime | Horizon Scanning, Impact Assessment |
| Remediation & Attestation | Regulatory Change Management | Compliance & Financial Crime | Remediation & Sign-Off, Change Attestation |
| Branch Counter Servicing | Branch Operations | Channels & Engagement | Teller Servicing, Branch Counter Operations |
| Branch Cash Control | Branch Operations | Channels & Engagement | Vault & Drawer Control, Branch Cash Balancing |
| Digital Application Intake | Digital Onboarding Journey | Channels & Engagement | DAO Intake, Digital Intake |
| Digital Identity & Activation | Digital Onboarding Journey | Channels & Engagement | eKYC & Activation, Verify & Activate |
| Channel Authentication & Orchestration | Channel Servicing | Channels & Engagement | Session Orchestration, Channel Auth |
| Self-Service Resolution | Channel Servicing | Channels & Engagement | Self-Service Handling, In-Channel Servicing |
| ATM Cash Forecasting & Ordering | ATM Cash Servicing | Channels & Engagement | ATM Forecasting, Cash Ordering |
| ATM Replenishment & Reconciliation | ATM Cash Servicing | Channels & Engagement | Replenishment & Recon, ATM Balancing |
| Interaction Intake & Routing | Contact Centre Interaction | Channels & Engagement | IVR & Routing, Contact Intake |
| Interaction Handling & QA | Contact Centre Interaction | Channels & Engagement | Handling & QA, Resolution & Wrap-Up |

## Process flow steps

| Canonical Name | Process | Order | Depends On | Aliases |
|---|---|---|---|---|
| Receive Payment Instruction | Payment Processing | 1 | Payment Orchestration | Capture Instruction, Intake Payment |
| Validate Payment | Payment Processing | 2 | Payment Orchestration | Payment Validation, Field Validation |
| Screen Sanctions | Payment Processing | 3 | Transaction Monitoring Platform | Watchlist Screening Step, OFAC Screening |
| Authorize Payment | Payment Processing | 4 | Fraud Analytics | Payment Authorization Step, Approve Payment |
| Route Payment | Payment Processing | 5 | Payment Orchestration | Rail Selection, Payment Routing Step |
| Format Clearing Message | Payment Processing | 6 | Payment Orchestration | Build Clearing Message, Message Formatting |
| Submit To Clearing | Payment Processing | 7 | Payment Orchestration | Dispatch To Operator, Rail Submission Step |
| Capture Clearing Response | Payment Processing | 8 | Payment Orchestration | Process Clearing Status, Return Handling |
| Confirm Settlement | Reconciliation & Settlement | 1 | Payment Orchestration | Settlement Confirmation Step, Capture Settlement |
| Ingest Bank Statement | Reconciliation & Settlement | 2 | Integration Platform | Load Statement, Statement Ingestion |
| Match Transactions | Reconciliation & Settlement | 3 | Core Banking Processing | Auto Matching, Transaction Matching |
| Identify Breaks | Reconciliation & Settlement | 4 | Workflow Orchestration | Break Detection, Exception Identification |
| Investigate Break | Reconciliation & Settlement | 5 | Workflow Orchestration | Break Investigation, Exception Handling |
| Post Adjustment | Reconciliation & Settlement | 6 | General Ledger Engine | Adjustment Posting, Correcting Entry |
| Sign Off Reconciliation | Reconciliation & Settlement | 7 | Workflow Orchestration | Recon Certification, Reconciliation Sign-Off |
| Aggregate Balances | Cash Management | 1 | Integration Platform | Balance Aggregation, Gather Balances |
| Determine Cash Position | Cash Management | 2 | Core Banking Processing | Position Calculation, Cash Positioning Step |
| Forecast Cash Flow | Cash Management | 3 | Analytics Platform | Cash Forecasting Step, Liquidity Forecast |
| Decide Funding Actions | Cash Management | 4 | Analytics Platform | Funding Decisioning, Liquidity Decision |
| Execute Funding Transfer | Cash Management | 5 | Payment Orchestration | Sweep Execution, Funding Execution |
| Monitor Liquidity Position | Cash Management | 6 | Analytics Platform | Liquidity Monitoring, Position Monitoring |
| Report Cash Status | Cash Management | 7 | Analytics Platform | Cash Reporting, Treasury Reporting |
| Receive Application | Customer Onboarding | 1 | Digital Channel Platform | Capture Application, Intake Applicant |
| Capture Consent | Customer Onboarding | 2 | Customer Identity | Record Consent, Consent Capture Step |
| Collect Documents | Customer Onboarding | 3 | Intelligent Document Processing | Gather Documents, Document Collection Step |
| Verify Identity | Customer Onboarding | 4 | Identity Verification | Prove Identity, Identity Proofing Step |
| Screen Customer | Customer Onboarding | 5 | Transaction Monitoring Platform | Screen Applicant, Watchlist Check Step |
| Assess Customer Risk | Customer Onboarding | 6 | Customer Due Diligence | Risk Rate Customer, CDD Assessment Step |
| Approve Onboarding | Customer Onboarding | 7 | Workflow Orchestration | Decide Onboarding, Onboarding Approval Step |
| Create Customer Record | Customer Onboarding | 8 | Master Data Management | Establish Party Record, Customer Record Creation |
| Activate Customer | Customer Onboarding | 9 | Notification Services | Welcome Customer, Customer Activation Step |
| Log Complaint | Complaint Handling | 1 | Case Management | Register Complaint, Complaint Logging Step |
| Acknowledge Complaint | Complaint Handling | 2 | Notification Services | Send Acknowledgement, Complaint Acknowledgement Step |
| Triage Complaint | Complaint Handling | 3 | Workflow Orchestration | Classify Complaint, Complaint Triage Step |
| Investigate Complaint | Complaint Handling | 4 | Case Management | Examine Complaint, Complaint Investigation Step |
| Determine Outcome | Complaint Handling | 5 | Case Management | Decide Redress, Outcome Decision Step |
| Issue Final Response | Complaint Handling | 6 | Notification Services | Send Final Response, Final Response Step |
| Conduct Root Cause | Complaint Handling | 7 | Analytics Platform | Root Cause Analysis Step, Analyse Drivers |
| Close Complaint | Complaint Handling | 8 | Case Management | Resolve & Close, Complaint Closure Step |
| Capture Request | Service Request Handling | 1 | Contact Center Platform | Log Request, Request Capture Step |
| Authenticate Requester | Service Request Handling | 2 | Identity Access Management | Verify Requester, Requester Authentication Step |
| Categorize Request | Service Request Handling | 3 | Workflow Orchestration | Classify Request, Request Triage Step |
| Assess Request | Service Request Handling | 4 | Case Management | Evaluate Request, Request Assessment Step |
| Fulfil Request | Service Request Handling | 5 | Core Banking Processing | Action Request, Request Fulfilment Step |
| Confirm Resolution | Service Request Handling | 6 | Notification Services | Notify Customer, Resolution Confirmation Step |
| Close Request | Service Request Handling | 7 | Case Management | Resolve & Close Request, Request Closure Step |
| Capture Loan Application | Loan Origination Workflow | 1 | Loan Origination Platform | Intake Loan Request, Loan Capture Step |
| Pre-Qualify Borrower | Loan Origination Workflow | 2 | Credit Decisioning Engine | Soft Eligibility Check, Prequal Step |
| Collect Supporting Documents | Loan Origination Workflow | 3 | Intelligent Document Processing | Gather Loan Documents, Document Intake Step |
| Verify Borrower Income | Loan Origination Workflow | 4 | Document Management | Income Verification Step, Verify Affordability Inputs |
| Render Loan Decision | Loan Origination Workflow | 5 | Credit Decisioning Engine | Decide Loan, Loan Adjudication Step |
| Issue Loan Offer | Loan Origination Workflow | 6 | Loan Origination Platform | Present Loan Offer, Offer Issuance Step |
| Disburse Loan Funds | Loan Origination Workflow | 7 | Core Banking Processing | Fund Loan, Disbursement Step |
| Pull Credit Report | Credit Underwriting | 1 | Credit Decisioning Engine | Order Bureau Data, Credit Pull Step |
| Score Credit Risk | Credit Underwriting | 2 | Machine Learning Platform | Risk Grading Step, Credit Scoring |
| Assess Affordability | Credit Underwriting | 3 | Credit Decisioning Engine | Capacity Test, Affordability Step |
| Evaluate Collateral | Credit Underwriting | 4 | Collateral Valuation | Security Evaluation Step, Collateral Review |
| Apply Credit Policy | Credit Underwriting | 5 | Credit Decisioning Engine | Policy Check Step, Conditions Setting |
| Adjudicate Credit | Credit Underwriting | 6 | Workflow Orchestration | Make Credit Decision, Adjudication Step |
| Take Mortgage Application | Mortgage Origination | 1 | Loan Origination Platform | Capture 1003, Mortgage Intake Step |
| Issue Loan Estimate | Mortgage Origination | 2 | Document Management | Deliver LE, TRID Disclosure Step |
| Order Property Appraisal | Mortgage Origination | 3 | Collateral Management | Order Valuation, Appraisal Step |
| Review Title And Liens | Mortgage Origination | 4 | Document Management | Title Examination Step, Lien Search |
| Clear To Close | Mortgage Origination | 5 | Credit Decisioning Engine | CTC Step, Final Approval |
| Deliver Closing Disclosure | Mortgage Origination | 6 | Document Management | Deliver CD, Closing Disclosure Step |
| Fund Mortgage Loan | Mortgage Origination | 7 | Core Banking Processing | Close And Fund, Mortgage Funding Step |
| Detect Delinquency | Loan Collections | 1 | Core Banking Processing | Identify Arrears, Delinquency Detection Step |
| Segment Arrears | Loan Collections | 2 | Analytics Platform | Prioritise Accounts, Arrears Segmentation Step |
| Contact Borrower | Loan Collections | 3 | Notification Services | Dunning Outreach, Borrower Contact Step |
| Negotiate Repayment | Loan Collections | 4 | Workflow Orchestration | Arrange Repayment, Promise-To-Pay Step |
| Escalate To Recovery | Loan Collections | 5 | Workflow Orchestration | Escalate Arrears, Recovery Escalation Step |
| Charge Off Debt | Loan Collections | 6 | Core Banking Processing | Write Off Debt, Charge-Off Step |
| Receive Credit Application | Trade Finance Processing | 1 | Workflow Orchestration | Take LC Request, Credit Application Step |
| Assess Trade Limit | Trade Finance Processing | 2 | Credit Decisioning Engine | Trade Limit Check, Credit Margining Step |
| Issue Letter Of Credit | Trade Finance Processing | 3 | Integration Platform | Issue LC, Credit Issuance Step |
| Advise Beneficiary | Trade Finance Processing | 4 | Notification Services | Advise LC, Beneficiary Advising Step |
| Examine Trade Documents | Trade Finance Processing | 5 | Document Management | Check Documents, Document Examination Step |
| Settle Trade Payment | Trade Finance Processing | 6 | Core Banking Processing | Honor Presentation, Trade Settlement Step |
| Capture Account Application | Deposit Account Opening | 1 | Digital Channel Platform | Take Account Application, Opening Intake Step |
| Collect CIP Information | Deposit Account Opening | 2 | Intelligent Document Processing | Gather CIP Data, CIP Collection Step |
| Verify Account Applicant | Deposit Account Opening | 3 | Identity Verification | Run CIP Verification, Applicant Verification Step |
| Capture Signature Card | Deposit Account Opening | 4 | Core Banking Processing | Record Signatories, Signature Capture Step |
| Disclose Account Terms | Deposit Account Opening | 5 | Document Management | Provide TIS Disclosure, Terms Disclosure Step |
| Establish Deposit Account | Deposit Account Opening | 6 | Core Banking Processing | Create Account, Account Setup Step |
| Fund New Account | Deposit Account Opening | 7 | Core Banking Processing | Activate Account, Initial Funding Step |
| Determine Statement Cycle | Statement Generation | 1 | Core Banking Processing | Identify Cycle, Cycle Determination Step |
| Extract Account Activity | Statement Generation | 2 | Core Banking Processing | Pull Postings, Activity Extraction Step |
| Reconcile Statement Data | Statement Generation | 3 | Data Warehousing | Validate Statement Totals, Statement Recon Step |
| Assemble Statement Document | Statement Generation | 4 | Document Management | Compose Statement, Statement Assembly Step |
| Render Statement Output | Statement Generation | 5 | Document Management | Produce Statement Output, Rendering Step |
| Deliver Statement | Statement Generation | 6 | Notification Services | Distribute Statement, Statement Delivery Step |
| Archive Statement | Statement Generation | 7 | Document Management | Store Statement, Statement Archival Step |
| Receive Maintenance Request | Account Maintenance | 1 | Digital Channel Platform | Log Maintenance Request, Maintenance Intake Step |
| Verify Account Holder | Account Maintenance | 2 | Identity Access Management | Authenticate Account Holder, Holder Verification Step |
| Assess Change Impact | Account Maintenance | 3 | Workflow Orchestration | Evaluate Change, Impact Assessment Step |
| Apply Account Change | Account Maintenance | 4 | Core Banking Processing | Execute Account Change, Change Execution Step |
| Post Account Interest | Account Maintenance | 5 | Core Banking Processing | Apply Interest Posting, Interest Posting Step |
| Notify Account Change | Account Maintenance | 6 | Notification Services | Confirm Account Change, Change Notification Step |
| Receive Closure Request | Account Closure | 1 | Digital Channel Platform | Log Closure Request, Closure Intake Step |
| Validate Closure Eligibility | Account Closure | 2 | Workflow Orchestration | Check Closure Eligibility, Eligibility Validation Step |
| Settle Residual Balance | Account Closure | 3 | Core Banking Processing | Disburse Residual Funds, Balance Settlement Step |
| Issue Final Statement | Account Closure | 4 | Document Management | Produce Closing Statement, Final Statement Step |
| Deactivate Account | Account Closure | 5 | Core Banking Processing | Close Account Record, Account Deactivation Step |
| Issue Dormancy Notice | Account Closure | 6 | Notification Services | Send Dormancy Notice, Dormancy Notification Step |
| Escheat Dormant Account | Account Closure | 7 | Regulatory Reporting Engine | Remit Unclaimed Property, Escheatment Step |
| Detect Insufficient Funds | Overdraft Servicing | 1 | Core Banking Processing | Identify Shortfall, Insufficient Funds Detection Step |
| Check Overdraft Opt-In | Overdraft Servicing | 2 | Core Banking Processing | Verify Opt-In Status, Opt-In Check Step |
| Evaluate Overdraft Limit | Overdraft Servicing | 3 | Core Banking Processing | Assess Overdraft Limit, Limit Evaluation Step |
| Decide Pay Or Return | Overdraft Servicing | 4 | Decision Rules Engine | Make Pay Return Decision, Pay/Return Decision Step |
| Apply Overdraft Fee | Overdraft Servicing | 5 | Core Banking Processing | Assess Overdraft Fee, Fee Application Step |
| Notify Overdraft Outcome | Overdraft Servicing | 6 | Notification Services | Send Overdraft Notice, Outcome Notification Step |
| Capture Card Application | Card Issuance | 1 | Digital Channel Platform | Take Card Application, Card Intake Step |
| Decision Card Application | Card Issuance | 2 | Credit Decisioning Engine | Approve Card Application, Issuance Decisioning Step |
| Generate Card Credential | Card Issuance | 3 | Card Processing | Generate PAN, Credential Generation Step |
| Personalize Card | Card Issuance | 4 | Card Processing | Embossing Step, Card Personalization Step |
| Fulfill Card | Card Issuance | 5 | Notification Services | Dispatch Card, Card Fulfillment Step |
| Activate Card | Card Issuance | 6 | Card Processing | Enable Card, Card Activation Step |
| Provision Wallet Token | Card Issuance | 7 | Card Processing | Tokenize Card, Wallet Provisioning Step |
| Register Dispute Claim | Dispute Resolution | 1 | Workflow Orchestration | Log Dispute, Dispute Registration Step |
| Validate Dispute Rights | Dispute Resolution | 2 | Workflow Orchestration | Check Dispute Eligibility, Rights Validation Step |
| Apply Provisional Credit | Dispute Resolution | 3 | Core Banking Processing | Issue Provisional Credit, Provisional Credit Step |
| Gather Dispute Evidence | Dispute Resolution | 4 | Document Management | Collect Evidence, Evidence Gathering Step |
| Adjudicate Dispute Outcome | Dispute Resolution | 5 | Workflow Orchestration | Decide Dispute, Outcome Adjudication Step |
| Finalize Dispute Credit | Dispute Resolution | 6 | Core Banking Processing | Finalize Credit, Dispute Closure Step |
| Receive Authorization Request | Card Transaction Authorization | 1 | Card Processing | Intake Auth Request, Authorization Intake Step |
| Validate Card Cryptogram | Card Transaction Authorization | 2 | Card Processing | Verify Cryptogram, Cryptogram Validation Step |
| Check Available Limit | Card Transaction Authorization | 3 | Card Processing | Funds Check, Limit Verification Step |
| Apply Velocity Rules | Card Transaction Authorization | 4 | Fraud Analytics | Run Fraud Rules, Velocity Check Step |
| Authorize Transaction | Card Transaction Authorization | 5 | Card Authorization | Approve Or Decline, Authorization Decision Step |
| Return Authorization Response | Card Transaction Authorization | 6 | Card Processing | Send Auth Response, Authorization Response Step |
| Post Cleared Transaction | Card Transaction Authorization | 7 | Core Banking Processing | Post Presentment, Clearing Posting Step |
| Assign Reason Code | Chargeback Processing | 1 | Card Processing | Code Chargeback, Reason Code Assignment Step |
| Raise Chargeback | Chargeback Processing | 2 | Card Processing | File Chargeback, Chargeback Submission Step |
| Receive Representment | Chargeback Processing | 3 | Workflow Orchestration | Log Representment, Representment Intake Step |
| Review Representment Evidence | Chargeback Processing | 4 | Document Management | Assess Representment, Evidence Review Step |
| Escalate To Arbitration | Chargeback Processing | 5 | Workflow Orchestration | Pre-Arbitration Step, Arbitration Escalation Step |
| Settle Chargeback | Chargeback Processing | 6 | Core Banking Processing | Resolve Chargeback, Chargeback Settlement Step |
| Triage Fraud Alert | Card Fraud Handling | 1 | Fraud Analytics | Prioritize Alert, Fraud Triage Step |
| Verify Cardholder Activity | Card Fraud Handling | 2 | Notification Services | Confirm Activity, Cardholder Verification Step |
| Block Compromised Card | Card Fraud Handling | 3 | Card Processing | Freeze Card, Card Block Step |
| Reissue Card | Card Fraud Handling | 4 | Card Processing | Replace Card, Card Reissue Step |
| Adjudicate Fraud Claim | Card Fraud Handling | 5 | Workflow Orchestration | Decide Fraud Claim, Fraud Adjudication Step |
| Refer Suspicious Activity | Card Fraud Handling | 6 | Transaction Monitoring Platform | Refer For SAR, Suspicious Activity Referral Step |
| Capture Investor Profile | Wealth Onboarding | 1 | Investment Advisory | Capture Investor Data, Investor Intake Step |
| Capture Risk Profile | Wealth Onboarding | 2 | Investment Advisory | Profile Risk, Risk Profiling Step |
| Assess Investor Suitability | Wealth Onboarding | 3 | Investment Advisory | Suitability Check Step, Best Interest Step |
| Open Investment Account | Wealth Onboarding | 4 | Portfolio Management | Establish Investment Account, Account Opening Step |
| Execute Advisory Mandate | Wealth Onboarding | 5 | Portfolio Management | Sign Mandate, Mandate Execution Step |
| Fund Investment Account | Wealth Onboarding | 6 | Portfolio Management | Initial Investment Funding, Account Funding Step |
| Capture Client Goals | Financial Planning | 1 | Investment Advisory | Client Fact Find Step, Goal Capture Step |
| Determine Risk Tolerance | Financial Planning | 2 | Investment Advisory | Risk Tolerance Step, Determine Risk Appetite |
| Formulate Investment Plan | Financial Planning | 3 | Investment Advisory | Construct Plan Step, Plan Formulation Step |
| Confirm Suitability | Financial Planning | 4 | Investment Advisory | Suitability Confirmation Step, Best Interest Check Step |
| Draft Investment Policy Statement | Financial Planning | 5 | Investment Advisory | Draft IPS Step, IPS Drafting Step |
| Agree Investment Plan | Financial Planning | 6 | Investment Advisory | Agree Plan Step, IPS Sign-Off Step |
| Measure Portfolio Drift | Portfolio Rebalancing | 1 | Portfolio Management | Drift Measurement Step, Measure Allocation Drift |
| Evaluate Drift Threshold | Portfolio Rebalancing | 2 | Portfolio Management | Threshold Evaluation Step, Tolerance Check Step |
| Generate Rebalance Proposal | Portfolio Rebalancing | 3 | Portfolio Management | Rebalance Proposal Step, Propose Rebalance Step |
| Run Pre-Trade Compliance | Portfolio Rebalancing | 4 | Portfolio Management | Pre-Trade Compliance Step, Compliance Screening Step |
| Approve Rebalance Plan | Portfolio Rebalancing | 5 | Portfolio Management | Rebalance Approval Step, Sign Off Rebalance Step |
| Raise Rebalance Orders | Portfolio Rebalancing | 6 | Brokerage & Trading | Raise Orders Step, Order Generation Step |
| Capture Order | Trade Order Management | 1 | Brokerage & Trading | Order Capture Step, Intake Order Step |
| Validate Order | Trade Order Management | 2 | Brokerage & Trading | Order Validation Step, Pre-Trade Validation Step |
| Route Order | Trade Order Management | 3 | Brokerage & Trading | Order Routing Step, Venue Selection Step |
| Execute Order | Trade Order Management | 4 | Brokerage & Trading | Order Execution Step, Fill Capture Step |
| Confirm Trade | Trade Order Management | 5 | Brokerage & Trading | Trade Confirmation Step |
| Allocate Fills | Trade Order Management | 6 | Brokerage & Trading | Trade Allocation Step, Block Allocation Step |
| Settle Trade | Trade Order Management | 7 | Brokerage & Trading | Securities Settlement Step, Settle Securities Trade Step |
| Value Portfolio | Performance Reporting | 1 | Portfolio Management | Portfolio Valuation Step, Mark-to-Market Step |
| Process Corporate Actions | Performance Reporting | 2 | Portfolio Management | Corporate Actions Step, Entitlement Processing Step |
| Reconcile Positions | Performance Reporting | 3 | Portfolio Management | Position Reconciliation Step, Book Recon Step |
| Calculate Returns | Performance Reporting | 4 | Portfolio Management | Return Calculation Step, TWR Calculation Step |
| Compute Attribution | Performance Reporting | 5 | Portfolio Management | Attribution Analysis Step, Benchmark Comparison Step |
| Produce Performance Report | Performance Reporting | 6 | Portfolio Management | Report Production Step, Report Delivery Step |
| Ingest Transaction Stream | Fraud Detection | 1 | Data Streaming | Capture Event Stream, Stream Ingestion Step |
| Screen Transaction Risk | Fraud Detection | 2 | Fraud Analytics | Score Transaction Risk, Risk Screening Step |
| Generate Fraud Alert | Fraud Detection | 3 | Fraud Analytics | Raise Fraud Alert, Alert Generation Step |
| Apply Detection Block | Fraud Detection | 4 | Fraud Analytics | Block Or Allow, Detection Block Step |
| Route Fraud Alert | Fraud Detection | 5 | Workflow Orchestration | Dispatch Alert, Alert Routing Step |
| Adjudicate Fraud Alert | Fraud Investigation | 1 | Case Management | Triage Alert, Alert Adjudication Step |
| Open Fraud Case | Fraud Investigation | 2 | Case Management | Create Case, Case Opening Step |
| Investigate Fraud Case | Fraud Investigation | 3 | Case Management | Examine Fraud Case, Fraud Investigation Step |
| Recover Fraud Loss | Fraud Investigation | 4 | Core Banking Processing | Recover Funds, Loss Recovery Step |
| File Suspicious Activity Report | Fraud Investigation | 5 | Transaction Monitoring Platform | File SAR, Suspicious Activity Filing Step |
| Feed Detection Models | Fraud Investigation | 6 | Machine Learning Platform | Tune Detection Models, Feedback Loop Step |
| Define Risk Capacity | Risk Appetite Setting | 1 | Enterprise Risk Management | Assess Risk Capacity, Capacity Definition Step |
| Draft Appetite Statement | Risk Appetite Setting | 2 | Enterprise Risk Management | Author RAS, Appetite Drafting Step |
| Cascade Risk Limits | Risk Appetite Setting | 3 | Analytics Platform | Set Risk Limits, Limit Cascade Step |
| Approve Risk Appetite | Risk Appetite Setting | 4 | Workflow Orchestration | Set Risk Appetite, Appetite Approval Step |
| Embed Appetite Limits | Risk Appetite Setting | 5 | Workflow Orchestration | Operationalize Appetite, Appetite Embedding Step |
| Identify Risk Event | Risk Identification & Assessment | 1 | Operational Risk Management | Spot Risk, Risk Identification Step |
| Register Risk Item | Risk Identification & Assessment | 2 | Workflow Orchestration | Log Risk, Risk Registration Step |
| Score Inherent Risk | Risk Identification & Assessment | 3 | Analytics Platform | Rate Inherent Risk, Inherent Scoring Step |
| Evaluate Residual Risk | Risk Identification & Assessment | 4 | Analytics Platform | Assess Residual Risk, Residual Evaluation Step |
| Assign Risk Treatment | Risk Identification & Assessment | 5 | Workflow Orchestration | Decide Risk Response, Treatment Assignment Step |
| Track Risk Remediation | Risk Identification & Assessment | 6 | Workflow Orchestration | Monitor Remediation, Remediation Tracking Step |
| Design Stress Scenario | Stress Testing | 1 | Analytics Platform | Build Scenario, Scenario Design Step |
| Validate Risk Models | Stress Testing | 2 | Machine Learning Platform | Govern Models, Model Validation Step |
| Project Capital Impact | Stress Testing | 3 | Analytics Platform | Run Stress Models, Capital Projection Step |
| Assess Capital Adequacy | Stress Testing | 4 | Analytics Platform | Evaluate Capital Adequacy, Adequacy Assessment Step |
| Obtain Board Approval | Stress Testing | 5 | Workflow Orchestration | Approve Capital Plan, Board Sign-Off Step |
| Submit Capital Plan | Stress Testing | 6 | Regulatory Reporting Engine | Submit CCAR Plan, Capital Plan Submission Step |
| Aggregate Risk Exposure | Risk Reporting | 1 | Data Warehousing | Aggregate Exposure, Risk Aggregation Step |
| Reconcile Risk Data | Risk Reporting | 2 | Data Governance | Validate Risk Data, Data Reconciliation Step |
| Compare Against Limits | Risk Reporting | 3 | Analytics Platform | Check Limit Utilisation, Limit Comparison Step |
| Escalate Limit Breach | Risk Reporting | 4 | Workflow Orchestration | Raise Breach, Breach Escalation Step |
| Compile Risk Report | Risk Reporting | 5 | Analytics Platform | Produce Risk Report, Report Compilation Step |
| Distribute Risk Report | Risk Reporting | 6 | Regulatory Reporting Engine | Deliver Risk Report, Report Distribution Step |
| Collect KYC Documents | KYC Verification | 1 | Intelligent Document Processing | Gather KYC Documents, KYC Intake Step |
| Validate Customer Identity | KYC Verification | 2 | Identity Verification | Prove Customer Identity |
| Screen Against Watchlists | KYC Verification | 3 | Sanctions Screening | Run KYC Screening |
| Compile KYC Profile | KYC Verification | 4 | KYC Management | Build KYC Profile, Profile Compilation Step |
| Approve KYC Outcome | KYC Verification | 5 | Workflow Orchestration | Decide KYC Outcome, KYC Approval Step |
| Schedule KYC Review | KYC Verification | 6 | KYC Management | Set KYC Review, Review Scheduling Step |
| Triage AML Alert | Suspicious Activity Reporting | 1 | Transaction Monitoring Platform | Screen AML Alert, Alert Triage Step |
| Open Investigation Case | Suspicious Activity Reporting | 2 | Transaction Monitoring Platform | Create AML Case |
| Analyse Transaction Pattern | Suspicious Activity Reporting | 3 | Transaction Monitoring | Examine Transactions, Pattern Analysis Step |
| Determine Suspicion | Suspicious Activity Reporting | 4 | Governance Risk & Compliance Platform | Decide Suspicion, Suspicion Decision Step |
| Lodge SAR Filing | Suspicious Activity Reporting | 5 | Regulatory Reporting Engine | Submit SAR, SAR Filing Step |
| Notify Financial Intelligence | Suspicious Activity Reporting | 6 | Regulatory Reporting Engine | Confirm SAR, FIU Notification Step |
| Identify Filing Obligation | Regulatory Filing | 1 | Regulatory Compliance | Determine Filing, Obligation Identification Step |
| Aggregate Filing Data | Regulatory Filing | 2 | Data Warehousing | Gather Filing Data, Data Aggregation Step (Filing) |
| Compile Regulatory Return | Regulatory Filing | 3 | Regulatory Reporting Engine | Build Return, Return Compilation Step |
| Validate Filing Quality | Regulatory Filing | 4 | Regulatory Reporting Engine | Review Return, Filing Validation Step |
| Submit Regulatory Return | Regulatory Filing | 5 | Regulatory Reporting Engine | File Return, Return Submission Step |
| Archive Filing Record | Regulatory Filing | 6 | Document Management | Retain Filing, Filing Archival Step |
| Capture CIP Data | Customer Due Diligence Onboarding | 1 | Customer Due Diligence | Collect CIP Data, CIP Capture Step |
| Identify Beneficial Owner | Customer Due Diligence Onboarding | 2 | Customer Due Diligence | Capture UBO, Beneficial Ownership Step |
| Screen CDD Parties | Customer Due Diligence Onboarding | 3 | Sanctions Screening | Diligence Screening, CDD Screening Step |
| Rate Customer Risk | Customer Due Diligence Onboarding | 4 | Governance Risk & Compliance Platform | Score Customer Risk, Risk Rating Step |
| Trigger Enhanced Diligence | Customer Due Diligence Onboarding | 5 | Customer Due Diligence | Perform EDD, Enhanced Diligence Step |
| Approve CDD Outcome | Customer Due Diligence Onboarding | 6 | Workflow Orchestration | Decide CDD Outcome, CDD Approval Step |
| Establish CDD Profile | Customer Due Diligence Onboarding | 7 | KYC Management | Create CDD Profile, Profile Establishment Step |
| Match Against Watchlist | Sanctions Screening Operations | 1 | Sanctions Screening | Run Watchlist Match, Watchlist Matching Step |
| Generate Sanctions Alert | Sanctions Screening Operations | 2 | Payment Sanctions Filter | Raise Sanctions Alert, Alert Generation Step (Sanctions) |
| Triage Potential Match | Sanctions Screening Operations | 3 | Governance Risk & Compliance Platform | Screen Potential Match, L1 Triage Step |
| Resolve Sanctions Hit | Sanctions Screening Operations | 4 | Governance Risk & Compliance Platform | Adjudicate Sanctions Hit, Hit Resolution Step |
| Confirm Sanctions Block | Sanctions Screening Operations | 5 | Payment Sanctions Filter | Approve Sanctions Block, Block Confirmation Step |
| Report Sanctions Block | Sanctions Screening Operations | 6 | Regulatory Reporting Engine | File Sanctions Report, Block Reporting Step |
| Scan Regulatory Change | Regulatory Change Management | 1 | Regulatory Compliance | Horizon Scan, Regulatory Scanning Step |
| Map Regulatory Obligation | Regulatory Change Management | 2 | Governance Risk & Compliance Platform | Map Obligation, Obligation Mapping Step |
| Assess Regulatory Impact | Regulatory Change Management | 3 | Governance Risk & Compliance Platform | Evaluate Change Impact, Regulatory Impact Assessment Step |
| Plan Change Remediation | Regulatory Change Management | 4 | Workflow Orchestration | Plan Remediation, Remediation Planning Step |
| Implement Compliance Control | Regulatory Change Management | 5 | Policy & Control Management | Embed Compliance Change, Control Implementation Step |
| Attest Change Compliance | Regulatory Change Management | 6 | Governance Risk & Compliance Platform | Sign Off Change, Change Attestation Step |
| Open Branch Cash | Branch Operations | 1 | Branch Banking | Branch Opening, Float Issuance |
| Serve Counter Customer | Branch Operations | 2 | Branch Banking | Counter Service, Customer Identification |
| Process Teller Transaction | Branch Operations | 3 | Core Banking Processing | Teller Posting, Transaction Execution |
| Replenish Teller Drawer | Branch Operations | 4 | Branch Banking | Drawer Buy/Sell, Cash Transfer |
| Balance Teller Drawer | Branch Operations | 5 | Branch Banking | Drawer Balancing, Teller Recon |
| Reconcile Branch Cash | Branch Operations | 6 | Branch Banking | Branch Balancing, EOD Recon |
| Close Branch | Branch Operations | 7 | Branch Banking | Branch Closing, EOD Close |
| Start Digital Application | Digital Onboarding Journey | 1 | Digital Banking | Begin Online Application, Start DAO |
| Capture Applicant Details | Digital Onboarding Journey | 2 | Digital Banking | Capture Application Data, Applicant Capture |
| Verify Digital Identity | Digital Onboarding Journey | 3 | Identity Proofing Service | Run eKYC, Digital ID Proofing |
| Enrol Strong Authentication | Digital Onboarding Journey | 4 | Customer Authentication | Enrol SCA, Set Up MFA |
| Fund Digital Account | Digital Onboarding Journey | 5 | Payment Orchestration | Fund Online Account, First Deposit Capture |
| Activate Digital Channel | Digital Onboarding Journey | 6 | Notification Services | Channel Activation, Welcome Enablement |
| Open Channel Session | Channel Servicing | 1 | Channel Management | Start Channel Session, Session Init |
| Authenticate Channel User | Channel Servicing | 2 | Customer Authentication | Channel User Authentication, Step-Up Auth |
| Identify Service Intent | Channel Servicing | 3 | Conversational AI | Intent Detection, Need Identification |
| Orchestrate Channel Journey | Channel Servicing | 4 | Integration Platform | Channel Routing, Cross-Channel Orchestration |
| Resolve Self-Service Request | Channel Servicing | 5 | Core Banking Processing | In-Channel Resolution, Self-Serve Action |
| Escalate To Assisted Servicing | Channel Servicing | 6 | Workflow Orchestration | Assisted Escalation, Warm Transfer |
| Record Channel Interaction | Channel Servicing | 7 | CRM Platform | Log Interaction, Capture Channel Activity |
| Forecast ATM Demand | ATM Cash Servicing | 1 | ATM Management | Cash Forecasting (ATM), Per-Terminal Forecast |
| Plan Cash Order | ATM Cash Servicing | 2 | ATM Management | Cash Order Planning, Load Planning |
| Schedule Cash Delivery | ATM Cash Servicing | 3 | Integration Platform | CIT Scheduling, Delivery Scheduling |
| Replenish ATM Cash | ATM Cash Servicing | 4 | ATM Management | ATM Replenishment, Cassette Loading |
| Reconcile ATM Cash | ATM Cash Servicing | 5 | Core Banking Processing | ATM Reconciliation, Cash Balancing (ATM) |
| Resolve Cash Discrepancy | ATM Cash Servicing | 6 | Workflow Orchestration | Cash Variance Resolution, Exception Handling (ATM) |
| Capture IVR Selection | Contact Centre Interaction | 1 | Contact Center | IVR Capture, Menu Selection |
| Authenticate Caller | Contact Centre Interaction | 2 | Customer Authentication | Caller Authentication, Voice Verification |
| Route Interaction | Contact Centre Interaction | 3 | Contact Center Platform | Distribute Interaction, Skills Routing Step |
| Handle Customer Interaction | Contact Centre Interaction | 4 | Contact Center Platform | Interaction Handling, Call Handling |
| Wrap Up Interaction | Contact Centre Interaction | 5 | CRM Platform | After-Call Work, Disposition & Notes |
| Score Interaction Quality | Contact Centre Interaction | 6 | Contact Center Platform | QA Scoring, Quality Review |
| Close Subledgers | Financial Close | 1 | General Ledger Accounting | Cut Off Period, Close Sub-Ledgers |
| Post Closing Journals | Financial Close | 2 | General Ledger Accounting | Post Adjusting Entries, Book Period-End Journals |
| Reconcile Ledger Accounts | Financial Close | 3 | General Ledger Accounting | Reconcile GL, Account Reconciliation (Close) |
| Eliminate Intercompany Balances | Financial Close | 4 | Financial Reporting | Eliminate IC, IC Balance Elimination |
| Run Consolidation | Financial Close | 5 | Financial Reporting | Consolidate Group, Process Consolidation |
| Prepare Consolidated Statements | Financial Close | 6 | Financial Reporting | Prepare Group Accounts, Draft Statements |
| Certify Period Close | Financial Close | 7 | Financial Reporting | Sign Off Close, Close Sign-Off |
| Build Operating Budget | Management Reporting | 1 | Financial Reporting | Construct Budget, Prepare Budget |
| Approve Budget Plan | Management Reporting | 2 | Financial Reporting | Lock Budget, Sign Off Budget |
| Roll Forward Forecast | Management Reporting | 3 | Financial Reporting | Update Forecast, Reforecast |
| Capture Actual Results | Management Reporting | 4 | Financial Reporting | Load Actuals, Capture Actuals |
| Analyse Budget Variance | Management Reporting | 5 | Financial Reporting | Explain Variance, Budget Variance Analysis |
| Compile Management Accounts | Management Reporting | 6 | Financial Reporting | Build MI Pack, Prepare Management Accounts |
| Present Board Pack | Management Reporting | 7 | Financial Reporting | Distribute MI Pack, Board Sign-Off |
| Source Regulatory Data | Regulatory Capital Reporting | 1 | Regulatory Capital Management | Gather Capital Data, Ingest Reg Data |
| Calculate RWA | Regulatory Capital Reporting | 2 | Regulatory Capital Management | Compute RWA, Calculate Risk-Weighted Assets |
| Determine Own Funds | Regulatory Capital Reporting | 3 | Regulatory Capital Management | Compute Own Funds, Determine Capital Base |
| Assemble Capital Return | Regulatory Capital Reporting | 4 | Regulatory Capital Management | Build Capital Return, Compile COREP |
| Validate Return Quality | Regulatory Capital Reporting | 5 | Regulatory Capital Management | Validate COREP, Run Taxonomy Checks |
| Attest Capital Return | Regulatory Capital Reporting | 6 | Regulatory Capital Management | Sign Off Capital Return, Attest FR Y-14 |
| Submit Capital Return | Regulatory Capital Reporting | 7 | Regulatory Capital Management | File Capital Return, Submit COREP |
| Aggregate Cash Balances | Cash & Liquidity Management | 1 | Liquidity Management | Aggregate Nostro Balances, Consolidate Cash |
| Project Liquidity Position | Cash & Liquidity Management | 2 | Liquidity Management | Forecast Liquidity, Project Cash Position |
| Assess Liquidity Buffers | Cash & Liquidity Management | 3 | Liquidity Management | Check Liquidity Limits, Assess LCR Buffer |
| Decide Funding Action | Cash & Liquidity Management | 4 | Liquidity Management | Decide Funding, Determine Funding Action |
| Execute Funding Action | Cash & Liquidity Management | 5 | Liquidity Management | Execute Funding, Place Funds |
| Reconcile End-Of-Day Cash | Cash & Liquidity Management | 6 | Liquidity Management | EOD Cash Reconciliation, Reconcile Nostro |
| Report Liquidity Position | Cash & Liquidity Management | 7 | Liquidity Management | Produce Liquidity Report, Report Liquidity |
| Assemble Market Curves | Funds Transfer Pricing | 1 | Asset Liability Management | Gather Market Curves, Assemble Funding Curves |
| Build FTP Curve | Funds Transfer Pricing | 2 | Asset Liability Management | Construct FTP Curve, Build Transfer Curve |
| Set Behavioural Assumptions | Funds Transfer Pricing | 3 | Asset Liability Management | Define Behavioural Assumptions, Set FTP Assumptions |
| Approve FTP Methodology | Funds Transfer Pricing | 4 | Asset Liability Management | ALCO FTP Approval, Approve Transfer Curve |
| Apply Transfer Rates | Funds Transfer Pricing | 5 | Asset Liability Management | Apply FTP Rates, Assign Transfer Rates |
| Attribute Net Margin | Funds Transfer Pricing | 6 | Asset Liability Management | Attribute NIM, Allocate Net Margin |
| Report FTP Outcome | Funds Transfer Pricing | 7 | Asset Liability Management | Report Transfer Pricing, Publish FTP Results |

## Supporting concepts

| Canonical Name | Type | Aliases |
|---|---|---|
| Payment Operations Analyst | role | Payment Ops Analyst, Payments Operator |
| Clearing Operations Specialist | role | Clearing Operator, Rail Operations Specialist |
| Compliance Screening Officer | role | Sanctions Officer, Screening Analyst |
| Settlement Officer | role | Settlements Officer, Settlement Clerk |
| Reconciliation Analyst | role | Recon Analyst, Reconciliations Specialist |
| Treasury Cash Manager | role | Cash Manager, Liquidity Manager |
| Payment Initiated Event | event | Payment Received Event, Instruction Received |
| Settlement Received Event | event | Settlement Advice Event, Settlement Notified |
| Reconciliation Break Event | event | Break Raised Event, Exception Raised |
| Cut-Off Reached Event | event | Cut-Off Event, Window Closed Event |
| Payment Instruction | artifact | Payment Order Request, Pain.001 Message |
| Clearing Message | artifact | Pacs.008 Message, ACH Entry |
| Settlement File | artifact | Settlement Advice, Settlement Report |
| Bank Statement Message | artifact | Camt.053 Statement, Account Statement |
| Cash Forecast | artifact | Liquidity Forecast Report, Cash Flow Forecast |
| Reconciliation Report | artifact | Recon Report, Reconciliation Certificate |
| Onboarding Specialist | role | Onboarding Officer, New Accounts Officer |
| KYC Analyst | role | KYC Officer, Due Diligence Analyst |
| Complaints Officer | role | Complaint Handler, Dispute Resolution Officer |
| Service Advisor | role | Customer Service Agent, Service Desk Agent |
| Quality Assurance Reviewer | role | QA Analyst, Complaints QA Reviewer |
| Application Submitted Event | event | Onboarding Started Event, Application Received |
| Customer Activated Event | event | Onboarding Completed Event, Account Activated |
| Complaint Received Event | event | Complaint Raised Event, Complaint Logged |
| Service Request Raised Event | event | Request Submitted Event, Ticket Raised |
| SLA Breach Event | event | SLA Escalation Event, Deadline Breached |
| Customer Application | artifact | Onboarding Application, Account Application |
| Onboarding Case | artifact | Onboarding Record, Onboarding File |
| KYC Profile | artifact | CDD Profile, Customer Risk Profile |
| Consent Record | artifact | Consent Artifact, Opt-In Record |
| Complaint Record | artifact | Complaint Case, Complaint File |
| Final Response Letter | artifact | Final Response, FRL |
| Service Request Ticket | artifact | Service Ticket, Request Ticket |
| Loan Officer | role | Loan Originator, Lending Officer |
| Loan Processor | role | Loan Processing Clerk, File Processor |
| Credit Underwriter | role | Underwriter, Credit Analyst |
| Mortgage Loan Originator | role | MLO, Mortgage Consultant |
| Mortgage Closer | role | Closing Officer, Funder |
| Collections Agent | role | Collector, Arrears Agent |
| Recovery Officer | role | Recoveries Officer, Recovery Specialist |
| Trade Finance Officer | role | Trade Finance Specialist, LC Officer |
| Loan Application Submitted Event | event | Application Received Event, Origination Started Event |
| Credit Decision Issued Event | event | Decision Rendered Event, Adjudication Complete Event |
| Loan Funded Event | event | Disbursement Event, Loan Booked Event |
| Loan Charged Off Event | event | Charge-Off Event, Write-Off Event |
| Trade Settlement Event | event | LC Settled Event, Presentation Honored Event |
| Loan Application | artifact | Credit Application, Loan Request |
| Credit Report | artifact | Bureau Report, Credit File |
| Credit Decision | artifact | Underwriting Outcome, Adjudication Record |
| Loan Agreement | artifact | Credit Agreement, Promissory Note |
| Collateral Appraisal | artifact | Property Appraisal, Valuation Report |
| Letter Of Credit | artifact | Documentary Credit, LC |
| Deposit Operations Clerk | role | Deposit Ops Clerk, Account Servicing Clerk |
| Statement Production Officer | role | Statement Officer, Statement Production Clerk |
| Overdraft Operations Analyst | role | Overdraft Analyst, NSF Operations Analyst |
| Unclaimed Property Officer | role | Escheatment Officer, Dormancy Officer |
| Account Opened Event | event | Account Established Event, New Account Opened |
| Statement Issued Event | event | Statement Generated Event, Statement Delivered Event |
| Account Dormant Event | event | Dormancy Triggered Event, Inactivity Detected Event |
| Account Closed Event | event | Account Closure Event, Account Terminated Event |
| Overdraft Triggered Event | event | Insufficient Funds Event, NSF Triggered Event |
| Account Opening Form | artifact | Account Application Form, New Account Form |
| Signature Card | artifact | Signatory Mandate, Account Mandate Card |
| Bank Account Statement | artifact | Account Statement, Periodic Statement |
| Service Maintenance Request | artifact | Account Maintenance Request, Servicing Request |
| Account Closure Request | artifact | Closure Request, Close Account Application |
| Dormancy Notice | artifact | Abandoned Property Letter, Pre-Escheatment Notice |
| Reg E Opt-In Record | artifact | Overdraft Opt-In Record, Reg E Consent |
| Overdraft Fee | artifact | OD Fee, Insufficient Funds Fee |
| Card Issuance Officer | role | Card Issuing Officer, Card Operations Officer |
| Card Operations Analyst | role | Card Auth Analyst, Authorization Operations Analyst |
| Dispute Resolution Specialist | role | Chargeback Analyst, Disputes Specialist |
| Card Fraud Analyst | role | Card Fraud Investigator, Card Fraud Operations Analyst |
| Card Issued Event | event | Card Activated Event, Card Provisioned Event |
| Authorization Approved Event | event | Auth Approved Event, Authorization Granted Event |
| Chargeback Raised Event | event | Chargeback Filed Event, Dispute Raised Event |
| Dispute Resolved Event | event | Dispute Closed Event, Chargeback Settled Event |
| Fraud Detected Event | event | Card Fraud Event, Fraud Confirmed Event |
| Card Account Application | artifact | Card Product Application, Card Onboarding Application |
| Card Credential | artifact | Card Number Credential, PAN Credential |
| Authorization Request | artifact | Auth Request Message, ISO 8583 Auth Request |
| Chargeback Case | artifact | Dispute Case, Chargeback Record |
| Card Statement | artifact | Credit Card Statement, Card Billing Statement |
| Fraud Alert | artifact | Fraud Case Alert, Suspicious Transaction Alert |
| Financial Advisor | role | Wealth Advisor, Investment Adviser |
| Portfolio Manager | role | PM, Discretionary Manager |
| Wealth Relationship Manager | role | Private Banker, Wealth RM |
| Trader | role | Dealer, Execution Trader |
| Settlement Operations Officer | role | Securities Settlement Officer, Middle Office Operations |
| Performance Analyst | role | Investment Reporting Analyst, Performance Measurement Analyst |
| Investment Plan Agreed Event | event | IPS Signed Event, Plan Agreed Event |
| Rebalance Triggered Event | event | Drift Breach Event, Rebalance Trigger Event |
| Order Placed Event | event | Order Raised Event, Order Submitted Event |
| Trade Executed Event | event | Order Filled Event, Execution Event |
| Corporate Action Announced Event | event | CA Announced Event, Issuer Event |
| Investment Policy Statement | artifact | IPS, Investment Mandate Statement |
| Risk Profile | artifact | Investor Risk Profile, Risk Tolerance Profile |
| Order Ticket | artifact | Trade Order, Deal Ticket |
| Trade Confirmation | artifact | Trade Confirm, Contract Note |
| Performance Report | artifact | Investment Performance Report, Client Statement (Investments) |
| Chief Risk Officer | role | CRO, Head of Risk |
| Risk Analyst | role | Operational Risk Analyst, Risk Officer |
| Stress Testing Lead | role | Stress Test Manager, Capital Stress Lead |
| Risk Reporting Manager | role | Risk MI Manager, RDARR Lead |
| Fraud Detection Analyst | role | Fraud Monitoring Analyst, Detection Analyst |
| Fraud Investigator | role | Fraud Case Investigator, Financial Crime Investigator |
| Risk Appetite Approved Event | event | RAS Approved Event, Appetite Set Event |
| Risk Identified Event | event | New Risk Event, Risk Registered Event |
| Limit Breach Event | event | Appetite Breach Event, Threshold Breach Event |
| Stress Test Completed Event | event | Stress Cycle Completed Event, CCAR Submitted Event |
| Fraud Alert Raised Event | event | Alert Raised Event, Fraud Flag Event |
| Fraud Case Closed Event | event | Fraud Resolved Event, Case Closed Event (Fraud) |
| Risk Appetite Statement | artifact | RAS, Risk Appetite Framework Statement |
| Risk Register | artifact | Risk Log, Risk Inventory |
| Stress Scenario | artifact | Scenario Definition, Macro Stress Scenario |
| Stress Test Result | artifact | Stress Result, Capital Projection Result |
| Risk Report | artifact | Board Risk Report, Risk MI Pack |
| Fraud Case | artifact | Fraud Investigation Case, Fraud Case File |
| AML Compliance Officer | role | BSA Officer, CDD Officer, Onboarding AML Officer |
| AML Investigator | role | AML Analyst, Transaction Monitoring Investigator |
| MLRO | role | Money Laundering Reporting Officer, BSA/AML Compliance Officer |
| Regulatory Reporting Analyst | role | Reg Reporting Analyst, Compliance Reporting Analyst |
| Regulatory Change Manager | role | Reg Change Manager, Compliance Change Lead |
| Customer Risk Rated Event | event | CDD Completed Event, Risk Rating Assigned Event |
| KYC Profile Verified Event | event | KYC Completed Event, KYC Verified Event |
| Suspicious Activity Detected Event | event | Suspicion Confirmed Event, SAR Triggered Event |
| Sanctions Alert Event | event | Sanctions Match Event, Watchlist Hit Event |
| Regulatory Obligation Updated Event | event | Reg Change Embedded Event, Obligation Updated Event |
| Regulatory Filing Submitted Event | event | Filing Submitted Event, Return Filed Event |
| Customer Risk Score | artifact | CDD Risk Score, Customer Risk Tier |
| Sanctions Hit | artifact | Watchlist Match, Sanctions Match Alert |
| SAR Filing | artifact | Suspicious Activity Report, FinCEN Form 111 |
| CTR Filing | artifact | Currency Transaction Report, FinCEN Form 112 |
| Regulatory Obligation | artifact | Compliance Obligation, Regulatory Requirement |
| Teller | role | Bank Teller, Counter Clerk |
| Branch Manager | role | Branch Supervisor, Head Teller |
| Digital Onboarding Specialist | role | Digital Onboarding Officer, DAO Specialist |
| Channel Operations Analyst | role | Channel Ops Analyst, Omnichannel Analyst |
| ATM Custodian | role | ATM Cash Officer, ATM Operations Custodian |
| Contact Centre Agent | role | Call Centre Agent, Customer Service Representative |
| Session Started Event | event | Channel Session Opened Event, Session Init Event |
| Digital Application Submitted Event | event | Online Application Submitted Event, DAO Submitted Event |
| Interaction Captured Event | event | Contact Received Event, Interaction Logged Event |
| ATM Replenishment Due Event | event | Cash-Out Forecast Event, Replenishment Triggered Event |
| Cash Variance Event | event | Cash Discrepancy Event, ATM Variance Event |
| Digital Application | artifact | Online Application, DAO Application |
| Channel Session | artifact | Customer Session, Omnichannel Session |
| Interaction Record | artifact | Contact Record, Interaction Log |
| ATM Cash Forecast | artifact | ATM Demand Forecast, Cash Load Forecast |
| ATM Replenishment Record | artifact | Cash Load Record, ATM Load Sheet |
| Financial Controller | role | Group Financial Controller, Head of Financial Control |
| FP&A Manager | role | Head of FP&A, Planning & Analysis Manager |
| Regulatory Reporting Specialist | role | Prudential Reporting Analyst, Capital Reporting Specialist |
| Treasury Analyst | role | Liquidity Analyst, Treasury Operations Analyst |
| ALM Analyst | role | Asset-Liability Analyst, FTP Analyst |
| Period Close Initiated Event | event | Close Started Event, Period-End Triggered Event |
| Reporting Deadline Reached Event | event | Remittance Deadline Event, Reporting Cut-Off Event |
| Liquidity Limit Breach Event | event | Liquidity Breach Event, Buffer Breach Event |
| FTP Curve Approved Event | event | Curve Approved Event, ALCO Approval Event |
| Trial Balance | artifact | Adjusted Trial Balance, TB |
| Journal Entry | artifact | Adjusting Journal, GL Journal |
| Consolidated Financial Statements | artifact | Group Accounts, Consolidated Accounts |
| Management Accounts | artifact | Board MI Pack, Management Reporting Pack |
| Capital Adequacy Return | artifact | Prudential Return, COREP Return |
| Liquidity Position | artifact | Cash Position, Intraday Position |
| FTP Curve | artifact | Transfer Pricing Curve, Funding Curve |
