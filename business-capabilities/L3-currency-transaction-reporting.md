---
id: currency-transaction-reporting
title: Currency Transaction Reporting
type: business-capability
domain: Compliance & Financial Crime
level: L3
aliases: ["CTR Management", "Cash Transaction Reporting"]
status: draft
sources: ["https://www.fincen.gov/resources/filing-information", "https://bsaaml.ffiec.gov/manual"]
---

# Currency Transaction Reporting

**Definition.** Currency Transaction Reporting detects and files reports on cash transactions over the regulatory threshold (CTRs for currency transactions exceeding USD 10,000) per the US Bank Secrecy Act and FinCEN rules.
**Also known as:** CTR Management, Cash Transaction Reporting.

## Relationships
- Currency Transaction Reporting is defined in the Compliance & Financial Crime domain.
- Currency Transaction Reporting is derived from AML Monitoring.
- Currency Transaction Reporting depends on the Regulatory Reporting Engine capability.
- Currency Transaction Reporting depends on the Transaction Monitoring Platform capability.

## Details
The BSA requires a Currency Transaction Report (FinCEN Form 112) for each transaction in currency of more than $10,000 conducted by, through, or to the institution on a single business day, aggregating multiple transactions by the same person. CTRs must be filed within 15 calendar days. The capability also detects structuring — deliberately splitting cash to evade the $10,000 threshold — which is itself a federal offence and a SAR trigger. Exemptions for certain eligible business customers are governed by FinCEN's exemption rules.

## References
- [FinCEN filing information](https://www.fincen.gov/resources/filing-information)
- [FFIEC BSA/AML Examination Manual](https://bsaaml.ffiec.gov/manual)
