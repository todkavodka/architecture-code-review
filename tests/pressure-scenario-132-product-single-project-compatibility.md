# PS-132 — Product-free single-project compatibility

## Input state

An existing local review session selects no Product and has only its current
repository identity, local baseline, Session Intent, and Project-local
artifacts.

## Expected semantic behavior

The coordinator preserves the existing session shape and local artifact
references. Product fields are absent or `NONE`; no Product revision,
membership, baseline, package, or cross-project state is required.

## Forbidden behavior

- synthesizing a one-member Product;
- requiring Product identity or Product baseline for local review;
- rewriting existing WS-*/EV-*/STM/RF/CQ/TE/PRJ identities.

## Affected authority

Session Orchestration owns local routing. Existing evidence, STM, capability,
projection, and package contracts retain authority without Product context.

## Expected impact scope

Local Project/session scope only; no Product-context escalation occurs.

## Package/projection outcome

Existing single-project projection and package behavior remains available under
the existing policies, with no synthetic Product package.

## Verdict

`PS132_PASS_PRODUCT_FREE_ROUTE`
