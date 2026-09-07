# PS-150 — Product Architecture finding boundary

## Input state

Accepted cross-project WS/EV evidence and qualified STM relations show a
material architectural consequence spanning Projects A and B at one Product
revision and baseline.

## Expected semantic behavior

Architecture Review independently adjudicates an existing `RF-*` with Product
revision/baseline, affected Projects, qualified evidence/STM references,
consequence, severity, lifecycle, dependencies, and provenance.

## Forbidden behavior

- creating a Product-specific RF family;
- promoting a local RF by aggregation;
- treating a report, projection, or index as RF authority;
- allowing Architecture Review to write STM, CQ, or TE semantics.

## Affected authority

Architecture Review owns the Product RF interpretation. Shared Evidence and
STM remain factual authorities; other capabilities retain their ownership.

## Expected impact scope

The cross-project Product consequence and directly dependent Product records;
unrelated local RFs remain unchanged.

## Package/projection outcome

Product Architecture projections may render the accepted RF and become stale
when its qualified inputs change, but cannot revise the RF.

## Verdict

`PS150_PASS_PRODUCT_RF_BOUNDARY`
