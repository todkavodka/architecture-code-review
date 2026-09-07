# PS-137 — Product API compatibility across Projects

## Input state

Project A exposes `IF-001` at a selected baseline and Project B consumes a
same-named local `IF-001` at another baseline. Evidence includes declared,
implemented, consumed, and tested observations with a possible version conflict.

## Expected semantic behavior

WS/EV observations retain each qualified Project, exact Product baseline, and
observed view. STM accepts a cross-project relation only through the Technical
Model Gate; Test Engineering adjudicates contract consistency and Architecture
Review evaluates architectural consequence when required.

## Forbidden behavior

- colliding A::IF-001 and B::IF-001;
- resolving conflicting observations by implicit precedence;
- treating a report or compatibility matrix as authority;
- promoting a relation to a dependency automatically.

## Affected authority

Shared Evidence owns observations; STM owns accepted factual relations; Test
Engineering owns contract consistency; Architecture Review owns architectural
consequence.

## Expected impact scope

Only the qualified interface/consumer relation and dependent semantic slices
are candidates for impact; unrelated local facts remain preserved.

## Package/projection outcome

Dependent Product projections or packages may become stale or limited after
impact accounting; no projection is regenerated automatically.

## Verdict

`PS137_PASS_QUALIFIED_API_RELATION`
