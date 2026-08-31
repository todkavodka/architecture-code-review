# Architecture Code Review — Discovery Coverage Assurance Design

Date: 2026-08-31
Status: DESIGN_REVIEW_REQUIRED
Target repository: `todkavodka/architecture-code-review`
Target baseline: `main@fd7466a33362d04d964cb847d33c5a1e022ba48b`
Design branch: `design/discovery-coverage-assurance-v0.3`

## 1. Problem

The current Skill is evidence-first after a candidate exists: discovery creates `CAND-*`, then independent verification, root-boundary adjudication, severity adjudication, and the authoritative ledger strengthen, correct, or reject that candidate.

The missing guarantee is earlier: the workflow does not prove that all material mechanism classes were actually investigated before discovery is declared complete.

A field audit exposed this gap. A reachable authenticated SQL injection caused by direct request input interpolated into `WhereRaw(...)` was missed even though the same large controller file was inspected for unrelated findings. No systematic interpreter/raw-construction inventory existed, so no candidate was created. Downstream gates had nothing to verify.

A dedicated baseline pressure test against the current production Skill returned:

`PS45_RED_DISCOVERY_COVERAGE_GAP_CONFIRMED`

The failure boundary was thematic discovery, not independent verification, severity, root adjudication, or final editorial review.

## 2. Core objective

Introduce an explicit **Discovery Coverage Assurance** layer so audit completeness is demonstrated by mechanism coverage rather than inferred from finding count.

Core invariant:

> The number and severity of discovered findings are not evidence of audit completeness. Completeness is demonstrated by mechanism coverage, evidence trails, and an independent coverage challenge.

The design must preserve precision. It must make whole-class omissions less likely without turning the Skill into a vulnerability checklist or promoting suspicious API names into findings.

## 3. Revised review flow

```text
Baseline
→ As-Built Architecture
→ Independent As-Built Review
→ Thematic Discovery
→ Discovery Coverage Matrix closeout
→ Independent Coverage Review
→ targeted coverage correction/re-review, if needed
→ COVERAGE_ACCEPTED
→ Independent Candidate Verification
→ Root-Boundary Adjudication
→ Severity Adjudication
→ Authoritative Findings Ledger
→ Target Architecture, if requested
→ Roadmap, if requested
→ Final Package
→ Final Editorial Review
```

Candidate verification may start only when:

```text
DISCOVERY_COMPLETE
AND
COVERAGE_ACCEPTED
```

## 4. Discovery Coverage Matrix

### 4.1 Purpose

The matrix proves that relevant mechanism classes were actually considered with evidence. It is not a vulnerability quota and does not require findings.

### 4.2 Row schema

Each row contains at least:

```text
domain
applicability
coverage_status
evidence_refs
inventory_summary
candidate_ids
positive_controls
open_questions
limitations
```

### 4.3 Applicability

```text
YES
NO
CONDITIONAL
```

### 4.4 Coverage status

```text
PENDING
IN_PROGRESS
COVERED
PARTIALLY_COVERED
BLOCKED
NOT_APPLICABLE
```

Hard rules:

```text
PARTIALLY_COVERED != COMPLETE
BLOCKED != COMPLETE
```

`NOT_APPLICABLE` requires an evidence-based reason.

### 4.5 Valid coverage evidence

Coverage evidence can include:

- inspected paths and call chains;
- targeted inventory/search results bound to the baseline;
- representative semantic traces of high-risk sites;
- positive controls and considered-but-not-promoted conclusions;
- evidence-based proof that a mechanism class is absent.

Generic claims such as `security reviewed`, `controllers reviewed`, or `grep completed` are insufficient by themselves.

Search is an inventory mechanism, not semantic proof. `COVERED` requires enough interpretation to distinguish safe, unsafe, ambiguous, and non-applicable cases.

## 5. Canonical coverage domains

```text
ARCH-01 Architecture / responsibility
ARCH-02 Ownership / isolation / concurrency
ARCH-03 Lifecycle / cleanup / recovery
ARCH-04 Boundary contracts / IPC / API / process

SEC-01 Authentication / authorization / identity / scope
SEC-02 Interpreter / dynamic construction
SEC-03 Resource addressing / filesystem / paths
SEC-04 Outbound network target control
SEC-05 Parsing / deserialization / content handling
SEC-06 Secrets / sensitive-data propagation
SEC-07 Privilege / capability boundaries

DATA-01 Persistence / migrations / integrity

REL-01 Errors / fallback / fail-open behavior
REL-02 Availability / amplification / resource exhaustion
REL-03 Business abuse / replay / ordering / idempotency

OPS-01 Configuration / deployment assumptions
OPS-02 Supply chain / dynamic loading / update path
OPS-03 Observability / logging / privacy

COMP-01 Cross-version / legacy / compatibility surfaces

QUAL-01 Performance / blocking / queue/cache pressure
QUAL-02 Tests / testability / evidence quality
```

The taxonomy is mechanism-oriented and framework-neutral.

## 6. High-risk proof-of-coverage contracts

The following require stronger evidence than a generic thematic pass:

```text
SEC-01 Authorization / identity
SEC-02 Interpreter / dynamic construction
SEC-03 Resource addressing
SEC-04 Outbound network target control
SEC-05 Parsing / deserialization
SEC-06 Secrets / sensitive-data propagation
SEC-07 Privilege / capability boundaries
REL-03 Business abuse / replay / ordering
COMP-01 Cross-version / legacy surfaces
```

### SEC-01 Authorization / identity

Minimum trace:

```text
entrypoint / capability
→ authentication context
→ caller identity
→ object / workspace / owner scope
→ authorization decision
→ read/write side effect
→ alternate/fallback path
```

Representative point-read, list/bulk, write, and alternate-token/versioned paths should be considered where applicable.

### SEC-02 Interpreter / dynamic construction

Minimum trace:

```text
sink inventory
→ source/provenance
→ validation / normalization / escaping / parameterization
→ dynamic construction
→ interpreter semantics
→ reachable effect
```

Relevant mechanisms include raw SQL/ORM escape hatches, shell/CLI construction, template/eval/expression engines, regex built from untrusted input, and other query/interpreter DSLs.

Sources must be distinguished at least as:

```text
direct untrusted
validated / allowlisted
hardcoded constant
persisted / second-order
unresolved provenance
```

A raw API name alone is not a finding.

### SEC-03 Resource addressing

```text
external identifier
→ normalization / canonicalization
→ authorization/root boundary
→ path/object-key construction
→ filesystem/storage effect
```

Consider traversal, symlink/TOCTOU, archive extraction, temp files, object keys, overwrite/collision, and user-controlled filenames where applicable.

### SEC-04 Outbound network target control

```text
source URL/target
→ parsing / allowlist
→ DNS / redirect / proxy behavior
→ network client
→ reachable network zone / credential exposure
```

### SEC-05 Parsing / deserialization

```text
input/content
→ parser/deserializer
→ parser options / size limits
→ object construction / expansion
→ side effect / resource cost
```

### SEC-06 Secrets / sensitive-data propagation

```text
secret/sensitive source
→ use
→ logs/errors/traces
→ argv/env
→ storage/cache
→ network/export
→ cleanup/redaction
```

### SEC-07 Privilege / capability boundaries

```text
caller/context
→ capability acquisition
→ privileged API/process/device/socket
→ authorization
→ scope/lifetime
→ effect
```

### REL-03 Business abuse / replay / ordering

```text
business action
→ identity/scope
→ replay/idempotency behavior
→ ordering/concurrency
→ authoritative state
→ observable/business effect
```

### COMP-01 Cross-version / legacy

When a material candidate is found in a versioned/shared path, perform projection search across relevant sibling versions, shared/base implementations, helpers, and compatibility routes. Projections should be grouped by root mechanism rather than inflated into duplicate findings.

## 7. STANDARD_FULL vs FORENSIC

### STANDARD_FULL

- one compact coverage matrix is mandatory;
- multiple domains may share one thematic evidence artifact when the evidence is genuinely sufficient;
- high-risk domains still require concrete proof-of-coverage.

### FORENSIC

- the same matrix is mandatory;
- applicable high-risk domains require explicit evidence trails;
- material domains receive separate thematic sections/artifacts as needed;
- Independent Coverage Review is an explicit gate before candidate verification.

The design does not require one Markdown file per domain.

## 8. Independent Coverage Review

### 8.1 Purpose

The reviewer does **not** ask whether existing candidates are correct. It asks whether a material mechanism class exists in the accepted As-Built but lacks sufficient discovery evidence.

### 8.2 Fresh-context input

The reviewer receives a bounded factual packet:

- accepted As-Built;
- coverage matrix;
- thematic artifact registry;
- candidate registry;
- positive controls;
- open questions;
- baseline/revision binding.

Predecessor reasoning history is not required by default.

### 8.3 Review passes

1. **As-Built reconciliation** — map actual capabilities, interpreters, stores, external systems, privileged surfaces, versioned APIs, background flows, and resource boundaries to matrix domains.
2. **Evidence-quality check** — challenge `COVERED` rows that have no meaningful inventory, traces, positive controls, non-findings, candidates, or explicit N/A reasoning.
3. **Bounded blind-spot probes** — perform small risk-driven probes of selected domains to test whether claimed coverage matches the repository. Examples: raw interpreter escapes, dynamic outbound targets, representative list/read/write authorization paths, one secret-propagation trace, one versioned endpoint family.

The reviewer is not a second full auditor.

Expansion rule:

```text
probe finds no discrepancy
→ stop

probe finds material unreviewed class
→ targeted expansion only
```

### 8.4 Verdicts

```text
COVERAGE_ACCEPTED
COVERAGE_CORRECTION_REQUIRED
COVERAGE_BLOCKED
COVERAGE_AUTHORITY_DRIFT
```

Coverage review never assigns severity and never creates final RF directly.

## 9. Coverage correction and revalidation

A coverage gap triggers targeted correction:

```text
COVERAGE_CORRECTION_REQUIRED
→ targeted thematic pass
→ matrix update
→ new/updated CAND, PC, OQ, non-findings
→ impacted-domain coverage re-review
→ COVERAGE_ACCEPTED | BLOCKED
```

Do not restart the whole audit automatically.

If accepted As-Built later changes, perform a coverage impact scan and mark only affected domains `REVALIDATION_REQUIRED` under the existing freshness discipline.

Example:

```text
new Webhook Dispatcher discovered
→ affected domains:
   ARCH-04 Boundaries
   SEC-04 Outbound Network
   SEC-06 Secrets
→ only those coverage rows are revalidated
```

## 10. Safe Reproduction / Evidence Validation boundary

Runtime reproduction can materially strengthen confidence that an observed mechanism is real, but a public review Skill must not become an exploitation playbook.

This design therefore permits **Safe Reproduction / Evidence Validation** only under the following principles:

- reproduction is optional evidence, not a prerequisite for every finding;
- prefer existing tests, local fixtures, isolated test environments, and synthetic inputs;
- only test systems/repositories the user is authorized to assess;
- do not perform destructive actions, persistence, privilege escalation, credential theft, lateral movement, or data exfiltration;
- do not probe unrelated external targets or third-party infrastructure;
- do not turn a confirmed issue into a reusable offensive payload pack;
- demonstrate the minimum effect necessary to validate the mechanism;
- if safe reproduction is not available, preserve the correct static-evidence confidence/limitation instead of forcing a PoC;
- never claim runtime confirmation without actual runtime evidence.

For an injection-like issue, safe validation should prefer proving construction semantics or a harmless local/test boolean effect over extracting data or chaining capabilities.

This boundary is intentionally narrower than a penetration-testing framework. A dedicated active-security/PoC mode is out of scope for this version.

## 11. Working artifacts

### STANDARD_FULL

Add:

```text
working/
├── 01-discovery-and-scenarios.md
├── 01a-discovery-coverage-matrix.md
├── 01b-independent-coverage-review.md
├── 01c-coverage-correction.md       # conditional
├── 01d-coverage-re-review.md        # conditional
├── 02-independent-verification.md
...
```

### FORENSIC

Add between thematic discovery and current candidate verification:

```text
working/
├── 06a-discovery-coverage-matrix.md
├── 06b-independent-coverage-review.md
├── 06c-coverage-correction.md       # conditional
├── 06d-coverage-re-review.md        # conditional
├── 07-independent-verification.md
...
```

Exact numbering may be adjusted during implementation if needed to avoid awkward migration, but semantic order is normative.

## 12. INDEX projection

`working/INDEX.md` remains the persistent workflow authority but stores only a compact coverage projection, for example:

```text
## Discovery Coverage

coverage_artifact: working/06a-discovery-coverage-matrix.md
coverage_review: COVERAGE_ACCEPTED
baseline: <commit>

domains:
  total: 21
  covered: 16
  not_applicable: 5
  partial: 0
  blocked: 0

high_risk:
  applicable: 8
  accepted: 8
```

The full matrix remains in its owning artifact. Freshness/revision binding rules apply before compact state is used downstream.

## 13. Required reference changes

### New authoritative reference

`references/discovery-coverage.md`

Owns:

- matrix schema;
- domain taxonomy;
- applicability/status semantics;
- high-risk proof-of-coverage;
- Independent Coverage Review;
- correction/re-review;
- coverage completion rules.

### `SKILL.md`

Only orchestration changes:

- insert coverage matrix/review gate between thematic discovery and independent verification;
- add `discovery-coverage.md` to Authority Map;
- add coverage acceptance to Completion Gate.

### `references/review-method.md`

- require thematic discovery to produce/update coverage evidence;
- frame security-sensitive discovery as source/boundary/effect oriented rather than only topic enumeration.

### `references/review-modes-and-orchestration.md`

- add artifacts;
- add coverage stage/correction cycle;
- add compact coverage registry to INDEX;
- define resume/revalidation behavior.

### `references/boundary-contract-audit.md`

Broaden boundary language so interpreter, resource-addressing, and authority boundaries are not implicitly excluded by an IPC/process-centric reading. Detailed coverage semantics remain owned by `discovery-coverage.md`.

### `references/independent-verification.md`

No substantive role expansion. It remains responsible for verifying existing candidates, not discovering missing classes.

### `references/evidence-and-severity.md`

Preserve current attack-chain, confidence, severity, and anti-noise contracts. If Safe Reproduction terminology is referenced, it should state that runtime evidence strengthens confidence but does not authorize exploitation or override the normal candidate lifecycle.

### `references/final-editorial-review.md`

Do not turn editorial review into a technical re-audit. It only checks that final status does not claim `REVIEW_COMPLETE` while coverage is non-accepted.

## 14. Pressure-test strategy

Implementation must remain fail-first.

Known RED baseline:

- **PS-45 — Interpreter Boundary Omission**: current production Skill returned `PS45_RED_DISCOVERY_COVERAGE_GAP_CONFIRMED`.

Additional pressure scenarios should cover:

- **PS-46 — Authorization Completeness**: point endpoint protected, list/bulk scope missing, alternate service-token path.
- **PS-47 — Outbound Target Control**: static destinations plus one dynamic webhook/redirect path.
- **PS-48 — Cross-Version Projection**: issue fixed in new version but retained in old/base/compat path.
- **PS-49 — Secrets Propagation**: secret stored correctly but leaked through exception/log/telemetry propagation.
- **PS-50 — Business Replay / Ordering**: retry/replay creates duplicate durable business effect.
- **PS-51 — False-Positive Resistance**: many raw-looking sites, mostly constants/allowlisted/structured, one direct unsafe sink and one unresolved second-order source.

Success requires higher completeness **without** losing precision.

## 15. Acceptance criteria

The design is implemented successfully only if:

1. Both modes produce a coverage matrix.
2. `FORENSIC` cannot reach candidate verification without `COVERAGE_ACCEPTED`.
3. `STANDARD_FULL` also has compact coverage proof.
4. High-risk domains require semantic evidence, not generic review claims.
5. `NOT_APPLICABLE` requires evidence.
6. Zero findings remains a valid outcome.
7. Independent Coverage Review can detect absence of investigation.
8. Coverage Review remains bounded and does not become a full second audit.
9. New gaps trigger targeted correction rather than global restart.
10. Candidate verification remains a separate gate.
11. Severity remains a separate gate.
12. Search/grep alone is not sufficient proof.
13. Cross-version/projection search is part of completeness.
14. Second-order sources remain unresolved until provenance is demonstrated.
15. Final `REVIEW_COMPLETE` cannot hide material coverage gaps.
16. Existing final-report/editorial contracts remain intact.
17. Safe Reproduction, when used, is non-destructive, authorized, minimal, and explicitly evidenced; lack of a PoC does not force escalation or block a well-supported static finding.
18. The Skill does not become a public exploitation playbook.

## 16. Design decision summary

The chosen architecture is a **general Discovery Coverage Matrix plus Independent Coverage Review**, not a larger security checklist and not a SQL-specific patch.

This addresses the class of failure revealed by PS-45 while preserving the current evidence-first lifecycle and precision controls.
