# Discovery Coverage Assurance

Этот файл является **авторитетным источником** для доказательства полноты thematic discovery: Discovery Coverage Matrix, applicability/status semantics, proof-of-coverage, Independent Coverage Review, targeted coverage correction и coverage revalidation.

Он отвечает на вопрос:

> Какие material mechanism classes система действительно имеет, и есть ли evidence, что каждый применимый класс был исследован до завершения discovery?

Он **не** заменяет `independent-verification.md`, `root-boundary-adjudication.md` или `evidence-and-severity.md`.

## 1. Core invariant

Количество и критичность найденных замечаний не являются доказательством полноты аудита.

Полнота discovery доказывается:

```text
accepted As-Built
→ mechanism coverage
→ evidence trail
→ independent coverage challenge
```

Ноль findings допустим, если применимые domains реально исследованы и coverage evidence достаточен.

Много findings не позволяет закрыть нерассмотренный material domain.

## 2. Discovery Coverage Matrix

Оба режима — `STANDARD_FULL` и `FORENSIC` — ведут Discovery Coverage Matrix.

Минимальная строка:

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

Закрытый набор:

```text
YES
NO
CONDITIONAL
```

`YES` — механизм явно присутствует и требует coverage evidence.

`NO` — механизм архитектурно отсутствует на принятом baseline.

`CONDITIONAL` — необходимость глубины зависит от фактически обнаруженной capability/implementation shape.

`NO` не означает автоматически `NOT_APPLICABLE`: требуется evidence-based reason, связанный с accepted As-Built и/или targeted inventory.

### 2.2 Coverage status

Закрытый набор:

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

`NOT_APPLICABLE` допустим только с конкретным evidence-based объяснением.

Нельзя использовать формулировки вида:

```text
Security: COVERED — security reviewed
Controllers: COVERED — grep completed
```

как достаточное доказательство.

## 3. Что считается coverage evidence

Coverage evidence может включать:

- inspected paths и concrete call/data/control chains;
- targeted inventory/search results, привязанные к baseline;
- representative semantic traces высокорисковых sites;
- positive controls;
- considered-but-not-promoted conclusions/non-findings;
- open questions для unresolved provenance/intent;
- evidence-based proof отсутствия mechanism class.

Search/grep — **inventory mechanism**, а не semantic proof.

`COVERED` требует интерпретации, достаточной чтобы различать, где применимо:

```text
safe
unsafe candidate
ambiguous / unresolved
not applicable
```

Не требуй полного построчного reread всего repository, если bounded inventory + representative/high-risk semantic traces дают достаточную confidence о классе.

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

Taxonomy mechanism-oriented и framework-neutral. Она не является vulnerability quota.

## 5. Общие proof-of-coverage правила

Для каждого применимого domain coverage closeout должен отвечать минимум на четыре вопроса:

1. **Что было инвентаризировано?**
2. **Какие representative/high-risk traces реально прослежены?**
3. **Как классифицированы material sites/mechanisms?**
4. **Что осталось unresolved/blocked?**

Если ответов нет, `COVERED` не обоснован.

Для high-risk domains ниже generic thematic paragraph недостаточен.

## 6. High-risk proof-of-coverage contracts

Усиленный proof обязателен для:

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

Где применимо, проверь representative:

- point-read;
- list/bulk read;
- write/mutation;
- admin/service-token path;
- versioned/compatibility path;
- asynchronous/cross-service identity propagation.

Наличие auth middleware или успешного login-path не закрывает domain само по себе.

Если существуют session/token mechanisms, рассмотрение включает lifecycle semantics:

- issuance;
- refresh/rotation;
- revocation;
- expiry;
- replay resistance;
- stale sessions;
- session fixation;
- issuer/audience/signature verification;
- service/admin fallback credentials;
- identity propagation across async/service boundaries.

Object-level/scope authorization и session/token lifecycle — разные dimensions внутри одного domain; наличие одного не доказывает другое.

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

Relevant mechanisms, если присутствуют:

- raw SQL / ORM escape hatches;
- shell/CLI command construction;
- template/eval/expression engines;
- regex from external/persisted input;
- query/search DSL;
- other interpreter-facing dynamic text.

Для arguments/sources различай минимум:

```text
direct untrusted
validated / allowlisted
hardcoded constant
persisted / second-order
unresolved provenance
```

Raw API name, f-string, string concatenation или dynamic expression сами по себе не finding.

Пример semantic distinction:

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
- temp files;
- archive extraction;
- object-store keys;
- overwrite/collision;
- user-controlled filenames;
- cleanup ownership.

API/type names such as `Path` не считаются защитой сами по себе; доказывай actual normalization/root/authorization semantics.

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

- user/config-controlled scheme/host/port;
- webhooks/callbacks;
- redirects;
- proxy/environment interaction;
- credential forwarding;
- internal/metadata-like destinations;
- destination validation before and after redirects where relevant.

Не называй SSRF только потому, что существует HTTP client. Нужен control over destination + reachable effect.

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
- YAML/XML/document/image/archive parsers;
- multipart/upload pipelines;
- active content;
- parser recursion/size limits;
- archive/decompression expansion.

Если система не принимает material complex content и targeted inventory это подтверждает, `NOT_APPLICABLE` допустим с evidence.

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

Review не ограничивается местом хранения секрета.

Consider:

- access/refresh/API tokens;
- credentials/passwords;
- DSN/service credentials;
- sensitive business/user data;
- exception bodies;
- structured logs/tracing attributes;
- query strings/URLs;
- subprocess argv/env inheritance;
- debug dumps/caches;
- telemetry/exporters.

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

- elevation/sudo-like flows;
- service accounts;
- Docker/container/host-control sockets;
- host mounts/devices;
- native APIs;
- browser preload/native bridges;
- privileged admin/local endpoints;
- dynamic plugin/module capabilities.

Ключевой вопрос: кто реально может активировать capability и с каким scope/lifetime?

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
- decompression/parser expansion;
- pathological regex/expression cost;
- expensive fan-out;
- queue/cache growth;
- retry storms;
- worker starvation;
- blocking/exhausted resource pools;
- request-driven amplification.

Generic slowness/performance suspicion не является material security/reliability finding без reachable effect.

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
- stale/out-of-order completion;
- duplicate durable side effect;
- cancellation races;
- retry changing business semantics;
- quota/accounting/state-transition bypass.

Это material correctness/security domain даже когда классической injection/auth vulnerability нет.

### 6.10 COMP-01 — Cross-version / legacy / compatibility surfaces

Когда material candidate найден в versioned/shared path, выполняй projection search по применимым:

```text
sibling API versions
shared/base implementations
helpers
compatibility routes
legacy/fallback paths
copied equivalent blocks
```

Не создавай автоматически отдельный root finding для каждого совпадения. Root/projection identity определяется downstream `root-boundary-adjudication.md`.

## 7. Conditional mechanisms

### 7.1 Cryptography / signatures / TLS

Cryptography, signature/token verification и TLS-specific mechanisms не являются обязательным отдельным domain.

Когда они реально присутствуют, проверяй их внутри relevant `SEC-*` domain:

- issuer/audience/signature verification;
- randomness/nonces/IVs;
- certificate/TLS verification;
- key handling;
- home-grown cryptographic constructions.

Не придумывай crypto findings в проекте без соответствующего mechanism.

### 7.2 Supply chain / dynamic loading / update path

`OPS-02` имеет applicability-driven depth.

Material applicability возникает, например, при наличии:

- plugin/module loading;
- runtime extensions;
- installers/hooks;
- update mechanisms;
- executable/module search paths;
- dynamic imports from externally influenced locations.

Если этих mechanisms нет, evidence-backed `NOT_APPLICABLE` допустим.

## 8. STANDARD_FULL и FORENSIC

### STANDARD_FULL

- одна compact Discovery Coverage Matrix обязательна;
- один thematic artifact может закрывать несколько domains, если evidence действительно достаточен;
- high-risk domains сохраняют concrete proof-of-coverage;
- coverage closeout обязателен до candidate verification.

### FORENSIC

- та же matrix обязательна;
- применимые high-risk domains имеют explicit evidence trail;
- material domains получают отдельные thematic sections/artifacts по необходимости;
- Independent Coverage Review является отдельным явным gate до candidate verification.

Не создавай механически отдельный Markdown-файл на каждый domain.

## 9. Discovery closeout

Перед Independent Coverage Review coordinator сверяет каждую строку matrix.

Для каждого domain допускается только честное текущее состояние:

```text
COVERED
PARTIALLY_COVERED
BLOCKED
NOT_APPLICABLE
```

Если row остаётся `PARTIALLY_COVERED`, выполни targeted discovery до review или передай gap reviewer-у явно.

Если material row `BLOCKED`, обычный downstream acceptance запрещён.

`DISCOVERY_COMPLETE` означает, что planned thematic passes завершены как artifacts. Он **не означает**, что discovery coverage принято.

Candidate verification может начаться только при:

```text
DISCOVERY_COMPLETE
AND
COVERAGE_ACCEPTED
```

## 10. Independent Coverage Review

### 10.1 Purpose

Coverage Reviewer не проверяет заново правильность каждого существующего `CAND-*`.

Главный вопрос:

> Существует ли material mechanism/class, видимый из accepted As-Built или bounded probe, но не имеющий достаточного discovery coverage evidence?

Это проверка **absence of investigation**, а не candidate correctness.

### 10.2 Fresh-context packet

По умолчанию reviewer получает bounded factual packet:

- accepted technical As-Built;
- Discovery Coverage Matrix;
- thematic artifact registry;
- candidate registry;
- positive controls;
- open questions;
- baseline/revision binding.

Не передавай predecessor chain-of-thought/reasoning history как authority.

Если packet недостаточен для конкретного coverage challenge, reviewer может расширить context только по concrete recorded trigger.

### 10.3 Pass 1 — As-Built reconciliation

Сопоставь actual capabilities с matrix:

- runtimes/processes;
- APIs/IPC/events;
- interpreters/dynamic construction;
- stores/files/resources;
- external network dependencies;
- privileged capabilities;
- background/lifecycle mechanisms;
- versioned/legacy surfaces;
- content/parser surfaces;
- sensitive-data flows.

Если capability существует, а corresponding domain отсутствует/необоснованно `NOT_APPLICABLE`, это coverage gap.

### 10.4 Pass 2 — Evidence-quality challenge

Особенно challenge `COVERED`, когда row имеет:

```text
inventory: none
semantic traces: none
candidates: none
positive controls: none
non-findings: none
open questions: none
evidence_refs: generic thematic file only
```

Ноль findings допустим. Ноль evidence исследования — нет.

### 10.5 Pass 3 — Bounded blind-spot probes

Выбери несколько risk-driven probes, основанных на accepted As-Built и matrix claims.

Примеры:

- raw/interpreter escape-hatch inventory;
- dynamic outbound target sites;
- representative list/read/write auth paths;
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

Coverage Reviewer не превращается во второй полный auditor.

## 11. Coverage review verdicts

Закрытый набор:

```text
COVERAGE_ACCEPTED
COVERAGE_CORRECTION_REQUIRED
COVERAGE_BLOCKED
COVERAGE_AUTHORITY_DRIFT
```

### COVERAGE_ACCEPTED

Matrix claims достаточно подтверждены; material gaps не найдены.

### COVERAGE_CORRECTION_REQUIRED

Один или несколько domains недоисследованы или `COVERED` не подтверждён evidence.

### COVERAGE_BLOCKED

Material domain невозможно достаточно проверить из-за отсутствующего source/access/tool/runtime evidence. Blocker должен быть конкретным.

### COVERAGE_AUTHORITY_DRIFT

Accepted As-Built/baseline изменился или contradicted так, что matrix больше не связана с текущей authority.

Coverage Review:

- не назначает severity;
- не создаёт final `RF-*` напрямую;
- не self-corrects owning thematic artifacts;
- не принимает disputed As-Built как факт без authority reconciliation.

## 12. Coverage correction

При gap:

```text
COVERAGE_CORRECTION_REQUIRED
→ targeted thematic pass
→ matrix update
→ new/updated CAND / PC / OQ / non-findings
→ impacted-domain coverage re-review
→ COVERAGE_ACCEPTED | COVERAGE_BLOCKED
```

Не перезапускай весь audit автоматически.

Correction scope должен фиксировать:

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

Discovery coverage связано с accepted As-Built revision и repository baseline.

Если technical As-Built меняется после accepted coverage:

```text
As-Built correction
→ coverage impact scan
→ only affected domains become REVALIDATION_REQUIRED
```

Пример:

```text
new Webhook Dispatcher discovered
→ ARCH-04 Boundary Contracts
→ SEC-04 Outbound Network
→ SEC-06 Sensitive Data
```

Не сбрасывай unrelated accepted rows без evidence impact.

Compact coverage projection в `working/INDEX.md` usable downstream только при корректном freshness/revision binding по `revalidation-and-freshness.md`.

## 14. Safe Reproduction / Evidence Validation interaction

Coverage evidence и candidate verification могут использовать safe runtime reproduction по контракту `evidence-and-severity.md`, но reproduction:

- не является обязательным для каждой row/finding;
- не заменяет source/provenance/semantic tracing;
- не позволяет превращать coverage probe в exploitation exercise;
- не повышает severity автоматически.

Если runtime validation недоступна или небезопасна, фиксируй limitation и используй фактическую силу static evidence.

## 15. Anti-noise / precision rules

Discovery Coverage Assurance не разрешает:

- finding quota по domain;
- `Raw`/`eval`/HTTP client/path API как vulnerability keywords;
- auto-promotion всех inventory hits;
- severity во время coverage closeout;
- giant repo reread для формального checkbox completion;
- generic grep как достаточный proof;
- invented findings для `NOT_APPLICABLE` domains;
- false certainty для persisted/second-order sources без provenance.

Главный precision invariant:

```text
coverage completeness != finding inflation
```

## 16. Completion contract

Нельзя использовать обычный accepted downstream flow, если material coverage имеет любой из статусов/вердиктов:

```text
PARTIALLY_COVERED
BLOCKED
COVERAGE_CORRECTION_REQUIRED
COVERAGE_BLOCKED
COVERAGE_AUTHORITY_DRIFT
REVALIDATION_REQUIRED
```

Для перехода к candidate verification требуется:

```text
DISCOVERY_COMPLETE
AND
COVERAGE_ACCEPTED
```

Финальный `REVIEW_COMPLETE` невозможен, если coverage gate не принят или material coverage limitation скрыта.
