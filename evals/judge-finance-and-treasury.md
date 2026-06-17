# LLM-Judge Report — Finance & Treasury deep-dive

Reviewer: judge sub-agent (strict). Date: 2026-06-17.
Sample: 28 notes (all exist; none skipped).
Method: read each note + corroborated load-bearing framework/vendor claims against cited or authoritative sources (BCBS d368/d424/d248, IFRS 18/IAS 1, Kyriba, SunGard/FIS, BIAN/APQC). ~6 source lookups used.

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|---|---|---|---|---|---|---|
| technology-capabilities/treasury-management-system.md | 5 | 4 | 5 | 5 | 5 | TMS scope accurate; Kyriba "9,900+ connections"/AI forecasting verified. Minor: Details files AvantGard under "ION Treasury (Wallstreet Suite, Reval, IT2)" but AvantGard went to FIS, not ION. |
| technology-capabilities/asset-liability-management-engine.md | 5 | 5 | 5 | 5 | 5 | IRRBB/EVE/NII/behavioural scope correct; supersedes mapping to QRM/SAS sensible; Risk Analytics Engine is canonical. |
| technology-capabilities/financial-consolidation-platform.md | 5 | 5 | 5 | 5 | 4 | IFRS 10, XBRL/ESEF, intercompany/CTA all correct. Overlaps in scope with child Consolidation Engine but altitude (L1 platform vs L2 engine) is defensible. |
| technology-capabilities/funds-transfer-pricing-engine.md | 5 | 5 | 5 | 5 | 5 | Matched-maturity transfer curve, liquidity/basis/optionality add-ons correct; derived_from ALM Engine right grain. |
| technology-capabilities/period-close-manager.md | 5 | 4 | 5 | 5 | 5 | SAP Financial Closing Cockpit pattern accurate; sources are SAP-blog tier but support the claims. |
| technology-capabilities/consolidation-engine.md | 5 | 5 | 5 | 5 | 4 | Full/equity/proportional method, NCI, CTA, IFRS 10 correct; some overlap with parent platform but appropriate L2 decomposition. |
| systems/legacy/oracle-hyperion-hfm.md | 5 | 5 | 5 | 5 | 5 | HFM as on-prem consolidation incumbent, EPM Cloud successor — accurate and grounded. |
| systems/legacy/sungard-avantgard.md | 5 | 4 | 5 | 5 | 5 | Integrity/Quantum workstations, "now FIS", cloud displacement all verified; single source but corroborated. |
| systems/modern/kyriba.md | 5 | 5 | 5 | 5 | 5 | Cloud Liquidity Performance platform, AI forecasting, supersedes legacy on-prem workstation — verified. supersedes SunGard AvantGard is same-capability. |
| systems/modern/onestream.md | 5 | 5 | 5 | 5 | 5 | Unified CPM, Extensible Dimensionality, FDQ; supersedes HFM/SAP BPC same-capability. |
| systems/modern/empyrean-sol-alm.md | 5 | 5 | 5 | 5 | 5 | Cloud ALM/IRRBB/FTP scope correct; RiskTech100 2025 cited; supersedes QRM/SAS same-capability. |
| business-capabilities/L3-journal-management.md | 5 | 4 | 5 | 5 | 5 | BIAN + APQC PCF 9.x mapping reasonable; "universal journal" continuous-accounting claim well-known. |
| business-capabilities/L3-statutory-reporting.md | 5 | 5 | 5 | 5 | 5 | IAS 1 complete-set + IFRS 18 (eff. 1 Jan 2027, income-statement categories, MPMs) verified accurate. |
| business-capabilities/L3-treasury-cash-positioning.md | 5 | 5 | 5 | 5 | 5 | Nostro/intraday MT940/942, BCBS d248 intraday-liquidity monitoring tools correctly cited. |
| business-capabilities/L3-funds-transfer-pricing-management.md | 5 | 4 | 5 | 5 | 5 | Matched-maturity/liquidity-premium/risk-transfer-to-treasury correct; Ferma source is secondary but supportive. |
| business-capabilities/L3-rwa-calculation.md | 5 | 5 | 5 | 5 | 5 | BCBS d424, 72.5% output floor, CET1/T1/total ratios — all verified correct. |
| business-capabilities/L4-journal-validation-and-control.md | 5 | 5 | 5 | 5 | 5 | SoD, open-period/account edits, top-side sign-off, audit trail — atomic L4, derived_from Journal Management. |
| business-capabilities/L4-eve-sensitivity-analysis.md | 5 | 5 | 5 | 5 | 5 | Six BCBS d368 shock scenarios + 15% Tier 1 outlier test — verified exactly correct. |
| business-capabilities/L4-leverage-ratio-calculation.md | 5 | 5 | 3 | 5 | 5 | Content correct (T1 / exposure measure, SA-CCR, 3% min, G-SIB buffer). REL issue: derived_from RWA Calculation contradicts the note's own (correct) point that LR is non-risk-based — it is a sibling capital metric, not a child of RWA. |
| business-processes/financial-close.md | 5 | 5 | 5 | 5 | 5 | R2R flow, controller ownership, IFRS 10/SOX controls, coherent step chain. |
| business-processes/funds-transfer-pricing.md | 5 | 5 | 5 | 5 | 5 | Curve build -> apply -> attribute flow with ALCO governance; ALM Analyst owner. |
| process-flows/financial-close/01-close-subledgers.md | 5 | 5 | 5 | 5 | 5 | Single action (cut-off + subledger close); event/inputs/outputs/controls coherent. |
| process-flows/financial-close/05-run-consolidation.md | 5 | 5 | 5 | 5 | 5 | Single consolidation action, IFRS 10 control, correct downstream cause. |
| process-flows/regulatory-capital-reporting/01-source-regulatory-data.md | 5 | 5 | 5 | 5 | 5 | GL-to-risk tie-out, COREP context; atomic step. |
| process-flows/regulatory-capital-reporting/04-assemble-capital-return.md | 5 | 5 | 5 | 5 | 5 | COREP/FINREP + FR Y-9C/Y-14 schedules accurate; appropriate step grain. |
| process-flows/funds-transfer-pricing/04-approve-ftp-methodology.md | 5 | 5 | 5 | 5 | 5 | ALCO approval gate, event-raising, governance controls; single action. |
| concepts/trial-balance.md | 5 | 5 | 5 | 5 | 5 | Double-entry proof, unadjusted vs adjusted TB, CoA organisation — accurate. |
| concepts/ftp-curve.md | 5 | 5 | 5 | 5 | 5 | Matched-maturity build from market curves + term-liquidity premium, behavioural tenors, ALCO version/effective date — accurate. |

## Per-dimension means (n=28)

- Definitional accuracy: 5.00
- Groundedness: 4.75
- Relationship sensibility: 4.93
- Canonical-naming fidelity: 5.00
- Granularity fit: 4.86

## Verdict

**PASS.**

- Every dimension mean is >= 4.0 (lowest is Groundedness 4.75).
- No individual note scores <3 on Groundedness or Relationship sensibility (the gate dimensions). The lowest gate score is the leverage-ratio note's REL = 3, which is acceptable (not below 3).
- No FABRICATED framework specifics found: BCBS d368 (six EVE shocks, 15% Tier 1 outlier test), BCBS d424 (72.5% output floor), BCBS d248 (intraday liquidity tools), IAS 1 / IFRS 18 (eff. 1 Jan 2027) all verified correct against authoritative sources. Document numbers and standard names are accurate.

## Recommended fixes (non-blocking; none fail the gate)

- **L4-leverage-ratio-calculation.md** (REL=3): change `derived_from RWA Calculation` to a sibling/sequence relationship under a shared parent (e.g. `derived_from Regulatory Capital Management`, matching RWA Calculation's parent), since the leverage ratio is by design non-risk-based and is not a decomposition of RWA. Currently the only gate-adjacent weakness.
- **treasury-management-system.md** (grounded=4): the Details associates "SunGard AvantGard" with "ION Treasury (Wallstreet Suite, Reval, IT2)". AvantGard moved to FIS, not ION; reword so AvantGard is attributed to SunGard/FIS and only Wallstreet Suite/Reval/IT2 to ION.
- **period-close-manager.md / sungard-avantgard.md / L3-journal-management.md / L3-funds-transfer-pricing-management.md** (grounded=4): claims are correct but lean on vendor-blog/secondary sources; consider adding a primary source (SAP Help, FIS product page, BIAN/APQC element id) to strengthen grounding. Not required for PASS.
