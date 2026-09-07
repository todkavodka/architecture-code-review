# PS-139 — True Product Architecture finding

## Input state

Accepted cross-project evidence and STM relations show a consequence spanning
Projects A and B at one accepted Product revision and exact baseline.

## Expected semantic behavior

Architecture Review independently adjudicates a Product-scoped `RF-*` with
Product revision/baseline, affected Projects, contributing WS/EV and STM
references, consequence, severity, lifecycle, and dependencies. The finding
remains Architecture-owned.

## Forbidden behavior

- promoting a Project-local RF merely because it is visible in Product scope;
- treating a Product report or projection as the finding authority;
- moving CQ or Test Engineering ownership into Architecture Review;
- omitting qualified provenance.

## Affected authority

Architecture Review owns the Product RF. STM and Shared Evidence remain factual
upstream authorities; Code Quality and Test Engineering retain their own
cross-project semantic ownership.

## Expected impact scope

Only the affected Product interpretation and its direct downstream dependencies
are in scope; local RFs without Product consequence remain unchanged.

## Package/projection outcome

Product Architecture outputs may project the accepted RF and become stale when
its evidence or STM inputs change; projection content cannot revise the RF.

## Verdict

`PS139_PASS_TRUE_PRODUCT_RF`
