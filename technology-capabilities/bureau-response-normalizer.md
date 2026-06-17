---
id: bureau-response-normalizer
title: Bureau Response Normalizer
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Bureau Data Normaliser", "Credit Report Parser", "Bureau Attribute Mapper"]
status: draft
sources: ["https://assets.equifax.com/marketing/US/assets/comparing_scores_whitepaper.pdf", "https://www.creditbureauconnection.com/compliance_solutions/adverse_action.php"]
---

# Bureau Response Normalizer

**Definition.** Bureau Response Normalizer parses and standardises credit-bureau report responses from multiple bureaus into a common attribute model for downstream scoring and decisioning.
**Also known as:** Bureau Data Normaliser, Credit Report Parser, Bureau Attribute Mapper.

## Relationships
- Bureau Response Normalizer is defined in the Core Processing domain.
- Bureau Response Normalizer is derived from Bureau Data Integration.
- Bureau Response Normalizer is related to Credit Scoring Service.

## Details
Bureau Response Normalizer parses the raw report formats returned by Equifax, Experian and TransUnion and maps tradelines, inquiries, public records and scores into one harmonised attribute set. Because each bureau organises and labels data differently — and a consumer's score can vary across bureaus due to differing data and model versions, as Equifax's score-comparison note explains — the normaliser resolves these differences so decisioning logic reads a single consistent schema regardless of source. The normalised attributes are then supplied to Credit Scoring Service for model execution.

## References
- [Comparing credit scores (Equifax)](https://assets.equifax.com/marketing/US/assets/comparing_scores_whitepaper.pdf)
- [Adverse action compliance solutions (Credit Bureau Connection)](https://www.creditbureauconnection.com/compliance_solutions/adverse_action.php)
