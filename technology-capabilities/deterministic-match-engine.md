---
id: deterministic-match-engine
title: Deterministic Match Engine
type: technology-capability
domain: Data & Analytics
level: L3
aliases: ["Rule-Based Matching", "Exact Match Engine", "Identifier Matching"]
status: draft
sources: ["https://www.informatica.com/resources/articles/master-data-governance-framework.html", "https://www.actian.com/blog/data-governance/master-data-governance/"]
---

# Deterministic Match Engine

**Definition.** Deterministic Match Engine links records using exact and rule-based key comparisons to identify the same entity with high precision.
**Also known as:** Rule-Based Matching, Exact Match Engine, Identifier Matching.

## Relationships
- Deterministic Match Engine is defined in the Data & Analytics domain.
- Deterministic Match Engine is derived from Party Matching & Merge.
- Deterministic Match Engine is related to Probabilistic Match Engine.

## Details
Deterministic Match Engine declares two records the same when defined keys agree exactly after normalisation, for example identical national ID plus date of birth, or a standardised name plus address. Rules are explicit and explainable, so a match either passes or fails a condition with no probability score. Deterministic matching gives very high precision and is fast and auditable, which suits regulated linkage where false merges carry compliance risk, but it misses links when identifiers are missing, mistyped, or formatted differently. It is therefore typically paired with probabilistic matching, which scores fuzzy similarity to catch the records that exact rules cannot, within the same party match-and-merge capability.

## References
- [Informatica: Master data governance framework](https://www.informatica.com/resources/articles/master-data-governance-framework.html)
- [Actian: Master data governance](https://www.actian.com/blog/data-governance/master-data-governance/)
