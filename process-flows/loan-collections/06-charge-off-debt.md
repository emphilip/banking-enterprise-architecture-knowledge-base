---
id: charge-off-debt
title: Charge Off Debt
type: process-step
process: Loan Collections
order: 6
aliases: ["Write Off Debt", "Charge-Off Step"]
status: draft
sources: ["https://en.wikipedia.org/wiki/Charge-off", "https://www.debt.org/credit/collection-agencies/debt-collectors/"]
---

# Charge Off Debt

**Definition.** Charge Off Debt writes the debt off as uncollectable and places it for recovery or agency collection.
**Also known as:** Write Off Debt, Charge-Off Step.

## Relationships
- Charge Off Debt is defined in the Loan Collections process.
- Charge Off Debt depends on the Core Banking Processing capability.
- Charge Off Debt mentions Recovery Officer.

## Details
The Recovery Officer executes the charge-off. Inputs are the recovery case; outputs are a recovery outcome. Controls include the charge-off threshold (typically 180 days), accounting controls and agency placement. This terminal step emits the Loan Charged Off Event.

## References
- [Wikipedia: charge-off](https://en.wikipedia.org/wiki/Charge-off)
- [Debt.org: debt collectors](https://www.debt.org/credit/collection-agencies/debt-collectors/)
