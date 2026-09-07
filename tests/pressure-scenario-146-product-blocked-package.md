# PS-146 — Product package with a blocked member

## Input state

A Product package selects Findings and Summary as required outputs. A required
Project subpackage is blocked while an unrelated optional projection is stale.

## Expected semantic behavior

The package resolves explicit required, optional, and conditional members plus
dependency closure. The applicable gate blocks only when the blocked member is
within the resolved required scope; semantic authority remains independent.

## Forbidden behavior

- requiring every projection in every member Project;
- treating package blocking as a failed semantic finding;
- replacing Project subpackages with embedded Product copies;
- redefining `ALL_SCOPED_CURRENT` globally.

## Affected authority

The shared package contract owns gate evaluation. Project capabilities and
projections retain their semantic and lifecycle authority.

## Expected impact scope

The selected Product package and its dependency closure; unrelated packages or
outputs do not become blocked without dependency.

## Package/projection outcome

`PERMISSIVE`, `REQUIRED_SCOPE_CURRENT`, and `ALL_SCOPED_CURRENT` evaluate only
the resolved Product scope and preserve unrelated stale members visibly.

## Verdict

`PS146_PASS_SCOPED_PACKAGE_GATE`
