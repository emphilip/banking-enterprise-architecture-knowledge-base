---
id: sanctions-alert-event
title: Sanctions Alert Event
type: event
domain: Compliance & Financial Crime
aliases: ["Sanctions Match Event", "Watchlist Hit Event"]
status: draft
sources: ["https://salv.com/blog/sanctions-screening-guide/"]
---

# Sanctions Alert Event

**Definition.** Sanctions Alert Event is the business event raised when a watchlist match is generated, confirmed and a transaction or relationship is blocked and reported. Sanctions Alert Event drives triage, four-eyes resolution and regulatory reporting of confirmed hits.
**Also known as:** Sanctions Match Event, Watchlist Hit Event.

## Relationships
- Sanctions Alert Event is related to the Compliance & Financial Crime domain.
- Sanctions Alert Event mentions Sanctions Screening Operations.
- Sanctions Alert Event causes Resolve Sanctions Hit.

## Details
Sanctions Alert Event carries the matched party or transaction reference, the matched watchlist entry (e.g. an OFAC SDN record), the match score, the alert priority and the screening timestamp. It is emitted when name or transaction matching exceeds threshold and routes the alert into L1/L2 triage and resolution under the preponderance standard. Confirmation of a true match triggers blocking and reporting to OFAC within 10 business days, with four-eyes approval and a full audit trail retained for the regulatory record.

## References
- [OFAC sanctions compliance guidance](https://ofac.treasury.gov/)
- [Wolfsberg sanctions screening guidance](https://www.wolfsberg-principles.com/)
