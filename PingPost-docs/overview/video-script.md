### CS50 Final Project – PingPost Video Script (<= 3 minutes)

Note: Adjust names and locations. Aim for 2:45–2:55 runtime.

#### 0:00 – 0:12 Opening slate

On screen: Title card.
Narration:
“PingPost. By <Your Name>. GitHub: <your_github>, edX: <your_edx>. <City, Country>. Recorded on <Date>.”

#### 0:12 – 0:20 What PingPost is

On screen: `/tweet/` list page.
Narration:
“PingPost is a minimalist microblog built with Django. It lets you post short updates, optionally with an image, and manage your posts with a clean, responsive UI.”

#### 0:20 – 1:35 Live demo

1) Registration (0:20–0:40)
On screen: Click Sign up, fill username, email, password, submit.
Narration:
“I’ll start by creating an account. The form uses Django’s built-in password validation. Notice the floating password help for quick guidance.”

2) Create a ping (0:40–0:58)
On screen: Click Ping; enter short text and upload an image; submit.
Narration:
“I’ll create a ping with an optional image. Posts appear at the top in reverse chronological order.”

3) Edit (0:58–1:12)
On screen: Click Edit on your card; change text; Done.
Narration:
“Editing uses the same form. Ownership is enforced server-side, so you can only modify your own content.”

4) Delete (1:12–1:22)
On screen: Click Delete; confirm.
Narration:
“Deletes are confirmed and restricted to the post’s owner.”

5) Logout (1:22–1:35)
On screen: Click Logout.
Narration:
“The app uses Django’s session-based auth for login and logout.”

#### 1:35 – 2:35 Highlights from the code

Quick code tour; keep to ~15 seconds per file.

1) Settings (1:35–1:50)
On screen: `PingPost/PingPost/settings.py` – templates, static/media, auth redirects.
Narration:
“Settings configure templates, static and media files, and auth redirects. SQLite keeps development simple.”

2) Model (1:50–2:00)
On screen: `PingPost/tweet/models.py` – `Tweet` model.
Narration:
“The core model is Tweet: user, text up to 250 characters, optional image, and timestamps.”

3) Views (2:00–2:15)
On screen: `PingPost/tweet/views.py` – create/edit/delete functions.
Narration:
“Create, edit, and delete are standard Django views. `@login_required` guards mutations, and ownership is enforced with object queries filtered by the current user.”

4) Templates (2:15–2:25)
On screen: `PingPost/templates/layout.html` and `tweet_list.html`.
Narration:
“A shared base layout provides the navbar and theme. The list page renders tweets with Bootstrap cards.”

5) Security (2:25–2:35)
On screen: Any form template.
Narration:
“All forms use CSRF tokens. Passwords rely on Django’s validators and hashing.”

#### 2:35 – 2:55 Design choices and future work

On screen: `project_docs/reports/future-fix.md`.
Narration:
“I prioritized simplicity and clarity: a single domain model, server-rendered pages, and Bootstrap styling. Future work includes pagination, profiles, likes, and a REST API, as outlined in my docs.”

#### 2:55 – 3:00 Closing

On screen: Repo `README.md`.
Narration:
“This is PingPost. The source code and full documentation are in the repository. Thanks for watching.”
