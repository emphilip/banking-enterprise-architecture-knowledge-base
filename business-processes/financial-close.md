---
id: financial-close
title: Financial Close
type: business-process
domain: Finance & Treasury
aliases: ["Record to Report", "R2R", "Month-End Close", "Period Close"]
status: draft
sources: ["https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf", "https://www.highradius.com/resources/Blog/ultimate-guide-on-financial-close-process/", "https://www.readyratios.com/reference/accounting/intercompany_eliminations.html"]
---

# Financial Close

**Definition.** Financial Close is the periodic record-to-report process that closes subledgers and the general ledger, posts period-end adjustments, reconciles accounts, eliminates intercompany balances, runs consolidation and produces the consolidated financial statements for an accounting period.
**Also known as:** Record to Report, R2R, Month-End Close, Period Close.

## Relationships
- Financial Close is defined in the Finance & Treasury domain.
- Financial Close depends on the General Ledger Accounting capability.
- Financial Close depends on the Financial Reporting capability.

## Details
Financial Close is owned by the Financial Controller. Inputs are subledger balances, journal feeds, intercompany data and the prior-period close; outputs are an adjusted Trial Balance, the Consolidated Financial Statements and a close certification. Controls include period-end cut-off, journal approval and segregation of duties, account reconciliation, intercompany elimination, SOX/ICFR and IFRS 10 consolidation, with controller sign-off.

## Flow
- Close Subledgers causes Post Closing Journals.
- Post Closing Journals causes Reconcile Ledger Accounts.
- Reconcile Ledger Accounts causes Eliminate Intercompany Balances.
- Eliminate Intercompany Balances causes Run Consolidation.
- Run Consolidation causes Prepare Consolidated Statements.
- Prepare Consolidated Statements causes Certify Period Close.

## References
- [APQC Manage Financial Resources PCF](https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf)
- [Ultimate guide on the financial close process](https://www.highradius.com/resources/Blog/ultimate-guide-on-financial-close-process/)
- [Intercompany eliminations](https://www.readyratios.com/reference/accounting/intercompany_eliminations.html)
