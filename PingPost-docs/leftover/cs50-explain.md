### CS50 Final Project — What to Know Before You Start

This guide distills the official requirements and practical tips for CS50’s final project. Always defer to the course page for the source of truth: [CS50 Final Project Requirements](https://cs50.harvard.edu/x/project/).

#### What the final project is

- The capstone for CS50x: build a piece of software that draws on the course’s lessons. Tech stack is your choice (language, frameworks, infrastructure) as long as the work is your own and you learn from it.
- You may work solo or in a group of 2–3; group scope should be proportionally larger than a solo project.
- Staff audits submissions; academic honesty policies apply, and violations can result in removal from the course and revocation of certificates.

#### Ideas and scope

- Example categories: web apps (JavaScript/Python/SQL), iOS/Android apps, games, browser extensions, CLI tools, or hardware-based projects.
- Keep scope realistic. Define a “good,” “better,” and “best” outcome up front. Expect tasks to take longer than planned.

#### Planning checklist (before you code)

- What will it do? Who is it for? Why does it matter?
- Core features vs stretch goals; how will you execute it? (architecture, data, UI)
- What new skills do you need? What will you research?
- If collaborating, split responsibilities clearly.
- Define milestones and a short, written roadmap.

#### AI tools policy (final project only)

- You may use AI tooling (e.g., ChatGPT, Copilot) for the final project, but the essence of the work must be your own. Treat AI as an assistant, not a substitute.
- Cite any AI assistance in your code comments. Be specific about where and how it helped.

#### Directory and environment

- If using the CS50 Codespace, create a `project/` directory for your code and artifacts. You may also develop locally or elsewhere.
- Keep your repository tidy: avoid committing build artifacts or large media. Target total submission size under ~100MB.

#### Deliverables overview (three steps)

1) Video presentation (≤ 3 minutes)
2) README.md at your project root
3) Submission via `submit50` and Gradebook confirmation

##### 1) Video presentation (required)

- Length: no more than 3 minutes.
- Your video must begin with an opening slate that displays:
  - Project title
  - Your name
  - Your GitHub and edX usernames
  - Your city and country
  - The date you recorded the video
- Then demonstrate your project in action (screenshare or camera). Upload to YouTube (unlisted is OK). Keep the URL handy.

Practical tips (Linux):
- OBS Studio is a good recorder (1080p, 30fps, mic filters). Close distractions; zoom your UI for readability. Keep a script.

##### 2) README.md (required)

- Create `README.md` in your project folder with:
  - Project Title
  - “Video Demo: <URL>” line linking your YouTube demo
  - A multi-paragraph description with depth: what the project is, what each file/folder does, and design choices with rationale.
- Aim for several hundred words. Around 750 words is a healthy target and suggests a sufficiently complex project.

Template (from CS50):

```md
# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:
TODO
```

##### 3) Submit and confirm completion (required)

- From the directory that contains your `README.md` and code, run:

```bash
submit50 cs50/problems/2025/x/project
```

- After submitting, visit your Gradebook at `https://cs50.me/cs50x` to finalize completion and claim your certificate. This step is required to register completion.

#### Deadlines and certificates

- Complete all three steps before 2025‑12‑31 23:59:00 UTC.
- After submission, load your Gradebook to trigger certificate generation (free certificate instantly; verified certificate within ~30 days if applicable). Claim the free certificate before 1 January 2026.

#### Troubleshooting submission

- If your project is too large to submit:
  - Zip the contents (excluding `README.md`) and submit the archive instead.
  - Reduce repository size below ~100MB (remove large binaries, compress media).
  - Alternatively, upload via GitHub’s web UI to your `me50/USERNAME` repo on the `cs50/problems/2025/x/project` branch per instructions.

#### Quality expectations (what “good” looks like)

- The project should be more substantial than a typical problem set.
- Your README should read like professional documentation: features, file-by-file overview, architecture, data model, design decisions, and trade-offs.
- The demo video should be concise, easy to follow, and clearly demonstrate the core flows.

#### Suggested workflow

- Week 1: Ideation and scope; write a one-page plan; set milestones.
- Week 2: Prototype core data model and minimal UI; validate end-to-end.
- Week 3: Implement features; add input validation and error states.
- Week 4: Polish UI, write README and scripts; rehearse and record video; submit.

#### Academic honesty (reminder)

- Submissions are audited. Cite any third-party code or AI assistance. Do not submit work that is not your own. Violations can lead to removal from the course and revocation of certificates.

#### Link

- Official requirements and submission instructions: [CS50 Final Project Requirements](https://cs50.harvard.edu/x/project/)
