# PS-133 — Product with three clean Projects

## Input state

An accepted Product revision contains three Projects with exact clean
committed repository/scope bindings and a selected Product baseline.

## Expected semantic behavior

Product mode pins the accepted Product revision, immutable membership snapshot,
and exact per-Project baseline vector. The vector records each repository,
scope, and commit; it may carry `COHERENT` only when coordination evidence
supports that classification and never collapses to one Git SHA.

## Forbidden behavior

- treating Product as a repository or Project;
- inferring membership from paths;
- representing the multi-repository baseline with one SHA;
- retargeting the session when Product `current_revision` advances.

## Affected authority

The Product Context Workflow owns selection and pinning. Existing Project-local
evidence, STM, capability, projection, and package authorities consume the
qualified baseline references.

## Expected impact scope

Product scope is bounded to the selected membership snapshot and its exact
source vector; unrelated Products remain isolated.

## Package/projection outcome

Later Product outputs may resolve only the selected members and dependency
closure; no output is generated merely by selecting Product mode.

## Verdict

`PS133_PASS_EXACT_PRODUCT_VECTOR`
