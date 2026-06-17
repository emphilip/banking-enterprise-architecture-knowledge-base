---
id: replenish-teller-drawer
title: Replenish Teller Drawer
type: process-step
process: Branch Operations
order: 4
aliases: ["Drawer Buy/Sell", "Cash Transfer"]
status: draft
sources: ["https://www.tcs.com/content/dam/global-tcs/en/pdfs/what-we-do/platforms/TCS-BaNCS/research-journal/tcs-bancs-research-journal-16-understanding-cash-handling.pdf"]
---

# Replenish Teller Drawer

**Definition.** Replenish Teller Drawer buys and sells cash between the teller drawer and the vault to keep the drawer within approved limits.
**Also known as:** Drawer Buy/Sell, Cash Transfer.

## Relationships
- Replenish Teller Drawer is defined in the Branch Operations process.
- Replenish Teller Drawer causes Balance Teller Drawer.
- Replenish Teller Drawer depends on the Branch Banking capability.
- Replenish Teller Drawer mentions Teller.

## Details
The Teller manages the drawer position. Inputs are the drawer balance and vault cash; outputs are a balanced drawer. At the decision point, if the drawer is not within limit a dual-custody vault transfer is made. Controls include drawer limits and dual-custody vault transfers (branch balancing discipline).

## References
- [TCS BaNCS understanding cash handling](https://www.tcs.com/content/dam/global-tcs/en/pdfs/what-we-do/platforms/TCS-BaNCS/research-journal/tcs-bancs-research-journal-16-understanding-cash-handling.pdf)
