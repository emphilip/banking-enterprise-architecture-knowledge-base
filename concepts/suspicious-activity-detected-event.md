---
id: suspicious-activity-detected-event
title: Suspicious Activity Detected Event
type: event
domain: Compliance & Financial Crime
aliases: ["Suspicion Confirmed Event", "SAR Triggered Event"]
status: draft
sources: ["https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-suspicious-activity-report-sar"]
---

# Suspicious Activity Detected Event

**Definition.** Suspicious Activity Detected Event is the business event raised when an investigation concludes that reasonable grounds for suspicion exist. Suspicious Activity Detected Event triggers the SAR decision and filing path and escalates the case to the MLRO.
**Also known as:** Suspicion Confirmed Event, SAR Triggered Event.

## Relationships
- Suspicious Activity Detected Event is related to the Compliance & Financial Crime domain.
- Suspicious Activity Detected Event mentions Suspicious Activity Reporting.
- Suspicious Activity Detected Event causes Lodge SAR Filing.

## Details
Suspicious Activity Detected Event carries the case identifier, the customer and account references, the suspicion determination and supporting findings, the relevant money-laundering typology and the escalating investigator. It is emitted when the reasonable-grounds standard is met and routes the case to the MLRO for sign-off and filing within the FinCEN 30-day deadline. The event is handled under strict tipping-off prohibitions and feeds continuing-activity tracking and the five-year retention obligation.

## References
- [FinCEN SAR FAQs](https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-suspicious-activity-report-sar)
- [FATF Recommendation 20](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html)
