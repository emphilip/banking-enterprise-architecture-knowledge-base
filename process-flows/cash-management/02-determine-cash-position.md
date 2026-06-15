---
id: determine-cash-position
title: Determine Cash Position
type: process-step
process: Cash Management
order: 2
aliases: ["Position Calculation", "Cash Positioning Step"]
status: draft
sources: ["https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/", "https://www.jpmorgan.com/payments/solutions/treasury/liquidity"]
---

# Determine Cash Position

**Definition.** Determine Cash Position computes the consolidated cash position by account, currency and value date.
**Also known as:** Position Calculation, Cash Positioning Step.

## Relationships
- Determine Cash Position is defined in the Cash Management process.
- Determine Cash Position causes Forecast Cash Flow.
- Determine Cash Position depends on the Core Banking Processing capability.
- Determine Cash Position mentions Treasury Cash Manager.

## Details
The Treasury Cash Manager computes the consolidated position. Inputs are aggregated balances; outputs are the cash position. The Cut-Off Reached Event marks the value-date boundary. Controls include position sign-off and intraday limit checks.

## References
- [Kyriba cash and liquidity management](https://www.kyriba.com/resource/what-is-cash-and-liquidity-management/)
- [J.P. Morgan liquidity](https://www.jpmorgan.com/payments/solutions/treasury/liquidity)
