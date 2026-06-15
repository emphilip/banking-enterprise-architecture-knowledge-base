# LLM-Judge Report — Customer Management Deep-Dive

Reviewer: `judge` sub-agent. Date: 2026-06-15. Rubric: `evals/rubric.md`.
Sample: 28 representative new notes. All 28 paths exist (none skipped).

## Method notes / source-fetch caveats
- Every cited URL was fetched. `bian.org` (all variants) and several vendor/regulator
  sites (cxtoday, reltio.com pages, microsoft sub-pages partly, hypr, kasisto,
  fca.org.uk handbook, sanctionscanner, idenfy, etc.) returned **HTTP 403** to the
  fetcher. For those, claims were corroborated via independent web search against the
  same primary sources (AWS docs, Reltio docs, Salesforce, Microsoft, FCA Handbook
  text, ISO, Informatica, Pega, Kasisto, ITIL). Where a note cites a **generic BIAN
  landscape index** (`bian.org/servicelandscape/`) but asserts a *specific* named
  service domain, the cited page would not by itself substantiate the mapping — this
  is noted and lightly penalized, though the named BIAN domains were confirmed to
  exist via search.
- Naming/relationship correctness was cross-checked against
  `glossary/_canonical-names.md` (the single source of truth).

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|---|---|---|---|---|---|---|
| systems/legacy/sap-crm.md | 4 | 4 | 4 | 5 | 4 | On-prem SAP CRM in maintenance, superseded by SAP cloud CX — confirmed (SAP mainstream maint. to 2027; Sales Cloud is cloud successor). Rel "CRM Platform depends on SAP CRM" + "related to Siebel CRM" match registry. Single cxtoday source 403 but claim corroborated. |
| systems/legacy/informatica-mdm.md | 5 | 5 | 5 | 5 | 4 | Multidomain MDM, match-merge, survivorship, stewardship, Siperian heritage, on-prem→SaaS all confirmed (Informatica docs/site). "MDM depends on Informatica MDM" + "related to Reltio" match registry. |
| systems/modern/microsoft-dynamics-365.md | 5 | 5 | 5 | 5 | 4 | microsoft.com fetched directly: "agentic CRM, CCaaS, and ERP", Copilot/agents, Customer Service + Contact Center — every claim grounded. supersedes SAP CRM matches registry exactly. |
| systems/modern/pega-customer-service.md | 5 | 5 | 5 | 5 | 4 | Case-centric, low-code, next-best-action, banking complaints/omnichannel all confirmed (Pega site/G2). supersedes Siebel CRM matches registry. |
| systems/modern/reltio.md | 5 | 5 | 5 | 5 | 4 | Cloud-native, API-first, ML/AI entity resolution, dynamic survivorship, golden record, SaaS — all confirmed (Reltio docs/site). supersedes Informatica MDM + related to Snowflake match registry. |
| systems/modern/amazon-lex.md | 5 | 5 | 5 | 5 | 4 | Managed conversational AI, ASR+NLU, voice/text, Amazon Connect integration confirmed (AWS docs: "same ASR/NLU as Alexa", native Connect integration). supersedes Legacy IVR System matches registry. Only one source but it fully covers the claims. |
| technology-capabilities/customer-360-view.md | 5 | 5 | 5 | 5 | 4 | Aggregated single actionable profile of holdings/transactions/interactions confirmed (Salesforce: "single view…consolidates insights…actionable profile"). derived_from CRM Platform; related to Contact & Account Management — both canonical sub-caps. |
| technology-capabilities/golden-record-management.md | 5 | 5 | 5 | 5 | 4 | Survivorship → best-version-of-truth with crosswalks + lineage confirmed (Reltio: OV/winner values, crosswalk aggregation). derived_from MDM; depends_on Data Governance; related to Party Matching & Merge — all canonical. |
| technology-capabilities/customer-authentication.md | 5 | 4 | 5 | 5 | 4 | Adaptive/MFA/passwordless FIDO passkeys + step-up confirmed via CIAM/FIDO search (HYPR + Medium both 403, corroborated). derived_from Customer Identity; depends_on Threat Detection; related to Digital Channel Platform — all canonical & sensible. |
| technology-capabilities/consent-management-service.md | 5 | 4 | 5 | 5 | 4 | Consent capture/enforce/audit, versioning, GDPR/open-banking confirmed (CIAM sources, WSO2 403 but corroborated). derived_from Customer Identity; depends_on Data Governance; related to Regulatory Compliance — all canonical. |
| technology-capabilities/self-service-virtual-assistant.md | 5 | 5 | 5 | 5 | 4 | NLU/NLG chat+voice self-service with human handoff, Kasisto KAI + Amazon Lex confirmed. derived_from Conversational AI; depends_on Generative AI Platform; related to Customer Servicing — all canonical. |
| business-capabilities/L3-lead-management.md | 4 | 3 | 5 | 5 | 4 | BIAN Lead/Opportunity Management domain exists (confirmed via BIAN BOM search). Aliases & derived_from Customer Acquisition match registry. Grounded=3: bian 9.1 view URL 403 and APQC PCF page not independently verified; Details is boilerplate ("grounded in BIAN…APQC…cloud-native, API-led, AI-assisted") not tied to a quoted source line. |
| business-capabilities/L3-onboarding-orchestration.md | 4 | 3 | 5 | 5 | 4 | BIAN Party Lifecycle Management exists. derived_from Customer Acquisition; depends_on Workflow Orchestration — sensible & canonical. Grounded=3: cited bian object URL 403; boilerplate Details with no source-anchored claim. |
| business-capabilities/L3-consent-and-preference-management.md | 4 | 3 | 5 | 5 | 4 | Maps to "BIAN Party Authentication and Customer Profile" — plausible but the cited generic `servicelandscape/` index + a Medium blog do not substantiate that specific dual mapping. derived_from Party Data Management; depends_on MDM — canonical. Grounded=3 (generic index, unverified specific mapping). |
| business-capabilities/L3-complaint-management.md | 4 | 3 | 5 | 5 | 4 | Maps to "BIAN Customer Case Management"; BIAN's domain is actually **Customer Case** (Customer Case Management is the capability/plan variant) — minor imprecision. derived_from Customer Servicing; depends_on Workflow Orchestration — canonical. Grounded=3: generic bian index + APQC page unverified for the specific mapping. |
| business-capabilities/L3-behavioural-analytics.md | 4 | 3 | 5 | 5 | 4 | Maps to BIAN "Customer Behavior Insights" + "Customer Event History" — both confirmed to exist. derived_from Customer Segmentation; depends_on Analytics Platform — canonical. Grounded=3: both cited bian URLs 403, domain existence corroborated only via 3rd-party search; Details boilerplate. |
| business-capabilities/L4-lead-capture.md | 4 | 3 | 5 | 5 | 5 | Atomic intake of inbound/outbound leads — correct L4 altitude, no sibling overlap with Lead Qualification. derived_from Lead Management; depends_on CRM Platform — canonical. Grounded=3: generic bian index + unverified APQC; boilerplate Details. |
| business-capabilities/L4-lead-qualification.md | 4 | 3 | 5 | 5 | 5 | Scores/ranks/routes leads — correct atomic L4, distinct from Lead Capture. derived_from Lead Management; depends_on Analytics Platform — canonical & sensible. Grounded=3 (same generic-source issue). |
| business-capabilities/L4-application-decisioning.md | 4 | 3 | 5 | 5 | 5 | Approve/refer/decline against eligibility/policy/risk — correct atomic L4. Maps to BIAN Customer Offer / Sales Product Agreement (Zafin Medium blog covers SalesProductAgreement). derived_from Application Processing; depends_on Workflow Orchestration — canonical. Grounded=3: blog supports SPA only, generic bian index for the rest. |
| business-capabilities/L4-application-tracking.md | 4 | 3 | 5 | 5 | 5 | Status/completeness/SLA + notify — correct atomic L4, distinct from Decisioning. derived_from Application Processing; depends_on Notification Services — canonical & sensible. Grounded=3 (generic bian index + unverified APQC). |
| process-flows/customer-onboarding/01-receive-application.md | 5 | 4 | 5 | 5 | 5 | Single-action step (capture application, open case) — correct step altitude. causes Capture Consent (order 1→2 ✓); depends_on Digital Channel Platform matches registry (Receive Application → Digital Channel Platform). Roles/artifacts/event all canonical. Capco/Wavetec support digital onboarding capture. |
| process-flows/customer-onboarding/05-screen-customer.md | 5 | 5 | 5 | 5 | 5 | Sanctions/PEP/adverse-media screen with hold/escalate — single action, confirmed by Sanction Scanner/SEON. causes Assess Customer Risk (5→6 ✓); depends_on Transaction Monitoring Platform matches registry exactly. KYC Analyst/KYC Profile canonical. |
| process-flows/complaint-handling/01-log-complaint.md | 5 | 5 | 5 | 5 | 5 | Log inbound complaint + reference number — confirmed by ISO 10002 (issue tracking number, record details). causes Acknowledge Complaint (1→2 ✓); depends_on Case Management matches registry. Complaints Officer/Complaint Record/Complaint Received Event canonical. |
| process-flows/complaint-handling/04-investigate-complaint.md | 5 | 5 | 5 | 5 | 5 | "investigate competently, diligently and impartially" verbatim from FCA DISP 1.4.1 (confirmed). causes Determine Outcome (4→5 ✓); depends_on Case Management matches registry. Canonical roles/artifacts. |
| process-flows/service-request-handling/01-capture-request.md | 5 | 4 | 5 | 5 | 5 | Capture request + create ticket — single action, consistent with ITIL SRM (Giva/ConnectWise). causes Authenticate Requester (1→2 ✓); depends_on Contact Center Platform matches registry. Service Advisor/Service Request Ticket/event canonical. |
| process-flows/service-request-handling/05-fulfil-request.md | 5 | 4 | 5 | 5 | 5 | Execute change in system of record — single action, ITIL handling/fulfilment stage. causes Confirm Resolution (5→6 ✓); depends_on Core Banking Processing matches registry. Four-eyes/change control sensible. |
| concepts/kyc-profile.md | 5 | 4 | 5 | 5 | 4 | CDD record: identity evidence + screening + risk rating — confirmed by idenfy KYC content (403, corroborated). Aliases match registry. mentions Assess Customer Risk / Identity & Due Diligence / Create Customer Record — all canonical. Artifact altitude correct. |
| concepts/complaint-record.md | 5 | 5 | 5 | 5 | 4 | Case record w/ reference, category, findings, outcome, redress, retention/RCA — consistent with ComplaintLab DISP guide + ISO 10002. Aliases match registry. mentions Log Complaint / Complaint Intake & Triage / Complaint Handling — all canonical. |

## Per-dimension means (n=28)

| Dimension | Mean |
|---|---|
| Definitional accuracy | 4.61 |
| Groundedness | **3.96** |
| Relationship sensibility | 4.96 |
| Canonical-naming fidelity | 5.00 |
| Granularity fit | 4.39 |

(Groundedness sum = 111/28 = 3.96.)

## Verdict: **FAIL**

The gate requires mean ≥ 4.0 on **every** dimension. **Groundedness mean = 3.96 (< 4.0)**, so the sample fails the gate.

Mitigating facts:
- No individual note scored < 3 on Groundedness or Relationship sensibility, so the
  per-note hard-fail condition is **not** triggered.
- Relationship sensibility (4.96) and canonical-naming (5.00) are excellent — the
  graph is clean and `supersedes`/`derived_from`/`depends_on` directions are correct
  throughout, all matching `_canonical-names.md`.
- The single failing dimension is driven entirely by the **8 L3/L4 business-capability
  notes** (all scored Groundedness=3), whose `## Details` sections are templated
  boilerplate and whose BIAN/APQC citations are generic landscape-index pages (or
  403-blocked specific pages) that do not, by themselves, substantiate the specific
  named service-domain mapping asserted in the definition.

## Required fixes (to pass re-judge)

The cheapest path to mean ≥ 4.0 is to fix Groundedness on the 8 capability notes
(raising each from 3→4 lifts the mean to ~4.25).

- **L3-lead-management.md** — Replace the generic `bian.org/servicelandscape-9-1/views/view_98179.html` (403) with a stable, citable BIAN reference for the **Lead/Opportunity Management** service domain, and rewrite the boilerplate `## Details` to make at least one source-anchored claim (not "grounded in BIAN…cloud-native, API-led, AI-assisted").
- **L3-onboarding-orchestration.md** — Same: cite a reachable BIAN page for **Party Lifecycle Management** and de-boilerplate Details.
- **L3-consent-and-preference-management.md** — The cited generic `servicelandscape/` index + Medium blog do not support the asserted "Party Authentication and Customer Profile" dual mapping. Either cite specific BIAN domain pages or soften the claim; replace the Medium blog with an authoritative consent/GDPR or BIAN source.
- **L3-complaint-management.md** — Correct the mapping name: BIAN's service domain is **Customer Case** (not "Customer Case Management", which is the capability/business-object variant); cite a reachable BIAN Customer Case page; de-boilerplate Details.
- **L3-behavioural-analytics.md** — Both cited BIAN URLs 403; add a citable confirmation of the **Customer Behavior Insights** and **Customer Event History** domains and anchor one Details claim to it.
- **L4-lead-capture.md / L4-lead-qualification.md** — Replace generic `servicelandscape/` index citation with a specific Lead/Opportunity Management reference and/or a verifiable APQC PCF element; rewrite identical boilerplate Details so the two siblings cite distinct supporting evidence.
- **L4-application-tracking.md** — Replace generic bian index with a citable Customer Offer reference; de-boilerplate Details.

Optional (already passing, but would harden Groundedness toward 4.5+):
- The single-source system notes (**amazon-lex.md**) and 403-only sources
  (**customer-authentication.md**, **consent-management-service.md**, **kyc-profile.md**)
  would benefit from one additional reachable primary source each, but all are
  currently corroborated and score ≥4.
