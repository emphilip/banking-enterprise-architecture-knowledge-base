---
id: sweep-rule-execution
title: Sweep Rule Execution
type: business-capability
domain: Deposits & Accounts
level: L4
aliases: ["Sweep Execution", "Balance Sweep Run"]
status: draft
sources: ["https://www.openriskmanual.org/wiki/Category:BIAN_Service_Domain", "https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-204"]
---

# Sweep Rule Execution

**Definition.** Sweep Rule Execution evaluates and executes target-balance and zero-balance sweep rules across linked accounts, supporting the standing-instruction behaviour of the BIAN Current Account service domain.
**Also known as:** Sweep Execution, Balance Sweep Run.

## Relationships
- Sweep Rule Execution is defined in the Deposits & Accounts domain.
- Sweep Rule Execution is derived from Standing Orders & Sweeps.
- Sweep Rule Execution depends on the Core Banking Processing capability.

## Details
The BIAN Current Account standing-instruction behaviour runs the sweep; zero-balance and target-balance sweeps between checking and a savings sub-account are limited by the account-classification provisions of Regulation D (12 CFR 204).

## References
- [BIAN Service Domain](https://www.openriskmanual.org/wiki/Category:BIAN_Service_Domain)
- [Regulation D 12 CFR Part 204](https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-204)
