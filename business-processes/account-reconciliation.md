---
id: account-reconciliation
title: Account Reconciliation
type: business-process
domain: Payments
aliases: ["Statement Matching", "Nostro Recon"]
status: draft
sources: ["https://www.skydo.com/blog/nostro-reconciliation", "https://corporates.dzbank.com/content/firmenkunden/en/homepage/products/transaction-banking/national-international_payments/iso-20022/camt-053-52.html"]
---

# Account Reconciliation

**Definition.** Account Reconciliation matches internal ledger entries to nostro/clearing statements and surfaces breaks.
**Also known as:** Statement Matching, Nostro Recon.

## Relationships
- Account Reconciliation is derived from Reconciliation & Settlement.
- Account Reconciliation is defined in the Payments domain.
- Account Reconciliation depends on the Core Banking Processing capability.

## Details
The sub-process is performed by the Reconciliation Analyst. Inputs are the Bank Statement Message; outputs are a reconciliation result identifying matches and unmatched items. Controls include matching tolerance rules and segregation of duties.

## References
- [Nostro reconciliation](https://www.skydo.com/blog/nostro-reconciliation)
- [camt.053/camt.052 statements](https://corporates.dzbank.com/content/firmenkunden/en/homepage/products/transaction-banking/national-international_payments/iso-20022/camt-053-52.html)
