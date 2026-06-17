---
id: bank-statement-ingestion-service
title: Bank Statement Ingestion Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Statement Parsing Service", "BAI2 MT940 Parser", "Electronic Bank Statement Loader"]
status: draft
sources: ["https://www.debtbook.com/blog/common-bank-reporting-payment-file-formats-bai2-edi-iso-20022-xml", "https://www.gtreasury.com/posts/how-electronic-bank-statements-enable-automated-bank-reporting"]
---

# Bank Statement Ingestion Service

**Definition.** Bank Statement Ingestion Service parses and normalises electronic bank statements in BAI2, MT940 and CAMT.053 formats from multiple banks to feed intraday and prior-day cash positions.
**Also known as:** Statement Parsing Service, BAI2 MT940 Parser, Electronic Bank Statement Loader.

## Relationships
- Bank Statement Ingestion Service is defined in the Core Processing domain.
- Bank Statement Ingestion Service is derived from Cash Positioning Service.
- Bank Statement Ingestion Service is related to Bank Connectivity Hub.

## Details
Bank Statement Ingestion Service consumes end-of-day and intraday statement files and maps each format to a common model. BAI2 uses three-digit type codes for opening/closing ledger and available balances and individual transaction detail; SWIFT MT940 carries the customer statement with :60F: opening and :62F: closing balance fields; ISO 20022 CAMT.053 is the XML bank-to-customer statement and CAMT.052 the intraday report. The service normalises balances and transactions across banks so prior-day and intraday positions can be assembled. The raw files are typically delivered through Bank Connectivity Hub.

## References
- [Common bank reporting file formats: BAI2, EDI, ISO 20022 (DebtBook)](https://www.debtbook.com/blog/common-bank-reporting-payment-file-formats-bai2-edi-iso-20022-xml)
- [How electronic bank statements enable automated bank reporting (GTreasury)](https://www.gtreasury.com/posts/how-electronic-bank-statements-enable-automated-bank-reporting)
