# План исправлений и проверка исполнимости

Этот этап выполняется только для `REVIEW_PLUS_TARGET_AND_ROADMAP` после принятия Target Architecture.

## 1. Roadmap строится по зависимостям, не по severity

Severity помогает приоритизировать риск, но порядок реализации определяется prerequisites и безопасной активацией.

Каждая material task должна содержать два слоя: сначала человеческое объяснение архитектурной проблемы и результата, затем implementation contract.

### 1.1 Human-readable task layer

До списка файлов, tests, prerequisites и rollback каждая material task объясняет:

1. **Проблема.** Что сейчас работает неправильно или нестабильно.
2. **Почему это происходит.** Какой ownership/lifecycle/boundary/state mechanism является причиной.
3. **Практическое последствие.** Какой runtime/security/reliability/testability effect возникает.
4. **Что нужно изменить.** Какой target mechanism вводится или какая ответственность переносится.
5. **Почему это закрывает root cause.** Какая causal link исчезает после изменения.
6. **Что получим после исправления.** Как изменится наблюдаемое поведение системы.

Human-readable layer пишется связанными абзацами. Для material explanatory prose придерживайся правила **one primary mechanism per paragraph**: один абзац может содержать evidence и последствия одного механизма, но не должен одновременно объяснять несколько независимых root causes.

Specialist English term или hybrid shorthand сначала объясни естественным русским предложением, если термин не очевиден из контекста. После этого точное техническое имя можно использовать как сокращение. Не превращай текст в словарь и не переводи exact identifiers.

**Не считай технический shorthand объяснением.** Например `eager startup`, `registered shutdown`, `drain+close`, `in-flight`, `producer-miss`, `single-flight` могут быть точными терминами, но сначала должно быть понятно, какое наблюдаемое поведение системы они обозначают.

Паттерн трансформации:

```text
Плохо:
NATS получает eager startup + registered shutdown + drain.

Хорошо:
При запуске приложение заранее проверяет доступность NATS и не объявляет себя готовым, если соединение установить невозможно. При остановке оно сначала завершает уже начатые операции, а затем корректно закрывает соединение. После такого объяснения поведение можно кратко называть fail-fast startup и graceful drain.
```

Точные слова примера не нормативны. Нормативен порядок: **объяснение механизма → специализированный термин**.

Если изменение существенно меняет topology, ownership, lifecycle, ordering или trust boundary, добавь Before → After Mermaid/flow diagram либо ссылку на соответствующую target diagram.

Не начинай task сразу с class/registry/function names. Сначала читатель должен понять **зачем вообще существует эта задача**.

Заголовок material task должен быть человеческим и описывать результат задачи. Не помещай в него `[prereq: ...]`, RF/SER metadata или другую execution metadata. Такие сведения относятся к техническому контракту.

### 1.2 Технический контракт реализации

После human-readable layer **обязательно** создай subsection с точным heading:

```markdown
### Технический контракт реализации
```

Только после этой границы размещай:

```text
TASK ID
RF/SER addressed
target mechanism
prerequisites
invariant transition
regression test first where applicable
allowed implementation boundary
forbidden scope
verification
exit criteria
rollback/fail-closed consideration where relevant
```

Предпочтительный формат — таблица или другой явно справочный блок. Implementation details должны быть точными, но не заменяют explanatory prose.

Пример формы:

```markdown
## TASK-F — Сделать жизненный цикл NATS управляемым

### Что сейчас не так
<connected prose>

### Почему это происходит
<ownership/lifecycle mechanism>

### Практическое последствие
<runtime consequence>

### Что предлагаем изменить
<target mechanism described in natural language first>

### Почему это закрывает корневую причину
<causal explanation>

### Что получим после исправления
<observable resulting behavior>

### Технический контракт реализации

| Параметр | Требование |
|---|---|
| Связанные замечания | RF-F |
| Целевой механизм | `CacheLifecycleManager` |
| Зависимости | Нет |
| Инвариант | ... |
| Регрессионные тесты | ... |
| Допустимая область изменений | ... |
| Запрещённая область | ... |
| Проверка | ... |
| Критерий завершения | ... |
| Откат / безопасная активация | ... |
```

Equivalent table contents are allowed, but the `### Технический контракт реализации` boundary is mandatory for every material roadmap task.

Unresolved product/deployment decision блокирует только зависимые tasks.

## 2. Semantic invariant → concrete representation

Roadmap обязан переводить target semantics в реальную runtime representation.

Проверяй, например:

- semantic composite key vs equality semantics конкретного языка/Map/dictionary;
- generation/version identity vs mutable object reference;
- cancellation scope vs global abort primitive;
- ownership model vs actual storage/index keys;
- durable idempotency vs process-local memory.

Красивый semantic type не гарантирует правильное runtime behavior.

## 3. Dependency isolation

Не создавай global phase gate, если решение влияет только на несколько tasks.

Нормально:

```text
Decision D2
→ blocks TASK-61 only

Independent TASK-31/32
→ may proceed
```

Неправильно: весь phase блокируется всеми decisions «для простоты».

## 4. Safe activation boundary

Для security/ownership/lifecycle changes явно опиши допустимое intermediate state.

Примеры риска:

- fake verifier существует до production trust authority и случайно активирует execution;
- новый auth path включён до миграции identity/state;
- новый cancellation protocol частично активирован и оставляет старый global cancel;
- signing/checksum enforcement включён несогласованно.

Если безопасной промежуточной комбинации нет — активируй зависимые production pieces атомарно или сохраняй fail-closed/old-safe behavior до полного cutover.

Test fake/fixture никогда не становится production trust authority.

## 5. Execution Consistency Review

Fresh-context reviewer проверяет цепочку:

```text
semantic invariant
→ concrete runtime representation
→ dependency isolation
→ safe production activation boundary
```

Также проверяет:

- task покрывает реальный RF/SER/target, а не новый scope;
- task title понятен как инженерная цель без bracketed prerequisite metadata;
- human-readable layer действительно объясняет current problem, root mechanism, consequence и target result;
- material paragraphs не смешивают несколько независимых root mechanisms;
- specialist shorthand не используется как замена объяснению;
- каждый material task содержит точный heading `### Технический контракт реализации`;
- execution metadata находится после этого heading;
- regression test реально проверяет mechanism;
- dependencies acyclic/объяснимы;
- task boundary достаточно мала для отдельного review;
- product decision не спрятан как implementation detail;
- platform/deployment constraints учтены;
- rollback/fail-closed behavior определён для risky activation;
- Before/After diagram присутствует, если без неё material ownership/lifecycle transition трудно понять;
- Mermaid diagrams, входящие в final roadmap, проходят render-validation gate из `lifecycle-and-mermaid.md`.

## 6. Review lifecycle

```text
roadmap author
→ self-check
→ fresh-context execution-consistency review
→ ROADMAP_ACCEPTED
   or ROADMAP_CORRECTION_REQUIRED
      → separate correction pass
      → fresh-context re-review
      → ACCEPTED | BLOCKED
```

Reviewer формирует issues, а не редактирует roadmap сам.

## 7. Acceptance

Roadmap accepted только когда:

- все material RF/SER target coverage traceable;
- material task titles human-readable and free of bracketed execution metadata;
- tasks имеют human-readable problem/result explanation и concrete implementation contract;
- каждый material task содержит `### Технический контракт реализации` перед execution metadata;
- specialist shorthand не заменяет объяснение механизма;
- tasks имеют concrete representation и verification;
- independent tasks не блокируются unrelated gates;
- unsafe intermediate activation не допускается;
- unresolved decisions изолированы;
- correction/re-review history сохранена;
- нет placeholders `TBD/TODO/implement later` в executable parts;
- dense internal shorthand не заменяет объяснение того, что задача решает и зачем;
- roadmap explanatory prose не содержит known paragraph-overload issues;
- все final roadmap Mermaid diagrams соответствуют diagram render-validation contract.
