# Аудит контрактов границ

Используй этот reference для анализа значимых границ, где данные, identity,
authority или dynamic construction переходят из одного semantic contract в
другой. Factual boundary objects/views (components, interfaces, interactions,
flows, auth/trust, stores, configuration and error contracts) потребляются из
accepted/fresh STM; этот файл не поддерживает параллельный factual boundary
inventory.

Это включает не только IPC/API/RPC/native/process/event interaction boundaries, но и:

```text
interaction boundaries
interpreter boundaries
resource-addressing boundaries
authority / capability boundaries
```

Это не checklist ради количества; цель — проверить, сохраняет ли граница необходимую идентичность, порядок, отмену, владение, validation/trust semantics и ошибки.

Discovery completeness для классов границ регулируется `discovery-coverage.md`; этот файл задаёт dimensions и метод анализа конкретной границы.

## Типы границ

### Interaction boundaries

IPC/API/RPC/native/process/event transitions между producer и consumer.

### Interpreter boundaries

Dynamic text/value construction, который затем интерпретируется SQL engine, shell, template/eval/expression engine, regex/query DSL или другим interpreter-like consumer.

### Resource-addressing boundaries

Переход от external/persisted identifier к filesystem path, object-storage key, archive target, temp resource, URL/endpoint или другому resource locator.

### Authority / capability boundaries

Место, где caller identity/context превращается в permission/capability: privileged API, admin/service path, native bridge, process/device/socket control, mutation authority или access to protected state.

Один runtime path может пересекать несколько типов одновременно.

## Контрактные измерения

| Dimension | Проверочный вопрос |
|---|---|
| Identity | О какой сущности/владельце операция? Может ли локальный ID быть неоднозначным без parent identity? |
| Correlation | Можно ли однозначно связать ответ/event с инициировавшим запросом? |
| Ordering | Что происходит при late/out-of-order response/event? |
| Concurrency | Могут ли две операции существовать одновременно и не перезаписать состояние друг друга? |
| Cancellation | Какая именно операция отменяется? Отмена scoped или глобальная? |
| Timeout | Ограничено ли ожидание там, где бесконечность не является явным контрактом? |
| Authorization / trust | Кто имеет право вызывать capability и на каком boundary это проверяется? |
| Validation | Проверяются ли runtime arguments/shape/range/content на границе? |
| Provenance | Кто контролирует значение: direct external input, validated input, persisted data, config, constant, internal state? |
| Construction / interpretation | Становится ли значение executable/interpreted syntax или остаётся bind/data value? Какие escaping/parameterization semantics реальны? |
| Resource resolution | Как identifier нормализуется/canonicalizes и к какому фактическому resource/root/network target разрешается? |
| Serialization | Реально ли payload безопасно и однозначно сериализуется через boundary? |
| Lifecycle | Кто регистрирует/снимает handler/listener/subscription? |
| Ownership | Кто имеет право менять упомянутый ресурс/состояние? |
| Error contract | Может ли caller отличить error classes и сохранить контекст? |
| Backpressure | Может ли producer опередить consumer и что тогда происходит? |

Не каждое dimension применимо к каждому типу границы.

## Метод

1. Получи accepted/fresh STM boundary objects/views для scope данного pass и
   проверь их coverage/freshness/provenance. Если factual slice missing, stale
   или conflicting, запроси `TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT` или
   `TECH_FACT_REVALIDATION_REQUEST` у Technical Model Gate; не молча создавай
   второй inventory.
2. Для каждого material path проследи producer/source → boundary → consumer/interpreter/resource → side effect → response/event/effect.
3. Отдельно отметь runtime validation, provenance, sender/origin/trust checks и parameterization/normalization semantics, где они применимы.
4. Проверь duplicate/in-flight/cancel/late completion сценарии из `ownership-and-scenarios.md` для stateful/async boundaries.
5. Фиксируй positive controls; отсутствие проверки в одном слое может быть компенсировано реальной гарантией в другом — это надо проследить, а не предположить.
6. Используй `discovery-coverage.md`, чтобы доказать, что material boundary classes были рассмотрены; наличие одного хорошо разобранного IPC path не закрывает interpreter/resource/authority coverage автоматически.

## IPC / event-specific

Проверяй:

- generic preload surface vs actual reachable renderer compromise;
- `sendToAllWindows`/broadcast semantics;
- listener accumulation и cleanup;
- request IDs / owner IDs;
- `.on` / `.once` фактическую EventEmitter semantics, не интуитивную модель;
- event payload содержит identity, но consumer её игнорирует;
- renderer selection state используется как owner identity для асинхронного completion.

Broad capability surface без достижимого attacker entry point — не автоматический RCE finding. Security promotion регулируется `evidence-and-severity.md`.

## Interpreter-specific

Для raw/dynamic interpreter construction проверь:

```text
source provenance
→ validation / allowlist
→ escaping / parameterization
→ construction
→ interpreter semantics
→ reachable effect
```

Не приравнивай:

```text
string interpolation into a bind/data value
```

к:

```text
string interpolation into interpreted command/query text
```

и не считай raw-looking API finding без concrete provenance/effect.

Detailed source classifications и proof-of-coverage находятся в `discovery-coverage.md`.

## Resource-addressing-specific

Проверяй:

- normalization/canonicalization;
- root/scope containment;
- path traversal;
- symlink/TOCTOU semantics;
- archive extraction destination;
- object-key collisions/overwrites;
- user-controlled filenames;
- URL/host/redirect/proxy target resolution;
- cleanup ownership.

## Authority / capability-specific

Проверяй:

- caller identity/context;
- object/workspace/owner scope;
- alternate service/admin paths;
- capability acquisition and lifetime;
- privileged API/process/device/socket access;
- stale identity/capability reuse;
- read vs write authority;
- bulk/list semantics vs point operation semantics.

## Native/process boundaries

Для child processes/CLI/native integration проверь:

- аргументы и секреты в argv/environment;
- shell usage и quoting;
- process ownership/lifetime;
- cancellation/termination scope;
- fixed ports/files/temp paths;
- exit/error propagation;
- privilege boundary/elevation;
- cleanup during shutdown.

## Output

Каждый material boundary issue должен содержать:

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

Не создавай findings для каждого непокрытого измерения; dimensions — lens, а не quota.
