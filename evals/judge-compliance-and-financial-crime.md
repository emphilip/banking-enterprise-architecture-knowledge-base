# LLM-Judge Report — Compliance & Financial Crime deep-dive

Reviewer: judge sub-agent (strict). Date: 2026-06-17. Sample: 28 notes.
Scoring 1–5 per rubric dimension (3 = acceptable, <3 = fail).

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|---|---|---|---|---|---|---|
| technology-capabilities/kyc-onboarding-platform.md | 4 | 4 | 4 | 4 | 4 | Accurate CLM/perpetual-KYC framing; vendors (Fenergo, NICE Actimize CDD, SAS CDD) named in Details but only Fenergo/SAS cited — Actimize CDD not sourced, minor. Relationships sensible (depends_on Watchlist Screening Engine, IDP). |
| technology-capabilities/watchlist-screening-engine.md | 5 | 4 | 4 | 4 | 4 | Fuzzy/phonetic matching, good-guy suppression all correct and grounded in Bridger Insight/Actimize. `derived_from Transaction Monitoring Platform` is a slight strain (screening ≠ monitoring) but defensible as FinCrime-stack parent. |
| technology-capabilities/scenario-detection-engine.md | 5 | 5 | 5 | 5 | 4 | Behaviour-detection/scenario layer accurately mapped to Oracle FCCM Behavior Detection; segmentation and look-back claims grounded. Clean. |
| technology-capabilities/financial-crime-case-manager.md | 5 | 4 | 5 | 4 | 4 | ActOne / Oracle ECM correctly identified; four-eyes, audit trail, SAR hand-off accurate. Oracle release-notes URL is a thin citation for ECM features but product is real. |
| technology-capabilities/regulatory-taxonomy-manager.md | 4 | 3 | 4 | 4 | 4 | XBRL/DPM, EBA/EIOPA taxonomy framing accurate. One source is a Medium blog (Suade) — weak for vendor claims; Regnology source supports hub but not DPM-cell mapping specifics. Grounded but thinly. |
| technology-capabilities/data-lineage-tracker.md | 4 | 3 | 4 | 4 | 4 | Column-level lineage + BCBS 239 traceability correct. Both sources are third-party blogs about Collibra, not primary docs; BCBS 239 "complete lineage" claim not tied to a BCBS source. Acceptable but soft. |
| systems/legacy/sas-anti-money-laundering.md | 5 | 5 | 5 | 4 | 4 | SAS AML scope (TM, screening, case mgmt, SAR) grounded in SAS pages. `Transaction Monitoring Platform depends_on SAS AML` correct direction. |
| systems/legacy/lexisnexis-bridger-insight.md | 4 | 4 | 4 | 4 | 4 | Verified: Fircosoft/Firco IS part of LexisNexis Risk Solutions, so aliases and "LexisNexis (Fircosoft)" are correct (not a misattribution). WorldCompliance data claim not directly cited but accurate. Bridger Insight XG real. |
| systems/modern/napier-ai.md | 4 | 4 | 3 | 5 | 4 | Continuum scope (TM, transaction+client screening, case mgmt, explainable AI) accurate and publicly documented. `supersedes SAS AML` is same-capability (sound). `supersedes LexisNexis Bridger Insight` is weaker — Bridger is screening-only while Napier is a broader suite; same-capability holds via Napier's screening module but it is a partial overlap. |
| systems/modern/fenergo.md | 5 | 5 | 5 | 5 | 4 | API-first SaaS CLM/KYC, perpetual KYC, policy engine all grounded in Fenergo docs. `KYC Onboarding Platform depends_on Fenergo` correct. |
| business-capabilities/L2-financial-crime-risk-compliance.md | 2 | 2 | 4 | 4 | 4 | DEFINITIONAL/GROUNDEDNESS ERROR: attributes the "harmonised list of 22 predicate offences" and "criminal liability for legal persons" to Directive (EU) 2024/1640. Those are features of the criminal-law 6AMLD = Directive (EU) 2018/1673; 2024/1640 (the 2024 AML-package directive) governs the supervisory/institutional framework, not the predicate-offence list. The cited source does not support the mapping made. |
| business-capabilities/L3-aml-customer-due-diligence.md | 5 | 5 | 5 | 5 | 4 | FATF R.10 four triggers, FinCEN CDD Rule fifth pillar (2018), 25% prong, four core elements all accurate and grounded in cited FATF/FinCEN sources. Exemplary. |
| business-capabilities/L3-beneficial-ownership-identification.md | 5 | 5 | 5 | 5 | 4 | 25% ownership prong + control prong, FATF R.24/25, AMLD6 registers all correct and sourced to FinCEN BOI/FATF. AMLD6 here used generically (registers) — defensible. |
| business-capabilities/L3-alert-management.md | 4 | 3 | 5 | 4 | 4 | Triage/disposition/false-positive framing correct. ">90% false-positive rate" stated as fact but the cited Wolfsberg/FinCEN pages do not establish that specific figure — unsupported quantitative claim. |
| business-capabilities/L3-adverse-media-screening.md | 5 | 4 | 5 | 5 | 4 | Negative-news/NLP/EDD-escalation accurate; FATF R.10 ongoing-diligence link grounded. Wolfsberg cite is generic but supportive. |
| business-capabilities/L3-regulatory-change-compliance.md | 4 | 4 | 4 | 4 | 4 | Horizon-scan/interpret/operationalise accurate; FFIEC manual "keep controls current" grounded. BIAN "Regulatory Compliance service domain" named in definition but no BIAN source cited — minor naming-of-framework gap. EU AMLA/AMLR single-rulebook mention is accurate. |
| business-capabilities/L4-bribery-and-corruption-risk-assessment.md | 5 | 5 | 5 | 5 | 5 | UK Bribery Act six-principles risk assessment + DOJ/SEC FCPA risk-based weighting (CPI, intermediaries) accurate and grounded in primary sources. Atomic L4. |
| business-capabilities/L4-typology-modelling.md | 5 | 4 | 5 | 5 | 5 | FATF methods-and-trends typologies (TBML, structuring, mules, funnel accounts) accurate. FinCEN-advisory-to-scenario mapping is reasonable; FinCEN filing-info cite is a weak link for "advisories" specifically. Good L4 grain. |
| business-capabilities/L4-sanctions-list-curation.md | 5 | 5 | 5 | 5 | 5 | Good-guy/whitelist governance, OFAC 50% Rule, OFAC Framework internal-controls all accurate and grounded in OFAC primary sources. Strong atomic L4. |
| business-processes/customer-due-diligence-onboarding.md | 5 | 4 | 5 | 5 | 4 | End-to-end CDD onboarding flow coherent; CIP→UBO→screen→rate→EDD→approve→establish is sensible ordering. FATF R.10/12 cited via secondary (Thomson Reuters/First AML/Trulioo) blogs — adequate for process, not primary. |
| business-processes/sanctions-screening-operations.md | 4 | 4 | 5 | 5 | 4 | Exact/fuzzy matching, three-tier triage, 10-business-day report VERIFIED correct (31 CFR 501.603/604). "Preponderance standard" phrasing for hit resolution is reasonable. Flow well-formed. |
| process-flows/customer-due-diligence-onboarding/01-capture-cip-data.md | 4 | 3 | 5 | 4 | 5 | Single-action step, correct grain. Details thin/near-boilerplate ("captures applicant data... controls include CIP minimum-data, data quality, consent"). Sources are CDD-overview blogs, adequate. |
| process-flows/customer-due-diligence-onboarding/05-trigger-enhanced-diligence.md | 5 | 4 | 5 | 4 | 5 | Correct EDD decision point (PEP, source of wealth/funds). Grounded in Trulioo EDD source. Clean step grain. |
| process-flows/sanctions-screening-operations/01-match-against-watchlist.md | 5 | 4 | 5 | 4 | 5 | OFAC/UN/EU exact+fuzzy match, OFAC 50% rule control accurate. Single-action grain correct. Sources adequate. |
| process-flows/sanctions-screening-operations/04-resolve-sanctions-hit.md | 4 | 3 | 5 | 4 | 4 | Correct decision-point grain. Details are generic/near-boilerplate; "preponderance standard" for sanctions true-match adjudication is asserted but neither cited source clearly establishes that exact legal standard for OFAC hit resolution. |
| process-flows/regulatory-change-management/01-scan-regulatory-change.md | 4 | 3 | 5 | 4 | 4 | Horizon-scan single action correct. Details boilerplate; both sources are vendor blogs (BeInformed, Finreg-e) — thin grounding but topic-appropriate. NOTE: parent process "Regulatory Change Management" differs from the L3 capability name "Regulatory Change Compliance" — confirm registry consistency. |
| concepts/sar-filing.md | 5 | 5 | 5 | 5 | 5 | FinCEN Form 111, BSA E-Filing, 30-day (60 if no subject) deadline, tipping-off, 5-year retention all accurate and grounded in FinCEN SAR FAQ. Exemplary artifact note. |
| concepts/mlro.md | 4 | 4 | 5 | 4 | 4 | MLRO accountability, reasonable-grounds standard, 30/60-day filing, FIU liaison accurate. Alias "BSA/AML Compliance Officer" conflates the UK MLRO role with the US BSA Officer — defensible as alias but loosely equivalent. References list FATF R.20 / Wolfsberg not in frontmatter sources (minor frontmatter/References mismatch). |

## Per-dimension means

- Definitional accuracy: (4+5+5+5+4+4+5+4+4+5+2+5+5+4+5+4+5+5+5+5+4+4+5+5+4+4+5+4) / 28 = **125 / 28 = 4.46**
- Groundedness: (4+4+5+4+3+3+5+4+4+5+2+5+5+3+4+4+5+4+5+4+4+3+4+4+3+3+5+4) / 28 = **111 / 28 = 3.96**
- Relationship sensibility: (4+4+5+5+4+4+5+4+3+5+4+5+5+5+5+4+5+5+5+5+5+5+5+5+5+5+5+5) / 28 = **130 / 28 = 4.64**
- Canonical-naming fidelity: (4+4+5+4+4+4+4+4+5+5+4+5+5+4+5+5+5+5+5+5+5+4+4+4+4+4+5+4) / 28 = **124 / 28 = 4.43**
- Granularity fit: (4+4+4+4+4+4+4+4+4+4+4+4+4+4+4+5+5+5+4+4+5+5+5+4+4+4+5+4) / 28 = **121 / 28 = 4.32**

## Verdict: FAIL

Two gate conditions:
1. Mean >= 4.0 on every dimension — FAILS on **Groundedness (3.96 < 4.0)**.
2. No individual note <3 on Groundedness or Relationship sensibility — FAILS: `L2-financial-crime-risk-compliance.md` scores **2 on both Definitional accuracy and Groundedness**.

Either condition alone fails the gate. The L2 note must be fixed and re-judged before this domain can be marked `done`.

## Required fixes

- **L2-financial-crime-risk-compliance.md (blocking):** The "harmonised list of 22 predicate offences" and "criminal liability for legal persons" belong to the criminal-law 6AMLD = **Directive (EU) 2018/1673**, not Directive (EU) 2024/1640. Either (a) re-cite 2018/1673 for the predicate-offence/criminal-liability claims, or (b) rewrite the Details to describe what 2024/1640 actually governs (the 2024 AML-package institutional/supervisory framework alongside the AMLR and AMLA). Disambiguate the "AMLD6" alias. Re-judge after fix.
- **L3-alert-management.md:** Remove or source the ">90% false-positive rate" figure — it is not supported by the cited Wolfsberg/FinCEN pages. Cite a study that establishes it or soften to "frequently very high."
- **04-resolve-sanctions-hit.md / sanctions-screening-operations.md:** "Preponderance standard" for sanctions true-match adjudication is asserted without a supporting source; either cite a standard (OFAC/Oracle disposition guidance) or replace with neutral wording (e.g., "documented true-match/false-positive determination").
- **regulatory-taxonomy-manager.md & data-lineage-tracker.md:** Replace or supplement blog/Medium sources with primary vendor or standards docs (EBA DPM/XBRL spec; BCBS 239 text for the lineage/traceability claim).
- **01-scan-regulatory-change.md (naming):** Confirm the parent process id "Regulatory Change Management" is the registered process backing the L3 capability "Regulatory Change Compliance"; align names if they are meant to be the same flow.
- **mlro.md (minor):** References list (FATF R.20, Wolfsberg) is not reflected in frontmatter `sources`; align. Consider clarifying that "BSA/AML Compliance Officer" is the US analogue, not an exact synonym.
- **kyc-onboarding-platform.md (minor):** "NICE Actimize CDD" named in Details has no cited source; either cite or drop.
