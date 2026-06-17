---
id: beneficiary-verification-service
title: Beneficiary Verification Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Confirmation of Payee Service", "Payee Validation Service", "Account Verification Service"]
status: draft
sources: ["https://developer.payments.jpmorgan.com/blog/guides/importance-validation-services-financial-transactions", "https://www.linkedin.com/pulse/payments-ecosystem-topic-banks-payment-engine-sreenivasula-jambapuram-fvtrc"]
---

# Beneficiary Verification Service

**Definition.** Beneficiary Verification Service validates payee account and name details against external data sources before a payment is released, returning positive, partial or negative match outcomes.
**Also known as:** Confirmation of Payee Service, Payee Validation Service, Account Verification Service.

## Relationships
- Beneficiary Verification Service is defined in the Core Processing domain.
- Beneficiary Verification Service is derived from Payment Validation Engine.

## Details
Beneficiary Verification Service checks that the account a payment is going to belongs to the person or business the payer intends to pay, before funds leave the account. It compares the supplied payee name against the name on the destination account using fuzzy matching that tolerates abbreviations and minor differences, and returns a match outcome — full match, close/partial match with the actual name suggested, or no match — so the payer can stop and reconsider. This Confirmation of Payee style check is a primary control against authorised push payment fraud and misdirected payments, sitting in the pre-release validation step of the payment flow.

## References
- [Importance of validation services in financial transactions (J.P. Morgan)](https://developer.payments.jpmorgan.com/blog/guides/importance-validation-services-financial-transactions)
- [Bank payment engine in the payments ecosystem (LinkedIn)](https://www.linkedin.com/pulse/payments-ecosystem-topic-banks-payment-engine-sreenivasula-jambapuram-fvtrc)
