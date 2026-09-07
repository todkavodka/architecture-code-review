# PS-136 — Product baseline advancement after acceptance

## Input state

Product P has an accepted revision and immutable baseline B1. One member
source advances to a new exact revision after a session has pinned B1.

## Expected semantic behavior

B1 and the historical session remain addressable and unchanged. A later
session may select a new Product baseline candidate and use the owning
revalidation rules to determine bounded impact; Product `current_revision`
does not retarget the earlier session.

## Forbidden behavior

- rewriting B1;
- silently changing the pinned session's source binding;
- treating every advancement as an automatic full Product audit;
- regenerating projections without impact analysis and explicit request.

## Affected authority

Product revision/baseline routing preserves history; revalidation and
projection contracts own later impact/freshness decisions.

## Expected impact scope

Only records depending on the advanced binding are candidates for Product
revalidation; unaffected accepted state remains preserved.

## Package/projection outcome

Affected Product packages/projections may become non-current after impact
accounting; unrelated resolved package members are not blocked automatically.

## Verdict

`PS136_PASS_HISTORICAL_BASELINE_PINNING`
