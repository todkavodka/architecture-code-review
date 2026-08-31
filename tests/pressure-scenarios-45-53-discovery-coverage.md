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

A harmless synthetic reasoning check demonstrates that a quote-breaking boolean predicate can alter the WHERE expression. The test is about construction semantics and reachable filter manipulation, not data extraction, stacked statements, writes, or RCE.

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

## PS-46 through PS-53

Reserved by the approved Discovery Coverage Assurance design for authorization completeness, outbound target control, cross-version projection, secrets propagation, business replay/order, false-positive resistance, availability/amplification, and conditional crypto/transport coverage. Their full scenario contracts are added before the corresponding behavior is implemented.
