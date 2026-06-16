---
id: trader
title: Trader
type: role
domain: Wealth & Investments
aliases: ["Dealer", "Execution Trader"]
status: draft
sources: ["https://www.crd.com/solutions/charles-river-trader", "https://www.magmio.com/news/160-trade-execution"]
---

# Trader

**Definition.** Trader is the dealing role that validates, routes and executes securities orders on best terms in the order and execution management system, capturing fills for downstream allocation and settlement in the wealth flow.

**Also known as:** Dealer, Execution Trader.

## Relationships
- Trader is related to the Wealth & Investments domain.
- Trader mentions Trade Order Management.
- Trader mentions Execute Order.

## Details
Trader captures the Order Ticket into the OMS with instrument, side, quantity and constraints, then validates the order and runs pre-trade compliance against mandate, limits and restricted lists. Trader routes the validated order to the chosen venue or broker for best execution, monitors venue selection and execution quality, and executes the order, capturing full or partial fills. Trader confirms executed fills with the counterparty or broker and issues the Trade Confirmation, observing best-execution and trade-affirmation controls. Trader works within the front office and hands off to settlement operations for allocation and T+1 settlement.

## References
- https://www.crd.com/solutions/charles-river-trader
- https://www.magmio.com/news/160-trade-execution
