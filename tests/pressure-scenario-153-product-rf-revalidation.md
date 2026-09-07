# PS-153 — Product RF targeted revalidation

## Input state

A qualified STM relation supporting a Product RF changes for Project B while
the Product retains unrelated accepted Projects and findings.

## Expected semantic behavior

Product `REVALIDATE` follows the changed binding and direct dependency slice,
then Architecture Review re-adjudicates only the affected Product consequence.
The RF remains bound to its exact Product revision/baseline history and
unaffected findings are preserved.

## Forbidden behavior

- rereading or reopening every Product finding by default;
- treating impact traversal as RF adjudication;
- automatically executing a full Product audit;
- regenerating the report as part of semantic revalidation.

## Affected authority

Revalidation owns impact routing; STM owns changed factual relations;
Architecture Review owns the affected RF interpretation.

## Expected impact scope

Project B's qualified relation and directly dependent Product RF slice only;
unknown linkage requests bounded context expansion.

## Package/projection outcome

Dependent Product Architecture projections may become stale after impact
accounting; unrelated projections and packages remain independently gated.

## Verdict

`PS153_PASS_PRODUCT_RF_TARGETED_REVALIDATION`
