# PS-138 — Product shared component

## Input state

Projects A and B use a shared broker, database, SDK, or auth service. The
resource is external or has an explicitly named technical owner, and both
Projects record local facts about their use.

## Expected semantic behavior

Each Project-local fact remains in STM under its own qualified identity.
Product-scoped evidence and STM relations record usage, provider/consumer, or
shared-state participation with exact baseline provenance. Technical ownership
or external status remains explicit.

## Forbidden behavior

- making Product the generic technical owner;
- confusing membership or usage with ownership;
- creating a second Product fact authority;
- inferring a dependency without dependent-owned `DEPENDS_ON` metadata.

## Affected authority

The named technical owner or external source owns resource facts. Shared
Evidence owns observations, and the Technical Model Gate owns accepted
cross-project factual relations.

## Expected impact scope

Resource changes traverse only qualified direct dependencies and factual
relations that actually reference the resource; unrelated Project state is
preserved.

## Package/projection outcome

Outputs depending on the shared resource may be limited or stale under their
own package/freshness policy; resource cataloguing alone creates no output.

## Verdict

`PS138_PASS_EXPLICIT_SHARED_OWNERSHIP`
