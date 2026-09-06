# Совместимость и миграция

Review Suite рассчитан на повторное использование persisted audit packages между sessions и версиями Skill. Поэтому legacy state рассматривается как состояние, которое нужно понять и при необходимости согласовать, а не как автоматически «сломанное».

## Общий принцип

```text
legacy != corrupt
missing modern metadata != accepted modern state
```

Старая package может быть пригодна для чтения, `USE_EXISTING` или bounded migration, но отсутствие новых metadata нельзя молча интерпретировать как current/verified state.

## Что считается legacy package

Признаки могут включать:

- отсутствие Shared Technical Model в современной форме;
- старый `INDEX.md` без новых coordinator fields;
- Test Review, сохранённый только через legacy endpoint;
- final Markdown без `PRJ-*` lifecycle metadata;
- отсутствие современного projection dependency/fingerprint record.

Это признаки версии модели, а не автоматический failure verdict.

## Conservative reconciliation

Новая версия Skill должна modernize только то, что необходимо текущей задаче.

### `USE_EXISTING`

Может использовать surrounding accepted package state, если requested deliverable/authority пригодны. Не обязан мигрировать весь package «на всякий случай».

### `RESUME`

Восстанавливает first unfinished dependency и reconciles нужный state. Не переписывает unrelated accepted history.

### `EXTEND`

Backfills только dependency slice, необходимый для нового capability/output.

### `REVALIDATE`

Использует старое As-Built/evidence как historical context, но fresh affected semantics должна пройти current gates.

## Legacy Test Review

Старые values:

```text
REVIEW_ONLY
REVIEW_PLUS_TEST_PLAN
```

являются compatibility input, а не современными menu choices.

Conservative normalization:

```text
REVIEW_ONLY
  -> Test Assurance = true
  -> all optional outputs = false

REVIEW_PLUS_TEST_PLAN
  -> Test Assurance = true
  -> Test Plan = true
  -> all other optional outputs = false
```

Normalization не должна придумывать outputs, которых legacy state не доказывает.

## Legacy As-Built и STM

Старый Architecture As-Built нельзя автоматически объявить accepted STM.

Для reuse его factual content может быть historical context/candidate input, но modern STM authority требует baseline/evidence validation через Technical Model Gate.

Это защищает от «миграции по переименованию файла», при которой old prose внезапно становится factual authority без доказательств.

## Legacy projections

Readable Markdown без `PRJ-*` lifecycle metadata не становится `CURRENT` автоматически.

Registration path концептуально:

```text
legacy artifact
  -> identify owner
  -> assign PRJ identity
  -> define projection contract
  -> resolve dependencies
  -> verify against accepted authority
  -> establish fingerprint/revision
  -> CURRENT
```

Если semantic authority не удаётся установить, registration блокируется и работа возвращается в owning semantic workflow.

## Backfill coordinator metadata

Missing modern fields в старом `INDEX.md` требуют additive reconciliation, а не полной перезаписи package.

При backfill важно:

- не делать compact state substantive authority;
- ссылаться на current owning artifacts/revisions;
- не маскировать unknown as VALID;
- сохранять историю package.

## Compatibility promise

Human-facing expectation проекта:

1. legacy package не уничтожается молча;
2. отсутствие modern metadata обнаруживается явно;
3. migration/backfill выполняется только при необходимости текущей задачи;
4. old accepted meaning не повышается до более сильной modern authority без current evidence;
5. modern outputs/freshness claims требуют modern verification contracts.

Конкретные schema/version guarantees определяются текущими normative contracts и release history. Если вашей организации нужна строгая long-term compatibility matrix, фиксируйте used Skill SHA вместе с audit package governance.

## Обновление во время `IN_PROGRESS`

Если Skill обновлён посреди незавершённого audit:

1. не начинайте `NEW` только из-за update;
2. используйте `RESUME`;
3. coordinator проверит persisted state/owning revisions;
4. недостающие modern fields reconciles bounded way;
5. при semantic incompatibility workflow должен остановиться, а не угадывать migration.

## Migration failure

Не продолжайте downstream work, если:

- owner старого artifact неясен;
- baseline binding потерян;
- semantic meaning нельзя отделить от presentation;
- current dependency contract невозможно восстановить;
- old compact state конфликтует с owning artifact.

В таких случаях сохраняйте legacy material как non-current context и возвращайтесь к targeted technical revalidation/contract adjudication.

## См. также

- [Upgrade and Rollback](upgrade-and-rollback.md)
- [Troubleshooting](troubleshooting.md)
- [Authority and Provenance](../concepts/authority-and-provenance.md)
