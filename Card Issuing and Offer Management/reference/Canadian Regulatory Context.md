---
title: Canadian Regulatory Context
type: reference
domain: banking-and-payments
tags: [reference, regulatory, canada, disclosure, casl, consent, creditor-insurance, privacy]
aliases: [Regulatory Context, Canadian Regulation, Compliance Context]
---

# Canadian Regulatory Context

The regulatory backdrop relevant to the **content, disclosure, offer, and insurance** flows in this library, for a generic Canadian retail bank's card-issuing business. This is generalized context, not legal advice; specifics are configured per product and province.

## Cost-of-Borrowing & Card Disclosure

- **Cost-of-borrowing disclosure (Bank Act / Cost of Borrowing (Banks) Regulations).** Credit-card solicitations, applications, and account-opening material must disclose interest rates, fees, grace period, and other prescribed cost-of-borrowing information in an **information box**. This drives the rate/disclosure content authored in [[Content Management CPCMS Flow]] and [[Disclosure Management Flow]] and read at presentment in the offer flows.
- **Promotional / introductory rates.** Promotional pricing (e.g., balance-transfer offers in [[Pricing Offer Presentment Flow]]) must disclose the promotional rate, its duration, and the rate that applies afterward.
- **Disclosure-before-decision pattern.** Disclosures are presented and acknowledged **before** the customer commits — reflected by the disclosure steps preceding acceptance in the offer-presentment flows.

## Marketing Consent (CASL)

- **Canada's Anti-Spam Legislation (CASL)** governs commercial electronic messages (email, SMS). Outbound email/SMS campaigns require **express or implied consent**, sender identification, and a working unsubscribe mechanism.
- Consent state is held and honoured by [[Contact Management|Consent Tracking (CEN-CON-06)]] and checked before outreach in [[Apply List to Offers Flow]], [[Direct Marketing Campaign Flow]], and [[Publish Rewards Flow]]. List scrubbing includes consent/suppression filtering.

## Creditor / Credit-Protection Insurance

- Creditor insurance (balance/payment protection) is offered with **suitability and disclosure** obligations: the product must be explained, eligibility checked, and the customer must be able to **decline without penalty**. The eligibility/needs and decline paths in [[Add Insurance Product Phone Channel Flow]] and [[Insurance Offer Presentment Flow]] reflect this.
- Enrolment requires **explicit consent to the disclosure** (recorded), as in [[Value-Add Offers Flow]]. Certificates of insurance are produced on issuance ([[Insurance|PLB-INS-11]]).
- Provincial insurance regulators and the distribution rules for incidental/creditor insurance apply alongside federal market-conduct expectations.

## Privacy & Consent (PIPEDA)

- **PIPEDA** governs collection, use, and disclosure of personal information. Customer data used for enrichment, targeting, and presentment ([[Online Campaign Flow]], data-warehouse enrichment) must be within the consented purposes.
- Disposition and offer-history data ([[Contact Management|CEN-CON-03]]) is personal information subject to the same handling and retention expectations.

## Bilingual Obligations

- Card content and disclosures are authored in **English and French** (the CPCMS and CMS flows capture French content and validate French formatting), consistent with federal and Quebec (incl. French-language) requirements.

## Market Conduct

- **FCAC** (Financial Consumer Agency of Canada) oversees federal financial-institution market-conduct obligations, including clear disclosure, complaint handling, and fair selling practices — relevant to how offers are presented and how declines/rebuttals are handled across the presentment flows.

## Related

[[Disclosure Management Flow]] · [[Contact Management]] · [[Insurance]] · [[Offers]] · [[Glossary]]
