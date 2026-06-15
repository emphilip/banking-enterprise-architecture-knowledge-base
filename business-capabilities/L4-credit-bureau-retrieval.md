---
id: credit-bureau-retrieval
title: Credit Bureau Retrieval
type: business-capability
domain: Lending & Credit
level: L4
aliases: ["Bureau Pull", "Credit Reference Retrieval"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act"]
---

# Credit Bureau Retrieval

**Definition.** Credit Bureau Retrieval is the capability that requests and consolidates external credit bureau and reference data, mapping to the BIAN Customer Credit Rating service domain.
**Also known as:** Bureau Pull, Credit Reference Retrieval.

## Relationships
- Credit Bureau Retrieval is defined in the Lending & Credit domain.
- Credit Bureau Retrieval is derived from Affordability Assessment.
- Credit Bureau Retrieval depends on the Credit Decisioning Engine capability.
- Credit Bureau Retrieval depends on the Analytics Platform capability.

## Details
The BIAN Customer Credit Rating service domain ingests external reference data through Credit Bureau Retrieval to inform the credit view. A concrete banking specific: in the US a credit report is pulled from one or more of Equifax, Experian and TransUnion under a permissible purpose required by the Fair Credit Reporting Act (FCRA), and a hard inquiry is recorded on the consumer's file.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Fair Credit Reporting Act (FCRA)](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act)
