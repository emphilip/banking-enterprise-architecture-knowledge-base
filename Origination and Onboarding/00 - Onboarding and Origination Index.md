---
title: Onboarding & Origination — Knowledge Library Index
type: index
domain: banking-and-payments
capability-l0: Onboarding & Origination
tags: [onboarding, origination, capability-model, index, retail-banking, canada]
aliases: [Onboarding Index, Origination Index, ONB MOC]
---

# Onboarding & Origination — Knowledge Library

This library documents the **Onboarding & Origination** domain of the multi-functional retail banking capability model, paired with **generalized digital process flows** for a typical Canadian retail bank or consumer lender. It is structured for use as a queryable knowledge base: every capability has a stable ID, every process flow is mapped to the capabilities it exercises, and Canadian regulatory context is captured in dedicated reference notes.

**Scope.** The Onboarding & Origination L0 capability covers everything from a prospect's first interaction with an application entry point through to an opened, funded, activated, and enrolled account or credit facility. It spans six L1 capability groups and is exercised end-to-end by the process flows catalogued here.

**Provenance.** Process flows are generalized from a real Canadian digital lending and card origination program (loan and credit card products, province-aware, decision-engine-driven). Vendor and brand specifics have been abstracted to generic roles — e.g., *credit decision engine*, *financial data aggregator*, *digital identity verification provider* — so the content applies to the average Canadian retail bank. See [[Integration and Decisioning Patterns]] for the generic integration roles.

---

## 1. Capability Model

The L0 domain and its six L1 capability groups, each decomposed into L2 capabilities:

| L1 Capability | ID | Summary |
|---|---|---|
| [[Application]] | ONB-APP | Intake, application capture, application management, review, pre-qualification, up/cross-sell |
| [[Adjudication and Underwriting]] | ONB-ADJ | Credit decisioning, instant decisions, decision engine, bureau access, underwriting, risk assessment |
| [[AML KYC and Compliance]] | ONB-AKC | KYC, AML, regulatory checks, credit checks, sanctions screening, EDD, STR/SAR filing, ID validation |
| [[Account Setup and Fulfillment]] | ONB-ASF | Account opening, funding, card issuance, plastic production, virtual/instant issue, card activation |
| [[Collateral and Customer Communications]] | ONB-CCC | Disclosures, welcome kits, card carriers, inserts, T&C documents, returned mail |
| [[Activation and Enrolment]] | ONB-ACT | Online/mobile banking enrolment, wallet activation, card enrolment, virtual cards, renewal |

Overview note: [[Onboarding and Origination Capability Model]]

## 2. Process Flows

Generalized end-to-end and component flows, each mapped to the capabilities it exercises:

| Process Flow | Stage | Primary Capabilities |
|---|---|---|
| [[Pre-Qualification Flow]] | Pre-qualification | ONB-APP, ONB-ADJ, ONB-AKC, ONB-CCC |
| [[Post-Qualification Application Flow]] | Full application (orchestration) | ONB-APP, ONB-ADJ, ONB-AKC, ONB-ASF |
| [[Income Verification Flow]] | Full application (component) | ONB-ADJ, ONB-APP |
| [[Identity Verification Flow]] | Full application (component) | ONB-AKC, ONB-ADJ |
| [[Funding and Repayment Setup Flow]] | Full application (component) | ONB-ASF |
| [[Loan Finalization and Document Signing Flow]] | Fulfillment | ONB-ASF, ONB-CCC |
| [[Credit Card Application Flow]] | Full application (product path) | ONB-APP, ONB-ADJ, ONB-ASF, ONB-CCC, ONB-ACT |
| [[Manual Review Flow]] | Exception handling | ONB-ADJ, ONB-APP |

## 3. Reference

- [[Process-to-Capability Mapping Matrix]] — full traceability matrix of flow steps to L2 capabilities
- [[Canadian Regulatory Context]] — FINTRAC/PCMLTFA, cost-of-borrowing disclosure, criminal interest rate, provincial regimes, PAD rules, consent and privacy
- [[Integration and Decisioning Patterns]] — decision engine, data aggregation, IDV, embedded payments, CMS-driven content
- [[Data Requirements Reference]] — canonical intake, decisioning, and fulfillment data elements
- [[Glossary]] — terminology used across the library

---

## Identifier conventions

- **Capability IDs** — `ONB-XXX-nn` (e.g., `ONB-AKC-08`): the L2 capabilities defined in the [[Onboarding and Origination Capability Model]].
- **Step IDs** — `Step XX-nn` headings inside each process-flow note (`PQ-` pre-qualification, `POST-` orchestration, `IV-A`/`IV-B` income verification paths, `IDV-` identity verification, `FUND-` funding setup, `LF-` loan finalization, `CC-` card path, `MR-` manual review). Every step section is self-contained: a context line under the heading states its capability, preconditions, inputs, and exits, so a step can be retrieved and reasoned about in isolation. Steps are addressable as `[[Flow Name#Step XX-nn — Title]]`.
- **Data groups** — `D1`–`D12` in the [[Data Requirements Reference]]; **rules** — flow-local rule IDs such as `FUND-R1` for cross-cutting constraints.

## How to query this library

- **"What happens during pre-qualification?"** → [[Pre-Qualification Flow]]
- **"Which capability handles sanctions screening?"** → [[AML KYC and Compliance]] (ONB-AKC-05)
- **"How does income verification work when bank linking fails?"** → [[Income Verification Flow]] → [[Manual Review Flow]]
- **"What disclosures are required before collecting personal information?"** → [[Collateral and Customer Communications]] and [[Canadian Regulatory Context]]
- **"Which flows touch the decision engine?"** → [[Integration and Decisioning Patterns]] and [[Process-to-Capability Mapping Matrix]]
