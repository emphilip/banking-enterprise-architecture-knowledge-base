---
id: proposed-deposits-and-accounts-flows
title: Proposed Deposits & Accounts Process Flows
type: status-note
status: draft
domain: Deposits & Accounts
---

# Proposed Deposits & Accounts Process Flows

Multi-granularity process-flow decomposition for the **Deposits & Accounts** domain. The
domain currently defines only 2 processes (Deposit Account Opening, Statement Generation),
so this proposal adds **3 new processes** for adequate coverage and decomposes all **5**
processes into sub-processes, ordered steps, and supporting concepts.

Relationship verbs used (the 7): `depends_on`, `derived_from`, `supersedes`, `defined_in`,
`related_to`, `causes`, `mentions`.

Naming checked against `glossary/_canonical-names.md`. Collision avoidance notes:
- "Account Statement" collides with capability/artifact context -> artifact named **Bank Account Statement**.
- "Account Maintenance" (process) is distinct from capability "Loan Account Maintenance" / "Account Servicing".
- Verb-form step names kept distinct from capability names; all names globally unique vs Payments / Customer-Management / Lending entries already in the registry.

---

## 1. New Processes (type: business-process, level: process)

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Account Maintenance | business-process | process | — (domain: Deposits & Accounts) | Ongoing servicing of an open deposit account: change of address/details, mandate/signatory changes, stop payments, standing instructions, interest posting and fee changes. | Deposit Operations Clerk | Service Maintenance Request, account record | updated account record, confirmation | Account Servicing | Verify Account Holder | Signatory verification, Reg DD change-in-terms notice, dual control on static-data changes | Account Servicing Process, Account Detail Maintenance | https://www.associatedbank.com/forms-and-disclosures/disclosures/deposit-account-agreement ; https://openonline.53.com/product/service/apply/document/depositAccountRules |
| Account Closure | business-process | process | — (domain: Deposits & Accounts) | End-to-end closure of a deposit account incl. closure request capture, balance settlement to zero, final statement and account deactivation; covers dormancy-driven and escheatment closures. | Deposit Operations Clerk | Account Closure Request, account record | closed account, Closure Confirmation | Account Servicing | Validate Closure Eligibility | Signatory verification, zero-balance confirmation, dormancy rules, escheatment/CASS, record retention (5 yrs) | Account Termination, Account Offboarding | https://legalclarity.org/what-happens-when-you-close-a-bank-account/ ; https://www.incharge.org/blog/what-happens-to-dormant-bank-accounts/ |
| Overdraft Servicing | business-process | process | — (domain: Deposits & Accounts) | Handling of debit items that exceed available balance: opt-in capture, overdraft-vs-NSF decisioning, limit checks, pay/return decision and fee application under Reg E. | Overdraft Operations Analyst | overdraft/NSF item, Reg E Opt-In Record, available balance | pay/return decision, Overdraft Fee | Overdraft Management | Detect Insufficient Funds | Reg E opt-in, overdraft coverage limit, fee disclosure, fair-access underwriting | Overdraft Handling, NSF Processing | https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html ; https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-12.html |

---

## 2. Sub-Processes (type: business-process, level: sub-process)

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Application & Identity Capture | business-process | sub-process | Deposit Account Opening | Capture of account application, customer identifying data and consent, and CIP identity verification. | Onboarding Specialist | Account Opening Form, ID documents | verified applicant data | Account Opening | — | CIP/KYC, TIN collection | Opening Intake, CIP Capture | https://www.alogent.com/banking-definitions/customer-identification-program-cip |
| Account Setup & Funding | business-process | sub-process | Deposit Account Opening | Mandate/signature card capture, product setup, account creation and initial funding/activation. | Deposit Operations Clerk | Signature Card, product config | active account | Account Opening | — | Signatory verification, fee disclosure | Open & Fund, Activation | https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-B/section-1020.220 |
| Statement Assembly | business-process | sub-process | Statement Generation | Determine statement cycle, extract postings and assemble statement content with required disclosures. | Statement Production Officer | transaction ledger, cycle calendar | assembled statement | Account Servicing | — | Reg DD/Reg E periodic content, cycle consistency (+/-4 days) | Statement Build, Cycle Assembly | https://www.ecfr.gov/current/title-12/chapter-X/part-1030 |
| Statement Delivery | business-process | sub-process | Statement Generation | Render, deliver (print/e-statement) and archive statements per delivery preference. | Statement Production Officer | assembled statement, delivery prefs | delivered Bank Account Statement | Notification Services | — | E-delivery consent, archival/retention | Statement Distribution, E-Statement Delivery | https://www.federalreserve.gov/boarddocs/caletters/2009/0914/09-14-attachment.pdf |
| Maintenance Intake & Verification | business-process | sub-process | Account Maintenance | Capture maintenance request and verify the requester's authority/signatory status. | Deposit Operations Clerk | Service Maintenance Request | verified request | Account Servicing | — | Signatory verification, authentication | Maintenance Intake, Mandate Check | https://openonline.53.com/product/service/apply/document/depositAccountRules |
| Account Update Execution | business-process | sub-process | Account Maintenance | Apply requested changes (details, mandate, stop payment, standing instruction) and post interest/fee changes with notice. | Deposit Operations Clerk | verified request | updated account record | Core Banking Processing | — | Dual control, change-in-terms notice | Update Execution, Servicing Action | https://www.associatedbank.com/forms-and-disclosures/disclosures/deposit-account-agreement |
| Closure Request Handling | business-process | sub-process | Account Closure | Capture and validate a closure request and confirm eligibility (holds, pending items, signatories). | Deposit Operations Clerk | Account Closure Request | eligible closure | Account Servicing | — | Signatory verification, hold checks | Closure Intake, Closure Validation | https://www.sofi.com/learn/content/bank-letter-to-close-account/ |
| Balance Settlement & Deactivation | business-process | sub-process | Account Closure | Disburse residual balance to zero, produce final statement and deactivate the account. | Deposit Operations Clerk | eligible closure, residual balance | closed account, Closure Confirmation | Core Banking Processing | — | Zero-balance confirmation, record retention | Settle & Close, Final Settlement | https://legalclarity.org/what-happens-when-you-close-a-bank-account/ |
| Dormancy & Escheatment | business-process | sub-process | Account Closure | Identify dormant accounts, issue dormancy notice, and escheat unclaimed funds to the state. | Unclaimed Property Officer | dormancy report | escheated funds, escheatment report | Core Banking Processing | — | Dormancy rules, escheatment/CASS, state filing deadlines | Escheatment, Abandoned Property Handling | https://www.incharge.org/blog/what-happens-to-dormant-bank-accounts/ |
| Overdraft Decisioning | business-process | sub-process | Overdraft Servicing | Detect insufficient funds, check opt-in and limit, and decide pay-or-return. | Overdraft Operations Analyst | debit item, available balance | pay/return decision | Overdraft Management | — | Reg E opt-in, overdraft limit | OD Decisioning, Pay/Return Decision | https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html |
| Overdraft Fee & Notice | business-process | sub-process | Overdraft Servicing | Apply applicable overdraft/NSF fee and notify the customer with required disclosures. | Overdraft Operations Analyst | pay/return decision | Overdraft Fee, customer notice | Notification Services | — | Fee disclosure, NSF vs overdraft fee rules | Fee Application, OD Notice | https://www.consumerfinance.gov/about-us/blog/new-insights-on-bank-overdraft-fees-and-4-ways-to-avoid-them/ |

---

## 3. Process Steps (type: process-step)

### 3.1 Deposit Account Opening (existing)
Steps filed as `process-flows/deposit-account-opening/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capture Account Application | process-step | 1 | Deposit Account Opening | Capture applicant details and product selection on the Account Opening Form. | Onboarding Specialist | Account Opening Form | application record | Digital Channel Platform | causes Collect CIP Information | Data completeness, product eligibility | Take Account Application, Opening Intake Step | https://www.alogent.com/banking-definitions/customer-identification-program-cip ; https://www.socure.com/glossary/customer-identification-program |
| Collect CIP Information | process-step | 2 | Deposit Account Opening | Collect name, DOB, address and TIN required under the Customer Identification Program. | Onboarding Specialist | application record, ID documents | CIP dataset | Intelligent Document Processing | causes Verify Account Applicant | CIP/KYC, TIN collection | Gather CIP Data, CIP Collection Step | https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-B/section-1020.220 ; https://www.fdic.gov/news/financial-institution-letters/2024/fil24015a.pdf |
| Verify Account Applicant | process-step | 3 | Deposit Account Opening | Verify identity via documentary and non-documentary methods (incl. ChexSystems). | KYC Analyst | CIP dataset | verification result | Identity Verification | causes Capture Signature Card | CIP verification, watchlist check | Run CIP Verification, Applicant Verification Step | https://www.alogent.com/banking-definitions/customer-identification-program-cip |
| Capture Signature Card | process-step | 4 | Deposit Account Opening | Record authorized signatories and mandate on the Signature Card. | Deposit Operations Clerk | verification result | Signature Card | Core Banking Processing | causes Disclose Account Terms | Signatory verification, mandate setup | Record Signatories, Signature Capture Step | https://www.compliancecohort.com/blog/cip-requirements-for-business-account-signers |
| Disclose Account Terms | process-step | 5 | Deposit Account Opening | Present Truth-in-Savings (Reg DD) fee and rate disclosures and capture acceptance. | Onboarding Specialist | product config | accepted disclosures | Document Management | causes Establish Deposit Account | Reg DD fee/rate disclosure | Provide TIS Disclosure, Terms Disclosure Step | https://www.ecfr.gov/current/title-12/chapter-X/part-1030 |
| Establish Deposit Account | process-step | 6 | Deposit Account Opening | Create the account on the core ledger with product, mandate and limits. | Deposit Operations Clerk | accepted disclosures, Signature Card | account record | Core Banking Processing | causes Fund New Account | Account setup controls, dual control | Create Account, Account Setup Step | https://openonline.53.com/product/service/apply/document/depositAccountRules |
| Fund New Account | process-step | 7 | Deposit Account Opening | Apply initial deposit and activate the account; emit Account Opened Event. | Deposit Operations Clerk | account record, initial deposit | active account | Core Banking Processing | — | Funding verification, activation | Activate Account, Initial Funding Step | https://www.alogent.com/banking-definitions/customer-identification-program-cip |

### 3.2 Statement Generation (existing)
Steps filed as `process-flows/statement-generation/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Determine Statement Cycle | process-step | 1 | Statement Generation | Identify accounts due in the cycle and lock the cycle period. | Statement Production Officer | cycle calendar, account list | cycle population | Core Banking Processing | causes Extract Account Activity | Cycle consistency (+/-4 days) | Identify Cycle, Cycle Determination Step | https://www.ecfr.gov/current/title-12/chapter-X/part-1030 |
| Extract Account Activity | process-step | 2 | Statement Generation | Extract postings, balances and interest for each account in the cycle. | Statement Production Officer | cycle population, transaction ledger | extracted activity | Core Banking Processing | causes Reconcile Statement Data | Completeness reconciliation | Pull Postings, Activity Extraction Step | https://en.wikipedia.org/wiki/Bank_reconciliation |
| Reconcile Statement Data | process-step | 3 | Statement Generation | Reconcile extracted activity to ledger control totals before rendering. | Reconciliation Analyst | extracted activity | reconciled dataset | Data Warehousing | causes Assemble Statement Document | Control-total reconciliation | Validate Statement Totals, Statement Recon Step | https://ramp.com/blog/what-is-bank-reconciliation |
| Assemble Statement Document | process-step | 4 | Statement Generation | Compose statement content with required Reg E/Reg DD disclosures. | Statement Production Officer | reconciled dataset | assembled statement | Document Management | causes Render Statement Output | Reg E/Reg DD periodic content | Compose Statement, Statement Assembly Step | https://www.federalreserve.gov/boarddocs/caletters/2009/0914/09-14-attachment.pdf |
| Render Statement Output | process-step | 5 | Statement Generation | Render print/PDF/e-statement formats per delivery preference. | Statement Production Officer | assembled statement, delivery prefs | rendered Bank Account Statement | Document Management | causes Deliver Statement | Format integrity, e-delivery consent | Produce Statement Output, Rendering Step | https://www.ecfr.gov/current/title-12/chapter-X/part-1030 |
| Deliver Statement | process-step | 6 | Statement Generation | Deliver via mail or electronic channel; emit Statement Issued Event. | Statement Production Officer | rendered Bank Account Statement | delivered statement | Notification Services | causes Archive Statement | Delivery confirmation, e-consent | Distribute Statement, Statement Delivery Step | https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html |
| Archive Statement | process-step | 7 | Statement Generation | Archive the statement for retention and self-service retrieval. | Statement Production Officer | delivered statement | archived statement | Document Management | — | Record retention | Store Statement, Statement Archival Step | https://www.ecfr.gov/current/title-12/chapter-X/part-1030 |

### 3.3 Account Maintenance (new)
Steps filed as `process-flows/account-maintenance/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Receive Maintenance Request | process-step | 1 | Account Maintenance | Capture a Service Maintenance Request (details, mandate, stop payment, standing instruction). | Deposit Operations Clerk | Service Maintenance Request | logged request | Digital Channel Platform | causes Verify Account Holder | Request logging, channel auth | Log Maintenance Request, Maintenance Intake Step | https://openonline.53.com/product/service/apply/document/depositAccountRules |
| Verify Account Holder | process-step | 2 | Account Maintenance | Verify requester identity and signatory authority against the mandate. | Deposit Operations Clerk | logged request, mandate | verified requester | Identity Access Management | causes Assess Change Impact | Signatory verification, authentication | Authenticate Account Holder, Holder Verification Step | https://www.associatedbank.com/forms-and-disclosures/disclosures/deposit-account-agreement |
| Assess Change Impact | process-step | 3 | Account Maintenance | Determine downstream impacts and whether a change-in-terms notice is required. | Deposit Operations Clerk | verified requester | change assessment | Workflow Orchestration | causes Apply Account Change | Reg DD change-in-terms assessment | Evaluate Change, Impact Assessment Step | https://www.ecfr.gov/current/title-12/chapter-X/part-1030 |
| Apply Account Change | process-step | 4 | Account Maintenance | Execute the change in the core system under dual control. | Deposit Operations Clerk | change assessment | updated account record | Core Banking Processing | causes Post Account Interest | Dual control on static data | Execute Account Change, Change Execution Step | https://openonline.53.com/product/service/apply/document/depositAccountRules |
| Post Account Interest | process-step | 5 | Account Maintenance | Calculate and post accrued interest and any fee changes to the account. | Deposit Operations Clerk | updated account record | interest posting | Core Banking Processing | causes Notify Account Change | Interest accrual accuracy, fee disclosure | Apply Interest Posting, Interest Posting Step | https://www.ameriprise.com/binaries/content/assets/ampcom/ameriprise_bank_savings_account_deposit_account_agreement.pdf |
| Notify Account Change | process-step | 6 | Account Maintenance | Issue confirmation and any required change-in-terms notice to the customer. | Deposit Operations Clerk | updated account record | change confirmation | Notification Services | — | Change-in-terms notice, delivery confirmation | Confirm Account Change, Change Notification Step | https://www.zionsbank.com/content/dam/zbna/disclosures/shared/general/depositagreement.pdf |

### 3.4 Account Closure (new)
Steps filed as `process-flows/account-closure/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Receive Closure Request | process-step | 1 | Account Closure | Capture an Account Closure Request from customer or dormancy trigger. | Deposit Operations Clerk | Account Closure Request | logged closure | Digital Channel Platform | causes Validate Closure Eligibility | Request logging, signatory capture | Log Closure Request, Closure Intake Step | https://www.sofi.com/learn/content/bank-letter-to-close-account/ |
| Validate Closure Eligibility | process-step | 2 | Account Closure | Verify signatories and check holds, pending items and linked services. | Deposit Operations Clerk | logged closure, account record | eligible closure | Workflow Orchestration | causes Settle Residual Balance | Signatory verification, hold checks | Check Closure Eligibility, Eligibility Validation Step | https://legalclarity.org/what-happens-when-you-close-a-bank-account/ |
| Settle Residual Balance | process-step | 3 | Account Closure | Disburse remaining funds to zero by transfer, draft or cash. | Deposit Operations Clerk | eligible closure, residual balance | zero balance | Core Banking Processing | causes Issue Final Statement | Zero-balance confirmation | Disburse Residual Funds, Balance Settlement Step | https://www.sofi.com/learn/content/bank-letter-to-close-account/ |
| Issue Final Statement | process-step | 4 | Account Closure | Produce the final statement evidencing zero balance and closure. | Statement Production Officer | zero balance | final statement | Document Management | causes Deactivate Account | Final statement accuracy | Produce Closing Statement, Final Statement Step | https://piercelaw.com/news/probate-question-and-answer/what-is-a-bank-closing-statement-for-an-estate-account-and-how-do-i-request-one-that-shows-a-zero-balance-nc/ |
| Deactivate Account | process-step | 5 | Account Closure | Close the account on the core ledger and emit Account Closed Event. | Deposit Operations Clerk | final statement | closed account, Closure Confirmation | Core Banking Processing | causes Escheat Dormant Account | Record retention (5 yrs), closure confirmation | Close Account Record, Account Deactivation Step | https://legalclarity.org/what-happens-when-you-close-a-bank-account/ |
| Issue Dormancy Notice | process-step | 6 | Account Closure | Identify dormant accounts and send the Dormancy Notice before escheatment. | Unclaimed Property Officer | dormancy report | Dormancy Notice | Notification Services | causes Escheat Dormant Account | Dormancy rules, contact attempts | Send Dormancy Notice, Dormancy Notification Step | https://www.mtb.com/personal/checking-accounts/tips-on-managing-your-account/abandoned-funds |
| Escheat Dormant Account | process-step | 7 | Account Closure | Report and remit unclaimed funds to the state per escheatment rules. | Unclaimed Property Officer | Dormancy Notice, unclaimed balance | escheatment report, remitted funds | Regulatory Reporting Engine | — | Escheatment/CASS, state filing deadlines | Remit Unclaimed Property, Escheatment Step | https://www.incharge.org/blog/what-happens-to-dormant-bank-accounts/ ; https://www.witheisen.com/post/escheatment-process |

### 3.5 Overdraft Servicing (new)
Steps filed as `process-flows/overdraft-servicing/NN-<kebab-step>.md`.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Detect Insufficient Funds | process-step | 1 | Overdraft Servicing | Detect a presented debit item exceeding available balance. | Overdraft Operations Analyst | debit item, available balance | overdraft trigger | Core Banking Processing | causes Check Overdraft Opt-In | Available-balance accuracy | Identify Shortfall, Insufficient Funds Detection Step | https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html |
| Check Overdraft Opt-In | process-step | 2 | Overdraft Servicing | Check Reg E opt-in status for one-time debit/ATM items. | Overdraft Operations Analyst | overdraft trigger, Reg E Opt-In Record | opt-in status | Core Banking Processing | causes Evaluate Overdraft Limit | Reg E opt-in requirement | Verify Opt-In Status, Opt-In Check Step | https://www.consumer-action.org/alerts/articles/new_rule_on_overdraft_fees |
| Evaluate Overdraft Limit | process-step | 3 | Overdraft Servicing | Compare shortfall against the assigned overdraft coverage limit. | Overdraft Operations Analyst | opt-in status, shortfall | limit decision input | Core Banking Processing | causes Decide Pay Or Return | Overdraft coverage limit, fair-access criteria | Assess Overdraft Limit, Limit Evaluation Step | https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-12.html |
| Decide Pay Or Return | process-step | 4 | Overdraft Servicing | Decide to pay (overdraft) or return (NSF) the item. | Overdraft Operations Analyst | limit decision input | pay/return decision | Decision Rules Engine | causes Apply Overdraft Fee | Pay/return policy, decision audit | Make Pay Return Decision, Pay/Return Decision Step | https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html |
| Apply Overdraft Fee | process-step | 5 | Overdraft Servicing | Assess the applicable overdraft or NSF fee per disclosed schedule. | Overdraft Operations Analyst | pay/return decision | Overdraft Fee | Core Banking Processing | causes Notify Overdraft Outcome | Fee disclosure, NSF vs overdraft fee rules | Assess Overdraft Fee, Fee Application Step | https://www.consumerfinance.gov/about-us/blog/new-insights-on-bank-overdraft-fees-and-4-ways-to-avoid-them/ |
| Notify Overdraft Outcome | process-step | 6 | Overdraft Servicing | Notify the customer of the overdraft/NSF outcome and fee. | Overdraft Operations Analyst | Overdraft Fee, decision | customer notice | Notification Services | — | Notice timing, disclosure | Send Overdraft Notice, Outcome Notification Step | https://www.fdic.gov/consumer-resource-center/2021-12/overdraft-and-account-fees |

---

## 4. Supporting Concepts (roles, events, artifacts)

Flow columns (actor/inputs/outputs/depends_on/causes) left blank for these reference concepts.

| Canonical Name | type | level/order | parent process | definition | actor | inputs | outputs | depends_on | causes (next step) | controls | aliases | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Deposit Operations Clerk | role | — | — | Operations staff servicing deposit accounts: opening, maintenance and closure execution. | | | | | | | Deposit Ops Clerk, Account Servicing Clerk | https://openonline.53.com/product/service/apply/document/depositAccountRules |
| Statement Production Officer | role | — | — | Officer responsible for producing, rendering and delivering periodic account statements. | | | | | | | Statement Officer, Statement Production Clerk | https://www.ecfr.gov/current/title-12/chapter-X/part-1030 |
| Overdraft Operations Analyst | role | — | — | Analyst handling overdraft/NSF decisioning, limits and fee application under Reg E. | | | | | | | Overdraft Analyst, NSF Operations Analyst | https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-12.html |
| Unclaimed Property Officer | role | — | — | Officer managing dormancy identification, notices and escheatment/unclaimed-property reporting. | | | | | | | Escheatment Officer, Dormancy Officer | https://www.witheisen.com/post/escheatment-process |
| Account Opened Event | event | — | — | Business event signalling a new deposit account has been created and funded. | | | | | | | Account Established Event, New Account Opened | https://www.alogent.com/banking-definitions/customer-identification-program-cip |
| Statement Issued Event | event | — | — | Event signalling a periodic statement has been generated and delivered. | | | | | | | Statement Generated Event, Statement Delivered Event | https://www.ecfr.gov/current/title-12/chapter-X/part-1030 |
| Account Dormant Event | event | — | — | Event raised when an account exceeds its dormancy period without customer activity. | | | | | | | Dormancy Triggered Event, Inactivity Detected Event | https://www.incharge.org/blog/what-happens-to-dormant-bank-accounts/ |
| Account Closed Event | event | — | — | Event signalling a deposit account has been deactivated/closed. | | | | | | | Account Closure Event, Account Terminated Event | https://legalclarity.org/what-happens-when-you-close-a-bank-account/ |
| Overdraft Triggered Event | event | — | — | Event raised when a debit item exceeds available balance. | | | | | | | Insufficient Funds Event, NSF Triggered Event | https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html |
| Account Opening Form | artifact | — | — | Application document capturing applicant details and product selection at opening. | | | | | | | Account Application Form, New Account Form | https://www.alogent.com/banking-definitions/customer-identification-program-cip |
| Signature Card | artifact | — | — | Record of authorized signatories and account mandate. | | | | | | | Signatory Mandate, Account Mandate Card | https://www.compliancecohort.com/blog/cip-requirements-for-business-account-signers |
| Bank Account Statement | artifact | — | — | Periodic statement of account activity and balances delivered to the customer. | | | | | | | Account Statement, Periodic Statement | https://legalclarity.org/how-to-read-a-bank-statement-every-section-explained/ |
| Service Maintenance Request | artifact | — | — | Request to change account static data, mandate, stop payment or standing instruction. | | | | | | | Account Maintenance Request, Servicing Request | https://www.associatedbank.com/forms-and-disclosures/disclosures/deposit-account-agreement |
| Account Closure Request | artifact | — | — | Signed request to close a deposit account with balance disbursement instructions. | | | | | | | Closure Request, Close Account Application | https://www.sofi.com/learn/content/bank-letter-to-close-account/ |
| Dormancy Notice | artifact | — | — | Abandoned-property letter sent to a dormant account holder prior to escheatment. | | | | | | | Abandoned Property Letter, Pre-Escheatment Notice | https://www.mtb.com/personal/checking-accounts/tips-on-managing-your-account/abandoned-funds |
| Reg E Opt-In Record | artifact | — | — | Record of the consumer's affirmative opt-in to overdraft coverage of one-time debit/ATM items. | | | | | | | Overdraft Opt-In Record, Reg E Consent | https://www.consumer-action.org/alerts/articles/new_rule_on_overdraft_fees |
| Overdraft Fee | artifact | — | — | Fee assessed for paying an item into overdraft (distinct from an NSF return fee). | | | | | | | OD Fee, Insufficient Funds Fee | https://www.consumerfinance.gov/about-us/blog/new-insights-on-bank-overdraft-fees-and-4-ways-to-avoid-them/ |

---

## Summary counts

- New processes: **3** (Account Maintenance, Account Closure, Overdraft Servicing)
- Sub-processes: **11** (2-3 per process across all 5 processes)
- Process steps: **32** (7 + 7 + 6 + 7 + 5)
- Supporting concepts: **18** (4 roles, 5 events, 9 artifacts)
