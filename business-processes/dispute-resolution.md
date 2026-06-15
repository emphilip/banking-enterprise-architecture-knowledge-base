---
id: dispute-resolution
title: Dispute Resolution
type: business-process
domain: Cards
aliases: ["Chargeback Process"]
status: draft
---

# Dispute Resolution

**Definition.** Dispute Resolution is the process of handling cardholder transaction disputes and chargebacks, from claim intake through investigation, representment, and resolution.
**Also known as:** Chargeback Process.

## Relationships
- Dispute Resolution is defined in the Cards domain.
- Dispute Resolution depends on the Dispute Management capability.

## Details
Dispute Resolution registers the cardholder claim, gathers evidence, raises chargebacks to the scheme, manages merchant representment, and applies provisional and final credits. Actors include cardholders, dispute analysts, and scheme operators. Systems involved include a dispute management platform, card processing, and the core ledger.

## Flow
- Register Dispute Claim causes Validate Dispute Rights.
- Validate Dispute Rights causes Apply Provisional Credit.
- Apply Provisional Credit causes Gather Dispute Evidence.
- Gather Dispute Evidence causes Adjudicate Dispute Outcome.
- Adjudicate Dispute Outcome causes Finalize Dispute Credit.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
