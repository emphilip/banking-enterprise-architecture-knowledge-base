# LLM-Judge Report — Wealth & Investments deep-dive

Reviewer: judge sub-agent. Date: 2026-06-16. Sample: 26 files (representative).
Sources corroborated via WebSearch/WebFetch: BIAN Service Landscape, DTCC T+1 best
practices, Addepar Advent Converter (RIABiz/WealthManagement), CFA Institute, ESMA MiFID II.

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|---|---|---|---|---|---|---|
| technology-capabilities/portfolio-management-system.md | 5 | 4 | 5 | 5 | 5 | IBOR/front-to-back def accurate; vendor claims (Aladdin, SimCorp One, Geneva, Global Plus) all sourced or corroborated. |
| technology-capabilities/order-management-system.md | 5 | 5 | 5 | 5 | 5 | Buy-side OMS/EMS, FIX routing, T+1 affirmation all accurate and sourced (Bloomberg/CRD/SS&C). |
| technology-capabilities/investment-advisory-platform.md | 4 | 4 | 5 | 5 | 4 | Def sound; "InvestCloud (NaviPlan)" correct (InvestCloud acquired NaviPlan); GenAI dependency is forward-looking but plausibly sourced. |
| technology-capabilities/rebalancing-engine.md | 5 | 5 | 5 | 5 | 5 | Drift/trade-to-band/SMA-UMA and tax-aware constraints accurate; Limina/Envestnet/Bloomberg sourced. L2 derived_from PMS correct. |
| technology-capabilities/securities-settlement-processor.md | 5 | 4 | 5 | 5 | 5 | Post-trade/affirmation/SSI/CSD/DVP accurate; T+1 framing corroborated. derived_from OMS correct. |
| technology-capabilities/robo-advisory-engine.md | 5 | 4 | 5 | 5 | 5 | Automated/hybrid advice def accurate; Temenos/Comarch sourced; hands weights to Rebalancing Engine is sensible. |
| systems/modern/blackrock-aladdin.md | 5 | 5 | 5 | 5 | 5 | Front-to-back, common data language, API-first all per BlackRock docs. supersedes Geneva/Asset Arena = same-capability (portfolio accounting/IBOR). |
| systems/modern/charles-river-ims.md | 5 | 5 | 5 | 5 | 5 | OMS/EMS + State Street Alpha accurate; supersedes Advent Moxy is correct OMS->OMS. |
| systems/modern/addepar.md | 4 | 3 | 3 | 4 | 5 | "Advent Converter" is real but targets Advent APX/Axys/PortfolioCenter (RIA recordkeeping), NOT Geneva; supersedes Geneva is mis-targeted on the load-bearing migration claim. |
| systems/legacy/temenos-wealthsuite.md | 4 | 4 | 4 | 4 | 5 | Robo/advisory def sourced. Note: classed legacy-system yet is a current Temenos product positioned as modernization baseline — defensible but borderline. |
| systems/legacy/ssandc-advent-moxy.md | 5 | 5 | 5 | 5 | 5 | Desktop OMS for order generation/modelling accurate; related_to Geneva correct; superseded-by integrated platforms consistent with CRD note. |
| systems/legacy/fis-global-plus.md | 5 | 4 | 5 | 5 | 5 | Multi-currency trust/portfolio accounting IBOR accurate; "Unity Powered by Global Plus" alias plausible; Cutter trust-accounting source apt. |
| business-capabilities/L3-portfolio-construction.md | 5 | 4 | 5 | 5 | 5 | Maps to BIAN Investment Portfolio Planning (valid domain); CFA construction source apt; derived_from Portfolio Management correct. |
| business-capabilities/L3-financial-planning-advisory.md | 5 | 4 | 5 | 5 | 5 | Honestly hedges that holistic planning "extends beyond BIAN's retail core" rather than over-claiming a domain; CFA-grounded. Good restraint. |
| business-capabilities/L3-order-management.md | 5 | 5 | 5 | 5 | 5 | BIAN Trade Order domain valid; T+1 allocation/affirmation timing corroborated by DTCC source. |
| business-capabilities/L3-corporate-actions-processing.md | 5 | 4 | 5 | 5 | 5 | BIAN Corporate Action domain valid; mandatory vs voluntary, ex/pay-date, DTCC scrubbing accurate. |
| business-capabilities/L4-allocation-optimisation.md | 5 | 5 | 5 | 5 | 5 | Mean-variance/efficient frontier + real-world constraints accurate per CFA; atomic L4; derived_from Asset Allocation correct. |
| business-capabilities/L4-cost-basis-tracking.md | 4 | 4 | 4 | 3 | 5 | Tax-lot/FIFO/spec-id, 1099-B covered-securities, wash-sale all accurate (IRS Pub 550). BIAN domain is "Securities Position Keeping" — note says "Securities Position Management" (naming drift). |
| business-capabilities/L4-trade-affirmation.md | 5 | 5 | 5 | 5 | 5 | 9pm ET TD cutoff, May-2024 T+1, CTM/TradeSuite, BIAN Trade Confirmation Matching all corroborated. Atomic L4. |
| business-processes/trade-order-management.md | 5 | 4 | 5 | 5 | 5 | Capture->settle lifecycle, controls and actors accurate; flow edges coherent; T+1 framing sourced. |
| business-processes/portfolio-rebalancing.md | 5 | 4 | 5 | 5 | 5 | Drift->IPS->compliance->four-eyes->orders flow coherent; tax-lot/wash-sale controls accurate; FPA/Vanguard sources apt. |
| process-flows/portfolio-rebalancing/01-measure-portfolio-drift.md | 5 | 4 | 5 | 5 | 5 | Single atomic action (quantify drift vs IPS); causes Evaluate Drift Threshold; right altitude. |
| process-flows/trade-order-management/01-capture-order.md | 5 | 4 | 5 | 5 | 5 | Single action (capture Order Ticket into OMS); causes Validate Order; correct grain. |
| process-flows/trade-order-management/05-confirm-trade.md | 4 | 4 | 4 | 5 | 4 | Action correct but Details are thin/near-boilerplate ("confirms fills... issues Trade Confirmation"); aliases conflate confirm vs affirm (distinct steps). |
| process-flows/financial-planning/04-confirm-suitability.md | 5 | 5 | 5 | 5 | 5 | Suitability/best-interest branch accurate; MiFID II (ESMA) + Reg BI cited correctly; suitable/revise loop right grain. |
| concepts/investment-policy-statement.md | 5 | 4 | 5 | 5 | 5 | IPS components (objectives, SAA + ranges, constraints, benchmark, rebalancing policy) accurate; ties to drift/compliance/reporting coherent. |

## Per-dimension means (n=26)

- Definitional accuracy: **4.81**
- Groundedness: **4.27**
- Relationship sensibility: **4.77**
- Canonical-naming fidelity: **4.81**
- Granularity fit: **4.92**

## Verdict: **PASS**

- All five dimension means >= 4.0 (lowest is Groundedness at 4.27).
- No individual note scored <3 on Groundedness or Relationship sensibility (the two gating dimensions). The lowest gating scores are 3 (Addepar relationship/groundedness; cost-basis naming is on a non-gating dimension), which meets the "no note <3" bar exactly.
- Gate satisfied. Domain may be marked `done` after addressing the recommended fixes below (none are gate-blocking, but several are factual corrections).

## Required / recommended fixes (non-gate-blocking)

- **systems/modern/addepar.md** — `supersedes SS&C Advent Geneva` is mis-targeted. Addepar's "Advent Converter" migration path targets Advent **APX / Axys / PortfolioCenter** (RIA portfolio recordkeeping), not Geneva (institutional/hedge-fund accounting). Either (a) retarget the supersedes edge / Details to Advent APX or Axys, or (b) drop the implied Geneva-specific migration claim and keep Geneva only as a generic legacy reference. Verify the `Broadridge Portfolio Master` supersedes edge has a source; currently unsupported.
- **business-capabilities/L4-cost-basis-tracking.md** — BIAN domain name drift: the note maps to "Securities Position **Management**"; the canonical BIAN service domain is "Securities Position **Keeping**". Correct the domain name (twice in the file) to match BIAN.
- **process-flows/trade-order-management/05-confirm-trade.md** — Details are near-boilerplate; expand minimally (counterparty/broker confirmation vs custodian affirmation, matching platform). Also reconcile aliases: "Affirm Trade Step" conflates confirmation with affirmation, which the W&I model treats as a distinct downstream activity (see L4-trade-affirmation). Tighten to confirmation only.
- **systems/legacy/temenos-wealthsuite.md** — `type: legacy-system`/`maturity: legacy` for a currently marketed Temenos product is borderline. Confirm this classification is intentional (modernization-baseline framing) vs. should be `modern-system`; if kept as legacy, the Details framing already supports it.
- **technology-capabilities/investment-advisory-platform.md** — The `depends_on Generative AI Platform` edge reflects an emerging, not core, dependency; consider `related_to` or annotate as emerging to avoid over-stating a hard dependency.

## Notes on method

- BIAN service domains referenced (Investment Portfolio Planning, Trade Order, Corporate Action, Trade Confirmation Matching) confirmed as valid BIAN landscape domains. "Securities Position Keeping" is the canonical name (cost-basis note used "Management").
- DTCC T+1 facts (9:00 PM ET TD affirmation cutoff, 7:00 PM ET allocation, May 2024 effective, CTM/TradeSuite, 90% target) corroborated.
- Did not exhaustively fetch every URL (budget); ~4 targeted lookups corroborated the highest-risk vendor/framework claims.
