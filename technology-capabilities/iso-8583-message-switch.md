---
id: iso-8583-message-switch
title: ISO 8583 Message Switch
type: technology-capability
domain: Core Processing
level: L3
aliases: ["8583 Switch Service", "Card Scheme Message Switch", "Authorization Message Switch"]
status: draft
sources: ["https://medium.com/@rizkyian78/iso-8583-the-messaging-standard-behind-every-card-transaction-2ef1246f8663", "https://www.linkedin.com/pulse/whats-iso-8583-message-flow-part-two-ahmed-el-nazer"]
---

# ISO 8583 Message Switch

**Definition.** ISO 8583 Message Switch parses, validates and routes ISO 8583 authorization, reversal and advice messages between acquirers, schemes and the issuer host, preserving transaction context for request-response matching.
**Also known as:** 8583 Switch Service, Card Scheme Message Switch, Authorization Message Switch.

## Relationships
- ISO 8583 Message Switch is defined in the Core Processing domain.
- ISO 8583 Message Switch is derived from Card Transaction Switch.
- ISO 8583 Message Switch is related to Card Authorization Engine.

## Details
ISO 8583 Message Switch handles the scheme messaging standard for card transactions. It decodes the Message Type Indicator (for example 0100 authorization request, 0110 response, 0400 reversal) and the bitmap-indexed data elements such as DE2 primary account number, DE4 amount, DE7 transmission datetime, DE11 STAN and DE37 retrieval reference number. The switch keys requests and responses on STAN and RRN so a 0110 is matched to its 0100, manages timeouts and reversals, and routes the parsed message to Card Authorization Engine for the approve/decline decision before formatting the response back to the acquirer.

## References
- [ISO 8583: the messaging standard behind card transactions](https://medium.com/@rizkyian78/iso-8583-the-messaging-standard-behind-every-card-transaction-2ef1246f8663)
- [ISO 8583 message flow](https://www.linkedin.com/pulse/whats-iso-8583-message-flow-part-two-ahmed-el-nazer)
