---
id: data-extraction-service
title: Data Extraction Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["OCR Extraction Service", "Field Extraction Engine", "Document Data Extractor"]
status: draft
sources: ["https://www.docsumo.com/blog/mortgage-ocr", "https://klearstack.com/lending-document-ocr-guide"]
---

# Data Extraction Service

**Definition.** Data Extraction Service uses OCR and natural-language models to extract structured fields from classified loan documents such as applications, pay stubs and tax forms for the origination system.
**Also known as:** OCR Extraction Service, Field Extraction Engine, Document Data Extractor.

## Relationships
- Data Extraction Service is defined in the Core Processing domain.
- Data Extraction Service is derived from Document Capture & Verification.
- Data Extraction Service is related to Document Classification Service.

## Details
Data Extraction Service converts a classified document image into structured data. It runs OCR to recover text, then applies template or model-based key-value and table extraction to pull fields such as gross pay and year-to-date earnings from a pay stub, borrower and property data from a 1003 application, or income lines from a tax return. Mortgage-OCR guides describe confidence scoring per field and a human-in-the-loop review queue for low-confidence values before the data is written to the loan-origination record. The service depends on the upstream document type from Document Classification Service to choose the correct extraction schema.

## References
- [Mortgage OCR (Docsumo)](https://www.docsumo.com/blog/mortgage-ocr)
- [Lending document OCR guide (KlearStack)](https://klearstack.com/lending-document-ocr-guide)
