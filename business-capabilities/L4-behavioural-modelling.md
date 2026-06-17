---
id: behavioural-modelling
title: Behavioural Modelling
type: business-capability
domain: Finance & Treasury
level: L4
aliases: ["NMD Modelling", "Prepayment Modelling", "Behavioural Assumptions"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d368.htm", "https://www.afme.eu/media/t5tehhpr/afmeirrbbfinal.pdf"]
---

# Behavioural Modelling

**Definition.** Behavioural Modelling estimates non-maturity deposit, prepayment and early-redemption behaviour used in IRRBB and ALM cash-flow modelling.
**Also known as:** NMD Modelling, Prepayment Modelling, Behavioural Assumptions.

## Relationships
- Behavioural Modelling is defined in the Finance & Treasury domain.
- Behavioural Modelling is derived from Interest Rate Risk In The Banking Book.
- Behavioural Modelling depends on the Asset Liability Management Engine capability.

## Details
Behavioural Modelling converts contractually open-ended or optionable products into modelled cash-flow profiles: it splits non-maturity deposits (NMDs) into stable "core" and rate-sensitive "non-core" balances with assumed repricing/run-off, and estimates loan prepayment and term-deposit early-withdrawal rates. BCBS d368 caps the average behavioural life of NMDs (e.g. retail/transactional limits) and requires assumptions be documented and back-tested. These assumptions are the single largest driver of EVE and NII results, so the capability calibrates and validates them against observed history.

## References
- [Interest rate risk in the banking book (BCBS d368)](https://www.bis.org/bcbs/publ/d368.htm)
- [AFME IRRBB paper](https://www.afme.eu/media/t5tehhpr/afmeirrbbfinal.pdf)
