---
id: posting-determination-service
title: Posting Determination Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Posting Rule Resolver", "Ledger Entry Determination", "Entry Generation Service"]
status: draft
sources: ["https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products", "https://www.oracle.com/financial-services/banking/flexcube/core-banking-software/"]
---

# Posting Determination Service

**Definition.** Posting Determination Service evaluates the configurable rules that determine how an incoming transaction is decomposed into debit and credit ledger entries, including value dating, contra-account selection and posting restrictions.
**Also known as:** Posting Rule Resolver, Ledger Entry Determination, Entry Generation Service.

## Relationships
- Posting Determination Service is defined in the Core Processing domain.
- Posting Determination Service is derived from Transaction Posting Engine.
- Posting Determination Service is related to General Ledger Posting.

## Details
Posting Determination Service turns a business event into a balanced set of ledger entries. For each transaction type it resolves the debit and credit legs, the value date versus booking date, the contra and suspense accounts to use, and any posting restrictions (blocked, hold, no-debit) before the entries are committed. Core-banking ledger models keep this rule layer separate from the immutable double-entry ledger so the mapping from event to entries is configurable per product. The resolved entries are then handed to General Ledger Posting for downstream GL transfer.

## References
- [Core banking data model and ledger (clefincode)](https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products)
- [Oracle FLEXCUBE core banking](https://www.oracle.com/financial-services/banking/flexcube/core-banking-software/)
