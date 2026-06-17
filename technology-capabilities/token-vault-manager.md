---
id: token-vault-manager
title: Token Vault Manager
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Issuer Token Vault Service", "PAN Token Vault", "Token Mapping Store"]
status: draft
sources: ["https://thefinancialbrand.com/news/payments-trends/explainer-how-bank-card-tokenization-works-186561", "https://www.securetechalliance.org/wp-content/uploads/EMV-Tokenization-Encryption-WP-v51-102414-FINAL-clean.pdf"]
---

# Token Vault Manager

**Definition.** Token Vault Manager operates the secure token vault that stores and protects the mapping between primary account numbers and issued tokens together with their domain and usage controls.
**Also known as:** Issuer Token Vault Service, PAN Token Vault, Token Mapping Store.

## Relationships
- Token Vault Manager is defined in the Core Processing domain.
- Token Vault Manager is derived from Card Tokenization Service.
- Token Vault Manager is related to Network Token Service.

## Details
Token Vault Manager is the protected store that holds the one-way mapping between a primary account number and the tokens issued against it. Each vault record carries the token, the associated PAN, the token domain and usage restrictions (channel, merchant, device) and the token state. De-tokenisation — resolving a token back to the funding PAN at authorisation time — is performed only inside the vault boundary, which keeps the real PAN out of merchant and processor systems and narrows PCI scope. The mappings it stores are populated by Network Token Service when scheme tokens are provisioned.

## References
- [How bank card tokenization works (The Financial Brand)](https://thefinancialbrand.com/news/payments-trends/explainer-how-bank-card-tokenization-works-186561)
- [EMV Tokenization and encryption white paper (Secure Technology Alliance)](https://www.securetechalliance.org/wp-content/uploads/EMV-Tokenization-Encryption-WP-v51-102414-FINAL-clean.pdf)
