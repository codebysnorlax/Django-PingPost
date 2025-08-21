### Backend Overview

PingPost uses Django 5.x with a single app `tweet` and the built-in `auth` app. The project follows standard Django conventions:

- `PingPost/PingPost/settings.py`: configuration (templates, static files, media, auth redirects).
- `PingPost/PingPost/urls.py`: routes top-level URLs, includes `tweet.urls`, exposes auth URLs, and serves media in dev.
- `PingPost/PingPost/views.py`: a simple JSON home endpoint for health/hint.
- `PingPost/tweet/`: app with models, forms, views, templates, and URL config.

Key server-side components:

- Model: `Tweet` with `user`, `text`, `photo`, `created_at`, `updated_at`.
- Forms: `TweetForms` for create/edit; `UserRegistrationForm` extends `UserCreationForm` with email.
- Views:
  - `tweet_list`: lists all tweets ordered by `-created_at`.
  - `tweet_create`: requires login; assigns `request.user` before save.
  - `tweet_edit`: requires login; fetches by `pk` and `user=request.user` to enforce ownership.
  - `tweet_delete`: requires login; same ownership constraint; confirms via template.
  - `register`: creates a user and logs them in.

Templates use Bootstrap 5 and a shared `layout.html`. Static assets are in `static/`, with a custom theme and a small helper JS.

Security and correctness:

- CSRF protection via Django templates `{% csrf_token %}`.
- Ownership checks in edit/delete.
- Password validation via `AUTH_PASSWORD_VALIDATORS`.

Persistence: SQLite (default) with media stored under `media/photos/`.
