---
id: transaction-posting-engine
title: Transaction Posting Engine
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Posting Engine", "Core Ledger Posting", "Postings Service"]
status: draft
sources: ["https://www.thoughtmachine.net/blog/product-development", "https://aws.amazon.com/blogs/apn/meeting-bank-grade-requirements-for-real-time-and-resilient-core-banking-with-finxact-on-aws/"]
---

# Transaction Posting Engine

**Definition.** Transaction Posting Engine is the technology capability that posts debits and credits to deposit accounts and the core ledger, applying value dating, balance updates, funds availability and double-entry integrity for both real-time and batch transaction streams.
**Also known as:** Posting Engine, Core Ledger Posting, Postings Service.

## Relationships
- Transaction Posting Engine is defined in the Core Processing domain.
- Transaction Posting Engine is derived from Core Banking Processing.
- Transaction Posting Engine is related to Account Servicing.

## Details
Transaction Posting Engine applies debits and credits to deposit accounts and the core ledger while enforcing value dating, funds availability and double-entry integrity. Thought Machine describes a postings ledger as the heart of the core, and the Finxact-on-AWS reference shows an event-driven, batch-free posting model that updates balances in real time, so both real-time and batch transaction streams settle through a single posting path.

## References
- [Thought Machine product development](https://www.thoughtmachine.net/blog/product-development)
- [Real-time core banking with Finxact on AWS](https://aws.amazon.com/blogs/apn/meeting-bank-grade-requirements-for-real-time-and-resilient-core-banking-with-finxact-on-aws/)
