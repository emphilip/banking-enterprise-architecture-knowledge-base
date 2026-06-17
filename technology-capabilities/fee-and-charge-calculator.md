---
id: fee-and-charge-calculator
title: Fee & Charge Calculator
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Fee Calculation Service", "Charge Computation Engine", "Relationship Pricing Service"]
status: draft
sources: ["https://www.celent.com/en/insights/enterprise-pricing-and-product-management-in-banking-next-generation-platforms-1", "https://www.amdocs.com/products-services/product-pricing-catalog-banking"]
---

# Fee & Charge Calculator

**Definition.** Fee & Charge Calculator computes fixed, tiered, percentage-based and relationship-based fees and charges per product and customer segment, applying price-list effectivity and waiver rules at transaction and cycle level.
**Also known as:** Fee Calculation Service, Charge Computation Engine, Relationship Pricing Service.

## Relationships
- Fee & Charge Calculator is defined in the Core Processing domain.
- Fee & Charge Calculator is derived from Product & Pricing Engine.
- Fee & Charge Calculator is related to Interest & Charges Engine.

## Details
Fee & Charge Calculator evaluates a price list against a transaction or billing cycle: it resolves the applicable fee schedule, applies fixed, tiered or ad-valorem rates, then applies relationship-pricing benefits (balance-bundle discounts, fee waivers) keyed to the customer relationship rather than a single account. Celent's enterprise pricing analysis describes relationship-based and dynamic pricing as the differentiator of next-generation pricing platforms, and Amdocs' catalogue binds price lists to products with effectivity dates so the calculator picks the rate in force at the event date. Computed charges are handed to Interest & Charges Engine for posting.

## References
- [Celent enterprise pricing and product management](https://www.celent.com/en/insights/enterprise-pricing-and-product-management-in-banking-next-generation-platforms-1)
- [Amdocs Product, Pricing & Catalog for Banking](https://www.amdocs.com/products-services/product-pricing-catalog-banking)
