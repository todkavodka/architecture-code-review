# Current Project Status

Этот документ фиксирует текущую принятую функциональную базовую точку
`architecture-code-review`. Стратегические направления остаются в
[Product Roadmap](roadmap.md), а подробные нормативные правила — в `SKILL.md`,
`references/` и capability-контрактах.

## Canonical semantic baseline

```text
canonical branch: main
latest promoted semantic head: 996ba6b5a79a39caa284dab7d454f80ae6df0984
status: PROMOTED
```

Текущий semantic baseline включает Finding Lifecycle & Progress Reporting поверх
ранее принятого Federated Product Audit Coordination, Product / Multi-Project
Review и Change Review lifecycle. Promotion была выполнена как `FAST_FORWARD`;
последующие documentation-only closeout commits не меняют принятую семантику.
Для проверки точного текущего Git HEAD
используйте сам `main`.

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
Federated Product Audit Coordination              DONE
Finding Lifecycle & Progress Reporting            DONE
```

Это означает завершённые contract/design/implementation/review/promotion циклы.
Репозиторий остаётся Markdown Skill/reference system: наличие контракта не
означает наличие отдельного runtime coordinator, repository crawler, scheduler
или test executor.

## Federated Product Audit Coordination

Последнее принятое расширение позволяет запускать Product-level coordination из
не-Git каталога, под которым находятся несколько дочерних репозиториев, и
переиспользовать их уже принятые локальные аудиты без создания нового semantic
authority.

```text
Coordination Root
    ↓
bounded repository/source discovery
    ↓
explicit Product membership + frozen coordination plan
    ↓
qualified child reuse / resume / revalidation / change review
    ↓
stable child checkpoints
    ↓
exact Product baseline candidate
    ↓
final exact requalification
    ↓
Product Baseline Acceptance
```

Ключевые ограничения:

- Coordination Root — только locator/discovery boundary, а не repository,
  Project, Product, baseline или semantic authority;
- filesystem containment не создаёт Product membership;
- `Project != repository`, поддерживаются один Project в нескольких repos и
  несколько Projects в одном monorepo;
- Product Coordination Plan замораживает Product revision, membership snapshot,
  base Product baseline, выбранные member/source/scope bindings, child actions,
  requested work и authorization до dispatch;
- Product confirmation не отменяет локальные owner/capability gates;
- parallel child work разрешён только при отсутствии конфликтующих writer scopes;
- Product baseline остаётся immutable exact qualified member/source vector;
- перед Product Baseline Acceptance выполняется точная requalification всех
  acceptance-relevant bindings;
- если child завершён на `B`, а source уже стал `C`, `B` нельзя представить как
  current `C`;
- independently advanced child authority не продвигает Product автоматически;
  accepted-state update идёт через Product `REVALIDATE`, candidate assessment —
  через новый complete-vector Product `CHANGE_REVIEW`;
- source advancement и semantic-authority advancement являются независимыми
  осями: новая accepted Architecture/CQ/TE/STM revision на том же source не
  меняет member source vector;
- Product impact/readiness — derived routing/presentation views, не новые
  authority или lifecycle;
- incomplete dependency coverage даёт `UNKNOWN_IMPACT`, а не `UNAFFECTED`;
- optional unavailable member допускается только как явное ограничение, если
  existing Product policy это разрешает; required unavailable member блокирует
  Product Baseline Acceptance, когда policy требует его доступности;
- не введены новые Session Intent, capability, Product STM, `PIA-*` authority,
  automatic reconciliation или automatic projection regeneration.

## Change Review lifecycle

Change Review остаётся отдельным orchestration lifecycle для проверки изменений
до принятия нового baseline:

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

## Finding Lifecycle & Progress Reporting

Последнее принятое расширение делает эволюцию Architecture `RF-*` и Code
Quality `CQ-*` findings явной между принятыми baseline, сохраняя owner
authority. Identity finding стабильна; принятый owner lifecycle использует
`ACTIVE`, `RESOLVED` и `SUPERSEDED`, а derived progress — `NEW`, `RESOLVED`,
`REOPENED`, `SUPERSEDED`, `SEVERITY_INCREASED` и `SEVERITY_DECREASED`.

Disposition, `remediation_status` и freshness остаются отдельными измерениями.
`ACCEPTED_RISK` не означает `RESOLVED`. Отчёт или projection не могут разрешить
finding: для resolution требуются accepted owner evidence, revalidation или
adjudication.

Результаты разделяются на `CURRENT STATE`, `PROGRESS SINCE PREVIOUS ACCEPTED
BASELINE`, `HISTORICAL` и `RESIDUAL ACCEPTED RISK`. Изменение severity не создаёт
новый finding, reopening не создаёт новую identity, supersession не является
resolution, accepted risk не является resolution, а historical count не равен
current count.

Если finding resolved на baseline `B`, затем dependency/source advances to `C`
без revalidation, историческое resolution на `B` сохраняется, но resolution
для current `C` не утверждается и требуется `RESOLUTION_REVALIDATION_REQUIRED`.
ACTIVE finding при advancement source/binding без revalidation остаётся видимым
с stale/limited qualification; он не удаляется молча. Stale resolution не
синтезирует `ACTIVE` автоматически.

Product views квалифицируют состояние child findings; Product не становится
finding lifecycle authority. Недоступный Product member даёт limitation /
`LIMITED` / `UNKNOWN` aggregate, где применимо, и не вносит фиктивные `zero`,
`UNCHANGED` или `verified absence`.

CFV-1 строит SHA-256 digest из canonical semantic payload. Markdown wording,
row ordering и workspace path digest не меняют; severity, lifecycle,
disposition, freshness qualification, source binding, accepted owner revision и
qualification меняют его. CFV не становится новым источником истины.

## Promotion evidence

### Finding Lifecycle & Progress Reporting

```text
approved implementation base:
ffd9fe969340dd4566f2b503979d7f9f908a5c98

reviewed feature head:
996ba6b5a79a39caa284dab7d454f80ae6df0984

promotion:
FAST_FORWARD

canonical semantic head:
996ba6b5a79a39caa284dab7d454f80ae6df0984
```

Implementation review: `APPROVE / READY_FOR_PROMOTION`.

```text
HIGH: 0
MEDIUM: 0
LOW: 1

remaining remediation:
NONE REQUIRED FOR PROMOTION
```

### Federated Product Audit Coordination

```text
approved design remediation:
e8494f720d2cca7d53b57a4da08ed21dc9ca609a

approved implementation plan remediation / implementation base:
9bf5c4c33034826a916b88b033ee4b8f1011bc18

approved feature head:
9422f77c9cc0c2ecdcc66c217ce7006d4e57ff49

feature promotion merge:
adb576e16067ec3113182f5b4f9a865a4ca7e062
```

Independent implementation review: `APPROVE / READY_FOR_PROMOTION`.
Remaining findings: `0 HIGH / 0 MEDIUM / 0 LOW`.
Promotion completed without conflicts; feature ancestry and promoted contract
checks passed before push to canonical `main`.

### Change Review & Baseline Reconciliation

```text
approved design head:
bc3d7410652a3c73ddb74da6de7e49a1815ec5b9

approved plan head:
e61f53ba560b50d3ca21475b40f572c9ac8c9085

approved feature head:
d870198eacaf1c2cd4d4ff685212fdb48491c3d7

feature promotion merge:
2091a44622371bbc39fb913c00c1876d7f182dec
```

## Validation summary

```text
Finding lifecycle scenarios:         30/30 PASS
Finding lifecycle safety scenarios:   6/6 PASS
Fail-first fixtures:                 10/10 PASS
Backward compatibility:              PASS
Authority:                           PASS
YAGNI:                               PASS
Allowlist:                           PASS

Federated coordination FC scenarios: 24/24 CLOSED
Federated pressure scenarios:        13/13 PASS
Federated backward compatibility:    12/12 PASS

Change Review scenarios:             36/36 exact design mapping
Merge/reuse scenarios:               10/10 deterministic
Partial reconciliation scenarios:     5/5 deterministic
Authority barrier:                    8/8 pass
Intent routing:                      10/10 deterministic
Projection separation:                6/6 pass
Product qualification:                6/6 pass
Baseline-binding remediation:          5/5 pass
Migration:                             COMPATIBLE_EXTENSION
Harness:                               DO_NOT_BUILD_HARNESS
```

Finding lifecycle validation является contract-level Markdown validation, а не
executable runtime validation. Federated validation является contract-level
Markdown evidence и smoke checking. Она не утверждает наличие live repository crawler, SCM/PR adapter,
child workflow executor, automatic owner adjudication или runtime baseline
mutation.

## Where to read next

- [Report contract](../references/report-contract.md)
- [Идентификаторы и статусы](reference/identifiers-and-statuses.md)
- [Итоговые документы](reference/outputs.md)
- [Артефакты и состояние](reference/artifacts.md)
- [Жизненный цикл и актуальность](concepts/lifecycle-and-freshness.md)
- [Finding Lifecycle & Progress Reporting design](superpowers/specs/2026-09-16-finding-lifecycle-progress-reporting-design.md)
- [Finding Lifecycle & Progress Reporting validation](../tests/finding-lifecycle-progress-reporting-validation.md)
- [Finding Lifecycle & Progress Reporting backward compatibility](../tests/finding-lifecycle-progress-reporting-backward-compatibility.md)
- [Reuse, changes and Product coordination](guides/reuse-and-change.md)
- [Change Review guide](guides/change-review.md)
- [Session Intent reference](reference/workflows.md)
- [Product Roadmap](roadmap.md)
- [Federated Product Audit Coordination design](superpowers/specs/2026-09-11-federated-product-audit-coordination-design.md)
- [Federated Product Audit Coordination implementation plan](superpowers/plans/2026-09-11-federated-product-audit-coordination-implementation-plan.md)
- [Change Review closeout](superpowers/reviews/2026-09-11-change-review-baseline-reconciliation-closeout.md)
