---
id: card-fraud-handling
title: Card Fraud Handling
type: business-process
domain: Cards
aliases: ["Card Fraud Management", "Card Fraud Operations"]
status: draft
sources: ["https://www.checkout.com/blog/velocity-check", "https://www.sardine.ai/issuing-fraud", "https://chargebacks911.com/velocity-checks/"]
---

# Card Fraud Handling

**Definition.** Card Fraud Handling is the detection and operational handling of suspected card fraud: triage of fraud alerts, cardholder verification/outreach, blocking and reissuing the compromised card, fraud-claim adjudication and SAR consideration.
**Also known as:** Card Fraud Management, Card Fraud Operations.

## Relationships
- Card Fraud Handling is defined in the Cards domain.
- Card Fraud Handling depends on the Fraud Management capability.

## Details
Card Fraud Handling triages a Fraud Alert raised by real-time scoring and velocity rules, verifies suspect activity with the cardholder, and blocks the compromised card to stop further authorizations. The card is reissued and re-credentialed, the fraud claim is adjudicated under Reg E unauthorized-EFT liability rules, and confirmed fraud is referred for SAR consideration and regulatory reporting. PCI DSS protects card data throughout. Actors include the Card Fraud Analyst.

## Flow
- Triage Fraud Alert causes Verify Cardholder Activity.
- Verify Cardholder Activity causes Block Compromised Card.
- Block Compromised Card causes Reissue Card.
- Reissue Card causes Adjudicate Fraud Claim.
- Adjudicate Fraud Claim causes Refer Suspicious Activity.

## References
- [Velocity checks](https://www.checkout.com/blog/velocity-check)
- [Issuing fraud](https://www.sardine.ai/issuing-fraud)
- [Velocity checks explained](https://chargebacks911.com/velocity-checks/)
