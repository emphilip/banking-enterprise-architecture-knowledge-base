---
id: receive-authorization-request
title: Receive Authorization Request
type: process-step
process: Card Transaction Authorization
order: 1
status: draft
sources: ["https://dpogroup.com/blog/a-step-by-step-guide-to-the-emv-and-online-card-transaction-journey/"]
---

# Receive Authorization Request

**Definition.** Receive Authorization Request receives the Authorization Request (with ARQC) routed from the acquirer via the scheme.

## Relationships
- Receive Authorization Request is defined in the Card Transaction Authorization process.
- Receive Authorization Request causes Validate Card Cryptogram.
- Receive Authorization Request depends on the Card Processing capability.
- Receive Authorization Request mentions Authorization Request.
- Receive Authorization Request mentions Card Operations Analyst.

## Details
Receive Authorization Request ingests the ISO 8583 Authorization Request carrying the EMV ARQC, enforcing PCI DSS PAN protection and message-integrity controls on intake.

## References
- [EMV and online card transaction journey](https://dpogroup.com/blog/a-step-by-step-guide-to-the-emv-and-online-card-transaction-journey/)
