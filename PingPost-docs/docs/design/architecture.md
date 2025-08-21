### Architecture

PingPost follows a layered Django MVC (Model-Template-View) architecture:

- Presentation: Django templates with Bootstrap 5 and a global `layout.html`.
- Application: View functions in `tweet/views.py` orchestrate form handling and redirection.
- Domain: `Tweet` model encapsulates core data; business rules are simple and enforced in views/forms.
- Data: SQLite database with a single `tweet_tweet` table and Django auth tables; media files on disk.

Components and boundaries:

- `PingPost/PingPost/urls.py` is the composition root, wiring sub-routers and auth.
- The `tweet` app is self-contained: `urls.py`, `views.py`, `forms.py`, `models.py`, and templates.
- Static files are served via `STATICFILES_DIRS` in dev; media is exposed with `static()` for local development only.

Runtime behavior:

- Requests enter via URLconf, land in a view, which loads/saves ORM entities via forms, then renders a template or redirects.
- Authentication is enforced via `@login_required` and ownership filtering.

Scalability considerations:

- Stateless views enable horizontal scaling; session storage remains default (DB-backed) for simplicity.
- For production, switch to Postgres, a cloud media store (e.g., S3), and a real web server (ASGI/WSGI).
