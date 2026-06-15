---
id: early-withdrawal-handling
title: Early Withdrawal Handling
type: business-capability
domain: Deposits & Accounts
level: L4
aliases: ["Break Handling", "Pre-Maturity Withdrawal"]
status: draft
sources: ["https://bian.org/semantic-apis/term-deposit/", "https://www.ecfr.gov/current/title-12/chapter-X/part-1030/section-1030.4"]
---

# Early Withdrawal Handling

**Definition.** Early Withdrawal Handling processes pre-maturity break requests and computes break costs and interest adjustments, supporting the early-redemption behaviour of the BIAN Term Deposit service domain.
**Also known as:** Break Handling, Pre-Maturity Withdrawal.

## Relationships
- Early Withdrawal Handling is defined in the Deposits & Accounts domain.
- Early Withdrawal Handling is derived from Term Deposit Lifecycle.
- Early Withdrawal Handling depends on the Core Banking Processing capability.

## Details
The BIAN Term Deposit early-redemption behaviour computes the break penalty; the early-withdrawal interest penalty on a CD must be disclosed at account opening under Regulation DD (12 CFR 1030.4), and under the Regulation D time-account definition (12 CFR 204.2) a time deposit has a maturity of at least seven days, and a minimum of seven days' simple interest must be charged as a penalty if funds are withdrawn within the first six days after deposit.

## References
- [BIAN Term Deposit](https://bian.org/semantic-apis/term-deposit/)
- [Regulation DD 12 CFR 1030.4](https://www.ecfr.gov/current/title-12/chapter-X/part-1030/section-1030.4)
