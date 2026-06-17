---
id: rebalance-triggered-event
title: Rebalance Triggered Event
type: event
domain: Wealth & Investments
aliases: ["Drift Breach Event", "Rebalance Trigger Event"]
status: draft
sources: ["https://datafi.co/blog/client-portfolio-rebalancing-triggers/", "https://investor.vanguard.com/investor-resources-education/portfolio-management/rebalancing-your-portfolio"]
---

# Rebalance Triggered Event

**Definition.** Rebalance Triggered Event is the business event raised when measured portfolio drift breaches the Investment Policy Statement tolerance bands, triggering the rebalancing process in the wealth flow.

**Also known as:** Drift Breach Event, Rebalance Trigger Event.

## Relationships
- Rebalance Triggered Event is related to the Wealth & Investments domain.
- Rebalance Triggered Event mentions Portfolio Rebalancing.
- Rebalance Triggered Event causes Generate Rebalance Proposal.

## Details
Rebalance Triggered Event fires when drift of current holdings from the Investment Policy Statement target allocation exceeds a tolerance band, whether detected on a periodic schedule or by a market-driven threshold breach. Rebalance Triggered Event carries the portfolio identifier, the breached asset-class weights versus targets, the measured drift magnitude and the trigger timestamp. Rebalance Triggered Event initiates generation of a compliant rebalance proposal of buys and sells to restore the targets, considering tax lots and costs. The event is consumed by portfolio management to begin pre-trade compliance and four-eyes approval before orders are raised into trading.

## References
- https://datafi.co/blog/client-portfolio-rebalancing-triggers/
- https://investor.vanguard.com/investor-resources-education/portfolio-management/rebalancing-your-portfolio
