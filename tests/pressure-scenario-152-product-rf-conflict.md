# PS-152 — Product RF conflicting inputs

## Input state

Two Projects provide conflicting qualified STM/evidence views for a shared API
boundary, and a Product RF candidate depends on that boundary.

## Expected semantic behavior

The conflict remains explicit and bound to the Product baseline. The Technical
Model Gate or evidence owner adjudicates factual conflict first; Architecture
Review may keep the RF unresolved/limited until sufficient factual authority
exists, then independently adjudicates architectural consequence.

## Forbidden behavior

- resolving the conflict by report order or projection freshness;
- accepting a Product RF without qualified factual provenance;
- allowing Product context to overwrite Project-local facts;
- treating a reverse index as conflict authority.

## Affected authority

Shared Evidence and STM own factual conflict handling; Architecture Review owns
only the Product architectural interpretation.

## Expected impact scope

The conflicting Product boundary and dependent RF candidate; unrelated accepted
facts and findings remain preserved.

## Package/projection outcome

Affected Product Architecture output may be limited or blocked by its owning
authority gate; unrelated package members remain independent.

## Verdict

`PS152_PASS_PRODUCT_RF_CONFLICT_HANDLING`
