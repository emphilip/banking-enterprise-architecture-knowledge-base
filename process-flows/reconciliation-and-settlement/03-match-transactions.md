---
id: match-transactions
title: Match Transactions
type: process-step
process: Reconciliation & Settlement
order: 3
aliases: ["Auto Matching", "Transaction Matching"]
status: draft
sources: ["https://www.skydo.com/blog/nostro-reconciliation", "https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/"]
---

# Match Transactions

**Definition.** Match Transactions auto-matches statement entries to internal ledger/payment records using references and tolerances.
**Also known as:** Auto Matching, Transaction Matching.

## Relationships
- Match Transactions is defined in the Reconciliation & Settlement process.
- Match Transactions causes Identify Breaks.
- Match Transactions depends on the Core Banking Processing capability.
- Match Transactions mentions Reconciliation Analyst.

## Details
The Reconciliation Analyst runs automated matching. Inputs are loaded statement data; outputs are a reconciliation result. Controls include matching tolerance rules and structured reference checks to maximise straight-through matching.

## References
- [Nostro reconciliation](https://www.skydo.com/blog/nostro-reconciliation)
- [ISO 20022 pain messages](https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/)
