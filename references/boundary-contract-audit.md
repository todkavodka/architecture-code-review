# Boundary Contract Audit

Use this reference to analyze material boundaries where data, identity, authority, or dynamic construction crosses from one semantic contract into another. Factual boundary objects and views — components, interfaces, interactions, flows, auth/trust, stores, configuration, and error contracts — are consumed from accepted, sufficiently fresh STM. This reference does not maintain a parallel factual boundary inventory.

The scope includes not only IPC, API, RPC, native, process, and event interaction boundaries, but also:

```text
interaction boundaries
interpreter boundaries
resource-addressing boundaries
authority / capability boundaries
```

This is not a checklist for producing volume. The purpose is to determine whether a boundary preserves the required identity, ordering, cancellation, ownership, validation/trust semantics, and error behavior.

Discovery completeness for boundary classes is governed by `discovery-coverage.md`. This file defines the dimensions and method for analyzing a specific boundary.

## Boundary types

### Interaction boundaries

IPC, API, RPC, native, process, or event transitions between a producer and a consumer.

### Interpreter boundaries

Dynamic text or value construction that is later interpreted by a SQL engine, shell, template/eval/expression engine, regex/query DSL, or another interpreter-like consumer.

### Resource-addressing boundaries

Transitions from an external or persisted identifier to a filesystem path, object-storage key, archive target, temporary resource, URL/endpoint, or another resource locator.

### Authority / capability boundaries

A point where caller identity or context is converted into permission or capability: a privileged API, admin/service path, native bridge, process/device/socket control, mutation authority, or access to protected state.

One runtime path may cross several boundary types at once.

## Contract dimensions

| Dimension | Review question |
|---|---|
| Identity | Which entity or owner does the operation concern? Can a local ID be ambiguous without parent identity? |
| Correlation | Can a response or event be unambiguously correlated with the request that initiated it? |
| Ordering | What happens to a late or out-of-order response/event? |
| Concurrency | Can two operations coexist without overwriting each other’s state? |
| Cancellation | Which exact operation is cancelled? Is cancellation scoped or global? |
| Timeout | Is waiting bounded where infinite waiting is not an explicit contract? |
| Authorization / trust | Who may invoke the capability, and at which boundary is that authority checked? |
| Validation | Are runtime arguments, shape, range, and content validated at the boundary? |
| Provenance | Who controls the value: direct external input, validated input, persisted data, configuration, constant, or internal state? |
| Construction / interpretation | Does the value become executable/interpreted syntax or remain a bind/data value? Which escaping or parameterization semantics actually apply? |
| Resource resolution | How is the identifier normalized/canonicalized, and to which actual resource, root, or network target does it resolve? |
| Serialization | Can the payload actually be serialized across the boundary safely and unambiguously? |
| Lifecycle | Who registers and unregisters the handler, listener, or subscription? |
| Ownership | Who is allowed to mutate the referenced resource or state? |
| Error contract | Can the caller distinguish error classes while preserving context? |
| Backpressure | Can the producer outrun the consumer, and what happens if it does? |

Not every dimension applies to every boundary type.

## Method

1. Obtain the accepted, sufficiently fresh STM boundary objects/views for the scope of this pass and verify their coverage, freshness, and provenance. If the factual slice is missing, stale, or conflicting, request `TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT`, or `TECH_FACT_REVALIDATION_REQUEST` through the Technical Model Gate. Do not silently create a second inventory.
2. For every material path, trace producer/source → boundary → consumer/interpreter/resource → side effect → response/event/effect.
3. Separately record runtime validation, provenance, sender/origin/trust checks, and parameterization/normalization semantics where applicable.
4. For stateful or asynchronous boundaries, test the duplicate, in-flight, cancel, and late-completion scenarios from `ownership-and-scenarios.md`.
5. Record Positive Controls. A missing check in one layer may be compensated by a real guarantee in another layer; trace that guarantee instead of assuming it.
6. Use `discovery-coverage.md` to prove that material boundary classes were considered. One well-analyzed IPC path does not automatically close interpreter, resource, or authority coverage.

## IPC / event-specific

Check:

- generic preload surface vs an actually reachable renderer compromise;
- `sendToAllWindows` / broadcast semantics;
- listener accumulation and cleanup;
- request IDs and owner IDs;
- actual `.on` / `.once` EventEmitter semantics rather than an intuitive model;
- cases where an event payload contains identity but the consumer ignores it;
- use of renderer selection state as owner identity for asynchronous completion.

A broad capability surface without a reachable attacker entry point is not automatically an RCE finding. Security promotion is governed by `evidence-and-severity.md`.

## Interpreter-specific

For raw or dynamic interpreter construction, trace:

```text
source provenance
→ validation / allowlist
→ escaping / parameterization
→ construction
→ interpreter semantics
→ reachable effect
```

Do not equate:

```text
string interpolation into a bind/data value
```

with:

```text
string interpolation into interpreted command/query text
```

Do not create a finding from a raw-looking API without concrete provenance and effect.

Detailed source classifications and proof-of-coverage requirements are defined in `discovery-coverage.md`.

## Resource-addressing-specific

Check:

- normalization and canonicalization;
- root/scope containment;
- path traversal;
- symlink and TOCTOU semantics;
- archive extraction destination;
- object-key collisions and overwrites;
- user-controlled filenames;
- URL/host/redirect/proxy target resolution;
- cleanup ownership.

## Authority / capability-specific

Check:

- caller identity and context;
- object/workspace/owner scope;
- alternate service/admin paths;
- capability acquisition and lifetime;
- privileged API/process/device/socket access;
- stale identity/capability reuse;
- read vs write authority;
- bulk/list semantics vs point-operation semantics.

## Native/process boundaries

For child processes, CLIs, and native integrations, check:

- arguments and secrets in argv/environment;
- shell usage and quoting;
- process ownership and lifetime;
- cancellation/termination scope;
- fixed ports, files, and temporary paths;
- exit/error propagation;
- privilege boundaries and elevation;
- cleanup during shutdown.

## Output

Every material boundary issue must record:

```text
boundary type
boundary
identity/scope
source/producer
consumer/interpreter/resource
provenance
reachable scenario
failed/absent contract
existing guard/falsification
concrete impact
```

Do not create findings for every uncovered dimension. Dimensions are an analysis lens, not a quota.

## Product-spanning Architecture boundaries

For Product scope, record every participating Project, repository/scope binding, accepted Product baseline, qualified evidence, and STM relation when an architectural claim crosses a Project boundary. A cross-project relation or shared resource is factual context, not by itself an Architecture finding; the Architecture Review owner must adjudicate the material Product consequence. A Project-local boundary claim remains local unless that independent consequence is established.