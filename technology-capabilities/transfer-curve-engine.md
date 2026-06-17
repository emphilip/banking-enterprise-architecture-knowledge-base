---
id: transfer-curve-engine
title: Transfer Curve Engine
type: technology-capability
domain: Core Processing
level: L3
aliases: ["FTP Curve Engine", "Matched-Maturity Curve Service", "Transfer Rate Curve Builder"]
status: draft
sources: ["https://docs.oracle.com/cd/E26401_01/doc.122/e48860/T427784T427787.htm", "https://www.fermacrisk.com/alm-structural-risk"]
---

# Transfer Curve Engine

**Definition.** Transfer Curve Engine constructs and maintains the matched-maturity transfer-pricing curves, base curves and liquidity premia used to assign transfer rates to assets and liabilities.
**Also known as:** FTP Curve Engine, Matched-Maturity Curve Service, Transfer Rate Curve Builder.

## Relationships
- Transfer Curve Engine is defined in the Core Processing domain.
- Transfer Curve Engine is derived from Funds Transfer Pricing Engine.

## Details
Transfer Curve Engine builds the term-structure curves that the matched-maturity FTP method uses to charge funding and credit earnings. It maintains a base interest curve and adds a liquidity premium term-liquidity-premium (TLP) curve, then derives the transfer rate for each instrument from the point on the curve corresponding to its repricing or maturity tenor, so a five-year fixed loan is priced off the five-year transfer rate. Oracle FTP documentation describes this matched-maturity assignment, which isolates the interest-rate component into Treasury and leaves business lines with a clean credit and deposit spread.

## References
- [Oracle funds transfer pricing methodologies](https://docs.oracle.com/cd/E26401_01/doc.122/e48860/T427784T427787.htm)
- [ALM and structural interest rate risk (Ferma Risk)](https://www.fermacrisk.com/alm-structural-risk)
