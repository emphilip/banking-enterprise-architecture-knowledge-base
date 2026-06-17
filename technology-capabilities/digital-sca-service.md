---
id: digital-sca-service
title: Digital SCA Service
type: technology-capability
domain: Channels & Engagement
level: L2
aliases: ["Step-Up Authentication Service", "In-App SCA", "Dynamic Linking Service"]
status: draft
sources: ["https://www.onespan.com/blog/strong-customer-authentication-under-psd2-good-bad-and-ugly", "https://www.saltedge.com/products/strong_customer_authentication"]
---

# Digital SCA Service

**Definition.** Digital SCA Service is the technology sub-capability enforcing in-channel strong customer authentication for digital sessions and transactions, including step-up, dynamic linking, biometrics and transaction risk analysis.
**Also known as:** Step-Up Authentication Service, In-App SCA, Dynamic Linking Service.

## Relationships
- Digital SCA Service is defined in the Channels & Engagement domain.
- Digital SCA Service is derived from Digital Channel Platform.
- Digital SCA Service depends on Customer Identity.
- Digital SCA Service is related to Customer Authentication.

## Details
Digital SCA Service implements PSD2 Strong Customer Authentication: two of three factors (knowledge, possession, inherence), dynamic linking that binds an authentication code to the specific payee and amount, and Transaction Risk Analysis (TRA) to apply exemptions for low-risk payments. It orchestrates step-up challenges (push approval, FIDO/passkey, biometrics) mid-session and records auditable evidence. It delegates the underlying authenticator and credential management to the enterprise identity layer rather than owning credentials itself.

## References
- [OneSpan: Strong Customer Authentication under PSD2](https://www.onespan.com/blog/strong-customer-authentication-under-psd2-good-bad-and-ugly)
- [Salt Edge: Strong Customer Authentication](https://www.saltedge.com/products/strong_customer_authentication)
