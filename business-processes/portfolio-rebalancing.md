---
id: portfolio-rebalancing
title: Portfolio Rebalancing
type: business-process
domain: Wealth & Investments
aliases: ["Rebalancing", "Drift Management"]
status: draft
sources: ["https://www.financialplanningassociation.org/sites/default/files/2020-05/9%20Opportunistic%20Rebalancing%20A%20New%20Paradigm%20for%20Wealth%20Managers.pdf", "https://www.investipal.co/blog/how-to-automate-portfolio-rebalancing-tools-strategies-and-compliance-considerations/", "https://investor.vanguard.com/investor-resources-education/portfolio-management/rebalancing-your-portfolio"]
---

# Portfolio Rebalancing

**Definition.** Portfolio Rebalancing is the periodic or triggered process that detects drift of holdings from the Investment Policy Statement target allocation, generates a compliant rebalance proposal, pre-trade compliance-checks it against mandate limits, approves it and raises orders to restore the target.
**Also known as:** Rebalancing, Drift Management.

## Relationships
- Portfolio Rebalancing is defined in the Wealth & Investments domain.
- Portfolio Rebalancing depends on the Portfolio Management capability.

## Details
Portfolio Rebalancing measures drift against the Investment Policy Statement targets, generates a buy/sell proposal mindful of tax lots and costs, runs pre-trade compliance against mandate and IPS limits, obtains four-eyes approval, and raises Order Tickets into trading. Controls include drift tolerance bands, pre-trade compliance, four-eyes approval, and tax-lot/wash-sale checks. Actors include the Portfolio Manager.

## Flow
- Measure Portfolio Drift causes Evaluate Drift Threshold.
- Evaluate Drift Threshold causes Generate Rebalance Proposal.
- Generate Rebalance Proposal causes Run Pre-Trade Compliance.
- Run Pre-Trade Compliance causes Approve Rebalance Plan.
- Approve Rebalance Plan causes Raise Rebalance Orders.

## References
- [Opportunistic Rebalancing for Wealth Managers](https://www.financialplanningassociation.org/sites/default/files/2020-05/9%20Opportunistic%20Rebalancing%20A%20New%20Paradigm%20for%20Wealth%20Managers.pdf)
- [Automating portfolio rebalancing and compliance](https://www.investipal.co/blog/how-to-automate-portfolio-rebalancing-tools-strategies-and-compliance-considerations/)
