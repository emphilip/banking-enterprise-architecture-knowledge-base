---
id: card-tokenization-service
title: Card Tokenization Service
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Token Vault Service", "Network Tokenization", "Digital Card Tokenisation"]
status: draft
sources: ["https://www.marqeta.com/platform/tokenization-digital-wallets", "https://aws.amazon.com/blogs/industries/credit-card-payment-processing-on-aws/"]
---

# Card Tokenization Service

**Definition.** Card Tokenization Service is the technology capability that generates and manages network tokens and a secure token vault, mapping device and wallet tokens to the underlying PAN for digital-wallet provisioning, card-on-file and secure authorization without exposing the real card number.
**Also known as:** Token Vault Service, Network Tokenization, Digital Card Tokenisation.

## Relationships
- Card Tokenization Service is defined in the Core Processing domain.
- Card Tokenization Service is derived from Card Processing.
- Card Tokenization Service depends on Identity Access Management.
- Card Tokenization Service is related to Card Issuing.

## Details
Card Tokenization Service issues network tokens through Visa and Mastercard token services and holds the PAN-to-token mapping in a secure vault that keeps the real card number out of merchant and device systems, reducing PCI DSS scope. It provisions tokens to Apple Pay, Google Pay and card-on-file merchants and resolves tokens to the PAN during authorization. Tokenization preserves PAN confidentiality while enabling per-device cryptograms.

## References
- [Marqeta Tokenization & Digital Wallets](https://www.marqeta.com/platform/tokenization-digital-wallets)
- [Credit Card Payment Processing on AWS](https://aws.amazon.com/blogs/industries/credit-card-payment-processing-on-aws/)
