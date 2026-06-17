---
id: average-price-book-service
title: Average Price Book Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Average Pricing Service", "Block Average Price Engine", "Fill Aggregation Service"]
status: draft
sources: ["https://tradingtechnologies.com/trading/oms/", "https://www.crd.com/solutions/charles-river-trader"]
---

# Average Price Book Service

**Definition.** Average Price Book Service aggregates multiple fills of a block order into an average price and allocates the resulting positions across participating accounts.
**Also known as:** Average Pricing Service, Block Average Price Engine, Fill Aggregation Service.

## Relationships
- Average Price Book Service is defined in the Core Processing domain.
- Average Price Book Service is derived from Trade Allocation Engine.

## Details
Average Price Book Service collects the partial fills of a block order, each at its own execution price, and computes the volume-weighted average price for the block. It then allocates the filled quantity to the participating client accounts pro rata to their order share at that single average price, so every account in the block receives identical execution pricing — a fairness requirement for aggregated orders. Order management systems such as Charles River and Trading Technologies hold the average-price book until the block is fully filled, then post the allocations to each account.

## References
- [Trading Technologies OMS](https://tradingtechnologies.com/trading/oms/)
- [Charles River Trader](https://www.crd.com/solutions/charles-river-trader)
