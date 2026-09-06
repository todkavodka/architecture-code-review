# Пример: повторная проверка после изменений

## Исходная ситуация

Месяц назад команда завершила Architecture Review + Test Engineering. Package принят на baseline `A`.

С тех пор появились 24 commits. Изменены:

- retry coordinator;
- completion event publisher;
- два integration tests;
- UI не менялся;
- auth subsystem не менялся.

Пользователь просит:

```text
Используй существующий audit package и проверь изменения после прошлого accepted baseline.
```

## Intent

Skill рекомендует:

```text
REVALIDATE
```

Предыдущая Review Suite configuration восстанавливается read-only. Пользователь не выбирает заново capabilities и outputs.

## Change inventory

Git diff и Project Profile delta используются для routing:

```text
src/retry/* changed
src/events/publisher.py changed
tests/integration/retry_* changed
```

Эти paths не являются сами по себе доказательством semantic impact.

## Dependency impact

Accepted records показывают зависимости:

```text
INT-PUBLISH-COMPLETION
  -> RF-007
  -> BC-022
  -> MAT-012
  -> CQ-019 (if selected in prior suite)
```

Auth facts и unrelated storage migration records не имеют demonstrated linkage к change.

Impact классифицируется как `BOUNDARY`, потому что затронута material publication/retry boundary.

## Minimum dependency slice

Skill revalidates:

- affected evidence observations;
- relevant STM interactions/events;
- `RF-007`;
- `BC-022` / `MAT-012` / associated `TM/GAP`;
- dependent projections after semantic stabilization.

Он не обязан заново анализировать auth, unrelated REST endpoints или весь test suite.

## Fresh evidence

Создаются/обновляются observations на current baseline `B`.

Допустим, новый implementation добавил durable publication key и tests подтверждают timeout/retry scenario.

Technical Model Gate принимает revised interaction fact.

Architecture revalidation решает, остаётся ли `RF-007`, изменяется или superseded.

Test Engineering revalidation обновляет `TM-*` и может закрыть соответствующий `GAP-*` после accepted evidence.

## Preservation

Unchanged accepted auth subsystem сохраняется без revalidation, потому что dependency analysis не показывает impact.

Это ключевой смысл targeted workflow:

```text
changed HEAD
!=
full audit automatically required
```

## Projection impact

После semantic stabilization выполняется Projection Impact Analysis.

Допустим:

```text
Architecture Report -> STALE
Test Assurance Summary -> STALE
Unrelated Contract Report -> CURRENT
```

Impact accounting не переписывает documents.

Если пользователь требует fresh Architecture Report и Assurance Summary, запускается explicit targeted `RG-*` session.

## Когда был бы нужен full reaudit

Если changes одновременно перестроили persistence ownership, runtime topology, trust boundaries и major lifecycle, impact мог бы стать `SYSTEMIC`.

Тогда Skill возвращает:

```text
FULL_REAUDIT_RECOMMENDED
user_decision_required: true
```

И ждёт решения пользователя.

## Итог

`REVALIDATE` даёт три важных свойства:

1. fresh evidence только там, где она нужна;
2. preservation unaffected accepted state;
3. явное отделение semantic revalidation от projection regeneration.
