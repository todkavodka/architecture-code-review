# PS-55 fixture

This is a deliberately small review fixture for finding-materiality testing.

It is not production code and is not intended to be secure.

The reviewer should reason from code evidence, not from this README's labels.

Run target: static architecture/code review only. No network service needs to be started.

Files:

- `app.py` — request handlers and authentication context.
- `db.py` — document reads, one unsafe raw SQL path, one safe raw-looking path.
- `outbound.py` — outbound HTTP target with intentionally incomplete provenance.
- `maintenance.py` — duplicated helpers and TODO markers.
- `large_module.py` — repetitive but behaviorally harmless data declarations.
- `models.py` — simple data model.
