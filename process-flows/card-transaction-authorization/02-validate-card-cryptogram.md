---
id: validate-card-cryptogram
title: Validate Card Cryptogram
type: process-step
process: Card Transaction Authorization
order: 2
status: draft
sources: ["https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html"]
---

# Validate Card Cryptogram

**Definition.** Validate Card Cryptogram validates the EMV ARQC and PIN/CVM to confirm card authenticity and cardholder.

## Relationships
- Validate Card Cryptogram is defined in the Card Transaction Authorization process.
- Validate Card Cryptogram causes Check Available Limit.
- Validate Card Cryptogram depends on the Card Processing capability.
- Validate Card Cryptogram mentions Authorization Request.
- Validate Card Cryptogram mentions Card Operations Analyst.

## Details
Validate Card Cryptogram verifies the EMV ARQC and the PIN/CVM under HSM key control, confirming card authenticity and cardholder presence before limit checks.

## References
- [ARQC validation for issuers](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html)
