# PS-177 — Stage F bounded provider impact

## Design mapping

`PS-F24`: a provider change impacts only dependent consumers and projections.

## Setup / evidence shape

A provider IF operation changes from one accepted exact revision to another.
Only some consumer IF/INT records and Product-qualified views reference the old
provider revision; unrelated Project facts and Product members do not.

## Expected accepted semantic records

The new provider revision is a new accepted IF revision when supported. Impact
analysis identifies the exact dependent consumer/CC inputs and Product views.
Unlinked facts remain unchanged; old CC results remain bound to the old exact
pair.

## Prohibited inference / authority result

- provider revision change does not invalidate every Project or Product fact;
- an old CC result does not prove current compatibility;
- reverse indexes do not become dependency authority;
- impact does not trigger a full Product reread or automatic regeneration.

## Expected projection behavior

Only affected Service/Product projections become `STALE` or `BLOCKED` as
appropriate after impact accounting. Regeneration is an explicit `RG-*` action
and does not mutate STM or old snapshots.

## Backward-compatibility constraint

Historical provider revisions, consumer records, CC records, and Product
baselines retain their original meaning. New verification/revalidation is
bounded to the changed dependency slice.

## GREEN criteria

GREEN iff impact follows consumer-to-prerequisite dependencies, only affected
outputs are marked, old exact results remain historical, and no automatic
regeneration or broad revalidation occurs.

## Verdict

`PS177_PASS_BOUNDED_PROVIDER_IMPACT`
