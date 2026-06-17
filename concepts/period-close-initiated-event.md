---
id: period-close-initiated-event
title: Period Close Initiated Event
type: event
domain: Finance & Treasury
aliases: ["Close Started Event", "Period-End Triggered Event"]
status: draft
sources: ["https://www.highradius.com/resources/Blog/ultimate-guide-on-financial-close-process/", "https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf"]
---

# Period Close Initiated Event

**Definition.** Period Close Initiated Event is the business event marking the start of an accounting-period close once the period has been cut off. Period Close Initiated Event triggers the record-to-report cycle in the finance and treasury function.

**Also known as:** Close Started Event, Period-End Triggered Event.

## Relationships
- Period Close Initiated Event is related to the Finance & Treasury domain.
- Period Close Initiated Event causes Close Subledgers.
- Period Close Initiated Event mentions Financial Close.

## Details
Period Close Initiated Event fires when the accounting calendar reaches the period-end cut-off and the close window opens. The event sets the period cut-off date, locks new postings to the closing period and signals the general-ledger accounting team to begin closing the AP, AR, fixed-asset and inventory subledgers. Period Close Initiated Event is the trigger that starts the Financial Close process and its first step, ensuring transactions are captured in the correct period before adjusting journals, reconciliation, intercompany elimination and consolidation proceed.

## References
- https://www.highradius.com/resources/Blog/ultimate-guide-on-financial-close-process/
- https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf
