---
id: settle-trade-payment
title: Settle Trade Payment
type: process-step
process: Trade Finance Processing
order: 6
aliases: ["Honor Presentation", "Trade Settlement Step"]
status: draft
sources: ["https://www.dripcapital.com/resources/blog/letter-of-credit-lc", "https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/trade-finance-services/pub-ch-trade-finance.pdf"]
---

# Settle Trade Payment

**Definition.** Settle Trade Payment honors compliant documents and settles payment, or refuses and notifies on discrepancies.
**Also known as:** Honor Presentation, Trade Settlement Step.

## Relationships
- Settle Trade Payment is defined in the Trade Finance Processing process.
- Settle Trade Payment depends on the Core Banking Processing capability.
- Settle Trade Payment mentions Trade Finance Officer.

## Details
The Trade Finance Officer settles or refuses. Inputs are the examination result; outputs are a trade settlement. Controls include the honor/refuse decision, four-eyes on payment and AML on settlement. This terminal step emits the Trade Settlement Event.

## References
- [Drip Capital: letter of credit](https://www.dripcapital.com/resources/blog/letter-of-credit-lc)
- [OCC: trade finance services handbook](https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/trade-finance-services/pub-ch-trade-finance.pdf)
