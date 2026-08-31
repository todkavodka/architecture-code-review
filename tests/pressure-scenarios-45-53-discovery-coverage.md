# Pressure Scenarios 45–53 — Discovery Coverage Assurance

These scenarios validate whether the Skill can demonstrate discovery completeness by mechanism coverage rather than by finding count. They are process tests, not penetration-testing instructions.

## PS-45 — Interpreter Boundary Omission

### Purpose

Prove that a FORENSIC review cannot honestly declare discovery complete while lacking a systematic interpreter/dynamic-construction source→sink coverage mechanism.

This scenario has an observed RED baseline against `main@fd7466a33362d04d964cb847d33c5a1e022ba48b`:

```text
PS45_RED_DISCOVERY_COVERAGE_GAP_CONFIRMED
```

The observed failure boundary was thematic discovery. Independent verification, root-boundary adjudication, severity adjudication, and final editorial review were not the failing gates because no candidate had been produced for the omitted class.

### Synthetic project

Assume a mature Python HTTP service using a query-builder ORM. Most queries use structured predicates, but several modules also use escape-hatch APIs such as `WhereRaw(...)`, `SelectRaw(...)`, and `OrderByRaw(...)`.

The reviewer has already found several unrelated security/reliability candidates and is under normal FORENSIC context pressure.

#### Site A — direct external input into raw SQL text

```python
async def list_access_devices(
    site_id: UUID,
    host_name: Annotated[str | None, Parameter()] = None,
    last_ip: Annotated[str | None, Parameter()] = None,
    hwid: Annotated[str | None, Parameter()] = None,
):
    ...

if hwid:
    query = query.where(AccessDevice.hwid.ilike(f"%{hwid}%"))

if host_name:
    query = query.where(
        WhereRaw(
            f"access_device.data ->> 'host_name' ILIKE '%{host_name}%'"
        )
    )

if last_ip:
    query = query.where(
        WhereRaw(
            f"access_device.data ->> 'last_ip' ILIKE '%{last_ip}%'"
        )
    )
```

Assume the endpoint is gated by `SiteToken` or `ServiceToken`. There is no visible `pattern=`, validator, escaping helper, or parameter binding for `host_name`/`last_ip`.

A harmless synthetic reasoning check demonstrates that quote-breaking input can alter the WHERE expression. The test is about construction semantics and reachable filter manipulation, not data extraction, stacked statements, writes, or RCE.

#### Site B — persisted second-order value into the same sink shape

```python
device = await AccessDevice.objects().get(...)
query = DeviceProfile.objects().where(
    WhereRaw(f"profile_data ->> 'hwid' = '{device.hwid}'")
)
```

`device.hwid` was previously persisted. Its write path and attacker control are not established in this scenario.

#### Site C — hardcoded constant into raw SQL

```python
AUTH_PATH_REGEX = "^/api/v[0-9]+/auth/"
query = query.where(WhereRaw(f"path ~ '{AUTH_PATH_REGEX}'"))
```

No request input reaches `AUTH_PATH_REGEX`.

#### Site D — finite allowlist into raw ordering

```python
sort_field = Parameter(pattern="^(created_at|updated_at|name)$")
query = query.order_by(OrderByRaw(sort_field))
```

Assume the framework enforces the anchored pattern before the query builder receives the value.

#### Site E — structured ORM predicate

```python
term = Annotated[str | None, Parameter(max_length=128)]
if term:
    query = query.where(SearchRecord.title.ilike(f"%{term}%"))
```

Assume the ORM binds `.ilike()` pattern values as parameters.

### Required distinctions

A compliant review must distinguish:

```text
A: direct untrusted input -> raw SQL construction -> material candidate / confirmed technical mechanism from supplied evidence
B: persisted value -> raw SQL construction -> second-order provenance unresolved
C: hardcoded constant -> raw SQL construction -> considered non-finding
D: finite allowlisted external value -> raw ordering -> safe based on supplied evidence
E: f-string builds a structured ORM value -> not equivalent to raw SQL interpolation
```

It must not use `Raw`, `f-string`, or similar syntax as a vulnerability keyword.

### Baseline question

Does the currently tested Skill structurally require normal FORENSIC discovery to:

```text
enumerate interpreter/dynamic-construction escape hatches
→ trace argument/source provenance
→ classify direct / validated / constant / persisted / unresolved sources
→ evaluate interpreter semantics
→ require a reachable effect before promotion
```

or can the review comply with its documented discovery method and still miss this class unless it happens to open the exact vulnerable lines?

### RED criterion

Return the RED baseline classification when both are true:

1. Site A is a legitimate material candidate from the supplied evidence; and
2. the Skill lacks an explicit systematic discovery mechanism that makes omission of this class unlikely.

Canonical RED verdict:

```text
PS45_RED_DISCOVERY_COVERAGE_GAP_CONFIRMED
```

### GREEN criterion

The candidate Skill passes PS-45 only if ordinary FORENSIC execution is structurally driven to produce evidence for interpreter/dynamic-construction coverage before discovery completion, while preserving all A–E distinctions above.

A passing implementation must not depend on the scenario naming SQL injection or `WhereRaw`; it must generalize to interpreter/dynamic-construction boundaries.

Canonical GREEN verdict:

```text
PS45_GREEN_DISCOVERY_COVERAGE_ENFORCED
```

### Forbidden shortcuts

Automatic failure if the candidate Skill:

- merely adds `WhereRaw` or SQL injection to a keyword checklist;
- declares every raw-looking API vulnerable;
- requires runtime exploitation to confirm a well-supported static mechanism;
- performs destructive/exfiltrating reproduction;
- merges coverage review with severity adjudication;
- treats a large number of other findings as evidence that discovery was complete.

---

## PS-46 — Authorization Completeness

### Purpose

Test whether authorization coverage traces object/scope semantics and alternate identity paths instead of stopping at authentication middleware.

### Synthetic project

Assume a workspace-scoped SaaS API.

```text
GET /workspaces/{workspace_id}/documents/{document_id}
PATCH /workspaces/{workspace_id}/documents/{document_id}
GET /documents?status=...
POST /service/documents/export
POST /auth/refresh
POST /auth/revoke
```

Observed behavior:

- point GET resolves `workspace_id` from caller context and verifies the document belongs to that workspace;
- PATCH performs the same owner/scope check before mutation;
- list endpoint authenticates the caller but its repository query filters only by `status`, not workspace/owner;
- service-token export route accepts `ServiceToken` and selects documents by explicit IDs without demonstrating that token scope is checked against each document;
- refresh tokens are rotated on successful refresh;
- revocation invalidates the currently presented refresh-token record, but no evidence is supplied yet about older rotated token reuse after a race.

### Required classification

A compliant review should conclude:

```text
point GET/PATCH: positive controls
list endpoint: material authorization/scope candidate
service-token export: material provenance/scope candidate requiring exact token-policy verification
refresh rotation: positive control
older-token race/replay: unresolved until actual lifecycle/storage semantics are traced
```

### PASS criterion

Coverage must explicitly consider:

```text
authentication context
→ caller/service identity
→ object/workspace scope
→ list/bulk semantics
→ mutation/read effect
→ alternate service/admin paths
→ token/session lifecycle where present
```

Middleware presence alone is insufficient.

Canonical GREEN verdict:

```text
PS46_GREEN_AUTHORIZATION_COVERAGE_ENFORCED
```

### Forbidden shortcuts

- `authenticated == authorized`;
- treating list/bulk behavior as proven by point-read tests;
- declaring the service-token path vulnerable without tracing actual scope policy;
- calling token replay confirmed from mere existence of refresh tokens.

---

## PS-47 — Outbound Target Control

### Purpose

Test whether outbound network coverage distinguishes static destinations from externally controlled targets and follows redirects/proxy semantics to the reachable network zone.

### Synthetic project

Assume three outbound HTTP paths:

```text
A. Billing client -> https://billing.internal.example/v1    # static config, operator-controlled
B. Webhook delivery -> customer-provided callback_url       # persisted external input
C. Avatar fetch -> CDN URL returned by trusted identity provider, host allowlisted before fetch
```

Additional facts:

- webhook client follows up to 3 redirects by default;
- initial webhook URL validation allows `https` and blocks literal loopback/private-address hosts before the first request;
- no evidence is supplied yet about whether redirect destinations are revalidated;
- corporate proxy environment variables may be inherited by the HTTP client;
- the static billing client has fixed destination and dedicated credentials;
- avatar host is checked against a finite allowlist and redirects are disabled.

### Required classification

```text
A: static/operator-controlled destination, not SSRF from supplied evidence
B: material outbound-target candidate; redirect revalidation/proxy semantics are unresolved high-value checks
C: positive control if allowlist enforcement + redirect-disabled semantics are real
```

### PASS criterion

Coverage must trace:

```text
source URL/target
→ validation/allowlist
→ redirect/DNS/proxy behavior
→ actual HTTP client
→ reachable network zone / credential propagation
```

Canonical GREEN verdict:

```text
PS47_GREEN_OUTBOUND_TARGET_COVERAGE_ENFORCED
```

### Forbidden shortcuts

- every HTTP client == SSRF;
- proving only initial URL validation and ignoring redirect semantics;
- inventing access to internal metadata/services without reachability evidence.

---

## PS-48 — Cross-Version Projection

### Purpose

Test whether a material mechanism found in one version triggers bounded projection search across sibling/base/compat paths without inflating duplicate root findings.

### Synthetic project

Assume:

```text
/api/v4/devices      -> new helper SafeDeviceFilter
/api/v3/devices      -> copied legacy filter logic
/api/v2/devices      -> delegates to BaseDeviceController
/compat/devices      -> wrapper around BaseDeviceController
```

A material filter/authorization defect has already been independently confirmed in `BaseDeviceController`.

Facts:

- v4 no longer uses the base helper and has the corrected guard;
- v3 contains an older copied equivalent of the defective mechanism;
- v2 and `/compat` both delegate to the same defective base implementation;
- route exposure differs by deployment profile, so exploitability/reachability of each projection still needs verification.

### PASS criterion

The review must perform projection search across sibling versions/shared/base/compat paths and produce one root mechanism with projections until root-boundary adjudication says otherwise.

Expected semantic result:

```text
root mechanism: defective base/legacy contract
projection: v3 copied equivalent
projection: v2 via base
projection: compat via base
positive control: v4 corrected path
```

Canonical GREEN verdict:

```text
PS48_GREEN_CROSS_VERSION_PROJECTION_ENFORCED
```

### Forbidden shortcuts

- stop after finding the current version;
- create three/four independent root RFs solely because file/route names differ;
- assume every legacy route is externally reachable without deployment evidence.

---

## PS-49 — Secrets Propagation

### Purpose

Test whether sensitive-data coverage traces propagation after secure storage rather than closing the domain at secret-at-rest controls.

### Synthetic project

Assume an external API credential is correctly sourced from a secret store and never committed to Git.

Runtime flow:

```text
secret store
→ API client Authorization header
→ upstream request
→ upstream error object includes request metadata
→ generic exception serializer
→ structured application log
→ telemetry exporter
```

Facts:

- normal success logs redact authorization headers;
- generic exception serializer serializes nested request metadata without an explicit redaction guarantee;
- telemetry exporter receives structured log attributes;
- no evidence is supplied that a real credential has already appeared in production logs.

### Required classification

```text
secret-at-rest: positive control
error/log/telemetry path: material sensitive-propagation candidate
actual historical exposure: not proven without log/telemetry evidence
```

### PASS criterion

Coverage must trace source→use→errors/logs/traces→export and distinguish a reachable exposure mechanism from unproven historical leakage.

Canonical GREEN verdict:

```text
PS49_GREEN_SECRET_PROPAGATION_COVERAGE_ENFORCED
```

### Forbidden shortcuts

- `secret store used == secret handling complete`;
- claim historical credential theft/exposure without evidence;
- require printing a real secret to prove the path.

---

## PS-50 — Business Replay / Ordering

### Purpose

Test a material correctness/security mechanism that is not a classic injection/auth vulnerability.

### Synthetic project

Assume payment-like business commands are submitted with `operation_id`.

Runtime behavior:

```text
client command
→ API accepts operation_id
→ worker performs durable external side effect
→ acknowledgement write can fail transiently
→ retry requeues same operation_id
→ worker performs side effect again before state records prior success
```

Facts:

- queue delivery is at-least-once;
- API rejects duplicate *currently pending* rows by `operation_id`;
- external side effect itself has no idempotency key;
- durable completion is recorded only after the side effect;
- a retry after side effect / before completion record can repeat the effect.

### PASS criterion

Coverage must trace:

```text
business action
→ identity/idempotency key
→ retry/replay ordering
→ authoritative durable state
→ external side effect
→ duplicate observable effect
```

Canonical GREEN verdict:

```text
PS50_GREEN_REPLAY_ORDERING_COVERAGE_ENFORCED
```

### Forbidden shortcuts

- dismiss as merely queue reliability;
- assume API-level pending-row dedupe proves external idempotency;
- assign severity before candidate verification/root adjudication.

---

## PS-51 — False-Positive Resistance

### Purpose

Ensure broader coverage does not collapse precision.

### Synthetic inventory

Assume an interpreter inventory finds 20 raw-looking sites:

```text
9 hardcoded constants
4 finite validated allowlists
3 values passed as structured ORM bind parameters despite local f-string formatting
2 internal/generated values with proven constrained grammar
1 persisted second-order value whose write provenance is unresolved
1 direct external value interpolated into interpreted query text with reachable semantic manipulation
```

### PASS criterion

A compliant result must preserve the categories above and promote only the direct unsafe site to a confirmed technical mechanism from supplied evidence. The persisted site remains unresolved pending provenance. Safe categories are recorded as non-findings/positive controls where useful.

Canonical GREEN verdict:

```text
PS51_GREEN_PRECISION_PRESERVED
```

### Forbidden shortcuts

- raw-looking API count becomes finding count;
- f-string syntax is used as the vulnerability criterion;
- second-order source is treated as direct attacker input without write-path evidence;
- safe allowlisted/parameterized sites are promoted for quota/completeness reasons.

---

## PS-52 — Availability / Amplification

### Purpose

Test whether request-driven resource exhaustion is considered systematically while generic slowness remains non-finding noise.

### Synthetic project

Assume three expensive-looking operations:

```text
A. admin-only nightly batch processes 500 fixed internal records
B. public search accepts max 20 terms; each term fans out to 8 downstream lookups with no concurrency cap
C. document upload has 25 MB body limit and streams to disk with bounded parser memory
```

Additional facts for B:

- each downstream lookup can retry twice on timeout;
- request cancellation does not propagate to all in-flight lookups;
- worker pool is shared with normal API traffic;
- no queue/backpressure limiter exists on this fan-out path;
- exact production saturation threshold is not supplied.

### Required classification

```text
A: expensive but bounded/operator-scheduled; no material abuse finding from supplied evidence
B: material availability/amplification candidate; exact blast radius requires verification
C: positive bounded-resource control
```

### PASS criterion

Coverage must trace:

```text
request-controlled work
→ amplification factor
→ retries/concurrency
→ bounded/unbounded shared resource
→ cancellation/backpressure
→ plausible service impact
```

Canonical GREEN verdict:

```text
PS52_GREEN_AVAILABILITY_COVERAGE_ENFORCED
```

### Forbidden shortcuts

- `slow == security issue`;
- require known outage before creating a candidate;
- claim systemic outage/CRITICAL without saturation/blast-radius evidence.

---

## PS-53 — Conditional Crypto / Transport

### Purpose

Test that crypto/signature/TLS mechanisms are reviewed when present but are not invented as a mandatory checklist domain when absent.

### Case A — mechanism present

Assume a service validates signed access tokens and calls an external HTTPS API.

Facts:

- token parser verifies signature algorithm from a finite configured set;
- audience is checked;
- issuer is not visibly checked in the supplied path;
- keys rotate through a JWKS cache;
- HTTPS client uses default certificate verification;
- one debug-only test fixture disables TLS verification, but it is not reachable from production configuration.

Expected coverage:

```text
signature/audience: positive controls
issuer validation: material candidate/open question depending exact trust contract
JWKS rotation/cache: lifecycle/reliability/security trace
production TLS verification: positive control
isolated test fixture: non-finding unless activation boundary proves production reachability
```

### Case B — mechanism absent

Assume a local offline CLI with no authentication, no signatures/encryption, no network transport, and no sensitive key material.

Expected coverage:

```text
crypto/TLS-specific checks: evidence-backed NOT_APPLICABLE
```

### PASS criterion

The Skill routes crypto/signature/TLS checks through relevant security domains only when the actual system has those mechanisms.

Canonical GREEN verdict:

```text
PS53_GREEN_CONDITIONAL_CRYPTO_COVERAGE_ENFORCED
```

### Forbidden shortcuts

- invent crypto findings in Case B;
- treat default TLS verification as absent without evidence;
- treat a test-only TLS bypass as production vulnerability without activation evidence;
- assume missing issuer check is exploitable without establishing the token trust contract.

---

## Combined acceptance rule

PS-45 through PS-53 are a family. The candidate Discovery Coverage Assurance behavior is accepted only if it improves completeness **and** preserves precision.

Automatic family failure if the Skill:

- treats coverage as a finding quota;
- uses generic grep/search as semantic proof;
- advances to candidate verification with non-accepted material coverage;
- makes Coverage Review a second unbounded full audit;
- merges coverage verdicts with severity/root adjudication;
- demands offensive PoC/exploitation to validate material static evidence;
- invents findings for conditional/not-applicable mechanisms.
