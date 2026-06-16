---
id: rebalancing-engine
title: Rebalancing Engine
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Portfolio Rebalancer", "Drift Management Engine", "Model Rebalancing Service"]
status: draft
sources: ["https://www.limina.com/solutions/portfolio-modelling-and-portfolio-tracking-software", "https://www.envestnet.com/wealth-management/unified-managed-accounts", "https://professional.bloomberg.com/solutions/buy-side/"]
---

# Rebalancing Engine

**Definition.** Rebalancing Engine is the technology capability that detects portfolio drift against target allocations or models, computes the buy and sell trades needed to realign accounts, and supports cash-flow rebalancing and managed-account (SMA/UMA) automation across many accounts.
**Also known as:** Portfolio Rebalancer, Drift Management Engine, Model Rebalancing Service.

## Relationships
- Rebalancing Engine is defined in the Core Processing domain.
- Rebalancing Engine is derived from Portfolio Management System.
- Rebalancing Engine depends on Model Portfolio Manager.
- Rebalancing Engine is related to Portfolio Management.

## Details
Rebalancing Engine measures the drift between current holdings and target weights set by the Model Portfolio Manager, then generates orders to bring accounts back within tolerance bands. It handles cash-flow rebalancing (deposits and withdrawals), trade-to-target and trade-to-band strategies, and scales across thousands of managed accounts in SMA and UMA programmes. Platforms such as Envestnet, Bloomberg buy-side and Limina realize batch and on-demand rebalancing, often layering tax-aware constraints (wash-sale, replacement securities) so realignment improves after-tax outcomes for managed accounts.

## References
- [Limina Portfolio Modelling](https://www.limina.com/solutions/portfolio-modelling-and-portfolio-tracking-software)
- [Envestnet Unified Managed Accounts](https://www.envestnet.com/wealth-management/unified-managed-accounts)
- [Bloomberg Buy-Side](https://professional.bloomberg.com/solutions/buy-side/)
