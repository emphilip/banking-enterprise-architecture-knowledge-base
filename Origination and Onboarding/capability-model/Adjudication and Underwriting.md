---
title: Adjudication & Underwriting
type: capability
level: L1
capability-id: ONB-ADJ
parent: Onboarding & Origination (ONB)
tags: [capability, adjudication, underwriting, credit-decisioning, decision-engine, retail-banking]
aliases: [ONB-ADJ, Adjudication, Underwriting, Credit Decisioning]
---

# Adjudication & Underwriting (ONB-ADJ)

**Parent:** [[Onboarding and Origination Capability Model|Onboarding & Origination (ONB)]]

Adjudication & Underwriting covers how the bank **decides** — evaluating an application against credit policy, risk appetite, bureau data, and verified applicant data to produce eligibility and approval outcomes, amounts, limits, and terms. In the modern Canadian retail bank this is a centralized, engine-driven capability: channels collect data and render outcomes; the decision engine owns the logic.

## L2 Capabilities

### ONB-ADJ-01 — Credit Decisioning

The end-to-end discipline of producing a credit decision for an application.

- **Two-decision pattern.** Origination produces (at least) two distinct decisions for the same applied product: a **pre-qualification eligibility decision** (soft inquiry, indicative ranges, gates entry to the full application) and a **post-qualification approval decision** (hard inquiry where applicable, final approved amount/limit and terms, gates fulfillment). Both are evaluated in the context of the single applied product captured at intake.
- **Decision context.** Inputs include the applied product, applicant identity/contact/residency data, self-declared and verified income, housing costs, address, consents, bureau data, and verification outcomes (income verification method and results, identity verification result).
- **Outcome handling.** Eligible/approved outcomes carry product attributes (amount ranges, rate, fee, term structure) for rendering; ineligible/declined outcomes route to general alternative-product messaging or defined decline screens — the front end never overrides the engine and never lets the applicant pursue a product the engine did not return.

### ONB-ADJ-02 — Instant Decision

Real-time, automated decisions returned synchronously within the digital session.

- Pre-qual eligibility returns immediately on submission; post-qual approval returns immediately after income/identity verification and (for cards) application acknowledgement.
- Instant decisioning is conditional on **straight-through data**: when an application carries manually uploaded documents (proof of income, proof of banking), the instant path is suspended and the application diverts to [[Manual Review Flow]] before any approval decision is rendered.
- The engine can also return **conditional decisions** — e.g., "approved subject to identity verification" — which the orchestration layer translates into conditional flow steps (see [[Identity Verification Flow]]).

### ONB-ADJ-03 — Decision Engine

The centralized rules/decisioning platform (e.g., Provenir-class, FICO-class, or in-house) that owns eligibility, approval, and step-gating logic.

- **Single source of decision truth:** eligibility criteria, decisioning logic, decision codes, approved amounts/limits, and which product combinations apply are owned by the engine and are explicitly out of scope for channel front ends.
- **Step gating:** beyond approve/decline, the engine gates conditional journey steps — most notably whether identity verification is required for a given applicant — making the journey itself risk-adaptive.
- **Champion/challenger and policy management** (strategy versioning, decision audit) belong to this capability even where not visible in the customer journey.
- See [[Integration and Decisioning Patterns]] for the integration contract.

### ONB-ADJ-04 — Bureau Access

Connectivity to Canadian credit bureaus (Equifax Canada, TransUnion Canada) and management of inquiry types.

- **Soft inquiries** support pre-qualification without affecting the applicant's score; the consent and trust messaging obligations around this are significant (see [[Canadian Regulatory Context]]).
- **Hard inquiries** support final approval; flows must be explicit about exactly when a hard credit check occurs, and disclosures/agreements that must precede the hard inquiry (e.g., the card application acknowledgement) are sequenced before it.
- Bureau consent is captured as an individually acknowledged, required consent during application capture ([[Application]] ONB-APP-02).
- Bureau data feeds both credit decisioning and identity verification (knowledge-based matching), and partial-match handling policy (decline vs. remediation) is a defined decision point.

### ONB-ADJ-05 — Underwriting

Human and policy-based evaluation beyond automated rules.

- **Manual underwriting/review queues** for applications with uploaded documentation: trained staff verify proof-of-income and proof-of-banking documents against declared data within a published service level (typically 1–3 business days), then trigger the approval decision. See [[Manual Review Flow]].
- **Verification standards:** document-to-declaration matching (the system warns applicants that uploaded document data must match entered data), eligible-income-type policies per product, and operational rules layered on top of engine rules for review-to-approval transitions.
- **Capacity assessment:** affordability inputs — income by source, total household income, housing cost, rent/own status — are mandatory capture items because they feed debt-servicing evaluation.

### ONB-ADJ-06 — Risk Assessment

Application-level risk evaluation feeding the decision.

- Aggregates bureau risk, income stability signals (verified vs. unverified income, direct-deposit indicators, deposit history from account aggregation), identity risk (IDV outcome, phone intelligence/PICRA-style mobile carrier checks), and policy risk (province, product, reapplication history).
- Determines **risk-based step-up**: higher-risk applications receive identity verification requirements and/or manual review; lower-risk applications proceed straight through.
- Interfaces with the enterprise **Fraud & Risk** and **Credit Risk** domains (fraud detection, credit risk assessment, credit limits) — origination risk assessment is the application-time instantiation of those enterprise capabilities.

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Pre-Qualification Flow]] | ONB-ADJ-01, 02, 03, 04 (soft) |
| [[Post-Qualification Application Flow]] | ONB-ADJ-01, 02, 03, 04 (hard), 06 |
| [[Income Verification Flow]] | ONB-ADJ-05, 06 |
| [[Identity Verification Flow]] | ONB-ADJ-03 (gating), 06 |
| [[Credit Card Application Flow]] | ONB-ADJ-01, 02, 03, 04 |
| [[Manual Review Flow]] | ONB-ADJ-05 |

## Related

[[Application]] · [[AML KYC and Compliance]] · [[Integration and Decisioning Patterns]] · [[Canadian Regulatory Context]]
