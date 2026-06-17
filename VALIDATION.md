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

---

## Deep-dive: Deposits & Accounts domain (2026-06-15)

Fourth domain deep-dive via the eval-gated pipeline.

**Added (+126 concepts):** 23 L3 + 22 L4 business capabilities; 11 technology
sub-capabilities (8 L2, 3 L3) under Core Banking Processing; 3 new top-level
processes (Account Maintenance, Account Closure, Overdraft Servicing); 11
sub-processes; 33 ordered process-flow steps across 5 processes (with `## Flow`
sections); 18 supporting concepts (4 role, 5 event, 9 artifact); 3 new legacy +
3 new modern systems.

**Eval gates (deterministic):** research / steward / author / weave / all (incl.
regression) → all **0 FAIL / 0 WARN**.

**Steward:** 2 alias-collision renames (Deposit Statement Production, Deposit
Statement Delivery); 3 new processes added to the Business processes table; every
new legacy given a successor (FIS Horizon ← SAP Deposits Management).

**Eval gate (semantic, LLM-judge, `evals/judge-deposits-and-accounts.md`):** PASS
(means — accuracy 4.50, groundedness 4.00, relationships 4.50, naming 4.08,
granularity 4.67). Marginal on Groundedness, so six recommended fixes were
applied to harden it: corrected BIAN domain naming on two L3 notes (Current /
Savings / Term Deposit; dropped non-existent "Deposit Account" and "Interest
Determination" domains); removed a factually wrong "CASS rules" control from the
escheatment step (UK client-money regulation, not US escheatment) and repointed
dormancy/escheatment sources to NAUPA / Uniform Law Commission RUUPA; tightened
the Regulation D 7-day/6-day early-withdrawal phrasing. (Note: two earlier judge
runs were lost to a session-limit reset; this is the completed re-run.)

**Knowledge base totals after Deposits & Accounts deep-dive:** 219 business
capabilities (L1–L4), 81 technology capabilities + sub-capabilities, 65
processes + sub-processes, 111 process-flow steps, 69 supporting concepts,
55 legacy + 63 modern systems, 10 glossary terms.

---

## Deep-dive: Cards domain (2026-06-15)

Fifth domain deep-dive via the eval-gated pipeline.

**Added (~106 concepts):** 22 L3 + 9 L4 business capabilities; 11 technology
sub-capabilities (8 L2, 3 L3) under Card Processing; 3 new top-level processes
(Card Transaction Authorization, Chargeback Processing, Card Fraud Handling); 14
sub-processes; 32 ordered process-flow steps across 5 processes (with `## Flow`
sections); 15 supporting concepts (4 role, 5 event, 6 artifact); 3 new legacy +
5 new modern systems.

**Eval gates (deterministic):** research / steward / author / weave / all → 0
FAIL. One advisory WARN remains: Fiserv OmniPay (an acquirer / merchant-processing
platform) has no modern successor — intentional, as no same-capability
acquirer-side modern is in scope (the modern card systems modelled are
issuer-side processors). Documented as a known gap.

**Steward:** resolved a capability-vs-process name clash (capability →
**Chargeback Handling**, process stays **Chargeback Processing**); artifact
**Card Account Application** vs capability Card Application; sub-process
**Authorization Validation & Decisioning** vs capability Authorization
Decisioning.

**Harness improvement:** the author check now warns about a missing "Also known
as" line only when the note actually declares aliases (process-step notes
legitimately have none) — eliminated 32 false-positive WARNs.

**Eval gate (semantic, LLM-judge, `evals/judge-cards.md`):** initial run FAILed on
the per-note floor — `thredd.md` scored 2 on Relationship sensibility for a
wrong-capability supersede ("Thredd supersedes Fiserv OmniPay": issuer processor
vs acquirer platform). Fixed: removed that supersede (Thredd supersedes only the
same-capability First Data Cards); also repointed 3-D Secure Service derived_from
Card Tokenization Service → Card Authorization Engine. Re-judge: both notes now
score 4 on Relationship sensibility. Final means — accuracy 4.64, groundedness
4.04, relationships 4.61, naming 4.25, granularity 4.21 → PASS.

**Knowledge base totals after Cards deep-dive:** 250 business capabilities
(L1–L4), 92 technology capabilities + sub-capabilities, 82 processes +
sub-processes, 143 process-flow steps, 84 supporting concepts, 58 legacy +
68 modern systems, 10 glossary terms.

---

## Deep-dive: Wealth & Investments domain (2026-06-16)

Sixth domain deep-dive via the eval-gated pipeline. This domain had **no
top-level technology capability** in v1, so the run minted new ones.

**Added (~130 concepts):** 18 L3 + 20 L4 business capabilities; **3 new top-level
technology capabilities** (Portfolio Management System, Order Management System,
Investment Advisory Platform) + 14 sub-capabilities (11 L2, 3 L3); 4 new
top-level processes (Financial Planning, Portfolio Rebalancing, Trade Order
Management, Performance Reporting); 12 sub-processes; 31 ordered process-flow
steps across 5 processes (with `## Flow` sections); 16 supporting concepts (6
role, 5 event, 5 artifact); 6 new legacy + 7 new modern systems (the first wealth
systems in the base).

**Eval gates (deterministic):** research / steward / author / weave / all → 0
FAIL. The one advisory WARN is the pre-existing Cards Fiserv OmniPay gap
(out of scope).

**Steward:** resolved capability-vs-process clashes (Portfolio Rebalancing →
**Portfolio Rebalancing Management**; Financial Planning → **Financial Planning
Advisory**); classified Temenos WealthSuite as a legacy advisory system; every
wealth legacy given a SAME-CAPABILITY successor (portfolio→portfolio, OMS→OMS,
advisory→advisory).

**Eval gate (semantic, LLM-judge, `evals/judge-wealth-and-investments.md`):** PASS
on first pass (means — accuracy 4.81, groundedness 4.27, relationships 4.77,
naming 4.81, granularity 4.92). Same-capability supersedes (the Cards lesson) held
— no per-note floor breach. Four non-blocking fixes applied: Addepar's "Advent
Converter" scope corrected and its mis-targeted Geneva supersede dropped (Geneva
remains covered by BlackRock Aladdin); Cost Basis Tracking BIAN name corrected to
Securities Position Keeping; the confirm/affirm alias conflation removed from the
Confirm Trade step; the Investment Advisory Platform GenAI dependency softened to
related_to.

**Knowledge base totals after Wealth & Investments deep-dive:** 288 business
capabilities (L1–L4), 109 technology capabilities + sub-capabilities, 98
processes + sub-processes, 174 process-flow steps, 100 supporting concepts,
64 legacy + 75 modern systems, 10 glossary terms.

---

## Deep-dive: Risk Management domain (2026-06-16)

Seventh domain deep-dive via the eval-gated pipeline. Like Wealth, this domain had
no dedicated top-level technology capability in v1, so the run minted new ones.

**Added (~143 concepts):** 6 L2 + 22 L3 + 12 L4 business capabilities; **4 new
top-level technology capabilities** (Risk Analytics Engine, Risk Data Aggregation,
Model Risk Management Platform, Governance Risk & Compliance Platform) + 13
sub-capabilities; 4 new top-level processes (Risk Appetite Setting, Risk
Identification & Assessment, Stress Testing, Risk Reporting); 14 sub-processes; 34
ordered process-flow steps across 6 processes — including the **first
decomposition of the two fraud processes** — (with `## Flow` sections); 18
supporting concepts (6 role, 6 event, 6 artifact, reusing the existing Fraud
Alert); 8 new legacy + 8 new modern risk systems.

**Eval gates (deterministic):** research / steward / author / weave / all → 0
FAIL. The one advisory WARN is the pre-existing Cards Fiserv OmniPay gap.

**Steward:** renames (Stress Testing capability → **Stress Testing Management**;
sub-processes Risk Identification → Risk Capture & Registration, Risk Data
Aggregation → Reporting Data Aggregation); a level-monotonicity adjustment (6
cross-cutting caps leveled to L2, their children to L3); reused the existing Fraud
Alert artifact; same-capability supersedes only (greenfield ValidMind/ModelOp left
without a supersede, by design).

**Eval gate (semantic, LLM-judge, `evals/judge-risk-management.md`):** PASS on
first pass (means — accuracy 4.82, groundedness 4.36, relationships 5.00, naming
5.00, granularity 4.64). Same-capability supersedes verified. One correctness fix
applied (risk-data-aggregation source/claim mismatch repointed to Moody's
RiskAuthority + Quantexa); three thin-source advisories on obvious process steps
left as acceptable (all above the <3 floor).

**Knowledge base totals after Risk Management deep-dive:** 328 business
capabilities (L1–L4), 126 technology capabilities + sub-capabilities, 116
processes + sub-processes, 208 process-flow steps, 118 supporting concepts,
72 legacy + 83 modern systems, 10 glossary terms.

---

## Deep-dive: Compliance & Financial Crime domain (2026-06-16)

Eighth domain deep-dive via the eval-gated pipeline.

**Added (~137 concepts):** 1 L2 + 23 L3 + 19 L4 business capabilities; **1 new
top-level technology capability** (KYC Onboarding Platform) + 20 sub-capabilities
(decomposing Transaction Monitoring Platform, Regulatory Reporting Engine, Data
Governance); 3 new top-level processes (Customer Due Diligence Onboarding,
Sanctions Screening Operations, Regulatory Change Management); 13 sub-processes;
37 ordered process-flow steps across 6 processes — including the **first
decomposition of KYC Verification, Suspicious Activity Reporting, and Regulatory
Filing** — (with `## Flow` sections); 16 supporting concepts (reusing KYC
Profile, Compliance Screening Officer, KYC Analyst); 2 new legacy + 2 new modern
systems.

**Eval gates (deterministic):** research / steward / author / weave / all → 0
FAIL. The one advisory WARN is the pre-existing Cards Fiserv OmniPay gap.

**Steward:** renames (cap Regulatory Change Management → **Regulatory Change
Compliance**; process keeps the plain name; existing SAR process alias → SAR
Process so the new SAR Filing artifact takes that canonical; step Assess Change
Impact → Assess Regulatory Impact); reused KYC Profile / Compliance Screening
Officer / KYC Analyst; Napier AI covers both new legacies same-capability;
Fenergo greenfield.

**Eval gate (semantic, LLM-judge, `evals/judge-compliance-and-financial-crime.md`):**
initial run FAILed — Groundedness 3.96 and a blocking per-note error
(L2 Financial Crime Risk Compliance mis-attributed the 22 predicate offences /
criminal liability for legal persons to Directive (EU) 2024/1640; these belong to
the criminal-law 6AMLD = Directive (EU) 2018/1673). Fixed the directive citation
(L2 re-judged 2→5 on accuracy and groundedness) plus removed an unsourced ">90%"
false-positive stat, replaced an unsourced "preponderance standard" with a
documented true/false-match determination, and swapped blog sources for EBA
DPM/XBRL and BCBS 239. Re-judge: PASS — means accuracy 4.57, groundedness 4.21,
relationships 4.64, naming 4.43, granularity 4.32.

**Knowledge base totals after Compliance & Financial Crime deep-dive:** 370
business capabilities (L1–L4), 147 technology capabilities + sub-capabilities,
132 processes + sub-processes, 245 process-flow steps, 134 supporting
concepts, 74 legacy + 85 modern systems, 10 glossary terms.

---

## Deep-dive: Channels & Engagement domain (2026-06-17)

Ninth domain deep-dive via the eval-gated pipeline.

**Added (~127 concepts):** 22 L3 + 22 L4 business capabilities; 25 technology
sub-capabilities (decomposing Digital Channel Platform + Contact Center Platform;
CRM Platform was already decomposed); 4 new top-level processes (Digital
Onboarding Journey, Channel Servicing, ATM Cash Servicing, Contact Centre
Interaction); 10 sub-processes; 32 ordered process-flow steps across 5 processes
— including the **first decomposition of Branch Operations** — (with `## Flow`
sections); 16 supporting concepts (6 role, 5 event, 5 artifact); 2 new legacy + 7
new modern systems.

**Eval gates (deterministic):** research / steward / author / weave / all → 0
FAIL. The one advisory WARN is the pre-existing Cards Fiserv OmniPay gap.

**Steward:** resolved two cross-proposal collisions (tech sub-cap Digital
Onboarding Journey → **Onboarding Journey Orchestrator**; process ATM Cash
Management → **ATM Cash Servicing**, keeping the L3 capability canonical) plus 12
alias fixes; same-capability supersedes for both new legacies (Kony DBX → Temenos
Infinity; Verint WFM → Verint WFM Cloud).

**Eval gate (semantic, LLM-judge, `evals/judge-channels-and-engagement.md`):**
initial run FAILed on a blocking per-note error — L3 Servicing Resource
Management cited a non-existent BIAN "Servicing Position Management" service
domain (Groundedness 2). Fixed: re-grounded in contact-centre workforce
engagement management (WEM) practice with no fabricated framework claim, plus two
advisory step fixes (human-agent step depends_on Contact Center Platform not
Conversational AI; self-service IVR step no longer attributed to an agent role).
Re-judge: PASS — means accuracy 4.75, groundedness 4.25, relationships 4.75,
naming 4.82, granularity 4.93.

**Knowledge base totals after Channels & Engagement deep-dive:** 414 business
capabilities (L1–L4), 172 technology capabilities + sub-capabilities, 146
processes + sub-processes, 277 process-flow steps, 150 supporting concepts,
76 legacy + 92 modern systems, 10 glossary terms.
