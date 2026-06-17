---
id: extract-account-activity
title: Extract Account Activity
type: process-step
process: Statement Generation
order: 2
aliases: ["Pull Postings", "Activity Extraction Step"]
status: draft
sources: ["https://en.wikipedia.org/wiki/Bank_reconciliation"]
---

# Extract Account Activity

**Definition.** Extract Account Activity extracts postings, balances and interest for each account in the cycle.
**Also known as:** Pull Postings, Activity Extraction Step.

## Relationships
- Extract Account Activity is defined in the Statement Generation process.
- Extract Account Activity causes Reconcile Statement Data.
- Extract Account Activity depends on the Core Banking Processing capability.
- Extract Account Activity mentions Statement Production Officer.

## Details
The Statement Production Officer extracts activity from the transaction ledger for the cycle population. Controls include completeness reconciliation of extracted postings.

## References
- [Bank reconciliation](https://en.wikipedia.org/wiki/Bank_reconciliation)
