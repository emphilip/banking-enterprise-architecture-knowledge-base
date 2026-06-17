---
id: fx-exposure-aggregation-service
title: FX Exposure Aggregation Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["FX Exposure Engine", "Currency Exposure Aggregator", "Net FX Position Service"]
status: draft
sources: ["https://www.highradius.com/resources/Blog/what-is-treasury-management-system/", "https://www.bamboodt.com/building-a-modern-treasury-management-system-architecture-features-and-implementation-best-practices/"]
---

# FX Exposure Aggregation Service

**Definition.** FX Exposure Aggregation Service consolidates foreign-exchange exposures across entities, currencies and instruments to net positions for hedging decisions and limit monitoring.
**Also known as:** FX Exposure Engine, Currency Exposure Aggregator, Net FX Position Service.

## Relationships
- FX Exposure Aggregation Service is defined in the Core Processing domain.
- FX Exposure Aggregation Service is derived from Treasury Risk Management Service.

## Details
FX Exposure Aggregation Service collects currency exposures from receivables, payables, forecast cash flows, deposits, loans and derivative positions across legal entities, then nets long and short positions by currency pair to produce a single net open position per currency. The netted view drives hedge sizing, hedge-ratio policy and limit checks against per-currency and aggregate exposure limits. Treasury management system designs centralise this aggregation so the dealing desk hedges the residual group exposure rather than gross positions held in each subsidiary.

## References
- [What is a treasury management system (HighRadius)](https://www.highradius.com/resources/Blog/what-is-treasury-management-system/)
- [Modern treasury management system architecture (BambooDT)](https://www.bamboodt.com/building-a-modern-treasury-management-system-architecture-features-and-implementation-best-practices/)
