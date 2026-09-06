# Пример: Code Quality Review

## Исходная ситуация

Frontend имеет несколько entrypoints и постепенно оброс локальными workaround для локализации, retries и state synchronization. Команда хочет понять, какие проблемы действительно существенны, а не получить список lint warnings.

Запрос:

```text
Используй architecture-code-review.
Нужен только Code Quality Review: Findings View, Summary и Maintainability Hotspots.
Architecture Review и Test Engineering не включай.
```

## Review Suite

```text
Architecture Review: OFF
Test Engineering: OFF
Code Quality Review: ON
  Findings View/Report
  Code Quality Summary
  Maintainability Hotspots
```

## Signal collection

Инструменты и repository inspection находят:

- duplicated locale fallback functions;
- 11 hardcoded user-facing labels;
- большой state coordinator;
- несколько ignored promise rejections.

На этом этапе findings ещё нет.

```text
tool warning != CQ finding
metric != CQ finding
smell != CQ finding
```

## Проверка material consequence

Для duplicated locale fallback исследование показывает:

- desktop entrypoint normalizes unknown locale to English;
- web entrypoint falls back to system locale;
- settings preview uses a third mapping;
- один и тот же user profile показывает разные language results в зависимости от entrypoint.

Это уже evidence-backed consequence.

Accepted finding может выглядеть так:

```text
CQ-014
mechanism: three independent locale fallback implementations
material consequence: the same profile can render different language depending on entrypoint
severity: MEDIUM
```

## Что осталось только signal

Допустим, большой state coordinator действительно имеет 2400 LOC, но targeted review не доказал material defect/maintenance consequence beyond size itself.

Он остаётся observation/candidate и не превращается в `CQ-*` только по metric.

## Maintainability Hotspot

Если несколько accepted findings концентрируются в `src/session/`, hotspot может объединить их для planning:

```text
Hotspot: session/state orchestration
linked findings:
  CQ-021
  CQ-024
  CQ-031
reason:
  repeated lifecycle/error-handling mechanisms create coupled maintenance burden
```

Hotspot не строится просто по LOC ranking.

## Remediation

Для `CQ-014` создаётся action:

```text
CQRA-006
centralize locale resolution behind one accepted policy
```

После реализации action получает `COMPLETED`.

Но finding остаётся открытым до revalidation:

```text
CQRA COMPLETED != CQ RESOLVED
```

Revalidation должна проверить, что divergent behavior действительно исчезло во всех material entrypoints.

## Связь с другими capabilities

Если investigation обнаружит architecture-level ownership issue, Code Quality может создать relation/escalation к Architecture concern, но не должна сама переписать это в `RF-*` без Architecture owning flow.

Если проблема — отсутствие executable proof, это Test Engineering concern, а не автоматический `CQ-*`.

## Итоговые документы

Пользователь получает:

- Findings View — detailed record-level view;
- Summary — компактную картину material risks;
- Hotspots — areas of concentrated accepted maintenance burden.

Каждый документ — projection accepted CQ authority, а не отдельная semantic truth.

## Снимок принятого результата

```text
baseline: a1b2c3d
Review Suite: Code Quality Review = ON
selected documents: Findings View/Report, Code Quality Summary,
                    Maintainability Hotspots
package members: PRJ-CQ-00-FINDINGS-VIEW, PRJ-CQ-01-SUMMARY,
                 PRJ-CQ-02-HOTSPOTS
freshness: CURRENT for selected members
```

Путь проверки вывода:

```text
PRJ-CQ-00-FINDINGS-VIEW
  -> CQ-014
  -> WS/EV or source references
  -> affected locale-resolution entrypoints at a1b2c3d
```

`PRJ-CQ-*` не получает право менять `CQ-*`; новый код проверяется через
`REVALIDATE`, а свежий документ создаётся через `RG-*` при необходимости.
