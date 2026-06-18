---
id: amazon-sns
title: Amazon SNS
type: modern-system
domain: Integration & APIs
maturity: emerging
aliases: ["Simple Notification Service", "AWS SNS"]
status: draft
sources: ["https://aws.amazon.com/sns/"]
---

# Amazon SNS

**Definition.** Amazon SNS is a fully managed publish-subscribe messaging and notification service from Amazon Web Services for application-to-application and application-to-person delivery via SMS, push, email, and HTTP/SQS endpoints with fan-out.
**Also known as:** Simple Notification Service, AWS SNS.

## Relationships
- Notification Services depends on Amazon SNS.
- Amazon SNS supersedes Legacy SMS Gateway.
- Amazon SNS is related to Amazon SES.

## Details
Amazon SNS provides pub/sub topics that fan out messages to multiple subscribers, supporting application-to-application delivery to SQS, Lambda, and HTTP endpoints, and application-to-person delivery via SMS, push, and email. It is fully managed and elastic. This modernizes fixed-capacity on-premises notification gateways with managed cloud delivery.

## References
- [Amazon SNS](https://aws.amazon.com/sns/)
- [Amazon SNS FAQs](https://aws.amazon.com/sns/faqs/)
