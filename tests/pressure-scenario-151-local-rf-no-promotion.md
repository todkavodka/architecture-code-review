# PS-151 — Local RF is not Product RF

## Input state

Project A has an accepted local `RF-*`; Project B is a Product member but no
qualified evidence establishes a Product-spanning consequence.

## Expected semantic behavior

The local RF remains Project-scoped with its original identity, root boundary,
severity, lifecycle, and provenance. A Product report may navigate to it, but
no Product RF is created without independent Product adjudication.

## Forbidden behavior

- auto-promoting the local RF because of membership;
- copying report text into Product authority;
- changing the local RF baseline or lifecycle;
- treating absence of Product evidence as a negative finding.

## Affected authority

Architecture Review owns the local RF. Product composition and report
projections remain non-authoritative for finding semantics.

## Expected impact scope

Project A local scope only; Product scope expands only after evidence-backed
boundary crossing.

## Package/projection outcome

The local package/output may remain current. Product summaries may include a
navigational reference without requiring unrelated member projections.

## Verdict

`PS151_PASS_LOCAL_RF_ISOLATION`
