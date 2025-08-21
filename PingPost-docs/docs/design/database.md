### Database Design

Relational schema (SQLite by default):

- auth_user: built-in Django users
- tweet_tweet:
  - id (PK)
  - user_id (FK → auth_user.id, on delete cascade)
  - text (TEXT, <= 250 chars validated at form level)
  - photo (VARCHAR path to media/photos/*)
  - created_at (DATETIME, auto_now_add)
  - updated_at (DATETIME, auto_now)

Indexes:

- Implicit PK index on `id`.
- Implicit FK index on `user_id`.
- Query pattern orders by `-created_at`; consider adding an index on `created_at` for large datasets.

Migrations: Tracked in `tweet/migrations/` with initial migration `0001_initial.py`.
