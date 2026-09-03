# Architecture Code Review Skill

Переиспользуемый agent skill для evidence-first (сначала доказательства) архитектурного и кодового ревью существующих программных систем.

Skill не превращает ревью в список запахов кода. Он помогает восстановить фактическую архитектуру системы, проследить владение состоянием и lifecycle, независимо проверить кандидатов на проблемы, отделить корневые причины от их проявлений и только после этого оценить severity и предложить направление исправления.

Итоговый пользовательский отчёт по умолчанию пишется связным русским техническим текстом. Точные идентификаторы кода, названия протоколов, пути, API/IPC-имена и формальные status markers сохраняются без перевода.

## Что проверяет Skill

Используйте его для ревью всего проекта или отдельной подсистемы, когда существенны:

- границы ответственности и архитектура;
- владение состоянием и ресурсами;
- lifecycle запуска, штатной работы, восстановления, reconnect, cancellation и shutdown;
- concurrency и фоновые операции;
- контракты IPC/API/native boundaries;
- security и trust boundaries;
- configuration и persistence;
- контракты ошибок и observability;
- maintainability и testability;
- Target Architecture и remediation roadmap, если они явно запрошены.

В репозитории есть technology-specific lenses для:

- Tauri;
- Electron;
- React;
- Django;
- FastAPI;
- Litestar;
- Ansible (stack addendum).

Общий метод ревью technology-independent. Stack addenda добавляют вопросы для сбора evidence, но не заменяют основной workflow.

Ansible подключается через обычный механизм stack addenda. Это не отдельная capability, endpoint, группа артефактов или lifecycle.

## Основные возможности v0.2

Версия 0.2 вводит управляемый многоступенчатый workflow:

- явный выбор глубины `STANDARD_FULL` или `FORENSIC`;
- независимый выбор требуемого endpoint;
- подробная реконструкция As-Built Architecture до поиска тематических проблем;
- обязательное независимое ревью As-Built в обоих режимах;
- матрицы владения, инвариантов и неблагоприятных сценариев;
- отдельный анализ контрактов IPC/API/native boundaries;
- независимая проверка кандидатов до превращения их в authoritative findings;
- разделение root, projection и SER до назначения severity;
- требование evidence-backed attack chain для серьёзных security-утверждений;
- постоянное состояние workflow в `working/INDEX.md` и возобновляемые handoff-артефакты;
- обработка архитектурных corrections и `REVALIDATION_REQUIRED`;
- опциональные Target Architecture и независимое ревью её реализуемости;
- опциональный remediation roadmap с проверкой согласованности порядка выполнения;
- свежий editorial review, который не может незаметно изменить технический смысл;
- chunked writing и восстановление работы при ограничении контекста.

## Установка

### OpenCode / Codex и другие агенты, использующие `~/.agents/skills`

Клонируйте репозиторий непосредственно в каталог персональных skills:

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

Затем начните новую сессию агента, чтобы Skill был обнаружен с диска.

Если каталог уже существует, обновите его вместо повторного клонирования:

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git pull --ff-only
```

Проверьте установленную ревизию:

```bash
cd ~/.agents/skills/architecture-code-review
git rev-parse HEAD
```

### Установка конкретной опубликованной версии

Когда появится release tag, для воспроизводимости можно закрепить установку на нём:

```bash
cd ~/.agents/skills/architecture-code-review
git fetch --tags
git checkout v0.2.0
```

Чтобы позже вернуться к последней production-версии:

```bash
git switch main
git pull --ff-only
```

## Использование

Начните новую сессию агента в репозитории, который хотите проверить, и явно попросите использовать Skill:

```text
Use architecture-code-review to perform a full architecture review of this repository.
```

Или по-русски:

```text
Используй architecture-code-review и проведи полный архитектурный аудит этого проекта.
```

Результат можно указать сразу:

```text
Используй architecture-code-review.
Нужен полный аудит плюс целевая архитектура и план исправлений.
```

Skill не должен сразу начинать глубокое исследование. Сначала Start Gate разделяет два независимых решения: глубину ревью и требуемый итоговый результат.

Architecture Review — основной umbrella workflow. Test Review — composable capability, которую можно выбрать в начале, подключить по рекомендации discovery, если обнаружена существенная поверхность автоматизированных тестов, или добавить позже, возобновив существующий audit из `working/INDEX.md`.

Пример выбора capability:

```text
Architecture Review: REVIEW_ONLY
Test Review: REVIEW_PLUS_TEST_PLAN
```

Endpoint Test Review независим от endpoint Architecture Review и может быть `REVIEW_ONLY` или `REVIEW_PLUS_TEST_PLAN`. Позднее подключение Test Review по умолчанию не перезапускает уже принятые этапы архитектурного ревью. Детальная assurance map и evidence остаются в authoritative артефакте Test Review, а umbrella report связывает и синтезирует принятые cross-capability выводы.

Коротко:

```text
Use architecture-code-review for a full architecture review.
Add Test Review now when test assurance is requested.
Later, resume the existing audit and add Test Review to its capability registry.
```

## Глубина ревью

### `STANDARD_FULL`

Полное архитектурное ревью с цепочкой verification и adjudication, но с достаточно компактным тематическим исследованием.

Это обычный режим для большинства production-репозиториев.

### `FORENSIC`

Более глубокое расследование с раздельными тематическими проходами, расширенным evidence trail, неблагоприятными сценариями и дополнительными рабочими артефактами.

Выбирайте его, когда проблемы тонкие, связаны с несколькими процессами, concurrency, security или плохо воспроизводятся обычным ревью.

Skill может рекомендовать глубину, но не должен молча выбирать `FORENSIC`.

## Требуемый endpoint

Глубина и endpoint выбираются независимо.

### `REVIEW_ONLY`

Формирует архитектурный review и authoritative findings ledger.

### `REVIEW_PLUS_TARGET_ARCHITECTURE`

Дополнительно формирует Target Architecture / To-Be design и проводит её ревью. Она строится на verified findings, инвариантах, положительных механизмах и явных product decisions.

### `REVIEW_PLUS_TARGET_AND_ROADMAP`

Дополнительно формирует Target Architecture и remediation roadmap с зависимостями и проверкой согласованности порядка исправлений.

Выбор `FORENSIC` сам по себе не означает, что нужна Target Architecture или Roadmap.

## Как устроен workflow

В общих чертах:

```text
baseline
  -> As-Built Architecture
  -> independent As-Built review
  -> thematic discovery
  -> candidate verification
  -> root-boundary adjudication
  -> severity adjudication
  -> authoritative findings ledger
  -> optional Target Architecture + independent review
  -> optional remediation roadmap + execution-consistency review
  -> final package assembly
  -> fresh editorial review / correction / re-review
```

Ключевой принцип: discovery не создаёт final findings напрямую. Кандидат должен пройти independent verification, root-boundary adjudication и severity adjudication.

## Evidence-first подход

Для material finding разделяйте:

1. observation — что система фактически делает;
2. interpretation — почему это важно;
3. concrete mechanism — какой механизм создаёт проблему;
4. impact — к какому последствию он приводит;
5. recommendation — в каком направлении исправлять.

Утверждения должны ссылаться на конкретное evidence в формате `path:line-range`. Для cross-layer findings обычно нужны доказательства с каждой существенно затронутой границы.

Claim scope не может быть шире evidence scope: один handler не доказывает system-wide authorization isolation, успешный nominal path не доказывает retry/idempotency/restart/concurrency, а read-path не доказывает write, enumeration, background или export paths. Если область не исследована, результатом должны быть `PARTIAL`, `NOT_PROVEN` или `UNKNOWN`, а не выдуманный дефект.

Поэтому Skill намеренно отвергает типичные shortcuts:

- имена директорий не доказывают архитектуру;
- размер файла сам по себе не является дефектом;
- `unwrap`, `clone`, mocks, TODOs и hardcoded values не становятся findings без доказанного impact;
- отсутствие тестов не доказывает, что production behavior сломан;
- широкие privileged APIs сами по себе не доказывают RCE;
- security severity не повышается без правдоподобной attacker chain;
- rewrite не предлагается только потому, что можно вообразить более «чистую» архитектуру.

## Discovery coverage

Полнота discovery определяется не числом файлов, тестов или findings, а bounded material accounting — ограниченным учётом всех существенных domains и механизмов в заявленной области.

Перед общим выводом capability формирует bounded inventory material targets/domains. Каждый применимый элемент получает evidence, disposition или явное ограничение. Selective deep inspection допустимо; sample, test count, line coverage и зелёный CI не являются доказательством полноты.

Architecture Discovery Coverage ведёт свою domain matrix. Test Review ведёт собственный bounded target universe; одна матрица не подменяет другую.

## Независимая проверка и корневые причины

Автор discovery не является окончательным судьёй. Кандидаты проходят отдельную falsification/verification-проверку: проверяется достижимость, ownership, guards, альтернативные пути, concrete effect и наличие противоречащего evidence.

После этого root-boundary adjudication отвечает на вопрос, является ли наблюдаемое поведение одной корневой проблемой, projection того же механизма, supporting engineering risk или отдельным finding. Несвязанные механизмы не объединяются только по тематическому сходству.

Severity назначается только после того, как correctness кандидата подтверждена и корневая граница определена. Высокая уверенность в том, что проблема существует, не означает автоматически высокую severity.

## Persistent workflow и артефакты

Для длинных ревью `working/INDEX.md` — persistent authority состояния workflow. Результат агента не считается принятым только потому, что агент сообщил о завершении.

Рабочие артефакты проходят явные состояния:

```text
PENDING
IN_PROGRESS
ARTIFACT_WRITTEN
REVIEW_REQUIRED
CORRECTION_REQUIRED
REVALIDATION_REQUIRED
BLOCKED
COMPLETE
NOT_APPLICABLE
```

Downstream stage не должен использовать `REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED` или `BLOCKED` как accepted truth.

Типовой итоговый пакет создаётся в:

```text
docs/reviews/architecture-review/
```

В зависимости от endpoint он содержит:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md       # when requested
├── 04-remediation-roadmap.md       # when requested
└── working/
    └── ... intermediate evidence and review artifacts
```

`working/` содержит промежуточные evidence, разбор кандидатов, независимые проверки, corrections и persisted handoffs. Промежуточные claims могут быть исправлены или опровергнуты; authoritative state отслеживается через workflow registry и итоговые документы.

## Структура репозитория

```text
.
├── README.md
├── LICENSE
├── SKILL.md
├── references/
│   ├── review-modes-and-orchestration.md
│   ├── review-method.md
│   ├── evidence-and-severity.md
│   ├── ownership-and-scenarios.md
│   ├── boundary-contract-audit.md
│   ├── independent-verification.md
│   ├── root-boundary-adjudication.md
│   ├── lifecycle-and-mermaid.md
│   ├── report-contract.md
│   ├── target-architecture-review.md
│   ├── remediation-roadmap-review.md
│   ├── final-editorial-review.md
│   └── stacks/
└── tests/
    ├── pressure-scenarios.md
    └── pressure-validation-matrix.md
```

`SKILL.md` — намеренно компактный orchestrator. Подробные нормативные правила находятся в authoritative reference files, а не дублируются в entrypoint.

## Validation

Реализация v0.2 была проверена pressure scenarios в свежих изолированных контекстах агентов.

Результат runtime validation:

```text
32 / 32 required scenarios PASS
0 failed
0 blocked
0 inconclusive
```

Независимое implementation review сообщило:

```text
BLOCKER 0
HIGH    0
```

Development repository сохраняет внутренние benchmarks, design documents, review materials и raw validation evidence. Этот public repository содержит только распространяемый Skill package и его pressure-test contracts.

## Обновление Skill

Для обычной установки, отслеживающей `main`:

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git pull --ff-only
```

После обновления начните новую сессию агента, чтобы runtime заново загрузил Skill с диска.

В production-средах, где важна воспроизводимость, предпочтительно закреплять release tag, а не постоянно следовать за `main`.

## Разработка и contribution

Изменения Skill следует рассматривать как изменения поведения, а не как обычную правку текста. Для новых указаний используются pressure scenarios и fresh-context validation, чтобы проверить изменение поведения агента и отсутствие конфликтующей authority или workflow regression.

Перед продвижением существенного изменения сохраняйте последовательность:

```text
design
-> implementation plan
-> isolated implementation
-> independent review
-> pressure validation
-> promotion readiness
-> public package
-> release
```

Сам по себе внешний вид documentation-only изменения не доказывает, что поведение Skill осталось неизменным.

## Лицензия

Проект распространяется по лицензии MIT. Полный текст находится в `LICENSE`.
