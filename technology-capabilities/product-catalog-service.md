---
id: product-catalog-service
title: Product Catalog Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Product Catalogue Service", "Product Definition Service", "Universal Product Catalog"]
status: draft
sources: ["https://www.amdocs.com/products-services/product-pricing-catalog-banking", "https://www.oracle.com/financial-services/banking/flexcube/core-banking-software/"]
---

# Product Catalog Service

**Definition.** Product Catalog Service maintains the central, configuration-driven catalogue of deposit and lending product definitions, variants and eligibility attributes so new products are launched mostly through configuration rather than code.
**Also known as:** Product Catalogue Service, Product Definition Service, Universal Product Catalog.

## Relationships
- Product Catalog Service is defined in the Core Processing domain.
- Product Catalog Service is derived from Product & Pricing Engine.
- Product Catalog Service is related to Account Lifecycle Manager.

## Details
Product Catalog Service externalises product structure as configuration. A catalogue entry carries product type, currency eligibility, term and balance bands, eligibility rules and the price-list and interest-table references the product binds to. Oracle FLEXCUBE and Amdocs catalogue platforms model a product hierarchy with reusable components and effectivity dating, so a new variant is created by cloning and parameterising an existing definition rather than writing posting or pricing code. Account Lifecycle Manager consumes the catalogue when instantiating accounts of a given product type.

## References
- [Amdocs Product, Pricing & Catalog for Banking](https://www.amdocs.com/products-services/product-pricing-catalog-banking)
- [Oracle FLEXCUBE core banking](https://www.oracle.com/financial-services/banking/flexcube/core-banking-software/)
