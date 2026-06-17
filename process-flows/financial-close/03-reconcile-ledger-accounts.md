---
id: reconcile-ledger-accounts
title: Reconcile Ledger Accounts
type: process-step
process: Financial Close
order: 3
aliases: ["Reconcile GL", "Account Reconciliation (Close)"]
status: draft
sources: ["https://www.numeric.io/blog/month-end-reconciliation", "https://strategiccfo.com/articles/banking-financing/account-reconciliation/"]
---

# Reconcile Ledger Accounts

**Definition.** Reconcile Ledger Accounts reconciles general-ledger accounts to subledgers and supporting schedules, clearing breaks before consolidation.

## Relationships
- Reconcile Ledger Accounts is defined in the Financial Close process.
- Reconcile Ledger Accounts causes Eliminate Intercompany Balances.
- Reconcile Ledger Accounts causes Post Closing Journals.
- Reconcile Ledger Accounts depends on the General Ledger Accounting capability.
- Reconcile Ledger Accounts mentions Financial Controller.
- Reconcile Ledger Accounts mentions Trial Balance.

## Details
The General Ledger Accountant reconciles GL balances to subledger detail and clears breaks. Inputs are GL balances and subledger detail; outputs are reconciled accounts and a break log. Controls include account reconciliation and break clearance. An unresolved break causes a return to Post Closing Journals for correction before consolidation proceeds.

## References
- [Month-end reconciliation](https://www.numeric.io/blog/month-end-reconciliation)
- [Account reconciliation](https://strategiccfo.com/articles/banking-financing/account-reconciliation/)
