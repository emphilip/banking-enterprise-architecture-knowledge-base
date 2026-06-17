---
id: credit-exposure-management
title: Credit Exposure Management
type: business-capability
domain: Risk Management
level: L3
aliases: ["Counterparty Exposure Management", "EAD Measurement"]
status: draft
sources: ["https://www.bis.org/basel_framework/chapter/CRE/52.htm", "https://bian.org/servicelandscape/"]
---

# Credit Exposure Management

**Definition.** Credit Exposure Management measures, aggregates and monitors current and potential credit exposure across counterparties, including derivative exposure under SA-CCR, supported by the BIAN Position Keeping service domain.
**Also known as:** Counterparty Exposure Management, EAD Measurement.

## Relationships
- Credit Exposure Management is defined in the Risk Management domain.
- Credit Exposure Management is derived from Credit Risk Management.
- Credit Exposure Management depends on the Risk Analytics Engine capability.
- Credit Exposure Management depends on the Risk Data Aggregation capability.

## Details
Credit Exposure Management computes exposure at default for on- and off-balance-sheet items, applying credit conversion factors to undrawn commitments and the Basel SA-CCR formula (CRE52) for derivative EAD: EAD = 1.4 × (replacement cost + potential future exposure). It aggregates gross and net exposure by counterparty, group, country and sector to support limit monitoring and concentration analysis, reconciling exposure figures to the position-keeping ledger.

## References
- [Basel Framework CRE52 (SA-CCR)](https://www.bis.org/basel_framework/chapter/CRE/52.htm)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
