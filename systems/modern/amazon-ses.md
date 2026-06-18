---
id: amazon-ses
title: Amazon SES
type: modern-system
domain: Integration & APIs
maturity: emerging
aliases: ["Simple Email Service", "AWS SES"]
status: draft
sources: ["https://aws.amazon.com/ses/"]
---

# Amazon SES

**Definition.** Amazon SES is a fully managed, high-throughput cloud email service from Amazon Web Services for transactional and notification email and inbound receiving, with deliverability, bounce and complaint handling, and SNS event integration.
**Also known as:** Simple Email Service, AWS SES.

## Relationships
- Notification Services depends on Amazon SES.
- Amazon SES supersedes Legacy SMS Gateway.
- Amazon SES is related to Amazon SNS.

## Details
Amazon SES delivers transactional and notification email at high throughput with configuration sets, dedicated IPs, and reputation and deliverability tooling, plus bounce and complaint handling surfaced through SNS events. Banks use it for statements, alerts, and confirmations. This modernizes SMTP-based on-premises mail gateways with managed cloud email.

## References
- [Amazon SES](https://aws.amazon.com/ses/)
- [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)
