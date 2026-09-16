# Discovery Coverage Assurance

This file is the **authoritative reference** for proving completeness of thematic discovery: the Discovery Coverage Matrix, applicability and status semantics, proof of coverage, Independent Coverage Review, targeted coverage correction, and coverage revalidation.

It answers one question:

> Which material mechanism classes actually exist in the system, and is there evidence that every applicable class was investigated before discovery was considered complete?

It **does not** replace `independent-verification.md`, `root-boundary-adjudication.md`, or `evidence-and-severity.md`.

## 1. Core invariant

The number and severity of findings do not prove audit completeness. This is the Architecture Review specialization of the shared bounded material-accounting principle in `shared-assurance-principles.md`; it does not replace or absorb the separate bounded target universe used by Test Review.

Discovery completeness is established through:

```text
accepted/fresh STM and the As-Built projection
→ mechanism coverage
→ evidence trail
→ independent coverage challenge
```

Zero findings is acceptable when applicable domains were genuinely investigated and coverage evidence is sufficient.

Many findings do not permit an unreviewed material domain to be marked complete.

Discovery Coverage remains Architecture Review authority. It is distinct from the factual STM matrix and `TECHNICAL_MODEL_COVERAGE_ACCEPTED`: STM coverage asks whether the required technical surface is represented, while this matrix asks whether architecture and risk mechanism classes were investigated. STM acceptance does not prove architectural discovery, and `COVERAGE_ACCEPTED` does not make `PARTIAL`, `BLOCKED`, or `UNKNOWN` STM rows complete.

## 2. Discovery Coverage Matrix

Both `STANDARD_FULL` and `FORENSIC` maintain a Discovery Coverage Matrix.

Minimum row:

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

### 2.1 Applicability

Closed set:

```text
YES
NO
CONDITIONAL
```

`YES` — the mechanism clearly exists and requires coverage evidence.

`NO` — the mechanism is architecturally absent on the accepted baseline.

`CONDITIONAL` — required depth depends on the actually discovered capability or implementation shape.

`NO` does not automatically mean `NOT_APPLICABLE`: an evidence-based reason tied to accepted As-Built and/or a targeted inventory is required.

### 2.2 Coverage status

Closed set:

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

`NOT_APPLICABLE` is allowed only with a concrete evidence-based explanation.

Statements such as:

```text
Security: COVERED — security reviewed
Controllers: COVERED — grep completed
```

are not sufficient evidence.

## 3. What counts as coverage evidence

Coverage evidence may include:

- inspected paths and concrete call/data/control chains;
- targeted inventory or search results bound to the baseline;
- representative semantic traces of high-risk sites;
- Positive Controls;
- considered-but-not-promoted conclusions and non-findings;
- open questions for unresolved provenance or intent;
- evidence-based proof that a mechanism class is absent.

Search or grep is an **inventory mechanism**, not semantic proof.

`COVERED` requires enough interpretation to distinguish, where applicable:

```text
safe
unsafe candidate
ambiguous / unresolved
not applicable
```

Do not require a complete line-by-line reread of the repository when a bounded inventory plus representative and high-risk semantic traces provide sufficient confidence about the class.

## 4. Canonical coverage domains

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

The taxonomy is mechanism-oriented and framework-neutral. It is not a vulnerability quota.

## 5. Shared proof-of-coverage rules

For every applicable domain, coverage closeout must answer at least four questions:

1. **What was inventoried?**
2. **Which representative or high-risk traces were actually followed?**
3. **How were material sites or mechanisms classified?**
4. **What remains unresolved or blocked?**

If these answers do not exist, `COVERED` is not justified.

For the high-risk domains below, a generic thematic paragraph is insufficient.

## 6. High-risk proof-of-coverage contracts

Stronger proof is mandatory for:

```text
SEC-01 Authentication / authorization / identity / scope
SEC-02 Interpreter / dynamic construction
SEC-03 Resource addressing / filesystem / paths
SEC-04 Outbound network target control
SEC-05 Parsing / deserialization / content handling
SEC-06 Secrets / sensitive-data propagation
SEC-07 Privilege / capability boundaries
REL-02 Availability / amplification / resource exhaustion
REL-03 Business abuse / replay / ordering / idempotency
COMP-01 Cross-version / legacy / compatibility surfaces
```

### 6.1 SEC-01 — Authentication / authorization / identity / scope

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

Where applicable, inspect representative:

- point-read;
- list/bulk read;
- write/mutation;
- admin/service-token path;
- versioned/compatibility path;
- asynchronous or cross-service identity propagation.

The presence of auth middleware or a successful login path does not close the domain by itself.

If session or token mechanisms exist, coverage includes lifecycle semantics:

- issuance;
- refresh/rotation;
- revocation;
- expiry;
- replay resistance;
- stale sessions;
- session fixation;
- issuer/audience/signature verification;
- service/admin fallback credentials;
- identity propagation across asynchronous or service boundaries.

Object-level or scope authorization and session/token lifecycle are different dimensions within the same domain; evidence for one does not prove the other.

### 6.2 SEC-02 — Interpreter / dynamic construction

Minimum trace:

```text
sink inventory
→ source/provenance
→ validation / normalization / escaping / parameterization
→ dynamic construction
→ interpreter semantics
→ reachable effect
```

Relevant mechanisms, when present, include:

- raw SQL and ORM escape hatches;
- shell or CLI command construction;
- template, eval, or expression engines;
- regex derived from external or persisted input;
- query/search DSLs;
- other interpreter-facing dynamic text.

For arguments and sources, distinguish at least:

```text
direct untrusted
validated / allowlisted
hardcoded constant
persisted / second-order
unresolved provenance
```

A raw API name, f-string, string concatenation, or dynamic expression is not a finding by itself.

Example semantic distinction:

```text
direct HTTP input -> raw SQL text          => material candidate if reachable effect exists
persisted DB value -> raw SQL text         => second-order provenance unresolved until write path is traced
hardcoded constant -> raw SQL text         => non-finding from injection perspective
finite allowlist -> raw identifier/order   => may be safe when validation semantics are proven
f-string -> structured ORM bind value      => not equivalent to raw SQL construction
```

### 6.3 SEC-03 — Resource addressing / filesystem / paths

Minimum trace:

```text
external/resource identifier
→ normalization / canonicalization
→ authorization/root boundary
→ path/object-key construction
→ filesystem/storage effect
```

Consider where applicable:

- path traversal;
- symlink / TOCTOU;
- temporary files;
- archive extraction;
- object-store keys;
- overwrite or collision;
- user-controlled filenames;
- cleanup ownership.

API or type names such as `Path` are not protection by themselves. Prove the actual normalization, root, and authorization semantics.

### 6.4 SEC-04 — Outbound network target control

Minimum trace:

```text
source URL/target
→ parsing / allowlist
→ DNS / redirect / proxy behavior
→ network client
→ reachable network zone / credential exposure
```

Consider:

- user- or configuration-controlled scheme, host, or port;
- webhooks and callbacks;
- redirects;
- proxy/environment interaction;
- credential forwarding;
- internal or metadata-like destinations;
- destination validation before and after redirects where relevant.

Do not label something SSRF merely because an HTTP client exists. Control over destination plus a reachable effect is required.

### 6.5 SEC-05 — Parsing / deserialization / content handling

Minimum trace:

```text
input/content
→ parser/deserializer
→ parser options / size limits
→ object construction / expansion
→ side effect / resource cost
```

Consider where applicable:

- object deserialization;
- YAML, XML, document, image, or archive parsers;
- multipart or upload pipelines;
- active content;
- parser recursion and size limits;
- archive or decompression expansion.

If the system does not accept materially complex content and a targeted inventory establishes that fact, evidence-backed `NOT_APPLICABLE` is allowed.

### 6.6 SEC-06 — Secrets / sensitive-data propagation

Minimum trace:

```text
secret/sensitive source
→ use
→ logs/errors/traces
→ argv/env
→ storage/cache
→ network/export
→ cleanup/redaction
```

Review is not limited to where a secret is stored.

Consider:

- access, refresh, and API tokens;
- credentials and passwords;
- DSN or service credentials;
- sensitive business or user data;
- exception bodies;
- structured logs and tracing attributes;
- query strings and URLs;
- subprocess argv/env inheritance;
- debug dumps and caches;
- telemetry and exporters.

### 6.7 SEC-07 — Privilege / capability boundaries

Minimum trace:

```text
caller/context
→ capability acquisition
→ privileged API/process/device/socket
→ authorization
→ scope/lifetime
→ effect
```

Consider:

- elevation and sudo-like flows;
- service accounts;
- Docker/container/host-control sockets;
- host mounts and devices;
- native APIs;
- browser preload/native bridges;
- privileged admin or local endpoints;
- dynamic plugin/module capabilities.

The key question is: who can actually activate the capability, and with what scope and lifetime?

### 6.8 REL-02 — Availability / amplification / resource exhaustion

Minimum trace:

```text
untrusted/request-driven work
→ amplification factor
→ bounded/unbounded resource
→ cancellation/backpressure/limits
→ service impact
```

Consider where applicable:

- unbounded request bodies;
- decompression or parser expansion;
- pathological regex or expression cost;
- expensive fan-out;
- queue or cache growth;
- retry storms;
- worker starvation;
- blocking or exhausted resource pools;
- request-driven amplification.

Generic slowness or performance suspicion is not a material security/reliability finding without a reachable effect.

### 6.9 REL-03 — Business abuse / replay / ordering / idempotency

Minimum trace:

```text
business action
→ identity/scope
→ replay/idempotency behavior
→ ordering/concurrency
→ authoritative state
→ observable/business effect
```

Consider:

- duplicate submission;
- replay;
- stale or out-of-order completion;
- duplicate durable side effect;
- cancellation races;
- retry changing business semantics;
- quota, accounting, or state-transition bypass.

This is a material correctness/security domain even when no classic injection or authentication vulnerability exists.

### 6.10 COMP-01 — Cross-version / legacy / compatibility surfaces

When a material candidate is found in a versioned or shared path, search applicable projections across:

```text
sibling API versions
shared/base implementations
helpers
compatibility routes
legacy/fallback paths
copied equivalent blocks
```

Do not automatically create a separate root finding for every match. Root/projection identity is determined downstream by `root-boundary-adjudication.md`.

## 7. Conditional mechanisms

### 7.1 Cryptography / signatures / TLS

Cryptography, signature/token verification, and TLS-specific mechanisms are not a mandatory separate domain.

When they actually exist, review them inside the relevant `SEC-*` domain:

- issuer/audience/signature verification;
- randomness, nonces, and IVs;
- certificate and TLS verification;
- key handling;
- home-grown cryptographic constructions.

Do not invent cryptography findings in a project that has no relevant mechanism.

### 7.2 Supply chain / dynamic loading / update path

`OPS-02` uses applicability-driven depth.

Material applicability exists, for example, when the system contains:

- plugin or module loading;
- runtime extensions;
- installers or hooks;
- update mechanisms;
- executable or module search paths;
- dynamic imports from externally influenced locations.

If those mechanisms do not exist, evidence-backed `NOT_APPLICABLE` is allowed.

## 8. STANDARD_FULL and FORENSIC

### STANDARD_FULL

- one compact Discovery Coverage Matrix is mandatory;
- one thematic artifact may cover several domains when the evidence is genuinely sufficient;
- high-risk domains retain concrete proof of coverage;
- coverage closeout is mandatory before candidate verification.

### FORENSIC

- the same matrix is mandatory;
- applicable high-risk domains have an explicit evidence trail;
- material domains receive separate thematic sections or artifacts when needed;
- Independent Coverage Review is a separate explicit gate before candidate verification.

Do not mechanically create one Markdown file per domain.

## 9. Discovery closeout

Before Independent Coverage Review, the coordinator reconciles every matrix row.

For every domain, only an honest current state is allowed:

```text
COVERED
PARTIALLY_COVERED
BLOCKED
NOT_APPLICABLE
```

If a row remains `PARTIALLY_COVERED`, perform targeted discovery before review or hand the gap to the reviewer explicitly.

If a material row is `BLOCKED`, ordinary downstream acceptance is prohibited.

`DISCOVERY_COMPLETE` means the planned thematic passes have finished as artifacts. It **does not** mean discovery coverage has been accepted.

Candidate verification may begin only when:

```text
DISCOVERY_COMPLETE
AND
COVERAGE_ACCEPTED
```

## 10. Independent Coverage Review

### 10.1 Purpose

The Coverage Reviewer does not re-check the correctness of every existing `CAND-*`.

The primary question is:

> Is there a material mechanism or class visible from accepted As-Built or a bounded probe that lacks sufficient discovery coverage evidence?

This is a review of **absence of investigation**, not candidate correctness.

### 10.2 Fresh-context packet

By default, the reviewer receives a bounded factual packet:

- accepted technical As-Built;
- Discovery Coverage Matrix;
- thematic artifact registry;
- candidate registry;
- Positive Controls;
- open questions;
- baseline/revision binding.

Do not pass predecessor chain-of-thought or reasoning history as authority.

If the packet is insufficient for a specific coverage challenge, the reviewer may expand context only from a concrete recorded trigger.

### 10.3 Pass 1 — As-Built reconciliation

Map actual capabilities to the matrix:

- runtimes and processes;
- APIs, IPC, and events;
- interpreters and dynamic construction;
- stores, files, and resources;
- external network dependencies;
- privileged capabilities;
- background and lifecycle mechanisms;
- versioned and legacy surfaces;
- content and parser surfaces;
- sensitive-data flows.

If a capability exists while the corresponding domain is absent or unjustifiably `NOT_APPLICABLE`, that is a coverage gap.

### 10.4 Pass 2 — Evidence-quality challenge

Challenge `COVERED` especially when the row contains:

```text
inventory: none
semantic traces: none
candidates: none
positive controls: none
non-findings: none
open questions: none
evidence_refs: generic thematic file only
```

Zero findings is acceptable. Zero evidence of investigation is not.

### 10.5 Pass 3 — Bounded blind-spot probes

Choose several risk-driven probes based on accepted As-Built and matrix claims.

Examples:

- raw/interpreter escape-hatch inventory;
- dynamic outbound target sites;
- representative list/read/write authorization paths;
- one session/token lifecycle path;
- one secret-propagation path;
- one request-driven amplification path;
- one versioned endpoint family.

Expansion rule:

```text
probe finds no discrepancy
→ stop

probe finds material unreviewed class
→ targeted expansion only
```

The Coverage Reviewer does not become a second full auditor.

## 11. Coverage review verdicts

Closed set:

```text
COVERAGE_ACCEPTED
COVERAGE_CORRECTION_REQUIRED
COVERAGE_BLOCKED
COVERAGE_AUTHORITY_DRIFT
```

### COVERAGE_ACCEPTED

Matrix claims are sufficiently supported; no material gaps were found.

### COVERAGE_CORRECTION_REQUIRED

One or more domains were under-investigated or `COVERED` lacks sufficient evidence.

### COVERAGE_BLOCKED

A material domain cannot be reviewed sufficiently because required source, access, tool, or runtime evidence is unavailable. The blocker must be concrete.

### COVERAGE_AUTHORITY_DRIFT

Accepted As-Built or baseline changed, or was contradicted, such that the matrix is no longer bound to current authority.

Coverage Review:

- does not assign severity;
- does not create final `RF-*` directly;
- does not self-correct owning thematic artifacts;
- does not accept disputed As-Built as fact without authority reconciliation.

## 12. Coverage correction

When a gap is found:

```text
COVERAGE_CORRECTION_REQUIRED
→ targeted thematic pass
→ matrix update
→ new/updated CAND / PC / OQ / non-findings
→ impacted-domain coverage re-review
→ COVERAGE_ACCEPTED | COVERAGE_BLOCKED
```

Do not restart the entire audit automatically.

Correction scope records:

```text
domain
trigger
missing fact/mechanism
why it matters
paths/surfaces inspected
result
new candidates / positive controls / open questions
```

## 13. Coverage freshness / revalidation

Discovery Coverage is bound to the accepted As-Built revision and repository baseline.

If technical As-Built changes after accepted coverage:

```text
As-Built correction
→ coverage impact scan
→ only affected domains become REVALIDATION_REQUIRED
```

Example:

```text
new Webhook Dispatcher discovered
→ ARCH-04 Boundary Contracts
→ SEC-04 Outbound Network
→ SEC-06 Sensitive Data
```

Do not invalidate unrelated accepted rows without evidence of impact.

The compact coverage summary in `working/INDEX.md` is usable downstream only with the correct freshness/revision binding from `revalidation-and-freshness.md`; the summary is coordinator state, not a Stage B projection artifact.

## 14. Safe Reproduction / Evidence Validation interaction

Coverage evidence and candidate verification may use Safe Reproduction according to `evidence-and-severity.md`, but reproduction:

- is not mandatory for every row or finding;
- does not replace source, provenance, or semantic tracing;
- does not permit a coverage probe to become an exploitation exercise;
- does not automatically increase severity.

If runtime validation is unavailable or unsafe, record the limitation and use the actual strength of static evidence.

## 15. Anti-noise / precision rules

Discovery Coverage Assurance does not permit:

- a finding quota per domain;
- treating `Raw`, `eval`, an HTTP client, or a path API as vulnerability keywords;
- automatic promotion of every inventory hit;
- severity assignment during coverage closeout;
- a giant repository reread for checkbox completion;
- generic grep as sufficient proof;
- invented findings for `NOT_APPLICABLE` domains;
- false certainty for persisted or second-order sources with unresolved provenance.

Primary precision invariant:

```text
coverage completeness != finding inflation
```

## 16. Completion contract

Ordinary accepted downstream flow is prohibited while material coverage has any of these statuses or verdicts:

```text
PARTIALLY_COVERED
BLOCKED
COVERAGE_CORRECTION_REQUIRED
COVERAGE_BLOCKED
COVERAGE_AUTHORITY_DRIFT
REVALIDATION_REQUIRED
```

Progression to candidate verification requires:

```text
DISCOVERY_COMPLETE
AND
COVERAGE_ACCEPTED
```

Final `REVIEW_COMPLETE` is impossible while the coverage gate is not accepted or a material coverage limitation is hidden.