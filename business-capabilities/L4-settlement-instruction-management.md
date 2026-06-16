---
id: settlement-instruction-management
title: Settlement Instruction Management
type: business-capability
domain: Wealth & Investments
level: L4
aliases: ["SSI Management", "Settlement Messaging"]
status: draft
sources: ["https://www.dtcc.com/-/media/Files/PDFs/T2/Accelerating-the-US-Securities-Settlement-Cycle-to-T1-December-1-2021.pdf", "https://bian.org/servicelandscape/"]
---

# Settlement Instruction Management

**Definition.** Settlement Instruction Management creates, enriches, and transmits standing and trade settlement instructions to custodians and CSDs; it supports the BIAN Securities Fulfillment service domain.
**Also known as:** SSI Management, Settlement Messaging.

## Relationships
- Settlement Instruction Management is defined in the Wealth & Investments domain.
- Settlement Instruction Management is derived from Trade Settlement.
- Settlement Instruction Management depends on the Order Management System capability.
- Settlement Instruction Management depends on the Core Banking Processing capability.

## Details
Settlement Instruction Management maintains standing settlement instructions (SSIs) — the account, custodian, and place-of-settlement data per counterparty and security type — and enriches each affirmed trade with them before sending delivery-versus-payment instructions to the custodian or CSD via SWIFT (ISO 15022/20022). Clean, automated SSIs are critical to settling within the DTCC T+1 cycle and avoiding fails, supporting the BIAN Securities Fulfillment service domain.

## References
- [DTCC — Accelerating the US Securities Settlement Cycle to T+1](https://www.dtcc.com/-/media/Files/PDFs/T2/Accelerating-the-US-Securities-Settlement-Cycle-to-T1-December-1-2021.pdf)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
