---
id: digital-consent-capture
title: Digital Consent Capture
type: business-capability
domain: Channels & Engagement
level: L4
aliases: ["E-Consent Capture", "Terms Acceptance"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://newgensoft.com/blog/guide-to-digital-customer-onboarding-in-banking/"]
---

# Digital Consent Capture

**Definition.** Digital Consent Capture is the Channels & Engagement capability that records terms acceptance and data-sharing permissions in the digital onboarding flow, fronting the BIAN Customer Access Entitlement service domain and feeding the Consent & Preference Management capability.
**Also known as:** E-Consent Capture, Terms Acceptance.

## Relationships
- Digital Consent Capture is defined in the Channels & Engagement domain.
- Digital Consent Capture is derived from Digital Onboarding.
- Digital Consent Capture depends on the Customer Identity capability.

## Details
Digital Consent Capture fronts BIAN Customer Access Entitlement by recording explicit, granular consents (terms acceptance, marketing permissions, open-banking data sharing) with a tamper-evident audit trail of what was shown, when and by whom. It must satisfy GDPR Article 7 conditions for valid consent (freely given, specific, informed, unambiguous, withdrawable) and the US ESIGN Act for legally binding electronic signatures. Captured consents flow to Consent & Preference Management as the system of record, and PSD2 open-banking consent is time-boxed and re-confirmable. Versioned terms ensure the exact disclosure a customer agreed to is reproducible for disputes.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [GDPR Article 7 Conditions for Consent](https://gdpr-info.eu/art-7-gdpr/)
- [Guide to Digital Customer Onboarding](https://newgensoft.com/blog/guide-to-digital-customer-onboarding-in-banking/)
