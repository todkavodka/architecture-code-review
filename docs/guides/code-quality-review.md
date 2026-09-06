# Руководство по Code Quality Review

Code Quality Review ищет не «плохой стиль» сам по себе, а конкретные механизмы реализации с доказуемым существенным последствием.

## Когда выбирать

Используйте capability, если нужно оценить:

- дублирование, которое реально приводит к divergent behavior;
- excessive complexity, мешающую изменению и доказанно расширяющую defect surface;
- неправильные lifecycle/resource patterns;
- concurrency hazards на implementation level;
- fragile error handling;
- плохие dependency boundaries;
- hardcoded user-facing values/localization defects;
- framework-specific anti-patterns;
- testability problems;
- maintainability hotspots.

Architecture Review и Test Engineering могут быть выключены.

## Что не является finding автоматически

```text
tool warning != CQ finding
metric != CQ finding
smell != CQ finding
candidate != semantic authority
```

Например, большой файл, высокая cyclomatic complexity или duplication percentage — только signals.

Чтобы появился `CQ-*`, нужно доказать material consequence.

## `CQ-*`

Accepted Code Quality finding обычно связывает:

- concrete implementation mechanism;
- evidence/provenance;
- material consequence;
- severity;
- confidence;
- applicability/disposition;
- relations к другим records;
- remediation/revalidation state.

Пример:

```text
CQ-014
mechanism: duplicated locale fallback rules in three entrypoints
consequence: user-visible behavior diverges depending on entrypoint
severity: MEDIUM
```

## `CQRA-*`

Code Quality remediation action принадлежит Code Quality Review.

Завершение action не закрывает finding автоматически:

```text
CQRA COMPLETED != CQ RESOLVED
```

После remediation нужна revalidation, которая показывает, что mechanism и consequence действительно устранены.

## Граница с Architecture Review

Code Quality finding не должен заменять architecture root finding.

Пример:

- duplicated retry code с локальным maintenance consequence → `CQ-*`;
- отсутствие единственного owner terminal publication на системной boundary → возможно `RF-*`.

Один mechanism может породить связанные `CQ-*` и `RF-*`, но ownership остаётся раздельным.

## Граница с Test Engineering

Отсутствие test evidence — не Code Quality finding только потому, что код трудно тестировать.

- недостаточное доказательство поведения → `GAP-*`;
- implementation mechanism, который материально разрушает testability → может быть `CQ-*`.

## User-facing outputs

Все перечисленные документы выбираются явно и являются derived projections:

```text
Findings View/Report
Code Quality Summary
Maintainability Hotspots
Roadmap Contribution
```

`DERIVED_PROJECTION` описывает их отношение к accepted authority. Это не означает auto-selection.

### Findings View/Report

Подробный report для инженерной работы с `CQ-*`.

### Summary

Краткое представление наиболее существенных patterns и concentrations of risk.

### Maintainability Hotspots

Группирует accepted evidence/findings по областям системы. Hotspot не должен вычисляться только по LOC или metric threshold.

### Roadmap Contribution

Формирует Code Quality contribution для planning: remediation groups, ordering constraints, dependencies и revalidation expectations. Не заменяет Architecture Remediation Roadmap.

## Coverage

Code Quality Review должен фиксировать, что именно было исследовано. Tool output или grep across repository не является достаточной coverage guarantee.

Если review bounded одной подсистемой, итог не должен называться глобальным code-quality verdict всего repository.

## Revalidation

После code changes:

```text
changed source/config/dependency/addendum/evidence/STM
  -> dependency impact
  -> affected CQ records
  -> targeted fresh evidence
  -> revalidation
```

Unrelated accepted `CQ-*` сохраняются, если dependency analysis подтверждает отсутствие impact.

## Addenda

Language/framework addenda уточняют, какие implementation patterns исследовать, но не создают отдельную semantic authority.

Например, Rust addendum может усилить checks ownership/lifetimes/unsafe/resource lifecycle, а frontend addendum — state/event/localization patterns. Finding всё равно принимается через общий CQ contract.

## Связанные документы

- [Code Quality example](../examples/code-quality-review.md)
- [Output Reference](../reference/outputs.md)
- [Authority and provenance](../concepts/authority-and-provenance.md)
