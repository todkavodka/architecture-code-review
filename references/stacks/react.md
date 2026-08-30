# React Frontend Review Addendum

Apply to React frontends, including those embedded in Tauri or Electron.

Review:

- routing, top-level providers and application initialization;
- server state versus application state versus local UI state;
- duplicated or derived state stored unnecessarily;
- effect lifecycle, cleanup, stale closures, repeated subscriptions and requests after unmount;
- async request cancellation and race conditions between navigation/state changes and responses;
- excessive global context/store ownership;
- component responsibilities and business rules embedded in presentation code;
- data-fetching/cache strategy and invalidation;
- error/loading/empty states and error boundaries where appropriate;
- unsafe HTML, URL handling and user-provided content;
- localization, interpolation and hardcoded user-visible strings;
- accessibility for important workflows;
- large-list virtualization only where data volume justifies it;
- type assertions, `any`, non-null assertions and runtime validation at untrusted boundaries;
- frontend/native or frontend/API contract duplication.

Do not treat render counts or component length as findings without demonstrating actual complexity, performance or ownership impact.
