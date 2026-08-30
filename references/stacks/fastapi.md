# FastAPI Review Addendum

Apply when the backend uses FastAPI/Starlette.

Review:

- application factory and lifespan startup/shutdown;
- dependency injection scopes and resources created per request versus per application;
- sync blocking work inside async routes/dependencies;
- database/session transaction ownership;
- background tasks and whether work that must survive process loss is incorrectly delegated to in-process background execution;
- authentication/authorization dependencies and route coverage;
- Pydantic request/response models, validation boundaries and accidental overexposure of internal fields;
- exception handlers and stable public error contracts;
- middleware order, CORS, proxy/header trust and request body/logging concerns;
- streaming/file upload resource limits and cleanup;
- HTTP client reuse, timeouts and shutdown;
- WebSocket lifecycle if present;
- OpenAPI exposure where sensitive/internal routes exist;
- worker/process model assumptions, shared in-memory state and startup duplication under multiple workers.

Trace at least one request from ASGI entry through dependencies, domain/application logic, persistence/external calls, response serialization and exception handling.
