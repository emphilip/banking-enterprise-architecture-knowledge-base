---
id: atm-cash-forecasting
title: ATM Cash Forecasting
type: business-capability
domain: Channels & Engagement
level: L4
aliases: ["Cash Demand Forecasting", "Replenishment Optimisation"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://us.brinks.com/branch-services"]
---

# ATM Cash Forecasting

**Definition.** ATM Cash Forecasting is the Channels & Engagement capability that predicts per-device demand to optimise replenishment cycles and minimise cash holding costs, an analytics-driven extension supporting the BIAN ATM Network Operations service domain.
**Also known as:** Cash Demand Forecasting, Replenishment Optimisation.

## Relationships
- ATM Cash Forecasting is defined in the Channels & Engagement domain.
- ATM Cash Forecasting is derived from ATM Cash Management.
- ATM Cash Forecasting depends on the Analytics Platform capability.

## Details
ATM Cash Forecasting supports BIAN ATM Network Operations with per-device, per-denomination demand models built on historical dispense, calendar effects (paydays, weekends, public holidays) and local events. The objective minimises the carrying cost of insured idle cash and the interest forgone against the service cost of a dispense failure (cassette stock-out) and extra CIT visits. Time-series and machine-learning models (gradient boosting, Prophet-style) recommend replenishment amount and timing per terminal, which then drives Cash-in-Transit Coordination scheduling. Forecast accuracy and cash-out incidents are the governing KPIs, with safety stock tuned per site risk.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Brinks Branch Services](https://us.brinks.com/branch-services)
- [APQC Process Frameworks](https://www.apqc.org/process-frameworks)
