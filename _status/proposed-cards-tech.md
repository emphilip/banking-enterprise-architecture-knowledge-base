---
title: Proposed Cards Technology Decomposition
type: proposal
status: draft
author: tech-decomposition sub-agent
date: 2026-06-15
---

# Proposed Cards Technology Decomposition

Scope: enabling technology-capability decomposition for the Cards domain's core
enabling technology capability, **Card Processing** (the EXISTING parent in the
Core Processing technology domain), plus a systems refresh of notable card
platforms not already covered.

Grounding: card-management-system / issuer-processing reference architectures and
vendor docs (Marqeta card processing, Dynamic Authorization and tokenization /
digital-wallet docs; Galileo card-program-to-network connectivity; Thredd / GPS
Apex issuer processing; Lithic debit/credit ledgers and processing-only; i2c
unified issuer processing; Pismo / Visa Global Issuer Processing; Fiserv OmniPay
clearing/settlement/dispute and Optis; FIS Payments One issuer processing),
the card transaction lifecycle (authorization -> clearing -> settlement -> funding),
ISO 8583 interchange messaging and the authorization switch, EMV chip
personalization and cryptogram (ARQC/ARPC) validation, EMVCo 3-D Secure /
network tokenization, PCI DSS & PCI Card Production, Visa VCR/VROL and Mastercard
Mastercom dispute lifecycles, plus stand-in / on-behalf-of (STIP) processing and
cloud-native event-driven ledger patterns.

Naming verified globally unique against `glossary/_canonical-names.md`. Tech names
are deliberately kept distinct from the Cards business capabilities and processes,
e.g.:
- tech "Card Authorization Engine" vs business cap "Card Authorization"
- tech "Card Issuing & Personalisation" vs business cap "Card Issuing" / process "Card Issuance"
- tech "Dispute & Chargeback System" vs business cap "Dispute Management" / process "Dispute Resolution"
- tech "Card Account Ledger" vs deposits tech sub-cap "Transaction Posting Engine" and tech cap "General Ledger Engine"
- tech "Clearing & Settlement Processor" vs business cap "Payment Clearing & Settlement" / payments tech "Settlement Instruction Engine"
- tech "Card Transaction Switch" vs payments tech "Payment Routing Engine" / "Scheme Connectivity Gateway"

Also checked against payments, lending and deposits tech sub-caps already added
(e.g. "Settlement Instruction Engine", "Transaction Posting Engine", "Payment
Routing Engine", "Scheme Connectivity Gateway") — no clashes.

Relationship verbs used (of the allowed 7): `derived_from`, `defined_in`,
`depends_on`, `related_to`.

## 1) Technology sub-capabilities

All `type = technology-capability`, `domain = Core Processing`,
`parent = Card Processing` (L2 rows) and the named L2 (L3 rows).

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Card Authorization Engine | technology-capability | L2 | Card Processing | Core Processing | Real-time issuer authorization decisioning that evaluates each inbound card transaction against account status, available balance/credit, spend controls, velocity and risk rules and returns an approve/decline within scheme timeouts. | Authorization Decisioning Engine, Issuer Auth Engine, Dynamic Authorization | derived_from Card Processing; defined_in Core Processing; related_to Card Authorization; depends_on Card Transaction Switch | https://www.marqeta.com/platform/card-processing ; https://www.marqeta.com/docs/developer-guides/about-transactions |
| Card Transaction Switch | technology-capability | L2 | Card Processing | Core Processing | Network-facing switching layer that connects to card schemes, parses and builds ISO 8583 / network messages, and routes authorization, reversal and advice traffic between the schemes and the issuer authorization host. | Issuer Switch, ISO 8583 Switch, Scheme Message Switch | derived_from Card Processing; defined_in Core Processing; related_to Card Authorization | https://en.wikipedia.org/wiki/ISO_8583 ; https://www.galileo-ft.com/blog/connect-card-program-to-payment-network/ |
| Card Issuing & Personalisation | technology-capability | L2 | Card Processing | Core Processing | Manufactures and provisions physical and virtual cards: PAN/BIN allocation, EMV chip personalisation and key injection, instant and bureau issuance, and digital card-credential creation under PCI Card Production controls. | Card Issuance Engine, Personalisation Service, Card Provisioning | derived_from Card Processing; defined_in Core Processing; related_to Card Issuing; depends_on Card Tokenization Service | https://www.payhuddle.com/post/emv-card-personalization-validation-process ; https://enfuce.com/blog/card-issuing-api/ |
| Card Tokenization Service | technology-capability | L2 | Card Processing | Core Processing | Generates and manages network tokens and a secure token vault, mapping device/wallet tokens to the underlying PAN for digital-wallet provisioning, card-on-file and secure authorization without exposing the real card number. | Token Vault Service, Network Tokenization, Digital Card Tokenisation | derived_from Card Processing; defined_in Core Processing; related_to Card Issuing; depends_on Identity Access Management | https://www.marqeta.com/platform/tokenization-digital-wallets ; https://aws.amazon.com/blogs/industries/credit-card-payment-processing-on-aws/ |
| Card Account Ledger | technology-capability | L2 | Card Processing | Core Processing | Maintains the cardholder account system-of-record: balances, holds and authorizations-in-flight, posted transactions, statement billing cycles, fees and (for credit) credit-limit and revolving-balance accounting. | Cardholder Ledger, Card Billing Engine, Card Statement Ledger | derived_from Card Processing; defined_in Core Processing; related_to Card Issuing | https://www.lithic.com/blog/developer-first-issuer-processing ; https://www.pismo.io/ |
| Clearing & Settlement Processor | technology-capability | L2 | Card Processing | Core Processing | Processes incoming and outgoing scheme clearing files, matches presentments to prior authorizations, calculates interchange and scheme fees, and computes net settlement positions and funding with the card networks. | Card Clearing Engine, Interchange & Settlement Processor, Presentment Processor | derived_from Card Processing; defined_in Core Processing; related_to Card Authorization; depends_on Card Account Ledger | https://docs.fiserv.dev/private/docs/omnipay-boarding-intro ; https://medium.com/@umutt.akbulut/card-network-settlement-a-comprehensive-architectural-operational-and-distributed-systems-2de92a158b37 |
| Dispute & Chargeback System | technology-capability | L2 | Card Processing | Core Processing | Manages the issuer side of the scheme dispute lifecycle — chargeback initiation and reason-code assignment, representment, pre-arbitration/arbitration and provisional credits — integrating with Visa VROL/VCR and Mastercard Mastercom. | Chargeback Engine, Dispute Management System, Chargeback Processor | derived_from Card Processing; defined_in Core Processing; related_to Dispute Management | https://rivero.tech/blog/dispute-lifecycle-explained ; https://payabl.com/news/mastercard-and-visa-chargeback-rules-and-processes |
| Card Rewards Engine | technology-capability | L2 | Card Processing | Core Processing | Calculates and accrues card rewards, points, cashback and loyalty benefits against qualifying transactions, applying earn rules, tiers, multipliers and redemption against the cardholder account. | Loyalty & Rewards Engine, Points Engine, Cashback Engine | derived_from Card Processing; defined_in Core Processing; related_to Card Issuing; depends_on Card Account Ledger | https://www.marqeta.com/resources/program-management-guide ; https://www.fiserv.com/content/dam/fiserv-ent/final-files/marketing-collateral/sales-sheets/credit-select-sales-sheet-0623.pdf |
| EMV Cryptogram Validation | technology-capability | L3 | Card Authorization Engine | Core Processing | Validates EMV chip cryptograms (ARQC) during authorization and generates the response cryptogram (ARPC), deriving session keys from issuer master keys to confirm card authenticity and counter cloned/skimmed cards. | ARQC Validation, Chip Cryptogram Service, EMV Validation Service | derived_from Card Authorization Engine; defined_in Core Processing; related_to Card Authorization | https://network.americanexpress.com/globalnetwork/dam/jcr:7d61622d-72b8-4cd2-9a28-625ef4e2c221/EMV%20Validation%20Service%20Product%20Capability%20Guide.pdf ; https://www.cryptomathic.com/blog/a-brief-overview-of-the-challenges-involved-in-key-management-for-emv-personalization-the-main-actors-of-emv-personalization |
| Stand-In Processing Service | technology-capability | L3 | Card Authorization Engine | Core Processing | Provides stand-in / on-behalf-of (STIP) authorization decisioning when the issuer host is unavailable or times out, applying parameterised limits and risk rules so transactions can still be approved or declined. | STIP Service, On-Behalf-Of Processing, Stand-In Authorization | derived_from Card Authorization Engine; defined_in Core Processing; related_to Card Authorization | https://network.americanexpress.com/globalnetwork/dam/jcr:7d61622d-72b8-4cd2-9a28-625ef4e2c221/EMV%20Validation%20Service%20Product%20Capability%20Guide.pdf ; https://dwaynegefferie.substack.com/p/modern-issuer-processing |
| 3-D Secure Service | technology-capability | L3 | Card Tokenization Service | Core Processing | Performs EMV 3-D Secure cardholder authentication for e-commerce: operates/integrates the issuer Access Control Server, risk-based authentication and challenge flows to confirm the legitimate cardholder. | 3DS Service, EMV 3DS ACS, Cardholder Authentication Service | derived_from Card Tokenization Service; defined_in Core Processing; related_to Card Authorization; depends_on Customer Authentication | https://www.emvco.com/emv-technologies/3-d-secure/ ; https://www.mastercard.com/content/dam/public/mastercardcom/globalrisk/pdf/Top-10-Things-to-Know-About-3DS.pdf |

## 2) Systems refresh

Only genuinely new, verifiable card systems NOT already covered are listed.
Already covered (not repeated): TSYS TS2, First Data Cards (legacy); Marqeta,
Galileo (modern). All rows `realizes = Card Processing`.

Legacy additions (incumbent issuer/acquirer card platforms still widely run):

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| FIS Card Management | card-system (legacy) | Card Processing | — | FIS | FIS issuer card-management / processing platform (incl. the Payments One / former CMS issuer stack) covering credit, debit and prepaid card issuing, authorization and account servicing. | FIS CMS, FIS Payments One, FIS Card Processing | https://www.fisglobal.com/products/payments-ecosystem ; https://www.celent.com/en/insights/643377026 |
| Fiserv OmniPay | card-system (legacy) | Card Processing | — | Fiserv | Acquirer/merchant card-processing platform providing authorization switching, clearing, settlement, billing, funding, dispute management and reporting for processors and sponsor banks. | OmniPay, Fiserv OmniPay Platform | https://docs.fiserv.dev/private/docs/omnipay-boarding-intro ; https://www.finextra.com/pressarticle/25002/omnipay-upgrades-to-latest-fidelity-national-processing-system |
| Fiserv Optis | card-system (legacy) | Card Processing | — | Fiserv | Fiserv issuer card-processing platform for credit card programs (account management, authorization, billing and statementing), one of the major US issuer-processing platforms profiled for modernization. | Optis, Fiserv Optis Platform | https://www.celent.com/en/insights/643377026 ; https://www.fiserv.com/en-ap/who-we-serve/financial-institutions/issuing-solutions.html |

Modern additions (supersede legacy card platforms per the supersedes rule):

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| Thredd | card-system (modern) | Card Processing | First Data Cards | Thredd | Cloud, API-first issuer-processing platform (formerly Global Processing Services / GPS Apex) for prepaid, debit, credit and virtual card programmes, with card controls, risk/fraud and wallet services. | GPS, Global Processing Services, GPS Apex | https://www.thredd.ai/solutions/issuer-processing ; https://docs.thredd.com/keyconcepts/Content/Key_Concepts/GPS_Role.htm |
| Lithic | card-system (modern) | First Data Cards | — | Lithic | Developer-first, API-first issuer processor providing programmable card issuing, money movement and precise debit/credit ledgers with full program observability; offers processing-only deployment. | Lithic Issuer Processing, Privacy.com | https://www.lithic.com/ ; https://www.lithic.com/blog/issuer-processors-101-what-they-are-and-how-they-power-card-programs |
| i2c | card-system (modern) | TSYS TS2 | — | i2c Inc | Cloud-native unified issuer-processing platform supporting credit, debit and prepaid programs on a single configurable stack with building-block APIs for card programs. | i2c Inc, i2c Issuer Processing | https://www.i2cinc.com/what-we-do/issuer-processing/ ; https://dashdevs.com/blog/top-card-issuing-providers/ |
| Pismo | card-system (modern) | TSYS TS2 | — | Visa (Pismo) | Cloud-native, network-agnostic issuer-processing and core-banking platform (acquired by Visa) covering card issuing, authorizations and a high-throughput ledger for all card product types via APIs. | Pismo Platform, Visa Global Issuer Processing | https://www.pismo.io/ ; https://developers.pismo.io/pismo-docs/docs/card-issuing-basics |
| Episode Six | card-system (modern) | First Data Cards | — | Episode Six | Modern, configurable issuer-processing and ledger platform (TRITIUM) enabling instant card issuance, payment processing, spend limits and merchant-category controls across card and wallet products. | Episode Six TRITIUM, E6 | https://episodesix.com/solutions/issuer-processing ; https://www.cbinsights.com/company/episode-six |

Notes:
- `supersedes` targets are limited to the two registry-existing legacy card
  platforms (TSYS TS2, First Data Cards); modern issuer processors are mapped to
  the legacy platform whose programs they most directly displace (fintech/prepaid
  and debit programs -> First Data Cards; credit/large-issuer programs -> TSYS TS2).
- The three new legacy rows (FIS Card Management, Fiserv OmniPay, Fiserv Optis)
  are distinct, well-documented platforms not duplicating TSYS TS2 / First Data
  Cards; OmniPay is acquirer-side while Optis/FIS are issuer-side.
- Marqeta and Galileo are intentionally not repeated (already in the registry).
