---
id: b2b-edi-gateway
title: B2B/EDI Gateway
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["EDI Gateway", "B2B Integration Gateway", "Trading Partner Gateway"]
status: draft
sources: ["https://www.ibm.com/think/topics/edi-integration", "https://www.thruinc.com/blog/ipaas-for-edi-mft/"]
---

# B2B/EDI Gateway

**Definition.** B2B/EDI Gateway exchanges structured business documents with external trading partners using EDI standards (X12, EDIFACT) and partner onboarding, mapping, and acknowledgement handling.
**Also known as:** EDI Gateway, B2B Integration Gateway, Trading Partner Gateway.

## Relationships
- B2B/EDI Gateway is defined in the Integration & APIs domain.
- B2B/EDI Gateway is derived from Integration Platform.
- B2B/EDI Gateway depends on Data Mapping & Transformation.

## Details
B2B/EDI Gateway translates between internal application formats and partner EDI standards such as ANSI X12 (810 invoice, 850 purchase order) and UN/EDIFACT, manages per-partner trading profiles and envelopes (ISA/GS/ST), and exchanges over AS2, SFTP, or VANs. It generates and reconciles functional acknowledgements (997/CONTRL), enforces partner-specific validation, and maintains non-repudiation audit trails. Partner onboarding configures identifiers, document types, and connectivity so each relationship is governed and traceable end to end.

## References
- [IBM: EDI integration](https://www.ibm.com/think/topics/edi-integration)
- [iPaaS for EDI and MFT](https://www.thruinc.com/blog/ipaas-for-edi-mft/)
