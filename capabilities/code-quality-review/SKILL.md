---
name: code-quality-review
description: Use when assessing implementation-quality mechanisms for material maintainability, reliability, testability, lifecycle, resource, concurrency, dependency, localization, framework, or related consequences.
---

# Code Quality Review

Code Quality Review evaluates implementation-quality mechanisms that have a
material consequence. It is a distinct capability from Architecture Review and
Test Engineering.

## Semantic authority

Code Quality Review owns:

- `CQ-*` accepted Code Quality findings;
- `CQRA-*` Code Quality remediation actions;
- bounded Code Quality assessment/session coverage state.

The semantic contract and lifecycle are defined in:

- [Code Quality contract](references/code-quality-contract.md);
- [Code Quality lifecycle](references/code-quality-lifecycle.md).

This entrypoint references those contracts; it does not redefine them. A
candidate, tool warning, metric, or `EV-*` observation is not itself a
semantic finding. An accepted finding requires the evidence and materiality
adjudication specified by the referenced contract.

## Factual substrate and prerequisites

Code Quality Review reuses the shared factual substrate:

- `WS-*` worksets for bounded review scope;
- `EV-*` addressable source observations;
- relevant accepted, sufficiently fresh `STM` facts where system-level
  context is required.

Code Quality does not create a private factual model, rewrite `STM`, or treat
`working/INDEX.md` as semantic authority. Missing or stale prerequisites block
only the dependent interpretation through the existing shared workflow.

## Ownership boundaries

`CQ-*` is not an Architecture `RF-*` finding and is not Test Engineering
authority (`BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, or `TASK-*`). `CQRA-*`
is Code Quality remediation authority and is not a Test Engineering `TASK-*`
or a generic project-management record.

Code Quality must not create, mutate, resolve, downgrade, or replace
Architecture or Test Engineering authority. A local quality concern remains
Code Quality-owned unless the existing Architecture/security semantics require
separate adjudication. There is currently no dedicated Security Review
capability; security-relevant concerns may retain a CQ interpretation and may
later be correlated or escalated to existing Architecture/security authority.

Tool output, including linter, AST, dependency, framework, language-server,
scanner, grep, or agent output, is evidence or a candidate only:

```text
tool output != accepted CQ-* finding
candidate != semantic authority
```

## Modes and implementation boundary

The approved capability design supports `NEW`, `EXTEND`, `REVALIDATE`, and
`RESUME`. Shared orchestration, persistent scope/output restoration, coverage
orchestration, impact-driven revalidation, and CQRA freshness execution are
defined by the repository contracts referenced by this capability. This
entrypoint summarizes those integrations without duplicating their detailed
rules.

## Outputs and projections

Semantic CQ findings remain authority, not a projection or output toggle.
Each listed Code Quality document is a `DERIVED_PROJECTION` of accepted CQ
authority and is also `USER_SELECTABLE`. Derived describes the document's
source relationship; it does not mean automatically selected, mandatory, or
always generated. This applies to Code Quality Findings View/Report, Code
Quality Summary, Maintainability Hotspots, and Roadmap Contribution. Generated
outputs must use the shared Stage B projection lifecycle; no parallel Code
Quality projection lifecycle is defined here.

Projection repair cannot change CQ semantic authority, and semantic
`REVALIDATE` is not projection regeneration. `working/INDEX.md` remains
coordinator workflow authority only.

## Handoff boundary

Use the referenced semantic contracts for finding identity, taxonomy, evidence,
applicability, disposition, lifecycle, freshness, severity, coverage,
remediation, and cross-capability relationships. Handoffs to Architecture,
Test Engineering, or existing Architecture/security semantics preserve the
other capability’s ownership and adjudication.
