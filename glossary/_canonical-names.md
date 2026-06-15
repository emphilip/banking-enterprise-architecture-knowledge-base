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
| Financial Reporting | L2 | Finance & Treasury | Finance Management | Management Reporting |
| Regulatory Capital Management | L2 | Finance & Treasury | Finance Management | Capital Management |
| Treasury Management | L1 | Finance & Treasury | — | Treasury |
| Liquidity Management | L2 | Finance & Treasury | Treasury Management | Cash & Liquidity |
| Asset Liability Management | L2 | Finance & Treasury | Treasury Management | ALM |
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
| Behavioural Analytics | L3 | Customer Management | Customer Segmentation | Behavioral Analytics, Customer Event Analytics, Behavioural Modelling |
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
| Contact Routing Management | L4 | Customer Management | Contact Dialogue Management | Interaction Routing, Skills-Based Routing |
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
| Suspicious Activity Reporting | Compliance & Financial Crime | Transaction Monitoring | SAR Filing |
| Regulatory Filing | Compliance & Financial Crime | Regulatory Reporting | Regulatory Submission |
| Statement Generation | Deposits & Accounts | Account Servicing | Statement Production |
| Reconciliation & Settlement | Payments | Payment Clearing & Settlement | Recon & Settlement |
| Complaint Handling | Customer Management | Customer Servicing, Case Management | Complaints Process |
| Service Request Handling | Customer Management | Customer Servicing, Case Management | Service Requests |
| Branch Operations | Channels & Engagement | Branch Banking | Branch Process |
| Trade Finance Processing | Lending & Credit | Collateral Management | Trade Finance |
| Cash Management | Payments | Payment Execution, Liquidity Management | Corporate Cash Management |
| Wealth Onboarding | Wealth & Investments | Portfolio Management, Customer Acquisition | Investor Onboarding |

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

## Modern systems

Format: Canonical Name | Realizes (tech cap depends_on it) | Supersedes (legacy) | Vendor | Aliases

| Canonical Name | Realizes (tech cap) | Supersedes | Vendor | Aliases |
|---|---|---|---|---|
| Thought Machine Vault | Core Banking Processing | Temenos T24; Oracle FLEXCUBE | Thought Machine | Vault, Vault Core |
| Mambu | Core Banking Processing | Fiserv DNA; Jack Henry SilverLake | Mambu | Mambu Core |
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
| MeridianLink | Loan Origination Platform | Ellie Mae Encompass | MeridianLink | MeridianLink Consumer, MeridianLink Opening |
| Provenir | Credit Decisioning Engine | FICO Origination Manager; Experian PowerCurve | Provenir | Provenir AI, Provenir Decisioning |

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
| Evaluate Collateral | Credit Underwriting | 4 | Credit Decisioning Engine | Security Evaluation Step, Collateral Review |
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
