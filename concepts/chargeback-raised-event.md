---
id: chargeback-raised-event
title: Chargeback Raised Event
type: event
domain: Cards
aliases: ["Chargeback Filed Event", "Dispute Raised Event"]
status: draft
sources: ["https://www.chargeflow.io/chargebacks-101/chargeback-rules", "https://chargebacks911.com/chargeback-life-cycle/"]
---

# Chargeback Raised Event

**Definition.** Chargeback Raised Event is the event signalling that an issuer chargeback has been submitted against the acquirer/merchant for a disputed card transaction. Chargeback Raised Event opens the scheme dispute clock and triggers the representment and resolution phases.

**Also known as:** Chargeback Filed Event, Dispute Raised Event.

## Relationships
- Chargeback Raised Event is related to the Cards domain.
- Chargeback Raised Event mentions Chargeback Processing.
- Chargeback Raised Event causes Raise Chargeback.

## Details
Chargeback Raised Event fires when Raise Chargeback submits the first-presentment dispute to the acquirer via the scheme, carrying the Chargeback Case identifier, the assigned scheme reason code (e.g. Visa 10-13, Mastercard 4837/4853), the disputed amount and the filing date. Chargeback Raised Event confirms the chargeback was lodged within the 120-day filing limit and starts the 30-day phase-response window for merchant representment. Accounting systems consume Chargeback Raised Event to record the provisional recovery and to drive escalation to pre-arbitration/arbitration if the case remains contested.

## References
- https://www.chargeflow.io/chargebacks-101/chargeback-rules
- https://chargebacks911.com/chargeback-life-cycle/
