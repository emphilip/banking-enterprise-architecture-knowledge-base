---
id: fraud-case-closed-event
title: Fraud Case Closed Event
type: event
domain: Risk Management
aliases: ["Fraud Resolved Event", "Case Closed Event (Fraud)"]
status: draft
sources: ["https://www.getfocal.ai/blog/bank-fraud-investigation", "https://www.fincen.gov/resources/filing-information"]
---

# Fraud Case Closed Event

**Definition.** Fraud Case Closed Event is the business event signalling that a fraud case has been adjudicated, recovered and closed, with confirmed outcomes fed back to detection models.

**Also known as:** Fraud Resolved Event, Case Closed Event (Fraud).

## Relationships
- Fraud Case Closed Event is related to the Risk Management domain.
- Fraud Case Closed Event causes Feed Detection Models.
- Fraud Case Closed Event mentions Fraud Case.

## Details
Fraud Case Closed Event is emitted at the end of the Fraud Investigation process, once the investigator has confirmed or dismissed the fraud, recovered or reversed funds where applicable, filed any required SAR within the regulatory window, and reached a final disposition on the Fraud Case. The event triggers the model-feedback loop, where confirmed labels are returned to tune detection rules and machine-learning models, improving future scoring quality. Closing the case as an explicit event supports loss accounting, regulatory recordkeeping and performance metrics such as fraud loss rate, recovery rate and false-positive rate, and ensures label quality and change governance for the feedback into detection.

## References
- https://www.getfocal.ai/blog/bank-fraud-investigation
- https://www.fincen.gov/resources/filing-information
