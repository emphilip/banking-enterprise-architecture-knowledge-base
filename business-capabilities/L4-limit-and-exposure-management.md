---
id: limit-and-exposure-management
title: Limit & Exposure Management
type: business-capability
domain: Risk Management
level: L4
aliases: ["Credit Limit Management", "Limit Monitoring", "Concentration Limit Control"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.bis.org/bcbs/publ/d283.htm"]
---

# Limit & Exposure Management

**Definition.** Limit & Exposure Management defines, allocates and monitors counterparty, country, sector and product limits, flagging breaches and excesses, supported by the BIAN Limit and Exposure Management service domain.
**Also known as:** Credit Limit Management, Limit Monitoring, Concentration Limit Control.

## Relationships
- Limit & Exposure Management is defined in the Risk Management domain.
- Limit & Exposure Management is derived from Credit Exposure Management.
- Limit & Exposure Management depends on the Risk Analytics Engine capability.
- Limit & Exposure Management depends on the Risk Data Aggregation capability.

## Details
Limit & Exposure Management cascades the risk appetite into a hierarchy of hard and soft limits — single-counterparty, group, country, sector, tenor and product — and checks utilisation pre-deal and intraday. It enforces the Basel Large Exposures Framework (BCBS d283) cap of 25% of Tier 1 capital to a single counterparty or connected group (15% for G-SIB-to-G-SIB), manages temporary excess approvals, and escalates breaches through a defined governance workflow with an audit trail.

## References
- [BCBS Supervisory Framework for Measuring and Controlling Large Exposures (d283)](https://www.bis.org/bcbs/publ/d283.htm)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
