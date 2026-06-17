---
id: olap-cube-engine
title: OLAP Cube Engine
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["OLAP Engine", "Multidimensional Model Engine", "Analysis Services Engine"]
status: draft
sources: ["https://www.atscale.com/", "https://www.databricks.com/blog/what-are-business-intelligence-platforms"]
---

# OLAP Cube Engine

**Definition.** OLAP Cube Engine provides multidimensional modelling and fast slice-and-dice aggregation over dimensions and measures for interactive analytical queries.
**Also known as:** OLAP Engine, Multidimensional Model Engine, Analysis Services Engine.

## Relationships
- OLAP Cube Engine is defined in the Data & Analytics domain.
- OLAP Cube Engine is derived from Analytics Platform.
- OLAP Cube Engine is related to Semantic Layer Service.
- OLAP Cube Engine is related to BI & Reporting Service.

## Details
OLAP Cube Engine organises data as a multidimensional cube of measures intersected by dimensions and hierarchies, pre-aggregating combinations so users can slice, dice, drill down, and pivot with sub-second response. Tools query cubes through multidimensional expressions such as MDX, and engines like SQL Server Analysis Services materialise aggregations or compute them on the fly. Modern "logical OLAP" approaches push the multidimensional model down to a cloud warehouse rather than copying data into a proprietary cube, blending cube semantics with live warehouse data. This serves finance and risk reporting where consistent hierarchical roll-ups across time, entity, and product are required.

## References
- [AtScale: multidimensional analytics platform](https://www.atscale.com/)
- [Databricks: What are business intelligence platforms?](https://www.databricks.com/blog/what-are-business-intelligence-platforms)
