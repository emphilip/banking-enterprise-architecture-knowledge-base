---
id: document-classification-service
title: Document Classification Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Document Type Classifier", "Page Classification Service", "Doc Sorting Service"]
status: draft
sources: ["https://www.klippa.com/en/blog/information/ocr-loan-processing/", "https://www.llamaindex.ai/blog/loan-document-automation"]
---

# Document Classification Service

**Definition.** Document Classification Service identifies and labels each captured page by document type before extraction, splitting multi-document packages so the correct extraction logic is applied.
**Also known as:** Document Type Classifier, Page Classification Service, Doc Sorting Service.

## Relationships
- Document Classification Service is defined in the Core Processing domain.
- Document Classification Service is derived from Document Capture & Verification.
- Document Classification Service is related to Data Extraction Service.

## Details
Document Classification Service inspects each scanned page and assigns a document type — loan application, pay stub, W-2, bank statement, tax return, identity document — using layout and content features. Because borrowers upload mixed multi-document packages as a single file, the service detects document boundaries and splits the package into its constituent documents, so each downstream extraction template is applied only to the pages it matches. This classify-then-split step, described in loan-document automation guides, is what lets the pipeline route a 40-page upload into correctly typed sub-documents before Data Extraction Service pulls fields.

## References
- [OCR for loan processing (Klippa)](https://www.klippa.com/en/blog/information/ocr-loan-processing/)
- [Loan document automation (LlamaIndex)](https://www.llamaindex.ai/blog/loan-document-automation)
