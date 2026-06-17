---
id: cost-basis-tracking
title: Cost Basis Tracking
type: business-capability
domain: Wealth & Investments
level: L4
aliases: ["Tax Lot Accounting", "Basis Reporting"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.irs.gov/publications/p550"]
---

# Cost Basis Tracking

**Definition.** Cost Basis Tracking maintains tax lots and cost basis across acquisitions, disposals, and corporate actions for tax reporting; it supports the BIAN Securities Position Keeping service domain.
**Also known as:** Tax Lot Accounting, Basis Reporting.

## Relationships
- Cost Basis Tracking is defined in the Wealth & Investments domain.
- Cost Basis Tracking is derived from Portfolio Accounting.
- Cost Basis Tracking depends on the Portfolio Management System capability.
- Cost Basis Tracking depends on the Core Banking Processing capability.

## Details
Cost Basis Tracking maintains per-lot acquisition cost and date and applies a disposal method (FIFO, specific identification, or average cost) to compute realised gain or loss and its short- or long-term character. US broker-dealers must report adjusted basis for covered securities to clients and the IRS on Form 1099-B, so the capability also applies wash-sale and corporate-action basis adjustments feeding the BIAN Securities Position Keeping service domain.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [IRS Publication 550 — Investment Income and Expenses](https://www.irs.gov/publications/p550)
