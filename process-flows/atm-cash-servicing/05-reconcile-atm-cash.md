---
id: reconcile-atm-cash
title: Reconcile ATM Cash
type: process-step
process: ATM Cash Servicing
order: 5
aliases: ["ATM Reconciliation", "Cash Balancing (ATM)"]
status: draft
sources: ["https://www.slideshare.net/slideshow/atm-reconciliation-manual-62909276/62909276"]
---

# Reconcile ATM Cash

**Definition.** Reconcile ATM Cash reconciles dispensed (EJ / host) versus loaded cash and the ATM cash GL daily.
**Also known as:** ATM Reconciliation, Cash Balancing (ATM).

## Relationships
- Reconcile ATM Cash is defined in the ATM Cash Servicing process.
- Reconcile ATM Cash causes Resolve Cash Discrepancy.
- Reconcile ATM Cash depends on the Core Banking Processing capability.
- Reconcile ATM Cash mentions ATM Custodian.
- Reconcile ATM Cash mentions ATM Replenishment Record.

## Details
The ATM Custodian reconciles cash. Inputs are EJ files, host records and the load record; outputs are a reconciled GL. At the decision point, if a variance exists a discrepancy is raised. Controls include daily ATM GL reconciliation and EJ-versus-host matching.

## References
- [ATM reconciliation manual](https://www.slideshare.net/slideshow/atm-reconciliation-manual-62909276/62909276)
