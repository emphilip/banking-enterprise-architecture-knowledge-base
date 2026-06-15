---
id: statement-issued-event
title: Statement Issued Event
type: event
domain: Deposits & Accounts
aliases: ["Statement Generated Event", "Statement Delivered Event"]
status: draft
sources: ["https://www.ecfr.gov/current/title-12/chapter-X/part-1030", "https://www.federalreserve.gov/boarddocs/caletters/2009/0914/09-14-attachment.pdf"]
---

# Statement Issued Event

**Definition.** Statement Issued Event is the business event signalling that a periodic deposit statement has been generated and delivered to the customer. Statement Issued Event records completion of a statement cycle within deposit servicing.

**Also known as:** Statement Generated Event, Statement Delivered Event.

## Relationships
- Statement Issued Event is related to the Deposits & Accounts domain.
- Statement Issued Event mentions Statement Generation.
- Statement Issued Event causes Deliver Statement.

## Details
Statement Issued Event fires at Deliver Statement when the rendered Bank Account Statement is dispatched by mail or electronic channel, carrying the account identifier, cycle period, delivery channel and document reference. Statement Issued Event opens the Reg E error-resolution and billing-dispute clock, triggers archival for retention, and feeds self-service retrieval. Notification systems consume Statement Issued Event to alert customers that a new statement is available.

## References
- https://www.ecfr.gov/current/title-12/chapter-X/part-1030
- https://www.federalreserve.gov/boarddocs/caletters/2009/0914/09-14-attachment.pdf
