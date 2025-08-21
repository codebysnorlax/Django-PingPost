### Core Concepts

PingPost is a minimal social microblog built with Django. Core concepts include:

- Users can create short text updates ("pings") with an optional image.
- Authenticated users can create, edit, and delete only their own pings.
- The public, pageless timeline lists pings in reverse chronological order.
- Authentication, authorization, and session handling rely on Django’s built-in auth.

Domain model:

- Tweet: user (ForeignKey to auth.User), text (<= 250 chars), photo (ImageField), timestamps.

Primary flows:

- Create: POST to `tweet/create/` with text and optional image; server assigns current user.
- Edit/Delete: Restricted to tweet owner via object fetch filtered by `user=request.user`.
- Register/Login/Logout: Provided via `UserCreationForm`-based registration and Django auth URLs.

Non-goals (v1): likes, comments, search, real-time updates.
