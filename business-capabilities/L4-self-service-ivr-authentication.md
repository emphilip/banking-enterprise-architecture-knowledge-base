---
id: self-service-ivr-authentication
title: Self-Service IVR Authentication
type: business-capability
domain: Channels & Engagement
level: L4
aliases: ["Voice Authentication", "IVR Caller Verification"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://justcall.io/blog/what-is-ivr-in-banking.html"]
---

# Self-Service IVR Authentication

**Definition.** Self-Service IVR Authentication is the Channels & Engagement capability that verifies callers in the voice channel using PIN, OTP and voice biometrics before servicing, realising the BIAN Party Authentication service domain in the IVR context.
**Also known as:** Voice Authentication, IVR Caller Verification.

## Relationships
- Self-Service IVR Authentication is defined in the Channels & Engagement domain.
- Self-Service IVR Authentication is derived from Self-Service IVR.
- Self-Service IVR Authentication depends on the Customer Authentication capability.

## Details
Self-Service IVR Authentication realises BIAN Party Authentication in the voice channel: verifying callers via card/account plus PIN, one-time passcode, knowledge factors and increasingly passive voice biometrics that match the speaker's voiceprint during natural speech. Authentication strength is risk-tiered to FFIEC layered-security expectations, with step-up before high-risk servicing and money movement. Voice biometric enrolment requires explicit consent and GDPR/BIPA-compliant handling of biometric templates, and anti-spoofing guards against recordings and synthetic voice. Successful IVR authentication can be passed to a connected agent so the customer is not re-verified on transfer.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [FFIEC Authentication Guidance](https://www.ffiec.gov/guidance.htm)
- [What is IVR in Banking](https://justcall.io/blog/what-is-ivr-in-banking.html)
