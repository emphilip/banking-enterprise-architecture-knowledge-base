---
id: digital-identity-verification
title: Digital Identity Verification
type: business-capability
domain: Channels & Engagement
level: L4
aliases: ["Remote ID Verification", "eKYC Capture"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://newgensoft.com/blog/guide-to-digital-customer-onboarding-in-banking/"]
---

# Digital Identity Verification

**Definition.** Digital Identity Verification is the Channels & Engagement capability that proves a prospect's identity remotely during onboarding using document and biometric checks, fronting the BIAN Party Authentication service domain; it is distinct from the Customer Management Identity Verification capability by its in-channel digital scope.
**Also known as:** Remote ID Verification, eKYC Capture.

## Relationships
- Digital Identity Verification is defined in the Channels & Engagement domain.
- Digital Identity Verification is derived from Digital Onboarding.
- Digital Identity Verification depends on the Customer Identity capability.

## Details
Digital Identity Verification fronts BIAN Party Authentication for remote enrolment: capturing a government ID image, running document authentication and NFC chip read, then a selfie with passive or active liveness to bind the person to the document. It operationalises eIDAS/eKYC and AML CDD identity requirements, and NIST SP 800-63A Identity Assurance Levels (IAL2) frame the proofing strength. Vendors include Onfido, Jumio and iProov. Bias and false-reject rates across demographics are a controlled risk, with manual review fallback to keep the journey accessible while satisfying regulatory identity evidence.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [NIST SP 800-63A Identity Proofing](https://pages.nist.gov/800-63-3/sp800-63a.html)
- [Guide to Digital Customer Onboarding](https://newgensoft.com/blog/guide-to-digital-customer-onboarding-in-banking/)
