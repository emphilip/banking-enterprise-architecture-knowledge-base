---
id: core-banking-processing
title: Core Banking Processing
type: technology-capability
domain: Core Processing
aliases: ["Core Banking System", "Core Ledger"]
status: draft
---

# Core Banking Processing

**Definition.** Core Banking Processing is the technology capability that maintains the system of record for accounts, balances, postings, and product processing, executing deposits, withdrawals, interest, and the bank's central ledger in real time or batch.
**Also known as:** Core Banking System, Core Ledger.

## Relationships
- Core Banking Processing is defined in the Core Processing domain.
- Core Banking Processing depends on the General Ledger Engine capability.
- Core Banking Processing mentions Temenos T24.
- Core Banking Processing mentions Legacy Mainframe Core.
- Core Banking Processing mentions Thought Machine Vault.
- Core Banking Processing mentions Mambu.
- Core Banking Processing is related to Payment Orchestration.

## Details
Core Banking Processing sits at the centre of a bank's reference architecture, exposing product and account services to channels via the Integration Platform and API Management capabilities. Legacy realizations are monolithic mainframe and packaged cores running nightly batch, while modern cloud-native platforms such as Thought Machine Vault, Mambu, and 10x Banking offer real-time, ledger-as-code, and event-driven designs that scale horizontally. Migration typically proceeds product-by-product to retire batch windows and enable continuous processing.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Thought Machine Vault Architecture](https://www.thoughtmachine.net/vault-core)
