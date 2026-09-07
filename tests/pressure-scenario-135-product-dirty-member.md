# PS-135 — Product with a dirty member

## Input state

Product A includes a member with a committed base plus tracked changes and
selected untracked content; the source may also be detached, local-only,
missing its remote, or diverged.

## Expected semantic behavior

The baseline binds the exact base commit, changed paths and raw-content
fingerprints, selected untracked paths and fingerprints, and each applicable
noncanonical state. Explicit baseline acceptance records limitations. Dirty
content is neither automatically invalid nor automatically accepted.

## Forbidden behavior

- calling dirty content a clean remote-canonical baseline;
- including untracked content without explicit selection and fingerprints;
- silently accepting dirty or noncanonical content;
- replacing the Product vector with a single commit SHA.

## Affected authority

The Product Baseline Acceptance Gate owns admission of the exact binding;
source-read and dirty-admission authorization remain separate from Product
membership.

## Expected impact scope

Claims depending on the dirty member carry the recorded limitation and may
require bounded evidence expansion; unaffected member state is preserved.

## Package/projection outcome

A selected package requiring the dirty member may be limited or blocked by its
own policy; dirty state alone does not invalidate semantic authority globally.

## Verdict

`PS135_PASS_EXPLICIT_DIRTY_BINDING`
