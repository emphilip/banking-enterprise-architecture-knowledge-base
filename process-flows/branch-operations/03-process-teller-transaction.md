---
id: process-teller-transaction
title: Process Teller Transaction
type: process-step
process: Branch Operations
order: 3
aliases: ["Teller Posting", "Transaction Execution"]
status: draft
sources: ["https://help.cubase.org/cubase/teller_control_and_balancing_procedures.htm"]
---

# Process Teller Transaction

**Definition.** Process Teller Transaction executes the cash, cheque or account transaction in the teller application and posts it to core.
**Also known as:** Teller Posting, Transaction Execution.

## Relationships
- Process Teller Transaction is defined in the Branch Operations process.
- Process Teller Transaction causes Replenish Teller Drawer.
- Process Teller Transaction depends on the Core Banking Processing capability.
- Process Teller Transaction mentions Teller.

## Details
The Teller posts the transaction. Inputs are the captured transaction; outputs are a posted entry. Controls include transaction limits and dual control on large or override items.

## References
- [Cubase teller control and balancing](https://help.cubase.org/cubase/teller_control_and_balancing_procedures.htm)
