---
id: tiered-interest-calculator
title: Tiered Interest Calculator
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Tiered Rate Calculator", "Banded Interest Service", "Bonus Rate Engine"]
status: draft
sources: ["https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products", "https://www.alogent.com/banking-definitions/core-banking-systems"]
---

# Tiered Interest Calculator

**Definition.** Tiered Interest Calculator is the technology capability that computes interest under tiered, banded and bonus-rate structures, applying balance-tier rules, promotional or bonus conditions and day-count conventions to deposit balances.
**Also known as:** Tiered Rate Calculator, Banded Interest Service, Bonus Rate Engine.

## Relationships
- Tiered Interest Calculator is defined in the Core Processing domain.
- Tiered Interest Calculator is derived from Interest & Charges Engine.
- Tiered Interest Calculator is related to Interest Calculation.

## Details
Tiered Interest Calculator selects the applicable rate by balance band and applies promotional or bonus conditions with the correct day-count convention. Core-banking data-model references describe tiered pricing and rate tables as configurable product attributes, and core-system component definitions treat interest computation as a parameterised engine, which this service specialises for tiered, banded and bonus deposit rates.

## References
- [Core banking data model, ledger and products](https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products)
- [Alogent core banking systems definitions](https://www.alogent.com/banking-definitions/core-banking-systems)
