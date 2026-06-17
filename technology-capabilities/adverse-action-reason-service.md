---
id: adverse-action-reason-service
title: Adverse Action Reason Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Reason Code Derivation Service", "Principal Reason Service", "ECOA Reason Service"]
status: draft
sources: ["https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/", "https://fairplay.ai/glossary/adverse-action-reason/"]
---

# Adverse Action Reason Service

**Definition.** Adverse Action Reason Service derives the specific principal-reason codes that explain a declined or modified credit decision, sourcing them from the scoring model to meet FCRA and ECOA disclosure rules.
**Also known as:** Reason Code Derivation Service, Principal Reason Service, ECOA Reason Service.

## Relationships
- Adverse Action Reason Service is defined in the Core Processing domain.
- Adverse Action Reason Service is derived from Adverse Action Generator.
- Adverse Action Reason Service is related to Credit Scoring Service.

## Details
Adverse Action Reason Service identifies the principal reasons that most reduced an applicant's score and renders them as specific, accurate statements for the adverse-action notice. ECOA's Regulation B requires the creditor to disclose the specific reasons for the action, and CFPB Circular 2022-03 confirms that creditors using complex or algorithmic models must still provide accurate, specific reasons — generic or checklist-only reasons are insufficient when the model relies on factors not on the standard list. The service consumes the reason codes produced by Credit Scoring Service and maps them to the disclosable principal-reason text.

## References
- [CFPB Circular 2022-03 on adverse action and complex algorithms](https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/)
- [Adverse action reason (FairPlay glossary)](https://fairplay.ai/glossary/adverse-action-reason/)
