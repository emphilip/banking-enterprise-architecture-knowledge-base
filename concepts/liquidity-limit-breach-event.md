---
id: liquidity-limit-breach-event
title: Liquidity Limit Breach Event
type: event
domain: Finance & Treasury
aliases: ["Liquidity Breach Event", "Buffer Breach Event"]
status: draft
sources: ["https://www.tcs.com/what-we-do/industries/banking/white-paper/next-gen-cash-liquidity-management-treasury-operations", "https://analystprep.com/study-notes/frm/part-2/intraday-liquidity-risk-management/"]
---

# Liquidity Limit Breach Event

**Definition.** Liquidity Limit Breach Event is the business event raised when the projected liquidity position breaches an LCR / NSFR or internal limit. Liquidity Limit Breach Event escalates funding decisions in the finance and treasury function.

**Also known as:** Liquidity Breach Event, Buffer Breach Event.

## Relationships
- Liquidity Limit Breach Event is related to the Finance & Treasury domain.
- Liquidity Limit Breach Event causes Decide Funding Action.
- Liquidity Limit Breach Event mentions Assess Liquidity Buffers.

## Details
Liquidity Limit Breach Event fires when buffer assessment of the projected Liquidity Position finds a regulatory LCR or NSFR shortfall or a breach of an internal liquidity limit. The event flags the breach, records the breached limit and severity, and escalates to the treasurer for action. Liquidity Limit Breach Event is the branch trigger that drives the Decide Funding Action step within Cash & Liquidity Management, prompting funding, placement or buffer-rebuild decisions to bring the position back within limits, and supports the audit trail for limit governance and treasurer escalation.

## References
- https://www.tcs.com/what-we-do/industries/banking/white-paper/next-gen-cash-liquidity-management-treasury-operations
- https://analystprep.com/study-notes/frm/part-2/intraday-liquidity-risk-management/
