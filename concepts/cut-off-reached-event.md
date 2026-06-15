---
id: cut-off-reached-event
title: Cut-Off Reached Event
type: event
domain: Payments
aliases: ["Cut-Off Event", "Window Closed Event"]
status: draft
sources: ["https://achdevguide.nacha.org/how-ach-works"]
---

# Cut-Off Reached Event

**Definition.** Cut-Off Reached Event is the time-based event marking a clearing-rail or value-date cut-off. Cut-Off Reached Event triggers clearing submission in payment processing and positioning in cash management.

**Also known as:** Cut-Off Event, Window Closed Event.

## Relationships
- Cut-Off Reached Event is related to the Payments domain.
- Cut-Off Reached Event causes Submit To Clearing.
- Cut-Off Reached Event mentions Payment Processing.
- Cut-Off Reached Event mentions Cash Management.

## Details
Cut-Off Reached Event fires when a scheme window or value-date deadline is reached, forcing batched or queued payments to be dispatched to the ACH operator, Fedwire or instant-payment network before the window closes. In treasury, the same event drives end-of-day cash positioning and funding decisions tied to the value date.

## References
- https://achdevguide.nacha.org/how-ach-works
