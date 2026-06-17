---
id: withholding-tax-calculation
title: Withholding Tax Calculation
type: business-capability
domain: Deposits & Accounts
level: L4
aliases: ["WHT Calculation", "Interest Tax Deduction"]
status: draft
sources: ["https://bian.org/semantic-apis/customer-tax-handling/", "https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding"]
---

# Withholding Tax Calculation

**Definition.** Withholding Tax Calculation derives and deducts applicable withholding tax on credit interest at posting, supporting the tax-processing behaviour aligned to the BIAN Customer Tax Handling service domain.
**Also known as:** WHT Calculation, Interest Tax Deduction.

## Relationships
- Withholding Tax Calculation is defined in the Deposits & Accounts domain.
- Withholding Tax Calculation is derived from Deposit Tax Withholding.
- Withholding Tax Calculation depends on the Core Banking Processing capability.

## Details
The BIAN Customer Tax Handling tax-processing behaviour deducts tax at source; US backup withholding of 24% applies to interest when a payee has not furnished a certified TIN on Form W-9 or the IRS has notified the bank of an incorrect TIN.

## References
- [BIAN Customer Tax Handling](https://bian.org/semantic-apis/customer-tax-handling/)
- [IRS Backup Withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding)
