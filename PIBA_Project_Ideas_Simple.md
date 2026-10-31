# Project Ideas – Simple Version
Software Architecture Lab WS 2026/27 · Theme: *Architecting Innovative Products with AI*
PIBA due: **12.11.2026** in ILIAS

> Brainstormed with AI support (Claude). We still need to pick, refine and own the idea ourselves.

Every idea below is built the same basic way:

**Web page → our backend code → AI API (OpenRouter)**, plus a free local database (SQLite) if we need to save things.
No real data needed: we use open data, data we make ourselves, or fake data.

---

## 1. ArchGuard – "Did this code break our architecture?"
- **Problem:** Code slowly stops following the planned structure (e.g. UI talks directly to the database), and nobody notices.
- **What it does:** When someone opens a pull request, it checks the code against simple rules and an AI explains what's wrong.
- **Demo:** Open a PR with a planted mistake → bot comments "UI layer should not call the database directly."
- **Data:** Any open-source GitHub project.

## 2. PrivIntake – "Tell the doctor your symptoms before the visit"
- **Problem:** Patients repeat their symptoms many times, but sending health data to AI is a privacy risk.
- **What it does:** Patient chats with the app; names and personal details are removed first, then AI writes a short summary for the doctor.
- **Demo:** Chat as a fake patient → doctor page shows a clean summary with no names.
- **Data:** Fake patient stories we write or generate.

## 3. StudyRouter – "A cheap and smart study helper"
- **Problem:** Good AI models are expensive; cheap ones give bad answers.
- **What it does:** Answers questions about our lecture slides. Easy questions go to a cheap model, hard ones to a better model. Repeated questions are answered from saved answers.
- **Demo:** Ask questions → see the answer + which model was used + how much it cost.
- **Data:** Our own SA lecture slides.

## 4. ReRoute – "Fix delivery plans when something goes wrong"
- **Problem:** Small delivery companies re-plan by phone when a truck is late or broken.
- **What it does:** A driver writes "stuck on A8, 40 min" → AI understands it and suggests a new plan → dispatcher clicks approve.
- **Demo:** A fake city with 5 drivers; trigger a traffic jam and watch the plan update.
- **Data:** Fake deliveries and events (simulated).

## 5. WattWise – "When should I run my washing machine?"
- **Problem:** Electricity prices change during the day, but people don't know when it's cheapest.
- **What it does:** Looks at prices and suggests when to run devices, with a simple explanation.
- **Demo:** "Run the dishwasher at 13:00 – 40% cheaper."
- **Data:** Public electricity price data + fake household devices.

## 6. FairPlay GM – "An AI game master that doesn't forget the rules"
- **Problem:** AI text games forget facts and break the rules, especially with several players.
- **What it does:** Normal code keeps track of the game (items, positions, rules); the AI only tells the story.
- **Demo:** 3 players play together; the AI never "gives back" an item someone already used.
- **Data:** A small game world we design.

## 7. TransitBuddy – "Ask the bus app in normal language"
- **Problem:** Transport apps are hard for elderly, blind, or non-German speakers, especially during delays.
- **What it does:** You ask (by voice or text) "How do I get to the university?" → it finds the real connection and explains it simply.
- **Demo:** Ask in English or another language, get a correct VVS connection.
- **Data:** Free public timetable data for Stuttgart.

## 8. Interview2Req – "Turn interviews into requirements"
- **Problem:** Turning long interview notes into a requirements list takes hours.
- **What it does:** Upload an interview recording → AI writes a list of requirements, each linked to the sentence it came from.
- **Demo:** Upload our own mock interview → get a requirements list we can edit and export.
- **Data:** A mock interview our team records.
- **Bonus:** We can use it for our own Requirements deliverable.

---

## How to choose (quick)
For each idea, ask:
1. Can we build a small working version in ~2 months?
2. Does it have a few clear parts that work together?
3. Is it more than just a normal chatbot?
4. Do we like it?

## Our own ideas
- …
- …
