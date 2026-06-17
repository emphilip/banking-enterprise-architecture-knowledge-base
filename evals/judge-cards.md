# LLM-Judge Results — Cards Domain Deep-Dive (NEW notes)

Judge: strict EA reviewer. Date: 2026-06-15. Sample: 28 notes (representative).
Scoring 1-5 per rubric dimension (3 = acceptable, <3 = fail).

## Corroboration performed (web)
- Visa completed acquisition of Pismo for ~US$1B, Jan 2024; cloud-native issuer-processing + core-banking platform (pismo.io, Visa newsroom, PYMNTS).
- Thredd = rebrand of Global Processing Services (GPS); GPS Apex platform, Visa/Mastercard-certified issuer processor (thredd.com newsroom, docs.thredd.com).
- Visa dispute categories 10 Fraud / 11 Authorization / 12 Processing Errors / 13 Consumer Disputes under VCR (Visa rules PDF, Sift, Kount).
- BIAN Card Case service domain "captures, tracks, resolves and reports on card related transactional disputes" between issuer/network/acquirer (bian.org/semantic-apis/card-case).
- Mastercard 4837 = No Cardholder Authorization; 4853 = Cardholder Dispute; acquirer 45-day / issuer 120-day windows (chargebackgurus, chargebacks911, Sift).
- Fiserv OmniPay = acquirer/merchant platform (clearing, settlement, funding, dispute mgmt); Fiserv Optis = issuer credit-card platform (Fiserv docs/site, Celent). Confirms acquirer vs issuer split.

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|---|---|---|---|---|---|---|
| systems/legacy/fis-card-management.md | 4 | 4 | 4 | 4 | 4 | Payments One / CMS framing accurate; Celent modernization profile supports claim. "related to Fiserv Optis" weak but not wrong. |
| systems/legacy/fiserv-omnipay.md | 5 | 4 | 5 | 4 | 4 | Acquirer-side switching/clearing/settlement confirmed by Fiserv docs. Sound. |
| systems/legacy/fiserv-optis.md | 4 | 4 | 4 | 4 | 4 | Issuer credit platform confirmed (Celent "Reengineering the Core"). "profiled for modernization" supported. |
| systems/modern/thredd.md | 4 | 4 | 2 | 3 | 4 | GPS rebrand & API-first issuer processing fully corroborated. REL=2: `supersedes Fiserv OmniPay` is cross-capability — OmniPay is acquirer-side, Thredd is issuer-side; wrong-capability supersede. `supersedes First Data Cards` also issuer/cross unclear. |
| systems/modern/lithic.md | 4 | 4 | 4 | 4 | 4 | API-first processor, processing-only model, Privacy.com origin plausible. `supersedes First Data Cards` defensible (issuer-side). Grounded by lithic.com. |
| systems/modern/pismo.md | 5 | 5 | 4 | 4 | 4 | Visa acquisition & cloud-native issuer/core-banking confirmed at $1B. `supersedes TSYS TS2 / FIS Card Management` are same-capability (issuer) — sensible. Strong. |
| systems/modern/i2c.md | 4 | 4 | 4 | 4 | 4 | Unified configurable issuer platform supported by i2cinc.com. Supersedes TS2/Optis are same-capability issuer — sensible. Second source is a listicle (weaker). |
| technology-capabilities/card-authorization-engine.md | 5 | 4 | 5 | 5 | 4 | Real-time auth decisioning; Marqeta dynamic-auth claim traces to cited Marqeta docs. Relationships well-formed (derived_from Card Processing, depends_on switch). |
| technology-capabilities/card-tokenization-service.md | 5 | 4 | 4 | 4 | 4 | Network token vault, Visa/MC token services, PCI scope reduction — accurate; AWS + Marqeta sources adequate. |
| technology-capabilities/dispute-and-chargeback-system.md | 4 | 4 | 5 | 3 | 4 | Lifecycle accurate. NAMING=3: conflates "VCR" (Visa Claims Resolution) with "VROL" (Visa Resolve Online, the prior platform) — lists "VROL and VCR" as if co-current; imprecise canonical use. Sources (Rivero, payabl) support lifecycle. |
| technology-capabilities/emv-cryptogram-validation.md | 5 | 4 | 5 | 5 | 4 | ARQC validation / ARPC generation / session-key-from-master-key / HSM all technically correct; Amex + Cryptomathic sources relevant. L3 derived_from Card Authorization Engine is sensible. |
| technology-capabilities/3-d-secure-service.md | 5 | 4 | 3 | 5 | 4 | EMV 3DS / ACS / RBA accurate; EMVCo + Mastercard sources good. REL=3: `derived_from Card Tokenization Service` is questionable — 3DS is cardholder authentication, not a child of tokenization; expected derived_from an authentication/authorization parent. |
| business-capabilities/L3-card-application.md | 5 | 4 | 5 | 4 | 4 | Card Capture / Card Terms BIAN domains real; Reg Z Schumer-box detail correct (eCFR cited). Well-grounded. |
| business-capabilities/L3-authorization-decisioning.md | 5 | 5 | 5 | 5 | 4 | BIAN Card Authorization + ISO 8583 0100/0110 + action codes (00/05/51) all accurate and cited. Exemplary. |
| business-capabilities/L3-chargeback-handling.md | 5 | 5 | 5 | 4 | 4 | BIAN Card Case + Visa 10-13 + MC 4853/4837 + Reg E/Z all corroborated. Strong. |
| business-capabilities/L3-pre-arbitration-and-arbitration.md | 4 | 4 | 5 | 4 | 4 | MC 45-day pre-arb response confirmed; "Card Network Participant Facility" is a real BIAN domain though loosely fitted. Sound. |
| business-capabilities/L4-card-personalisation.md | 5 | 4 | 5 | 4 | 4 | BIAN Issued Device Administration + EMVCo Book 2/3 + PCI Card Production + key derivation accurate. Atomic L4. |
| business-capabilities/L4-chargeback-filing.md | 4 | 4 | 5 | 4 | 4 | Visa 13.1 / 10.4 condition codes correct; derived_from Chargeback Handling correct child grain. |
| business-capabilities/L4-reward-points-redemption.md | 4 | 3 | 5 | 4 | 4 | Mechanics plausible; "BIAN Reward Points Account" service domain not verified and APQC source is a generic landing page — GROUNDED=3 (acceptable, at floor). Atomic L4. |
| business-processes/card-transaction-authorization.md | 5 | 4 | 5 | 4 | 4 | EMV/ARQC/PIN/STIP/hold flow accurate; AWS Payment Cryptography + ACI sources relevant. Flow ordering coherent. |
| business-processes/chargeback-processing.md | 5 | 4 | 5 | 4 | 4 | Lifecycle, 120-day filing, 30-day representment, Reg Z 60-day all accurate; sources adequate (some blog-tier). |
| process-flows/card-transaction-authorization/01-receive-authorization-request.md | 5 | 4 | 5 | 5 | 5 | Single-action step; ISO 8583 intake + PCI controls correct; clean relationships. |
| process-flows/card-transaction-authorization/05-authorize-transaction.md | 5 | 4 | 5 | 5 | 5 | Atomic decide/hold/STIP step; depends_on Card Authorization correct. |
| process-flows/chargeback-processing/01-assign-reason-code.md | 5 | 4 | 5 | 5 | 5 | Single action; Visa 10-13 / MC 4837/4853 + 120-day correct; Rivero source relevant. |
| process-flows/chargeback-processing/04-review-representment-evidence.md | 5 | 4 | 5 | 5 | 5 | Atomic review step; depends_on Document Management sensible; payabl source supports. |
| process-flows/card-fraud-handling/01-triage-fraud-alert.md | 4 | 3 | 5 | 5 | 5 | Triage action well-scoped; depends_on Fraud Analytics correct. GROUNDED=3: single source is a generic "velocity checks" blog that does not directly support alert triage/prioritization. |
| concepts/authorization-request.md | 5 | 4 | 5 | 4 | 4 | ISO 8583 MTI 0100/0200, MCC, POS entry mode, ARQC fields accurate; well-cited. Artifact grain correct. |
| concepts/chargeback-case.md | 5 | 4 | 5 | 4 | 4 | Case-record fields, reason codes, Reg Z/E timelines, 120-day filing accurate. Blog-tier sources but claims standard/verifiable. |

## Per-dimension means (n=28)

- Definitional accuracy: (4+5+4+4+4+5+4+5+5+4+5+5+5+5+5+4+5+4+4+5+5+5+5+5+5+4+5+5) = 130 / 28 = **4.64**
- Groundedness: (4+4+4+4+4+5+4+4+4+4+4+4+4+5+5+4+4+4+3+4+4+4+4+4+4+3+4+4) = 113 / 28 = **4.04**
- Relationship sensibility: (4+5+4+2+4+4+4+5+4+5+5+3+5+5+5+5+5+5+5+5+5+5+5+5+5+5+5+5) = 129 / 28 = **4.61**
- Canonical-naming fidelity: (4+4+4+3+4+4+4+5+4+3+5+5+4+5+4+4+4+4+4+4+4+5+5+5+5+5+4+4) = 119 / 28 = **4.25**
- Granularity fit: (4+4+4+4+4+4+4+4+4+4+4+4+4+4+4+4+4+4+4+4+4+5+5+5+5+5+4+4) = 118 / 28 = **4.21**

## Verdict: FAIL

Means clear the >=4.0 bar on every dimension (accuracy 4.64, grounded 4.04, rel 4.61, naming 4.25, gran 4.21).
HOWEVER the gate also requires **no individual note <3 on Groundedness or Relationship sensibility**.
One note violates this:

- `systems/modern/thredd.md` — Relationship sensibility = **2** (`supersedes Fiserv OmniPay`: acquirer-side platform superseded by an issuer-side processor — a wrong-capability supersede; rubric requires `supersedes` to target a *same-capability* legacy system).

Because a sampled note scores <3 on Relationship sensibility, the domain **does not pass** and must not be marked `done` until fixed and re-judged.

## REQUIRED FIXES (blocking)

- **systems/modern/thredd.md**: Remove the `Thredd supersedes Fiserv OmniPay` relationship. OmniPay is an acquirer/merchant-processing platform; Thredd is an issuer processor. Re-point any supersede to a same-capability legacy *issuer* platform (e.g., a legacy issuer-processing stack) or drop it. Re-verify `supersedes First Data Cards` is issuer-side before re-judge.

## RECOMMENDED FIXES (non-blocking; would raise means / margins)

- **technology-capabilities/dispute-and-chargeback-system.md** (naming 3): Do not present "VROL and VCR" as co-equal current systems. VCR = Visa Claims Resolution (current dispute process); VROL = Visa Resolve Online (legacy). State the relationship/timeline precisely or reference only the current canonical term.
- **technology-capabilities/3-d-secure-service.md** (rel 3): Reconsider `derived_from Card Tokenization Service`. 3-D Secure is cardholder authentication; deriving it from tokenization is a weak parent. Prefer derivation from an authentication/authorization parent capability.
- **business-capabilities/L4-reward-points-redemption.md** (grounded 3): Verify the "BIAN Reward Points Account" service-domain name against the BIAN landscape and replace the generic APQC landing-page source with a specific, claim-supporting reference.
- **process-flows/card-fraud-handling/01-triage-fraud-alert.md** (grounded 3): Replace/supplement the generic "velocity checks" blog with a source that actually supports fraud-alert triage and prioritization.

## Re-judge (relationship fixes)

Date: 2026-06-15. Re-scoring only the 2 revised notes on Relationship sensibility and Definitional accuracy.

Corroboration: First Data Cards / VisionPLUS confirmed as an issuer-side card management & processing platform — transaction authorization, account servicing, card management for credit/debit/prepaid issuers (Fiserv Issuing Solutions, digitaltransactions.net). Thredd is an API-first issuer processor; both are issuer-side card processing = same capability.

| path | rel (before->after) | accuracy | notes |
|---|---|---|---|
| systems/modern/thredd.md | 2 -> 4 | 4 | Cross-capability `supersedes Fiserv OmniPay` (acquirer vs issuer) REMOVED. Remaining `supersedes First Data Cards` is same-capability: VisionPLUS is a legacy issuer card-management/processing platform, Thredd is a modern issuer processor — sensible same-capability supersede. "Realizes Card Processing" is expressed as `Card Processing depends on Thredd` (correct direction). |
| technology-capabilities/3-d-secure-service.md | 3 -> 4 | 5 | `derived_from` changed from Card Tokenization Service to Card Authorization Engine. 3-D Secure is the cardholder-authentication step within the e-commerce authorization flow; deriving the L3 3DS capability from the L2 Card Authorization Engine is a sensible authentication/authorization parent. |

Both notes now score >=3 on Relationship sensibility (thredd = 4, 3-d-secure-service = 4): the gate's per-note Relationship floor is satisfied for these two notes.
