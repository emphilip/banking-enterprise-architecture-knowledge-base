---
id: limit-breach-event
title: Limit Breach Event
type: event
domain: Risk Management
aliases: ["Appetite Breach Event", "Threshold Breach Event"]
status: draft
sources: ["https://www.bis.org/publ/bcbs239.htm", "https://www.deloitte.com/us/en/services/consulting/articles/basel-risk-data-aggregation-and-reporting-requirements.html"]
---

# Limit Breach Event

**Definition.** Limit Breach Event is the business event raised when an exposure breaches an approved risk limit or appetite tolerance, triggering escalation through risk governance.

**Also known as:** Appetite Breach Event, Threshold Breach Event.

## Relationships
- Limit Breach Event is related to the Risk Management domain.
- Limit Breach Event causes Escalate Limit Breach.
- Limit Breach Event mentions Risk Report.

## Details
Limit Breach Event fires during the risk-reporting cycle when an aggregated and reconciled exposure exceeds an approved limit or moves outside an appetite tolerance band. The event drives severity-based escalation: minor utilisation warnings route to risk owners, while material breaches escalate to risk committees and the board, each with defined thresholds, owners and audit trails. Limit Breach Event is the operational link between the Risk Appetite Statement and day-to-day monitoring, ensuring that appetite is not merely declared but actively enforced. Recurrence patterns also inform whether limits, the appetite itself, or underlying controls need recalibration.

## References
- https://www.bis.org/publ/bcbs239.htm
- https://www.deloitte.com/us/en/services/consulting/articles/basel-risk-data-aggregation-and-reporting-requirements.html
