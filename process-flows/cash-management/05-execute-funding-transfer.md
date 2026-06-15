---
id: execute-funding-transfer
title: Execute Funding Transfer
type: process-step
process: Cash Management
order: 5
aliases: ["Sweep Execution", "Funding Execution"]
status: draft
sources: ["https://www.nilus.com/glossary/cash-concentration", "https://www.atlar.com/guides/how-to-enable-growth-with-cash-pooling"]
---

# Execute Funding Transfer

**Definition.** Execute Funding Transfer generates and releases sweep/pooling/funding payment instructions to move cash to target balances.
**Also known as:** Sweep Execution, Funding Execution.

## Relationships
- Execute Funding Transfer is defined in the Cash Management process.
- Execute Funding Transfer causes Monitor Liquidity Position.
- Execute Funding Transfer depends on the Payment Orchestration capability.
- Execute Funding Transfer mentions Treasury Cash Manager.

## Details
The Treasury Cash Manager releases funding instructions. Inputs are the funding decision; outputs are funding instructions executing sweeps and pooling. Controls include sweep parameters and dual authorization.

## References
- [Cash concentration glossary](https://www.nilus.com/glossary/cash-concentration)
- [Cash pooling guide](https://www.atlar.com/guides/how-to-enable-growth-with-cash-pooling)
