---
title: Collateral & Customer Communications
type: capability
level: L1
capability-id: ONB-CCC
parent: Onboarding & Origination (ONB)
tags: [capability, disclosures, documents, communications, retail-banking]
aliases: [ONB-CCC, Collateral, Customer Communications, Disclosures]
---

# Collateral & Customer Communications (ONB-CCC)

**Parent:** [[Onboarding and Origination Capability Model|Onboarding & Origination (ONB)]]

This capability group covers the **documents and communications** that accompany origination: mandated disclosures, terms-and-conditions and agreement documents, welcome materials, physical card packaging, and the handling of communications that fail to reach the customer. In Canada this is a heavily regulated capability — disclosure content, timing, and format are prescribed by federal cost-of-borrowing regulations, provincial lending statutes, and FCAC guidance (see [[Canadian Regulatory Context]]).

## L2 Capabilities

### ONB-CCC-01 — Customer Disclosures

Presenting regulated information to the applicant at mandated points in the journey.

- **Pre-collection licensing and cost-of-borrowing disclosure.** Before any personal information is collected, the digital flow presents a province-specific disclosure step containing: the lender's provincial licence, downloadable disclosure documents, the applicable resident agreement identifier, the maximum allowable cost of borrowing under provincial regulation, the lender's actual cost, and a worked sample calculation (amount advanced, total cost of borrowing, total repayable, **APR**). The applicant must actively agree before advancing.
- **Dynamic recalculation:** the sample calculation uses a default illustrative amount on first view and recalculates with the applicant's selected amount when they revisit.
- **Province-specific content** — documents, regulatory text (e.g., payday-loan-act references), and regulator-approved educational links — is retrieved from the CMS keyed by province, never hardcoded; changing province mid-flow reloads the correct disclosure set.
- **Decision and outcome disclosures:** eligibility outcomes carry a disclaimer that eligibility is not final approval; flows are explicit about when a hard credit inquiry occurs and when no hard check applies; cooling-off-period messaging is presented for products carrying reapplication restrictions.
- **Pre-hard-inquiry product disclosure:** for cards, the disclosure statement and cardholder agreement summary are presented **before** the application is submitted for the hard-inquiry decision.

### ONB-CCC-02 — Welcome Kits

Post-approval welcome materials: account/product welcome packages (digital and print), getting-started guidance, fee schedules and key-terms summaries, and confirmation communications. Observed digital pattern: terminal confirmation screens summarizing what happens next ("application complete — funding in process"; "activate your card via email") followed by email confirmation with activation instructions. Welcome communications are the hand-off point into [[Activation and Enrolment]].

### ONB-CCC-03 — Card Carriers

The personalized carrier document mailed with a physical card: cardholder identification, activation instructions, summary terms, and marketing panels. Produced in coordination with [[Account Setup and Fulfillment|plastic production (ONB-ASF-04)]].

### ONB-CCC-04 — Envelopes / Inserts

Physical mail packaging and regulatory/marketing inserts accompanying cards, agreements, and welcome kits — including insert eligibility rules (which inserts may legally accompany which communications) and print-vendor management.

### ONB-CCC-05 — T&C Documents

The agreement documents themselves, and their execution.

- **Document set by product:** loans — Loan Agreement plus **PAD Agreement**; credit cards — **Cardholder Agreement** (always), PAD Agreement (when PAD established), and balance-protection insurance agreement (when elected). Optional creditor insurance adds its own certificate/agreement. Document counts vary by product and elections (observed range: two to seven documents per application).
- **E-signature patterns:** each document presented with an individual acknowledgement checkbox, inline preview, and download/print actions; a final binding **"I Agree"** action constitutes acceptance of all acknowledged documents; signed documents are saved to the customer's authenticated account. Declining an optional insurance produces its own signed waiver/agreement.
- **Provincial e-sign variation:** some provinces accept click-to-agree per document; others (observed: BC, NL, MB) require additional per-section checkboxes or initials — the signing experience is therefore province-configurable, with vendor e-sign (DocuSign-class) as the forward path.
- **Consent-text linkage:** every consent presented during capture links to the full text of the referenced document (terms, privacy policy).
- See [[Loan Finalization and Document Signing Flow]] for the full signing process.

### ONB-CCC-06 — Returned Mail

Handling undeliverable physical communications: returned card/PIN/welcome mail intake, account flagging and hold rules (e.g., blocking card activation on returned card mail as a fraud control), address-remediation outreach, and feedback into address-quality rules at capture ([[Application|ONB-APP-02]]).

## Content Management Pattern (Cross-Cutting)

All configurable customer-facing content — disclosure documents and labels, cost-of-borrowing parameters, regulatory text, option lists, outcome messaging, CTA labels and destinations — is **CMS-managed** (Contentful-class) and keyed by province, product, and entry context. The front end renders; legal/compliance owns content through the CMS workflow. This pattern is what makes province-aware compliance sustainable. See [[Integration and Decisioning Patterns]].

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Pre-Qualification Flow]] | ONB-CCC-01 |
| [[Loan Finalization and Document Signing Flow]] | ONB-CCC-01, 05 |
| [[Credit Card Application Flow]] | ONB-CCC-01, 02, 05 |
| [[Post-Qualification Application Flow]] | ONB-CCC-01 (entry consents and security messaging) |

## Related

[[Canadian Regulatory Context]] · [[AML KYC and Compliance]] · [[Account Setup and Fulfillment]]
