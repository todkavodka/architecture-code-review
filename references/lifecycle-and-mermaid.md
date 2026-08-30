# Жизненный цикл и Mermaid

Lifecycle reconstruction (реконструкция жизненного цикла) обязательна там, где поведение зависит от времени, фоновой работы, соединений, сессий, ресурсов, retry/reconnect или shutdown. Диаграммы нужны только когда добавляют архитектурную информацию; декоративной квоты нет, но substantial final report не должен оставаться без визуального объяснения material topology/lifecycle/ownership только потому, что writer его не нарисовал.

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

### Before → After architecture

Используй две компактные диаграммы или одну явно разделённую диаграмму, когда remediation/target меняет owner, lifecycle, boundary, ordering или source of truth. Читатель должен визуально видеть не только новый компонент, но и **какая проблемная зависимость исчезает**.

### Roadmap dependencies

Для нетривиальной dependency graph показывай prerequisites, gates и safe-activation boundary. Не рисуй последовательную цепочку, если задачи реально могут идти параллельно.

## 3. Visual coverage contract for final artifacts

Для substantial `STANDARD_FULL` или `FORENSIC` final package ожидается следующее визуальное покрытие, если соответствующая сложность существует в проекте:

1. **As-Built component/boundary view** — когда есть несколько существенных runtime-компонентов, процессов или внешних систем.
2. **Material runtime/lifecycle view** — когда ordering, ownership, concurrency, retry, startup или shutdown влияют на correctness.
3. **Target Architecture view** — когда endpoint включает target и target существенно меняет boundaries/ownership/flows.
4. **Before → After view** — для material correction, которую трудно понять только из prose.
5. **Roadmap dependency view** — когда prerequisites/safe activation нелинейны.

Это не механическая квота. Если конкретный пункт неприменим, диаграмма не нужна. Но если substantial report содержит сложную topology/lifecycle/target механику и не содержит ни одной полезной диаграммы, final writer/reviewer должен явно обосновать, почему визуализация не добавит информации.

Диаграммы относятся к user-facing explanation. Working artifacts могут содержать больше или меньше визуализаций по необходимости.

## 4. Диаграмма должна соответствовать evidence

Для каждой важной стрелки/transition должен существовать подтверждённый code path или явно маркированное допущение.

Не допускается:

- показывать target behavior как будто это current behavior;
- придумывать state только ради красивой FSM;
- скрывать race/interleaving, превращая конкурентные операции в линейную sequence;
- использовать диаграмму как единственное доказательство finding;
- рисовать generic boxes без связи с реальными subsystem names;
- повторять directory tree вместо runtime architecture.

## 5. Diagram explanation contract

Каждая material диаграмма сопровождается коротким prose-блоком:

- что именно она показывает;
- какой механизм/риск становится на ней виден;
- где current и где target state;
- какой вывод читатель должен из неё сделать.

Не вставляй Mermaid без контекста и не заставляй читателя самостоятельно угадывать смысл стрелок.

## 6. Проверка согласованности

Перед принятием документа сравни:

```text
prose
↔ ownership matrix
↔ state tables
↔ Mermaid
↔ authoritative findings
```

Если они расходятся, это consistency issue, а не редакционная мелочь.

## 7. Mermaid quality

- Используй простой стандартный Mermaid syntax.
- Реальные subsystem names, не `Service1`/`Component2`.
- Не кодируй огромные листинги в диаграмме.
- Подписывай owner/scope там, где это важно для понимания.
- Проверяй, что arrows/states отражают фактический path.
- Если Mermaid renderer недоступен, хотя бы проверяй структуру и избегай экзотического syntax.
