---
id: drift-monitoring-service
title: Drift Monitoring Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Model Drift Monitor", "Tolerance Band Service", "Rebalance Trigger Service"]
status: draft
sources: ["https://meradia.com/thought-leadership/process-based-attribution-getting-to-the-heart-of-value-add/", "https://www.ortecfinance.com/-/media/project/ortec/shared/files/whitepapers/ip-multi-period-performance-attribution-ortec-finance_bas-leerink.pdf"]
---

# Drift Monitoring Service

**Definition.** Drift Monitoring Service tracks how account holdings drift from target model weights and raises rebalance triggers when allocations breach configured tolerance bands.
**Also known as:** Model Drift Monitor, Tolerance Band Service, Rebalance Trigger Service.

## Relationships
- Drift Monitoring Service is defined in the Core Processing domain.
- Drift Monitoring Service is derived from Model Portfolio Manager.
- Drift Monitoring Service is related to Rebalancing Engine.

## Details
Drift Monitoring Service compares each managed account's current holdings against its assigned model portfolio and measures drift at the position, asset-class and sleeve level. It evaluates absolute tolerance bands (for example plus or minus 5% around a target weight) and relative bands, and when a holding moves outside its band it flags the account as out-of-tolerance and emits a rebalance trigger. This continuous monitoring lets a manager rebalance only the accounts that have actually drifted rather than the whole book. The triggered rebalance is executed by Rebalancing Engine.

## References
- [Process-based attribution (Meradia)](https://meradia.com/thought-leadership/process-based-attribution-getting-to-the-heart-of-value-add/)
- [Multi-period performance attribution (Ortec Finance)](https://www.ortecfinance.com/-/media/project/ortec/shared/files/whitepapers/ip-multi-period-performance-attribution-ortec-finance_bas-leerink.pdf)
