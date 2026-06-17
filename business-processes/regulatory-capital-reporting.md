---
id: regulatory-capital-reporting
title: Regulatory Capital Reporting
type: business-process
domain: Finance & Treasury
aliases: ["Prudential Reporting", "COREP Reporting", "CCAR Reporting"]
status: draft
sources: ["https://www.regnology.net/en/resources/regulatory-topics/common-reporting-corep/", "https://regreportingdesk.com/corep-reporting-explained/", "https://www.federalreserve.gov/publications/comprehensive-capital-analysis-and-review-summary-instructions-2020.htm"]
---

# Regulatory Capital Reporting

**Definition.** Regulatory Capital Reporting is the prudential reporting process that sources finance and risk data, calculates risk-weighted assets and own funds, assembles capital-adequacy returns (COREP/FINREP, FR Y-9C/FR Y-14), validates against the regulator taxonomy and submits with board attestation under CCAR.
**Also known as:** Prudential Reporting, COREP Reporting, CCAR Reporting.

## Relationships
- Regulatory Capital Reporting is defined in the Finance & Treasury domain.
- Regulatory Capital Reporting depends on the Regulatory Capital Management capability.

## Details
Regulatory Capital Reporting is run by the Regulatory Reporting Specialist. Inputs are general-ledger data, credit/market/operational risk exposures and own-funds data; outputs are risk-weighted assets, the Capital Adequacy Return and the regulatory submission. Controls include data-quality reconciliation, RWA calculation governance, COREP/FINREP taxonomy validation, FR Y-14 attestation, ICFR over regulatory reporting, board/CFO sign-off and CCAR submission.

## Flow
- Source Regulatory Data causes Calculate RWA.
- Calculate RWA causes Determine Own Funds.
- Determine Own Funds causes Assemble Capital Return.
- Assemble Capital Return causes Validate Return Quality.
- Validate Return Quality causes Attest Capital Return.
- Attest Capital Return causes Submit Capital Return.

## References
- [Common Reporting (COREP)](https://www.regnology.net/en/resources/regulatory-topics/common-reporting-corep/)
- [COREP reporting explained](https://regreportingdesk.com/corep-reporting-explained/)
- [CCAR summary instructions](https://www.federalreserve.gov/publications/comprehensive-capital-analysis-and-review-summary-instructions-2020.htm)
