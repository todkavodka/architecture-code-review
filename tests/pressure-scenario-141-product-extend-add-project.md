# PS-141 — Product `EXTEND` adds a Project

## Input state

Product P has accepted Projects A–C. A user explicitly requests `EXTEND` to
add Project D and its declared source binding.

## Expected semantic behavior

The coordinator creates a new Product revision for the membership change,
keeps prior revisions/baselines immutable, and resolves only D's minimum
required evidence, semantic slice, and qualified dependencies. Accepted A–C
state is preserved unless a recorded dependency crosses into it.

## Forbidden behavior

- silently mutating the prior Product revision;
- reopening unrelated A–C authority;
- treating membership as repository-read or write authorization;
- running a full Product audit by default.

## Affected authority

Product Context Workflow owns revision/membership routing. Existing Evidence,
STM, capability, revalidation, projection, and package contracts own their
semantic decisions.

## Expected impact scope

The new member and any explicitly discovered dependent cross-project slice;
unaffected accepted A–C domains remain preserved.

## Package/projection outcome

Only selected Product outputs whose resolved dependency closure includes D
need impact/freshness evaluation; no automatic regeneration occurs.

## Verdict

`PS141_PASS_ADDITIVE_PRODUCT_EXTEND`
