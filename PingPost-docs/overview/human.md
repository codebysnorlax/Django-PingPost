### Human-Friendly Video Script (read this aloud)

Hey everyone! I’m <Your Name>, and this is my CS50 final project, PingPost. You’ll see my info on the opening slide: GitHub <your_github>, edX <your_edx>, I’m in <City, Country>, and I recorded this on <Date>. Alright, let’s jump in.

[on screen: browser at /tweet/]
PingPost is a tiny, no‑nonsense microblog I built with Django. Think of it as a place to quickly “ping” a thought, with an optional image, and move on. I wanted something simple, fast, and kind of delightful to use.

First, I’ll create an account. [click Sign up]
The form is straightforward: username, email, and password twice. As I type, there’s a little password help that pops up to guide me—keeps things friendly without being in the way. [submit]

Great, I’m in. Now I’ll post my first ping. [click Ping]
I’ll write a short message, attach an image, and hit Done. [submit]
New posts show up at the top so it feels instant. If there’s an image, it’s front and center; if not, the card just stays clean and simple.

If I want to change something, I can. [click Edit]
I’ll tweak the text and save. That edit goes through only because I’m the owner; the server double‑checks that behind the scenes.

And if I’m done with a ping, I can remove it. [click Delete → confirm]
There’s a quick confirmation so I don’t delete by accident. When I’m finished for the day, I can log out from the navbar. [click Logout]

Alright, a super quick peek at the code—promise I’ll keep this short.

[on screen: settings.py]
In `settings.py`, I configured templates, static files, and media uploads. Authentication redirects send you back to the main timeline. For development I’m using SQLite so it’s zero‑setup.

[on screen: models.py]
In `models.py`, there’s just one main model: `Tweet`. It belongs to a user, has up to 250 characters of text, an optional image, and timestamps. Keeping the domain small made everything else cleaner.

[on screen: views.py]
In `views.py`, create, edit, and delete are traditional Django view functions. I used `@login_required` to guard changes, and when editing or deleting, I fetch the tweet with `user=request.user` so you can only change your own content. It’s simple and safe.

[on screen: layout.html → tweet_list.html]
Templates are Bootstrap‑based with a shared `layout.html` for the navbar and theme. The list page renders pings as cards in a responsive grid, so it looks good on a phone or a laptop.

Design‑wise, I aimed for dark, cozy colors with a purple accent, rounded corners, and subtle shadows—just enough personality, without getting in the way. Everything is server‑rendered so pages are fast and accessible, and I didn’t overcomplicate things with a front‑end framework for this version.

If I had more time, I’d add pagination or infinite scroll, user profiles with avatars, likes and comments, and a small REST API so a mobile app could talk to it. Those are all in my “future work” notes in the repo.

And that’s PingPost. It’s intentionally small, but complete: register, log in, post, edit, delete, and log out—plus a clean UI and clear code. The source and full docs are in the repository, including a setup guide if you want to run it yourself.

Thanks for watching—and thanks to the CS50 team for a great course.
