---
id: tax-loss-harvesting-service
title: Tax-Loss Harvesting Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["TLH Service", "Tax-Aware Rebalancing", "Loss Harvesting Engine"]
status: draft
sources: ["https://www.envestnet.com/wealth-management/unified-managed-accounts", "https://www.envestnet.com/wealth-management/unified-managed-accounts/pros-and-cons", "https://www.limina.com/solutions/portfolio-modelling-and-portfolio-tracking-software"]
---

# Tax-Loss Harvesting Service

**Definition.** Tax-Loss Harvesting Service is the technology capability that identifies positions trading below cost basis and proposes loss-realising trades, with wash-sale and replacement-security constraints, during rebalancing to improve after-tax returns in managed accounts.
**Also known as:** TLH Service, Tax-Aware Rebalancing, Loss Harvesting Engine.

## Relationships
- Tax-Loss Harvesting Service is defined in the Core Processing domain.
- Tax-Loss Harvesting Service is derived from Rebalancing Engine.
- Tax-Loss Harvesting Service is related to Portfolio Management.

## Details
Tax-Loss Harvesting Service scans tax lots for unrealised losses, then proposes selling losing positions to realise capital losses that offset gains, while substituting a correlated replacement security to maintain market exposure. It enforces wash-sale rules (the 30-day window in the US) to keep harvested losses deductible and operates as a tax-aware overlay during the rebalancing run. Platforms such as Envestnet realize automated TLH across unified managed accounts, weighing the after-tax benefit against transaction cost and tracking-error drift.

## References
- [Envestnet Unified Managed Accounts](https://www.envestnet.com/wealth-management/unified-managed-accounts)
- [Envestnet UMA Pros and Cons](https://www.envestnet.com/wealth-management/unified-managed-accounts/pros-and-cons)
- [Limina Portfolio Modelling](https://www.limina.com/solutions/portfolio-modelling-and-portfolio-tracking-software)
