---
id: run-consolidation
title: Run Consolidation
type: process-step
process: Financial Close
order: 5
aliases: ["Consolidate Group", "Process Consolidation"]
status: draft
sources: ["https://www.netsuite.com/portal/resource/articles/accounting/consolidation-accounting.shtml", "https://datasights.co/financial-consolidation-and-close/"]
---

# Run Consolidation

**Definition.** Run Consolidation aggregates entity trial balances with elimination adjustments into the consolidated group position and produces the adjusted Trial Balance.

## Relationships
- Run Consolidation is defined in the Financial Close process.
- Run Consolidation causes Prepare Consolidated Statements.
- Run Consolidation depends on the Financial Reporting capability.
- Run Consolidation mentions Financial Controller.
- Run Consolidation mentions Trial Balance.

## Details
The Group Accountant aggregates entity trial balances with elimination journals into the consolidated position. Inputs are entity trial balances and elimination journals; outputs are consolidated balances and the adjusted Trial Balance. Controls include IFRS 10 consolidation and consolidation worksheet review.

## References
- [Consolidation accounting](https://www.netsuite.com/portal/resource/articles/accounting/consolidation-accounting.shtml)
- [Financial consolidation and close](https://datasights.co/financial-consolidation-and-close/)
