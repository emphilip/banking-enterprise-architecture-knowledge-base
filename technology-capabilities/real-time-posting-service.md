---
id: real-time-posting-service
title: Real-Time Posting Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Real-Time Ledger Service", "Instant Posting Service", "Streaming Postings"]
status: draft
sources: ["https://www.thoughtmachine.net/blog/product-development", "https://aws.amazon.com/blogs/apn/meeting-bank-grade-requirements-for-real-time-and-resilient-core-banking-with-finxact-on-aws/"]
---

# Real-Time Posting Service

**Definition.** Real-Time Posting Service is the technology capability that provides low-latency, idempotent real-time posting and instant balance updates, replacing overnight batch with an event-driven model that exposes a postings API and a streaming event feed of ledger changes.
**Also known as:** Real-Time Ledger Service, Instant Posting Service, Streaming Postings.

## Relationships
- Real-Time Posting Service is defined in the Core Processing domain.
- Real-Time Posting Service is derived from Transaction Posting Engine.
- Real-Time Posting Service depends on Data Streaming.

## Details
Real-Time Posting Service delivers idempotent, low-latency postings with instant balance updates instead of overnight batch cycles. Thought Machine exposes Postings and Streaming APIs that emit ledger changes as events, and the Finxact-on-AWS reference details a batch-free, event-driven core, so real-time posting publishes a continuous stream of balance and entry events to downstream consumers.

## References
- [Thought Machine product development](https://www.thoughtmachine.net/blog/product-development)
- [Real-time core banking with Finxact on AWS](https://aws.amazon.com/blogs/apn/meeting-bank-grade-requirements-for-real-time-and-resilient-core-banking-with-finxact-on-aws/)
