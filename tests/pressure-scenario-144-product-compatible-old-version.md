# PS-144 — Older but compatible Project version

## Input state

Project B consumes an older provider version than Project A currently offers.
STM contains declared, implemented, consumed, and tested views; Test
Engineering has evidence for the supported range.

## Expected semantic behavior

The version facts and qualified observations remain independently bound to the
Product baseline. Test Engineering adjudicates compatibility through its
existing contract semantics; Architecture Review evaluates a consequence only
if evidence shows one. Compatibility is not inferred solely from version
ordering.

## Forbidden behavior

- creating an automatic compatibility engine or resolver;
- treating a matrix/report as authority;
- declaring incompatibility solely because versions differ;
- rewriting Project-local identities or facts.

## Affected authority

STM owns factual version/interface views, Test Engineering owns compatibility
contract adjudication, and Architecture Review owns any architectural
consequence.

## Expected impact scope

Only the qualified provider/consumer contract and dependent Product slices are
evaluated; unrelated Project-local facts remain preserved.

## Package/projection outcome

Selected Product assurance or architecture outputs may remain current when
compatibility evidence is accepted; affected outputs become stale only through
normal impact accounting.

## Verdict

`PS144_PASS_EXPLICIT_COMPATIBILITY_ADJUDICATION`
