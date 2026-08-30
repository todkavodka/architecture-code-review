# Tauri Review Addendum

Apply when the project contains Tauri/Rust native code.

Review:

- `tauri.conf.*`, capabilities, permissions, plugin scopes and least privilege;
- command registration, request/response types and whether commands contain business logic rather than acting as boundary adapters;
- frontend `invoke` usage and whether command names/contracts are centralized and typed;
- events/channels, listener cleanup, duplicate subscriptions, payload typing and event-name consistency;
- shared `State<T>`, `Arc`, `Mutex`, `RwLock`, ownership across windows/sessions and locks across `.await`;
- Tokio task lifecycle, cancellation, `spawn_blocking`, orphan tasks and shutdown;
- shell/process/sidecar execution, executable paths, argument validation and child cleanup;
- filesystem/dialog/opener/deep-link/updater permissions and validation;
- secrets crossing the webview/native boundary;
- Rust error types versus serialized user-facing error contracts;
- DTO drift between Rust and TypeScript;
- updater signing and release behavior where present;
- multi-window lifecycle and second-instance behavior where relevant.

Useful safe checks when defined by the project include `cargo fmt --check`, `cargo clippy --all-targets --all-features`, `cargo check`, `cargo test`, frontend lint/typecheck/tests/build and the repository's Tauri build/check command. Do not invent flags that conflict with project policy.
