---
id: ingest-transaction-stream
title: Ingest Transaction Stream
type: process-step
process: Fraud Detection
order: 1
aliases: ["Capture Event Stream", "Stream Ingestion Step"]
status: draft
sources: ["https://www.getfocal.ai/blog/bank-fraud-investigation"]
---

# Ingest Transaction Stream

**Definition.** Ingest Transaction Stream ingests real-time transaction and event streams for fraud scoring.
**Also known as:** Capture Event Stream, Stream Ingestion Step.

## Relationships
- Ingest Transaction Stream is defined in the Fraud Detection process.
- Ingest Transaction Stream causes Screen Transaction Risk.
- Ingest Transaction Stream depends on the Data Streaming capability.
- Ingest Transaction Stream mentions Fraud Detection Analyst.

## Details
The Fraud Detection Analyst relies on a normalized event feed produced from the ingested streams. Controls include stream integrity, latency SLAs and data completeness so that no in-scope event is missed before scoring.

## References
- [Focal — Bank Fraud Investigation](https://www.getfocal.ai/blog/bank-fraud-investigation)
