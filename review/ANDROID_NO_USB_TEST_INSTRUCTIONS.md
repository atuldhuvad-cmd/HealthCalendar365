# Android Physical Acceptance — No USB Testing Instructions

**Requirement:** Android test phone and host computer connected to the same private Wi-Fi network.

---

## 1. Build Preview Runtime Mirror

To prevent stale builds, hand-copy drift, or missing precache assets, always build the deterministic preview runtime mirror first:

```bash
python build_preview_runtime.py
```

This verifies that all 97 precache assets exist in source, copies them to `build/preview-runtime/`, and validates byte-for-byte SHA-256 parity.

---

## 2. Start the Local Server with LAN Binding

Start the local server bound to `0.0.0.0` serving the preview runtime:

```bash
python serve.py --host 0.0.0.0 --root build/preview-runtime
```

*(Optional: specify `--port 8080` if you require a fixed port).*

### Read the LAN URL Printed by the Server

When bound to `0.0.0.0`, `serve.py` automatically detects your active local Wi-Fi IPv4 address and prints:

- **Desktop URL (this PC):** `http://127.0.0.1:<PORT>/index.html`
- **Phone URL (LAN Wi-Fi):** `http://<LAN_IP>:<PORT>/index.html`
- **Origin string for Chrome flag:** `http://<LAN_IP>:<PORT>`

> [!IMPORTANT]
> **Do not hardcode or assume an IP address.** DHCP can assign a new IP address across sessions or router reconnects. Always read the exact LAN IP and port printed by `serve.py`.

---

## 3. Mandatory Origin Stability Rule

> [!CAUTION]
> **The origin (`http://<LAN_IP>:<PORT>`) must remain completely stable throughout the duration of physical device testing.**
>
> In the Web platform, a Progressive Web App's Service Worker registration, Cache Storage (`health-poster-v1.6`), and IndexedDB databases are strictly sandboxed and bound to their exact origin `(protocol, hostname, port)`.
>
> If the origin changes (e.g. from DHCP address changes, restarting on a different port, or switching tunnel hostnames), Android treats it as an entirely different website. This wipes tester state, severs service worker control, and **strictly invalidates test evidence for:**
> - **G-DEV-02** (*Installed-PWA Launch & Offline Relaunch*)
> - **G-DEV-03** (*Service-Worker Upgrade from v1.4 to Future Release*)
> - **G-DEV-10** (*Update Recovery, Cache Eviction & Data Preservation*)
>
> Keep the host computer on the same Wi-Fi lease and use the same port for all sequential test runs.

---

## 4. Enable the Temporary Secure-Origin Exception on Android

Because Service Workers require a Secure Context (HTTPS or localhost), Android Chrome requires an explicit origin exception when testing over private HTTP LAN:

1. In Android Chrome, navigate to:  
   `chrome://flags/#unsafely-treat-insecure-origin-as-secure`
2. Set the feature to **Enabled**.
3. In the text area, enter the exact origin printed by `serve.py` (e.g. `http://<LAN_IP>:<PORT>`), strictly **without** `/index.html` and without a trailing slash.
4. Tap **Relaunch** at the bottom of the screen.
5. In the relaunched browser, open the Phone URL:  
   `http://<LAN_IP>:<PORT>/index.html`

*Note: USB debugging is not required. Remove or disable the Chrome flag after testing.*

---

## 5. Evidence to Record

Use [`review/PHYSICAL_DEVICE_FINAL_CHECKLIST.md`](file:///d:/HealthCalendar365/review/PHYSICAL_DEVICE_FINAL_CHECKLIST.md). Record device model, Android OS version, Chrome version, test timestamp, PASS/FAIL status, and empirical observations for every gate. Capture mobile screenshots for:
- Home screen icon installation
- Standalone offline launch (Airplane Mode)
- Offline Gujarati font & typography rendering
- Exported posters (Square and Story)
- WhatsApp sharing preview and compression readability

---

## 6. Stop Conditions

- Mark a gate **FAIL** if the observed behavior deviates from specification.
- Every gate must remain **`NOT TESTED`** until physically executed on authentic Android hardware. Desktop emulations (Playwright / DevTools) do not sign off physical hardware gates.
