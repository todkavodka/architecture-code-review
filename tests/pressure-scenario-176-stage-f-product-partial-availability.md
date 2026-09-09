# PS-176 — Stage F Product partial availability

## Design mapping

`PS-F23`: an unavailable Project yields partial Product availability, not a
universal failure or clean state.

## Setup / evidence shape

Product P has an exact baseline vector naming Projects A and B. Project A has
accepted/fresh inputs; Project B is unavailable or only partially covered for
the selected Product view.

## Expected accepted semantic records

Product resolution preserves A’s qualified accepted inputs and records B’s
source availability, review coverage, semantic availability, projection
freshness, and package gate result independently. No facts are accepted for B
without its authority/evidence.

## Prohibited inference / authority result

- unavailable B does not mean no interfaces, no access, clean, compatible, or
  not applicable;
- one available Project cannot stand in for the baseline vector;
- Product projection cannot create missing B facts or a global failure;
- the five availability dimensions must not be flattened.

## Expected projection behavior

Product views render available A content and an explicit partial/unavailable B
limitation. Affected projections or package gates may be stale/blocked under
existing policy; no automatic full Product reread or regeneration occurs.

## Backward-compatibility constraint

Prior Product snapshots retain their exact baseline and historical availability
state. Revalidation is bounded to affected dependencies.

## GREEN criteria

GREEN iff B remains explicitly unavailable/partial, A’s valid content is not
discarded, availability dimensions stay distinct, and no clean/global result is
manufactured.

## Verdict

`PS176_PASS_PRODUCT_PARTIAL_AVAILABILITY`
