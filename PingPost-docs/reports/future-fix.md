### Future Fixes and Enhancements (Prioritized)

This document lists actionable fixes for current defects and near-term enhancements to improve robustness, security, and UX. Items reference the bug report where applicable.

#### Priority 0 — Critical styling/security correctness

1) CSS variable root selector (Bug #1)
- Change `::root` → `:root` in `static/css/theme.css`.

2) Dark theme selector (Bug #2)
- Update `[data-bs-theme="dark"] html` → `html[data-bs-theme="dark"]`.

3) SECRET_KEY management (Bug #13)
- Load from environment; document in ops runbook; ensure distinct dev/prod keys.

#### Priority 1 — Stability and DX

4) Bootstrap CDN SRI (Bug #3)
- Replace with official integrity hashes or pin to local files; verify in DevTools.

5) Remove unused imports and settings (Bug #4, #5)
- Delete `auth_views` import in root `urls.py`.
- Remove `STATICS_URL` from settings.

6) Align LOGIN_URL (Bug #6)
- Set `LOGIN_URL = '/accounts/login/'` to avoid redirect surprises.

7) File validation for uploads (Bug #10)
- Add validators for content type (`image/*`) and max size (e.g., 5MB) to `TweetForms` or a custom clean method.
- Add reverse proxy/body size limits in production (Nginx `client_max_body_size`).

8) Media in version control (Bug #11)
- Add `media/` to `.gitignore`; move demo assets to `static/` or a `seed/` folder.

#### Priority 2 — Quality and polish

9) Tests
- Implement tests in `tweet/tests.py`:
  - Auth redirect tests for create/edit/delete when not logged in.
  - Ownership enforcement on edit/delete.
  - Happy-path create/edit/delete.
  - Basic template rendering and context checks.

10) Rename template (Bug #7)
- `tweet_conform_delete.html` → `tweet_confirm_delete.html`; update references.

11) Typography consistency (Bug #8)
- Choose single primary font (Poppins or Inter); remove conflicting body font rule.

12) Harden password help JS (Bug #9)
- Target the password input by `id` or `name` to avoid ambiguity; fallback safely.

13) Dead code cleanup (Bug #14)
- Remove unused `index.html` or wire it under a dedicated route for a welcome page.

#### Priority 3 — Enhancements

14) Pagination and performance
- Add pagination to `/tweet/` (e.g., 12–20 per page); later consider infinite scroll.

15) Accessibility and semantics
- Ensure all interactive icons have `aria-label` and controls have accessible names.

16) Production asset pipeline
- Local vendoring or CDN with correct SRI; add `collectstatic` config in deployment.

17) Observability
- Add basic middleware or logging config for request IDs and structured logs in production.

18) API surface (future)
- Introduce DRF endpoints for listing and creating tweets; keep server-rendered UI.

19) Security headers
- In production, set HSTS, CSP (with hashes or nonces if inlined scripts are used), and referrer policy.

20) Rate limiting
- Consider rate limiting on create endpoints to prevent abuse.

#### Notes

All code changes should preserve functional behavior and pass tests. For production-only changes, guard with environment-driven settings to avoid disrupting development.
