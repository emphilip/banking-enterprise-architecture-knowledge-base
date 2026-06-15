# LLM-Judge Report — Payments Deep-Dive (sample of 28)

Judge: strict EA knowledge-base reviewer. Method: each note read in full; every
URL in `## References` / `sources` fetched (most vendor + BIAN/ISO/Nacha pages
returned HTTP 403 to direct fetch, so the load-bearing factual claims were
corroborated via web search against the same vendor/standards material and
primary sources). Scores are 1–5 per the rubric; 3 = acceptable, <3 = fail.

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|---|---|---|---|---|---|---|
| systems/modern/form3.md | 5 | 5 | 5 | 5 | 5 | Every claim (cloud-native, multi-cloud, PaaS, zero-downtime A2A, single-API scheme access) confirmed by Form3 press release "zero-downtime payment processing using multi-cloud architecture and a single code base"; supersedes Legacy Payment Hub + Finastra GPP both Payment Orchestration. |
| systems/modern/aci-connetic.md | 5 | 5 | 5 | 5 | 5 | "cloud-native SaaS … microservices, multi-rail orchestration" confirmed by ACI Connetic page / ffnews "one cloud-native platform … microservices, APIs, embedded AI"; supersedes ACI BASE24 + ACI EPP, both Payment Orchestration — correct. |
| systems/modern/bottomline-payments.md | 4 | 4 | 4 | 5 | 4 | ISO 20022 transformation/enrichment + connectivity confirmed (Bottomline message-transformation page); but Bottomline is primarily a transformation/connectivity player, so "payments orchestration / payments hub" framing and supersedes-FIS-OPF are registry-aligned yet a definitional stretch — no source calls it a full payment hub. |
| systems/legacy/fis-open-payment-framework.md | 5 | 5 | 5 | 5 | 5 | "ISO 20022-native … parsing, validation, routing, warehousing across instant, high-value and ACH" confirmed by FIS OPF brochure ("ISO 20022-based foundation … high-value domestic, instant, batch and international"); tier-1 backed by Gartner Leader release. |
| systems/legacy/finastra-global-payplus.md | 5 | 5 | 5 | 5 | 5 | "modular multi-rail … ISO 20022-native … automated repair … high-value, mass, real-time" all confirmed verbatim by Finastra GPP overview ("ISO 20022-native … automated repair … high-value payments, mass payments and real-time payments"). |
| systems/legacy/aci-enterprise-payments-platform.md | 4 | 3 | 5 | 5 | 4 | multi-bank/multi-currency, RTGS/ACH/instant/cross-border, SWIFT gpi/Go all confirmed by ACI EPP page; BUT the specific "50+ networks" figure is NOT supported by any cited source (search explicitly: "unable to find that specific detail") — invented precision, drags Groundedness. |
| technology-capabilities/payment-routing-engine.md | 5 | 5 | 5 | 5 | 5 | Rules-driven least-cost/optimal-rail selection confirmed by Volante Payment Hub ("smart routing for optimal rail selection"); exemplars (Volante, FIS OPF, ACI EPP) all real Payment Orchestration hubs; derived_from Payment Orchestration correct. |
| technology-capabilities/scheme-connectivity-gateway.md | 5 | 5 | 5 | 5 | 5 | Certified rail adapters (SWIFT/Fedwire/CHIPS/FedNow/RTP/ACH/SEPA/TARGET2/CHAPS/FPS) supported by Volante US Payments + Form3 single-API scheme access; depends_on Payment Message Transformer + derived_from Payment Orchestration correct. |
| technology-capabilities/iso-20022-translation-service.md | 5 | 5 | 5 | 5 | 5 | Bidirectional MT/MX translation, coexistence handling confirmed by Volante ISO 20022 + Bottomline transformation pages; derived_from Payment Message Transformer (L3 under correct L2) and mentions ISO 20022 — exact. |
| technology-capabilities/payment-sanctions-filter.md | 5 | 5 | 5 | 5 | 5 | Sub-second in-flight hold/release/reject before settlement for instant rails confirmed by sanctions.io real-time-payments + TIS payments-hub screening; depends_on Transaction Monitoring Platform, related_to Fraud Analytics, mentions Sanctions Screening — all correct grain/direction. |
| business-capabilities/L3-payment-order-capture.md | 5 | 5 | 5 | 5 | 5 | BIAN Payment Order service domain ("handling customer requests for payment orders") confirmed; derived_from Payment Initiation, depends_on Payment Orchestration — correct L3 grain. |
| business-capabilities/L3-request-to-pay.md | 4 | 4 | 5 | 5 | 5 | pain.013/pain.014 accept/decline confirmed (NACHA RfP-live + ISO 20022 pain.013 Creditor Payment Activation Request); "defer" option is unsupported (sources show accept/reject only) and source #1 URL is a pain.001/002 page, not the cited pain.013/014 message — source-relevance + minor over-claim. |
| business-capabilities/L3-interbank-settlement.md | 5 | 5 | 5 | 5 | 5 | Net/gross discharge across central-bank accounts (RTGS/FedNow) confirmed by Federal Reserve interbank-settlement notice + BoE payment-and-settlement; derived_from Payment Clearing & Settlement correct. |
| business-capabilities/L3-correspondent-banking.md | 5 | 5 | 5 | 5 | 5 | BIAN Correspondent Bank Operations + Correspondent Bank Directory domains confirmed to exist; nostro/vostro + cross-border routing accurate; derived_from Payment Execution correct. |
| business-capabilities/L3-direct-debit-mandate-management.md | 4 | 4 | 5 | 5 | 5 | pain.009/010/011 create/amend/cancel + BIAN Direct Debit Mandate domain confirmed for SEPA; but Bacs mandates use AUDDIS, NOT ISO 20022 pain.009/010/011 — "ISO 20022 pain.009/010/011, SEPA and Bacs" conflates two schemes (cited GoCardless Bacs page does not support pain-message use for Bacs). |
| business-capabilities/L4-same-day-ach-processing.md | 5 | 5 | 5 | 5 | 5 | Intraday windows, per-entry $1M limit, submission cut-offs under Nacha rules confirmed (Nacha Same Day ACH phases + Fed FAQ); derived_from Domestic Payments — correct L4 atomic grain. |
| business-capabilities/L4-instant-payment-clearing.md | 5 | 5 | 5 | 5 | 5 | Immediate, irrevocable, 24/7/365 individual clearing on RTP/FedNow confirmed (Cross River RTP-vs-FedNow + ACI FedNow); derived_from Real-Time Payments, depends_on Data Streaming — sensible for low-latency event processing. |
| business-capabilities/L4-fx-conversion-for-payments.md | 5 | 5 | 5 | 5 | 5 | Currency conversion/rate sourcing/margin on cross-border instructions aligned to BIAN Payment Execution ("bank-side processing … applying payment preferences") + Correspondent Bank Operations; derived_from Cross-Border Payments correct. |
| business-capabilities/L4-nostro-reconciliation.md | 5 | 5 | 5 | 5 | 5 | Matching nostro movements vs expected correspondent activity + routing unmatched items confirmed (Skydo nostro guide + BIAN correspondent view); derived_from Correspondent Banking correct. |
| process-flows/payment-processing/01-receive-payment-instruction.md | 5 | 5 | 5 | 5 | 5 | Intake of pain.001/file/API confirmed (Cashbook pain guide + Nacha); causes Validate Payment, depends_on Payment Orchestration, mentions Payment Operations Analyst + Payment Instruction — exact ordered-step grain. |
| process-flows/payment-processing/05-route-payment.md | 5 | 5 | 5 | 5 | 5 | Rail selection (ACH/Fedwire/RTP-FedNow/SWIFT) by amount/speed/destination confirmed (Fedwire + Modern Treasury RTP/FedNow interop); causes Format Clearing Message — correct order; single-action grain. |
| process-flows/reconciliation-and-settlement/01-confirm-settlement.md | 5 | 5 | 5 | 5 | 5 | Capture settlement advices + finality confirmation supported (Fedwire + FedNow/RTP settlement page); causes Ingest Bank Statement, mentions Settlement Officer + Settlement File, triggered by Settlement Received Event — correct. |
| process-flows/reconciliation-and-settlement/04-identify-breaks.md | 5 | 5 | 5 | 5 | 5 | Surfacing/classifying unmatched items as breaks confirmed (SmartStream exception mgmt: "breaks are identified instantly, routed through governed workflows"); causes Investigate Break, depends_on Workflow Orchestration, raises Reconciliation Break Event — correct. |
| process-flows/cash-management/01-aggregate-balances.md | 5 | 5 | 5 | 5 | 5 | Intraday/prior-day balance collection across accounts/entities/currencies confirmed (Kyriba cash & liquidity); causes Determine Cash Position, depends_on Integration Platform, mentions Treasury Cash Manager + Bank Statement Message — correct first step. |
| process-flows/cash-management/05-execute-funding-transfer.md | 5 | 5 | 5 | 5 | 5 | Generating/releasing sweep/pool/funding instructions to target balances confirmed (Nilus cash concentration + Atlar pooling; Kyriba target-balance sweeps); causes Monitor Liquidity Position, depends_on Payment Orchestration — correct. |
| concepts/payment-instruction.md | 5 | 5 | 5 | 5 | 5 | Artifact = customer/channel funds-move request (pain.001/file/API) carrying debtor/creditor/amount/remittance — confirmed by Cashbook pain guide; related_to Payments + mentions Receive Payment Instruction/Payment Processing — correct soft links for an artifact. |
| concepts/payment-initiated-event.md | 5 | 5 | 5 | 5 | 5 | Trigger event on accepted instruction; causes Receive Payment Instruction — correct event→step causality and grain (Cashbook pain guide supports the pain.001/file/API arrival). |
| concepts/settlement-officer.md | 5 | 5 | 4 | 5 | 5 | Role confirming settlement finality + posting adjustments under dual control is sound (Fedwire); mentions Confirm Settlement + Post Adjustment correct, BUT claim that the role "signs off / certifies the reconciliation outcome" overlaps the Reconciliation Analyst role's grain (registry assigns Sign Off Reconciliation / Reconciliation Report there) — minor grain bleed via soft verbs only. |

## Per-dimension means (n=28)

- Definitional accuracy: (5×22 + 4×6) / 28 = **4.79**
- Groundedness: (5×23 + 4×4 + 3×1) / 28 = **4.79**
- Relationship sensibility: (5×26 + 4×2) / 28 = **4.93**
- Canonical-naming fidelity: 5×28 / 28 = **5.00**
- Granularity fit: (5×25 + 4×3) / 28 = **4.89**

## Verdict

**PASS.**

- All five per-dimension means are ≥ 4.0 (lowest = 4.79).
- No note scores < 3 on Groundedness (lowest = 3, `aci-enterprise-payments-platform.md`) or on Relationship sensibility (lowest = 4, `settlement-officer.md`).

The gate is met. The PASS is marginal on Groundedness for one note (the "50+
networks" claim sits exactly at the failing threshold) and should be tightened.

## Required fixes (recommended; none block the gate)

- **systems/legacy/aci-enterprise-payments-platform.md** — Remove or source the
  unsupported "50+ networks" figure. No cited source states a network count;
  reword to "across RTGS, ACH, instant, cross-border and card networks" or add a
  source that gives the number. (This is the only note at the Groundedness floor.)
- **business-capabilities/L3-direct-debit-mandate-management.md** — Fix the
  scheme/standard conflation: pain.009/010/011 apply to SEPA, not Bacs (Bacs uses
  AUDDIS). Either scope the pain messages to SEPA and describe Bacs mandates
  separately, or drop "Bacs" from the ISO 20022 pain clause.
- **business-capabilities/L3-request-to-pay.md** — (a) Replace source #1
  (`iso20022payments.com/cbpr/pain-001-pain-002/`) with a pain.013/pain.014 (RfP)
  source, since the cited claim is about pain.013/014; (b) drop or source the
  "defer" response option — sources support accept/decline only.
- **systems/modern/bottomline-payments.md** — Soften the "payments hub /
  orchestration" framing or add a source that positions Bottomline as a payment
  hub; current sources support transformation/enrichment/connectivity, not full
  multi-rail orchestration. Keep the supersedes edges (registry-aligned).
- **concepts/settlement-officer.md** — Remove the "signs off / certifies the
  reconciliation outcome" claim (or change to "supports") to avoid grain overlap
  with the Reconciliation Analyst role, which owns Sign Off Reconciliation.
