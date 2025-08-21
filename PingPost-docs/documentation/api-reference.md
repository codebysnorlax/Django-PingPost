### API Reference

This project is primarily HTML-based. The following endpoints and parameters are relevant to form submissions.

- POST `/tweet/create/`
  - Fields: `text` (string, required, <=250), `photo` (file, optional)
- POST `/tweet/<id>/edit/`
  - Fields: same as create
- POST `/tweet/<id>/delete/`
  - No fields; CSRF token required
- POST `/tweet/register/`
  - Fields: `username`, `email`, `password1`, `password2`
- POST `/accounts/login/`
  - Fields: `username`, `password`

Responses are redirects or rendered HTML. CSRF token is required on all POSTs.
