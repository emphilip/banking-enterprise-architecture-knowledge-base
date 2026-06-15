---
id: screen-sanctions
title: Screen Sanctions
type: process-step
process: Payment Processing
order: 3
aliases: ["Watchlist Screening Step", "OFAC Screening"]
status: draft
sources: ["https://www.statestreet.com/web/insights/articles/documents/state-street-client-guide-to-iso-20022-2025.pdf", "https://www.iso20022payments.com/cbpr/pacs-008-serial-method/"]
---

# Screen Sanctions

**Definition.** Screen Sanctions screens debtor, creditor and message data against sanctions/watchlists and holds and escalates hits.
**Also known as:** Watchlist Screening Step, OFAC Screening.

## Relationships
- Screen Sanctions is defined in the Payment Processing process.
- Screen Sanctions causes Authorize Payment.
- Screen Sanctions depends on the Transaction Monitoring Platform capability.
- Screen Sanctions mentions Compliance Screening Officer.

## Details
The Compliance Screening Officer adjudicates screening hits. Inputs are the validated payment order; outputs are a screened payment order. The sanctions screening control branches on a hit (hold/escalate) versus clear. Hits are held and escalated for manual review before release.

## References
- [State Street ISO 20022 client guide](https://www.statestreet.com/web/insights/articles/documents/state-street-client-guide-to-iso-20022-2025.pdf)
- [CBPR+ pacs.008 serial method](https://www.iso20022payments.com/cbpr/pacs-008-serial-method/)
