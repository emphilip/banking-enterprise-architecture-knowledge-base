---
id: representment-handling
title: Representment Handling
type: business-capability
domain: Cards
level: L3
aliases: ["Second Presentment Handling", "Re-presentment"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.mastercard.us/en-us/business/overview/support/rules.html"]
---

# Representment Handling

**Definition.** Representment Handling processes the merchant/acquirer second presentment and re-presented evidence against an issuer chargeback within the BIAN Card Case service domain.
**Also known as:** Second Presentment Handling, Re-presentment.

## Relationships
- Representment Handling is defined in the Cards domain.
- Representment Handling is derived from Dispute Management.
- Representment Handling depends on the Workflow Orchestration capability.

## Details
After the issuer files a chargeback, the acquirer may respond with a second presentment (re-presentment) supplying remedial evidence such as a valid AVS/CVV2 result, 3-D Secure liability shift, or proof of delivery. Within the BIAN Card Case service domain this capability evaluates the second presentment against the original reason code and the scheme rules (Visa VCR second-presentment conditions, Mastercard second-presentment message reason codes) and decides whether to accept the re-presentment or escalate to pre-arbitration.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Mastercard Rules](https://www.mastercard.us/en-us/business/overview/support/rules.html)
