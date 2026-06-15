---
id: settlement-file
title: Settlement File
type: artifact
domain: Payments
aliases: ["Settlement Advice", "Settlement Report"]
status: draft
sources: ["https://fedwireservice.org/"]
---

# Settlement File

**Definition.** Settlement File is the operator or correspondent file or advice that evidences interbank settlement. Settlement File is the artifact consumed when confirming settlement in reconciliation and settlement.

**Also known as:** Settlement Advice, Settlement Report.

## Relationships
- Settlement File is related to the Payments domain.
- Settlement File mentions Confirm Settlement.
- Settlement File mentions Reconciliation & Settlement.
- Settlement File is related to Settlement Confirmation.
- Settlement File is related to Interbank Settlement.

## Details
Settlement File arrives from a clearing operator or correspondent bank to evidence that interbank money movement has reached finality. The artifact is captured by the settlement role under dual control during the Confirm Settlement step and underpins downstream statement ingestion, matching and adjustment activities.

## References
- https://fedwireservice.org/
