### API Design

PingPost is primarily server-rendered. A minimal JSON endpoint exists at `/` for a health-style response.

Public endpoints:

- `GET /` → JSON: `{ status, message, user, Hint }`
- `GET /tweet/` → HTML: list of tweets
- `GET /tweet/create/` → HTML form (auth required)
- `POST /tweet/create/` → Create tweet (auth required)
- `GET /tweet/<id>/edit/` → HTML form (owner)
- `POST /tweet/<id>/edit/` → Update tweet (owner)
- `GET /tweet/<id>/delete/` → Confirm delete (owner)
- `POST /tweet/<id>/delete/` → Delete tweet (owner)
- `GET /tweet/register/` → Registration form
- `POST /tweet/register/` → Create account
- `GET /accounts/login/` → Login form
- `POST /accounts/login/` → Login
- `POST /accounts/logout/` → Logout

Authentication: Django session cookies; CSRF tokens on POST.

Error handling: standard Django 403 for permission issues (guarded via view decorators and ownership filters).
