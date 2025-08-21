### Bug Report (Deep Analysis)

This report enumerates observed defects and risky pitfalls in the current codebase, with reproduction steps, impact, and proposed fixes. Code citations include file paths and line ranges for precision.

#### 1) CSS variables not applied due to invalid selector

Evidence:

```4:16:PingPost/static/css/theme.css
::root {
  --pp-bg: #140a14;
  --pp-surface: #1e0f1f;
  --pp-surface-2: #2a1830;
  --pp-text: #f4f1f6;
  --pp-text-dim: #c8bfd0;
  --pp-accent: #7d2b58;
  --pp-accent-2: #9c3b6d;
  --pp-danger: #e05252;
  --pp-success: #2bb673;
  --pp-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
  --pp-radius: 16px;
}
```

Expected: `:root` (single colon). Actual: `::root` (double colon) is invalid, so the entire rule is ignored and CSS variables are not defined.

Impact: Any property using `var(--pp-*)` may be dropped by the browser, causing inconsistent or missing styling (e.g., buttons, cards, background).

Fix: Change `::root` → `:root`.

Severity: High (global styling correctness).

Repro: Open any page and inspect elements with `var(--pp-*)` properties; computed styles may show unset values and dropped declarations.

#### 2) Dark-theme selector never matches

Evidence:

```18:23:PingPost/static/css/theme.css
[data-bs-theme="dark"] html {
  background: var(--pp-bg);
}
```

Markup sets `data-bs-theme` on the `html` element:

```1:18:PingPost/templates/layout.html
<html lang="en" data-bs-theme='dark'>
```

Selector `[data-bs-theme="dark"] html` means “an `html` element nested inside an element with that attribute.” The `html` element has no parent, so this never matches.

Impact: Theme background and any other rules scoped this way never apply.

Fix: Use `html[data-bs-theme="dark"] { ... }`.

Severity: Medium–High (affects theme application).

#### 3) External CDN resources include questionable SRI hashes

Evidence:

```8:12:PingPost/templates/layout.html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet"
  integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
...
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"
  integrity="sha384-ppQhHc4t8l2o8pQZVn1B2u4Q3Xq3Z2X2t2T2R2wz7vQ0X2D1l1Z1l" crossorigin="anonymous"></script>
```

The SRI hashes do not look like official values. With an incorrect `integrity` attribute, browsers will block the resource.

Impact: Bootstrap CSS/JS may silently fail to load, breaking layout or components.

Fix options:

- Replace with official SRI hashes for the exact version.
- Or remove `integrity` (less secure) until correct values are provided.

Severity: Medium (may be masked by custom CSS, but still risky).

Repro: Check DevTools console for “Failed to find a valid digest in the 'integrity' attribute” errors.

#### 4) Unused import in URLConf

Evidence:

```17:30:PingPost/PingPost/urls.py
from django.contrib.auth.urls import views as auth_views
```

`auth_views` is not referenced.

Impact: Minor lint/clarity issue.

Fix: Remove the unused import.

Severity: Low.

#### 5) Typo/misnamed setting: `STATICS_URL`

Evidence:

```118:135:PingPost/PingPost/settings.py
STATIC_URL = 'static/'
...
STATICS_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

`STATICS_URL` is not a Django setting and appears to be a typo/misleading duplicate.

Impact: Confusion for maintainers; no functional effect (unused).

Fix: Remove `STATICS_URL`.

Severity: Low (cleanliness).

#### 6) LOGIN_URL missing trailing slash (redirect quirk)

Evidence:

```131:135:PingPost/PingPost/settings.py
LOGIN_URL = '/accounts/login'
```

Django’s included auth URLs expose login at `/accounts/login/` (trailing slash). Without `APPEND_SLASH=False`, Django will typically 301 redirect to the trailing slash, but mismatches can lead to surprising redirects.

Impact: Minor UX quirk and potential confusion if reverse-generated URLs differ.

Fix: Use `LOGIN_URL = '/accounts/login/'`.

Severity: Low.

#### 7) Template file name typo: `tweet_conform_delete.html`

Evidence: File name contains “conform” instead of “confirm”.

Impact: None functionally (referenced consistently), but confusing to contributors.

Fix: Rename file and update reference in `tweet_delete` view and any links.

Severity: Low.

#### 8) Mixed/duplicate font strategy in theme

Evidence:

Top of file imports Poppins and sets it as body font, but later overrides body font to Inter:

```2:36:PingPost/static/css/theme.css
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap");
...
34:36: font-family: "Poppins", ...
...
246:251:PingPost/static/css/theme.css
font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
  Arial, sans-serif;
```

Impact: Inconsistent typography; extra font downloads.

Fix: Choose one primary font family and remove the conflicting rule.

Severity: Low (visual polish).

#### 9) Registration password help panel JS edge cases

Evidence:

```1:16:PingPost/static/js/hint.js
var pwdField = document.querySelector(".field-with-help input");
var help = document.querySelector(".field-with-help .field-help");
```

If the register form structure changes (e.g., multiple inputs inside `.field-with-help`), selector becomes ambiguous. Current markup is fine, but brittle.

Impact: Potential UI regression on future template changes.

Fix: Narrow selector to the specific password field (e.g., by name or id), or bind via a data attribute.

Severity: Low.

#### 10) Media handling lacks validation and size limits

Evidence: `TweetForms` does not validate file type/size; `ImageField` will accept any image-like file but not enforce size or content type beyond Pillow decoding.

Impact: Large files or unexpected formats could be uploaded, affecting performance, storage, or security (e.g., image bombs).

Fix: Add form validators for content type and max size; enforce server-side limits and reverse proxy size limits in production.

Severity: Medium (operational risk).

#### 11) Repository hygiene: large media under VCS

Evidence: Numerous images under `PingPost/media/photos/` checked into git.

Impact: Repository bloat; slower clones; potential licensing/privacy concerns.

Fix: Remove media from VCS; add `media/` to `.gitignore`; keep only sample seed images if needed.

Severity: Low–Medium (DX/ops).

#### 12) Tests missing

Evidence: `tweet/tests.py` empty.

Impact: Changes risk regressions without automated coverage.

Fix: Add basic tests for create/edit/delete flows, ownership enforcement, and auth redirects.

Severity: Medium (quality risk).

#### 13) Hard-coded SECRET_KEY in settings

Evidence:

```22:29:PingPost/PingPost/settings.py
SECRET_KEY = 'django-insecure-...'
```

Impact: Unsafe for non-local use.

Fix: Load from environment in production; do not commit real keys.

Severity: High (security) if deployed.

#### 14) Minor: unused `index.html`

Evidence: `tweet/templates/index.html` exists while its route is commented out in `tweet/urls.py`.

Impact: None; dead code.

Fix: Remove or wire it properly.

Severity: Low.

---

Known non-bugs (by design):

- Public tweet listing without authentication is intentional.
- Server-rendered HTML flows over REST API for v1 scope.
