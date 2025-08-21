### Installation Guide

Prerequisites:

- Python 3.12+
- pip and virtualenv (recommended)
- SQLite (default, bundled)

Steps:

1. Clone repository and enter directory.
2. Create and activate a virtual environment.
3. Install dependencies from `requrements.txt`.
4. Run migrations.
5. Start the development server.

Commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requrements.txt
python PingPost/manage.py migrate
python PingPost/manage.py runserver
```

Open `http://127.0.0.1:8000/tweet/` to browse pings. Register an account at `/tweet/register/` to start posting.


Optional:

- Create a superuser for admin: `python PingPost/manage.py createsuperuser`
- Configure `DEBUG`, `ALLOWED_HOSTS`, static/media for production.
