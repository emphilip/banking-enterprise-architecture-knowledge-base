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
