---
id: network-token-service
title: Network Token Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Scheme Token Connector", "EMVCo Token Service", "VTS MDES Connector"]
status: draft
sources: ["https://evervault.com/blog/what-are-network-tokens-and-how-do-they-work", "https://www.securetechalliance.org/wp-content/uploads/EMV-Tokenization-Encryption-WP-v51-102414-FINAL-clean.pdf"]
---

# Network Token Service

**Definition.** Network Token Service integrates with scheme token service providers to request, provision and lifecycle-manage EMVCo network tokens, mapping PAN to scheme tokens for card-on-file and wallet credentials.
**Also known as:** Scheme Token Connector, EMVCo Token Service, VTS MDES Connector.

## Relationships
- Network Token Service is defined in the Core Processing domain.
- Network Token Service is derived from Card Tokenization Service.
- Network Token Service is related to Token Vault Manager.

## Details
Network Token Service connects the issuer to scheme token service providers such as Visa VTS and Mastercard MDES under the EMVCo payment tokenisation framework. It requests provisioning of a network token (a DPAN, device or domain-specific account number distinct from the funding PAN), supplies and responds to identification-and-verification (ID&V) steps, and handles token lifecycle events — activation, suspension, resume, delete and automatic updates on card reissue. Because the DPAN carries domain controls, a compromised card-on-file or wallet credential can be revoked without reissuing the underlying PAN. The PAN-to-token mapping it obtains is persisted by Token Vault Manager.

## References
- [What are network tokens and how do they work (Evervault)](https://evervault.com/blog/what-are-network-tokens-and-how-do-they-work)
- [EMV Tokenization and encryption white paper (Secure Technology Alliance)](https://www.securetechalliance.org/wp-content/uploads/EMV-Tokenization-Encryption-WP-v51-102414-FINAL-clean.pdf)
