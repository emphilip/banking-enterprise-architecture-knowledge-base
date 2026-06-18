---
id: saga-orchestration-service
title: Saga Orchestration Service
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Saga Orchestrator", "Distributed Transaction Coordinator", "Long-Running Saga Manager"]
status: draft
sources: ["https://docs.camunda.io/docs/components/concepts/concepts-overview/", "https://camunda.com/platform/"]
---

# Saga Orchestration Service

**Definition.** Saga Orchestration Service coordinates long-running distributed transactions across microservices, sequencing local steps and triggering compensating actions to preserve consistency on failure.
**Also known as:** Saga Orchestrator, Distributed Transaction Coordinator, Long-Running Saga Manager.

## Relationships
- Saga Orchestration Service is defined in the Integration & APIs domain.
- Saga Orchestration Service is derived from Workflow Orchestration.
- Saga Orchestration Service is related to Integration Message Broker.

## Details
Saga Orchestration Service replaces distributed two-phase commit with the saga pattern: it executes a sequence of local transactions and, when a later step fails, invokes compensating transactions to undo prior committed steps, achieving eventual consistency without locking across services. An orchestrated saga uses a central coordinator (often a BPMN process with compensation handlers) rather than choreographed events, making the flow and rollback explicit. In banking it spans payment, ledger, and notification services so a failed posting cleanly reverses an earlier debit reservation.

## References
- [Camunda concepts overview](https://docs.camunda.io/docs/components/concepts/concepts-overview/)
- [Camunda platform](https://camunda.com/platform/)
