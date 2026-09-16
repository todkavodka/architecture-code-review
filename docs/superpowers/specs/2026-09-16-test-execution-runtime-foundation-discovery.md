# Discovery — Test Execution Runtime Foundation

Дата: 2026-09-16
Базовая ревизия: `main@8e62de7e939cbf715561b95a58032389f917f927`
Статус документа: Discovery, не design и не implementation plan

## Executive summary

Текущая система остаётся Markdown Skill/reference system. В репозитории нет
исполнителя тестов, subprocess-адаптера, очереди выполнения или механизма
приёма runtime-результатов. Это подтверждается инвентаризацией дерева: кроме
контрактных Markdown-файлов и небольших fixtures, production runtime-кода нет.

При этом принятые контракты уже оставляют точный и безопасный шов для будущего
исполнения:

```text
accepted Test Engineering semantics
    ↓  what must be proven
separate execution authorization
    ↓  what may be run
immutable exact execution binding
    ↓  source + environment + bounded command/input
one execution attempt
    ↓
immutable runtime observation/evidence
    ↓
existing Test Engineering adjudication
```

Следующий безопасный архитектурный рубеж целесообразно назвать
`Test Execution Runtime Foundation`. Он должен быть узким execution substrate,
а не новой capability, новым `Session Intent`, Test Engineering authority,
Product authority или projection mechanism.

Минимальная безопасная граница требует отдельного разрешения выполнения,
замороженной `argv`-спецификации без shell по умолчанию, точной source/tree и
environment binding, bounded timeout, изолированного рабочего каталога,
отсутствия секретов и сетевого доступа в первой конфигурации, а также
неизменяемой записи каждой попытки и её наблюдений. Для произвольного
непроверенного кода локальный host не является достаточной изоляцией; поэтому
в design следует отдельно решить, ограничивается ли первая реализация
доверенными локальными профилями или сразу использует контейнерную границу.

Рекомендация Discovery: перейти к design с названием
`Test Execution Runtime Foundation`, сохранив первым срезом выполнение уже
существующего исполняемого теста или verification command в явно разрешённом
сценарии. Provisioning, генерация тестов, Service Simulator, Product-wide E2E,
распределённые workers и arbitrary shell остаются за пределами этого среза.

## Current-state inventory

### Что уже определено

| Область | Состояние | Evidence |
|---|---|---|
| Test semantic authority | `DEFINED` | Test Review владеет Test Assurance; `BC-*` принадлежит Behavior Model, `MAT-*`/`TM-*`/`GAP-*` — Test Assurance. См. `capabilities/test-review/SKILL.md`, разделы «Current capability boundary», «Stage B projection boundary», и `capabilities/test-review/references/test-engineering-contract.md`, «Ownership». |
| Что должно быть доказано | `DEFINED` | `BC-*` — independently verifiable behavior, `MAT-*` — material assurance target, `TM-*` — mapping к executable evidence; `test-engineering-contract.md`, «Behavior Contract Model». |
| Test case vs execution vs result | `DEFINED` | `accepted_test_case != executed_test != tested_result`; `expected_result != observed_result`; `test-engineering-contract.md`, «API input boundary case semantics». |
| `TESTED` qualification | `DEFINED` | Требуются accepted actual execution/observation evidence, execution/result record, exact environment and baseline, execution time, status/result и provenance; там же. |
| Existing observed evidence | `DEFINED` | `EV-*` имеет source locator, exact baseline/project/Product binding, `observed_view`, limitation и sensitivity; `references/shared-evidence-model.md`, «Fine-grained observation shape». |
| Source/revision and baseline binding | `DEFINED` | Source bindings должны быть revision-bound и содержать concrete values; `test-engineering-contract.md`, «Reuse / Extend / Revalidate»; Change Review использует отдельные immutable base/candidate bindings в `references/review-modes-and-orchestration.md`. |
| Dirty-state distinction | `DEFINED` | По умолчанию exact committed `HEAD`; для dirty worktree определяются base commit, changed paths/content fingerprints и explicit admission; `references/session-orchestration.md`, «Dirty working tree and baseline». |
| Product qualification | `DEFINED` | Product Test Engineering использует `TRS-*`, immutable Product baseline и exact Project/source bindings; membership не даёт test/code/environment permissions; `capabilities/test-review/SKILL.md`, «Product Test Engineering scope». |
| Change Review boundary | `DEFINED` | `CHANGE_REVIEW_CANDIDATE` read-only к accepted authority; candidate output не создаёт `TESTED`; `references/review-modes-and-orchestration.md`, «Change Review candidate execution mode», и `test-engineering-contract.md`, «Change Review candidate test impact». |
| Projection boundary | `DEFINED` | `PRJ-*` — derived projection; report не принимает, не исправляет и не разрешает semantic records; `SKILL.md`, Stage B boundary, и `references/report-contract.md`. |
| Finding/assurance separation | `DEFINED` | Finding lifecycle/progress не меняется execution output напрямую; current/historical/freshness и owner adjudication остаются отдельными; `docs/reference/outputs.md`, «Finding lifecycle and progress reporting». |
| Evidence immutability/provenance principle | `DEFINED` | Evidence сохраняет provenance, limitation и baseline; старые observations не переписываются и не обогащаются предположением; `references/shared-evidence-model.md`, «Safe evidence excerpts» и «Historical and Product compatibility». |

### Что определено только частично

| Область | Состояние | Точная граница |
|---|---|---|
| Test intent | `PARTIALLY_DEFINED` | `Session Intent` (`USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, `CHANGE_REVIEW`, `PROJECTION_REPAIR`) маршрутизирует работу, а `BC/MAT/TM` описывают assurance intent. Отдельного accepted «run this test» intent нет. См. `references/session-orchestration.md`, «Session Intent», и `test-engineering-contract.md`, «Behavior Contract Model». |
| Test task identity | `PARTIALLY_DEFINED` | `TASK-*` — Test Engineering remediation work, но не executable test, не result и не permission; completion `TASK-*` не resolves `GAP-*`. См. `docs/reference/identifiers-and-statuses.md` и `docs/reference/artifacts.md`. |
| Implementation state | `PARTIALLY_DEFINED` | Есть состояния/планы для Test Plan, simulator spec и simulator implementation plan, но нет identity или lifecycle реализованного test package. См. `capabilities/test-review/SKILL.md`, «Selectable outputs», и `test-engineering-contract.md`, «Service Simulator Design». |
| Execution authorization | `PARTIALLY_DEFINED` | Контракт говорит, что test execution, simulators, environments, code changes и publication требуют отдельной explicit authorization; владельца, записи, scope и expiry такой authorization нет. См. `capabilities/test-review/SKILL.md`, «Product Test Engineering scope», и `test-engineering-contract.md`, «Product and report consumption». |
| Environment identity | `PARTIALLY_DEFINED` | `TESTED` требует exact environment, а Test Environment Design описывает стратегии зависимостей (`REAL_DISPOSABLE`, `SERVICE_EMULATOR`, …), но fingerprint, toolchain, dependencies, fixtures и external endpoints для execution record не определены. См. `test-engineering-contract.md`, «Test Environment Design». |
| Runtime evidence | `PARTIALLY_DEFINED` | `EV-*` допускает `RUNTIME_OBSERVATION` и accepted runtime observation reference, а `TESTED` требует execution/result record; отдельного immutable runtime record и ingestion boundary нет. См. `references/shared-evidence-model.md`, «Operation-level ... evidence», и `test-engineering-contract.md`, строки про `TESTED`. |
| Runtime freshness/reuse | `PARTIALLY_DEFINED` | Общая freshness привязана к source, dependencies, configuration и evidence, но exact reuse key для executed test не задан. См. `references/revalidation-and-freshness.md`, «Context Orchestration» и Test Engineering `REVALIDATE` в `test-engineering-contract.md`. |

### Что пока не определено

Следующие элементы имеют состояние `NOT_DEFINED` в принятом контракте:

```text
execution command / argv schema
working-directory and filesystem policy for a run
environment fingerprint and executor identity/version
runtime input binding and input redaction
secret capability model and log redaction at execution boundary
network policy for execution
timeout default/maximum and override authority
cancellation and process-group cleanup contract
CPU/memory/disk/process limits
ExecutionAttempt identity and attempt lifecycle
raw stdout/stderr/artifact storage references
normalized runtime evidence schema
failure taxonomy for executor/environment/source failures
retry and reuse semantics for actual execution
authorization-to-execution TOCTOU verification
```

Это не пробелы текущего Test Engineering semantic contract: это intentionally
unimplemented execution substrate. Discovery не превращает их в `GAP-*` или
новые Test Engineering findings.

### Что явно вне текущей границы

`capabilities/test-review/SKILL.md` прямо указывает, что capability не
реализует product tests, Service Simulator или test infrastructure; API cases
не выполняются, а runtime execution, fuzzing, DAST, payload submission и
environment provisioning имеют состояние `UNAVAILABLE`. Service Simulator
implementation требует separately accepted/fresh specification и explicit
authorization. Product membership не даёт execution permissions. Это текущие
`OUT_OF_SCOPE`, а не разрешение на неявное расширение.

## Problem statement

Нужно получить воспроизводимый runtime evidence для уже принятого
`WHAT MUST BE PROVEN`, сохранив следующую цепочку:

```text
BC/MAT/TM/GAP semantic authority
    → explicit execution authorization
    → exact bounded execution specification
    → one attempt
    → raw observation
    → normalized evidence
    → Test Engineering owner adjudication
```

Сегодня между `TM-*` и accepted `TESTED`/runtime observation находится только
контрактное требование. Если добавить прямой `run` к существующему CLI/MCP или
позволить отчёту запускать строку команды, возникнут неразрешённые вопросы:
кто разрешил запуск, какой source фактически выполнялся, в какой среде, что
произошло при timeout, можно ли повторно использовать результат и кто имеет
право превратить exit code в assurance conclusion.

Минимальный substrate должен отвечать на эти вопросы, но не отвечать за то,
соответствует ли система принятому поведению. Последнее остаётся за
Test Engineering owner и существующими `BC-*`, `MAT-*`, `TM-*`, `GAP-*` и
`CC-*` контрактами.

## Non-goals

В Discovery не предлагаются как часть первого runtime slice:

- полный CI/CD, scheduler, distributed worker fleet или database-backed queue;
- Kubernetes, remote agent fleet или generic workflow engine;
- arbitrary shell, command strings, pipes, redirects и command substitution;
- automatic package installation, dependency resolution или environment mutation;
- provisioning инфраструктуры, database schema migration или service startup;
- генерация test code, Service Simulator implementation или test implementation;
- Product-wide E2E orchestration и cross-Project distributed execution;
- secret manager, dashboard, web UI или новая пользовательская capability;
- автоматические retries, автоматическое закрытие `GAP-*`, `MAT-*` или finding;
- принятие semantic verdict по `exit_code == 0` без explicit owner contract;
- изменение accepted baseline, Product baseline, findings или projections;
- shell/tool invocation из Markdown, LLM текста, MCP call или report prose.

## Existing authority boundaries

### Test Engineering authority

Behavior Model принимает и замещает `BC-*`; Contract Verification владеет
`CC-*`; Test Assurance владеет `MAT-*`, `TM-*` и `GAP-*`. `TASK-*` описывает
работу, но её completion не закрывает gap автоматически. Эти записи — semantic
authority, а Test Review Summary/Map и прочие numbered outputs — projections.

Runtime layer может создать observation/evidence reference и сообщить
технический результат запуска. Он не может принять `BC-*`, изменить `MAT-*`,
переклассифицировать `GAP-*`, закрыть `CC-*` или опубликовать `TESTED` без
существующей owner adjudication.

### Orchestration authority

`Session Intent` определяет routing, а не permission to execute. `CHANGE_REVIEW`
является candidate/read-only mode; candidate runtime evidence должен быть связан
с candidate source и не может мутировать accepted baseline. Product
Coordination Plan может авторизовать dispatch, но child source-access,
capability, test и owner gates остаются отдельными. Поэтому orchestration
authorization может быть контекстом, но не должна подменять execution-specific
authorization.

### Evidence and projection authority

`EV-*` фиксирует наблюдение и provenance, но evidence record сам не решает его
acceptance. `PRJ-*` и Markdown reports могут отобразить accepted runtime
evidence, но не становятся источником истины. Runtime logs нельзя направлять
сразу в projection с последующим выводом о compliance.

## Gap matrix

| Вопрос | Сейчас | Минимальная будущая граница | Почему это не должно быть скрыто в существующем owner record |
|---|---|---|---|
| Кто разрешил запуск? | Отдельная authorization только упомянута | Явный authorization record с субъектом, scope, expiry и exact input references | `TASK-*` описывает работу, но не permission; Product/Session routing не достаточно granular. |
| Что разрешено запустить? | Нет command contract | `ExecutionSpec` из approved profile или explicitly approved exact argv | LLM/report text не является trusted command source. |
| Какой source? | Source/baseline binding задан для semantic evidence | Exact commit плюс tree fingerprint и workspace verification | Commit SHA не описывает dirty/untracked/generated content. |
| Где запустить? | Environment design — planning strategy | Exact environment binding и execution location policy | Environment design projection не является runtime identity. |
| Что произошло? | `EV-*` допускает runtime observation, но record отсутствует | Immutable attempt + raw observation | Нельзя переписывать старый результат или смешивать retries. |
| Что означает результат? | Existing owner semantics требуют adjudication | Normalized evidence input, не verdict | `exit_code` не универсально равен assurance PASS. |
| Когда повторить/переиспользовать? | Общая freshness, no exact run key | Conservative exact-match/revalidation decision | Отсутствие наблюдаемого изменения не доказано автоматически. |
| Как прекратить запуск? | Нет execution cancellation contract | Timeout/cancel/process-group boundary и recorded termination reason | Generic `FAILED` теряет важную provenance. |

## Layer separation evaluation

Предлагаемое разделение не означает, что каждый объект обязан сразу стать
отдельной таблицей или сервисом. Оно означает, что разные authority и
жизненные циклы не могут быть представлены одной mutable строкой.

| Layer | Нужна отдельная семантическая граница? | Discovery conclusion |
|---|---|---|
| Test semantic authority | Да, уже существует | Reuse `BC/MAT/TM/GAP/CC`; не добавлять execution fields как их permission или process state. |
| Execution Authorization | Да | Отдельная first-class запись нужна для auditability, expiry, scope и TOCTOU input binding. |
| Execution Specification | Да | Замороженная нормализованная спецификация нужна, чтобы approved command/profile нельзя было ретarget после approval. |
| Execution Attempt | Да | Каждое фактическое invocation должно иметь собственную identity; retry не переписывает прошлую попытку. |
| Raw observation | Да как immutable payload/reference, не обязательно отдельный semantic family | Сохранять exit/termination/stdout/stderr/artifact hashes и executor metadata с redaction. |
| Normalized Runtime Evidence | Да как derived evidence record | Нормализация отделяет transport/storage details от Test Engineering interpretation, но не создаёт новый verdict authority. |
| Bounded Executor | Нет как semantic record | Это trusted mechanism/adapter, который принимает только authorized immutable spec и создаёт attempt/observation. |

Итого: минимальное design-предложение — `ExecutionAuthorization`,
`ExecutionSpec`, `ExecutionAttempt` и `RuntimeEvidence`; `ExecutionProfile`
может быть конфигурацией command owner, а не новой authority, если его всегда
раскрывают в immutable `ExecutionSpec`. Raw observation можно хранить как часть
attempt с content-addressed references, если его immutability и provenance
явно сохранены. `BoundedExecutor` остаётся механизмом, а не записью.

## Authority analysis

### Option A — accepted Test Engineering `TASK-*`

`TASK-*` хорошо связывает execution с remediation work и сохраняет связь
`GAP → TASK`. Но текущий контракт специально говорит, что `TASK-*` не равен
`GAP-*`, а completion не resolves gap. Использование TASK как permission
создало бы authority escalation: task author или assignee получил бы право
запустить произвольный код, хотя текущая запись описывает только требуемую
работу.

- Security: слабее; task scope не обязательно содержит command, source,
  environment, secrets и expiry.
- Auditability: traceability хорошая, permission audit неполный.
- Compatibility: сохраняет существующую identity, но меняет её смысл.
- YAGNI: удобно как linkage, опасно как authorization.
- Вывод: использовать как optional reason/reference, но не как permission.

### Option B — отдельная explicit human/agent Execution Authorization

Явная authorization лучше всего фиксирует principal, purpose, allowed scope,
source/environment/spec fingerprint, resource policy, expiry и decision. Она
может ссылаться на `TASK-*`, `TM-*`, `BC-*` или Change Review, не поглощая их.

- Security: сильная least-privilege boundary и понятный audit trail.
- Auditability: лучший вариант для подтверждения «кто и что разрешил».
- Compatibility: additive; не меняет владельцев Test Engineering records.
- YAGNI: это минимально необходимая новая boundary, если выполнение вообще
  должно быть безопасным.
- Риск: design должен определить trusted approver и не превратить любой agent
  message в approval.

### Option C — orchestration-owned authorization tied to Session Intent

Session/coordination already owns routing, Product plan and dispatch context.
Это даёт естественный correlation ID, но Session Intent не является test
permission и может быть broad (`NEW`, `REVALIDATE`, `CHANGE_REVIEW`). Если
orchestration запись сама разрешает command, routing начинает владеть
capability-specific execution policy.

- Security: средняя; риск broad permission и confused deputy.
- Auditability: хорошо виден context, но не обязательно exact command approval.
- Compatibility: максимально переиспользует orchestration, но может нарушить
  разделение `requested_work != resolved_work`.
- YAGNI: отдельный record всё равно потребуется для exact execution binding.
- Вывод: использовать как parent/context и dispatch gate, не как единственную
  authorization.

### Authority conclusion

Evidence поддерживает Option B как execution permission boundary с Option C как
контекстом и Option A как traceability reference. Design должен разрешить
точную форму trusted approval, но не может считать `TASK-*`, Product membership,
report prose, LLM output или MCP call достаточным разрешением.

## Command authorization alternatives

### Model 1 — exact command snapshot

Frozen structured `argv`, working directory, environment allowlist, source and
resource policy. Это наиболее прозрачная модель для первой границы: parser не
нужен, shell metacharacters не интерпретируются, а execution fingerprint можно
проверить перед запуском. Недостаток — повторение команд и более трудная
переиспользуемость.

### Model 2 — repository-owned named execution profile

`test_profile_id` разрешается trusted server/tool configuration, содержащей
command template and policy. Это удобнее для повторения и позволяет владельцу
репозитория контролировать supported tests, но profile revision должен быть
заморожен и раскрыт в exact spec. Mutable config, branch-local profile или
filename alone не должны ретarget approved execution.

### Model 3 — generated command requiring explicit approval

Кандидатная команда может быть предложена агентом или LLM, но до выполнения
нужны human/approved service decision, exact snapshot and policy validation.
Это полезно позднее для developer ergonomics, но сложнее по approval UX и
прямее подвержено prompt injection.

### Сравнение и вывод

Для first slice нужен Model 1 либо Model 2, материализованный как Model 1 до
запуска. Model 3 не должен быть default. Во всех моделях запрещены `shell=True`,
arbitrary command strings, command substitution, pipes и redirects. Если
shell syntax когда-либо понадобится, это отдельная design boundary с более
сильным approval и sandboxing, а не скрытый fallback.

## Shell boundary

Первая версия должна принимать только structured `argv: [executable, arg, ...]`
и запускать process без shell. Нельзя интерпретировать строку, собранную из
параметров, нельзя позволять `$(...)`, backticks, `;`, `&&`, `|`, redirects или
shell startup files. Executable path/profile resolution должен быть
allowlisted и fingerprinted before run.

Shell может быть исследован позже только если конкретный accepted test contract
требует shell semantics и есть отдельная authorization/sandbox boundary.
Наличие shell-команды в README, Test Plan или LLM-generated text не является
таким доказательством.

## Source and workspace binding

### Required source relation

Каждая `ExecutionSpec` должна ссылаться на exact qualified source binding и
проверять его непосредственно перед запуском. Минимально это:

```text
repository/project/product qualification
resolved source identity
commit or immutable source revision
whole-tree or relevant-tree fingerprint
dirty/untracked/generated-content admission decision
test implementation fingerprint
```

Accepted baseline, Change Review candidate и runtime workspace — разные роли:

```text
accepted baseline B  !=  candidate source C  !=  runtime workspace W
```

Для single repository clean revision можно использовать commit плюс verified
tree fingerprint. Для dirty worktree нужно сохранять base commit, changed paths
и content fingerprints; execution нельзя приписывать clean commit. Untracked
generated files и temporary test implementation либо входят в explicit tree
binding, либо выполнение считается не квалифицированным для accepted evidence.

Для multi-repository Project first slice должен принимать одну exact qualified
repository/source binding на попытку. Project-spanning execution требует
нескольких explicitly qualified bindings и composite fingerprint; Product E2E
остаётся extension seam. Для Change Review execution source — candidate C,
результат остаётся candidate evidence и не меняет accepted B.

### TOCTOU requirement

Approval-time snapshot недостаточен. Перед dispatch executor обязан повторно
разрешить и сравнить source/tree fingerprint, profile/spec revision и workspace
root с frozen values. При mismatch запуск блокируется как `SOURCE_MISMATCH` или
`SPEC_MISMATCH`; нельзя продолжать «примерно тот же» запуск.

### Workspace policy

Безопасный first-slice default:

```text
read: exact source snapshot only
write: isolated temporary workspace and explicit artifact directory
canonical repository mutation: forbidden
untracked/generated files: explicit admission only
symlink/path traversal outside workspace: rejected
cleanup: bounded and recorded; evidence refs remain immutable
```

A local executor может использовать checkout/snapshot в temporary workspace, но
не должен запускать из произвольного caller-provided path. Container executor
добавляет stronger filesystem boundary; его необходимость — design decision,
не скрытая реализация в Discovery.

## Environment identity analysis

Полный CI environment fingerprint был бы избыточен для первого среза. Но
«host OS + command» недостаточно для воспроизводимости. Минимальная identity
должна включать:

```text
executor identity and version
execution location/isolation mode
OS/architecture or container image digest
runtime/toolchain versions used by the command
dependency lockfile/content fingerprint
non-secret environment allowlist and values/fingerprints
declared service/fixture dependency identities
network policy
resource/timeout policy
```

Секретные values никогда не входят в fingerprint или Runtime Evidence. Если
внешний endpoint/fixture/database materially влияет на result, он должен быть
named and qualified; отсутствие exact input — `UNKNOWN`/limitation, а не
assumption of unchanged environment.

### Provisioning boundary

`EXECUTE_IN_EXISTING_ENVIRONMENT` должен быть первым explicit mode. Он означает,
что environment уже существует и входит в binding; executor не устанавливает
пакеты, не поднимает произвольные сервисы и не изменяет host configuration.

`PROVISION_ENVIRONMENT` — отдельный later milestone. Provisioning имеет свою
authority, rollback, secrets, network, cleanup и failure semantics и не должен
прятаться внутри execute request.

## Secrets and network

### Secrets

Первая конфигурация должна быть `no secrets by default`. `ExecutionSpec` не
должна принимать raw secret values. Named secret capability можно рассмотреть
позже, только с отдельным owner, explicit allowlist, expiry, non-persistence,
redaction and audit record. Secret provenance может фиксировать, что named
secret был доступен, но не его значение.

stdout/stderr и captured artifacts должны проходить redaction before durable
storage; redaction не должна превращать неполную запись в доказательство
отсутствия секрета. Existing `SECRET`, `SENSITIVE_INTERNAL` и
`SAFE_TECHNICAL_IDENTIFIER` classes из `references/shared-evidence-model.md`
нужно переиспользовать.

### Network

First-slice default: `NO_NETWORK`. Environment-owned service dependencies могут
быть extension seam, но их endpoint/allowlist, DNS behavior, egress and
qualification должны быть explicit. `UNRESTRICTED_NETWORK` недопустим как
convenience default: тест может эксфильтрировать secrets или атаковать третьи
системы.

## Execution Attempt and state

Одна фактическая invocation должна иметь отдельную immutable identity,
связанную с одним frozen spec. Минимальные candidate states:

```text
PENDING → RUNNING → SUCCEEDED | FAILED | CANCELLED | TIMED_OUT
```

`PENDING/RUNNING/...` — process execution state, не Test Assurance verdict.
`SUCCEEDED` означает только, что process завершился с contract-defined success
condition; даже это не означает `TESTED`, `PASSED` или compliance без owner
interpretation. Ненулевой exit code не должен уничтожать distinction между
test assertion failure и executor/environment failure.

Minimum attempt provenance should retain:

```text
attempt identity
authorization/spec references
source/tree/environment binding
executor identity/version
start/finish timestamps
exit code when available
termination reason
stdout/stderr/artifact references and hashes
observed cleanup result
```

### Failure taxonomy

Минимально различать:

```text
PROCESS_NONZERO
TIMEOUT
CANCELLED
EXECUTOR_FAILURE
ENVIRONMENT_UNAVAILABLE
SOURCE_MISMATCH
SPEC_MISMATCH
AUTHORIZATION_DENIED
ARTIFACT_CAPTURE_FAILURE
ARTIFACT_PARSE_FAILURE
UNKNOWN_OUTCOME
```

`PROCESS_NONZERO` может быть нормализован Test Engineering как failed test,
но это interpretation. `TIMEOUT`, `CANCELLED`, `ENVIRONMENT_UNAVAILABLE` и
`UNKNOWN_OUTCOME` не должны автоматически становиться assurance FAIL или
RESOLVED/ACTIVE lifecycle transition.

## Runtime Evidence alternatives

### Alternative 1 — one normalized result record

Attempt сразу сохраняет exit code, logs, artifacts и normalized status. Это
просто, но смешивает immutable observation с последующей нормализацией и
затрудняет повторное чтение/исправление parser без потери raw data.

### Alternative 2 — raw observation → normalized evidence

Raw output сохраняется immutable как content-addressed refs; отдельная
normalized record связывает его с exact attempt/spec/source/environment и
указывает parser/normalizer version. Test Engineering owner затем принимает
его как evidence. Это на один слой больше, но лучше сохраняет provenance,
reprocessing boundary и distinction `observed_result` vs semantic conclusion.

### Alternative 3 — runtime evidence directly in `EV-*`

Это максимально переиспользует existing evidence family, но опасно, если
`EV-*` начнёт владеть process lifecycle, log storage, retry или execution
authorization. Existing contract позволяет reference accepted runtime
observation, но не задаёт ingestion mechanism.

### Вывод

Рекомендуется Alternative 2 с bridge/reference в existing `EV-*` и `TM-*`.
Raw observation и normalized evidence не являются новой assurance authority;
они — execution provenance records, которые Test Engineering может принять по
своим правилам. Если design докажет, что отдельный raw record чрезмерен, его
можно физически объединить с attempt при сохранении двух логических слоёв.

## Retry, cancellation, timeout and resources

### Retry

Retry — это новый `ExecutionAttempt` с тем же exact `ExecutionSpec` и новым
attempt identity. Изменение source, argv, environment, inputs или policy — не
retry, а новый spec/authorization. Automatic semantic retry не нужен в first
slice; explicit orchestration может запросить новую попытку, сохранив связь с
предыдущей и reason.

### Cancellation and process tree

Timeout/user cancellation/orchestrator cancellation должны сохранять
различные requested/observed reasons. Termination должна охватывать process
group/tree, а не только parent, иначе child process и network/file side effects
могут остаться после `CANCELLED`/`TIMED_OUT`. Cleanup outcome должен попасть в
observation; orphaned process — explicit executor failure/limitation.

### Timeout

Unlimited execution недопустим. Design должен задать conservative default и
hard maximum; override разрешён только authorization policy, не caller input.
Точные численные значения требуют design/operational decision и здесь не
изобретаются.

### Resource limits

| Ресурс | First slice |
|---|---|
| Wall-clock timeout | `REQUIRED_FIRST_SLICE` |
| Process-group termination | `REQUIRED_FIRST_SLICE` |
| Memory/CPU | `REQUIRED_FIRST_SLICE` для untrusted/container execution; иначе explicit residual risk и design decision |
| Disk/output quota | `REQUIRED_FIRST_SLICE` |
| Process count/fork limit | `REQUIRED_FIRST_SLICE` для untrusted/container execution |
| File descriptors | `LATER`, если host/container policy не предоставляет bounded default |
| Distributed scheduling/backpressure | `LATER` |

## Execution location alternatives

| Подход | Benefits | Cost/risks | Fit |
|---|---|---|---|
| A. Local bounded executor | Минимальная operational complexity, удобно для developer workflow, быстрое выполнение argv-only команд | Слабее isolation; malicious test может повредить host, читать лишние files или оставить processes; нужны OS-level limits | Подходит только для trusted/explicitly admitted code и как narrow adapter; residual host risk нужно принять явно. |
| B. Isolated container executor | Сильнее filesystem/process/network boundary, reproducible image digest, естественный seam для later environments | Container runtime dependency, image lifecycle, volume/UID/port complexity, more setup; container не абсолютная security boundary | Лучший default для безопасного execution of nontrivial or untrusted tests; fits future simulator/E2E seam without making them first slice. |
| C. External CI adapter | Reuses mature isolation/secrets/logging and remote resources; useful for Product/E2E later | Provider-specific authority, network/API dependency, result trust/identity mapping, hard local reproducibility, more integration | Не подходит как first substrate in Markdown repo; later adapter over same authorization/spec/evidence contract. |

### Recommendation

Рекомендуется design around a common bounded execution contract with B as the
security-oriented implementation target and A as an explicitly restricted
developer adapter only if the trust model permits it. C remains a later adapter.
The contract must not expose location-specific authority: all approaches
consume the same authorized immutable spec and produce the same attempt/evidence
provenance.

## Change Review integration

Candidate flow:

```text
accepted baseline B
    → CHANGE_REVIEW with candidate C
    → selected/authorized test execution on C
    → candidate-bound attempt/evidence
    → Test Engineering candidate assessment
    → explicit RECONCILE_CHANGE / owner reproof if accepted
```

Execution on C must not mutate accepted B, `BC/MAT/TM/GAP/CC`, Product baseline
or projections. If the candidate is dirty, its tree fingerprint and admission
decision are part of the candidate binding. Candidate runtime evidence may
support `candidate_test_impact`, but it is not accepted `TESTED` until the
existing owner-controlled reconciliation/adjudication path accepts it.

## Product / multi-repository extension seam

First slice: one command, one qualified Project/repository source binding, one
isolated workspace. A future Project-spanning test can compose a frozen vector
of per-repository bindings plus explicit service/environment bindings. Product
execution must use the existing Product revision/baseline qualification and
must not infer member permissions from membership.

Product-wide E2E is later because it adds orchestration, topology, cross-member
authorization, environment lifecycle and result aggregation. The seam is a
composite ExecutionSpec/EnvironmentBinding, not a Product lifecycle authority.
One Project attempt cannot automatically advance Project/Product baseline,
finding lifecycle or assurance authority.

## Simulator/test-implementation separation

Service Simulator implementation is later and separate. Existing contract
distinguishes a dependency substitute from a simulator of the reviewed service,
requires accepted/fresh simulator specification and explicit authorization, and
does not implement simulator code during review. Execution Runtime can execute
an already-built simulator as a dependency only when its source/environment
binding is explicitly authorized; it does not generate, write, or publish the
simulator.

The same boundary applies to test implementation:

```text
implement test  !=  execute existing test
```

First slice accepts only an already-existing executable test or explicitly
approved verification command. Code generation, file mutation and commit are
separate future authority. `GAP-* → TASK-* → implementation authorization →
test implementation → execution authorization` is a later workflow seam, not
new meaning for current `TASK-*`.

## GAP-* and TASK-* evolution

The eventual traceability can be:

```text
GAP-*
  → TASK-* remediation work
  → separate implementation authorization (if code must be written)
  → existing test implementation binding
  → separate execution authorization
  → ExecutionSpec / Attempt / Runtime Evidence
  → Test Engineering owner adjudication
```

This preserves current ownership. A completed `TASK-*` does not resolve a
`GAP-*`; a successful process does not resolve a `GAP-*`; only accepted
sufficient evidence under Test Engineering semantics can change the assurance
state.

## Assurance interpretation

The executor may normalize process facts, but the semantic path remains:

```text
ExecutionAttempt
  → RawExecutionObservation
  → NormalizedRuntimeEvidence
  → existing TM/MAT/Test Assurance owner
  → accepted assurance result
```

`exit_code == 0` can be interpreted as successful process completion only where
the accepted test contract defines that mapping. It never universally means
`PASSED`, `TESTED`, compliance, finding resolution, or baseline advancement.

## Freshness and conservative reuse

Runtime evidence becomes stale or requires revalidation when any materially
bound input changes:

```text
source/tree
test implementation
execution profile/spec/normalizer
environment image/toolchain/dependency lock
relevant configuration/fixtures/service bindings
accepted behavior/contract/assurance semantics
```

Candidate exact reuse requires a complete match of execution spec fingerprint,
source/tree fingerprint, environment fingerprint, test implementation
fingerprint and relevant input/config snapshot. An omitted or unknown input is
not proof that it did not change. Reuse is therefore an explicit qualified
decision, not a cache hit inferred from filename or successful prior output.

Existing `REVALIDATE` and Projection Impact machinery can route affected
semantic/projection consumers. It must not be replaced by a parallel runtime
freshness authority.

## Focused execution threat model

| Threat | First-slice mitigation | Later mitigation | Residual risk |
|---|---|---|---|
| Prompt injection → command execution | No LLM/report/MCP text is executable input; only explicit authorization and structured argv/profile | Human approval UX, policy engine, signed profiles | Authorized malicious command remains possible within granted scope. |
| Shell injection | No shell, no arbitrary command string, argv-only | Strongly reviewed shell adapter in isolated sandbox if necessary | Executable itself can still be malicious. |
| Path traversal/workspace escape | Canonicalize and validate roots, reject `..`/outside paths and symlink escapes, isolated workspace | Container mounts/user namespaces | Kernel/container vulnerabilities and misconfiguration. |
| Secret leakage | No secrets by default; no raw values in spec/fingerprint/evidence; redact logs/artifacts | Named secret capabilities and external secret broker | Test may exfiltrate any explicitly granted secret; redaction can be incomplete. |
| Network exfiltration | `NO_NETWORK` default, no implicit endpoints | Explicit allowlisted egress and network sandbox | Required environment-owned networking adds attack surface. |
| Fork/process bomb | Hard timeout; process-group kill; process/memory limits in container mode | Strong cgroups/rlimits/seccomp | Host local adapter has weaker containment. |
| Resource exhaustion | Wall timeout, output/disk quota, bounded temp area | CPU/memory/fd quotas and scheduler admission | Workload may fail due to conservative quotas. |
| Orphan processes | Kill process group/tree and record cleanup outcome | Runtime-specific supervisor/container teardown | Unobservable detached children remain residual risk. |
| Malicious test artifacts | Treat artifacts as untrusted bytes; hash/reference, do not execute or parse with privileged plugins | Typed parsers and separate analysis sandbox | Parser vulnerabilities in later consumers. |
| Log/artifact spoofing | Bind hashes to attempt and capture metadata; distinguish raw observation from normalized evidence | Signed executor attestations | A compromised executor can lie about local observation. |
| Source substitution | Verify source/tree at execution time; block mismatch | Immutable snapshot store and signed source attestations | Workspace/storage compromise. |
| Authorization TOCTOU | Freeze authorization/spec/profile revision and recheck immediately before run | Atomic snapshot/lease and signed policy decision | Race inside external environment remains possible. |
| Profile retargeting | Expand named profile to immutable exact spec and fingerprint it | Signed versioned profile registry | Trusted profile owner can authorize a dangerous profile. |
| Caller confused deputy | Authorization includes principal, purpose, scope, source, environment and expiry; Product membership grants none | Separate service identities and policy evaluation | Broad service credentials if introduced later. |
| Unauthorized repository mutation | Read-only source snapshot; writes only isolated temp/output; no commit/push | OS/container read-only mounts and explicit mutation workflow | Tests can mutate their temporary workspace. |

The most important first-slice residual risk is local execution of malicious or
untrusted code. If the product promise includes arbitrary repository tests,
container isolation (or external equivalent) is not optional hardening but a
design prerequisite. If first slice is restricted to trusted commands, that
restriction must be explicit, enforced and visible in authorization.

## YAGNI exclusions

The first design should explicitly exclude:

```text
full CI system
scheduler / distributed workers / Kubernetes
generic workflow engine
arbitrary shell and shell pipelines
automatic package installation
environment provisioning
Service Simulator generation
test code generation or modification
Product-wide E2E orchestration
secret manager
dashboard
database-backed queue
remote agent fleet
automatic semantic retry
automatic finding/GAP resolution
```

These are not merely deferred implementation tasks. Each would add authority,
security, lifecycle or operational semantics that must be separately designed.

## 2–3 architecture approaches

### A. Local argv-only bounded executor

Benefits: smallest code and operational footprint; fits a Markdown repository
and developer verification workflow; easy to debug. Security depends on strong
authorization, path policy, resource limits and trust in the host. It is
acceptable only for explicitly trusted/admitted source and leaves material
workspace/process escape residual risk for hostile tests.

### B. Isolated container executor

Benefits: clearer read/write/network/process boundary, reproducible image
identity and future seam for disposable environments, simulators and E2E.
Cost: container runtime, images, mounts, UID/permissions, artifact transfer
and operational diagnostics. It is the recommended security baseline when the
runtime will execute repository-controlled or otherwise untrusted code.

### C. External CI execution adapter

Benefits: provider may already offer isolation, secrets, logs, quotas and
multi-service environments. Cost: provider API trust, external availability,
source/result identity mapping, network dependency, local developer friction
and provider-specific semantics. It is a later adapter, not the first
execution authority; it must consume the same authorization/spec contract.

### Recommendation

Use a location-neutral bounded execution contract, design B as the safe default,
and allow A only as a deliberately narrower trusted-local profile if design
evidence justifies it. Keep C as a future adapter. Do not expose a generic
`run(command)` API.

## Recommended next design scope

Proceed to design the proposed bounded milestone:

```text
Test Execution Runtime Foundation
```

The design should decide the exact schema and ownership for:

- explicit `ExecutionAuthorization`, optionally linked to `TASK-*`, `TM-*`,
  Change Review and Session context but never replaced by them;
- immutable `ExecutionSpec`, preferably materialized from a versioned profile
  into structured argv and exact policies;
- one `ExecutionAttempt` per process invocation with process-state lifecycle;
- raw observation storage and normalized runtime evidence references;
- source/tree, workspace and environment binding with execution-time checks;
- no-shell, no-secret, no-network defaults and bounded output/filesystem policy;
- timeout, process-group cancellation and minimal resource limits;
- bridge to existing `EV-*`/`TM-*` and Test Engineering owner adjudication;
- one-repository first slice and explicit seams for Change Review, Product and
  later simulator/E2E execution.

This is a design scope, not an implementation sequence, API commitment or
roadmap status change.

## Open questions that genuinely require design decisions

1. Is the first supported threat model trusted local tests only, or must it
   safely contain repository-controlled/untrusted test code? This determines
   whether container isolation is mandatory rather than optional.
2. Which trusted principal may approve execution, and how is that approval
   represented, expired and revoked?
3. Should repository-owned named profiles be supported immediately, or should
   first design require exact argv snapshots only?
4. What OS/container mechanism supplies process-group kill and CPU/memory/disk
   limits on supported platforms?
5. Which result formats are in scope for first normalization (exit/process
   facts only, JUnit/XML, coverage), and which remain raw artifacts?
6. What exact source/tree snapshot mechanism handles clean, dirty, untracked
   and generated test content without mutating the canonical repository?
7. Which environment inputs are material for freshness and exact reuse, and
   how are non-secret values/fingerprints captured?
8. Is `NO_NETWORK` sufficient for the first executable tests, or is one
   environment-owned allowlisted dependency required by an accepted use case?
9. Which existing `EV-*`/`TM-*` acceptance fields are sufficient as references,
   and which attempt/evidence metadata must remain execution-owned?
10. What is the minimum artifact retention and redaction policy that preserves
    evidence without becoming a log/archive service?

## Discovery exit criteria

Discovery is complete enough to enter design when the following are accepted:

```text
current absence of runtime executor recorded
Test Engineering semantic authority preserved
execution authorization separated from TASK/Session/Product/report authority
argv-only and no-shell first-slice boundary recorded
source/tree TOCTOU and dirty-state rules identified
environment, secrets, network and filesystem defaults identified
attempt/evidence/assurance layers kept distinct
retry/cancel/timeout/resource failure classes identified
Change Review and Product extension seams identified
simulator and test implementation excluded from first slice
YAGNI exclusions explicit
open decisions reduced to design questions
```

## Discovery verdict

`READY_FOR_DESIGN`

Proposed bounded design title: `Test Execution Runtime Foundation`.

This verdict does not introduce Stage G, a new capability, a new `Session
Intent`, a runtime implementation, a Product/projection authority or an
implementation plan. It authorizes only the next design conversation under the
existing owner, evidence, freshness, authorization and projection boundaries.
