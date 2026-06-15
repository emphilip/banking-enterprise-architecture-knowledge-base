---
id: settlement-received-event
title: Settlement Received Event
type: event
domain: Payments
aliases: ["Settlement Advice Event", "Settlement Notified"]
status: draft
sources: ["https://fedwireservice.org/"]
---

# Settlement Received Event

**Definition.** Settlement Received Event is the event raised when a settlement advice or file is received from an operator or correspondent. Settlement Received Event signals reconciliation and settlement to confirm interbank money movement.

**Also known as:** Settlement Advice Event, Settlement Notified.

## Relationships
- Settlement Received Event is related to the Payments domain.
- Settlement Received Event causes Confirm Settlement.
- Settlement Received Event mentions Reconciliation & Settlement.
- Settlement Received Event is related to Settlement File.

## Details
Settlement Received Event fires when an operator or correspondent transmits evidence that interbank settlement has occurred. The event prompts the settlement role to capture the advice, verify settlement finality under dual control, and feed downstream statement ingestion and matching activities.

## References
- https://fedwireservice.org/
