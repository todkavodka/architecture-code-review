# Аудит контрактов границ

Используй этот reference для значимых IPC/API/RPC/native/process/event boundaries (границ взаимодействия). Это не checklist ради количества; цель — проверить, сохраняет ли граница необходимую идентичность, порядок, отмену, владение и ошибки.

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
| Validation | Проверяются ли runtime arguments/shape/range на границе? |
| Serialization | Реально ли payload безопасно и однозначно сериализуется через boundary? |
| Lifecycle | Кто регистрирует/снимает handler/listener/subscription? |
| Ownership | Кто имеет право менять упомянутый ресурс/состояние? |
| Error contract | Может ли caller отличить error classes и сохранить контекст? |
| Backpressure | Может ли producer опередить consumer и что тогда происходит? |

## Метод

1. Инвентаризируй boundary channels/endpoints/commands/events.
2. Для каждого material path проследи producer → boundary → consumer → side effect → response/event.
3. Отдельно отметь runtime validation и sender/origin/trust checks.
4. Проверь duplicate/in-flight/cancel/late completion сценарии из `ownership-and-scenarios.md`.
5. Фиксируй positive controls; отсутствие проверки в одном слое может быть компенсировано реальной гарантией в другом — это надо проследить, а не предположить.

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
boundary
identity/scope
producer
consumer
reachable scenario
failed/absent contract
existing guard/falsification
concrete impact
```

Не создавай findings для каждого непокрытого измерения; измерения — lens, а не quota.
