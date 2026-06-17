---
id: close-subledgers
title: Close Subledgers
type: process-step
process: Financial Close
order: 1
aliases: ["Cut Off Period", "Close Sub-Ledgers"]
status: draft
sources: ["https://www.oreilly.com/library/view/the-fast-close/9781119554493/c05.xhtml", "https://www.highradius.com/resources/Blog/ultimate-guide-on-financial-close-process/"]
---

# Close Subledgers

**Definition.** Close Subledgers cuts off the accounting period and closes the AP, AR, fixed-asset and inventory subledgers, posting their balances to the general ledger.

## Relationships
- Close Subledgers is defined in the Financial Close process.
- Close Subledgers causes Post Closing Journals.
- Close Subledgers depends on the General Ledger Accounting capability.
- Close Subledgers mentions Financial Controller.
- Close Subledgers mentions Trial Balance.

## Details
The General Ledger Accountant cuts off the period once the Period Close Initiated Event is raised and closes the subledgers, posting balances to the general ledger. Inputs are subledger transactions and the period calendar; outputs are the closed subledgers and a GL feed. Controls include period-end cut-off and subledger-to-GL reconciliation.

## References
- [The Fast Close](https://www.oreilly.com/library/view/the-fast-close/9781119554493/c05.xhtml)
- [Ultimate guide on the financial close process](https://www.highradius.com/resources/Blog/ultimate-guide-on-financial-close-process/)
