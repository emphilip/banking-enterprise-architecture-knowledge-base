# LLM-Judge Report — Risk Management Deep-Dive

Judge: strict EA knowledge-base reviewer. Date: 2026-06-16.
Sample: 28 representative new Risk Management notes. Rubric: `evals/rubric.md`.
Scores 1-5 per dimension (3 = acceptable, <3 = fail).

Corroboration performed (load-bearing claims):
- SR 26-2 is a real Fed/OCC/FDIC supervisory letter (issued 2026-04-17) superseding SR 11-7 — confirmed via federalreserve.gov; ValidMind SR 26-2 alignment confirmed via ValidMind blog.
- Basel III output floor = 72.5% of standardised RWA; SA-CCR alpha = 1.4 on (RC + PFE) — confirmed (BIS d424 summary, EBF).
- IBM acquired Algorithmics (Toronto) in 2011 for ~USD 387m — confirmed (PR Newswire, CBC).
- BCBS doc IDs: d450 = Stress Testing Principles (2018), d328 = Corporate Governance Principles for Banks (2015), d292 = PSMOR — confirmed (BIS).
- Registry (`glossary/_canonical-names.md`) confirms supersedes pairs are same-capability: Murex MX.3 Risk / FIS Adaptiv (both Risk Analytics Engine); ServiceNow IRM / Archer IRM (both GRC Platform). Relationship targets (Stress Testing Engine, Model Inventory Registry, Loss Event Register, Enterprise Risk Management, Regulatory Capital Adequacy) all exist as registry entries.

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|---|---|---|---|---|---|---|
| technology-capabilities/risk-analytics-engine.md | 5 | 4 | 5 | 5 | 4 | Accurate VaR/ES/PFE/XVA definition; vendors (SAS, OFSAA, Algo, Adaptiv, Murex, MSCI, Numerix) all match registry; cited sources support the engine claims. |
| technology-capabilities/risk-data-aggregation.md | 5 | 4 | 5 | 5 | 4 | Correct BCBS 239 framing; the 3rd source is a SAS RDARR product page but body discusses Moody's RiskAuthority/Quantexa — minor source/claim mismatch, core BCBS 239 claims grounded. |
| technology-capabilities/model-risk-management-platform.md | 5 | 5 | 5 | 5 | 4 | SR 11-7 / SR 26-2 framing accurate and corroborated; ValidMind/ModelOp match registry; sources relevant. |
| technology-capabilities/governance-risk-and-compliance-platform.md | 5 | 4 | 5 | 5 | 4 | IRM/GRC + RCSA definition correct; OpenPages/Archer/ServiceNow/MetricStream match registry; sources support. |
| technology-capabilities/market-risk-engine.md | 5 | 4 | 5 | 5 | 5 | FRTB SA/IMA, PLA, VaR/ES accurate; derived_from Risk Analytics Engine correct grain; vendors cited. |
| technology-capabilities/model-validation-workbench.md | 5 | 4 | 5 | 5 | 5 | SR 11-7 effective-challenge / SR 26-2 framing correct; depends_on Model Inventory Registry valid (registry entry exists); derived_from MRM Platform correct. |
| technology-capabilities/risk-control-self-assessment-engine.md | 5 | 4 | 5 | 5 | 5 | RCSA cycle accurate; derived_from GRC Platform and depends_on Loss Event Register / Workflow Orchestration all valid registry targets. |
| systems/legacy/oracle-ofsaa.md | 5 | 5 | 5 | 5 | 4 | OFSAA modular apps + FSDF data foundation accurate; Oracle docs sources relevant; depends_on direction (Risk Analytics Engine depends on OFSAA) matches registry. |
| systems/legacy/ibm-algorithmics.md | 5 | 5 | 5 | 5 | 4 | 2011 IBM acquisition, Toronto origin, Algo Risk/Algo One all corroborated; related_to FIS Adaptiv sensible (same Risk Analytics Engine peer set). |
| systems/modern/murex-mx3-risk.md | 5 | 4 | 5 | 5 | 4 | VaR/ES/FRTB/SA-CCR/XVA accurate; supersedes FIS Adaptiv is same-capability (registry confirms; note omits OFSAA but that is a subset, acceptable). |
| systems/modern/servicenow-irm.md | 5 | 4 | 5 | 5 | 4 | Now Platform IRM modules accurate; supersedes Archer IRM is same-capability (both GRC Platform per registry). |
| systems/modern/validmind.md | 5 | 5 | 5 | 5 | 4 | AI-first MRM, SR 11-7/SR 26-2 alignment corroborated; depends_on direction matches registry; ValidMind docs sources relevant. |
| business-capabilities/L2-risk-appetite-management.md | 5 | 5 | 5 | 5 | 5 | COSO ERM + BCBS d328 framing accurate; derived_from Enterprise Risk Management correct; depends_on tech caps (right direction). |
| business-capabilities/L2-stress-testing-management.md | 5 | 5 | 5 | 5 | 5 | BCBS d450 + CCAR/DFAST nine-quarter CET1 projection accurate; relationships correct grain. |
| business-capabilities/L3-risk-capital-calculation.md | 5 | 5 | 5 | 5 | 5 | Basel CRE20/CRE30, FRTB, SMA BIC×ILM, 72.5% output floor all accurate/corroborated; derived_from Regulatory Capital Adequacy correct. |
| business-capabilities/L3-credit-exposure-management.md | 5 | 4 | 5 | 5 | 5 | SA-CCR EAD = 1.4×(RC+PFE) (CRE52) accurate; BIAN cited though "Position Keeping" mapping is loosely supported by the generic landscape link. |
| business-capabilities/L3-counterparty-credit-risk.md | 5 | 5 | 5 | 5 | 4 | SA-CCR + CVA (d325) accurate; derived_from Market Risk Management matches registry parent for Counterparty Credit Risk. |
| business-capabilities/L3-lcr-and-nsfr-management.md | 5 | 5 | 5 | 5 | 5 | LCR (d238, ≥100%, L1/L2A/L2B haircuts, 40%/15% caps) and NSFR (d295) accurate; derived_from Liquidity Risk Management correct. |
| business-capabilities/L4-limit-and-exposure-management.md | 5 | 5 | 5 | 5 | 5 | Large Exposures (d283) 25% Tier 1 / 15% G-SIB cap accurate; derived_from Credit Exposure Management matches registry; atomic L4 grain. |
| business-capabilities/L4-key-risk-indicator-monitoring.md | 5 | 4 | 5 | 5 | 5 | BCBS d292 PSMOR framing correct; KRI examples concrete (not boilerplate); derived_from Risk & Control Self-Assessment matches registry. |
| business-processes/stress-testing.md | 5 | 4 | 5 | 5 | 5 | End-to-end flow coherent; SR 11-7/OCC 2011-12 + CCAR/DFAST accurate; depends_on Market Risk Management matches registry; Wikipedia source acceptable for process overview. |
| process-flows/stress-testing/01-design-stress-scenario.md | 4 | 3 | 5 | 5 | 5 | Single action, correct order/causes; thin single non-authoritative source but claims are obvious process facts. |
| process-flows/stress-testing/05-obtain-board-approval.md | 4 | 4 | 5 | 5 | 5 | Single board sign-off action; Fed CCAR Q&A source supports board/capital-plan claim; correct causes Submit Capital Plan. |
| process-flows/risk-appetite-setting/01-define-risk-capacity.md | 5 | 5 | 5 | 5 | 5 | Risk-capacity vs appetite distinction correct; FSB RAF principles source is authoritative and relevant. |
| process-flows/risk-appetite-setting/04-approve-risk-appetite.md | 5 | 5 | 5 | 5 | 5 | Board/committee approval step correct; FSB + governance source relevant; correct causes Embed Appetite Limits. |
| process-flows/fraud-detection/01-ingest-transaction-stream.md | 4 | 3 | 5 | 5 | 5 | Single ingestion action; only a vendor-blog source but claims are generic/obvious for the step. |
| process-flows/fraud-detection/04-apply-detection-block.md | 4 | 3 | 5 | 5 | 5 | Decision-point step well-scoped; single vendor-blog source, generic but obvious claims. |
| concepts/risk-appetite-statement.md | 5 | 5 | 5 | 5 | 5 | FSB RAF + BCBS d328 framing accurate; artifact-level definition appropriate; relationships sensible. |

## Per-dimension means (n = 28)

- Definitional accuracy: 4.82
- Groundedness: 4.36
- Relationship sensibility: 5.00
- Canonical-naming fidelity: 5.00
- Granularity fit: 4.64

## Verdict

**PASS.**

- Gate condition 1 — mean ≥ 4.0 on every dimension: met (lowest is Groundedness at 4.36).
- Gate condition 2 — no individual note scoring <3 on Groundedness or Relationship sensibility: met (lowest Groundedness note = 3; lowest Relationship note = 5).

## Recommended fixes (non-blocking, all above the <3 fail line)

- `technology-capabilities/risk-data-aggregation.md`: the 3rd source is labelled "SAS Risk Data Aggregation and Reporting" but points to a financialit.net product page while the body discusses Moody's RiskAuthority and Quantexa. Either add a RiskAuthority/Quantexa source or relabel/align the citation to the vendors actually discussed.
- `process-flows/fraud-detection/01-ingest-transaction-stream.md` and `04-apply-detection-block.md`: both rely on a single vendor blog (getfocal.ai). Add one neutral/authoritative reference (e.g. real-time fraud-scoring or streaming-architecture guidance) to lift Groundedness off the floor.
- `process-flows/stress-testing/01-design-stress-scenario.md`: scenario-design step cites only a single non-authoritative knowledge-base page; consider citing the BCBS d450 or Fed CCAR scenario-design source already used by sibling notes.
- `business-capabilities/L3-credit-exposure-management.md`: the BIAN "Position Keeping" service-domain mapping is supported only by the generic BIAN landscape link; cite the specific BIAN service domain to firm up the mapping claim.
