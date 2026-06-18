---
id: notification-template-manager
title: Notification Template Manager
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Message Template Service", "Content Template Manager", "Notification Authoring"]
status: draft
sources: ["https://www.courier.com/blog/how-to-build-a-notification-center-for-web-and-mobile-apps", "https://codelit.io/blog/notification-system-architecture"]
---

# Notification Template Manager

**Definition.** Notification Template Manager authors, versions, and localizes channel-specific message templates with variable substitution so consistent content can be rendered across delivery channels.
**Also known as:** Message Template Service, Content Template Manager, Notification Authoring.

## Relationships
- Notification Template Manager is defined in the Integration & APIs domain.
- Notification Template Manager is derived from Notification Services.
- Notification Template Manager is related to Channel Preference Router.

## Details
Notification Template Manager stores templates per channel (SMS plain text, HTML email, push payload) and per locale, using a templating syntax (e.g. Handlebars/Liquid) for variable interpolation, conditionals, and partials so a single logical notification renders correctly everywhere. It versions templates with draft/publish states, supports preview with sample data, and centralizes branding and legal disclosures. In banking it keeps statement, OTP, and alert wording compliant and consistent, and downstream delivery services request the rendered template by key and locale at send time.

## References
- [How to build a notification center](https://www.courier.com/blog/how-to-build-a-notification-center-for-web-and-mobile-apps)
- [Notification system architecture](https://codelit.io/blog/notification-system-architecture)
