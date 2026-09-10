# API Operation Completeness Validation

## PRE-CHANGE — immutable fail-first evidence

Evidence base: `d68b9650a29820d8f9a563a81f5d90fb8f11d5e5`.

Inspected path: `references/shared-technical-model.md`, section 10.1, `IF-*`
interface and contract shape (including the existing role/view matrix and
protocol-property table).

| Check | Concrete contract observation at the evidence base | Expected result |
|---|---|---|
| FF01 — coarse one-IF/ten-operation CURRENT projection | The `IF-*` shape has one optional `operation_identity` field and no `operation_children` collection, so a CURRENT projection of ten operations requires coarse interface-level representation rather than ten independently identified children. | GAP PRESENT |
| FF02 — missing inventory accounting | The IF contract has no parent-qualified operation identifier, no child inventory, and no allocation rule from which a complete operation inventory can be accounted. | GAP PRESENT |
| FF03 — missing composed route requirement | The HTTP_REST controlled properties name method and path/template, but the IF contract has no requirement to persist a protocol-specific normalized operation identity composed from the route and operation semantics. | GAP PRESENT |
| FF04 — coarse EXTEND reuse | Reuse is defined only for accepted facts at the coarse STM-fact level; there is no parent-qualified child identity or `supersedes` rule for extending one operation while preserving the remaining IF contract. | GAP PRESENT |
| FF05 — material-only consumed grouping | `IF-*` identifies one material interaction surface and has a single `observed_view`; the `CONSUMED` view cannot group independently evidenced consumed operations without collapsing them into that material IF record. | GAP PRESENT |
| FF06 — complete-claim absence | The IF contract has no operation inventory or child lifecycle/accounting rule that could support a complete-operation claim for an interface. | GAP PRESENT |

This PRE-CHANGE evidence was recorded before the normative IF contract edit and
must not be reconstructed from the edited contract.
