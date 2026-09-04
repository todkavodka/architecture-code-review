# Technical Model Coverage

This reference owns bounded accounting of the factual system surface required by
the [Shared Technical Model](shared-technical-model.md). It defines the
`TECHNICAL_MODEL_COVERAGE_ACCEPTED` gate. It does not own technical fact
lifecycle, evidence observations, capability findings, or Architecture
Discovery Coverage.

## 1. Full technical domains

A `FULL` STM matrix contains each domain in this closed list exactly once and
classifies every materially applicable domain:

1. System Context
2. Components / Runtime Units
3. Entry Points
4. Provided Interfaces
5. Consumed Interfaces
6. Interactions
7. Events / Messaging
8. Data Stores / Persistence
9. State Ownership
10. Material Flows
11. Lifecycle / State Machines
12. Authentication / Authorization / Trust
13. Error / Failure Contracts
14. Configuration Surface
15. Concurrency / Serialization / Idempotency Mechanisms
16. Deployment / Runtime Topology
17. Observability Mechanisms
18. Platform-Specific Behavior

The matrix is materiality- and evidence-bounded. A domain absent by design is
recorded as `NOT_APPLICABLE` with the evidence-backed reason; it is not omitted.

## 2. Matrix rows and status vocabulary

Each domain row records its status, supporting STM facts/evidence, and the
current baseline and requested depth. The only row statuses are:

```text
PENDING
IN_PROGRESS
ACCEPTED
PARTIAL
BLOCKED
NOT_APPLICABLE
UNKNOWN
```

Every status other than `ACCEPTED` requires an evidence-based reason and a
downstream impact. In particular, `PARTIAL`, `BLOCKED`, and `UNKNOWN` are not
complete and cannot be concealed by a model-level prose verdict.

## 3. `FULL` semantics

`FULL` means every material applicable domain is bounded and classified with
sufficient evidence for the requested depth. It is not a requirement to record
every private helper or local function.

For interfaces and interactions, `FULL` means all known material externally
visible or architecturally relevant surfaces within the evidence-bounded scope.

## 4. Architecture mode projection

Both modes use one STM schema. They differ only in required population depth,
evidence granularity, flow detail, contradiction treatment, and review rigor.

```text
STANDARD_FULL:
  coverage: FULL
  depth: COMPACT
  evidence: MATERIAL
  flows: REPRESENTATIVE
  contradictions: MATERIAL
  review: full-model independent review

FORENSIC:
  coverage: FULL
  depth: FORENSIC
  evidence: GRANULAR
  flows: MECHANISM_COMPLETE_WHERE_MATERIAL
  contradictions: EXPLICIT_MULTI_VIEW
  review: critical-slice review where material + full-model integration review
```

`FULL/FORENSIC` satisfies `FULL/COMPACT`. Upgrading `STANDARD_FULL` to
`FORENSIC` enriches the same accepted model; it does not restart factual
discovery or create a second schema.

## 5. Technical Model Coverage Review gate

For a full Architecture Review, every material applicable row must be
`ACCEPTED` before the independent Technical Model Coverage Review can emit
`TECHNICAL_MODEL_COVERAGE_ACCEPTED`. A `NOT_APPLICABLE` row is admissible only
with its evidence-backed reason. The review binds its decision to the STM
baseline, requested coverage/depth, and owning matrix.

Capability execution that requires a complete factual substrate—including
Architecture thematic discovery—remains blocked until this gate is accepted.
An editor, projection, or reviewer prose verdict cannot override
`PARTIAL`, `BLOCKED`, or `UNKNOWN` rows; correct the bounded matrix and repeat
the required review instead.

## 6. Separate coverage authorities

Technical Model Coverage answers whether factual discovery bounded the required
technical system surface. [Architecture Discovery Coverage](discovery-coverage.md)
answers whether Architecture Review investigated the material
architecture/security/reliability mechanism classes required by its own
contract. Neither gate accepts, replaces, or contains the other.

For the full Architecture Review sequence:

```text
Shared Evidence
→ FULL STM
→ Technical Model Coverage Review
→ TECHNICAL_MODEL_COVERAGE_ACCEPTED
→ Architecture thematic discovery
→ Architecture Discovery Coverage
→ COVERAGE_ACCEPTED
→ candidate verification
```
