---
title: Systems and Integration Reference
type: reference
domain: banking-and-payments
tags: [reference, systems, integration, genericisation, vendor-abstraction, card-platform, retail-banking]
aliases: [Systems Reference, Integration Patterns, Genericisation Map, System Roles]
---

# Systems and Integration Reference

The process flows in this library are **generalized** from a real Canadian card-issuer integration program. Brand- and vendor-specific system names in the source diagrams have been abstracted to **generic system roles** so the content applies to an average Canadian retail bank. This note records those roles and the genericisation mapping, mirroring the integration-pattern reference used across the companion onboarding library.

## Generic System Roles

| Generic role | What it does in these flows | Capability home |
|---|---|---|
| **Card processing platform** | The core card management/processing system of record for accounts, options, rates, benefits, rewards, and operator security. Changes are applied via the [[Submit Options Maintenance Request Flow\|OMR]] process across validation and production environments. | [[Cards]] |
| **Product catalogue** | The product book of record; holds product instances, affinity, benefit, reward, pricing, and source-code definitions in Draft/Inactive/Active states. | [[Cards]] / Enterprise Support — Books of Record |
| **Loyalty platform** | Third-party loyalty processing; holds the loyalty components of rewards and program/tier data. | [[Loyalty]] / [[Rewards]] |
| **Offer & order management system (OMS)** | Holds offer definitions and customer dispositions; provides available/eligible offers at presentment and orchestrates fulfilment. | [[Offers]] |
| **Business rules engine** | Real-time ranking of account entitlements, offer eligibility, and availability; also a marketing-analytics rules engine for disposition analytics. | [[Offers]] (CEN-OFR-02) |
| **Workflow / BPM platform** | Drives screens, approvals, and case routing in the product-setup and presentment flows. | Operations — Workflow & Rules |
| **Content management system (CMS)** | Authoring/publishing of secure-site content, public-site campaign content, and site-refresh content. | [[Content Management]] |
| **Campaign content management system** | The public/sales-site CMS for card-acquisition campaign content across channel zones. | [[Content Management]] |
| **Customer communications / disclosure system** | Manages and serves disclosure messages/templates at content-authoring and offer-presentment time. | [[Content Management]] / ONB-CCC |
| **Pricing engine** | Supplies rate values to campaign content and pricing setup. | [[Servicing - Monetary]] |
| **Customer MDM** | Master customer/account data, read for landing-page assembly and campaign enrichment. | Enterprise Support — Books of Record |
| **Marketing data warehouse** | Audience enrichment with contact and campaign-offer information. | Enterprise Support — Data & Analytics |
| **Operator security administration system** | Administers operator security profiles/entitlements, synced to the card-platform security store. | Identity, Auth & Access |
| **Credit decisioning / behaviour-scoring engine** | Decisioning used for penalty-pricing strategy and new-customer adjudication. | Fraud & Risk — Credit Risk / Onboarding — Adjudication |
| **Prospect / lead management system** | Source of prospect lists for acquisition campaigns. | [[Marketing and Sales]] |
| **Originations / adjudication system** | Adjudicates new customers acquired through phone acquisition. | Onboarding & Origination |
| **List data management system** | Holds and updates campaign list data and disposition files. | [[Contact Management]] |
| **Third-party telemarketing / print / statement vendors** | External delivery channels for outbound campaigns. | [[Contact Management]] |

## Genericisation Mapping (source → generic)

| Source name (TD / MBNA deck) | Generalized to |
|---|---|
| MBNA | The bank's credit-card line of business / a generic Canadian retail bank |
| TD / "TD Insurance" | The bank / the bank's insurance arm |
| TSYS, TS2 | Card processing platform (and its security database) |
| TLP | Loyalty platform |
| OOMS | Offer & order management system (OMS) |
| PEGA | Workflow / BPM platform (agent workflow/desktop) |
| OTIS (MOOP/MOTP/MOHP/MOCO/MOOO/SAC screens, T32 debit module) | Operator security administration system / operator security profiles |
| TRIAD (+ Triad rules repository) | Credit decisioning / behaviour-scoring engine (+ decisioning rules repository) |
| Thunderhead One | Customer communications / disclosure management system |
| BLAZE (Marketing Analytics) | Business rules engine (marketing-analytics rules) |
| CornerStone | Prospect / lead management system |
| OM4 | Originations / adjudication system |
| PC / MDM, Customer MDM | Product catalogue / customer MDM |
| CPCMS | Campaign content management system (public site) |
| CMS / Disclosure Management Tool | Content management system / disclosure management system |
| POE (Pricing Offering Engine) | Pricing engine |
| "Bacardi" | List data management system |
| CECOM / CFACE / CMAIL / CRETL | Channel content zones (Web / POS-portal / Referral / Retail-front) |
| CACC (Cards Info / Control Data / Mapping) | Card product (Info / Control Data / Mapping) screens |
| World Card / WorldCard | Premium (World-tier) card product |
| MasterCard (benefits) | Card-network (benefits) |
| ARQ ID / ARQ1 / ARQ2 | Reward ID / primary & secondary reward attributes (reward code) |
| TSP | Pricing strategy code |
| SAC | Account-control / security-access code (per context) |
| OMR | Options Maintenance Request (a controlled card-platform change request) |
| V-Region / P-Region | Validation environment / production environment |
| Credit Wise | Credit-protection insurance product |
| TFN | Toll-free number |

## Integration Patterns Observed

- **Catalogue is the book of record; the platform is downstream.** Product/offer changes are authored in the product catalogue (Draft → Inactive/Active) and propagated to the card processing platform via the [[Submit Options Maintenance Request Flow\|OMR]] — never written platform-first.
- **Two-environment promotion.** Card-platform changes are applied and reconciled in a validation environment before production, with automated extract-file reconciliation at each stage.
- **Offers are engine-eligible, disposition-tracked.** Presentment always retrieves *eligible* offers (rules engine + OMS) and always writes back a disposition to offer/contact history.
- **Disclosures are single-sourced.** Content and offer flows reference managed disclosure templates rather than embedding legal text — see [[Disclosure Management Flow]] and [[Canadian Regulatory Context]].
- **Editor → Publisher separation.** Content publishing splits authoring from release, with legal approval and audit archival before go-live.

## Related

[[Generic Multi-Functional Bank Capability Model]] · [[Glossary]] · [[Process-to-Capability Mapping Matrix]] · [[Canadian Regulatory Context]]
