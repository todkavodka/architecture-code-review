# PS-156 — Stage F consumer/provider mismatch

## Design mapping

`PS-F03`: different consumer/provider paths coexist without aliasing; only a
resolved material mismatch produces `INCOMPATIBLE`.

## Setup / evidence shape

Provider and consumer IFs have separate exact Project/revision bindings. Their
paths or operation contracts differ materially. A candidate match may exist,
but the comparison is either unresolved, non-final, non-applicable, or backed
by a resolved accepted `CC-*` adjudication.

## Expected accepted semantic records

STM retains both IF identities. When applicable, Contract Verification compares
the exact qualified pair. Stage F displays `INCOMPATIBLE` only for a resolved,
valid `CC-*` adjudication accepting the material mismatch; otherwise it
displays `INDETERMINATE` for missing/unresolved/non-final required state, or no
compatibility result when there is no valid comparison pair.

## Prohibited inference / authority result

- similar names, paths, methods, or Product membership do not alias IFs;
- `MATCH_CANDIDATE` is not `COMPATIBLE`;
- missing data is not `INCOMPATIBLE` or `NOT_COMPARABLE`;
- Technical Documentation and Product projections do not adjudicate.

CC-* remains Test Engineering compatibility authority.

## Expected projection behavior

Interface projections preserve provider/consumer identities and candidate or
unresolved state. A compatibility label appears only with the exact accepted
CC reference and qualified revisions; stale or non-final CC state remains
`INDETERMINATE`.

## Backward-compatibility constraint

Historical CC records retain their identity, revision, status, and meaning. A
new provider revision does not inherit compatibility from an old revision.

## GREEN criteria

GREEN iff IF identities remain distinct, the result is derived only from exact
qualified CC authority, every unresolved/non-applicable branch is explicit, and
no path/name similarity produces compatibility.

## Verdict

`PS156_PASS_CC_BOUNDARY`
