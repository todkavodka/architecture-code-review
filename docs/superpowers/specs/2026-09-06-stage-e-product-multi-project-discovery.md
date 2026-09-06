# Stage E — Product / Multi-Project Review: Discovery

**Дата:** 2026-09-06

**Тип документа:** Discovery, не Design и не implementation plan

**Базовая ревизия:** `63bef65c765d0a381b63a7b4fdffe1679d89eee5`
**Ветка:** `main`

## Резюме

Текущая модель убедительно описывает один review target: выбранный baseline,
рабочие области доказательств `WS-*`/`EV-*`, фактическую семантическую модель
STM, независимые модули `Architecture Review`, `Test Engineering` и `Code
Quality Review`, а также производные проекции и пакеты. Она не содержит
принятой семантики Product, членства нескольких Projects или вектора
межрепозиторных ревизий.

Рекомендуемое направление для следующего Design — вариант C, гибрид:

```text
необязательная Product identity/membership с revision/history, при этом
необходимость постоянного Product aggregate должна быть доказана в Design
        + независимые Project authority и локальные пакеты
        + минимальный слой межпроектных фактов/связей и влияния
        + продуктовые проекции из принятых источников
```

Product не становится обязательным родителем обычного аудита. Project не
сливается с репозиторием, review target или рабочей областью. Новая
межпроектная семантика не должна появляться простым объединением проектных
отчётов. Точный формат Product/Project identity, политика членства,
частичного baseline, владелец продуктовых интерпретаций и способ хранения
межпроектных фактов требуют отдельного Design.

## Проверенный базис и источники

Состояние перед Discovery:

```text
branch: main
HEAD: 63bef65c765d0a381b63a7b4fdffe1679d89eee5
origin/main: 63bef65c765d0a381b63a7b4fdffe1679d89eee5
tracked tree: clean
```

Сохранены ранее существовавшие неотслеживаемые файлы. Прочитаны или
использованы как семантические источники:

- дорожная карта и границы этапа E — [`docs/roadmap.md`](../../roadmap.md);
- координация, baseline, intent и независимый выбор модулей —
  [`references/session-orchestration.md`](../../../references/session-orchestration.md)
  и [`references/review-modes-and-orchestration.md`](../../../references/review-modes-and-orchestration.md);
- общие доказательства —
  [`references/shared-evidence-model.md`](../../../references/shared-evidence-model.md);
- STM и фактическое владение техническими фактами —
  [`references/shared-technical-model.md`](../../../references/shared-technical-model.md);
- прямые зависимости, типы связей и bounded impact traversal —
  [`references/technical-model-dependencies.md`](../../../references/technical-model-dependencies.md);
- повторная проверка, preserved set и классы `LOCAL`/`BOUNDARY`/`SYSTEMIC` —
  [`references/revalidation-and-freshness.md`](../../../references/revalidation-and-freshness.md);
- жизненный цикл, влияние, пересборка, проверка и пакеты проекций —
  [`references/projection-lifecycle.md`](../../../references/projection-lifecycle.md),
  [`references/projection-impact.md`](../../../references/projection-impact.md),
  [`references/projection-regeneration.md`](../../../references/projection-regeneration.md),
  [`references/projection-gates-and-packages.md`](../../../references/projection-gates-and-packages.md);
- архитектурное владение и корневая граница —
  [`references/review-method.md`](../../../references/review-method.md),
  [`references/ownership-and-scenarios.md`](../../../references/ownership-and-scenarios.md),
  [`references/root-boundary-adjudication.md`](../../../references/root-boundary-adjudication.md),
  [`references/target-architecture-review.md`](../../../references/target-architecture-review.md)
  и [`references/remediation-roadmap-review.md`](../../../references/remediation-roadmap-review.md);
- Test Engineering — [`capabilities/test-review/SKILL.md`](../../../capabilities/test-review/SKILL.md)
  и [`test-engineering-contract.md`](../../../capabilities/test-review/references/test-engineering-contract.md);
- Code Quality — [`capabilities/code-quality-review/SKILL.md`](../../../capabilities/code-quality-review/SKILL.md),
  [`code-quality-contract.md`](../../../capabilities/code-quality-review/references/code-quality-contract.md),
  [`code-quality-lifecycle.md`](../../../capabilities/code-quality-review/references/code-quality-lifecycle.md)
  и [`code-quality-projection.md`](../../../capabilities/code-quality-review/references/code-quality-projection.md).

В `docs/roadmap.md` Stage D всё ещё помечен `PLANNED`; это устаревшее метаданное
состояние, не основание пересматривать завершённый Stage D. Синхронизацию
дорожной карты следует выполнить в отдельном checkpoint после Design и
promotion Stage E; этот Discovery файл её не меняет.

## Текущая модель одного проекта

### Слои и владение

```text
repository/path/ref + dirty state
        ↓
selected baseline and Project Profile
        ↓
WS-* / EV-* shared evidence
        ↓
STM factual technical authority
        ↓
Architecture Review → RF-*
Test Engineering → BC-* / CC-* / MAT-* / TM-* / GAP-* / TASK-*
Code Quality Review → CQ-* / CQRA-*
        ↓
PRJ-* projections → named gate-scoped package
```

`WS-*`/`EV-*` фиксируют наблюдения и происхождение, но не являются выводами.
STM принимает факты семейств `COMP-*`, `IF-*`, `INT-*`, `DS-*`, `EVENT-*`,
`FLOW-*`, `AUTH-*`, `CFG-*`, `ERR-*`. Модули интерпретируют факты каждый в своей
области; проекция не получает право записи в источник смысла. Прямые
зависимости принадлежат артефактам, а индексы являются воспроизводимыми
навигационными проекциями.

### Baseline, актуальность и процесс

Текущая модель привязывает доказательство и семантическую запись к выбранной
базовой ревизии. `REVALIDATE` связывает прежнюю принятую ревизию с текущей,
определяет влияние и читает минимальный затронутый срез. `LOCAL`, `BOUNDARY` и
`SYSTEMIC` — классы влияния; `SYSTEMIC` может вернуть
`FULL_REAUDIT_RECOMMENDED`, но это не автоматический полный аудит.

`EXTEND` добавляет только запрошенный объём. `PROJECTION_REPAIR` исправляет
только представление от неизменённого принятого источника; смысловое
расхождение останавливает его и требует технической повторной проверки.
`PRJ-*` и `RG-*` различны, а анализ влияния на проекции не запускает
пересборку неявно. Пакет использует явный выбор, замыкание зависимостей и
политику `PERMISSIVE`, `REQUIRED_SCOPE_CURRENT` или `ALL_SCOPED_CURRENT`.

### Ограничение текущей модели

В контрактах встречаются `repository_identity`, `repository/path/ref`,
`Project Profile`, selected scope и repository-scoped `CQ-*`, но нет
устойчивого Product identity, явного Project aggregate или baseline-вектора
из нескольких репозиториев. Нельзя считать репозиторий Product, а файл,
workset, package или `working/INDEX.md` — Project identity.

## Выявленная Stage E проблема

Продукт может состоять из нескольких логических проектов и общих компонентов:

```text
Product
├── Project A
├── Project B
├── Project C
└── Shared Components / Infrastructure
```

Нужно отвечать на вопросы о совместимости, владении, влиянии и архитектурных
границах между ними, не нарушая single-project operation. Главные опасные
смешения:

| Неверное отождествление | Почему оно опасно |
|---|---|
| Product = Project | Любой обычный аудит стал бы обязан иметь продуктового родителя. |
| Project = repository | Монорепозиторий, несколько сервисов и один проект из нескольких репозиториев теряют смысл. |
| Product baseline = один Git SHA | Нельзя точно связать межпроектный вывод с разными состояниями источников. |
| Product finding = сумма отчётов | Межпроектная интерпретация и новое последствие остаются недоказанными. |
| relation = dependency | Фактическая связь начинает неявно управлять impact traversal. |
| projection = authority | Сводный документ превращается в скрытый продуктовый semantic owner. |

## Product identity и Project identity

### Product

**Discovery constraint:** Product — необязательная логическая область
агрегации, если система поддерживает продуктовый режим. Он не является
универсальным semantic owner и не требуется для `NEW` single-project review.
Любой Product context, используемый для принятого межпроектного вывода,
должен быть адресуемым и revision/history aware; изменившийся состав не
должен переписывать прошлый baseline.

Вариант C предполагает как рабочее направление устойчивую Product
identity/membership с историей, но это ещё не доказанная необходимость
persistent Product aggregate. Baseline-bound `WS-*`/`EV-*`, STM и capability
records уже дают provenance своих ревизий. Design должен доказать, какие
гарантии membership continuity, последующего `REVALIDATE` и исторической
идентификации package требуют отдельной долговечной Product identity, а какие
могут быть обеспечены revision-bound Product context. Никакая выбранная форма
не должна делать Product обязательным родителем Project или передавать Product
универсальное semantic ownership.

**Design decisions required:**

- точный формат и namespace Product identity;
- создаётся ли Product только явным пользователем или допускается обнаружение
  кандидата из манифеста/координации;
- допустима ли Product только с одним Project;
- может ли один Project входить в несколько Products и какие ограничения
  предотвращают циклы или противоречивое членство;
- кто принимает смысл membership и кто имеет право его изменить;
- какие ревизии Product сохраняются при добавлении, удалении или замене
  Project.

### Project

**Discovery resolved:** нужен явный логический Project context для межпроектной
работы. `repository_identity` остаётся важным источником происхождения, но
не исчерпывает Project identity. Один repository может содержать несколько
Projects (например, монорепозиторий), а один Project может включать несколько
репозиториев. Review target — выбранная область Project, а workspace/review
session — временная координация, не identity.

**Design decisions required:**

- stable Project identity при смене URL, локального пути, ветви или состава
  репозиториев;
- представление монорепозитория и нескольких сервисов внутри него;
- допустимая кардинальность `Project ↔ repository`;
- привязка Project identity к revision без превращения revision в identity;
- граница между Project Profile, review target и Project semantic authority.

## Membership и baseline

### Членство

Членство должно быть явным, версионируемым и адресуемым. Запись Product
membership не должна вычисляться из имён каталогов, произвольных glob или
текстовых отчётов. Для каждого члена понадобятся как минимум Project identity,
роль в продукте, источник членства, дата/ревизия принятия и состояние
доступности. Использование общего компонента — отдельная связь и не передаёт
ему ownership.

Точный реестр Product membership, возможность многократного членства и
политика удаления — `DESIGN_DECISION_REQUIRED`.

### Product baseline

Минимальная безопасная форма — вектор ревизий, а не один SHA:

```text
Product Baseline P-17
├── Project A @ repository-a / revision X
├── Project B @ repository-b / revision Y
├── Project C @ repository-c / revision Z
└── shared infrastructure @ source Q
```

Каждая запись должна сохранять способ получения ревизии, branch/ref или dirty
marker, Project Profile, доступность источника и связь с доказательствами.
Межпроектный вывод привязывается к полному набору contributing revisions,
а не только к репозиторию, где он был записан.

**Resolved constraints:** отсутствие репозитория, грязное отслеживаемое дерево,
плавающая revision или недоступный внешний контракт нельзя скрывать; такие
ограничения попадают в `limitations`, unavailable scope и freshness/coverage.
Vector baseline — безопасное направление для полной provenance, но не
завершённая модель принятия baseline.

**Design decisions required:** можно ли принять частичный Product baseline;
как отдельно представляются source availability, review coverage, semantic
conclusion availability, projection freshness и package gate при недоступном
обязательном Project; допускается ли смешанный committed/dirty vector; как
фиксируется момент согласованного снимка, если Project B продвинулся после
проверки Project A.

## Межпроектные доказательства

Project-local evidence и cross-project inference различаются:

```text
Project A WS-* / EV-* ─┐
                       ├─ cross-project observation/adjudication ─→ product claim
Project B WS-* / EV-* ─┘
```

`WS-*` может оставаться локальной рабочей областью каждого Project. Для
наблюдения, которое прямо сопоставляет provider и consumer, понадобится
адресуемая запись с несколькими source bindings и полным Product baseline либо
явная межпроектная workset-запись. Она должна ссылаться на конкретные `EV-*`,
внешние контракты, API/client views, deployment facts и revisions.

**Resolved constraint, not resolved authority:** cross-project claim не может
строиться из объединённых отчётов, но Discovery не выбирает форму новой
адресуемой записи. Design должен определить, остаётся ли она расширением
наблюдения `WS-*`/`EV-*`, принимаемым STM fact/relation, или capability-owned
interpretation с multi-source provenance. Design также должен определить
owner/writer, lifecycle, acceptance gate, coherent baseline binding и conflict
handling. Это не разрешает создавать новую evidence authority по умолчанию.

Доказательство совместимости provider/consumer не следует из того, что два
проекта упомянуты в одном отчёте. Нужны наблюдаемые представления
`DECLARED`/`IMPLEMENTED`/`CONSUMED`/`TESTED`, подтверждённая зависимость и
решение владельца спорного контракта. Product-level claim сохраняет все
исходные Project-local evidence и отдельную интерпретацию; исходный отчёт не
становится evidence authority.

## Межпроектный STM и зависимости

### STM

Существующие семейства STM способны описывать компоненты, интерфейсы,
взаимодействия, события, потоки, конфигурацию и границы, относящиеся к разным
Projects, если их идентичности и provenance получают явный Project/baseline
context. Например, `IF-*` provider и consumer, `INT-*` вызов между ними и
`AUTH-*` граница могут оставаться фактами STM.

**Discovery recommendation:** не вводить новую factual authority или новый
семейство фактов только для Product. Сначала исследовать additive extension
метаданных владельца/области и межпроектных ссылок в STM. Если существующий
контракт не может выразить relation с несколькими Project identities и
revision bindings, Design должен предложить узкий relation/index layer,
который не принимает STM facts. Форма, owner и acceptance boundary такого
слоя остаются Design decisions; его нельзя считать cross-project evidence
authority только потому, что он адресует несколько источников.

### Dependency != relation

Факт `CALLS`, `CONSUMES`, `PUBLISHES`, `DEPENDS_ON`, `DEPLOYS_AS` или другой
допустимой STM relation описывает техническую связь. Direct dependency metadata
определяет семантическую предпосылку и маршрут влияния (`HARD`, `CONDITIONAL`,
`INFORMATIONAL`). Межпроектное упоминание не делает зависимость автоматически.

Следует отдельно фиксировать тип зависимости:

| Область | Что нужно доказать |
|---|---|
| Runtime/API | Реальный вызов, интерфейс и версия/контракт ответа. |
| Build | Манифест, lockfile или иной источник сборочной зависимости. |
| Data | Совместное хранилище, схема, миграция или формат данных. |
| Event | Публикация, подписка, schema и delivery contract. |
| Deployment | Развёртывание, конфигурация и порядок/граница запуска. |
| Compatibility | Сопоставимые provider/consumer views и проверка допустимого диапазона. |
| Shared library/SDK | Фактическая поставка и потребление конкретной версии. |

Exact direct edge остаётся owned by the dependent artifact. Generated indexes
помогают найти candidate reverse edges, но не становятся authority.

## Shared Components и ownership

Shared database, broker, authentication service, SDK, common library и
deployment infrastructure могут быть:

1. Project-owned и используемыми другими Projects;
2. Product-owned только если отдельный принятый процесс действительно владеет
   его техническим смыслом;
3. External, когда источник и управление находятся вне продукта.

Usage, `CONSUMES` и dependency не означают ownership. Нельзя создать
Product-owned компонент лишь для удобства сводки. Для каждого shared component
нужны source, owner/writer, consumer Projects, baseline/revision и evidence
доступности. Ownership conflict направляется владельцу STM или Architecture
Review в зависимости от того, о факте или интерпретации идёт речь.

## Product-level findings и Architecture Review

`RF-*` остаётся архитектурной интерпретацией владельца `Architecture Review`.
На Discovery нет основания вводить новую семью идентификаторов. Product-level
`RF-*` может быть выражен с явным Product scope, если Design подтвердит, что
существующий контракт поддерживает scope и multiple-baseline provenance.

Обязательная цепочка:

```text
Project A / Project B evidence
  → accepted cross-project STM facts and dependency context
  → independent product-level interpretation
  → RF-* with Product scope, affected Projects and full provenance
```

Project finding не становится Product finding автоматически. Два локальных
`RF-*` могут быть коррелированы, но это не создаёт общего Product finding без
нового межпроектного механизма и доказанного общего последствия. Product
finding обязан иметь affected Projects, contributing revisions, owner,
severity/lifecycle rules, evidence, dependencies и projection behavior.

Требуется Design-решение о том, является ли Product scope полем существующего
`RF-*` или потребуется отдельная authority record без новой семантики
«продуктового root finding».

## Product-level Code Quality

`CQ-*` и `CQRA-*` остаются owned by `Code Quality Review`; действующий контракт
связывает finding с repository-scoped stable allocation и selected scope.

Разрешённые направления:

- Product projection может агрегировать Project-local `CQ-*` как навигацию,
  сохраняя identity, lifecycle, disposition, severity и confidence каждого
  finding;
- повторяющийся межпроектный механизм может дать Product-level candidate, но
  требуются новые evidence, material consequence и отдельная adjudication;
- `CQRA-*` одного Project не закрывает finding другого Project и не создаёт
  продуктовую remediation action автоматически.

**Design decisions required:** Product Code Quality interpretation остаётся
владением `Code Quality Review` с новым Product scope либо это отдельная
Architecture Review interpretation; как сохраняется repository-scoped CQ
identity при межпроектном паттерне; нужна ли продуктовая action-запись или
достаточно нескольких Project-local `CQRA-*`. Простая сумма Hotspots — только
projection, не semantic finding.

## Product-level Test Engineering

Семейства `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*` не требуют новых
идентификаторов только потому, что provider и consumer находятся в разных
Projects. Контракт должен привязать `BC-*` к поведению и к revision bindings
provider, consumer и declared/implemented views; `CC-*` — к сравниваемым
представлениям; `MAT-*`/`TM-*`/`GAP-*`/`TASK-*` — к доказательству, покрытию и
работе по устранению.

Product Test Assurance может быть производной проекцией совокупности принятых
Project and cross-project records. Она не становится Behavior Model authority.
Cross-project E2E, simulator и environment design остаются отдельными
выбираемыми результатами с явной authorization; наличие Product не запускает
их выполнение.

**Design decisions required:** когда cross-project behavior получает отдельный
`BC-*` scope, когда остаётся relation между Project-local `BC-*`; кто владеет
Product assurance summary; какие `GAP-*` относятся к отсутствию provider,
consumer, совместимости или сквозного доказательства; какие обязательные
члены получает продуктовый пакет.

## Version и compatibility analysis

Совместимость — не одно числовое поле «current version». Версия и конфигурация
могут быть фактом STM/обязательным источником, а допустимость сочетания —
выводом или проверенным контрактным сопоставлением. Для набора вроде
Frontend v4 + API v7 + SDK v3 нужны:

- точные Project revisions и version/configuration bindings;
- provider/consumer contract views;
- заявленный supported range или другой источник политики;
- observed compatibility evidence и baseline;
- владелец решения при конфликте объявленного и реализованного поведения.

Матрица версий может быть Product projection или controlled input, но не должна
автоматически создавать finding. Stale compatibility evidence требует
impact-driven revalidation затронутых Project/contract records. Точный формат
матрицы и owner adjudication — `DESIGN_DECISION_REQUIRED`; compatibility engine
не входит в Discovery.

## Product REVALIDATE и EXTEND

### `REVALIDATE`

Product revalidation расширяет текущий impact-driven процесс, не заменяя его:

```text
Project B changed at revision Y2
        ↓
direct cross-project dependency impact
        ↓
affected provider/consumer contracts and Project A records
        ↓
affected Product interpretation/projections
        ↓
minimum semantic revalidation slice
```

Изменение Project B не означает полный Product audit. Сначала проверяются
direct metadata, cross-project edges, affected `EV-*`/STM and capability
records. Project-local revalidation достаточна, если доказано отсутствие
межпроектного impact. Product scope добавляется при `HARD`/`CONDITIONAL`
dependency, изменении shared boundary, product membership или cross-project
semantic fact. Однако Discovery не утверждает, что Product-local
revalidation достаточна без accepted dependency state, который доказывает
отсутствие межпроектного impact. `SYSTEMIC` может вернуть
`FULL_REAUDIT_RECOMMENDED`; решение остаётся явным.

Design должен определить Product impact root, хранение multi-project
traversal, baseline coherency, impact membership-change, propagation of
partial/unavailable Projects, preserved-set behavior across Projects и точную
границу `LOCAL`/`BOUNDARY`/`SYSTEMIC` на Product scope. Существующие
preserved-set и `CONTEXT_EXPANSION_REQUIRED` правила должны применяться, а не
заменяться полным чтением всех репозиториев. Minimum necessary work остаётся
обязательным; полный Product reread не является default.

### `EXTEND`

`EXTEND` сохраняет принятую конфигурацию и добавляет только запрошенное:

```text
add Project D
add shared component
add Product Architecture Review
add Product Test Assurance
add cross-project output
```

Добавление Project D не открывает заново непричастные Project A–C findings.
Это additive `EXTEND` constraint, а не решение Product membership semantics.
Изменение membership, которое меняет Product meaning, требует отдельного
membership adjudication и затем адресного revalidation; оно не маскируется
как обычное добавление проекции. Design должен определить, как такая
membership revision меняет Product baseline, package membership snapshot,
direct impact roots, preserved set и Product interpretations, а также отличить
добавление выбранного Project от изменения requiredness или смысла существующего
члена.

## Partial availability и dirty state

### Недоступность

Product review может продолжаться частично только с явным `PARTIAL`/`BLOCKED`
охватом и раскрытыми ограничениями. Недоступный Project не считается чистым,
проверенным или сохранённым по умолчанию. Product projection может быть
частичной, если её контракт допускает такую область; обязательный отсутствующий
член может блокировать только соответствующий gate/package после Design-решения
о resolved membership и package policy.

Эти слова не вводят универсальный Product lifecycle/status enum. Design должен
раздельно определить и связать с существующими контрактами: (1) source
availability, (2) review coverage, (3) availability of semantic conclusions,
(4) projection availability/freshness и (5) package gate result. Отсутствие
Project не блокирует автоматически каждый Product output или независимый
Project gate; оно блокирует только claims и package gates, для которых
отсутствующий scope является явно обязательным. `PARTIAL`/`BLOCKED` здесь —
bounded descriptions до Design, а не принятый Product status.

Нельзя делать finding из отсутствия исходника. Нужно сохранить unavailable
scope, попытку доступа, baseline expectation и минимальное действие для
расширения контекста.

### Грязное или неканоническое состояние

Текущие контракты различают committed baseline, dirty baseline, detached HEAD,
ветвь/ref, локальные коммиты, missing remote и untracked files. Stage E должен
перенести эту дисциплину на каждый Project:

| Состояние | Discovery-ограничение |
|---|---|
| Чистый committed repo | Нормальный revision-bound evidence. |
| Dirty tracked state | Явный dirty baseline и точные file/content bindings; политика принятия — Design decision. |
| Только untracked files | Не удалять; не считать частью baseline без явного выбора. |
| Detached HEAD | Сохранить точный commit и отсутствие branch identity. |
| Local-only commits | Зафиксировать ref/commit и невозможность считать его remote canonical. |
| Missing remote | Не угадывать provenance или публикацию; состояние может быть local-only. |
| Разные branches/worktrees | Каждая Project revision и рабочая область должны быть адресуемыми отдельно. |

Automatic cleanup, branch switching, cloning и worktree removal не входят в
Discovery или будущую неявную политику.

## Проекции и пакеты

### Кандидаты Product outputs

| Кандидат | Возможный semantic owner | Источник | Характер |
|---|---|---|---|
| Product Architecture Review | `Architecture Review` | Product-scoped accepted STM, cross-project evidence и Product `RF-*` | Projection; требует явного Product scope и достаточного cross-project authority. |
| Cross-Project Dependency View | STM/dependency owners | accepted relations и direct dependency metadata | Projection; generated index не становится authority. |
| Product Target Architecture | `Architecture Review` target owner | accepted Product findings/invariants | Projection; requires target selection and independent target review. |
| Product Remediation Roadmap | roadmap owner | accepted RF/target/dependency decisions | Projection; roadmap task не заменяет `CQRA-*` или `TASK-*`. |
| Product Test Assurance | `Test Engineering` | accepted cross-project BC/CC/MAT/TM/GAP/TASK | Projection; обязательность и package membership design-required. |
| Product Code Quality Summary | `Code Quality Review` или явно выбранный продуктовый owner | Project CQ/CQRA плюс accepted product interpretation, если она появится | Aggregation alone is projection; new interpretation needs authority decision. |
| Product Technical Documentation | Technical Documentation/STM owner | accepted cross-project STM and provenance | Projection; incomplete availability must remain visible. |

Для каждого output нужны explicit selection, prerequisites, dependency closure,
freshness inputs, owner/writer и distinction Project-local/Product-level.

### Package

Stage B package semantics достаточно выразительны как основа: named package,
finite required/optional/conditional members, resolved membership snapshot,
freshness policy, explicit selection plus dependency closure. Product package
может содержать Project subpackages как projections or references, но не должен
вводить второй package authority.

`ALL_SCOPED_CURRENT` должен означать все требуемые resolved Product members,
а не каждый документ каждого Project. При недоступном required Project member
соответствующий package gate может быть заблокирован только если resolved
membership и выбранная policy делают его обязательным; это не блокирует
автоматически независимые Project gates или другие Product packages. При
`PERMISSIVE` ограничения видимы и deferred. Exact membership snapshot,
Project subpackage reference semantics, required/optional/conditional members,
partial/unavailable member behavior, freshness aggregation и relationship с
локальными subpackages — `DESIGN_DECISION_REQUIRED`.

## Authorization и human control

Discovery не предоставляет разрешений на изменение внешних репозиториев.
Будущая реализация должна явно авторизовать отдельно:

- открытие/чтение каждого дополнительного repository;
- выбор revision, branch, worktree и dirty baseline;
- создание или изменение Product membership;
- запись semantic artifacts или projections в каждом Project;
- запуск тестов, симуляторов или окружений;
- изменение кода, веток, worktrees и deployment configuration;
- генерацию remediation code, commit, PR или push.

Сводный отчёт, индекс, Product membership и межпроектная ссылка не дают права
записи в чужой authority. Никакая автоматическая клонизация, переключение
ветки, очистка worktree, provisioning или cross-project code generation не
должна быть скрытой частью Stage E.

## Context и scale

Нельзя решать масштаб конкатенацией всех репозиториев в один prompt. Требуется
evidence-first acquisition:

```text
Product membership / baseline vector
  → dependency-directed candidate edges
  → minimum Project evidence slices
  → cross-project evidence only for affected edges
  → accepted STM/capability authority
  → Product projections
```

Нужны staged reads, Project summaries только как навигация, lazy loading raw
sources, deterministic scope, explicit context budget и сохранённые
limitations. Summary не заменяет owning semantic artifact. Generated Product
index помогает искать reverse edges, но не решает ownership, impact или
materiality.

## Архитектурные варианты

### Вариант A — необязательный Product aggregate

Product — устойчивый aggregate, который только ссылается на независимые
Project review states. Межпроектные вопросы реализуются через relations и
проекции; Product почти не хранит собственную семантику.

**Плюсы:** минимальное влияние на single-project, простая миграция, повторное
использование локальных `PRJ-*` и пакетов. **Минусы:** трудно хранить
принятый cross-project fact и Product finding; большая часть интерпретации
остаётся в ephemeral session или отчёте.

### Вариант B — динамический Product workspace

Product review — временная композиция Project baselines и evidence без
устойчивого Product aggregate; каждый запуск заново собирает межпроектный
контекст.

**Плюсы:** нет новой долгоживущей identity/membership модели. **Минусы:**
слабая provenance, невозможность надёжно revalidate membership и baseline,
плохое продолжение между сеансами, риск скрытой authority в workspace.
Это не рекомендуется для продукта, который должен жить дольше одного сеанса.

### Вариант C — гибрид (рекомендуется)

Сохраняется необязательная Product identity/membership direction с историей и
vector baseline; необходимость именно persistent Product aggregate остаётся
proof obligation для Design. Project-local STM/capability authority остаётся независимой.
Узкий межпроектный слой выражает только принятые relations, cross-project
facts и impact edges с provenance; Product findings принадлежат уже
существующему владельцу только при подтверждённой scope-модели. Product
outputs — Stage B projections и пакеты поверх этих authorities.

**Плюсы:** сохраняет single-project, имеет устойчивый baseline/provenance,
поддерживает частичную доступность и impact-driven revalidation, не создаёт
вторую authority по умолчанию. **Минусы:** требует тщательно определить
identity, ownership, membership и cross-project adjudication; больше metadata
и проверок, чем вариант A.

**Рекомендация:** взять C в Design, но сначала принять решения из реестра
ниже. Не создавать новую factual authority или новый ID family до доказанного
разрыва существующих контрактов.

## Реестр решений

| Тема | Класс | Discovery-вывод |
|---|---|---|
| Product identity | `DESIGN_DECISION_REQUIRED` | Необязательная identity/membership с revision/history; необходимость persistent aggregate, format, owner и lifecycle требуют Design proof. |
| Project identity | `DESIGN_DECISION_REQUIRED` | Нужна явная identity, отличная от repository/review target/workspace. |
| Product membership | `DESIGN_DECISION_REQUIRED` | Явная версионируемая membership; кардинальность и изменение требуют решения. |
| Repository relationship | `DISCOVERY_RESOLVED` | Repository — источник ревизии/provenance, не синоним Project; нужны many-to-one и one-to-many случаи. |
| Product baseline | `DESIGN_DECISION_REQUIRED` | Нужен vector из Project/shared revisions; partial/dirty acceptance не задана. |
| Cross-project evidence | `DESIGN_DECISION_REQUIRED` | Адресуемые multi-source observations и запрет report-as-authority resolved; owner/lifecycle/acceptance form и conflict handling требуют Design. |
| Cross-project STM | `DESIGN_DECISION_REQUIRED` | Сначала расширить scope/provenance существующих STM; relation/index layer только при доказанном разрыве. |
| Dependency semantics | `DISCOVERY_RESOLVED` | Сохраняется различие factual relation и direct dependency/impact metadata. |
| Shared ownership | `DESIGN_DECISION_REQUIRED` | Owner, user и external status должны быть раздельными; Product ownership не предполагается. |
| Product findings | `DESIGN_DECISION_REQUIRED` | Вероятно существующий `RF-*` с Product scope; exact authority binding не задан. |
| Code Quality aggregation | `DESIGN_DECISION_REQUIRED` | Локальные `CQ-*` остаются authority; продуктовый pattern требует owner и новой adjudication. |
| Test Engineering | `DESIGN_DECISION_REQUIRED` | Существующие семейства могут покрыть provider/consumer; Product Assurance owner/package не задан. |
| Compatibility | `DESIGN_DECISION_REQUIRED` | Нужны exact revisions, contract views и evidence; engine/матрица не определены. |
| Product `REVALIDATE` | `DESIGN_DECISION_REQUIRED` | Расширить impact traversal и baseline vector без полного аудита каждого изменения. |
| Product `EXTEND` | `DESIGN_DECISION_REQUIRED` | Additive extension is a resolved constraint; membership meaning changes need adjudication, impact and package-routing design. |
| Partial availability | `DESIGN_DECISION_REQUIRED` | Раздельные availability/coverage/semantic/projection/package outcomes; Product status enum и acceptance rule не заданы. |
| Dirty state | `DISCOVERY_RESOLVED` | Не очищать и не угадывать; каждый Project получает explicit baseline/dirty binding. |
| Projections | `DESIGN_DECISION_REQUIRED` | Кандидаты определены, но owner/prerequisites/freshness каждого Product output требуют Design. |
| Package model | `DESIGN_DECISION_REQUIRED` | Повторно использовать Stage B; subpackages/partial gate policy не определены. |
| Authorization | `DISCOVERY_RESOLVED` | Любой межрепозиторный доступ и запись остаются explicit human-authorized. |
| Context/scale | `DISCOVERY_RESOLVED` | Нужны staged, dependency-directed reads; нельзя объединять все репозитории в prompt. |
| New identifier families | `DEFERRED_FUTURE_SCOPE` | Не вводить до Design-доказательства, что scoped existing identities недостаточны. |

## Риски

- Product identity может незаметно стать обязательным родителем и сломать
  single-project compatibility.
- Persistent Product identity может получить необоснованное ownership, если
  Design не докажет, что revision-bound context недостаточен.
- Один Product baseline без revision vector будет скрывать смешанные состояния.
- Сводные отчёты могут превратиться в неявную authority, если не сохранять
  ownership/provenance.
- Cross-project observation/adjudication может стать второй evidence authority,
  если Design не определит owner, acceptance gate и relation с `WS-*`/`EV-*`.
- Межпроектный dependency graph может смешать relations, reverse indexes и
  semantic prerequisites.
- Partial availability способна породить слишком широкое утверждение при
  `PARTIAL` или `BLOCKED` охвате.
- Product-level CQ/TE интерпретации могут незаметно передать ownership между
  capability-модулями.
- При shared component без owner/writer возникает конфликт обновления и
  неясный impact root.
- Dirty или diverged repositories могут дать ложный единый baseline.
- Product package с `ALL_SCOPED_CURRENT` может ошибочно блокировать независимые
  Project gates, если scope не будет разрешён явно.
- Context pressure может подтолкнуть к чтению summary вместо authority или к
  полной конкатенации исходников.

## Отложенная область

Вне этого Discovery остаются: Product database/service; graph/vector/RAG
infrastructure; automatic cloning, branch switching и cleanup; test/simulator
execution; environment provisioning/deployment; code generation/remediation;
automatic migration; PR/push; точный UX; новый ID family; compatibility
engine; runtime coordinator implementation.

## Fail-first pressure scenarios для Design

1. Обычный single-project review запускается без Product.
2. Product содержит три чистых репозитория с согласованным vector baseline.
3. Один обязательный Product Project недоступен.
4. Один repository имеет dirty tracked state.
5. Project B изменён после принятого Product baseline.
6. Межпроектная API compatibility break.
7. Shared component используется двумя Projects.
8. Product finding подтверждается evidence из двух Projects.
9. Project-local finding ошибочно пытаются превратить в Product finding.
10. `EXTEND` добавляет Project D.
11. `REVALIDATE` затрагивает только зависимые Projects.
12. Product projection stale, а Project semantic state valid.
13. Один Project использует старую, но совместимую версию.
14. Между Projects обнаружены conflicting evidence.
15. Product package имеет blocked required member.
16. Один Project повторно используется в двух Products (если это разрешено).
17. `EXTEND` меняет membership meaning или requiredness существующего Project.
18. Standalone Project получает или покидает однопроектный Product context.

Для каждого сценария Design должен проверять baseline/provenance, authority,
minimum dependency slice, partial/blocked result, package freshness и отсутствие
скрытой записи в чужой семантический источник. Сценарий 17 защищает границу
между additive `EXTEND` и membership-semantic revalidation. Сценарий 18
защищает Product optionality, отсутствие mandatory parent и нерешённую
кардинальность single-member Product. Сценарии 3 и 15 дополнительно должны
различать source availability, semantic coverage, projection freshness и
package gate; один unavailable Project не получает универсальный Product
status.

## Итог и следующий checkpoint

Discovery завершает Stage E на уровне ограничений и вариантов, но не принимает
новую runtime или semantic contract. Рекомендуется начать отдельный Stage E
Design с вариантом C и сначала закрыть Product/Project identity, membership,
vector baseline, cross-project STM relation boundary, Product finding owner,
partial availability и package semantics.

После принятия Design и его независимого review потребуется синхронизировать
`docs/roadmap.md`: отметить фактически завершённые Stage D и Stage E только в
соответствующих promotion checkpoints. В текущем Discovery дорожная карта
намеренно не изменялась.
