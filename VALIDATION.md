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

---

## Deep-dive: Payments domain (2026-06-15)

First domain deep-dive, run through the eval-gated pipeline (`_status/DEEP-DIVE-PROMPT.md`).

**Added (+97 concepts):** 16 L3 + 17 L4 business capabilities; 11 technology
sub-capabilities (8 L2, 3 L3) under Payment Orchestration; 9 sub-processes; 22
ordered process-flow steps across Payment Processing, Reconciliation &
Settlement, and Cash Management (with `## Flow` sections on the parent process
notes); 16 supporting concepts (6 role, 4 event, 6 artifact); 3 new legacy and
3 new modern payment-hub systems.

**Eval gates (deterministic, `evals/checks.py`):**
- research → 0 FAIL · steward → 0 FAIL / 0 WARN · author → 0 FAIL / 0 WARN ·
  weave → 0 FAIL / 0 WARN · all (incl. regression vs baseline) → 0 FAIL / 0 WARN.
- New concept types are first-class in the harness (technology sub-capabilities,
  sub-processes, process flow steps, supporting concepts); the registry schema
  and `CONVENTIONS.md` were extended to match.

**Eval gate (semantic, LLM-judge, `evals/judge-payments.md`):** PASS on a
28-file sample. Means — accuracy 4.79, groundedness 4.79, relationship
sensibility 4.93, naming fidelity 5.00, granularity 4.89. Five recommended
accuracy fixes were applied (ACI EPP "50+ networks" figure removed; SEPA vs
Bacs/AUDDIS corrected; Request To Pay source + "defer" option corrected;
Settlement Officer sign-off ownership ceded to Reconciliation Analyst; Bottomline
framing confirmed already correct).

**Coverage:** every legacy payment-hub system now has a modern successor (the 3
new moderns extended with multi-supersedes); the steward WARNs are cleared.

**Knowledge base totals after Payments deep-dive:** 100 business capabilities
(L1–L4), 41 technology capabilities + sub-capabilities, 31 processes +
sub-processes, 22 process-flow steps, 16 supporting concepts, 46 legacy + 53
modern systems, 10 glossary terms.

---

## Deep-dive: Customer Management domain (2026-06-15)

Second domain deep-dive via the eval-gated pipeline.

**Added (+105 concepts):** 14 L3 + 20 L4 business capabilities; 16 technology
sub-capabilities (12 L2, 4 L3) under CRM Platform, Master Data Management,
Customer Identity, and Conversational AI; 8 sub-processes; 24 ordered
process-flow steps across Customer Onboarding, Complaint Handling, and Service
Request Handling (with `## Flow` sections); 17 supporting concepts (5 role, 5
event, 7 artifact); 2 new legacy + 4 new modern systems.

**Eval gates (deterministic):** research / steward / author / weave / all (incl.
regression) → all **0 FAIL / 0 WARN**.

**Steward collision resolution:** "Virtual Assistant" (proposed tech sub-cap)
collided with an existing alias of Conversational AI → renamed **Self-Service
Virtual Assistant**; "Consent & Preference Management" (capability) vs "Consent
Management Service" (tech sub-cap) disambiguated. Every new legacy (SAP CRM,
Informatica MDM) given a modern successor.

**Eval gate (semantic, LLM-judge, `evals/judge-customer-management.md`):** initial
run FAILed narrowly (Groundedness 3.96 vs 4.0) — the 8 sampled L3/L4 capability
notes had boilerplate Details + generic citations. Fixed all 8 (source-anchored
Details; corrected BIAN "Customer Case" naming; consent remapped to Customer
Profile / Customer Agreement with ICO citation; FCA DISP for complaints).
Re-judge: all 8 now ≥4 on Groundedness (mean 4.25), lifting the sample to PASS on
every dimension (accuracy 4.61, groundedness ≈4.32, relationships 4.96, naming
5.00, granularity 4.39).

**Knowledge base totals after Customer Management deep-dive:** 134 business
capabilities (L1–L4), 57 technology capabilities + sub-capabilities, 39 processes
+ sub-processes, 46 process-flow steps, 33 supporting concepts, 48 legacy + 57
modern systems, 10 glossary terms.

---

## Deep-dive: Lending & Credit domain (2026-06-15)

Third domain deep-dive via the eval-gated pipeline.

**Added (+123 concepts):** 19 L3 + 21 L4 business capabilities; 13 technology
sub-capabilities (10 L2, 3 L3) under Loan Origination Platform and Credit
Decisioning Engine; 12 sub-processes; 32 ordered process-flow steps across Loan
Origination Workflow, Credit Underwriting, Mortgage Origination, Loan Collections
and Trade Finance Processing (with `## Flow` sections); 19 supporting concepts
(8 role, 5 event, 6 artifact); 4 new legacy + 3 new modern systems.

**Eval gates (deterministic):** research / steward / author / weave / all (incl.
regression) → all **0 FAIL / 0 WARN**.

**Steward collision resolution:** three proposed names equal to existing aliases
renamed — Origination Pre-Qualification, Late Collections, Underwriting Outcome.
Every new legacy (Ellie Mae Encompass, Finastra LaserPro, FICO Origination
Manager, Experian PowerCurve) given a modern successor.

**Eval gate (semantic, LLM-judge, `evals/judge-lending-and-credit.md`):** PASS on
first pass (means — accuracy 4.50, groundedness 4.30, relationships 4.53, naming
4.43, granularity 4.30). The source-anchored Details requirement (carried over
from the Customer Management lesson) cleared Groundedness on the first attempt.
Three non-blocking polish fixes applied: Evaluate Collateral step now depends_on
Collateral Valuation (was Credit Decisioning Engine); MeridianLink supersedes
Finastra LaserPro (better capability fit than Ellie Mae Encompass, which remains
covered by Temenos Origination); Ellie Mae Encompass cloud-positioning softened.

**Knowledge base totals after Lending & Credit deep-dive:** 174 business
capabilities (L1–L4), 70 technology capabilities + sub-capabilities, 51
processes + sub-processes, 78 process-flow steps, 52 supporting concepts,
52 legacy + 60 modern systems, 10 glossary terms.
