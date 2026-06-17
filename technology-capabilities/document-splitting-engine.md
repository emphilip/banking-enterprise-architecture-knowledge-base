---
id: document-splitting-engine
title: Document Splitting Engine
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Document Split Service", "Segment Splitting Engine", "Line-Item Splitting Service"]
status: draft
sources: ["https://learning.sap.com/courses/configuring-the-financial-closing-in-sap-s-4hana/explaining-the-purpose-of-document-splitting-in-general-ledger-accounting", "https://www.stechies.com/document-splitting-new-general-ledger/"]
---

# Document Splitting Engine

**Definition.** Document Splitting Engine splits posted accounting documents across segments, profit centres and other dimensions per configured splitting rules to maintain balanced sub-statements by dimension.
**Also known as:** Document Split Service, Segment Splitting Engine, Line-Item Splitting Service.

## Relationships
- Document Splitting Engine is defined in the Core Processing domain.
- Document Splitting Engine is derived from Accounting Rules Engine.

## Details
Document Splitting Engine decomposes the non-assigned lines of an accounting document — such as payables, receivables, tax and cash clearing lines — and inherits the account-assignment characteristics (segment, profit centre, business area) from the expense or revenue lines they relate to. As described in SAP S/4HANA general-ledger configuration, splitting classifies each line by an item category and applies a splitting method so that the document remains balanced to zero per dimension, enabling segment-level balance sheets and a complete document-split audit trail without manual allocation journals.

## References
- [Document splitting in general ledger accounting (SAP Learning)](https://learning.sap.com/courses/configuring-the-financial-closing-in-sap-s-4hana/explaining-the-purpose-of-document-splitting-in-general-ledger-accounting)
- [Document splitting in the new general ledger (STechies)](https://www.stechies.com/document-splitting-new-general-ledger/)
