---
id: bulk-payment-origination
title: Bulk Payment Origination
type: business-capability
domain: Payments
level: L3
aliases: ["Batch Payments", "File-Based Payments", "Bulk Disbursement"]
status: draft
sources: ["https://achdevguide.nacha.org/how-ach-works", "https://deepwiki.com/bian-official/public/5.1-payment-operations"]
---

# Bulk Payment Origination

**Definition.** Bulk Payment Origination ingests and disaggregates batched payment files (e.g. payroll and supplier runs) into individual instructions, mapping to the BIAN Bulk Payments service domain and Nacha batch entry types such as PPD and CCD.
**Also known as:** Batch Payments, File-Based Payments, Bulk Disbursement.

## Relationships
- Bulk Payment Origination is defined in the Payments domain.
- Bulk Payment Origination is derived from Payment Initiation.
- Bulk Payment Origination depends on the Payment Orchestration capability.

## Details
Bulk Payment Origination grounds in the BIAN Bulk Payments service domain. It ingests batched files such as payroll and supplier runs and disaggregates them into individual instructions, aligning to Nacha batch entry types like PPD and CCD. It feeds validated entries into downstream execution.

## References
- [Nacha ACH Developer Guide](https://achdevguide.nacha.org/how-ach-works)
- [BIAN Payment Operations](https://deepwiki.com/bian-official/public/5.1-payment-operations)
