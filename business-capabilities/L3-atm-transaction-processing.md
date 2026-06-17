---
id: atm-transaction-processing
title: ATM Transaction Processing
type: business-capability
domain: Channels & Engagement
level: L3
aliases: ["ATM Transactions", "Self-Service Terminal Processing"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://us.brinks.com/branch-services"]
---

# ATM Transaction Processing

**Definition.** ATM Transaction Processing is the Channels & Engagement capability that authorises and fulfils cash withdrawals, deposits and enquiries at ATM devices, realising the BIAN Card Terminal Operations and ATM Network Operations service domains.
**Also known as:** ATM Transactions, Self-Service Terminal Processing.

## Relationships
- ATM Transaction Processing is defined in the Channels & Engagement domain.
- ATM Transaction Processing is derived from ATM Management.
- ATM Transaction Processing depends on the Card Processing capability.

## Details
ATM Transaction Processing realises BIAN Card Terminal Operations: it reads the EMV chip or contactless card, validates the offline/online PIN, and sends an ISO 8583 authorisation request through the acquiring switch to the issuer or to interchange networks (Visa/Plus, Mastercard/Cirrus). EMV at the ATM shifts counterfeit-fraud liability and requires cryptogram validation; PCI PIN and PCI DSS govern key management and encrypted PIN blocks. The capability also drives dispense, deposit acceptance and receipt under ADA self-service accessibility rules (audio jack, reachable height, voice guidance). Stand-in rules apply when the issuer is unreachable.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [EMVCo Specifications](https://www.emvco.com/specifications/)
- [Brinks Branch Services](https://us.brinks.com/branch-services)
