# Artifact Layout and Package Completeness Hardening Design

## Goal

Prevent agents from inventing review directories, renumbering canonical deliverables, collapsing capability-owned outputs into arbitrary aggregate files, or declaring `REVIEW_COMPLETE` when the actual artifact tree does not match the selected workflow and package contract.

## Observed regression

A real `FORENSIC + REVIEW_PLUS_TARGET_AND_ROADMAP` run declared `REVIEW_COMPLETE` with this final package:

```text
docs/reviews/
├── 01-architecture-review.md
├── 02-target-architecture.md
├── 03-remediation-roadmap.md
├── 04-technical-documentation.md
├── 05-test-engineering.md
└── 06-code-quality.md
```

and ad-hoc working directories such as:

```text
working/technical-model/components/
working/technical-model/interfaces/
working/technical-model/auth/
working/technical-model/flows/
working/technical-model/errors/
working/technical-model/config/
working/technical-model/data-stores/
```

The agent later admitted that these paths were invented rather than resolved from the skill contracts. It also incorrectly claimed that `working/evidence/` was invented even though the FORENSIC package contract already declares that directory.

This exposed two gaps:

1. existing layout prose was treated as advisory rather than as an execution contract;
2. closeout verified semantic/workflow state but did not mechanically reconcile the expected artifact manifest with the actual filesystem tree.

## Design

### 1. Freeze an artifact layout manifest before substantive writes

After Session Intent, mode, endpoint, capability/output configuration, and any established repository-local review convention are resolved, the coordinator must persist one `ARTIFACT_LAYOUT_MANIFEST`.

The manifest records:

```text
package_root
layout_source
selected_mode
selected_endpoint
semantic_authority_paths
requested_projection_paths
capability_owned_paths
required_working_paths
conditional_paths
allowed_generated_operational_paths
forbidden_or_unresolved_paths
```

The manifest is coordinator routing metadata, not semantic authority and not projection authority.

### 2. Canonical root is deterministic

If the repository already has a valid established review-package convention compatible with the selected workflow, use it and record the evidence. Otherwise the canonical root is:

```text
docs/reviews/architecture-review/
```

The agent must not shorten this to `docs/reviews/`, invent a sibling root, or move authority/projection files for aesthetic reasons.

### 3. Existing filename roles are binding

For Architecture Review package roles:

```text
01-architecture-review.md
02-authoritative-findings-ledger.md
03-target-architecture.md          # selected endpoint only
04-remediation-roadmap.md          # selected endpoint only
working/README.md
working/INDEX.md
```

These filenames and role assignments are contract-owned. The executing agent cannot renumber Target Architecture/Roadmap, omit the findings ledger, or replace the ledger with a working copy.

### 4. Capability outputs remain capability-owned

Test Engineering and Code Quality outputs use their declared capability projection contracts and paths. The umbrella coordinator may link or summarize them but must not invent aggregate files such as:

```text
05-test-engineering.md
06-code-quality.md
```

unless those exact paths are explicitly registered by an approved projection contract.

### 5. No invented directories

Directories are created lazily only when a manifest-declared artifact or owning contract requires them.

The agent must not create speculative directories "for later" or infer taxonomy from semantic families. In particular, a structured STM semantic model does not authorize filesystem subdirectories such as `components/`, `interfaces/`, or `auth/` unless the Shared Technical Model persistence contract or frozen manifest explicitly declares those paths.

Unknown requested path → `ARTIFACT_PATH_NOT_DECLARED`.

### 6. Mode-specific working artifact completeness is required

The mode-specific working-artifact set in `review-modes-and-orchestration.md` becomes an executable manifest input.

For `FORENSIC`, every unconditional artifact declared by that mode must be represented in the manifest and exist before closeout. Conditional correction/re-review artifacts are included only when their trigger occurred.

Missing required file → `REQUIRED_ARTIFACT_MISSING`.

### 7. Closeout compares expected and actual trees

Before final editorial acceptance or `REVIEW_COMPLETE`, run `ARTIFACT_PACKAGE_RECONCILIATION`:

```text
frozen ARTIFACT_LAYOUT_MANIFEST
        vs
actual package tree
        vs
artifact registry
        vs
semantic/projection ownership
```

The result is:

```text
ARTIFACT_PACKAGE_RECONCILED
ARTIFACT_PACKAGE_RECONCILIATION_REQUIRED
```

Acceptance requires:

- every unconditional required path exists;
- every triggered conditional path exists;
- every actual generated review path is declared or explicitly classified as allowed operational history;
- semantic authorities are at their declared paths;
- projection paths match registered projection contracts;
- capability outputs stay capability-owned;
- no path-role collision exists;
- no undeclared empty/speculative directories remain inside the review package;
- package root matches the frozen root;
- artifact registry and actual tree agree.

### 8. Completion gate

`REVIEW_COMPLETE` requires both:

```text
FINAL_WORKFLOW_AUTHORITY_RECONCILED
ARTIFACT_PACKAGE_RECONCILED
```

A semantically valid review with an incomplete or drifted package tree is `REVIEW_PARTIALLY_COMPLETE`, not complete.

## Regression expectations

The following must fail:

```text
FORENSIC selected
→ agent writes docs/reviews/ instead of docs/reviews/architecture-review/
→ omits 02-authoritative-findings-ledger.md
→ renumbers target/roadmap
→ invents 05-test-engineering.md / 06-code-quality.md
→ creates undeclared working/technical-model/* taxonomy
→ declares REVIEW_COMPLETE
```

The valid route is:

```text
resolve/freeze ARTIFACT_LAYOUT_MANIFEST
→ create only declared paths lazily
→ write owner/capability artifacts at declared locations
→ complete semantic and projection gates
→ compare expected manifest vs actual tree
→ ARTIFACT_PACKAGE_RECONCILED
→ final editorial acceptance
→ REVIEW_COMPLETE
```

## Non-goals

- Do not redesign semantic authority.
- Do not force all repositories to use the canonical root when a valid established local convention already exists.
- Do not prescribe a new internal STM taxonomy.
- Do not merge capability-owned outputs into umbrella files.
- Do not create directories solely to make the tree look uniform.
