---
id: intraday-liquidity-management
title: Intraday Liquidity Management
type: business-capability
domain: Finance & Treasury
level: L3
aliases: ["Intraday Funding Management", "Intraday Cash Management", "Throughput Management"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d248.htm", "https://bian.org/servicelandscape/"]
---

# Intraday Liquidity Management

**Definition.** Intraday Liquidity Management actively manages payment timing, throughput and intraday funding to meet settlement obligations as they fall due, the treasury operating counterpart to the Risk-domain Intraday Liquidity Monitoring capability.
**Also known as:** Intraday Funding Management, Intraday Cash Management, Throughput Management.

## Relationships
- Intraday Liquidity Management is defined in the Finance & Treasury domain.
- Intraday Liquidity Management is derived from Liquidity Management.
- Intraday Liquidity Management depends on the Treasury Management System capability.

## Details
Intraday Liquidity Management sequences and throttles outgoing payments against available intraday liquidity (opening balances, incoming receipts and central-bank credit lines) so the bank settles RTGS and CLS obligations on time without holding excess buffers. It operationalises the BCBS d248 monitoring tools — daily maximum intraday liquidity usage, available intraday liquidity at start of day, total payments, and time-specific obligations — turning those measures into active throughput controls and queue management.

## References
- [BCBS Monitoring tools for intraday liquidity management (d248)](https://www.bis.org/bcbs/publ/d248.htm)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
