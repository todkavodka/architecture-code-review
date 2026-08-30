# Django Review Addendum

Apply when the backend uses Django.

Review:

- project/app boundaries and whether domain responsibilities align with Django apps;
- settings split, secrets, environment handling and deployment defaults;
- middleware ordering and hidden cross-cutting behavior;
- authentication, authorization and object-level access control;
- CSRF, CORS, sessions, cookies and trusted origins;
- ORM ownership, transaction boundaries, `select_for_update`, N+1 queries and accidental queries in loops/templates;
- model/service/view responsibility and business logic trapped in views/signals/models without clear ownership;
- signals causing implicit side effects, recursion or order dependencies;
- migrations, data migrations, irreversible operations and startup assumptions;
- Celery/background-task lifecycle if present;
- caching and cache invalidation;
- file/media upload validation and storage security;
- admin exposure and privileged actions;
- DRF serializers/viewsets/permissions if DRF is present;
- request lifecycle, exception mapping and logging of sensitive request data.

Review Django-specific security settings in the context of the actual deployment rather than requiring every hardened setting in local development.
