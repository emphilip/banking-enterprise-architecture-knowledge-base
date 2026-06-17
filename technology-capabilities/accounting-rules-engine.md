---
id: accounting-rules-engine
title: Accounting Rules Engine
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Account Determination Engine", "Posting Rules Engine", "Document Splitting Service"]
status: draft
sources: ["https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana", "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/523b8a55559ad007e10000000a44538d.html"]
---

# Accounting Rules Engine

**Definition.** Accounting Rules Engine is the technology capability that derives accounting treatment from business events through configurable rules — account determination, document-splitting and segment derivation, posting validation and substitution, and multi-GAAP rule sets — driving consistent, auditable postings.
**Also known as:** Account Determination Engine, Posting Rules Engine, Document Splitting Service.

## Relationships
- Accounting Rules Engine is defined in the Core Processing domain.
- Accounting Rules Engine is derived from General Ledger Engine.
- Accounting Rules Engine is related to Subledger Accounting.

## Details
Accounting Rules Engine maps each event type to the accounts, segments and tax/currency treatment it should post. Document splitting allocates a single document across profit centres or segments so that complete balanced financial statements can be drawn at the segment level. Validation and substitution rules block or correct non-compliant postings before they hit the ledger, and parallel rule sets produce different valuations for each accounting principle.

## References
- [SAP S/4HANA General Ledger Features](https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana)
- [SAP S/4HANA General Ledger Accounting](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/523b8a55559ad007e10000000a44538d.html)
