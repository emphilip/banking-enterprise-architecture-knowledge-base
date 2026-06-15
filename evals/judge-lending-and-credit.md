# LLM-Judge Report — Lending & Credit deep-dive (30-file sample)

Judge: strict EA knowledge-base reviewer. Date: 2026-06-15.
Method: each file read in full; URLs in `sources`/References fetched or
cross-checked via web search. Scores 1–5 per rubric dimension
(`evals/rubric.md`). Gate: mean ≥ 4.0 every dimension AND no individual note
scoring <3 on Groundedness or Relationship sensibility.

Source-verification notes used across the sample:
- BIAN service domains **Disbursement, Repayment, Collateral Asset Administration,
  Delinquent Account Handling, Customer Credit Rating, MortgageLoan, Credit
  Facility** confirmed to exist in the BIAN Service Landscape (bian.org;
  dev.bian.org/semantic-apis/disbursement, collateral-asset-administration;
  servicelandscape-10-0-0 Customer Credit Rating).
- Experian PowerCurve Originations global availability 2013 + value-based/
  profitable-acquisition framing confirmed (experianplc / prnewswire 2013).
- Reg Z 1026.53: excess-over-minimum applied to highest-APR balance first —
  confirmed (ecfr/law.cornell/CFPB).
- UCP 600 Art 14(b): maximum five banking days to examine — confirmed.
- Temenos Infinity Origination omni-channel, cloud, instant multi-factor
  decisioning lifting auto-decision rates — confirmed (temenos.com).
- Provenir cloud-native, low/no-code AI decisioning across lifecycle — confirmed
  (provenir.com/platform).
- nCino LOS booking to core banking / account creation — confirmed (ncino.com).

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|------|----------|----------|-----|--------|------|-------|
| systems/legacy/ellie-mae-encompass.md | 4 | 3 | 4 | 4 | 4 | Definition correct (ICE/Ellie Mae); but "on-premise/not cloud-native" framing is contradicted by ICE's current "Encompass Digital Lending Platform" cloud positioning, and cited sources are generic LOS blogs, not ICE docs. |
| systems/legacy/finastra-laserpro.md | 4 | 4 | 4 | 4 | 4 | Documentation-centric origination platform for community banks/CUs aligns with finastra.com/lending/origination; "related to Ellie Mae" is a weak but acceptable peer link. |
| systems/legacy/fico-origination-manager.md | 4 | 3 | 4 | 4 | 4 | Scorecards+rules+value-based offers plausible but the single cited source is a Slashdot comparison page, not FICO product doc; claims only loosely anchored. |
| systems/legacy/experian-powercurve.md | 5 | 5 | 4 | 4 | 4 | Component-based decisioning + 2013 PowerCurve Originations global availability both confirmed by experianplc press release. |
| systems/modern/temenos-origination.md | 5 | 5 | 5 | 5 | 4 | Omni-channel cloud + instant multi-factor decisioning + auto-decision lift confirmed by temenos.com. supersedes legacy LOS (Encompass/LaserPro) is correct grain. |
| systems/modern/meridianlink.md | 4 | 4 | 3 | 4 | 4 | Cloud LOS for CU/community banks + bureau integrations supported by vendor guide. `supersedes Ellie Mae Encompass` is questionable: MeridianLink Consumer is consumer LOS, Encompass is mortgage LOS — not strictly same-capability supersede. |
| systems/modern/provenir.md | 5 | 5 | 5 | 5 | 4 | Cloud-native no-code AI decisioning confirmed by provenir.com. supersedes FICO Origination Manager + PowerCurve = same decisioning capability, correct. |
| technology-capabilities/credit-scoring-service.md | 4 | 4 | 4 | 4 | 4 | Scorecards+ML scoring grounded in Provenir/Neontri; `derived_from Credit Decisioning Engine`, `depends_on ML Platform` sensible directions. |
| technology-capabilities/affordability-assessment-engine.md | 4 | 4 | 4 | 4 | 4 | DTI/income/stress framing supported by Inscribe underwriting source; relationships sensible. |
| technology-capabilities/decision-rules-engine.md | 5 | 4 | 5 | 4 | 4 | Strategy trees/cut-offs grounded in Provenir + PowerCurve; `depends_on Credit Scoring Service` correct direction. |
| technology-capabilities/offer-and-pricing-engine.md | 4 | 4 | 4 | 4 | 4 | Risk-based pricing/offer generation tied to PowerCurve Originations value-based offers; `derived_from Loan Origination Platform` acceptable. |
| technology-capabilities/disbursement-engine.md | 4 | 4 | 4 | 4 | 4 | Booking/funding/core hand-off confirmed by nCino booking-to-core source; `depends_on Core Banking Processing` correct. |
| business-capabilities/L3-loan-pricing.md | 5 | 5 | 5 | 5 | 4 | BIAN Credit Facility maps to priced terms; TILA/Reg Z disclosure + risk-based-pricing notice are accurate, source-anchored banking specifics. |
| business-capabilities/L3-loan-disbursement.md | 5 | 5 | 5 | 5 | 4 | BIAN Disbursement domain confirmed; TRID 3-business-day pre-funding wait accurate (CFPB TRID). |
| business-capabilities/L3-repayment-processing.md | 5 | 4 | 5 | 4 | 4 | BIAN Repayment domain confirmed; allocation-waterfall + delinquency hand-off accurate. APQC source generic but BIAN claim carries it. |
| business-capabilities/L3-collateral-valuation.md | 5 | 5 | 5 | 5 | 4 | BIAN Collateral Asset Administration confirmed; USPAP + Dodd-Frank/Reg Z appraiser-independence accurate, source-anchored. |
| business-capabilities/L3-delinquency-management.md | 5 | 5 | 5 | 4 | 4 | BIAN Delinquent Account Handling confirmed; DPD buckets + 90+ NPL classification accurate. |
| business-capabilities/L4-credit-bureau-retrieval.md | 4 | 5 | 4 | 4 | 4 | BIAN Customer Credit Rating confirmed; FCRA permissible purpose + hard inquiry accurate. `derived_from Affordability Assessment` is a slightly odd parent (bureau pull feeds scoring more than affordability) but defensible. |
| business-capabilities/L4-escrow-administration.md | 4 | 5 | 4 | 4 | 4 | RESPA/Reg X annual escrow analysis + cushion accurate. Mapping to BIAN MortgageLoan is loose (escrow is a servicing function) though MortgageLoan domain does exist. |
| business-capabilities/L4-payment-allocation.md | 5 | 5 | 5 | 5 | 5 | BIAN Repayment + Reg Z 1026.53 highest-APR-first rule both confirmed verbatim; atomic L4 grain. |
| business-capabilities/L4-repossession-management.md | 5 | 5 | 5 | 5 | 5 | UCC Art 9 commercially-reasonable disposal + deficiency/surplus notice accurate; BIAN Collection/Recovery mapping sensible. |
| process-flows/loan-origination-workflow/01-capture-loan-application.md | 4 | 4 | 5 | 5 | 5 | Single intake action; `causes Pre-Qualify Borrower`, `depends_on Loan Origination Platform` correct. Generic LOS-workflow sources but claims are modest/obvious. |
| process-flows/loan-origination-workflow/05-render-loan-decision.md | 4 | 4 | 5 | 5 | 5 | Approve/decline/refer branch + emits Credit Decision Issued Event correct grain; `depends_on Credit Decisioning Engine` correct. |
| process-flows/credit-underwriting/01-pull-credit-report.md | 4 | 4 | 5 | 4 | 5 | FCRA permissible-purpose control accurate; single action. Sources are "5 Cs" blogs (generic) but the FCRA control is correct and widely supported. |
| process-flows/credit-underwriting/04-evaluate-collateral.md | 4 | 3 | 4 | 4 | 5 | LTV/lien-perfection controls correct, but `depends_on Credit Decisioning Engine` is a weak fit for a collateral-valuation step (Collateral Valuation capability would be the right dependency), and the two "5 Cs" blog sources don't anchor the collateral-specific controls. |
| process-flows/mortgage-origination/01-take-mortgage-application.md | 5 | 4 | 5 | 5 | 5 | URLA/Form 1003 intake accurate; `causes Issue Loan Estimate` correct TRID sequencing. |
| process-flows/mortgage-origination/06-deliver-closing-disclosure.md | 5 | 5 | 5 | 5 | 5 | CD ≥3 business days before consummation + tolerance reconciliation accurate, anchored to CFPB KBYO/TRID FAQ sources. |
| concepts/loan-application.md | 4 | 4 | 4 | 4 | 4 | Accurate artifact description; URLA/1003 cross-reference correct. `mentions` links resolve to real registry nodes. |
| concepts/credit-report.md | 5 | 4 | 4 | 4 | 4 | Tradelines/inquiries/score contents accurate; permissible-purpose/adverse-action framing correct. Sources generic "5 Cs" blogs but content is standard. |
| concepts/letter-of-credit.md | 5 | 5 | 4 | 4 | 4 | UCP 600/ISP98 independence principle + five-banking-day examination accurate (UCP Art 14b). Trade-finance `mentions` links are coherent. |

## Per-dimension means (n=30)

| dimension | mean |
|-----------|------|
| Definitional accuracy | 4.50 |
| Groundedness | 4.30 |
| Relationship sensibility | 4.53 |
| Canonical-naming fidelity | 4.43 |
| Granularity fit | 4.30 |

Computation:
- accuracy sum = 135 → 135/30 = 4.50
- grounded sum = 129 → 129/30 = 4.30
- rel sum = 136 → 136/30 = 4.53
- naming sum = 133 → 133/30 = 4.43
- gran sum = 129 → 129/30 = 4.30

## Verdict

**PASS.**
- Every dimension mean ≥ 4.0 (lowest are Groundedness and Granularity at 4.30).
- No individual note scored <3 on Groundedness or Relationship sensibility
  (lowest on those two gating dimensions = 3).

The gate is met. Notes below scored exactly 3 on a gating dimension (≥ threshold,
so not blocking) but are flagged for improvement.

## Recommended fixes (non-blocking; lift weakest notes)

- **systems/legacy/ellie-mae-encompass.md** (Groundedness 3): the "on-premise /
  not cloud-native" deployment framing is contradicted by ICE's current
  "Encompass Digital Lending Platform" cloud positioning. Either soften to
  "historically on-premise, now offered as a cloud/hosted platform" or cite an
  ICE Mortgage Technology product page rather than two generic LOS-vendor blogs.
- **systems/legacy/fico-origination-manager.md** (Groundedness 3): replace the
  sole Slashdot comparison source with a FICO product/solution page so the
  scorecards+rules+value-based-offer claims are vendor-anchored.
- **process-flows/credit-underwriting/04-evaluate-collateral.md**
  (Groundedness 3): change `depends_on Credit Decisioning Engine` to the
  Collateral Valuation (or Collateral Valuation Service) capability, which is the
  correct dependency for a collateral-evaluation step; and add a
  collateral/appraisal-specific source (e.g. USPAP or an appraisal-process
  reference) since the two cited "5 Cs of credit" blogs do not anchor the
  LTV/lien-perfection controls.
- **systems/modern/meridianlink.md** (Relationship sensibility 3): `supersedes
  Ellie Mae Encompass` pairs a consumer/account-opening LOS with a mortgage LOS.
  Per the rubric, `supersedes` should target a *same-capability* legacy system —
  either retarget to a consumer-lending legacy LOS or replace with a
  `related_to`/`alternative_to` relationship.
- **business-capabilities/L4-escrow-administration.md** (naming/mapping nuance):
  consider mapping to a BIAN servicing-oriented domain rather than `MortgageLoan`
  for escrow administration; MortgageLoan exists but escrow is a servicing
  function, so the current mapping is loose (not failing).
