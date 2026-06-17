---
id: customer-risk-rated-event
title: Customer Risk Rated Event
type: event
domain: Compliance & Financial Crime
aliases: ["CDD Completed Event", "Risk Rating Assigned Event"]
status: draft
sources: ["https://www.sanctions.io/blog/cdd-sdd-and-kyc-explained"]
---

# Customer Risk Rated Event

**Definition.** Customer Risk Rated Event is the business event raised when a customer's CDD risk rating is assigned or changed during onboarding diligence. Customer Risk Rated Event signals that the risk tier is set and drives the onboarding decision and ongoing-monitoring cadence.
**Also known as:** CDD Completed Event, Risk Rating Assigned Event.

## Relationships
- Customer Risk Rated Event is related to the Compliance & Financial Crime domain.
- Customer Risk Rated Event mentions Customer Due Diligence Onboarding.
- Customer Risk Rated Event causes Trigger Enhanced Diligence.

## Details
Customer Risk Rated Event carries the customer identifier, the assigned customer risk score and tier, the contributing risk factors (geography, product, channel, behaviour, screening outcome) and the rating timestamp. A high-risk or PEP outcome triggers enhanced due diligence (source of wealth and source of funds) and senior-management approval; a standard outcome proceeds to the accept decision. The event also sets the risk-based review cycle for perpetual KYC and feeds downstream transaction-monitoring segmentation.

## References
- [FATF risk-based approach guidance](https://www.fatf-gafi.org/en/topics/fatf-recommendations/risk-based-approach.html)
- [Wolfsberg Group standards](https://www.wolfsberg-principles.com/)
