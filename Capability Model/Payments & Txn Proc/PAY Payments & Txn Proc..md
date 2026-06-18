---
title: Payments & Txn Proc.
type: capability-model
level: L0
capability-id: PAY
domain: banking-and-payments
tags: [capability-model, L0, payments-txn-proc]
aliases: [PAY, Payments & Txn Proc.]
---

# Payments & Txn Proc. (PAY)

**Parent:** [[00 - Master Capability Model]]

Payments & Txn Proc. moves money in and out of the bank and processes the card and payment transactions that flow across it — money-movement rails, authorization and clearing, settlement, payment servicing, merchant acquiring, internal movement, and collections.

## L1 Capability Groups

| ID | Capability Group | L2s | Summary |
|---|---|---|---|
| PAY-MMV | [[PAY-MMV Money Movement\|Money Movement]] | 6 | Money Movement covers the payment rails the bank uses to move funds — ACH, wires, real-time rails, e-transfer, and bill pay |
| PAY-TXN | [[PAY-TXN Txn Processing\|Txn Processing]] | 6 | Txn Processing covers authorization, clearing, and the chargeback, reversal, and exception handling of card and payment transactions |
| PAY-STL | [[PAY-STL Settlement\|Settlement]] | 6 | Settlement covers network and merchant settlement, payout allocation, customer payment posting, and settlement reconciliation and reporting |
| PAY-PSV | [[PAY-PSV Payment Servicing\|Payment Servicing]] | 6 | Payment Servicing covers mobile pay, pre-authorized debits, remittances, installments, and the fees and tracking around payments |
| PAY-MAQ | [[PAY-MAQ Merchant Acquisition\|Merchant Acquisition]] | 6 | Merchant Acquisition covers onboarding and integrating merchants, configuring POS, and the reporting, benchmarking, and contracts behind acquiring |
| PAY-IMV | [[PAY-IMV Internal Movement\|Internal Movement]] | 6 | Internal Movement covers transfers and cash movements within the bank — internal transfers, core deposits, cash handling, and book transfers |
| PAY-COL | [[PAY-COL Collections\|Collections]] | 6 | Collections covers past-due and overlimit management, hardship programs, recovery, skip-tracing, write-off, and debt sale |

## Related

[[00 - Master Capability Model]]
