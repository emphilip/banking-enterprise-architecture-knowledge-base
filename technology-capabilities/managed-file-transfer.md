---
id: managed-file-transfer
title: Managed File Transfer
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["MFT", "Secure File Transfer", "File Gateway"]
status: draft
sources: ["https://www.thruinc.com/blog/ipaas-for-edi-mft/", "https://www.celigo.com/articles/what-is-ipaas-integration-platform-as-a-service/"]
---

# Managed File Transfer

**Definition.** Managed File Transfer governs secure, auditable, policy-driven transfer of files between systems and partners with protocol support, encryption, and delivery tracking beyond plain FTP.
**Also known as:** MFT, Secure File Transfer, File Gateway.

## Relationships
- Managed File Transfer is defined in the Integration & APIs domain.
- Managed File Transfer is derived from Integration Platform.
- Managed File Transfer is related to B2B/EDI Gateway.

## Details
Managed File Transfer moves batch files reliably and securely using SFTP, FTPS, HTTPS, and AS2, with encryption in transit and at rest (PGP/OpenPGP), checkpoint restart for large files, scheduling, and automatic retry. It enforces policy (who can send what, where, and when), captures full audit logs and delivery receipts for compliance, and triggers downstream workflows on arrival. In banking it carries nightly payment files, statements, and regulatory submissions where plain FTP lacks the security, guaranteed delivery, and traceability MFT provides.

## References
- [iPaaS for EDI and MFT](https://www.thruinc.com/blog/ipaas-for-edi-mft/)
- [What is iPaaS?](https://www.celigo.com/articles/what-is-ipaas-integration-platform-as-a-service/)
