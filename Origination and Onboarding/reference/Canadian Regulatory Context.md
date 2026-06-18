---
title: Canadian Regulatory Context
type: reference
domain: banking-and-payments
jurisdiction: canada
tags: [reference, regulation, canada, fintrac, fcac, compliance, disclosure, lending]
aliases: [Regulatory Context, Canadian Regulations, Compliance Reference]
---

# Canadian Regulatory Context for Onboarding & Origination

The regulatory framework an average Canadian retail bank or consumer lender must satisfy during origination, mapped to the capabilities and flow steps where each obligation lands. This note generalizes the compliance behaviours observed in the source flows and grounds them in the governing regimes. *(Reference summary, not legal advice; verify current requirements with counsel and primary sources.)*

## 1. Anti-Money Laundering — PCMLTFA / FINTRAC

The *Proceeds of Crime (Money Laundering) and Terrorist Financing Act* and its regulations, administered by **FINTRAC**, drive [[AML KYC and Compliance|ONB-AKC]]:

- **Client identification** before opening accounts or entering prescribed transactions, via accepted methods: **government-issued photo ID** (digital document authenticity verification qualifies — the basis of [[Identity Verification Flow]]), the **credit-file method** (Canadian bureau file of sufficient age), or the **dual-process method** (two reliable independent sources). Layered approaches — OTP phone verification, carrier-data checks, bureau matching plus digital IDV — are standard practice.
- **PEP/HIO screening**, beneficial-ownership determination (entity accounts), ongoing monitoring, **suspicious transaction reporting**, and record-keeping (identification records, consents, and signed agreements retained — the flows persist signed documents to the customer's account).
- **Compliance program** requirements: appointed officer, documented policies, risk assessment, training, and effectiveness review — the institutional scaffolding behind ONB-AKC-02/05/06/07.

## 2. Cost-of-Borrowing Disclosure — Federal and Provincial

The disclosure behaviour in [[Pre-Qualification Flow]] (licence and cost disclosure **before any personal information**, active agreement required) and the regulated cost summaries in [[Loan Finalization and Document Signing Flow]] implement:

- **Federal (banks):** the Cost of Borrowing Regulations under the *Bank Act* and the FCAC-supervised **Financial Consumer Protection Framework** — pre-agreement disclosure of APR, total cost, term, and fees in clear, prominent language; express consent for optional products (relevant to creditor-insurance and balance-protection offers); complaint-handling disclosure.
- **Provincial (non-bank lenders and payday products):** lender licensing per province, payday-loan acts mandating display of the **maximum allowable cost per $100 borrowed**, the lender's actual cost, worked examples (amount advanced, total cost of borrowing, total repayable, APR), statutory references, and links to regulator-approved educational materials — exactly the content set observed on the disclosure screen, CMS-managed per province.
- **High-cost-credit regimes** in several provinces (e.g., BC, AB, MB, QC) add licensing, disclosure, and cancellation-rights obligations for credit above rate thresholds.

## 3. Criminal Interest Rate and Payday Caps (Current State)

Effective **January 1, 2025**, federal amendments lowered the **criminal interest rate** to **35% APR** (from the former 60% EAR ≈ 48% APR), and the Criminal Interest Rate Regulations imposed a **federal cap of $14 per $100 borrowed** on payday loans in provinces with approved payday regimes, harmonizing previously varied provincial caps, with dishonoured-payment fees limited to $20. Exemptions apply to certain commercial loans ($10,000–$500,000 at ≤48% APR; >$500,000 uncapped) and small pawn loans. Origination impact: product pricing, the cost-per-$100 disclosures rendered in-flow, and short-term-loan cost summaries (loan fee per $100, total cost of borrowing) must reflect these ceilings.

## 4. Credit Reporting and Inquiry Consent

- **Express consent** before any bureau inquiry, governed by provincial credit/consumer reporting acts and PIPEDA — implemented as the individually acknowledged, required credit-report consent at capture.
- **Soft vs. hard inquiries:** pre-qualification uses soft inquiries with explicit "will not affect your credit score" messaging; flows must be explicit about exactly when a hard inquiry occurs (the card path's acknowledgement-before-hard-check sequencing) and when a product involves no hard check at all.
- Bureaus: **Equifax Canada** and **TransUnion Canada**; Québec adds credit-assessment-agent obligations under its specific regime.

## 5. Privacy and Consent — PIPEDA / Provincial / CASL

- **PIPEDA** (and Québec's Law 25, plus AB/BC PIPAs): meaningful, purpose-specific consent for collection, use, and disclosure — the architecture of individually acknowledged consents linking to full policy text, with no bulk acceptance, implements this. Pre-checked consent boxes are a flagged regulatory risk (opt-in default expected for non-essential consents).
- **CASL:** marketing consent is express, optional, and never blocks the application — exactly the observed pattern.
- **Mobile-carrier disclosure consent** (PICRA-style): a specific, named consent authorizing the carrier to disclose number and account data **solely for identity verification and fraud protection** — purpose-limited consent done correctly.
- **Third-party data flows:** aggregator credentials/transaction data, IDV biometrics, and embedded card capture each require purpose-limited consent, vendor due diligence (OSFI **Guideline B-10** third-party risk for federally regulated institutions), and data-residency consideration.

## 6. Payments — PAD, e-Transfer, EFT

- **Payments Canada Rule H1** governs pre-authorized debits: a compliant **PAD agreement** (mandatory elements, pre-notification, cancellation rights) signed before debiting — the PAD Agreement executed at [[Loan Finalization and Document Signing Flow|document signing]] and on the card path.
- Canadian account identification — **institution number (3 digits), transit number (5 digits), account number** — is the canonical capture set on bank-account screens.
- **Interac e-Transfer** disbursement rides Interac rules and the bank's e-Transfer terms; the email-immutability rule in [[Funding and Repayment Setup Flow]] is a fraud control around this rail. Push-to-card disbursement operates under Visa Direct / Mastercard Send network rules.

## 7. Electronic Documents and Signatures

Federal (PIPEDA Part 2) and provincial electronic-commerce acts (e.g., Ontario's ECA, Québec's framework) recognize electronic agreements; consumer-lending statutes add per-province formalities. Observed consequence: per-document acknowledgement plus a binding "I Agree" suffices in most provinces, while some (e.g., BC, NL, MB in the source program) require additional checkboxes/initials — making the **e-sign experience province-configurable**, with vendor e-sign platforms as the scaling pattern. Signed documents must be delivered/retained (saved to the customer's account, downloadable and printable in-flow).

## 8. Product Availability and Jurisdiction Gating

Product–province availability is a regulatory artifact: licensing differences, product prohibitions, and channel restrictions produce the availability matrix (online / retail-only / not available) that gates [[Pre-Qualification Flow|intake]]. Notable patterns: provinces where certain short-term products are unavailable; one province (Québec, in the source program) with no digital lending application at all; and one province (Saskatchewan, in the source program) prohibiting credential-based bank linking for income verification — forcing the manual path in [[Income Verification Flow]]. Residence governs over geolocation, with the out-of-province-applicant edge case a defined policy point.

## 9. Optional Insurance Products

Creditor insurance (loan protection) and balance-protection insurance offered in-flow attract specific scrutiny (FCAC guidance on express consent for optional products; provincial insurance-licensing regimes for distribution): clear optionality, explicit yes/no elections, no negative-option enrolment, full cost disclosure, and proper agreements/waivers — the patterns implemented in [[Loan Finalization and Document Signing Flow]] and [[Credit Card Application Flow]].

## Quick Map — Obligation → Capability → Flow Step

| Obligation                                       | Capability              | Where it lands                                                                 |
| ------------------------------------------------ | ----------------------- | ------------------------------------------------------------------------------ |
| FINTRAC client ID                                | ONB-AKC-01/08           | [[Identity Verification Flow]]; identity capture in [[Pre-Qualification Flow]] |
| Licence & cost disclosure before data collection | ONB-CCC-01 / ONB-AKC-03 | Disclosure step, [[Pre-Qualification Flow]]                                    |
| 35% APR ceiling / $14-per-$100 payday cap        | ONB-CCC-01              | Cost summaries and disclosure parameters                                       |
| Bureau consent & inquiry typing                  | ONB-AKC-04 / ONB-ADJ-04 | Consents at capture; hard-check sequencing on the card path                    |
| PIPEDA/CASL consent architecture                 | ONB-AKC                 | Individually acknowledged consents throughout                                  |
| Rule H1 PAD agreement                            | ONB-ASF-02 / ONB-CCC-05 | [[Funding and Repayment Setup Flow]] + signing steps                           |
| E-sign formalities by province                   | ONB-CCC-05              | [[Loan Finalization and Document Signing Flow]]                                |
| Optional-insurance conduct                       | ONB-APP-05              | Insurance offers on loan and card paths                                        |
| Province availability gating                     | ONB-AKC-03 / ONB-APP-01 | Province selection, [[Pre-Qualification Flow]]                                 |
