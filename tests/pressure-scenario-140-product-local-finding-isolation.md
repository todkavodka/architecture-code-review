# PS-140 — Product-local finding isolation

## Input state

Project A has an accepted local RF or capability finding. Project B is a
member of the same Product but contributes no evidence of a Product-spanning
consequence for that finding.

## Expected semantic behavior

The local finding remains scoped to Project A and its own provenance. Product
views may aggregate or navigate to it as a projection, but no Product-scoped
semantic finding is created without independent cross-project evidence and
adjudication.

## Forbidden behavior

- auto-promoting local RF/STM/CQ/TE records to Product scope;
- treating Product membership as evidence or dependency;
- using an aggregate report as a new authority;
- mutating another Product's interpretation of Project A.

## Affected authority

The original capability owner retains the local finding. Product composition
owns only routing and projection selection; Architecture Review may write a
Product RF only after independent Product adjudication.

## Expected impact scope

Impact remains Project-local unless a qualified Product relation and sufficient
evidence establish a boundary crossing.

## Package/projection outcome

The local Project package/output may remain current. A Product summary may
include a navigational reference without requiring unrelated Product members.

## Verdict

`PS140_PASS_LOCAL_FINDING_ISOLATION`
