# Architecture Code Review

`architecture-code-review` — skill для глубокого архитектурного и кодового аудита существующих систем.

Его задача — не собрать длинный список «подозрительных мест», а восстановить, **как система реально устроена и работает**, проверить границы ответственности и владение состоянием, проследить важные сценарии исполнения и только после этого формулировать выводы.

В основе подхода — простой принцип:

> **ширина утверждения не должна превышать ширину доказательств.**

Если проверен один обработчик, это не доказывает корректность всей модели авторизации. Если работает обычный сценарий, это ещё не доказывает корректность повторов, восстановления после сбоя, конкурентного выполнения или остановки процесса. Если доказательств недостаточно, результат должен оставаться `PARTIAL`, `NOT_PROVEN` или `UNKNOWN`, а не превращаться в выдуманный дефект.

Skill подходит как для аудита всего репозитория, так и для отдельной подсистемы.

## Как начинается работа

Начиная с Orchestrator v0.3, запуск Skill начинается не с безусловного нового аудита и не с выбора глубины. Сначала Session Orchestrator определяет состояние проекта и уже существующих audit packages.

Упрощённо старт выглядит так:

```text
repository identity + baseline + dirty state
  -> previous audit discovery
  -> authority / lineage reconciliation
  -> Project Profile
  -> Session Intent
  -> Review Suite Configuration
  -> только затем substantive review work
```

Это важно для повторных запусков: один и тот же проект не должен автоматически проходить полный аудит заново только потому, что Skill был вызван ещё раз.

### Session Intent

Пользователю доступны ровно пять first-class Session Intent:

- `USE_EXISTING` — использовать уже принятый аудит для того же committed baseline без технического rerun;
- `NEW` — явно начать новый полный bounded audit;
- `RESUME` — продолжить незавершённый аудит после проверки authority, revision bindings и freshness;
- `REVALIDATE` — проверить изменения относительно принятого baseline и перечитать только затронутые evidence slices;
- `EXTEND` — расширить assurance scope, например добавить Test Review, Target Architecture или Roadmap, не перезапуская несвязанные принятые части.

Типичные рекомендации:

```text
нет предыдущего audit package       -> NEW
IN_PROGRESS                         -> RESUME
COMPLETE + тот же committed HEAD    -> USE_EXISTING
COMPLETE + изменившийся HEAD        -> REVALIDATE
новая capability / endpoint         -> EXTEND
```

Если старый `IN_PROGRESS` audit существует, но baseline изменился, Skill сначала выполняет reconciliation. Это не отдельный шестой Session Intent: `RESUME_WITH_RECONCILIATION` — только flow внутри `RESUME`.

Если найдено несколько audit packages, выбор строится по repository identity, authority/status и lineage/ancestry. Timestamp сам по себе не является достаточным основанием выбрать «самый новый» audit.

### Review Suite Configuration для `NEW`

Для нового аудита пользователь отдельно выбирает архитектурную глубину, архитектурный endpoint и Test Review.

Архитектурная глубина:

```text
STANDARD_FULL
FORENSIC
```

Архитектурный endpoint:

```text
REVIEW_ONLY
REVIEW_PLUS_TARGET_ARCHITECTURE
REVIEW_PLUS_TARGET_AND_ROADMAP
```

Test Review всегда виден отдельным выбором:

```text
OFF
REVIEW_ONLY
REVIEW_PLUS_TEST_PLAN
```

Skill может рекомендовать `FORENSIC` или Test Review после лёгкой reconnaissance, но не должен включать их молча. Stack addenda остаются отдельными технологическими линзами и не являются capabilities.

### Повторный запуск не означает повторный аудит

`REVALIDATE` по умолчанию работает по изменённой области, а не по всему репозиторию:

```text
previous baseline A
  -> current baseline B
  -> change inventory
  -> impact analysis
  -> LOCAL | BOUNDARY | SYSTEMIC
  -> minimum dependency slice
  -> targeted fresh evidence
  -> revalidation / adjudication
  -> delta reconciliation
```

`LOCAL` означает локальное изменение без пересечения существенных контрактов. `BOUNDARY` затрагивает API, auth, persistence, lifecycle, concurrency, ownership, IPC или другую архитектурную границу и требует расширить только соответствующий As-Built/evidence slice. `SYSTEMIC` означает, что изменение затронуло фундаментальную архитектурную модель.

Даже при `SYSTEMIC` Skill не должен сам превращать `REVALIDATE` в новый полный аудит. Он возвращает `FULL_REAUDIT_RECOMMENDED`, а решение остаётся за пользователем.

Если для корректного решения не хватает материала, используется `CONTEXT_EXPANSION_REQUIRED` с конкретной причиной и точным предложением, какой dependency slice нужно дочитать. Diff, список изменённых файлов и Project Profile помогают выбрать evidence, но не заменяют substantive proof.

Сохранённая область (`preserved`) означает только то, что impact analysis не обнаружил зависимости, требующей свежей проверки. Это не новая верификация и не новый GREEN.

### Project Profile

При старте Skill собирает дешёвый локальный Project Profile для маршрутизации и оценки объёма проекта. Это metadata, а не архитектурное доказательство.

Профиль включает:

- количество substantive tracked files;
- строки;
- символы;
- языковой footprint;
- отдельные категории generated, vendor/dependency, build artifacts и binaries.

Неизвестный текстовый тип учитывается как `Other Text`. Профиль считается локально и не требует отправлять содержимое каждого файла в LLM-контекст только ради статистики.

Project Profile versioned и привязан к baseline/revision. Старый audit package без профиля может получить `METADATA_BACKFILL` без открытия уже принятых технических gates. Если исторический Git baseline недоступен, фиксируется `HISTORICAL_PROFILE_UNAVAILABLE`: текущий профиль всё равно может быть собран, а технический аудит не становится недействительным только из-за отсутствия старой статистики.

При `REVALIDATE` профили старого и нового baseline могут использоваться для компактной delta по files, lines, characters и languages.

### Dirty working tree

Если рабочее дерево изменено, рекомендуемый reproducible baseline — точный committed `HEAD`.

Skill показывает явный выбор:

```text
1. Audit committed HEAD only — recommended
2. Include working-tree changes as EPHEMERAL snapshot
3. Stop
```

`EPHEMERAL` фиксирует commit, baseline type и детерминированный `working_tree_snapshot` с версией алгоритма. Такой baseline не должен представляться как обычная воспроизводимая Git-ревизия.

## Что именно проверяет Architecture Review

В зависимости от проекта аудит охватывает:

- архитектурные границы и распределение ответственности;
- владение состоянием, ресурсами и жизненным циклом;
- запуск, штатную работу, восстановление, переподключение, отмену операций и завершение работы;
- конкурентное выполнение и фоновые процессы;
- контракты между API, IPC, frontend/backend и native-слоями;
- безопасность и границы доверия;
- конфигурацию и хранение данных;
- обработку ошибок и наблюдаемость;
- сопровождаемость и тестируемость;
- существующую систему тестов — через отдельную capability **Test Review**;
- целевую архитектуру и план исправлений, если они явно запрошены.

Для некоторых технологий есть дополнительные stack addenda: Tauri, Electron, React, Django, FastAPI, Litestar и Ansible. Они добавляют специализированные вопросы к аудиту, но не заменяют общую методологию.

Ansible здесь именно stack addendum, а не отдельная capability.

## Чем этот подход отличается от обычного code review

Обычный review легко скатывается в набор локальных замечаний: большой файл, `TODO`, mock, `unwrap`, широкая функция, отсутствие теста, странный `clone`, неидеальная структура каталогов.

Само по себе это ещё не дефект.

`architecture-code-review` требует доказать цепочку:

```text
фактическое поведение
    ↓
конкретный механизм
    ↓
нарушенный контракт или архитектурная граница
    ↓
реальное последствие
    ↓
подтверждённый finding
    ↓
severity
```

Поэтому критичность назначается **после** проверки корректности finding, а не по первому впечатлению.

Для серьёзных security-выводов недостаточно написать «это небезопасно». Нужна правдоподобная attack chain: кто атакует, через какую поверхность, при каких предпосылках и к какому результату это приводит.

## Как устроен новый полный аудит

После Start Gate и выбора `NEW` базовый архитектурный поток выглядит так:

```text
baseline
  -> As-Built Architecture
  -> independent As-Built review
  -> thematic discovery
  -> Discovery Coverage review
  -> candidate verification
  -> root-boundary adjudication
  -> severity adjudication
  -> authoritative findings ledger
  -> optional Target Architecture
  -> optional remediation roadmap
  -> final package assembly
  -> editorial review / correction / re-review
```

### 1. As-Built Architecture

До поиска проблем агент должен понять фактическую систему: основные компоненты, процессы, владельцев состояния, ключевые границы, потоки данных и важные сценарии выполнения.

Это не пересказ README проекта и не предположение по именам директорий. Архитектурные утверждения должны опираться на реальные пути исполнения и конкретные участки кода.

As-Built проходит отдельную независимую проверку. Автор архитектурной реконструкции не может сам объявить её принятой.

### 2. Discovery

После принятия As-Built исследуются значимые области: lifecycle, ownership, concurrency, persistence, API/IPC-контракты, security, error handling и другие применимые механизмы.

Discovery создаёт кандидатов на проблемы, но ещё не окончательные findings.

### 3. Discovery Coverage

Полнота аудита не измеряется количеством просмотренных файлов, найденных замечаний или зелёных тестов.

Перед общим выводом формируется ограниченный перечень существенных областей и механизмов в заявленном scope. Для каждого должно быть понятно, чем он покрыт, почему неприменим либо почему остался неизвестным.

Independent Coverage Review проверяет эту матрицу отдельно. Если есть пробел, выполняется точечное доисследование, а не автоматический перезапуск всего аудита.

### 4. Independent candidate verification

Кандидат должен выдержать проверку на достижимость, фактическое владение, существующие guards, альтернативные пути и конкретное последствие.

После этого выполняется root-boundary adjudication: определяется, является ли наблюдение самостоятельной корневой проблемой, проявлением уже найденной причины или лишь сопутствующим инженерным риском.

Только после этой стадии назначается severity.

## Глубина Architecture Review

### `STANDARD_FULL`

Полный архитектурный аудит с обязательной реконструкцией As-Built, проверкой полноты, независимой верификацией кандидатов и финальной проверкой отчёта.

Это нормальный выбор для большинства production-репозиториев.

### `FORENSIC`

Более глубокое расследование для сложных случаев: нескольких процессов, тонкой конкурентности, восстановления после сбоев, сложных trust boundaries, неоднозначной архитектуры или трудно воспроизводимых дефектов.

Skill может рекомендовать `FORENSIC`, но не должен выбирать его молча.

## Architecture Review endpoint

Глубина аудита и итоговый результат выбираются независимо.

### `REVIEW_ONLY`

Архитектурный аудит и authoritative findings ledger.

### `REVIEW_PLUS_TARGET_ARCHITECTURE`

Дополнительно строится Target Architecture — целевое устройство системы с учётом подтверждённых findings, уже работающих механизмов и явных продуктовых ограничений.

### `REVIEW_PLUS_TARGET_AND_ROADMAP`

Дополнительно создаётся remediation roadmap: порядок исправлений, зависимости между изменениями и проверка того, что этот порядок архитектурно согласован.

Сам по себе `FORENSIC` не означает, что обязательно нужны Target Architecture или Roadmap.

## Test Review

Architecture Review — основной umbrella workflow. **Test Review** подключается как отдельная capability.

Её можно:

- выбрать сразу в Review Suite Configuration;
- подключить по рекомендации discovery, если в проекте есть существенная поверхность автоматизированных тестов;
- добавить позже через `EXTEND`.

Test Review отвечает не на вопрос «тесты зелёные или нет», а на более строгий вопрос:

> Какие существенные контракты системы действительно подтверждены исполняемыми тестами, какие подтверждены частично, какие не подтверждены и какие тесты могут создавать ложное чувство уверенности?

При этом Test Review ведёт собственный bounded inventory проверяемых контрактов. Архитектурная Discovery Coverage Matrix и матрица Test Review не подменяют друг друга.

Endpoint Test Review выбирается независимо от архитектурного endpoint и может быть `REVIEW_ONLY` или `REVIEW_PLUS_TEST_PLAN`.

Подключение Test Review позже не означает автоматический перезапуск уже принятых частей архитектурного аудита. Capability получает только тот объём актуального контекста, который нужен для её собственных решений.

## Общие assurance-принципы

**Сначала authority, потом verdict.** Если два значимых источника противоречат друг другу и непонятно, какой из них имеет приоритет, нельзя произвольно выбрать более свежий, удобный или похожий на истину. До разрешения authority-конфликта результат остаётся `UNKNOWN / AUTHORITY_UNRESOLVED`.

**Нельзя расширять вывод дальше доказанной области.** Узкая проверка даёт узкий вывод.

**Полнота требует bounded accounting.** Для общего вывода нужен явный учёт всех существенных целей в заявленном scope. Выборочное глубокое исследование допустимо; случайная выборка не является доказательством полноты.

**Отвергнутый механизм не должен унести с собой отдельный существенный контракт.** Если внутри слабого кандидата обнаружен реальный архитектурный или поведенческий вопрос, он получает собственную disposition и не исчезает вместе с исходным smell.

Эти правила зафиксированы в `references/shared-assurance-principles.md`.

## Состояние длинного review

Для больших аудитов используется `working/INDEX.md`. Это сохраняемое состояние workflow: что принято, что требует проверки, что устарело и что блокирует следующий этап.

Типичные состояния:

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

Артефакт со статусом `REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED` или `BLOCKED` нельзя использовать дальше как уже подтверждённую истину.

`INDEX.md` — workflow projection/state authority, но не substantive technical authority. Сводка или handoff также не получает автоматический приоритет над исходным техническим артефактом: перед использованием проверяется её свежесть и привязка к актуальной ревизии.

## Итоговые артефакты

По умолчанию пакет аудита создаётся в:

```text
docs/reviews/architecture-review/
```

Для полного сценария структура обычно выглядит так:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md       # если запрошена
├── 04-remediation-roadmap.md       # если запрошен
└── working/
    └── ... промежуточные evidence и review-артефакты
```

Финальный отчёт предназначен для человека. В нём должно быть понятно: **что происходит → почему это проблема → к чему приводит → что менять**.

Внутренние IDs, ledger rows и handoff-сокращения используются для трассировки и координации, но не должны подменять нормальное техническое объяснение.

## Установка

### OpenCode, Codex и другие агенты, использующие `~/.agents/skills`

Клонируйте репозиторий в каталог персональных skills:

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

После установки начните новую сессию агента, чтобы он заново обнаружил skill на диске.

Если репозиторий уже установлен:

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git pull --ff-only
```

Проверить установленную ревизию:

```bash
cd ~/.agents/skills/architecture-code-review
git rev-parse HEAD
```

Если для воспроизводимости используется конкретный release tag:

```bash
cd ~/.agents/skills/architecture-code-review
git fetch --tags
git checkout <release-tag>
```

Вернуться на актуальный `main`:

```bash
git switch main
git pull --ff-only
```

## Использование

Откройте новую сессию агента в репозитории, который нужно проверить, и явно попросите использовать skill.

Минимальный запрос:

```text
Используй architecture-code-review для этого проекта.
```

Дальше Skill сам проверит наличие предыдущего audit package и предложит подходящий Session Intent.

Если вы точно хотите новый полный аудит, можно сказать явно:

```text
Используй architecture-code-review.
Начни NEW аудит этого проекта.
```

Если нужен полный аудит с целевой архитектурой и roadmap:

```text
Используй architecture-code-review.
Начни NEW аудит. Нужны Architecture Review, Target Architecture и remediation roadmap.
```

Если нужно проверить, что изменилось после уже принятого аудита:

```text
Используй architecture-code-review.
Проверь предыдущий audit package и предложи REVALIDATE для текущего HEAD.
```

Если хочется добавить Test Review к существующему аудиту:

```text
Используй architecture-code-review.
EXTEND существующий аудит: добавь Test Review.
```

Даже если prompt заранее подсказывает желаемое направление, выбранный Session Intent и Review Suite Configuration должны быть явно reconciled и записаны в `working/INDEX.md`.

## Структура репозитория

```text
.
├── README.md
├── LICENSE
├── SKILL.md                         # компактный umbrella orchestrator
├── capabilities/
│   └── test-review/
│       └── SKILL.md                 # методология Test Review
├── references/
│   ├── session-orchestration.md     # Start Gate, Session Intent, Project Profile
│   ├── review-modes-and-orchestration.md
│   ├── revalidation-and-freshness.md
│   ├── shared-assurance-principles.md
│   ├── review-method.md
│   ├── discovery-coverage.md
│   ├── ownership-and-scenarios.md
│   ├── boundary-contract-audit.md
│   ├── independent-verification.md
│   ├── root-boundary-adjudication.md
│   ├── evidence-and-severity.md
│   ├── lifecycle-and-mermaid.md
│   ├── report-contract.md
│   ├── target-architecture-review.md
│   ├── remediation-roadmap-review.md
│   ├── final-editorial-review.md
│   └── stacks/
│       ├── ansible.md
│       ├── django.md
│       ├── electron.md
│       ├── fastapi.md
│       ├── litestar.md
│       ├── react.md
│       └── tauri.md
├── tests/                            # pressure scenarios и validation records
└── docs/
    └── superpowers/                  # design и implementation-документы
```

`SKILL.md` намеренно остаётся компактным orchestrator. Startup/session policy живёт в `references/session-orchestration.md`, execution workflow и capability state — в `references/review-modes-and-orchestration.md`, а freshness/project-change evidence semantics — в `references/revalidation-and-freshness.md`.

## О validation

В `tests/` хранятся pressure scenarios и записи отдельных validation-проходов. Они нужны для проверки конкретных изменений методологии и поведения агента.

Validation record относится к той ревизии и тому сценарию, для которых он был получен. Его нельзя автоматически трактовать как вечное доказательство для любого будущего `main`.

README намеренно не публикует одно общее число вроде «N/N scenarios PASS» как универсальный текущий статус всего Skill. Для проверки конкретного изменения нужно смотреть соответствующий validation record и его revision binding.

Если executable coordinator/collector отсутствует, runtime pressure result может оставаться `INCONCLUSIVE`. Static/contract verification в таком случае не должен называться runtime GREEN.

## Разработка

Изменение инструкций Skill считается изменением поведения, даже если технически это Markdown.

Для существенных изменений используется дисциплина:

```text
design
  -> implementation plan
  -> isolated implementation
  -> independent review
  -> pressure / real-world validation where applicable
  -> remediation
  -> promotion readiness
  -> merge to main
```

Новая capability должна иметь собственную область ответственности и собственный authoritative artifact. Общая методология не должна без необходимости дублироваться внутри неё.

Stack addendum, наоборот, остаётся дополнением для конкретной технологии и не превращается в capability только потому, что для него появился отдельный файл.

## Язык итоговых отчётов

Пользовательские документы по умолчанию пишутся нормальным русским техническим языком.

Точные идентификаторы кода, пути, названия API/IPC, протоколы, имена файлов и формальные status tokens не переводятся. Английский термин можно оставить там, где он является устойчивым названием понятия — например `As-Built`, `Test Review`, `finding` или `root-boundary adjudication` — но финальный текст не должен превращаться в смесь английских слов с русскими окончаниями.

## Лицензия

См. `LICENSE`.
