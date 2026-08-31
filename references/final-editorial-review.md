# Финальное редакционное ревью

Этот gate запускается только после технического принятия всех requested endpoint artifacts и финальной сборки пакета.

Editorial Review (редакционное ревью) **не редактирует документы напрямую**. Оно создаёт issue list. Исправление выполняет отдельный correction pass, затем новый fresh-context re-review.

## 1. Цель

Проверить, что финальные документы:

- написаны связным русским техническим языком;
- объясняют material mechanisms человеку, а не копируют terse working-artifact style;
- используют терминологию последовательно;
- содержат полезные и реально валидированные диаграммы там, где topology/lifecycle/ownership/target behavior трудно понять только текстом;
- не содержат stale/superseded technical claims;
- согласованы между собой и с authoritative ledger;
- имеют целостный cross-link graph;
- не искажают severity/evidence/target/roadmap semantics при редактуре;
- не заявляют `REVIEW_COMPLETE`, если Discovery Coverage не имеет принятого `COVERAGE_ACCEPTED` state.

Editorial Review **не является техническим re-audit**. Он не обязан заново искать пропущенные vulnerability/mechanism classes в repository. Проверка полноты thematic discovery и absence-of-investigation gaps принадлежит Independent Coverage Review из `discovery-coverage.md`.

## 2. Language contract

Narrative — русский.

При первом существенном употреблении допустимо:

```text
English term (русский аналог)
```

Дальше предпочитай русский аналог, если точность не теряется.

Не переводи exact:

- class/function/type identifiers;
- filenames/paths;
- API/IPC/protocol names;
- runtime states;
- verdict/status tokens;
- commands/code.

Флагай случайные английские paragraphs/headings/table explanations.

Также флагай mixed-language shorthand, если обычную мысль можно естественно выразить по-русски без потери точности. Примеры нежелательной final prose:

```text
error-boundary протекает credential-ами
prod-risks untestable
shutdown негрейсфул
designated owner отсутствует
runtime-drift
```

Не требуй искусственного перевода exact identifiers или established technical terms. Цель — профессиональный читаемый русский, а не языковой пуризм.

## 3. Prose quality contract

Working notes, HANDOFF SUMMARY, ledger rows и verification matrices могут быть плотными. Final user-facing narrative должен быть объясняющим.

Для каждого material conclusion проверь, что текст отвечает на четыре вопроса:

1. что происходит сейчас;
2. почему это происходит;
3. к чему это приводит;
4. что нужно изменить или сохранить.

Предпочтительная causal structure:

```text
mechanism → evidence → consequence → correction direction
```

Это структура мысли, а не требование писать стрелками.

### 3.1 Один основной механизм на абзац

Один абзац должен иметь один dominant architectural mechanism или одну causal chain. Связанные evidence/consequences могут находиться в том же абзаце, но несколько независимых root mechanisms не должны сливаться в одну стену текста.

Если после чтения абзаца на вопрос «какой один механизм здесь объясняется?» требуется перечислить несколько независимых ответов, раздели или реструктурируй текст.

Не вводи механическую квоту по длине предложений/абзацев: короткий сложный абзац тоже может быть перегружен, а длинный — оставаться связным, если раскрывает одну причинную цепочку.

### 3.2 Explain before compressing

На первом material употреблении specialist English term, hybrid shorthand или неочевидного architecture pattern объясни механизм естественным русским предложением. Exact term можно сохранить в скобках или использовать дальше как короткое имя.

**Technical shorthand не считается объяснением сам по себе.** Точное сочетание терминов может правильно называть решение, но не заменяет описания поведения системы.

Не пиши в explanatory layer так:

```text
NATS получает eager startup + registered shutdown + drain.
in-flight KV puts дропаются при shutdown.
single-flight wrapper предотвращает thundering-herd на cold-cache miss.
```

Сначала раскрой наблюдаемое поведение нормальным языком. Например:

```text
При запуске приложение заранее проверяет доступность NATS и не объявляет себя готовым, если соединение установить невозможно. При остановке оно сначала завершает уже начатые операции, а затем корректно закрывает соединение. Такой подход можно дальше кратко называть fail-fast startup и graceful drain.
```

Или:

```text
При остановке приложения уже начатые операции записи в NATS KV могут быть оборваны до завершения, если соединение закрывается без ожидания активной работы.
```

Для single-flight сначала объясни, что при одновременном отсутствии значения в кэше несколько одинаковых запросов могут обратиться к источнику параллельно, а механизм оставляет один запрос к источнику и заставляет остальные ждать его результат. После этого термин `single-flight` можно использовать как краткое имя уже объяснённого поведения.

Точные формулировки примеров не нормативны. Нормативен порядок: **сначала механизм на естественном языке → затем специализированный термин как краткое название**.

Не требуется заново объяснять общеизвестные для целевой аудитории термины в каждом абзаце. Gate направлен против кластеров shorthand, которые заменяют explanation.

### 3.3 Roadmap presentation

Roadmap task сначала содержит human-readable problem/cause/consequence/target-result layer, затем визуально отделённый implementation contract.

Для material roadmap task:

- заголовок должен быть понятен как инженерная задача без `[prereq: ...]`, `[RF: ...]` и другой execution metadata;
- prerequisite/RF/SER/target metadata переносится в технический контракт;
- после explanatory layer обязателен отдельный heading `### Технический контракт реализации`;
- prerequisites, allowed/forbidden scope, regression tests, verification, exit criteria, rollback и safe activation находятся после этого heading, предпочтительно в таблице или другом явно справочном формате.

Labels `Prerequisites`, `Allowed boundary`, `Verification` не должны сливаться с объясняющим текстом.

Флагай как `STYLE-*` / `TERM-*`, если:

- final prose выглядит как agent scratchpad/handoff;
- предложения заменены fragments/labels;
- стрелки `->`, `!=`, slash-compounds и скобочные IDs несут основную смысловую нагрузку;
- RF/SER/TASK IDs заменяют объяснение;
- implementation nouns появляются раньше объяснения самой проблемы;
- executive summary является ledger dump вместо synthesis;
- один абзац заставляет одновременно отслеживать несколько независимых root mechanisms;
- specialist shorthand используется до понятного объяснения его механики;
- technical shorthand сам является explanatory layer;
- material roadmap title содержит bracketed execution metadata;
- material roadmap task не содержит `### Технический контракт реализации`;
- roadmap human-readable layer и execution contract визуально не разделены.

## 4. Diagram coverage and renderability contract

Сверь final package с `lifecycle-and-mermaid.md` и `report-contract.md`.

Если в системе есть material topology, lifecycle, ownership, trust boundary, ordering или target transition, проверь наличие useful visual explanation.

Для substantial report особенно ожидаются, когда применимы:

- As-Built component/boundary diagram;
- runtime/lifecycle/sequence diagram;
- Target Architecture diagram;
- Before → After diagram для material correction;
- roadmap dependency diagram для нетривиального sequencing/safe activation.

Отсутствие диаграммы допустимо, если visual representation реально не добавляет архитектурной информации. В substantial package такое решение должно быть явно объяснимо.

Каждый Mermaid block в final user-facing artifacts должен быть enumerated. Если доступен совместимый parser/renderer, reviewer/correction workflow должен иметь evidence реального tool invocation для каждого блока. Известный parser/render failure блокирует acceptance.

Если renderer отсутствует, зафиксируй `MERMAID_RENDER_VALIDATION_UNAVAILABLE` и не называй Mermaid render validation успешной.

Флагай как `DIAG-*`, если:

- material architecture трудно понять без visual aid, но его нет;
- диаграмма декоративна и не объясняет real mechanism;
- current/target behavior смешаны;
- Mermaid противоречит prose или accepted evidence;
- diagram uses generic fake components instead of real subsystem names;
- Mermaid block не проходит доступный parser/renderer;
- часть final Mermaid blocks не была фактически проверена при доступном renderer;
- заявлен render-validation PASS без evidence tool invocation.

## 5. Issue types

Рекомендуемые IDs:

```text
LANG-###   language drift / grammar / hybrid shorthand
TERM-###   inconsistent or unexplained terminology
STYLE-###  machine-like / duplicate / telegraphic / overloaded prose
DIAG-###   missing/useless/misleading/unrenderable diagram
LINK-###   broken/missing cross-link
CONS-###   prose/table/diagram/document contradiction
STALE-###  superseded claim resurfaced
SEV-###    wording rhetorically exceeds adjudicated severity
STATUS-### final status contradicts accepted technical/coverage gate state
```

## 6. Checks

Проверь:

- connected prose `mechanism → evidence → consequence → correction direction`;
- one primary mechanism per paragraph for material explanatory prose;
- specialist shorthand explained before it becomes compressed terminology;
- technical shorthand is not used as the explanation itself;
- accidental English drift;
- mixed-language shorthand/transliteration;
- inconsistent translations/terms;
- grammar/readability;
- executive summary explains system-level causes before RF lists;
- material roadmap title is human-readable and does not carry bracketed execution metadata;
- roadmap tasks first explain problem/root cause/result, then contain mandatory `### Технический контракт реализации`;
- useful diagram coverage where material complexity warrants it;
- every final Mermaid block enumerated;
- actual parser/render validation for every final Mermaid block when a compatible renderer is available;
- failed Mermaid blocks corrected and revalidated before acceptance;
- explicit `MERMAID_RENDER_VALIDATION_UNAVAILABLE` when executable validation cannot be performed;
- duplicate paragraphs/findings;
- stale superseded statements;
- root titles/status/severity одинаковы во всех final artifacts;
- diagrams/state tables не противоречат prose;
- important relative links resolve conceptually;
- no orphan RF/SER/TASK/target references;
- target mechanisms link to motivating RF/SER/invariant;
- roadmap tasks link to target/RF;
- working superseded claims point forward to current authority where required;
- no unsupported intensifiers `catastrophic`, `RCE`, `data loss`, `critical` вне adjudicated context;
- final status соответствует `working/INDEX.md` и accepted Discovery Coverage state;
- package не утверждает `REVIEW_COMPLETE`, если coverage находится в `PARTIALLY_COVERED`, `BLOCKED`, `COVERAGE_CORRECTION_REQUIRED`, `COVERAGE_BLOCKED`, `COVERAGE_AUTHORITY_DRIFT` или material `REVALIDATION_REQUIRED`.

## 7. Semantic safety

Editorial reviewer **не имеет права молча менять**:

- evidence;
- root identity;
- severity;
- confidence/exploitability;
- product-intent status;
- target invariants/ownership;
- feasibility classification;
- roadmap dependencies/gates;
- security assumptions;
- Discovery Coverage technical verdict.

Editorial reviewer также **не выполняет новый repository-wide vulnerability/discovery search** для доказательства coverage. Если final package показывает non-accepted/stale coverage state, он флагирует status/consistency issue и возвращает пакет в соответствующий technical coverage gate.

Если language/diagram cleanup обнаруживает реальное technical contradiction, issue получает `CONS-*` и возвращается в соответствующий technical gate.

## 8. Output

Review artifact содержит:

```text
reviewed final artifact refs
baseline / authoritative ledger ref
coverage verdict / coverage artifact ref
issue ID
location
category
observed problem
required correction boundary
technical-gate escalation? yes/no
```

Для Mermaid validation дополнительно сохрани compact record:

```text
diagram/document location
validator/renderer used
result: PASS | FAIL | UNAVAILABLE
correction/revalidation ref if failed
```

Не переписывай полный документ в review artifact.

## 9. Correction loop

```text
FINAL PACKAGE ASSEMBLED
→ fresh-context editorial review
→ issue list
→ separate editorial correction writer
→ verify links/semantics + Mermaid renderability + status consistency
→ fresh-context editorial re-review
→ FINAL_PACKAGE_ACCEPTED | CORRECTION_REQUIRED | TECHNICAL_GATE_REQUIRED
```

Correction writer меняет только то, что разрешено issue list; новый technical content не добавляет без возврата в technical gate.

Coverage-related `STATUS-*` не исправляется редактором подменой verdict. Если coverage не принято, correction boundary — technical Coverage Review/correction/revalidation.

## 10. Final acceptance

Пакет нельзя объявлять финальным, пока:

- все editorial issues closed или explicitly blocked;
- re-review выполнен;
- cross-links проверены;
- no stale authoritative projection remains;
- language/prose quality contract соблюдён;
- material roadmap tasks имеют human-readable titles и явную границу `### Технический контракт реализации`;
- diagram coverage contract соблюдён либо отсутствие диаграмм обосновано;
- нет known Mermaid parser/render failures;
- при доступном renderer все final Mermaid blocks имеют executable validation evidence;
- при недоступном renderer limitation явно зафиксирован и render PASS не заявлен;
- requested target/roadmap artifacts уже accepted технически;
- Discovery Coverage имеет accepted `COVERAGE_ACCEPTED` state, bound to current accepted As-Built/baseline;
- final status не маскирует material coverage limitation.
