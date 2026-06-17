---
id: collateral-release
title: Collateral Release
type: business-capability
domain: Lending & Credit
level: L3
aliases: ["Security Discharge", "Lien Release"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.law.cornell.edu/ucc/9"]
---

# Collateral Release

**Definition.** Collateral Release is the capability that discharges security interests and returns pledged assets once obligations are met, mapping to the BIAN Collateral Asset Administration service domain.
**Also known as:** Security Discharge, Lien Release.

## Relationships
- Collateral Release is defined in the Lending & Credit domain.
- Collateral Release is derived from Collateral Management.
- Collateral Release depends on the Document Management capability.
- Collateral Release depends on the Core Banking Processing capability.

## Details
The BIAN Collateral Asset Administration service domain closes out the security interest when the underlying debt is satisfied, which Collateral Release executes. A concrete banking specific: once a UCC-secured loan is repaid, the bank files a UCC-3 termination statement to release the lien, and for mortgages records a release/satisfaction so the borrower's clear title is restored.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [UCC Article 9 Secured Transactions](https://www.law.cornell.edu/ucc/9)
