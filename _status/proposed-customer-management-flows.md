---
id: proposed-customer-management-flows
title: Proposed Customer Management Process-Flow Decomposition
type: proposal
status: draft
author: apqc-process research sub-agent
date: 2026-06-15
---

# Proposed Customer Management Process-Flow Decomposition

Multi-granularity process-flow decomposition for the three existing
Customer-Management-domain processes: **Customer Onboarding**, **Complaint Handling**,
and **Service Request Handling**.

Grounded in APQC PCF Banking ("Develop and Manage Customers" / "6.0 Manage Customer
Service"), banking KYC/CDD onboarding practice (CIP, CDD, EDD, ongoing monitoring),
FCA DISP (acknowledge / investigate / final response / root-cause / redress), CFPB
company complaint process (15-day initial / 60-day final response), ISO 10002
(receipt, acknowledgement, assessment, resolution, closure), and ITIL 4 Service
Request Management (triage, priority/SLA, fulfilment, closure).

Relationship verbs used: `defined_in`, `derived_from`, `supersedes`, `related_to`,
`depends_on`, `causes`, `mentions`. Steps are filed as
`process-flows/<kebab-process>/NN-<kebab-step>.md`.

All canonical names below are checked against `glossary/_canonical-names.md` and are new
(no collisions with existing domains, capabilities, processes, technology capabilities,
systems, or Payments-domain steps/roles/artifacts). Step names use verb form to stay
distinct from capability names.

Kebab process folders: `customer-onboarding`, `complaint-handling`,
`service-request-handling`.

---

## 1. Sub-Processes

Type: `business-process`, level: `sub-process`. Each `derived_from` its parent process.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Application Intake & Capture | business-process | sub-process | Customer Onboarding | Receiving, capturing and pre-checking a prospect's application and supporting documents before verification. | Onboarding Specialist | Customer Application | Captured Application | depends_on Customer Acquisition | — | Channel auth, data-quality checks, consent capture | Onboarding Intake, Application Capture | https://www.capco.com/intelligence/capco-intelligence/digital-onboarding-eight-steps-to-create-a-complete-solution ; https://www.veriff.com/kyc/business/onboarding |
| Identity & Due Diligence | business-process | sub-process | Customer Onboarding | Proving applicant identity (CIP) and performing CDD/EDD and screening to assign a risk rating. | KYC Analyst | Captured Application | Cleared Onboarding Case | depends_on Identity Verification | — | Identity proofing, CDD/EDD, sanctions/PEP screening | KYC & CDD, Verification & Diligence | https://hyperverge.co/blog/kyc-process-guide/ ; https://www.sanctionscanner.com/blog/customer-onboarding-in-aml-and-kyc-1246 |
| Account Setup & Activation | business-process | sub-process | Customer Onboarding | Creating the customer record, opening the product and activating access once due diligence clears. | Onboarding Specialist | Cleared Onboarding Case | Active Customer Profile | depends_on Customer Profile Management | — | Approval gate, four-eyes, activation logging | Onboarding Activation, Account Activation | https://www.investglass.com/customer-onboarding-in-banking-a-2026-guide-to-digital-compliant-and-sovereign-journeys/ ; https://microblink.com/resources/blog/requirements-for-digital-onboarding/ |
| Complaint Intake & Triage | business-process | sub-process | Complaint Handling | Logging an incoming complaint, acknowledging it and classifying/prioritising it for handling. | Complaints Officer | Complaint Record | Triaged Complaint | depends_on Case Management | — | Acknowledgement SLA, eligibility/jurisdiction check | Complaint Logging, Intake & Triage | https://handbook.fca.org.uk/handbook/disp1/disp1s4 ; https://blog.ansi.org/ansi/complaint-iso-10002-2018-customer-satisfaction/ |
| Complaint Investigation & Redress | business-process | sub-process | Complaint Handling | Investigating the complaint impartially, deciding the outcome and delivering redress and a final response. | Complaints Officer | Triaged Complaint | Resolved Complaint | depends_on Case Management | — | Impartial investigation, redress authorisation, final-response SLA | Investigation & Redress, Resolution & Redress | https://handbook.fca.org.uk/handbook/disp1/disp1s6 ; https://www.consumerfinance.gov/compliance/consumer-complaint-program/company-process/ |
| Complaint Closure & Learning | business-process | sub-process | Complaint Handling | Closing the complaint, capturing feedback and performing root-cause analysis to drive improvement. | Quality Assurance Reviewer | Resolved Complaint | Closed Complaint | depends_on Case Management | — | Root-cause analysis, MI/reporting, record retention | Closure & RCA, Learning & Reporting | https://www.rbcompliance.co.uk/post/2019/03/13/dispute-resolution-complaints-in-the-fca-handbook ; https://pacificcert.com/iso-10002-2018-quality-management-customer-satisfaction/ |
| Request Intake & Triage | business-process | sub-process | Service Request Handling | Capturing a service request, validating the requester and triaging it to a priority/queue. | Service Advisor | Service Request Ticket | Triaged Request | depends_on Customer Servicing | — | Requester authentication, priority/SLA assignment | Request Logging, Intake & Triage | https://www.givainc.com/resources/itil/service-request-management/ ; https://www.bland.ai/blog/customer-request-triage |
| Request Fulfilment & Closure | business-process | sub-process | Service Request Handling | Fulfilling the requested change/service, confirming with the customer and closing the ticket. | Service Advisor | Triaged Request | Fulfilled Request | depends_on Case Management | — | SLA tracking, escalation, closure confirmation | Fulfilment & Closure, Resolution & Closure | https://www.connectwise.com/blog/the-importance-of-service-request-management ; https://blog.invgate.com/itil-priority-matrix |

---

## 2. Steps — Customer Onboarding

Type: `process-step`, parent process: **Customer Onboarding**.
Files: `process-flows/customer-onboarding/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Receive Application | process-step | 01 | Customer Onboarding | Capture a prospect's onboarding application from a digital channel, branch or API and open an onboarding case. | Onboarding Specialist | Customer Application | Onboarding Case | depends_on Digital Channel Platform | causes Capture Consent | Channel authentication, intake logging | Capture Application, Intake Applicant | https://www.capco.com/intelligence/capco-intelligence/digital-onboarding-eight-steps-to-create-a-complete-solution ; https://www.wavetec.com/blog/banking/digitally-onboarding-new-customers/ |
| Capture Consent | process-step | 02 | Customer Onboarding | Present terms, privacy/data-use notices and marketing opt-ins; record explicit consent and e-signature. | Onboarding Specialist | Onboarding Case | Consent Record | depends_on Customer Identity | causes Collect Documents | Consent capture control, e-signature, audit trail | Record Consent, Consent Capture Step | https://www.salesforce.com/financial-services/digital-client-onboarding/ ; https://ondato.com/blog/digital-onboarding/ |
| Collect Documents | process-step | 03 | Customer Onboarding | Collect and classify identity, address and tax documents via upload or capture; extract key data. | Onboarding Specialist | Onboarding Case | Document Package | depends_on Intelligent Document Processing | causes Verify Identity | Document authenticity check, data extraction validation | Gather Documents, Document Collection Step | https://microblink.com/resources/blog/requirements-for-digital-onboarding/ ; https://www.checkfile.ai/en-US/blog/bank-customer-onboarding-kyc-verification |
| Verify Identity | process-step | 04 | Customer Onboarding | Prove applicant identity (CIP) via document and biometric/liveness checks; branch on pass, fail or manual review. | KYC Analyst | Document Package | Verified Identity | depends_on Identity Verification | causes Screen Customer | Identity proofing, liveness/biometric (branch: pass / fail / manual) | Prove Identity, Identity Proofing Step | https://www.veriff.com/kyc/business/onboarding ; https://regulaforensics.com/blog/digital-onboarding/ |
| Screen Customer | process-step | 05 | Customer Onboarding | Screen the applicant against sanctions, PEP and adverse-media lists; hold and escalate any hits. | KYC Analyst | Verified Identity | Screened Applicant | depends_on Transaction Monitoring Platform | causes Assess Customer Risk | Sanctions/PEP/adverse-media screening (branch: hit -> hold/escalate vs clear) | Screen Applicant, Watchlist Check Step | https://www.sanctionscanner.com/blog/customer-onboarding-in-aml-and-kyc-1246 ; https://seon.io/resources/kyc-onboarding/ |
| Assess Customer Risk | process-step | 06 | Customer Onboarding | Perform CDD and assign a risk rating; trigger EDD for high-risk customers (e.g. PEPs, high-risk geographies). | KYC Analyst | Screened Applicant | Risk-Rated Case | depends_on Customer Due Diligence | causes Approve Onboarding | CDD/EDD control, source-of-funds review (branch: standard vs EDD) | Risk Rate Customer, CDD Assessment Step | https://hyperverge.co/blog/kyc-process-guide/ ; https://idenfy.com/blog/kyc-onboarding/ |
| Approve Onboarding | process-step | 07 | Customer Onboarding | Make the accept/decline/refer decision against policy and apply four-eyes approval for elevated risk. | Onboarding Specialist | Risk-Rated Case | Approved Onboarding | depends_on Workflow Orchestration | causes Create Customer Record | Approval gate, four-eyes for high-risk (branch: accept / decline / refer) | Decide Onboarding, Onboarding Approval Step | https://www.fintechtris.com/blog/digital-onboarding-banking-kyc-kyb-id-verification ; https://resources.fenergo.com/blogs/customer-onboarding-expectations-vs-reality |
| Create Customer Record | process-step | 08 | Customer Onboarding | Create the golden customer/party record and KYC Profile in master data and provision the product. | Onboarding Specialist | Approved Onboarding | Active Customer Profile | depends_on Master Data Management | causes Activate Customer | Unique-party/dedupe control, data-quality validation | Establish Party Record, Customer Record Creation | https://www.axxiome.com/solutions/customer-onboarding-digital-solution ; https://www.backbase.com/blog/customer-onboarding-software-for-banks |
| Activate Customer | process-step | 09 | Customer Onboarding | Activate channel access and the product, deliver welcome communications and enrol in ongoing monitoring. | Onboarding Specialist | Active Customer Profile | Onboarded Customer | depends_on Notification Services | — | Activation logging, ongoing-monitoring enrolment | Welcome Customer, Customer Activation Step | https://www.investglass.com/customer-onboarding-in-banking-a-2026-guide-to-digital-compliant-and-sovereign-journeys/ ; https://www.capco.com/intelligence/capco-intelligence/digital-onboarding-eight-steps-to-create-a-complete-solution |

---

## 3. Steps — Complaint Handling

Type: `process-step`, parent process: **Complaint Handling**.
Files: `process-flows/complaint-handling/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Log Complaint | process-step | 01 | Complaint Handling | Record an inbound complaint from any channel into the case system with a reference number and key details. | Complaints Officer | Complaint Record | Logged Complaint | depends_on Case Management | causes Acknowledge Complaint | Mandatory-fields capture, reference issuance, record retention | Register Complaint, Complaint Logging Step | https://blog.ansi.org/ansi/complaint-iso-10002-2018-customer-satisfaction/ ; https://complaintlab.com/resources/knowledge-base/disp-complaint-handling-complete-regulatory-guide |
| Acknowledge Complaint | process-step | 02 | Complaint Handling | Send a prompt acknowledgement with the firm's complaints procedure and expected timeframes; attempt summary resolution. | Complaints Officer | Logged Complaint | Acknowledged Complaint | depends_on Notification Services | causes Triage Complaint | Acknowledgement SLA, 3-day summary-resolution option (branch) | Send Acknowledgement, Complaint Acknowledgement Step | https://handbook.fca.org.uk/handbook/disp1/disp1s4 ; https://www.consumerfinance.gov/compliance/consumer-complaint-program/company-process/ |
| Triage Complaint | process-step | 03 | Complaint Handling | Classify category, check eligibility/jurisdiction and prioritise; route to the right handler or specialist team. | Complaints Officer | Acknowledged Complaint | Triaged Complaint | depends_on Workflow Orchestration | causes Investigate Complaint | Eligibility/jurisdiction check, priority assignment (branch: route / reject) | Classify Complaint, Complaint Triage Step | https://handbook.fca.org.uk/handbook/disp3 ; https://swiftcase.co.uk/guides/fca-compliance/disp-complaints-framework/ |
| Investigate Complaint | process-step | 04 | Complaint Handling | Investigate competently, diligently and impartially; gather evidence and assess merits against the facts. | Complaints Officer | Triaged Complaint | Investigation Findings | depends_on Case Management | causes Determine Outcome | Impartial-investigation control, evidence trail | Examine Complaint, Complaint Investigation Step | https://handbook.fca.org.uk/handbook/disp1/disp1s4 ; https://www.fdcapital.co.uk/disp-handbook-guide/ |
| Determine Outcome | process-step | 05 | Complaint Handling | Decide whether the complaint is upheld and what redress applies; authorise compensation within delegated limits. | Complaints Officer | Investigation Findings | Redress Decision | depends_on Case Management | causes Issue Final Response | Redress authorisation, delegated-limit control (branch: uphold / reject / partial) | Decide Redress, Outcome Decision Step | https://www.rbcompliance.co.uk/post/2019/03/13/dispute-resolution-complaints-in-the-fca-handbook ; https://www.consumerfinance.gov/compliance/consumer-complaint-program/company-process/ |
| Issue Final Response | process-step | 06 | Complaint Handling | Send the final response with the outcome and, where applicable, referral rights to the Ombudsman within the deadline. | Complaints Officer | Redress Decision | Final Response Letter | depends_on Notification Services | causes Conduct Root Cause | 8-week final-response SLA, FOS/escalation referral rights | Send Final Response, Final Response Step | https://handbook.fca.org.uk/handbook/disp1/disp1s6 ; https://www.hl.co.uk/help/support/complaints/complaints-handling-procedure |
| Conduct Root Cause | process-step | 07 | Complaint Handling | Analyse drivers across complaints, identify systemic root causes and raise improvement actions and MI reporting. | Quality Assurance Reviewer | Final Response Letter | Root Cause Report | depends_on Analytics Platform | causes Close Complaint | Root-cause analysis, complaints MI/regulatory reporting | Root Cause Analysis Step, Analyse Drivers | https://www.rbcompliance.co.uk/post/2019/03/13/dispute-resolution-complaints-in-the-fca-handbook ; https://pacificcert.com/iso-10002-2018-quality-management-customer-satisfaction/ |
| Close Complaint | process-step | 08 | Complaint Handling | Confirm resolution with the customer, capture satisfaction feedback and close and retain the complaint record. | Complaints Officer | Root Cause Report | Closed Complaint | depends_on Case Management | — | Closure confirmation, feedback capture, 3-year record retention | Resolve & Close, Complaint Closure Step | https://certbetter.com/blog/iso-10002-simplified-a-practical-guide-to-effective-customer-satisfaction-complaints-handling ; https://handbook.fca.org.uk/handbook/disp1/disp1s6 |

---

## 4. Steps — Service Request Handling

Type: `process-step`, parent process: **Service Request Handling**.
Files: `process-flows/service-request-handling/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capture Request | process-step | 01 | Service Request Handling | Capture a customer service request from a channel and create a ticket with the request type and details. | Service Advisor | Service Request Ticket | Logged Request | depends_on Contact Center Platform | causes Authenticate Requester | Channel intake logging, mandatory-fields capture | Log Request, Request Capture Step | https://www.givainc.com/resources/itil/service-request-management/ ; https://www.connectwise.com/blog/the-importance-of-service-request-management |
| Authenticate Requester | process-step | 02 | Service Request Handling | Verify the requester's identity and entitlement to act on the account before any change is actioned. | Service Advisor | Logged Request | Verified Requester | depends_on Identity Access Management | causes Categorize Request | Requester authentication, entitlement check (branch: verified / step-up / reject) | Verify Requester, Requester Authentication Step | https://www.bland.ai/blog/customer-request-triage ; https://www.checkfile.ai/en-US/blog/bank-customer-onboarding-kyc-verification |
| Categorize Request | process-step | 03 | Service Request Handling | Classify the request type, assign priority/SLA and route to the appropriate fulfilment queue or specialist. | Service Advisor | Verified Requester | Triaged Request | depends_on Workflow Orchestration | causes Assess Request | Priority/SLA assignment, routing rules (branch: self-serve / agent / specialist) | Classify Request, Request Triage Step | https://blog.invgate.com/itil-priority-matrix ; https://www.bland.ai/blog/customer-request-triage |
| Assess Request | process-step | 04 | Service Request Handling | Determine whether the request can be fulfilled directly, needs approval, or must convert/escalate (e.g. to a complaint). | Service Advisor | Triaged Request | Assessed Request | depends_on Case Management | causes Fulfil Request | Eligibility/approval check (branch: fulfil / escalate / convert to complaint) | Evaluate Request, Request Assessment Step | https://www.givainc.com/resources/itil/service-request-management/ ; https://dl.acm.org/doi/fullHtml/10.1145/3599732.3641340 |
| Fulfil Request | process-step | 05 | Service Request Handling | Execute the requested change or service in the system of record (e.g. update details, issue document, amend product). | Service Advisor | Assessed Request | Fulfilled Request | depends_on Core Banking Processing | causes Confirm Resolution | Change control, four-eyes for sensitive changes | Action Request, Request Fulfilment Step | https://www.connectwise.com/blog/the-importance-of-service-request-management ; https://www.givainc.com/resources/itil/service-request-management/ |
| Confirm Resolution | process-step | 06 | Service Request Handling | Notify the customer that the request is complete, share outcome details and confirm satisfaction. | Service Advisor | Fulfilled Request | Confirmed Resolution | depends_on Notification Services | causes Close Request | Resolution confirmation, SLA-met check | Notify Customer, Resolution Confirmation Step | https://www.givainc.com/resources/itil/service-request-management/ ; https://blog.invgate.com/itil-priority-matrix |
| Close Request | process-step | 07 | Service Request Handling | Set the ticket to closed, capture feedback and retain the record; reopen if the customer responds within the window. | Service Advisor | Confirmed Resolution | Closed Request | depends_on Case Management | — | Closure control, feedback capture, reopen window (branch) | Resolve & Close Request, Request Closure Step | https://www.connectwise.com/blog/the-importance-of-service-request-management ; https://www.givainc.com/resources/itil/service-request-management/ |

---

## 5. Supporting Concepts (roles, events, artifacts)

Deduped across all three flows. Flow columns left blank; definition + flows that mention
them given. Type is `role`, `event`, or `artifact`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Onboarding Specialist | role | — | — | Front-office owner of the onboarding case who captures the application, drives it through approval and activates the customer. Mentioned in: Customer Onboarding. | — | — | — | — | — | — | Onboarding Officer, New Accounts Officer | https://www.capco.com/intelligence/capco-intelligence/digital-onboarding-eight-steps-to-create-a-complete-solution |
| KYC Analyst | role | — | — | Compliance/operations specialist who performs identity verification, screening and CDD/EDD during onboarding. Mentioned in: Customer Onboarding. | — | — | — | — | — | — | KYC Officer, Due Diligence Analyst | https://hyperverge.co/blog/kyc-process-guide/ |
| Complaints Officer | role | — | — | Owner of a complaint case who acknowledges, triages, investigates, decides redress and issues the final response. Mentioned in: Complaint Handling. | — | — | — | — | — | — | Complaint Handler, Dispute Resolution Officer | https://handbook.fca.org.uk/handbook/disp1/disp1s4 |
| Service Advisor | role | — | — | Service agent who captures, authenticates, triages, fulfils and closes customer service requests. Mentioned in: Service Request Handling. | — | — | — | — | — | — | Customer Service Agent, Service Desk Agent | https://www.givainc.com/resources/itil/service-request-management/ |
| Quality Assurance Reviewer | role | — | — | Second-line reviewer who conducts root-cause analysis, MI reporting and complaint/quality assurance. Mentioned in: Complaint Handling. | — | — | — | — | — | — | QA Analyst, Complaints QA Reviewer | https://pacificcert.com/iso-10002-2018-quality-management-customer-satisfaction/ |
| Application Submitted Event | event | — | — | Trigger raised when a prospect submits an onboarding application, starting the onboarding flow. Mentioned in: Customer Onboarding. | — | — | — | — | — | — | Onboarding Started Event, Application Received | https://www.wavetec.com/blog/banking/digitally-onboarding-new-customers/ |
| Customer Activated Event | event | — | — | Business event signalling that a new customer's profile and product have been activated. Mentioned in: Customer Onboarding. | — | — | — | — | — | — | Onboarding Completed Event, Account Activated | https://www.investglass.com/customer-onboarding-in-banking-a-2026-guide-to-digital-compliant-and-sovereign-journeys/ |
| Complaint Received Event | event | — | — | Trigger raised when a complaint is received on any channel, starting the complaint-handling flow. Mentioned in: Complaint Handling. | — | — | — | — | — | — | Complaint Raised Event, Complaint Logged | https://blog.ansi.org/ansi/complaint-iso-10002-2018-customer-satisfaction/ |
| Service Request Raised Event | event | — | — | Trigger raised when a customer submits a service request, starting the request-handling flow. Mentioned in: Service Request Handling. | — | — | — | — | — | — | Request Submitted Event, Ticket Raised | https://www.givainc.com/resources/itil/service-request-management/ |
| SLA Breach Event | event | — | — | Escalation event raised when an acknowledgement, final-response or fulfilment SLA threshold is breached. Mentioned in: Complaint Handling, Service Request Handling. | — | — | — | — | — | — | SLA Escalation Event, Deadline Breached | https://blog.invgate.com/itil-priority-matrix |
| Customer Application | artifact | — | — | The submitted application data and product selection that initiate onboarding. Mentioned in: Customer Onboarding. | — | — | — | — | — | — | Onboarding Application, Account Application | https://www.capco.com/intelligence/capco-intelligence/digital-onboarding-eight-steps-to-create-a-complete-solution |
| Onboarding Case | artifact | — | — | The case object tracking an onboarding instance, its documents, checks, risk rating and decision. Mentioned in: Customer Onboarding. | — | — | — | — | — | — | Onboarding Record, Onboarding File | https://resources.fenergo.com/blogs/customer-onboarding-expectations-vs-reality |
| KYC Profile | artifact | — | — | The structured customer due-diligence record holding identity evidence, screening results and risk rating. Mentioned in: Customer Onboarding. | — | — | — | — | — | — | CDD Profile, Customer Risk Profile | https://idenfy.com/blog/kyc-onboarding/ |
| Consent Record | artifact | — | — | The captured record of customer consents, e-signature and marketing opt-ins with timestamp and version. Mentioned in: Customer Onboarding. | — | — | — | — | — | — | Consent Artifact, Opt-In Record | https://ondato.com/blog/digital-onboarding/ |
| Complaint Record | artifact | — | — | The case record of a complaint with reference, category, investigation findings, outcome and redress. Mentioned in: Complaint Handling. | — | — | — | — | — | — | Complaint Case, Complaint File | https://complaintlab.com/resources/knowledge-base/disp-complaint-handling-complete-regulatory-guide |
| Final Response Letter | artifact | — | — | The firm's final written response to a complaint, including outcome, redress and Ombudsman referral rights. Mentioned in: Complaint Handling. | — | — | — | — | — | — | Final Response, FRL | https://handbook.fca.org.uk/handbook/disp1/disp1s6 |
| Service Request Ticket | artifact | — | — | The ticket capturing a customer service request, its type, priority/SLA, fulfilment actions and closure. Mentioned in: Service Request Handling. | — | — | — | — | — | — | Service Ticket, Request Ticket | https://www.givainc.com/resources/itil/service-request-management/ |

---

## Notes on naming collisions checked

- Step names are verb-form and distinct from capabilities: e.g. "Verify Identity" (step)
  vs "Identity Verification" (L3 capability); "Assess Customer Risk" (step) vs no
  capability of that name; "Triage Complaint" / "Capture Consent" are new.
- "KYC Analyst", "Onboarding Specialist", "Complaints Officer", "Service Advisor",
  "Quality Assurance Reviewer" are new roles (Payments roles were Payment Operations
  Analyst, Clearing Operations Specialist, Compliance Screening Officer, Settlement
  Officer, Reconciliation Analyst, Treasury Cash Manager).
- Sub-process names ("Application Intake & Capture", etc.) do not collide with Payments
  sub-processes or any capability.
- Events/artifacts are new (Payments used Payment Initiated Event, Payment Instruction,
  etc.); "Customer Application", "Onboarding Case", "KYC Profile", "Complaint Record",
  "Service Request Ticket" are all new.
