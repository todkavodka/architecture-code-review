# PS-148 — Product `EXTEND` output requiredness

## Input state

An accepted Product package selects one new Product output during `EXTEND`;
existing outputs and their accepted Project subpackages are unchanged.

## Expected semantic behavior

The extension records a finite Product membership/dependency snapshot and
classifies the new output as required, optional, or conditional under the
existing package policy. Unaffected accepted output state is preserved.

## Forbidden behavior

- making every existing Product or Project projection required;
- reopening unrelated semantic findings;
- using package membership as semantic authority;
- regenerating all projections automatically.

## Affected authority

The owning capability declares output dependencies; the shared package
contract resolves requiredness and freshness; Product routing records context.

## Expected impact scope

The added output and its dependency closure only, with bounded impact to
dependent Product projections or packages.

## Package/projection outcome

The resolved package gate covers the newly selected output and prerequisites;
unselected outputs remain outside `ALL_SCOPED_CURRENT`.

## Verdict

`PS148_PASS_ADDITIVE_OUTPUT_REQUIREDNESS`
