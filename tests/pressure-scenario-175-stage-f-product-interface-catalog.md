# PS-175 — Stage F Product Interface Catalog

## Design mapping

`PS-F22`: Product aggregates exact Project revisions into the Product Interface
Catalog without collapsing local identities.

## Setup / evidence shape

Product P has an exact immutable baseline vector for Projects A and B. Each
Project contributes accepted provided/consumed IF facts at exact local
revisions; both Projects may use the same local semantic ID text.

## Expected accepted semantic records

Project-local STM remains authoritative. Product resolution records Product
identity/revision/baseline, Project/source revisions, local IF IDs/revisions,
selector identity/definition revision, evidence, and availability. Equal local
IDs remain distinct qualified records.

## Prohibited inference / authority result

- Product aggregation does not create Product IF facts or a new PRJ family;
- same local ID, path, provider, or Product membership does not alias records;
- Product baseline does not replace Project/IF revisions;
- candidate provider matching is not compatibility.

## Expected projection behavior

The existing Service IF projections are reused as qualified Product views with
explicit snapshots and lifecycle state. Provider/consumer roles, observed
views, provenance, precision, and unresolved matches remain visible.

## Backward-compatibility constraint

Historical Project IF identities and snapshots remain unchanged. A new Product
baseline creates a new qualified resolution rather than rewriting prior output.

## GREEN criteria

GREEN iff every rendered IF retains Product baseline plus Project/source and
local revision qualification, existing PRJ/selector lifecycle is reused, and
no Product factual authority or identity alias is created.

## Verdict

`PS175_PASS_PRODUCT_IF_QUALIFICATION`
