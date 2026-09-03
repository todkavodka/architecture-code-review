# PS-78 — User-facing language follows the user

This scenario is a behavioral contract for user-facing localization. Runtime observations must remain separate from static contract inspection.

## Fixture

The user invokes `architecture-code-review` in Russian and asks for an architecture review. The repository has a material automated-test surface, so startup may recommend Test Review. No explicit request to answer in English is present.

## GREEN

- Menus, questions, recommendations, explanations, progress/status messages, and final user-facing narrative are written in Russian.
- Formal identifiers remain exact, including `USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, `STANDARD_FULL`, `FORENSIC`, `REVIEW_ONLY`, `REVIEW_PLUS_TARGET_ARCHITECTURE`, `REVIEW_PLUS_TARGET_AND_ROADMAP`, `OFF`, `REVIEW_PLUS_TEST_PLAN`, status tokens, API/IPC names, code identifiers, and paths.
- A formal token may be followed by a natural Russian explanation, for example `REVALIDATE — проверить изменения относительно принятой ревизии`.
- Test Review inherits the same user-facing language when attached to the umbrella workflow.
- When Test Review is invoked standalone, it uses the language of the user's current substantive request unless the user explicitly asks for another language.
- Persisted machine-oriented fields and canonical tokens may stay English where required by the contract; explanatory prose around them follows the user-facing language.

## RED

- Startup or capability menus switch to English merely because the Skill source text is English.
- Questions or recommendations are emitted in English to a Russian-speaking user without an explicit language request.
- Formal identifiers/status tokens are translated and therefore cease to be canonical.
- The response degenerates into avoidable English-Russian hybrid prose when a natural Russian technical formulation exists.

## Baseline observation

At `main@643cd628ee9d6b8b4c82bf8f1e85d7d3524f50b2`, static contract inspection shows that the umbrella `Language Contract` governs final documents but does not explicitly govern startup menus, questions, recommendations, progress/status messages, or attached capabilities. `capabilities/test-review/SKILL.md` also has no standalone user-facing language rule.

This is a contract-level RED observation only. No executable coordinator/runtime harness is available here, so it must not be reported as runtime RED or runtime GREEN.

Verdicts: `PS78_GREEN_USER_LANGUAGE_CONSISTENT` | `PS78_RED_USER_LANGUAGE_DRIFT` | `PS78_INCONCLUSIVE`
