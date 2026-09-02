# Ansible Review Addendum

Apply when the reviewed scope contains Ansible playbooks, roles, inventory, vars,
templates, or Ansible-driven deployment configuration.

Review, where material:

- playbook/role responsibility boundaries;
- inventory, groups, and host targeting;
- variable precedence and configuration ownership;
- handlers and restart/lifecycle semantics;
- task and role idempotency;
- `changed_when` / `failed_when` behavior;
- `become` and privilege boundaries;
- vault/secrets exposure and propagation;
- template-generated runtime configuration;
- retries, `delegate_to`, `run_once`, and `serial`/rolling execution;
- check-mode limitations;
- collection/module/artifact pinning and reproducibility;
- partial application and deployment-failure behavior.

These are evidence-collection prompts, not automatic findings. Run syntax-check,
lint, or check-mode validation only when the project defines those safe checks;
do not mandate a deployment or other destructive execution.
