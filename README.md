## PingPost
Ping-Post is a micro (temporary) blogging app where users can share short messages ("pings") along with pictures, similar to Twitter or Instagram Threads.


#### Description

PingPost is designed to make posting quick thoughts easy and distraction-free. Users can write short text updates (up to 250 characters), add a photo, and view all posts in a clean timeline. Each user manages their own posts—create, edit, or delete—while the public timeline shows everyone’s updates in reverse order. With Django handling authentication, CSRF protection, and password validation, the app stays secure and reliable. The interface is built with Bootstrap 5, keeping the design responsive and minimal. Overall, PingPost focuses on clarity, usability, and solid Django fundamentals without unnecessary complexity.

### Features

- Create short text posts (+ optional photo)
- Public timeline of all posts
- Login & registration with secure password rules
- Edit & delete only your posts

### Project Structure

- Here’s how the code is organized:
- PingPost/manage.py → Django entry point
- PingPost/PingPost/ → Project settings & main URLs
- PingPost/tweet/ → Core app (models, forms, views, templates)
- PingPost/templates/ → Shared layouts + auth pages
- PingPost/static/ → CSS + JS files
- PingPost/media/ → Uploaded photos (dev only)

<!-- ### Why this design? -->

The goal was clarity over complexity. Everything revolves around one model: Tweet.

Django handles authentication, sessions, and CSRF protection out of the box

Ownership checks make sure only the author can edit/delete their posts

Bootstrap handles responsiveness with almost no extra CSS

SQLite is the default database so you can run it right away. Later, it could be upgraded with profiles, likes, comments, or even a REST API.


#### Video Demo

Video Demo: <link soon>
