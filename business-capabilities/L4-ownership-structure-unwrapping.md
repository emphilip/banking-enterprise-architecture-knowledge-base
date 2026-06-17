---
id: ownership-structure-unwrapping
title: Ownership Structure Unwrapping
type: business-capability
domain: Compliance & Financial Crime
level: L4
aliases: ["Layered Ownership Analysis", "UBO Unwrapping"]
status: draft
sources: ["https://www.fatf-gafi.org/en/topics/beneficial-ownership.html", "https://www.fincen.gov/boi"]
---

# Ownership Structure Unwrapping

**Definition.** Ownership Structure Unwrapping traces layered legal-entity structures to the ultimate natural-person owners, supporting FATF Recommendations 24/25 and EU AMLD6 beneficial-ownership obligations.
**Also known as:** Layered Ownership Analysis, UBO Unwrapping.

## Relationships
- Ownership Structure Unwrapping is defined in the Compliance & Financial Crime domain.
- Ownership Structure Unwrapping is derived from Beneficial Ownership Identification.
- Ownership Structure Unwrapping depends on the Analytics Platform capability.
- Ownership Structure Unwrapping depends on the Data Governance capability.

## Details
FATF R.24/R.25 require firms to look through complex multi-layer corporate and trust structures to the beneficial owner, calculating indirect ownership multiplicatively across the chain. Under the FinCEN ownership prong, any natural person whose aggregated direct and indirect holdings reach 25% is a beneficial owner, so unwrapping must compute cumulative stakes through intermediary entities and flag structures designed to obscure control (e.g. nominee shareholders, bearer shares). The output feeds UBO records and control-person identification.

## References
- [FATF beneficial ownership](https://www.fatf-gafi.org/en/topics/beneficial-ownership.html)
- [FinCEN Beneficial Ownership Information](https://www.fincen.gov/boi)
