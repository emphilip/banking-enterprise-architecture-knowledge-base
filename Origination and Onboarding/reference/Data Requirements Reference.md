---
title: Data Requirements Reference
type: reference
domain: banking-and-payments
tags: [reference, data, data-elements, intake, verification, contracts]
aliases: [Data Reference, Canonical Data Elements, Data Dictionary]
---

# Data Requirements Reference

Canonical data elements collected, derived, or exchanged across the onboarding and origination flows, generalized for an average Canadian retail bank. Each group notes where the data is captured, how it is validated, and which capability consumes it. This is the data-side companion to the [[Process-to-Capability Mapping Matrix]].

## D1 — Pre-Qualification Intake (Applicant-Entered)

Captured in [[Pre-Qualification Flow]]; consumed by [[Application|ONB-APP]] App Capture and the soft-inquiry decision ([[Adjudication and Underwriting|ONB-ADJ]]).

| Element | Notes |
|---|---|
| Province of residence | First gate; drives product availability, disclosure content, and downstream flow configuration |
| Applied product | Single product per session, set by entry point (term loan, short-term loan, or credit card) — not user-selected mid-flow |
| Requested loan amount | Slider within product min/max (e.g., $100–$25,000); **skipped for card applications** |
| Legal first / last name | Entry triggers a re-application warning if a recent application (e.g., within 14 days) exists |
| Email address | Identity anchor; later immutable for e-Transfer disbursement (fraud control) |
| Mobile phone number | Verified by 6-digit OTP (3 failures → assisted/click-to-call path) |
| Date of birth | Age-of-majority validation per province |
| Residency status | Eligibility input |
| Residential address | Autocomplete-assisted; PO boxes permitted at this stage |
| Housing tenure + monthly cost | Rent/own selector plus dollar amount |
| Income sources (multi-select) | Drives a runtime-generated income form — one amount block per selected source |
| Income amounts per source | Net figures per source type |
| Total household income | Separate aggregate field |

## D2 — Consents (Captured with D1)

Individually acknowledged checkboxes; stored with timestamp and version. Consumed by [[AML KYC and Compliance|ONB-AKC]] and [[Canadian Regulatory Context|regulatory]] record-keeping.

| Consent | Required? | Purpose |
|---|---|---|
| Credit-report consent | Required | Authorizes soft inquiry (and later hard inquiry only after explicit card acknowledgement) |
| Terms & conditions / privacy | Required | Contractual and PIPEDA basis |
| Marketing communications | Optional | CASL express-consent; never blocks progression |
| Mobile-carrier verification consent | Required at post-qual entry | Gates entry to the verified application (PICRA-style carrier data check) |

## D3 — Pre-Qualification Decision Payload

Submitted to / returned by the decision engine (see [[Integration and Decisioning Patterns]]).

- **Request:** D1 + D2 identifiers, province, applied product.
- **Response:** outcome code (eligible / not eligible), pre-qualified amount or range, product attributes, finish-in-branch option flag. Declines return a generic alternatives outcome — no counter-offer payload.

## D4 — Aggregator-Derived Income (Verified Path)

Produced by the financial data aggregator in [[Income Verification Flow]].

| Element | Editability |
|---|---|
| Source bank (badge/attribution) | Read-only |
| Income source / employer name | Editable |
| Employer phone | Editable |
| Previous-month income | Editable |
| Direct-deposit indicator | Editable |
| Verified monthly amount(s) → "Total verified monthly income" | Derived; not free-text editable |

Constraints: minimum one income source must remain; deletion requires confirmation; **no add-source CTA** on the aggregator path (additions go through manual verification).

## D5 — Manual Income Submission (Unverified Path)

Captured on the manual income form; carries an "Unverified Income" badge until reviewed (1–3 business days) via [[Manual Review Flow]].

Income source type · employer name · pay frequency · employment start/end dates · net pay amount · direct-deposit indicator · **proof-of-income document** (file browse or photo capture).

## D6 — Bank Account for Disbursement and Repayment

Captured in [[Funding and Repayment Setup Flow]] (direct-deposit disbursement, and PAD setup):

| Element | Format |
|---|---|
| Bank / financial institution name | Selected or derived |
| Transit number | 5 digits |
| Institution number | 3 digits |
| Account number | Institution-specific length |

Rules: a **single account** serves both disbursement and repayment; if sourced from the aggregator it is **read-only/immutable**; the **primary account** heuristic (highest net deposits) selects the PAD account when multiple are linked.

## D7 — Debit Card Disbursement

Captured **inside the embedded card-capture vendor component only** (PCI isolation — see [[Integration and Decisioning Patterns]]). The bank's journey stores a success/failure event and a vendor reference token, never the PAN.

## D8 — Final Approval Payload

Returned by the decision engine after verification (hard inquiry where applicable):

Applied product · outcome · approved amount range (loans, e.g., term loan up to ~$3,500, short-term loan up to ~$1,500 in the source) or engine-set credit limit (cards) · pricing and term attributes. Rendered read-only on the approval screen; bounds all subsequent selections.

## D9 — Loan Configuration Selections

Captured at loan setup within the D8 envelope ([[Loan Finalization and Document Signing Flow]]):

Selected principal (slider within approved range) · payment frequency · term · optional creditor-insurance election (with per-period premium disclosed; a decline triggers a one-time benefits rebuttal screen, after which either choice proceeds). Short-term loans instead render a regulated cost summary including the fee per $100 borrowed (federally capped — see [[Canadian Regulatory Context]]).

## D10 — Card Acknowledgement and Setup

Card path equivalents ([[Credit Card Application Flow]]): read-only application summary with **explicit acknowledgement recorded before the hard inquiry**; PAD account details (immutable if aggregator-linked, editable form otherwise); optional balance-protection election (opt-out may require a signed agreement).

## D11 — Signing Artifacts

Captured at e-signature ([[Loan Finalization and Document Signing Flow]]):

Per-document checkbox acknowledgements (loan agreement + PAD agreement; or cardholder agreement plus conditional PAD/balance-protection agreements) · signature event ("I Agree" = submission) · timestamps · executed documents persisted to the customer's account record (FINTRAC/FCAC record-keeping).

## D12 — Manual Review Case Payload

Assembled when any flow exits to [[Manual Review Flow]]: applicant reference, triggering reason (income proof, IDV failure, repeated aggregator errors), uploaded evidence, and application snapshot. Submission is terminal for the session — the applicant lands on a dashboard pending review, and no further in-session steps (approval, setup, signing) occur.

## Cross-Cutting Data Rules

- **Provenance everywhere:** every income and account element carries its source (aggregator-verified vs. manually declared) so adjudication can weight it.
- **Immutability after verification:** verified emails and aggregator-linked accounts are locked downstream.
- **Province as a key:** province participates in nearly every contract — content, availability, validation, and signing rules.
- **Returning users:** authenticated returning applicants skip re-entry of stable D1 elements and instead confirm a consolidated data-review screen.

## Source Traceability

Element sets derive from the Momentum pre-qual data matrix and post-qual requirements (intake fields, aggregator income records, manual income form, bank-account fields, approval payloads, loan/card setup, signing), generalized to vendor-neutral roles and average-bank terminology. See [[Glossary]] for term definitions.
