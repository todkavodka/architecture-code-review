# Независимая проверка кандидатов

Этот файл определяет Independent Verification (независимую проверку) discovery-кандидатов. Discovery output — это гипотезы; verifier должен заново проверить код/путь и попытаться опровергнуть вывод.

## 1. Вход

Verifier получает:

- exact repository baseline;
- `working/INDEX.md`;
- список `CAND-*` и ссылки на исходные working artifacts;
- принятую As-Built Architecture;
- relevant positive controls/open questions;
- узкую задачу: подтвердить/исправить/опровергнуть candidates, не проектировать remediation.

Не доверяй формулировке кандидата только потому, что она появилась в предыдущем pass.

## 2. Допустимые исходы

```text
CONFIRMED
CORRECTED
REFUTED
UNVERIFIED
NEW_ADJACENT
```

`NEW_ADJACENT` допустим, если проверка конкретного кандидата обнаружила соседний механизм. Не превращай verification в новый бесконтрольный discovery pass.

## 3. Минимальный falsification contract

Для каждого кандидата явно спроси:

- состояние/ресурс действительно shared?
- global scope намеренный?
- существует ли guard на другом слое/path?
- alleged stale completion реально достижим?
- event/boundary уже переносит owner/request identity?
- consumer действительно теряет эту identity?
- выбранное состояние snapshot или live observable?
- resource fixed globally или изолирован другим mechanism?
- cleanup реально не awaited или runtime гарантированно ждёт?
- security entry point достижим attacker-controlled input?

Если falsification требует неизвестного product intent — не выдумывай его; зафиксируй open question / `PENDING_PRODUCT_INTENT` downstream.

## 4. Evidence shape

Для `CONFIRMED`/`CORRECTED` укажи:

```text
candidate ID
current mechanism
reachable path/scenario
code evidence
falsification attempted
why guard/alternative does not invalidate it
concrete effect
result
```

Для `REFUTED` обязательно объясни точный falsifier, а не просто «не подтвердилось».

Для `UNVERIFIED` укажи, какой evidence отсутствует/недоступен.

## 5. Correction propagation

Если механизм исправлен относительно раннего pass:

```text
old statement
→ corrected statement
→ evidence
→ affected candidate/findings searched
→ stale contradictory wording marked superseded
```

Известный тип ошибки: интуитивная модель library/runtime semantics (`once`, cancellation, shutdown) вместо фактической semantics. При сомнении проверяй реальные API guarantees/code behavior.

## 6. Роль verification

Verification отвечает на вопрос **«это реально так?»**.

Он не должен:

- назначать окончательную severity;
- объединять разные mechanisms под красивый root без root-boundary gate;
- проектировать Target Architecture;
- переписывать As-Built напрямую;
- считать absence evidence доказательством дефекта.

## 7. Handoff

Рабочий verification artifact заканчивается persisted `HANDOFF SUMMARY` по contract из `review-modes-and-orchestration.md`, включая outcome каждого `CAND-*`, новые `AC-*`/`OQ-*` и supersessions.
