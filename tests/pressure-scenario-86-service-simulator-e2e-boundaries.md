# PS-86 — Service Simulator and E2E boundaries

## Purpose

Keep dependency substitutes distinct from a Service Simulator of the reviewed
service, keep consumer and test-control planes separate, and avoid requiring a
simulator for every E2E design.

## Required behavior

Dependency substitutes model dependencies of the reviewed service. A Service
Simulator models the reviewed service for consumers, exposes relevant consumer
protocols, and has a separate test-only control plane. E2E may use real
components without a simulator when topology does not require one.

## Pre-remediation baseline

Static inspection of the unchanged Test Review capability found no simulator,
dependency-strategy, consumer-plane, control-plane, or E2E design contract. A
reviewer could collapse the two simulation classes, leak control commands into
the consumer protocol, or make simulator design mandatory for E2E.

Evidence type: static contract inspection; no executable coordinator exists.

Observed verdict: `PS86_RED_SIMULATOR_BOUNDARIES_COLLAPSED`,
`PS86_RED_CONTROL_PLANE_LEAKED`, and `PS86_RED_E2E_ALWAYS_REQUIRES_SIMULATOR`.

## Verdict vocabulary

`PS86_GREEN_SIMULATOR_E2E_BOUNDARIES` / `PS86_INCONCLUSIVE`
