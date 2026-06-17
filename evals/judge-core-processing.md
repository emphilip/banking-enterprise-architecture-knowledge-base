# LLM-Judge Results — Core Processing (Technology-only run)

Run scope: 26 new L3 technology sub-capabilities + 12 systems. Sample judged: 22 files
(15 technology-capabilities, 4 legacy systems, 3... see table — actually 3 legacy + 4 modern systems).
Date: 2026-06-17. Reviewer: judge sub-agent (strict).

Corroboration performed (1-2 lookups/file, batched): Orion AUA/Denali/Redtail (confirmed
$5.8T AUA, Denali AI, Redtail acq. 2022); FlexONE gRPC/Scala + "Best Buy-Side OMS 2026"
(confirmed, A-Team TradingTech Insight Europe 2026); Avaloq NEC ownership + SaaS/BPaaS
(confirmed, NEC 100% by 2021); Calypso/AxiomSL→Adenza→Nasdaq + cross-asset front-to-back
(confirmed); Fidessa sell-side OMS, ION, 6,500/600/100 figures (confirmed). ISO 8583 MTI/DE,
Brinson-Fachler formulas, IFRS 9 hedge mechanics checked against general knowledge + cited docs.

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|---|---|---|---|---|---|---|
| technology-capabilities/iso-8583-message-switch.md | 5 | 5 | 5 | 5 | 5 | MTI/bitmap/DE/STAN-RRN detail accurate; derived_from Card Transaction Switch + related Card Authorization Engine sensible. |
| technology-capabilities/network-token-service.md | 5 | 5 | 5 | 5 | 5 | EMVCo/DPAN/ID&V/lifecycle accurate; VTS/MDES sourced; parent Card Tokenization Service + related Token Vault Manager correct. |
| technology-capabilities/token-vault-manager.md | 5 | 5 | 5 | 5 | 4 | De-tokenisation/PCI-scope accurate; sibling-pair with Network Token Service well-bounded, slight conceptual overlap but distinct (vault vs scheme connector). |
| technology-capabilities/document-splitting-engine.md | 5 | 5 | 5 | 5 | 5 | SAP S/4HANA document-split item-category/inheritance accurate and sourced; derived_from Accounting Rules Engine sensible. |
| technology-capabilities/repricing-gap-engine.md | 5 | 4 | 5 | 5 | 5 | Gap/EaR mechanics correct; AFME IRRBB cite supports framing; derived_from IRRBB Analytics Engine sensible. |
| technology-capabilities/transfer-curve-engine.md | 5 | 4 | 5 | 5 | 5 | Matched-maturity FTP/TLP accurate, Oracle FTP doc supports; derived_from Funds Transfer Pricing Engine correct. |
| technology-capabilities/brinson-attribution-service.md | 5 | 5 | 5 | 5 | 5 | Brinson-Fachler allocation/selection/interaction formulas correct; geometric linking noted; parent Performance & Attribution Engine sensible. |
| technology-capabilities/gips-composite-service.md | 5 | 3 | 5 | 5 | 4 | Definition/GIPS mechanics correct, but cited sources (Softpak attribution blog, Wikipedia perf-attribution) are about attribution, not GIPS composites — weak fit for the load-bearing GIPS claims. |
| technology-capabilities/fix-order-gateway.md | 5 | 5 | 5 | 5 | 5 | FIX session/MsgType detail (D/G/8) accurate; TT & FlexTrade cited; derived_from Execution Management Service + related Order Routing Engine sensible. |
| technology-capabilities/beneficiary-verification-service.md | 5 | 4 | 5 | 5 | 5 | CoP/fuzzy-match/APP-fraud control accurate; J.P. Morgan validation guide supports; derived_from Payment Validation Engine sensible. |
| technology-capabilities/hedge-accounting-service.md | 5 | 3 | 5 | 5 | 5 | IFRS 9 economic-relationship test, CFH/FVH mechanics accurate, but the two cited sources are generic TMS overviews (HighRadius, AFP glossary) that do not substantiate the IFRS 9 hedge-accounting specifics. |
| technology-capabilities/product-catalog-service.md | 5 | 5 | 5 | 5 | 5 | Config-driven catalogue/effectivity/cloning accurate; FLEXCUBE & Amdocs cited; derived_from Product & Pricing Engine + related Account Lifecycle Manager sensible. |
| technology-capabilities/accrual-calculation-service.md | 5 | 4 | 5 | 5 | 5 | Day-count conventions, balance-base, daily batch accrual accurate; FLEXCUBE cited; derived_from Interest & Charges Engine sensible. |
| technology-capabilities/bureau-response-normalizer.md | 5 | 5 | 5 | 5 | 5 | Multi-bureau normalisation/score-variance accurate, Equifax note supports; derived_from Bureau Data Integration + related Credit Scoring Service correct. |
| technology-capabilities/intercompany-matching-service.md | 5 | 4 | 5 | 5 | 5 | IC matching/tolerances/pre-elimination accurate; OneStream/Oracle EPM cited (homepage-level); derived_from Consolidation Engine + related Intercompany Accounting Service sensible. |
| systems/legacy/avaloq-banking-suite.md | 5 | 5 | 5 | 5 | 5 | Swiss core+wealth, NEC-owned, SaaS/BPaaS all confirmed; Core Banking Processing depends_on + related Sopra Amplitude sensible. |
| systems/legacy/fidessa.md | 5 | 5 | 5 | 5 | 5 | Sell-side equities OMS, ION, 6,500/600/100 figures confirmed; OMS depends_on + related SS&C Advent Moxy sensible. |
| systems/legacy/nasdaq-calypso.md | 5 | 5 | 4 | 5 | 5 | Cross-asset front-to-back capital-markets/treasury, Calypso+AxiomSL→Adenza→Nasdaq confirmed. But it is a derivatives/treasury/risk platform mapped under "Order Management System depends_on" — a loose capability fit (it is far more than an OMS). |
| systems/modern/fis-modern-banking-platform.md | 5 | 5 | 5 | 5 | 5 | Cloud-native/Azure/modular SaaS confirmed; supersedes FIS Profile & FIS Horizon are same-capability (legacy FIS cores) — correct. |
| systems/modern/flexone.md | 5 | 4 | 2 | 5 | 5 | gRPC/buy-side OEMS/2026 award confirmed. FAIL on rel: supersedes Fidessa (sell-side OMS) and supersedes Nasdaq Calypso (derivatives/treasury platform) are NOT same-capability; only supersedes Linedata Longview (buy-side OMS) is valid. |
| systems/modern/orion.md | 5 | 5 | 4 | 5 | 5 | $5.8T AUA, Denali AI, Redtail confirmed. supersedes Objectway plausible (both wealth platforms) but Objectway is an active vendor, not a retired legacy system — supersede grain is loose. |
| systems/modern/sage-intacct.md | 5 | 5 | 5 | 5 | 5 | Multi-dimensional GL/cloud SaaS/AI confirmed; GL Engine depends_on + supersedes Infor SunSystems (same-capability legacy financials) sensible. |

## Per-dimension means (n=22)

- Definitional accuracy: 110/22 = **5.00**
- Groundedness: (5+5+5+5+4+4+5+3+5+4+3+5+4+5+4+5+5+5+4+5+5) ... = 100/22 = **4.55**
- Relationship sensibility: (5+5+5+5+5+5+5+5+5+5+5+5+5+5+5+5+4+5+2+4+5) = 100/22 = **4.55**
- Canonical-naming fidelity: 110/22 = **5.00**
- Granularity fit: (5+5+4+5+5+5+5+4+5+5+5+5+5+5+5+5+5+5+5+5+5) = 108/22 = **4.91**

(Means computed across all 22 rows; arithmetic: accuracy 5.00, grounded 4.55, rel 4.55, naming 5.00, gran 4.91 — all >= 4.0.)

## Verdict: **FAIL**

Gate requires mean >= 4.0 on every dimension (satisfied) AND no individual note scoring <3 on
Groundedness or Relationship sensibility. **flexone.md scores 2 on Relationship sensibility**,
which trips the per-note floor. Domain cannot be marked `done` until fixed and re-judged.

## Required fixes

- **systems/modern/flexone.md (BLOCKING — rel = 2):** Remove `supersedes Fidessa` and
  `supersedes Nasdaq Calypso`. FlexONE is a buy-side OEMS; Fidessa is a sell-side broker OMS and
  Calypso is a cross-asset derivatives/treasury/risk platform — neither is the same capability.
  Retain only `supersedes Linedata Longview` (buy-side OMS). If a Fidessa/Calypso relationship is
  wanted, express it as `related_to`, not `supersedes`.
- **systems/legacy/nasdaq-calypso.md (rel = 4, advisory):** "Order Management System depends_on
  Nasdaq Calypso" understates the platform. Consider mapping under a trading/treasury/risk
  capability (or a cross-asset trade-lifecycle capability) rather than OMS, or add a more precise
  parent capability.
- **systems/modern/orion.md (rel = 4, advisory):** `supersedes Objectway` — Objectway is an
  active competing wealth platform, not a retired legacy system. Verify the registry classifies
  Objectway as legacy in the same capability; otherwise downgrade to `related_to`.
- **technology-capabilities/gips-composite-service.md (grounded = 3, advisory):** Replace the two
  cited sources (a Brinson-vs-risk attribution blog and the Wikipedia performance-attribution
  article) with a GIPS-specific source (e.g. CFA Institute GIPS Standards) that actually supports
  the composite-construction and disclosure claims.
- **technology-capabilities/hedge-accounting-service.md (grounded = 3, advisory):** The IFRS 9
  hedge-accounting specifics (economic-relationship test, OCI/CFH reserve, FVH carrying-amount
  adjustment) are sourced only to generic TMS overviews. Add an IFRS 9 / IAS 39 hedge-accounting
  source that substantiates these mechanics.
