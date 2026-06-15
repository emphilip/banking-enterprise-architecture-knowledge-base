---
id: validation
title: Validation Report
type: report
status: draft
---

# Validation Report

Final QA for the Banking Enterprise Architecture Knowledge Base, run by the
`validator` pass. Industry: **Retail & Commercial Banking**. All checks below
were executed programmatically against the file tree and the canonical-names
registry.

## Scale (v1 first cut)

| Pillar | Count | Target |
|---|---|---|
| Domains (value streams + technology domains) | 15 | 8–14 |
| Business capabilities (L1: 12, L2: 42, L3: 13) | 67 | 40–80 |
| Business processes | 22 | 15–25 |
| Technology capabilities | 30 | 20–30 |
| Legacy systems | 43 | 30–50 |
| Modern / AI systems | 50 | 30–50 |
| Glossary terms | 10 | — |
| **Total concept files** | **237** | — |

Plus: `README.md`, `CONVENTIONS.md`, this `VALIDATION.md`, 8 `_index.md`
Maps-of-Content, `glossary/_canonical-names.md`, and 2 maps.

## Checklist

- [x] **(a) Every relationship sentence references a name in the registry.**
  All relationship bullets across all 237 concept files were parsed; every bullet
  containing one of the 7 verbs references at least one canonical name present in
  `glossary/_canonical-names.md`. Result: **0 violations.**
- [x] **(b) No file relies on frontmatter for relationships.** Every concept file
  carries an explicit `## Relationships` prose section; frontmatter is duplicated
  in prose. Result: **0 files missing `## Relationships`.**
- [x] **(c) Relationships sit within the first ~1800 chars of the body.** The
  `## Relationships` heading appears within 1800 characters of the body start in
  every file (largest concept file is ~2 KB). Result: **0 late relationship
  blocks.**
- [x] **(d) Every `_index.md` links its files.** Each of the 8 indexes
  (domains, business-capabilities, business-processes, technology-capabilities,
  systems/legacy, systems/modern, glossary, + the glossary registry link) was
  checked to wikilink every non-index `.md` in its folder. Result: **all files
  linked, 0 orphans.**
- [x] **(e) No orphan / duplicate concepts.** Registry canonical names (237) ==
  concept files on disk (237); **0 missing, 0 unexpected.** Filename → registry
  alignment verified for every pillar (level prefix for capabilities, kebab of
  the canonical name elsewhere).

## Canonical-name collision resolution (ontology-steward)

Three domain names originally collided with their L1 capability names, which
would have merged into a single graph node each. Resolved by renaming the L1
capabilities so they are distinct from their domains:

- `Customer Management` (L1 capability) → **Customer Lifecycle Management**
- `Payments` (L1 capability) → **Payment Services**
- `Risk Management` (L1 capability) → **Enterprise Risk Management**

All `derived_from` children, the domain note subjects, inverse `related_to`
links, and the registry were updated accordingly. After resolution: **237 unique
canonical names for 237 files (0 collisions).**

## Current → future-state coverage

- **Every legacy system has at least one modern successor** mapped via
  `supersedes` (verified: 0 legacy systems without a successor). See
  `maps/current-to-future-state.md`.
- Every `supersedes` target is a real legacy system; every system `realizes`
  (is depended on by) a real technology capability.

## Known gaps (acceptable for v1 — breadth over depth)

These are intentional v1 thin spots, not errors. Notes affected are marked
`status: draft`.

- **Technology capabilities with no legacy system mapped:** Data Governance,
  Generative AI Platform, Intelligent Document Processing, Machine Learning
  Platform, Master Data Management, Notification Services, Robotic Process
  Automation, Threat Detection. Several of these (Generative AI Platform,
  Intelligent Document Processing) are genuinely net-new categories with no
  meaningful incumbent; others are cross-cutting functions historically
  delivered as features of other platforms rather than a discrete product.
- **Technology capabilities with no modern system mapped:** Data Governance,
  Document Management, Master Data Management, Notification Services, Robotic
  Process Automation, Threat Detection. Candidate future additions: Collibra
  (Data Governance), Reltio (Master Data Management), UiPath (Robotic Process
  Automation), CrowdStrike / Microsoft Sentinel (Threat Detection), Twilio
  (Notification Services).
- All system/vendor notes are `status: draft` and cite the vendor source; vendor
  facts were kept to well-known, verifiable descriptions and generic where
  uncertain, per the no-invented-facts rule.

## How to re-run

The validator logic is reproducible: parse `glossary/_canonical-names.md` for
canonical names + expected filenames, then for every concept file confirm a
`## Relationships` section within the first 1800 chars whose bullets reference
only registry names, and confirm each `_index.md` links every file in its
folder.
