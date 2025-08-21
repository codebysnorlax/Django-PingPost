### Non-Functional Requirements

- Usability: Clean, responsive UI using Bootstrap; accessible navigation and clear actions.
- Security: CSRF protection on forms; password validation via Django defaults; object-level access control.
- Performance: Page loads under ~1s on local dev with <1k tweets; server-rendered pages.
- Maintainability: Clear app boundaries; minimal custom glue; conventional Django patterns.
- Portability: SQLite by default; easy migration to Postgres.
- Observability: Simplicity of logs and predictable error states in development.
