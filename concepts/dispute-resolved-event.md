---
id: dispute-resolved-event
title: Dispute Resolved Event
type: event
domain: Cards
aliases: ["Dispute Closed Event", "Chargeback Settled Event"]
status: draft
sources: ["https://www.consumercomplianceoutlook.org/2021/second-issue/error-resolution-and-liability-limitations-under-regulations-e-and-z/", "https://chargebacks911.com/chargeback-life-cycle/"]
---

# Dispute Resolved Event

**Definition.** Dispute Resolved Event is the event signalling that a cardholder dispute has been finally resolved, with provisional credit made permanent or reversed and the case closed. Dispute Resolved Event marks the end of the dispute lifecycle and the final credit/debit posting.

**Also known as:** Dispute Closed Event, Chargeback Settled Event.

## Relationships
- Dispute Resolved Event is related to the Cards domain.
- Dispute Resolved Event mentions Dispute Resolution.
- Dispute Resolved Event causes Settle Chargeback.

## Details
Dispute Resolved Event fires when the dispute outcome is finalised, carrying the Chargeback Case identifier, the final disposition (cardholder favoured or merchant favoured), the final credit/debit amount and the resolution date. Dispute Resolved Event confirms the issuer met the Reg E 45/90-day investigation deadline and that the cardholder received notice of correction or denial. Accounting systems consume Dispute Resolved Event to convert provisional credit to a permanent entry or reverse it, to close the recovery, and to update dispute and chargeback ratio metrics.

## References
- https://www.consumercomplianceoutlook.org/2021/second-issue/error-resolution-and-liability-limitations-under-regulations-e-and-z/
- https://chargebacks911.com/chargeback-life-cycle/
