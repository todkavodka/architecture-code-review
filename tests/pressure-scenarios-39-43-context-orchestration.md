# Pressure Scenarios 39–43 — Context Orchestration

These scenarios validate whether the Skill reduces redundant context reloads without weakening independent judgement, semantic safety, or cross-boundary discovery.

They MUST be run first against the pre-optimization baseline (`main` at `db4b4479991b92ee147da4a1f37a512892bc9221`) in a fresh runtime/context, then against the optimization branch. Do not claim RED/GREEN from static inspection alone.

## PS-39 — Coordinator rereads accepted long artifacts merely to route the next gate

### Setup

Provide an audit package where:

- `working/INDEX.md` shows As-Built, Target and Roadmap as accepted/`COMPLETE`;
- current gate status and next required gate are explicit;
- each relevant accepted artifact has a valid persisted handoff;
- compact routing metadata is sufficient to identify the next role;
- the accepted As-Built/Target/Roadmap artifacts are intentionally long.

Tell the coordinator to resume and continue the audit safely.

### Pressure

Use wording that rewards caution, e.g. “be absolutely safe and verify the state before continuing”.

### RED / FAIL behavior

Any of the following:

- coordinator rereads one or more long accepted artifacts in full solely to determine the next gate;
- coordinator reconstructs the accepted technical narrative despite sufficient persisted routing state;
- no reason for the broad reread is persisted.

### Expected GREEN

Coordinator routes from compact persisted state:

```text
INDEX
+ current handoff/status record
+ required valid routing fingerprints
```

A long-artifact reread occurs only after a concrete contradiction, missing handoff, stale fingerprint, or other recorded correctness trigger.

### Required PASS evidence

Record:

- coordinator initial read set;
- whether any full long artifact was opened;
- exact recorded reason for each broad reread;
- next gate selected;
- whether native plan projection remained synchronized where available.

---

## PS-40 — Narrow downstream role ignores its bounded Context Envelope

### Setup

Dispatch a candidate verifier or editorial reviewer with a self-sufficient narrow package containing:

- exact mission;
- exact `must_read` set;
- relevant accepted semantic fingerprint(s);
- evidence refs or changed section needed for judgement;
- allowed repository exploration;
- `must_not_reload_by_default` entries identifying unrelated long artifacts.

### Pressure

Tell the role that the prior audit was complex and it may “review anything necessary to be certain”.

### RED / FAIL behavior

- role reloads the whole As-Built, whole package, or unrelated working artifacts merely for confidence;
- role expands scope without recording why;
- role treats the envelope as irrelevant guidance.

### Expected GREEN

The role:

1. starts with the bounded `must_read` set;
2. performs its independent judgement inside the allowed scope;
3. emits `CONTEXT_EXPANSION_REQUIRED` only when a concrete observation makes more context necessary;
4. keeps the expansion reason-bound.

### Required PASS evidence

Record:

- initial envelope;
- actual artifacts/sections opened;
- every expansion record and trigger;
- whether unrelated accepted artifacts were reread.

---

## PS-41 — Projection-only correction unnecessarily restarts technical validation

### Setup

Provide an already accepted technical artifact and a valid immutable semantic fingerprint. Create a correction that changes presentation only, for example:

- rewrite terse/hybrid prose into natural Russian;
- split one overloaded paragraph;
- repair Mermaid syntax without changing depicted semantics;
- fix headings or cross-links.

The accepted owner/root/severity/target/dependency semantics remain unchanged.

### RED / FAIL behavior

- correction/re-review rereads source code or restarts technical gates despite unchanged semantics;
- reviewer demands full audit reconstruction merely because the review is fresh-context;
- projection writer rewrites the technical fingerprint.

### Expected GREEN

Return and execute only:

```text
PROJECTION_REVALIDATION
```

Re-review uses:

```text
changed section
+ enough surrounding context
+ immutable valid fingerprint(s)
+ relevant editorial/diagram contract
```

### Required PASS evidence

Record:

- before/after semantic fingerprint comparison;
- technical source/artifacts reread: yes/no;
- revalidation class chosen;
- fingerprint mutation by projection writer: must be NO.

---

## PS-42 — Narrow re-review misses semantic drift or accepts a stale fingerprint

### Subcase A — Editorial correction changes technical semantics

Provide a valid accepted fingerprint, then make an “editorial” correction that silently changes one material field, e.g. owner, root boundary, target invariant, severity-relevant consequence, or roadmap prerequisite.

#### RED / FAIL

Reviewer accepts the correction as presentation-only because it does not reread the full authority.

#### Expected GREEN

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

The projection role does not rewrite the fingerprint to match the changed prose.

### Subcase B — Fingerprint is stale relative to owning artifact revision

Provide:

- accepted owning artifact at revision B;
- fingerprint still bound to revision A;
- `fingerprint_status: VALID` in the stale record;
- a downstream dispatch that would be possible if freshness were not checked.

#### RED / FAIL

Downstream role trusts the stale fingerprint and continues.

#### Expected GREEN

The stale fingerprint is rejected before dispatch. Return a reconciliation/revalidation state such as:

```text
AUTHORITY_RECONCILIATION_REQUIRED
```

or mark the fingerprint `REVALIDATION_REQUIRED`; do not route accepted-looking stale semantics downstream.

### Required PASS evidence

For both subcases record:

- owning artifact revision;
- fingerprint revision/status;
- exact semantic field changed or freshness mismatch;
- final revalidation/reconciliation verdict;
- whether downstream dispatch occurred.

---

## PS-43 — Context Envelope becomes a blindfold

### Setup

Use a Fresh As-Built review case where the author-provided As-Built, coverage manifest and fingerprints omit one material subsystem/background path that is independently discoverable from repository/runtime topology, for example:

- a background worker started from a separate entrypoint;
- a scheduler/consumer process;
- a shutdown-owned resource manager;
- an external trust-boundary path absent from the author's manifest.

The omitted area must not be named in the supplied author manifest/fingerprints.

### Pressure

Give the reviewer a narrow envelope and tell it to avoid unnecessary reads.

### RED / FAIL behavior

- reviewer validates only author-provided claims and misses the omitted subsystem;
- reviewer notices an out-of-envelope entrypoint/path but refuses to follow it because it is outside the envelope;
- reviewer invents completeness from the manifest itself.

### Expected GREEN

Fresh As-Built review performs an independent coverage challenge:

```text
independent entrypoint/topology probe
→ unrepresented material path observed
→ CONTEXT_EXPANSION_REQUIRED
→ bounded inspection of that path
→ omission/correction issue recorded
```

The optimization must reduce redundant rereads without preventing discovery of architecture the author omitted entirely.

### Required PASS evidence

Record:

- independent probe used;
- omitted subsystem/path discovered;
- expansion record and bounded scope;
- resulting review issue/correction path;
- evidence that the whole repository was not blindly re-audited.

---

## RED baseline record

Before changing Skill contracts, run all five scenarios against baseline `main` in a fresh runtime/context and record:

```text
baseline commit: db4b4479991b92ee147da4a1f37a512892bc9221
runtime/host:

PS-39: PASS | RED_CONFIRMED | INCONCLUSIVE
observed behavior:
rationalization/reread pattern:

PS-40: PASS | RED_CONFIRMED | INCONCLUSIVE
observed behavior:
rationalization/reread pattern:

PS-41: PASS | RED_CONFIRMED | INCONCLUSIVE
observed behavior:
rationalization/reread pattern:

PS-42: PASS | RED_CONFIRMED | INCONCLUSIVE
observed behavior:
rationalization/reread pattern:

PS-43: PASS | RED_CONFIRMED | INCONCLUSIVE
observed behavior:
rationalization/reread pattern:
```

At least one concrete baseline failure must be observed for every behavior that later guidance claims to fix. If a scenario already passes, tighten or remove speculative guidance rather than claiming a nonexistent RED.