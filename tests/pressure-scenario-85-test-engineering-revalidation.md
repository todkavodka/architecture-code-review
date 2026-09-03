# PS-85 — Test Engineering impact-driven revalidation

## Purpose

Route freshness by changed source view instead of restarting every capability.

## Change sets and required behavior

```text
A: tests only changed
B: service implementation/OpenAPI changed
C: consumer repository changed; service repository unchanged
```

Expected routing is respectively `TM/MAT/GAP` impact without automatic BC
invalidity; affected `IMPLEMENTED`/`DECLARED` views with CC/BC impact analysis;
and affected `CONSUMED` views with consumer-facing simulator/E2E impact.

## Pre-remediation baseline

Static inspection of the unchanged revalidation reference found umbrella
freshness and project-change rules but no Test Engineering source bindings or
view-specific routing. It did not distinguish tests-only changes from service
or consumer changes for BC/CC/simulator/E2E purposes. Independent readers could
therefore perform global revalidation or apply a service-only freshness model.

Evidence type: static contract inspection; no executable coordinator exists.

Observed verdict: `PS85_RED_GLOBAL_REVALIDATION` and
`PS85_RED_SERVICE_ONLY_FRESHNESS_MODEL`.

## Verdict vocabulary

`PS85_GREEN_IMPACT_DRIVEN_REVALIDATION` / `PS85_INCONCLUSIVE`
