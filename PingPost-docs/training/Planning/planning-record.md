### CS50 Final Project Video – Recording Plan (Linux)

This plan helps you record a polished, <= 3-minute video for CS50’s final project requirement. See the official guidance for what to include in the video intro and how to submit: [CS50 Final Project Requirements](https://cs50.harvard.edu/x/project/).

#### CS50 video requirements (key points)

- Length: no more than 3 minutes.
- Opening must include: project title, your name, your GitHub and edX usernames, your city/country, and the recording date.
- Demonstrate your project in action (screen capture is fine). After recording, upload to YouTube (unlisted is OK) and include the URL in your README.

#### Tools on Linux (choose one)

- OBS Studio (recommended): pro-quality, scenes/sources, audio filters.
  - Install (Ubuntu/Debian): `sudo apt update && sudo apt install obs-studio -y`
- SimpleScreenRecorder: lightweight alternative.
  - Install: `sudo apt update && sudo apt install simplescreenrecorder -y`
- GNOME Screen Recorder (built-in on some desktops): minimal features.

#### OBS recommended settings

- Canvas/Output resolution: 1920×1080 (or your display native); FPS: 30.
- Output → Recording: MKV (safer) or MP4; bitrate ~6–8 Mbps for 1080p.
- Audio: select your microphone; add Noise Suppression and Compressor filters.
- Scene setup:
  - Source 1: Window Capture (browser – Chrome/Firefox)
  - Source 2: Window Capture (terminal)
  - Optional: Display Capture (fallback)
  - Optional: Video Capture Device (webcam) in a small corner.

#### Pre-record checklist

- Close unrelated apps and notifications (Do Not Disturb on).
- Increase system font scaling if needed for readability.
- Prepare demo data: Have at least one image in a known folder to upload.
- Open a clean browser window (incognito) for auth flows.
- Start backend:
  - Option A (project root): `cd ~/Projects/CS50_FP/PingPost/PingPost && python manage.py runserver`
  - Option B (from repo root): `python PingPost/manage.py runserver`
- Verify:
  - `http://127.0.0.1:8000/` returns JSON hint.
  - `http://127.0.0.1:8000/tweet/` shows the tweet list.

#### On-screen flow (timeboxed)

- 0:00–0:12: Opening slate (title, your name, GitHub + edX usernames, city/country, date).
- 0:12–0:20: Quick purpose statement: what PingPost is.
- 0:20–1:35: Live demo (register → create → edit → delete → logout).
- 1:35–2:35: Architecture/code highlights (very brief): folders, model, views, templates, security checks.
- 2:35–2:55: Future work and design choices.
- 2:55–3:00: Closing (where to find code + docs).

#### Detailed action plan

1) Browser at `/` JSON → navigate to `/tweet/`.
2) Click Sign up → fill username, email, password (show password help appears), submit.
3) Click Ping → type short text, attach image → Done → see new card at top.
4) Click Edit on your card → change text → Done.
5) Click Delete → confirm.
6) Navbar → Logout.
7) Switch to editor briefly:
   - Show `PingPost/PingPost/settings.py` (templates, media, auth redirects).
   - Show `PingPost/tweet/models.py` (Tweet model fields).
   - Show `PingPost/tweet/views.py` (ownership filtering on edit/delete).
   - Show `PingPost/templates/layout.html` (navbar, theme include).

Keep code views very short; focus on 1–2 sentences per file.

#### Voice and pacing tips

- Speak clearly, 130–150 words per minute; keep sentences short.
- Use present tense and emphasize the “why.”
- Don’t read file contents aloud; summarize what they do.

#### After recording

- If recorded as MKV in OBS, use “Remux Recordings” to convert to MP4.
- Upload to YouTube as Unlisted; copy URL.
- Add the URL to the top of `README.md` (Video Demo section) and ensure it matches CS50’s instructions.
- Double-check length ≤ 3 minutes.

#### Troubleshooting

- No audio: confirm the right mic in OBS; watch the mixer meters.
- Choppy video: lower resolution (1280×720) or FPS to 30; close heavy apps.
- Glitchy fonts: disable fractional scaling; use browser zoom 110–125%.

#### Submission notes

- Reconfirm requirements and deadlines on CS50’s page: [CS50 Final Project Requirements](https://cs50.harvard.edu/x/project/).
- Keep a local copy of the video and your OBS profile for re-recording if needed.
