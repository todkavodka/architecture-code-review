# Жизненный цикл и Mermaid

Lifecycle reconstruction (реконструкция жизненного цикла) обязательна там, где поведение зависит от времени, фоновой работы, соединений, сессий, ресурсов, retry/reconnect или shutdown. Диаграммы нужны только когда добавляют архитектурную информацию; фиксированной декоративной квоты нет.

## 1. Обязательные вопросы жизненного цикла

Для каждого significant process/connection/task/session/resource ответь:

- кто создаёт;
- какие prerequisites нужны;
- кто владеет во время работы;
- какие состояния реально существуют;
- какие события вызывают transitions;
- что происходит при failure;
- кто управляет retry/reconnect;
- что отменяет работу и какой scope у отмены;
- что происходит при logout/reconfiguration/window close/process shutdown;
- какие ресурсы должны быть освобождены;
- может ли случайно существовать несколько экземпляров;
- что происходит с in-flight work при смене owner/generation;
- какой completion считается stale и как он подавляется.

Связывай ответы с ownership matrix и adversarial scenarios из `ownership-and-scenarios.md`.

## 2. Какие диаграммы использовать

Создавай диаграмму, если она помогает доказать или объяснить важный механизм.

### Architecture flowchart

Показывай процессы/компоненты, state stores, внешние системы и trust-relevant boundaries. Не рисуй directory tree.

### Overall lifecycle / state diagram

`stateDiagram-v2` полезен, когда есть реальные состояния и transitions. Включай failure/recovery/cancel/shutdown, а не только happy path.

### Startup

Показывай configuration load, restoration, dependency construction, handler registration, background startup, UI/readiness и startup failure behavior, если это существенно.

### Runtime sequence

`sequenceDiagram` с реальными component names нужен для material end-to-end flow: initiator → boundaries → side effect → completion/error.

### Background task / retry / reconnect

Показывай creation, running/waiting, cancellation, retry/backoff, terminal failure и ownership. Если фоновой работы нет — не изобретай диаграмму.

### Shutdown

Показывай rejection of new work (если есть), cancellation/drain/flush, persistence, sockets/processes/database cleanup и final exit. Отдельно отмечай fire-and-forget cleanup и API, которые runtime может не ожидать.

### Trust boundaries

Показывай untrusted input и места validation/authorization: UI/native, network, filesystem, external process, plugin, deep link, uploaded content и т.п.

## 3. Диаграмма должна соответствовать evidence

Для каждой важной стрелки/transition должен существовать подтверждённый code path или явно маркированное допущение.

Не допускается:

- показывать target behavior как будто это current behavior;
- придумывать state только ради красивой FSM;
- скрывать race/interleaving, превращая конкурентные операции в линейную sequence;
- использовать диаграмму как единственное доказательство finding.

## 4. Проверка согласованности

Перед принятием документа сравни:

```text
prose
↔ ownership matrix
↔ state tables
↔ Mermaid
↔ authoritative findings
```

Если они расходятся, это consistency issue, а не редакционная мелочь.

## 5. Mermaid quality

- Используй простой стандартный Mermaid syntax.
- Реальные subsystem names, не `Service1`/`Component2`.
- Не кодируй огромные листинги в диаграмме.
- Подписывай owner/scope там, где это важно для понимания.
- Проверяй, что arrows/states отражают фактический path.
- Если Mermaid renderer недоступен, хотя бы проверяй структуру и избегай экзотического syntax.
