### Admin Guide

Admin access:

- Create a superuser: `python PingPost/manage.py createsuperuser`
- Admin site at `/admin/` (default Django admin).

Common tasks:

- Manage users via `auth.User`.
- Inspect and edit `Tweet` records if needed.

Maintenance:

- Backup `db.sqlite3` and `media/` regularly in production.
