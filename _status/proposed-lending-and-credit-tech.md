---
title: Proposed Lending & Credit Technology Decomposition
type: proposal
status: draft
author: tech-decomposition sub-agent
date: 2026-06-15
---

# Proposed Lending & Credit Technology Decomposition

Scope: enabling technology-capability decomposition for the Lending & Credit
domain, hung under the two EXISTING top-level technology capabilities in the
Core Processing technology domain — **Loan Origination Platform** and **Credit
Decisioning Engine** — plus a systems refresh.

Naming verified globally unique against `glossary/_canonical-names.md`. Tech
names deliberately kept distinct from business capability names (e.g. tech
"Credit Scoring Service" vs business "Credit Decisioning/Credit Assessment";
tech "Loan Product Configurator" vs business "Loan Origination").

Relationship verbs used (of the allowed 7): `derived_from`, `defined_in`,
`depends_on`, `related_to`.

## 1) Technology sub-capabilities

All `type = technology-capability`, `domain = Core Processing`.

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Application Intake Engine | technology-capability | L2 | Loan Origination Platform | Core Processing | Captures and validates inbound loan applications across channels, manages application state, eligibility pre-checks and routing into the origination workflow. | Application Capture Engine, Origination Intake Service | derived_from Loan Origination Platform; defined_in Core Processing; related_to Application Processing (business cap) | https://www.ncino.com/en-US/solutions/consumer-loan-origination-system ; https://www.temenos.com/en-us/solutions/suites/lifecycle-management/loan-origination/ |
| Document Capture & Verification | technology-capability | L2 | Loan Origination Platform | Core Processing | Collects, classifies and verifies borrower documents (ID, financials, statements) supporting the origination file, integrating OCR/IDP and e-signature. | Document Capture Service, Doc Verification Engine | derived_from Loan Origination Platform; defined_in Core Processing; depends_on Intelligent Document Processing | https://www.ncino.com/en-US/solutions/consumer-loan-origination-system ; https://www.finastra.com/lending/origination |
| Loan Product Configurator | technology-capability | L2 | Loan Origination Platform | Core Processing | Defines loan products, terms, eligibility parameters and workflow rules without code, enabling rapid product setup and multi-product origination. | Product Configurator, Lending Product Designer | derived_from Loan Origination Platform; defined_in Core Processing; related_to Loan Origination | https://www.temenos.com/en/solutions/lifecycle/loan-origination/ ; https://www.ncino.com/en-US/solutions/commercial-loan-origination-system |
| Offer & Pricing Engine | technology-capability | L2 | Loan Origination Platform | Core Processing | Generates risk-based pricing, rates and structured offers for an application, applying pricing strategies and producing presentable loan offers. | Loan Pricing Engine, Offer Generation Service | derived_from Loan Origination Platform; defined_in Core Processing; depends_on Credit Scoring Service | https://www.experianplc.com/newsroom/press-releases/2013/experian-announces-global-availability-of-powercurve-originations-1 ; https://www.temenos.com/en-us/solutions/suites/lifecycle-management/loan-origination/ |
| Disbursement Engine | technology-capability | L2 | Loan Origination Platform | Core Processing | Books the approved loan and executes funding/disbursement, coordinating account creation, fee handling and hand-off to servicing and the ledger. | Loan Booking & Funding, Funding Engine | derived_from Loan Origination Platform; defined_in Core Processing; depends_on Core Banking Processing | https://www.ncino.com/en-US/solutions/consumer-loan-origination-system ; https://www.finastra.com/lending/origination |
| Credit Scoring Service | technology-capability | L2 | Credit Decisioning Engine | Core Processing | Computes application and behavioural credit scores using scorecards and ML models, returning scores and contributing factors to the decision flow. | Scorecard Service, Credit Score Engine | derived_from Credit Decisioning Engine; defined_in Core Processing; depends_on Machine Learning Platform; related_to Credit Decisioning | https://neontri.com/blog/ai-credit-scoring/ ; https://www.provenir.com/platform/decisioning/ |
| Affordability Assessment Engine | technology-capability | L2 | Credit Decisioning Engine | Core Processing | Assesses borrower affordability and repayment capacity (income, expenditure, debt-to-income, stress tests) to support responsible-lending decisions. | Affordability Engine, Repayment Capacity Service | derived_from Credit Decisioning Engine; defined_in Core Processing; related_to Credit Risk Management | https://www.prosightfa.org/insights/harnessing-data-driven-strategies-for-a-deeper-understanding-of-loan-affordability/ ; https://www.inscribe.ai/loan-underwriting |
| Decision Rules Engine | technology-capability | L2 | Credit Decisioning Engine | Core Processing | Executes underwriting and product-offering rules (policy rules, cut-offs, strategy trees) to produce approve/decline/refer decisions and offer terms. | Underwriting Rules Engine, Policy Rules Engine | derived_from Credit Decisioning Engine; defined_in Core Processing; depends_on Credit Scoring Service | https://www.provenir.com/platform/decisioning/ ; https://sourceforge.net/software/compare/Experian-PowerCurve-Strategy-Management-vs-FICO-Blaze-Advisor/ |
| Bureau Data Integration | technology-capability | L2 | Credit Decisioning Engine | Core Processing | Connects to credit bureaus and alternative-data providers, retrieving and normalising credit reports and attributes for use in scoring and rules. | Bureau Connectivity Service, Credit Data Aggregation | derived_from Credit Decisioning Engine; defined_in Core Processing; depends_on Integration Platform | https://www.lendapi.com/blog/credit-decision-engine-unveiled-exploring-the-architecture-behind-smart-financial-decisions ; https://www.provenir.com/platform/decisioning/ |
| Adverse Action Generator | technology-capability | L2 | Credit Decisioning Engine | Core Processing | Produces compliant adverse-action reason codes and decline notices reflecting actual model/rule drivers, supporting explainability and regulatory obligations. | Adverse Action Service, Reason Code Generator | derived_from Credit Decisioning Engine; defined_in Core Processing; related_to Regulatory Compliance | https://www.lendapi.com/blog/from-data-to-decision-understanding-credit-decision-engine-algorithms ; https://oscilar.com/blog/ai-credit-scoring |

### L3 sub-capabilities (under the most important L2s)

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Income Verification Service | technology-capability | L3 | Affordability Assessment Engine | Core Processing | Verifies borrower income and employment from documents, payroll, open-banking or bureau sources to feed affordability and DTI calculations. | Income & Employment Verification, Payroll Verification Service | derived_from Affordability Assessment Engine; defined_in Core Processing; depends_on Bureau Data Integration | https://roundtables.us/guest-blog-income-verification/ ; https://www.inscribe.ai/loan-underwriting |
| Reject Inference Model | technology-capability | L3 | Credit Scoring Service | Core Processing | Statistical/ML model that infers likely performance of rejected or non-booked applicants to debias scorecards and widen the modelled population. | Reject Inference Engine, Inference Scorecard | derived_from Credit Scoring Service; defined_in Core Processing; depends_on Machine Learning Platform | https://www.experian.com/blogs/insights/reject-inference/ ; https://www.experian.com/blogs/insights/unique-approach-to-reject-inference-design/ |
| Strategy Design Studio | technology-capability | L3 | Decision Rules Engine | Core Processing | No-code authoring, simulation and champion/challenger testing environment for credit strategies and rules before deployment to the decision flow. | Strategy Authoring Studio, Champion-Challenger Workbench | derived_from Decision Rules Engine; defined_in Core Processing; related_to Analytics Platform | http://www.experian.com/strategy-management/powercurve.html ; https://sourceforge.net/software/compare/Experian-PowerCurve-Strategy-Management-vs-FICO-Blaze-Advisor/ |

## 2) Systems refresh

Notable lending/credit systems NOT already in the registry. `realizes` is an
EXISTING top-level technology capability (Loan Origination Platform or Credit
Decisioning Engine). `supersedes` populated for modern systems only.

Already covered (excluded): Black Knight Empower, Legacy Credit Scoring (legacy);
Zest AI, Upstart, Blend, nCino (modern).

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| Ellie Mae Encompass | legacy-system | Loan Origination Platform | — | ICE Mortgage Technology | Established on-premise/hosted mortgage loan origination system, long the dominant US mortgage LOS with deep compliance tooling. | Encompass, ICE Encompass, Ellie Mae | https://www.zeitro.com/blog/loan-origination-system-vendors-guide-to-choosing-comparing-and-optimizing-los-platforms ; https://www.loanpro.io/blog/best-loan-origination-software/ |
| Finastra LaserPro | legacy-system | Loan Origination Platform | — | Finastra | Long-standing loan documentation and origination platform for consumer, commercial and mortgage lending with strong compliance document generation. | LaserPro | https://www.finastra.com/lending/origination |
| FICO Origination Manager | legacy-system | Credit Decisioning Engine | — | FICO | Origination decisioning solution combining scorecards and decision rules to drive credit decisions and value-based offers during origination. | Origination Manager | https://slashdot.org/software/comparison/Experian-PowerCurve-Strategy-Management-vs-FICO-Origination-Manager/ |
| Experian PowerCurve | legacy-system | Credit Decisioning Engine | — | Experian | Component-based automated decision engine spanning data access, strategy design, decision automation and monitoring across the credit lifecycle. | PowerCurve, PowerCurve Strategy Management, PowerCurve Originations | http://www.experian.com/strategy-management/powercurve.html ; https://www.experianplc.com/newsroom/press-releases/2013/experian-announces-global-availability-of-powercurve-originations-1 |
| Temenos Origination | modern-system | Loan Origination Platform | Ellie Mae Encompass; Finastra LaserPro | Temenos | Cloud, omni-channel origination suite (Temenos Infinity) with instant multi-factor decisioning, lifting auto-decision rates and removing paper processes. | Temenos Infinity Origination, Infinity Origination | https://www.temenos.com/en-us/solutions/suites/lifecycle-management/loan-origination/ ; https://www.temenos.com/specialized/credit-unions-and-community/temenos-origination/ |
| MeridianLink | modern-system | Loan Origination Platform | Ellie Mae Encompass | MeridianLink | Cloud loan and account origination platform for credit unions and community banks with pre-built bureau integrations (Experian, Equifax, TransUnion). | MeridianLink Consumer, MeridianLink Opening | https://www.zeitro.com/blog/loan-origination-system-vendors-guide-to-choosing-comparing-and-optimizing-los-platforms |
| Provenir | modern-system | Credit Decisioning Engine | FICO Origination Manager; Experian PowerCurve | Provenir | Cloud-native, no-code AI decisioning platform connecting data, scoring and rules for instant credit decisions across the customer lifecycle. | Provenir AI, Provenir Decisioning | https://www.provenir.com/platform/decisioning/ |
