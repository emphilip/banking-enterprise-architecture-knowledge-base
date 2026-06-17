---
id: kyc-profile-verified-event
title: KYC Profile Verified Event
type: event
domain: Compliance & Financial Crime
aliases: ["KYC Completed Event", "KYC Verified Event"]
status: draft
sources: ["https://seon.io/resources/kyc-verification-process/"]
---

# KYC Profile Verified Event

**Definition.** KYC Profile Verified Event is the business event signalling that a KYC Profile has been verified, approved and scheduled for ongoing review. KYC Profile Verified Event confirms the customer has cleared identity proofing, screening and risk rating and can be activated.
**Also known as:** KYC Completed Event, KYC Verified Event.

## Relationships
- KYC Profile Verified Event is related to the Compliance & Financial Crime domain.
- KYC Profile Verified Event mentions KYC Verification.
- KYC Profile Verified Event mentions KYC Profile.
- KYC Profile Verified Event causes Schedule KYC Review.

## Details
KYC Profile Verified Event carries the customer identifier, the KYC Profile reference, the approval decision and approver (four-eyes), the screening disposition and the assigned review cadence. It is emitted after the KYC outcome is approved and triggers scheduling of the risk-based periodic review and trigger-based refresh rules for perpetual KYC. Downstream, the event releases account activation and unblocks servicing, and it is retained as evidence of completed customer due diligence.

## References
- [FATF Recommendation 10 (CDD)](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html)
- [FinCEN CDD Rule guidance](https://www.fincen.gov/resources/statutes-regulations/guidance)
