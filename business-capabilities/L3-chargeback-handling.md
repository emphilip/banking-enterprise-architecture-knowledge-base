---
id: chargeback-handling
title: Chargeback Handling
type: business-capability
domain: Cards
level: L3
aliases: ["Chargeback Initiation", "Issuer Chargeback Management"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.mastercard.us/en-us/business/overview/support/rules.html"]
---

# Chargeback Handling

**Definition.** Chargeback Handling initiates and manages issuer-side chargebacks against transactions, applying scheme reason codes within the BIAN Card Case service domain.
**Also known as:** Chargeback Initiation, Issuer Chargeback Management.

## Relationships
- Chargeback Handling is defined in the Cards domain.
- Chargeback Handling is derived from Dispute Management.
- Chargeback Handling depends on the Workflow Orchestration capability.

## Details
The BIAN Card Case service domain orchestrates the issuer chargeback against the acquirer through the scheme dispute systems (Visa VCR, Mastercard Mastercom). It assigns a scheme reason code — for example Visa dispute category 10 (Fraud), 11 (Authorization), 12 (Processing Errors), 13 (Consumer Disputes), or Mastercard codes such as 4853/4837 — within the network time limits (typically 120 days from transaction). Reg E (12 CFR 1005) and Reg Z govern the cardholder's underlying error-resolution rights that trigger the chargeback.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Mastercard Rules](https://www.mastercard.us/en-us/business/overview/support/rules.html)
