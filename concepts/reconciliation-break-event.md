---
id: reconciliation-break-event
title: Reconciliation Break Event
type: event
domain: Payments
aliases: ["Break Raised Event", "Exception Raised"]
status: draft
sources: ["https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/"]
---

# Reconciliation Break Event

**Definition.** Reconciliation Break Event is the event raised when an unmatched item or discrepancy is detected during reconciliation. Reconciliation Break Event triggers investigation within reconciliation and settlement.

**Also known as:** Break Raised Event, Exception Raised.

## Relationships
- Reconciliation Break Event is related to the Payments domain.
- Reconciliation Break Event causes Investigate Break.
- Reconciliation Break Event mentions Reconciliation & Settlement.
- Reconciliation Break Event is related to Exception Investigation.

## Details
Reconciliation Break Event is produced when auto-matching fails to reconcile a statement entry against internal ledger or payment records within tolerance. The event classifies the item by type and ageing, opens an investigation, and routes the break to the responsible owner for resolution and subsequent adjustment posting.

## References
- https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/
