---
id: cash-variance-event
title: Cash Variance Event
type: event
domain: Channels & Engagement
aliases: ["Cash Discrepancy Event", "ATM Variance Event"]
status: draft
sources: ["https://www.slideshare.net/slideshow/atm-reconciliation-manual-62909276/62909276"]
---

# Cash Variance Event

**Definition.** Cash Variance Event is the event raised when an ATM or teller cash reconciliation detects a difference between expected and actual cash. Cash Variance Event triggers investigation and resolution of the discrepancy in the cash reconciliation flow.

**Also known as:** Cash Discrepancy Event, ATM Variance Event.

## Relationships
- Cash Variance Event is related to the Channels & Engagement domain.
- Cash Variance Event causes Resolve Cash Discrepancy.
- Cash Variance Event mentions ATM Cash Management.
- Cash Variance Event is related to Reconcile ATM Cash.

## Details
Cash Variance Event fires when daily reconciliation of dispensed versus loaded cash, or a teller drawer balancing, surfaces a difference that exceeds tolerance. The event drives variance and exception management: investigating the cause, matching electronic-journal against host records, and posting approved adjustments. It supports the controls that protect the cash general ledger and flags potential operational or fraud issues for escalation.

## References
- https://www.slideshare.net/slideshow/atm-reconciliation-manual-62909276/62909276
