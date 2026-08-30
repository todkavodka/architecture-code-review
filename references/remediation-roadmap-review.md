# План исправлений и проверка исполнимости

Этот этап выполняется только для `REVIEW_PLUS_TARGET_AND_ROADMAP` после принятия Target Architecture.

## 1. Roadmap строится по зависимостям, не по severity

Severity помогает приоритизировать риск, но порядок реализации определяется prerequisites и безопасной активацией.

Каждая material task должна содержать:

```text
TASK ID
RF/SER addressed
target mechanism
prerequisites
invariant transition
regression test first where applicable
allowed implementation boundary
forbidden scope
verification
exit criteria
rollback/fail-closed consideration where relevant
```

Unresolved product/deployment decision блокирует только зависимые tasks.

## 2. Semantic invariant → concrete representation

Roadmap обязан переводить target semantics в реальную runtime representation.

Проверяй, например:

- semantic composite key vs equality semantics конкретного языка/Map/dictionary;
- generation/version identity vs mutable object reference;
- cancellation scope vs global abort primitive;
- ownership model vs actual storage/index keys;
- durable idempotency vs process-local memory.

Красивый semantic type не гарантирует правильное runtime behavior.

## 3. Dependency isolation

Не создавай global phase gate, если решение влияет только на несколько tasks.

Нормально:

```text
Decision D2
→ blocks TASK-61 only

Independent TASK-31/32
→ may proceed
```

Неправильно: весь phase блокируется всеми decisions «для простоты».

## 4. Safe activation boundary

Для security/ownership/lifecycle changes явно опиши допустимое intermediate state.

Примеры риска:

- fake verifier существует до production trust authority и случайно активирует execution;
- новый auth path включён до миграции identity/state;
- новый cancellation protocol частично активирован и оставляет старый global cancel;
- signing/checksum enforcement включён несогласованно.

Если безопасной промежуточной комбинации нет — активируй зависимые production pieces атомарно или сохраняй fail-closed/old-safe behavior до полного cutover.

Test fake/fixture никогда не становится production trust authority.

## 5. Execution Consistency Review

Fresh-context reviewer проверяет цепочку:

```text
semantic invariant
→ concrete runtime representation
→ dependency isolation
→ safe production activation boundary
```

Также проверяет:

- task покрывает реальный RF/SER/target, а не новый scope;
- regression test реально проверяет mechanism;
- dependencies acyclic/объяснимы;
- task boundary достаточно мала для отдельного review;
- product decision не спрятан как implementation detail;
- platform/deployment constraints учтены;
- rollback/fail-closed behavior определён для risky activation.

## 6. Review lifecycle

```text
roadmap author
→ self-check
→ fresh-context execution-consistency review
→ ROADMAP_ACCEPTED
   or ROADMAP_CORRECTION_REQUIRED
      → separate correction pass
      → fresh-context re-review
      → ACCEPTED | BLOCKED
```

Reviewer формирует issues, а не редактирует roadmap сам.

## 7. Acceptance

Roadmap accepted только когда:

- все material RF/SER target coverage traceable;
- tasks имеют concrete representation и verification;
- independent tasks не блокируются unrelated gates;
- unsafe intermediate activation не допускается;
- unresolved decisions изолированы;
- correction/re-review history сохранена;
- нет placeholders `TBD/TODO/implement later` в executable parts.
