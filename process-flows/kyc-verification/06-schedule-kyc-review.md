---
id: schedule-kyc-review
title: Schedule KYC Review
type: process-step
process: KYC Verification
order: 6
aliases: ["Set KYC Review", "Review Scheduling Step"]
status: draft
sources: ["https://seon.io/resources/kyc-verification-process/", "https://kyc-chain.com/kyc-verification-process-and-common-requirements/"]
---

# Schedule KYC Review

**Definition.** Schedule KYC Review sets the risk-based review cycle and trigger-based refresh rules and emits the KYC Profile Verified Event.
**Also known as:** Set KYC Review, Review Scheduling Step.

## Relationships
- Schedule KYC Review is defined in the KYC Verification process.
- Schedule KYC Review depends on the KYC Management capability.
- Schedule KYC Review mentions KYC Analyst.
- Schedule KYC Review mentions KYC Profile Verified Event.

## Details
The KYC Analyst sets the risk-based review cadence and perpetual-KYC triggers from the approval decision and Customer Risk Score. Controls include review-cadence governance and trigger-based refresh, with completion signalled by the KYC Profile Verified Event. This is the final step of KYC Verification.

## References
- [SEON — KYC verification process](https://seon.io/resources/kyc-verification-process/)
- [KYC-Chain — KYC verification process](https://kyc-chain.com/kyc-verification-process-and-common-requirements/)
