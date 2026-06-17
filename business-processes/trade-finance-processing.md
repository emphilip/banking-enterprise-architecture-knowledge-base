---
id: trade-finance-processing
title: Trade Finance Processing
type: business-process
domain: Lending & Credit
aliases: ["Trade Finance"]
status: draft
---

# Trade Finance Processing

**Definition.** Trade Finance Processing is the process of administering trade finance instruments such as letters of credit, guarantees, and documentary collections, including issuance, document examination, and settlement.
**Also known as:** Trade Finance.

## Relationships
- Trade Finance Processing is defined in the Lending & Credit domain.
- Trade Finance Processing depends on the Collateral Management capability.

## Details
Trade Finance Processing captures the trade instrument request, assesses limits and collateral, issues the instrument, examines presented documents for compliance, and settles obligations. Actors include trade finance officers, corporate clients, and correspondent banks. Systems involved include trade finance platforms, collateral and security services, and document processing.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)

## Flow
- Receive Credit Application causes Assess Trade Limit.
- Assess Trade Limit causes Issue Letter Of Credit.
- Issue Letter Of Credit causes Advise Beneficiary.
- Advise Beneficiary causes Examine Trade Documents.
- Examine Trade Documents causes Settle Trade Payment.
