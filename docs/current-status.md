# Current Project Status

Этот документ фиксирует текущую принятую базовую точку `architecture-code-review`.
Стратегические направления остаются в [Product Roadmap](roadmap.md), а подробные
нормативные правила — в `SKILL.md`, `references/` и capability-контрактах.

## Canonical baseline

```text
canonical branch: main
canonical baseline: 2091a44622371bbc39fb913c00c1876d7f182dec
status: PROMOTED
```

## Completed foundation

На текущем `main` приняты и продвинуты следующие крупные части:

```text
Shared Technical Model Foundation                 DONE
Audit Projection & Regeneration                   DONE
Test Engineering                                  DONE
Code Quality Review                               DONE
Product / Multi-Project Review                    DONE
Interface, API & Data Integration Catalog         DONE
API Operation Completeness                        DONE
Change Review & Baseline Reconciliation           DONE
```

Это означает завершённые contract/design/implementation/review/promotion циклы.
Репозиторий остаётся Markdown Skill/reference system: наличие контракта не
означает наличие отдельного runtime coordinator, scanner или test executor.

## Change Review lifecycle

Последнее принятое расширение добавляет отдельный orchestration lifecycle для
проверки изменений до принятия нового baseline:

```text
accepted baseline
    ↓
CHANGE_REVIEW
    ↓
candidate assessment
    ↓
RECONCILE_CHANGE
    ↓
existing owning authorities
    ↓
baseline advancement
    ↓
Projection Impact Analysis
    ↓
optional explicit regeneration
```

Ключевые ограничения:

- `CHANGE_REVIEW` — orchestration intent, а не новая capability;
- `CR-*`, `CF-*`, `CRF-*` не являются canonical authority;
- review можно выполнять для branch, commit или pull request;
- base и candidate привязываются к immutable source state;
- `RECONCILE_CHANGE` доступен только контекстно и не заменяет owner adjudication;
- review base должен совпадать с текущим accepted baseline либо весь промежуточный delta должен быть доказан linked/supplemental review chain;
- partial reconciliation не может продвинуть весь baseline;
- `TREE_EQUIVALENT` требует доказанного `WHOLE_TREE_EQUAL` или `FROZEN_RELEVANT_SCOPE_EQUAL`;
- candidate prediction не меняет `CURRENT` / `STALE` / `BLOCKED`;
- фактический Projection Impact выполняется только после принятой reconciliation;
- regeneration остаётся отдельным явным действием.

## Promotion evidence

```text
approved design head:
bc3d7410652a3c73ddb74da6de7e49a1815ec5b9

approved plan head:
e61f53ba560b50d3ca21475b40f572c9ac8c9085

approved feature head:
d870198eacaf1c2cd4d4ff685212fdb48491c3d7

promotion merge:
2091a44622371bbc39fb913c00c1876d7f182dec
```

Promotion used a clean `--no-ff` merge. The promoted merge tree matched the
approved feature tree exactly. Independent remediation re-review finished with
`0 HIGH / 0 MEDIUM / 0 LOW` remaining findings.

## Validation summary

```text
Change Review scenarios:          36/36 exact design mapping
Merge/reuse scenarios:            10/10 deterministic
Partial reconciliation scenarios: 5/5 deterministic
Authority barrier:                 8/8 pass
Intent routing:                   10/10 deterministic
Projection separation:             6/6 pass
Product qualification:             6/6 pass
Baseline-binding remediation:       5/5 pass
Migration:                          COMPATIBLE_EXTENSION
Harness:                            DO_NOT_BUILD_HARNESS
```

## Where to read next

- [Change Review guide](guides/change-review.md)
- [Reuse, changes and extension](guides/reuse-and-change.md)
- [Session Intent reference](reference/workflows.md)
- [Product Roadmap](roadmap.md)
- [Change Review closeout](superpowers/reviews/2026-09-11-change-review-baseline-reconciliation-closeout.md)
