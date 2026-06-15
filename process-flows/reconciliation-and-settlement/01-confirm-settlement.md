---
id: confirm-settlement
title: Confirm Settlement
type: process-step
process: Reconciliation & Settlement
order: 1
aliases: ["Settlement Confirmation Step", "Capture Settlement"]
status: draft
sources: ["https://fedwireservice.org/", "https://bankersbank.com/solutions/fednow-rtp-settlement-solutions/"]
---

# Confirm Settlement

**Definition.** Confirm Settlement captures settlement advices from operators/correspondents and confirms interbank money movement finality.
**Also known as:** Settlement Confirmation Step, Capture Settlement.

## Relationships
- Confirm Settlement is defined in the Reconciliation & Settlement process.
- Confirm Settlement causes Ingest Bank Statement.
- Confirm Settlement depends on the Payment Orchestration capability.
- Confirm Settlement mentions Settlement Officer.
- Confirm Settlement mentions Settlement File.

## Details
The Settlement Officer captures settlement advices. Inputs are the Settlement File; outputs are a confirmed settlement. The Settlement Received Event triggers this step. Controls include a settlement finality check and dual control.

## References
- [Fedwire Funds Service](https://fedwireservice.org/)
- [FedNow / RTP settlement solutions](https://bankersbank.com/solutions/fednow-rtp-settlement-solutions/)
