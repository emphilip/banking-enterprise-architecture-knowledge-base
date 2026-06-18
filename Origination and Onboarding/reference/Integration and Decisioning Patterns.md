---
title: Integration and Decisioning Patterns
type: reference
domain: banking-and-payments
tags: [reference, architecture, integration, decision-engine, vendors, patterns]
aliases: [Integration Patterns, Decisioning Patterns, Vendor Integration Reference]
---

# Integration and Decisioning Patterns

The origination flows in this library are orchestrations over a small set of external and internal services. This note generalizes the integration architecture observed in the source artifacts into reusable patterns for an average Canadian retail bank, so each pattern can be reasoned about independently of any specific vendor.

## 1. Decision Engine as the Single Source of Credit Truth

The front-end journey **never implements credit logic**. Every eligibility or approval outcome is produced by a centralized decision engine that consumes application data, bureau data, and policy rules, and returns a structured decision the journey merely renders and routes on.

Key properties observed and generalized:

- **Two-decision pattern.** Origination involves (at minimum) two distinct decisions: a **soft-inquiry pre-qualification decision** at the end of intake (see [[Pre-Qualification Flow]]) and a **hard-inquiry final adjudication** after verification is complete (see [[Post-Qualification Application Flow]]). Each has its own data contract, bureau-inquiry type, and consent prerequisite.
- **Decision gating of journey steps.** The engine's response controls which screens exist for a given applicant — e.g., whether identity verification is required at all is a decision-engine flag, not front-end logic (see [[Identity Verification Flow]]).
- **Outcome as structured contract.** Decisions return the applied product, an outcome code, an approved amount or range (loans) or an engine-set limit (cards), and pricing/term attributes. The journey renders these read-only; the applicant can select *within* the approved envelope (e.g., a loan amount slider bounded by the approved range) but never beyond it.
- **No counter-offer improvisation.** A declined applicant is routed to a generic alternatives message; the front end does not substitute or invent fallback products that the engine did not return.

This pattern maps to [[Adjudication and Underwriting|ONB-ADJ]] capabilities (decision engine, instant decision, bureau access) and keeps credit policy auditable in one place.

## 2. Financial Data Aggregator (Bank-Linking) Boundary

Income and account verification uses an embedded **financial data aggregator** widget (the generic role behind vendor names like Flinks or Plaid in the Canadian market):

- **Embedded widget, vendor chrome visible.** The aggregator's UI renders inside the bank's journey; the applicant authenticates to their own bank inside that boundary. The host journey never sees or stores online-banking credentials.
- **Defined exits, not shared state.** The integration contract is a set of exit events the host journey routes on: *success with data*, *success with zero usable income*, and *linking error*. Each exit has a designed destination (see [[Income Verification Flow]]) — verified-income review, an empty-state recovery screen, or a fallback to manual verification.
- **Failure budget.** Repeated linking failures (e.g., a second error) escalate to the manual path rather than looping the applicant indefinitely.
- **Derived data is read-mostly.** Aggregator-derived income records are displayed with source-bank attribution and only narrowly editable (employer details, recent-month figures); the verified amounts themselves are not free-text editable. Aggregator-linked bank accounts reused for pre-authorized debits are **immutable** in later steps (see [[Funding and Repayment Setup Flow]]) — verification value would be destroyed by post-hoc edits.
- **Jurisdictional switches.** Aggregator availability is a per-province configuration (one province in the source prohibits the aggregator path entirely, forcing manual verification). The pattern: capability availability is policy-configured per jurisdiction, not hard-coded.

## 3. Identity Verification (IDV) Provider Boundary

Document-plus-biometric identity verification is delegated to a specialist IDV provider:

- **Triggered, not universal.** The decision engine flags when IDV is required; the journey inserts the step only then.
- **Channel handoff.** Desktop applicants are handed to a mobile device via QR code because capture (ID front/back, selfie video) requires a camera; session state must survive the device handoff and return the result to the originating application.
- **Binary contract with manual fallback.** The provider returns pass/fail; pass is a precondition of final approval, fail routes to [[Manual Review Flow]] rather than terminating the application.
- The pattern implements FINTRAC's government-issued photo ID method (see [[Canadian Regulatory Context]]) and maps to ONB-AKC-08 *ID Validation*.

## 4. Embedded Card-Capture (PCI Isolation) Pattern

Instant disbursement to a debit card uses an embedded third-party capture component:

- Card PAN entry occurs **inside the vendor's hosted component**; the bank's systems never touch raw card data, keeping the journey out of most PCI-DSS scope.
- Like the aggregator, the component is a **black box with launch and exit contracts**: the journey launches it with a session/context token and resumes on a success or failure event, with no visibility into intermediate states.

## 5. CMS-Driven Jurisdictional Content

All regulated and province-variable content — lender-licence numbers, cost-of-borrowing disclosures, cost-per-$100 examples, product availability messaging — is served from a **headless CMS keyed by province and product**:

- Compliance and legal teams update disclosure content without code releases.
- The journey resolves `(province, product)` to a content bundle at runtime; the same screen skeleton renders different statutory content in different provinces.
- Province also gates **flow structure**, not just copy: product availability matrices, e-signature rules, cooling-off periods, and aggregator availability are all province-keyed configuration (see [[Canadian Regulatory Context]]).

## 6. The Black-Box Vendor Pattern (General Form)

Patterns 2–4 are instances of one general integration discipline that recurs across the flows:

1. **Launch contract** — the journey opens the vendor component with a scoped context (session token, applicant reference, product context).
2. **Opaque interior** — the journey makes no assumptions about, and takes no dependency on, the vendor's internal screens or sequence.
3. **Enumerated exits** — every vendor outcome is one of a small enumerated set, and each has a designed journey destination, including failure and abandonment.
4. **Manual fallback** — every automated vendor path has a human-reviewed alternative ([[Manual Review Flow]]) so a vendor outage degrades service rather than blocking origination.
5. **Provenance retained** — data acquired through a vendor carries its source (e.g., bank-badged income records, "unverified" badges on manual submissions) so downstream adjudication can weight it appropriately.

## Capability Mapping

| Pattern | Primary capabilities |
|---|---|
| Decision engine | [[Adjudication and Underwriting|ONB-ADJ]] — Decision Engine, Instant Decision, Bureau Access |
| Data aggregator | ONB-ADJ Risk Assess; [[Account Setup and Fulfillment|ONB-ASF]] Funding Account |
| IDV provider | [[AML KYC and Compliance|ONB-AKC]] — ID Validation, KYC |
| Card capture | ONB-ASF — Funding Account (disbursement rail) |
| CMS content | [[Collateral and Customer Communications|ONB-CCC]] — Customer Disclosures, T&C Documents |
| Manual fallback | [[Application|ONB-APP]] App Review; ONB-AKC EDD |

## Source Traceability

Generalized from the Momentum post-qualification requirements (decision-engine gating, aggregator exits, IDV handoff, embedded card capture, manual-review fallback) and pre-qualification requirements (CMS-managed provincial disclosure, soft-inquiry decisioning), with vendor names abstracted to roles. See [[Process-to-Capability Mapping Matrix]] for step-level mappings and [[Data Requirements Reference]] for the data contracts these integrations exchange.
