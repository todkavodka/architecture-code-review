# PS-149 — Single-member Product transition

## Input state

A Product initially has one Project member and later adds a second Project,
while a separate single-project review continues without Product mode.

## Expected semantic behavior

The Product remains an explicit composition with its own revision, baseline,
selector snapshot, and package scope. The local review remains Product-free;
the Product transition does not rewrite or require Product qualification for
existing local identities.

## Forbidden behavior

- equating one Product member with the Project or repository;
- forcing the local review into Product mode;
- rewriting existing `PRJ-*` or package identities;
- using the Product package as a replacement for Project authority.

## Affected authority

Product routing owns membership/revision composition. Existing Project and
single-project capability/package contracts remain authoritative for the local
review.

## Expected impact scope

Only the Product membership revision and dependent Product outputs are
affected; the independent local review remains unchanged.

## Package/projection outcome

Product package resolution uses its finite selected scope, while the local
Project package follows existing Stage B policy independently.

## Verdict

`PS149_PASS_SINGLE_MEMBER_BOUNDARY`
