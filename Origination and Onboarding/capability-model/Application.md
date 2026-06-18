---
title: Application
type: capability
level: L1
capability-id: ONB-APP
parent: Onboarding & Origination (ONB)
tags: [capability, application, intake, pre-qualification, retail-banking]
aliases: [ONB-APP, Application Capability, Application Intake]
---

# Application (ONB-APP)

**Parent:** [[Onboarding and Origination Capability Model|Onboarding & Origination (ONB)]]

The Application capability group covers how a bank **receives, captures, manages, and reviews** a customer's request for a product — from the first click on an entry point through a complete, submitted application. It is the front door of origination and the primary determinant of conversion: friction here is the single largest driver of digital application abandonment.

## L2 Capabilities

### ONB-APP-01 — Intake

Receiving the expression of product interest and initiating an application session.

- **Entry-point management.** Applications originate from product pages, campaign links, branch referrals, calculators, and the authenticated dashboard. Each entry point encodes an **applied product** (e.g., URL parameters or campaign configuration), captured once at session start and persisted for the whole journey — the applicant applies for exactly one product per session, and the product cannot be switched mid-flow. Invalid or missing entry product values must not start the flow.
- **Channel routing.** Intake supports digital self-serve as primary, with structured hand-offs to assisted channels: a "finish at a branch" option saves the in-progress application server-side and routes the applicant to a branch locator; repeated verification failures surface a click-to-call path to the contact centre.
- **Province/jurisdiction gating.** The first interaction establishes the applicant's province, which gates product availability (a product–province availability matrix marks each product *online*, *retail-only*, or *not available*), drives disclosure content, and later determines verification routing. Where no product is digitally available in a province, intake blocks digital advancement and directs the applicant to branch or contact centre.

### ONB-APP-02 — Application Capture

Collecting application data through guided, validated, step-based forms.

- **Linear stepped flows** with persistent progress indication (percent complete and estimated time remaining), back navigation that preserves entered data, and cancel actions that always require confirmation before abandoning.
- **Field-level patterns:** legal name capture as a dedicated step; combined personal details (email, phone, date of birth, residency status); multi-select income sources driving **runtime-generated** income forms (only selected sources produce input fields); housing status and cost; and address capture with search/autocomplete (Canada Post-style address lookup), editable pre-population, and configurable rules such as whether P.O. boxes are permitted.
- **Validation behaviour:** validation triggers on step submission rather than field blur; all errors on a step surface simultaneously in a summary banner with a "go to first error" control plus inline messages; error copy is specific and actionable.
- **Consent capture at the point of data collection:** individually acknowledged consents (credit-bureau consent, terms and privacy consent required; marketing consent optional), each linking to full text — bulk acceptance of multiple consents in a single action is not permitted. (Consent *content* obligations live in [[AML KYC and Compliance]] and [[Canadian Regulatory Context]].)
- **Contact verification in-flow:** phone number verified by 6-digit OTP before financial data is collected, with resend support and a lockout-to-human path after repeated failures.

### ONB-APP-03 — Application Management

Managing the lifecycle and state of an application across sessions, channels, and statuses.

- **Session and state persistence:** the applied product, province, and collected data persist across the session; "save for later" allows authenticated applicants to suspend and resume; saved applications carry expiry policies.
- **Cross-channel continuity:** an application started online can be completed in-branch (server-side save plus branch staff access), and a desktop session can hand off a verification step to mobile and resume (see [[Identity Verification Flow]]).
- **Status management:** applications move through states such as *in progress*, *submitted*, *under manual review*, *approved*, *declined*, and *completed*, with status surfaced on the authenticated customer dashboard.
- **Reapplication controls:** policy-driven restrictions (e.g., a 14-day reapplication bar following inaccurate information), enforced server-side and warned about prominently in the UI before identity submission; cooling-off rules between consecutive short-term loans.

### ONB-APP-04 — Application Review

Reviewing captured data — by the applicant, and by the bank — before and after decisioning.

- **Applicant-side review:** consolidated review screens before submission. Returning, authenticated applicants see pre-populated data in summary cards with per-category edit actions and must explicitly confirm (or amend) before submission — pre-population never bypasses confirmation.
- **Income review and confirmation:** verified or self-declared income sources are presented as cards with edit/delete controls, a real-time recalculating income total, and a minimum-one-source rule before advancement (detail in [[Income Verification Flow]]).
- **Bank-side review:** applications carrying uploaded documentation route to a human review queue before an approval decision — see [[Manual Review Flow]].

### ONB-APP-05 — Up / Cross-Sell

Presenting additional or alternative products during origination.

- **Optional add-on products** offered in-flow: creditor insurance (loan protection plans) presented during loan setup with a single structured "rebuttal" confirmation when declined, and balance protection insurance on the card path — both strictly optional, with decline never blocking completion.
- **Alternative-product routing on ineligibility:** when the decision engine returns no eligibility for the applied product, the outcome screen offers a general "explore other products" path (e.g., prepaid cards) rather than dead-ending the applicant. In-scope alternates are never silently substituted for the applied product.
- **Post-funding cross-sell** is surfaced on the authenticated dashboard rather than inside the origination flow, keeping the application linear.

### ONB-APP-06 — Pre-Qualification

A soft-inquiry eligibility stage before the full application. Detailed end-to-end in [[Pre-Qualification Flow]].

- Lets the applicant learn whether they can proceed **without a hard credit inquiry** ("checking eligibility will not affect your credit score" trust messaging is a standard pattern).
- Collects the minimum decisioning dataset (identity, contact, residency, income, housing, address) and obtains an eligibility outcome from the decision engine ([[Adjudication and Underwriting]]).
- Pre-qual eligibility and post-qual approval are **distinct decisions for the same applied product**; eligibility ranges shown at pre-qual are indicative, with final terms presented only at approval.

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Pre-Qualification Flow]] | ONB-APP-01, 02, 03, 04, 06 |
| [[Post-Qualification Application Flow]] | ONB-APP-02, 03, 04 |
| [[Income Verification Flow]] | ONB-APP-02, 04 |
| [[Credit Card Application Flow]] | ONB-APP-02, 04, 05 |
| [[Manual Review Flow]] | ONB-APP-03, 04 |

## Related

[[Adjudication and Underwriting]] · [[AML KYC and Compliance]] · [[Data Requirements Reference]] · [[Canadian Regulatory Context]]
