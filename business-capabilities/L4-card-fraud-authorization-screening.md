---
id: card-fraud-authorization-screening
title: Card Fraud Authorization Screening
type: business-capability
domain: Cards
level: L4
aliases: ["Auth Fraud Screening", "Real-Time Fraud Scoring (Cards)"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.iso.org/standard/31628.html"]
---

# Card Fraud Authorization Screening

**Definition.** Card Fraud Authorization Screening scores in-flight authorization requests for fraud risk before approval, feeding the BIAN Card Authorization decision.
**Also known as:** Auth Fraud Screening, Real-Time Fraud Scoring (Cards).

## Relationships
- Card Fraud Authorization Screening is defined in the Cards domain.
- Card Fraud Authorization Screening is derived from Authorization Decisioning.
- Card Fraud Authorization Screening depends on the Fraud Analytics capability.

## Details
Inside the BIAN Card Authorization window this capability produces a real-time fraud score from features in the ISO 8583 message (MCC, amount, country, terminal entry mode, EMV vs fallback) and behavioural history, typically via platforms like FICO Falcon or Feedzai. High scores drive a decline (e.g. 05/59) or step-up to 3-D Secure / EMV 3DS challenge, balancing fraud loss against false-positive friction within scheme response-time limits.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [ISO 8583 Financial transaction card messaging](https://www.iso.org/standard/31628.html)
