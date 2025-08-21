### Production Ops Runbook

Operational guidance for deploying and running PingPost in production.

#### 1) Configuration

- Environment variables (recommended):
  - `SECRET_KEY` (required, strong random value)
  - `DEBUG=false`
  - `ALLOWED_HOSTS=yourdomain.com`
  - Database: `DATABASE_URL=postgres://user:pass@host:5432/dbname` (use dj-database-url or equivalent mapping)
  - Static/Media storage: paths or cloud storage credentials if applicable
- Django settings changes (production):
  - Set `DEBUG=False`, configure `ALLOWED_HOSTS`.
  - Configure database to Postgres (performance and durability).
  - Configure `CSRF_COOKIE_SECURE=True`, `SESSION_COOKIE_SECURE=True` (HTTPS only).
  - Set `SECURE_HSTS_SECONDS` and related headers when behind HTTPS.

#### 2) Build and database

- Install dependencies in a virtualenv.
- Apply migrations: `python manage.py migrate`.
- Create a superuser: `python manage.py createsuperuser`.
- Collect static files: `python manage.py collectstatic` (served by web server or CDN).

#### 3) Application server

- Choose WSGI/ASGI server:
  - WSGI (Django classic): `gunicorn PingPost.wsgi:application --bind 0.0.0.0:8000 --workers 3`
  - ASGI (for websockets/future): `uvicorn PingPost.asgi:application --host 0.0.0.0 --port 8000 --workers 3`
- Run under a process manager (systemd, Supervisor) with auto-restart and logs.

Example systemd unit (gunicorn):

```ini
[Unit]
Description=PingPost Gunicorn
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/srv/pingpost/PingPost
Environment="DJANGO_SETTINGS_MODULE=PingPost.settings"
Environment="SECRET_KEY=..."
Environment="DEBUG=False"
ExecStart=/srv/pingpost/.venv/bin/gunicorn PingPost.wsgi:application --bind 127.0.0.1:8000 --workers 3 --timeout 60
Restart=always

[Install]
WantedBy=multi-user.target
```

#### 4) Reverse proxy and TLS

- Place Nginx in front of Gunicorn/Uvicorn:
  - Terminate TLS (Let’s Encrypt or managed certs).
  - Proxy `/` to `127.0.0.1:8000`.
  - Serve `/static/` directly from the collected static directory.
  - Serve `/media/` from the media directory or proxy to object storage URLs.

#### 5) Storage

- Static: generated via `collectstatic`, served by Nginx/CloudFront.
- Media uploads: store on disk with backups, or prefer S3/GCS in production. Lock down public read as needed.

#### 6) Backups and recovery

- Database: daily logical dumps (e.g., `pg_dump`), retain for 7–30 days.
- Media: periodic snapshots or object storage versioning.
- Test restore procedures quarterly.

#### 7) Observability

- Logs: capture Gunicorn/Uvicorn and Nginx logs; centralize with journald or ELK.
- Metrics: basic host metrics (CPU, RAM, disk), 5xx/latency from Nginx.
- Health check: `/` returns JSON; can be used as a lightweight liveness/readiness probe.

#### 8) Security hardening

- Keep dependencies updated; patch regularly.
- Enforce HTTPS; set `SECURE_SSL_REDIRECT=True`.
- Set `CSRF_COOKIE_SAMESITE='Lax'` or `'Strict'` and `SESSION_COOKIE_SAMESITE` accordingly.
- Limit upload size at Nginx and validate content types in forms (future enhancement).

#### 9) Deployment steps (summary)

1. Pull new code; install dependencies
2. Run migrations
3. Collect static
4. Restart application server
5. Warm cache (if used) and verify `/` and `/tweet/`

#### 10) Troubleshooting

- 500 errors after deploy: check migrations, environment vars, and SECRET_KEY.
- Images not loading: verify media location and Nginx/static config; check file permissions.
- CSRF errors: confirm HTTPS and correct cookie settings; ensure `{% csrf_token %}` in forms (present by default).
- Auth issues: verify `ALLOWED_HOSTS` includes the domain and session cookies are not blocked.
