---
id: tolerance-band-monitoring
title: Tolerance Band Monitoring
type: business-capability
domain: Wealth & Investments
level: L4
aliases: ["Drift Monitoring", "Rebalance Trigger"]
status: draft
sources: ["https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/overview-asset-allocation", "https://bian.org/servicelandscape/"]
---

# Tolerance Band Monitoring

**Definition.** Tolerance Band Monitoring tracks allocation drift against rebalancing thresholds and flags portfolios for action; it supports the BIAN Investment Portfolio Management service domain.
**Also known as:** Drift Monitoring, Rebalance Trigger.

## Relationships
- Tolerance Band Monitoring is defined in the Wealth & Investments domain.
- Tolerance Band Monitoring is derived from Portfolio Rebalancing Management.
- Tolerance Band Monitoring depends on the Portfolio Management System capability.
- Tolerance Band Monitoring depends on the Analytics Platform capability.

## Details
Per CFA Institute practice, percentage-of-portfolio rebalancing defines corridors around each asset class's strategic target (for example +/- 5%); a breach triggers rebalancing. Tolerance Band Monitoring evaluates current weights against these corridors on each pricing cycle, considering wider bands for less liquid or more volatile classes to balance tracking error against transaction costs, and raises rebalance triggers into the BIAN Investment Portfolio Management service domain.

## References
- [CFA Institute — Overview of Asset Allocation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/overview-asset-allocation)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
