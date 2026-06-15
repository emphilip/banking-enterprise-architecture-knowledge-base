---
id: card-transaction-switch
title: Card Transaction Switch
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Issuer Switch", "ISO 8583 Switch", "Scheme Message Switch"]
status: draft
sources: ["https://en.wikipedia.org/wiki/ISO_8583", "https://www.galileo-ft.com/blog/connect-card-program-to-payment-network/"]
---

# Card Transaction Switch

**Definition.** Card Transaction Switch is the technology capability providing the network-facing switching layer that connects to card schemes, parses and builds ISO 8583 and network messages, and routes authorization, reversal and advice traffic between the schemes and the issuer authorization host.
**Also known as:** Issuer Switch, ISO 8583 Switch, Scheme Message Switch.

## Relationships
- Card Transaction Switch is defined in the Core Processing domain.
- Card Transaction Switch is derived from Card Processing.
- Card Transaction Switch is related to Card Authorization.

## Details
Card Transaction Switch maintains certified connectivity to Visa and Mastercard, encoding and decoding ISO 8583 message types such as 0100 authorization requests, 0110 responses and 0400 reversals. It routes each message between scheme endpoints and the issuer authorization host, handling message versioning, MAC validation and store-and-forward for advices. The switch must pass scheme certification before production traffic flows.

## References
- [ISO 8583](https://en.wikipedia.org/wiki/ISO_8583)
- [Galileo: Connect a Card Program to a Payment Network](https://www.galileo-ft.com/blog/connect-card-program-to-payment-network/)
