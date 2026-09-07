# PS-147 — One Project in two Products

## Input state

Project B belongs to Product X and Product Y with different accepted Product
revisions, baselines, memberships, and selected output packages.

## Expected semantic behavior

Each Product stores an isolated resolved membership and selector snapshot.
Project-local authority may be reused only when its exact provenance and
freshness satisfy the consuming Product; Product interpretations and package
state remain separate.

## Forbidden behavior

- mutating Product Y when Product X changes membership or baseline;
- using Product X's selector snapshot for Product Y;
- making Product own Project B's technical facts;
- requiring a shared Product parent.

## Affected authority

Each Product Context Workflow owns its own Product revision/baseline/package
routing; Project-local owners retain their authority independently.

## Expected impact scope

Impact is isolated to the changed Product and its qualified dependent slice;
shared Project-local artifacts are reused only by exact binding, never by
cross-Product mutation.

## Package/projection outcome

Each Product package evaluates its own resolved members and freshness. A gate
in Product X cannot block unrelated Product Y output without dependency.

## Verdict

`PS147_PASS_MULTI_PRODUCT_ISOLATION`
