# User-facing Language Contract — Validation Record

## Scope

Behavioral change: user-facing menus, questions, recommendations, explanations, progress/status messages, and final narrative follow the user's language across the umbrella workflow and Test Review, while canonical identifiers remain unchanged.

## Baseline

```text
baseline: main@643cd628ee9d6b8b4c82bf8f1e85d7d3524f50b2
scenario: PS-78
observation_type: static contract inspection
result: RED
```

The baseline umbrella `Language Contract` constrained final-document prose but did not explicitly govern startup menus, questions, recommendations, progress/status messages, or attached capabilities. Standalone Test Review had no user-facing language rule.

This is not a runtime RED claim.

## Candidate

```text
umbrella_contract_commit: c83e63aae3b574008597255873b97957c61c7447
test_review_contract_commit: 7c4dd28dbcc12a1652b4c2eca5747e0e83e1342e
scenario: PS-78
observation_type: static contract inspection
```

Static contract predicates:

- user language selection is explicit and deterministic: PASS;
- explicit user language request wins: PASS;
- menus/questions/recommendations/explanations/progress/final narrative are covered: PASS;
- attached Test Review inherits umbrella language: PASS;
- standalone Test Review follows the current user request language: PASS;
- formal identifiers/status tokens/code/path/API names remain canonical: PASS;
- localized explanation may follow a canonical token: PASS;
- Skill source language cannot silently force English UI: PASS;
- language switch affects subsequent user-facing responses without rewriting persisted artifacts by default: PASS.

## Runtime pressure

```text
result: INCONCLUSIVE
reason: no executable coordinator/runtime harness was used for this change
```

No runtime GREEN claim is made. PS-78 is statically satisfied by the published contracts; behavioral runtime confidence still requires a future fresh-agent pressure run if one is available and useful.
