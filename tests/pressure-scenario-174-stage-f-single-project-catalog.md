# PS-174 — Stage F single-project catalog

## Design mapping

`PS-F21`: one Project produces a complete Service catalog without Product.

## Setup / evidence shape

A single Project has accepted, fresh STM/evidence slices for its provided and
consumed interfaces, integrations/events, data stores/access, and applicable
CC inputs. No Product context or membership is selected.

## Expected accepted semantic records

The normal single-project route accepts the supported STM facts through the
Technical Model Gate, invokes Contract Verification when applicable, and
resolves the existing Service Technical Documentation projections and package
scope from Project-qualified inputs.

## Prohibited inference / authority result

- Product context must not be mandatory for Stage F;
- a Service projection cannot become STM authority;
- package membership cannot be inferred from file presence;
- no Product facts or Product permissions are created.

## Expected projection behavior

The Service catalog renders the accepted Project facts, evidence/provenance,
redaction, limitations, and existing PRJ lifecycle state. Product views are
not required and are not implicitly generated.

## Backward-compatibility constraint

Existing Product-free single-project reviews remain first-class. Historical
single-project facts do not need retroactive Product qualification.

## GREEN criteria

GREEN iff the complete supported Service catalog is reachable with no Product
state, all authority gates remain in place, and no Product-specific lifecycle
or factual family is introduced.

## Verdict

`PS174_PASS_SINGLE_PROJECT_CATALOG`
