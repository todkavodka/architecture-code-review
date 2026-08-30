# Litestar Review Addendum

Apply when the backend uses Litestar.

Review:

- application construction and lifespan hooks;
- dependency providers and their scopes;
- controller/router ownership and separation from domain/application logic;
- guards, authentication and authorization coverage;
- request/response DTOs, validation and serialization boundaries;
- exception handlers and public error contracts;
- middleware ordering and cross-cutting state;
- async versus blocking work;
- database/session transaction ownership and repository boundaries;
- background work and process-survival assumptions;
- cache/storage plugins and invalidation/ownership;
- WebSocket lifecycle where used;
- HTTP client/resource creation and shutdown;
- worker/process model and unsafe reliance on process-local mutable state;
- OpenAPI/docs exposure for internal or privileged routes.

Because Litestar projects vary in architecture, follow repository conventions before proposing generic controller/service/repository layering.
