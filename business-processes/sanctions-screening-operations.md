---
id: sanctions-screening-operations
title: Sanctions Screening Operations
type: business-process
domain: Compliance & Financial Crime
aliases: ["Sanctions Operations", "Watchlist Screening Operations", "Screening Ops"]
status: draft
sources: ["https://salv.com/blog/sanctions-screening-guide/", "https://www.lenzo.ai/blog/sanctions-screening-false-positives-resolution-criteria/", "https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/customer-screening/8.1.2.10.0/csoug/alert-decision.html"]
---

# Sanctions Screening Operations

**Definition.** Sanctions Screening Operations is the operational process of screening parties and transactions against OFAC/UN/EU watchlists: name and transaction matching, alert generation, L1/L2 triage of potential matches, true-match versus false-positive resolution under four-eyes, and the blocking and reporting of confirmed hits within regulatory deadlines.
**Also known as:** Sanctions Operations, Watchlist Screening Operations, Screening Ops.

## Relationships
- Sanctions Screening Operations is defined in the Compliance & Financial Crime domain.
- Sanctions Screening Operations depends on the Sanctions Screening capability.

## Details
Sanctions Screening Operations applies exact and fuzzy matching against OFAC SDN and consolidated lists, raises Sanctions Hit alerts above threshold, performs three-tier triage (clear/review/block), resolves true matches with documented true-match/false-positive determinations, and blocks and reports confirmed matches within 10 business days under four-eyes. The lead actor is the Compliance Screening Officer. Outputs include the Sanctions Hit disposition, cleared alerts and the blocking report.

## Flow
- Match Against Watchlist causes Generate Sanctions Alert.
- Generate Sanctions Alert causes Triage Potential Match.
- Triage Potential Match causes Resolve Sanctions Hit.
- Resolve Sanctions Hit causes Confirm Sanctions Block.
- Confirm Sanctions Block causes Report Sanctions Block.

## References
- [Salv — Sanctions screening guide](https://salv.com/blog/sanctions-screening-guide/)
- [Lenzo — False-positive resolution criteria](https://www.lenzo.ai/blog/sanctions-screening-false-positives-resolution-criteria/)
- [Oracle — Customer screening alert decision](https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/customer-screening/8.1.2.10.0/csoug/alert-decision.html)
