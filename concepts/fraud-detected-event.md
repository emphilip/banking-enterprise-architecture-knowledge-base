---
id: fraud-detected-event
title: Fraud Detected Event
type: event
domain: Cards
aliases: ["Card Fraud Event", "Fraud Confirmed Event"]
status: draft
sources: ["https://chargebacks911.com/velocity-checks/", "https://www.sardine.ai/issuing-fraud"]
---

# Fraud Detected Event

**Definition.** Fraud Detected Event is the event raised when card fraud is detected or confirmed, triggering containment of the affected card. Fraud Detected Event initiates the card-fraud handling flow and the operational response of verification, blocking and reissue.

**Also known as:** Card Fraud Event, Fraud Confirmed Event.

## Relationships
- Fraud Detected Event is related to the Cards domain.
- Fraud Detected Event mentions Card Fraud Handling.
- Fraud Detected Event causes Triage Fraud Alert.

## Details
Fraud Detected Event fires when real-time scoring or velocity rules flag a suspect card transaction or pattern, carrying the card identifier, the triggering rule or risk score, the suspect transaction set and a severity grade. Fraud Detected Event causes the Fraud Alert to be triaged and prioritised, and where confirmed it drives cardholder verification, blocking of the compromised card to stop further authorizations, and reissue. Downstream, Fraud Detected Event feeds fraud-claim adjudication under Reg E and referral for SAR consideration, and updates fraud-model feedback loops.

## References
- https://chargebacks911.com/velocity-checks/
- https://www.sardine.ai/issuing-fraud
