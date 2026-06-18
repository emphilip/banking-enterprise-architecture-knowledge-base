---
title: AML, KYC & Compliance
type: capability
level: L1
capability-id: ONB-AKC
parent: Onboarding & Origination (ONB)
tags: [capability, aml, kyc, compliance, fintrac, sanctions, idv, retail-banking]
aliases: [ONB-AKC, AML KYC Compliance, KYC, Onboarding Compliance]
---

# AML, KYC & Compliance (ONB-AKC)

**Parent:** [[Onboarding and Origination Capability Model|Onboarding & Origination (ONB)]]

This capability group covers the regulatory obligations a Canadian bank must satisfy during onboarding: knowing the customer, screening for financial-crime risk, validating identity, obtaining mandated consents and disclosures, and reporting suspicious activity. In Canada these obligations flow primarily from the **PCMLTFA** (Proceeds of Crime (Money Laundering) and Terrorist Financing Act) administered by **FINTRAC**, provincial lending and consumer-protection statutes, federal cost-of-borrowing disclosure regulations, and privacy law (**PIPEDA** / provincial equivalents). See [[Canadian Regulatory Context]] for the regulatory detail; this note defines the capabilities.

## L2 Capabilities

### ONB-AKC-01 — KYC Check

Establishing and verifying who the customer is, per FINTRAC client-identification requirements.

- Collection of the core identity dataset: legal name, date of birth, residential address, occupation/income context, and **Canadian residency status** (a required, explicit selection at capture — observed flows treat it as both a compliance and a risk/decisioning input).
- Identity verification through accepted FINTRAC methods: government-issued photo ID verification (digital document capture qualifies — see ONB-AKC-08), the credit-file method, or the dual-process method (two reliable independent sources).
- Phone ownership verification (OTP) and carrier-data checks (mobile-provider disclosure consent for identity verification and fraud protection) supplement formal KYC as risk controls.
- Address quality rules: structured address capture with autocomplete; policy decisions on P.O. boxes (commonly accepted only where the P.O. box is the address of record); address-match requirements at adjudication.

### ONB-AKC-02 — AML Check

Anti-money-laundering controls at onboarding.

- Risk-rating the new relationship (product, geography, customer attributes) per the bank's AML compliance program.
- Detection of identity and application anomalies (synthetic identity signals, mismatched data) feeding [[Adjudication and Underwriting|risk assessment]].
- Record-keeping obligations: consents, identification records, and signed agreements retained to FINTRAC/PIPEDA standards (signed documents are saved to the customer's account at submission).

### ONB-AKC-03 — Regulatory Check

Jurisdiction-specific regulatory verification before product sale.

- **Province-aware compliance configuration:** lender licensing per province, product–province availability matrices (some products are simply not available, or not digitally available, in some provinces — e.g., no digital lending in Québec in the source program), and province-specific verification rules (one province prohibiting screen-scraping-based bank linking, forcing manual income verification).
- **Mandatory pre-sale presentation** of provincial licence information, regulator-approved educational materials, and statutory references (e.g., payday-loan legislation) before any personal information is collected.
- **Geolocation vs. residence rules:** policy for applicants physically located outside their province of residence.
- Compliance review checkpoints for content: all customer-facing legal copy flows through legal/compliance review; e-signature mechanics vary by province (some provinces require additional per-document checkboxes or initials).

### ONB-AKC-04 — Credit Check

The compliance dimension of bureau inquiries (operational access lives in [[Adjudication and Underwriting|ONB-ADJ-04]]).

- Express, informed, individually acknowledged consent before any bureau inquiry; the consent copy states the purpose and — for soft inquiries — that the check will not affect the applicant's credit score.
- Clear differentiation and disclosure of **soft vs. hard** inquiries, including being explicit when a product (e.g., a short-term loan) involves *no* hard credit check, and sequencing all required acknowledgements before the hard inquiry occurs.

### ONB-AKC-05 — Sanctions / Watchlist Screening

Screening applicants against sanctions and watchlists.

- Canadian regimes: UN Act regulations, *Special Economic Measures Act* lists, the *Justice for Victims of Corrupt Foreign Officials Act*, and Criminal Code terrorist listings; OFAC/other lists per the bank's exposure.
- **PEP/HIO determination:** politically exposed persons and heads of international organizations checks per PCMLTFA requirements.
- Screening occurs at onboarding and on an ongoing basis; onboarding hits route to compliance review rather than automated decline.

### ONB-AKC-06 — Enhanced Due Diligence (EDD)

Deeper diligence for higher-risk customers — additional information collection, source-of-funds/wealth inquiry, senior-management approval for high-risk relationships, and enhanced ongoing monitoring flags set at onboarding.

### ONB-AKC-07 — STR/SAR Filing

Reporting obligations arising at onboarding: suspicious transaction/attempted-transaction reports to FINTRAC where onboarding activity gives rise to reasonable grounds for suspicion, with supporting case documentation from [[Manual Review Flow|manual review]] and fraud investigation. (US-model naming: SAR.)

### ONB-AKC-08 — ID Validation

Technical validation of identity documents and biometric confirmation. Detailed in [[Identity Verification Flow]].

- **Digital document verification** through an IDV provider (Plaid/Onfido/Persona-class): government photo ID capture (front and back), authenticity checks, and a **liveness selfie video** matched to the document.
- **Device-adaptive orchestration:** desktop sessions hand off to mobile via QR code for camera capture, then resume on desktop; mobile sessions complete in-session.
- **Risk-based invocation:** IDV is required only when the decision engine demands it, keeping friction proportional to risk.
- **Fallback:** failed or unavailable digital IDV routes to manual document upload and human review ([[Manual Review Flow]]).

## Consent Architecture (Cross-Cutting)

Observed best practice generalizes to a consent architecture spanning this capability group:

| Consent | Required? | Captured at | Notes |
|---|---|---|---|
| Credit bureau consent | Required | Personal details step | Soft-inquiry "no score impact" statement at pre-qual |
| Terms & Conditions / Privacy | Required | Personal details step | Links to full documents |
| Marketing consent | Optional | Personal details step | CASL-aligned express consent; never blocks advancement |
| Mobile-carrier disclosure (PICRA-style) | Required at full application entry | Post-qual entry screen | Authorizes carrier data use for identity verification and fraud protection |
| Pre-authorized debit agreement | Required when PAD established | Document signing | Payments Canada Rule H1 — see [[Funding and Repayment Setup Flow]] |
| Product agreements (loan/cardholder/insurance) | Required per product | Document signing | See [[Loan Finalization and Document Signing Flow]] |

Each consent is **individually acknowledged** — bulk acceptance is prohibited — and the opt-in default state of checkboxes is a tracked regulatory concern (pre-checked consent boxes are a compliance red flag in Canada).

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Pre-Qualification Flow]] | ONB-AKC-01, 03, 04 |
| [[Post-Qualification Application Flow]] | ONB-AKC-01, 02, 04, 05 |
| [[Identity Verification Flow]] | ONB-AKC-01, 08 |
| [[Credit Card Application Flow]] | ONB-AKC-03, 04 |
| [[Manual Review Flow]] | ONB-AKC-06, 07 |

## Related

[[Canadian Regulatory Context]] · [[Collateral and Customer Communications]] · [[Adjudication and Underwriting]] · [[Identity Verification Flow]]
