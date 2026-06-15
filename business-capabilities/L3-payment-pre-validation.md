---
id: payment-pre-validation
title: Payment Pre-Validation
type: business-capability
domain: Payments
level: L3
aliases: ["Beneficiary Validation", "Account Verification", "Confirmation of Payee"]
status: draft
sources: ["https://deepwiki.com/bian-official/public/5.1-payment-operations", "https://www.iso20022payments.com/cbpr/pain-001-pain-002/"]
---

# Payment Pre-Validation

**Definition.** Payment Pre-Validation verifies beneficiary, account and routing details before an instruction is submitted to a rail, reducing failed and misdirected payments in the BIAN Payment Order pre-processing stage.
**Also known as:** Beneficiary Validation, Account Verification, Confirmation of Payee.

## Relationships
- Payment Pre-Validation is defined in the Payments domain.
- Payment Pre-Validation is derived from Payment Initiation.
- Payment Pre-Validation depends on the API Management capability.

## Details
Payment Pre-Validation grounds in the pre-processing stage of the BIAN Payment Order service domain. It checks beneficiary, account and routing data to reduce failed and misdirected payments. Confirmation of Payee and account verification services are typical implementations, often consumed through external APIs.

## References
- [BIAN Payment Operations](https://deepwiki.com/bian-official/public/5.1-payment-operations)
- [ISO 20022 pain.001/pain.002](https://www.iso20022payments.com/cbpr/pain-001-pain-002/)
