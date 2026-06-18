---
title: Process-to-Capability Mapping Matrix
type: reference
domain: banking-and-payments
tags: [reference, mapping, traceability, capability-model, process-flow]
aliases: [Mapping Matrix, Capability Matrix, Traceability Matrix]
---

# Process-to-Capability Mapping Matrix

Full traceability between the [[00 - Onboarding and Origination Index|library's]] process flows and the L2 capabilities of the Onboarding & Origination model. Step IDs (`PQ-`, `POST-`, `IV-`, `IDV-`, `FUND-`, `LF-`, `CC-`, `MR-`) are stable anchors matching the `Step XX-nn` headings inside each flow note. Legend: **P** = primary (the step *is* this capability in action) · **S** = supporting (the capability is exercised but not the step's purpose).

## Matrix — L1 Summary

| Process Flow | ONB-APP | ONB-ADJ | ONB-AKC | ONB-ASF | ONB-CCC | ONB-ACT |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| [[Pre-Qualification Flow]] | **P** | **P** | **P** | — | **P** | S |
| [[Post-Qualification Application Flow]] | **P** | **P** | **P** | **P** | S | S |
| [[Income Verification Flow]] | S | **P** | S | S | — | — |
| [[Identity Verification Flow]] | S | S | **P** | — | — | — |
| [[Funding and Repayment Setup Flow]] | S | — | — | **P** | S | — |
| [[Loan Finalization and Document Signing Flow]] | S | S | — | **P** | **P** | S |
| [[Credit Card Application Flow]] | **P** | **P** | S | **P** | **P** | **P** |
| [[Manual Review Flow]] | S | **P** | S | — | — | S |

## Matrix — Flow Step to L2 Capability

### [[Pre-Qualification Flow]]

| Step | L2 Capability | Role |
|---|---|---|
| `PQ-01` Entry point / applied product capture | ONB-APP-01 Intake | P |
| `PQ-02` Province selection & product gating | ONB-APP-01 Intake / ONB-AKC-03 Regulatory Check | P |
| `PQ-03` Licence & cost-of-borrowing disclosure | ONB-CCC-01 Customer Disclosures | P |
| `PQ-04` Loan amount selection | ONB-APP-02 Application Capture | P |
| `PQ-05` Name entry & reapplication warning | ONB-APP-02 / ONB-APP-03 Application Management | P |
| `PQ-05` Returning-user authentication | Identity/Auth domain (adjacent); ONB-APP-03 | S |
| `PQ-06` Personal details & consents | ONB-APP-02 / ONB-AKC-01 KYC / ONB-AKC-04 Credit Check (consent) | P |
| `PQ-07` Phone OTP verification | ONB-APP-02; Identity/Auth domain | P |
| `PQ-08` Income, housing, address capture | ONB-APP-02 (feeds ONB-ADJ-05/06) | P |
| `PQ-08R` Returning-user data review | ONB-APP-04 Application Review | P |
| `PQ-09` Eligibility decision | ONB-ADJ-01/02/03 Decisioning · ONB-ADJ-04 Bureau (soft) | P |
| `PQ-09` Eligibility / general outcome screens | ONB-APP-06 Pre-Qualification / ONB-APP-05 Up-Cross-Sell | P |
| `PQ-09` Finish at a branch | ONB-APP-01 Intake (channel hand-off) / ONB-APP-03 | S |

### [[Post-Qualification Application Flow]] (orchestration-owned steps)

| Step | L2 Capability | Role |
|---|---|---|
| `POST-01` Entry screen, prerequisites, carrier-disclosure consent | ONB-APP-02 / ONB-AKC-01 / ONB-CCC-01 | P |
| `POST-CHROME` Flow chrome, save-for-later, cancel confirmation | ONB-APP-03 Application Management | P |
| `POST-06` Approved results (hard decision) | ONB-ADJ-01/02/03/04 | P |
| `POST-06` Decline / alternate outcome | ONB-ADJ-01 / ONB-APP-05 | S |
| `POST-09` Completed application & dashboard hand-off | ONB-ASF-01 / ONB-ACT-01 / ONB-CCC-02 | P |

### [[Income Verification Flow]]

| Step | L2 Capability | Role |
|---|---|---|
| `IV-A1` Aggregator widget connection | ONB-ADJ-06 Risk Assessment (verified income evidence) | P |
| `IV-A2` Exit-state handling & fallback routing | ONB-APP-03 | S |
| `IV-B1` Manual income entry + document upload | ONB-APP-02 / ONB-ADJ-05 Underwriting | P |
| `IV-A3`/`IV-B2` Income review, edit/delete, totals | ONB-APP-04 Application Review | P |
| `IV-A3`/`IV-B2` Confirmation & product-aware routing | ONB-APP-03 | S |

### [[Identity Verification Flow]]

| Step | L2 Capability | Role |
|---|---|---|
| `IDV-00` Engine-gated invocation | ONB-ADJ-03 Decision Engine | P |
| `IDV-01` Intro & trust content | ONB-CCC-01 (trust messaging) | S |
| `IDV-02` Desktop QR hand-off & session linking | ONB-APP-03 Application Management | S |
| `IDV-03` ID scan + selfie (provider) | ONB-AKC-08 ID Validation / ONB-AKC-01 KYC | P |
| `IDV-04` Success gating of approval | ONB-ADJ-06 Risk Assessment | P |
| `IDV-04` Failure fallback | → [[Manual Review Flow]] | S |

### [[Funding and Repayment Setup Flow]]

| Step | L2 Capability | Role |
|---|---|---|
| `FUND-01` Payout method selection | ONB-ASF-02 Funding Account | P |
| `FUND-02` Embedded debit-card capture | ONB-ASF-02 (via embedded provider) | P |
| `FUND-03` Repayment bank account (PAD groundwork) | ONB-ASF-02 | P |
| `FUND-04` Path-aware submission routing | ONB-APP-03 | S |

### [[Loan Finalization and Document Signing Flow]]

| Step | L2 Capability | Role |
|---|---|---|
| `LF-01` Approved-offer presentation | ONB-ADJ-01 (hand-off) | S |
| `LF-02` Loan configuration within approved range | ONB-ASF-01 Account Opening | P |
| `LF-02`/`LF-03` Creditor-insurance offer & rebuttal | ONB-APP-05 Up/Cross-Sell | P |
| `LF-04` Regulated cost summaries | ONB-CCC-01 Customer Disclosures | P |
| `LF-05` Document signing (Loan + PAD agreements) | ONB-CCC-05 T&C Documents | P |
| `LF-05`/`LF-06` Submission & completion | ONB-ASF-01 / ONB-ACT-01 | P |

### [[Credit Card Application Flow]]

| Step | L2 Capability | Role |
|---|---|---|
| `CC-02` Application acknowledgement before hard inquiry | ONB-APP-02 / ONB-AKC-03/04 / ONB-CCC-01 | P |
| `CC-03` Card approval & limit assignment | ONB-ADJ-01/02/03/04 | P |
| `CC-04` PAD confirm/entry | ONB-ASF-02 | P |
| `CC-05` Balance-protection offer | ONB-APP-05 | P |
| `CC-06` Card document signing | ONB-CCC-05 | P |
| `CC-07` Confirmation & email activation hand-off | ONB-ASF-03/05/06 / ONB-ACT-01/04 / ONB-CCC-02 | P |

### [[Manual Review Flow]]

| Step | L2 Capability | Role |
|---|---|---|
| `MR-01` Submission & session pause | ONB-APP-03 | P |
| `MR-01` Review-pending status on dashboard | ONB-APP-03 / ONB-ACT-01 | S |
| `MR-02` Document verification | ONB-ADJ-05 Underwriting | P |
| `MR-02` EDD / reporting escalation | ONB-AKC-06 / ONB-AKC-07 | S |
| `MR-03` Post-review decision & resume | ONB-ADJ-01 / ONB-APP-03 | P |

## Coverage Notes

- **Strongly evidenced by source artifacts:** ONB-APP (all L2s), ONB-ADJ (all L2s), ONB-AKC-01/03/04/08, ONB-ASF-01/02/06, ONB-CCC-01/05, ONB-ACT-01.
- **Generalized from standard Canadian retail-bank practice** (thin or implicit in source artifacts): ONB-AKC-02/05/06/07 (AML program mechanics, sanctions, EDD, reporting), ONB-ASF-03/04/05 (issuance/production detail), ONB-CCC-02/03/04/06 (physical collateral), ONB-ACT-02/03/05/06 (mobile, wallet, virtual-card, renewal detail). These are documented at capability level in the L1 notes so the model remains complete for querying, with the generalization flagged.
