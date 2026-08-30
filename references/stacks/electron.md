# Electron Review Addendum

Apply when the project contains Electron main/preload/renderer code.

Review:

- separation of main, preload and renderer responsibilities;
- `contextIsolation`, `nodeIntegration`, sandboxing and webPreferences;
- `contextBridge` surface area and whether privileged APIs are narrowly exposed;
- `ipcMain`/`ipcRenderer` contracts, validation, authorization and handler cleanup;
- remote content, navigation, `window.open`, external URLs and protocol/deep-link handling;
- filesystem and shell/process access from renderer-facing paths;
- BrowserWindow creation/destruction, multi-window state and event listener cleanup;
- tray, menu, global shortcuts, second-instance and quit-versus-hide lifecycle;
- session partitions, cookies, tokens and credential storage;
- autoUpdater/download/install/restart lifecycle and signature assumptions;
- renderer CSP and unsafe HTML/content insertion;
- child processes, sidecars and cleanup;
- duplicated truth between renderer state, main-process state and persistent storage.

Trace at least one flow across renderer → preload → IPC → main/service → external side effect → response.
