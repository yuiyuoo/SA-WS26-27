# Project Ideas – Software Architecture Lab WS 2026/27
**Theme:** Architecting Innovative Products with AI
**Goal of this doc:** give us a starting point to discuss and pick ONE idea for the PIBA (due **12.11.2026 EOD** in ILIAS).

> ⚠️ These ideas were brainstormed with AI support (Claude). Per course rules, we must refine them with our own thinking and mention this in the PIBA's AI usage statement.

---

## How to use this document

1. Everyone reads all ideas (≈10 min).
2. Each person scores the ideas with the rubric below (1–5 per criterion).
3. In the meeting, discuss the top 2–3, then pick one.
4. Feel free to add your own ideas at the bottom — mixing ideas is allowed.

### Selection rubric (from Sheet 1, Task 5)

| Criterion | Question to ask |
|---|---|
| **Feasible** | Can we build and evaluate a prototype in ~8 weeks of real work (after requirements/models)? |
| **Architecturally interesting** | Are there several components, real interactions, and clear quality-attribute trade-offs? |
| **Somewhat novel** | Is it more than a rebuild of a textbook system or an existing product? |
| **Team fit** | Do we know the domain / tech? Are we motivated? |
| **Data available** | Can we use open or synthetic data (no personal/confidential data in AI tools!)? |

---

## Overview

| # | Idea | Domain | Key architectural tension | Difficulty |
|---|---|---|---|---|
| 1 | ArchGuard – architecture drift detection in pull requests | Software engineering | Deterministic analysis vs. LLM reasoning; cost per PR | Medium |
| 2 | PrivIntake – privacy-first patient intake assistant | Health | Privacy (local) vs. quality (cloud LLM) | Medium–High |
| 3 | StudyRouter – cost-aware AI study companion | Education | Cost vs. answer quality; caching vs. freshness | Medium |
| 4 | ReRoute – agent-based disruption handling for small logistics firms | Logistics | Responsiveness vs. safety; autonomy vs. human approval | High |
| 5 | WattWise – household energy co-pilot with dynamic tariffs | Energy / IoT | Edge vs. cloud; offline availability | Medium |
| 6 | FairPlay GM – AI game master for multiplayer text games | Games | LLM creativity vs. consistent game state; latency | Medium |
| 7 | TransitBuddy – accessible public transport assistant | Mobility / accessibility | Real-time data vs. latency; reliability of answers | Medium |
| 8 | Interview2Req – from stakeholder interviews to traceable requirements | Requirements engineering | Automation vs. traceability/verifiability | Medium |

---

## 1. ArchGuard – Architecture Drift Detection in Pull Requests

**Problem.** Teams document an intended architecture (layers, modules, ADRs), but code drifts away from it over time. Violations, like the UI calling the database directly, are only noticed late in code reviews, if at all. Existing linters check syntax/style, not architectural intent, and rule-based tools (e.g. ArchUnit) require hand-written rules that few teams maintain.

**Idea.** A service that hooks into GitHub/GitLab pull requests, extracts the actual dependency structure of the changed code, compares it with the intended architecture (C4/ADR/Markdown description), and comments on the PR with violations plus an LLM-generated explanation and fix suggestion. An LLM can also propose formal rules from natural-language ADRs.

**Possible components.**
- Webhook ingester (PR events)
- Static analyzer → dependency graph extractor
- Architecture model store (intended architecture + ADRs)
- Conformance checker (deterministic rules)
- LLM reasoning service (explain violations, translate ADR text → rules)
- PR commenter / dashboard

**Style/patterns.** Pipeline / pipes-and-filters, event-driven (webhooks), plugin architecture for language analyzers.

**Driving quality attributes.** Accuracy (few false positives), cost per PR, latency (feedback within minutes), extensibility (new languages).

**Interesting trade-offs.** What is decided deterministically vs. by the LLM? How much code context to send (cost vs. quality)?

**MVP.** One language (Java or Python), layered-architecture rules, GitHub integration, evaluated on 2–3 open-source repos with injected violations.

**Evaluation.** Precision/recall on injected violations; cost per PR; developer rating of explanations.

**Risks.** Static analysis tooling effort; avoid scope creep into "general code review bot".

---

## 2. PrivIntake – Privacy-First Patient Intake Assistant

**Problem.** In doctors' offices, patients fill in paper forms or repeat their symptoms several times; doctors have little time to read unstructured notes. Cloud AI could summarize, but sending health data to external LLMs is a serious privacy and legal (GDPR) issue.

**Idea.** A patient-facing chat assistant that collects symptoms before the appointment. A **local small model** detects and pseudonymizes personal data; only the anonymized text goes to a cloud LLM, which produces a structured summary (complaint, duration, medication, red flags) for the doctor. Data is re-identified only inside the practice.

**Possible components.**
- Patient chat frontend (web/mobile)
- Local anonymization service (small on-premise model + rules)
- Pseudonym vault (mapping, stays in practice)
- Cloud summarization service (LLM)
- Red-flag rule engine (deterministic safety checks)
- Doctor dashboard

**Style/patterns.** Hybrid edge/cloud, gateway/proxy for data minimization, layered security zones.

**Driving quality attributes.** Privacy/security, safety (never miss red flags), availability, usability for elderly users.

**Interesting trade-offs.** How much processing stays local (privacy) vs. goes to the cloud (quality, cost)? What happens if the cloud is down?

**MVP.** Web chat + local anonymizer + cloud summary + doctor view, using **synthetic patient cases only**.

**Evaluation.** PII leakage rate on synthetic data; summary correctness checked by the team against a checklist; latency.

**Risks.** Medical domain needs care — clearly position it as "intake/summarization", not diagnosis. Must use only synthetic data.

---

## 3. StudyRouter – Cost-Aware AI Study Companion

**Problem.** Students use AI to study lecture slides, but either pay a lot for top models or get poor answers from cheap ones. Generic chatbots do not know the course material and hallucinate. (This is exactly the budget problem our own course describes.)

**Idea.** A study assistant over uploaded course material (RAG) with an **intelligent model router**: it classifies each question (definition, summary, exam-style reasoning) and routes it to the cheapest model that is likely good enough, uses a semantic cache for repeated questions, and learns from user feedback when to escalate.

**Possible components.**
- Document ingestion & embedding pipeline
- Vector store / retrieval service
- Query classifier
- Model router + budget manager
- Semantic cache
- Feedback & evaluation loop
- Web frontend (chat + quiz mode)

**Style/patterns.** Microservices or modular monolith, strategy pattern for routing, cache-aside.

**Driving quality attributes.** Cost efficiency, answer quality, latency, modifiability (new models appear constantly).

**Interesting trade-offs.** Cost vs. quality per query; cache hit rate vs. stale/wrong answers; per-user vs. shared cache (privacy).

**MVP.** RAG over our own SA lecture slides, router with 2–3 OpenRouter models, simple cache, cost dashboard.

**Evaluation.** Compare cost and answer quality: always-premium vs. always-cheap vs. router, on a fixed question set.

**Risks.** "Chat with your PDF" is common — novelty must come from the routing/budget architecture. Respect copyright of slides (use only for our own course, not public).

---

## 4. ReRoute – Agent-Based Disruption Handling for Small Logistics Firms

**Problem.** Small delivery companies plan routes in the morning; when disruptions happen (traffic jam, vehicle breakdown, customer not home), dispatchers re-plan manually by phone. Enterprise tools are too expensive for them.

**Idea.** An event-driven system where disruption events trigger an AI planning agent that proposes re-plans (swap deliveries between drivers, reorder stops), explains them in natural language, and sends them to the dispatcher for one-click approval. A classic optimizer does the math; the LLM handles messy inputs (driver messages like "stuck at A8, 40 min") and explanations.

**Possible components.**
- Event ingestion (traffic feed, driver app messages)
- Message interpreter (LLM: free text → structured event)
- Route optimizer (e.g. OR-Tools)
- Planning agent / orchestrator
- Dispatcher dashboard (human-in-the-loop)
- Driver app (simulated)
- Simulation engine for testing

**Style/patterns.** Event-driven architecture, publish/subscribe, human-in-the-loop, agent orchestration.

**Driving quality attributes.** Responsiveness, safety/correctness of plans, explainability, scalability with number of drivers.

**Interesting trade-offs.** How autonomous may the agent be? LLM vs. optimizer responsibilities; consistency when several events arrive at once.

**MVP.** Simulated city with 5 drivers / 50 deliveries, 3 disruption types, dispatcher approval UI.

**Evaluation.** Time-to-new-plan, delivery delay vs. no re-planning, correctness of interpreted messages.

**Risks.** Most complex idea — optimization + simulation could eat time. Keep the optimizer simple.

---

## 5. WattWise – Household Energy Co-Pilot with Dynamic Tariffs

**Problem.** Dynamic electricity tariffs are spreading in Germany, but households don't know when to run the washing machine, charge the e-bike/EV, or use their solar surplus. Smart-home apps show data but don't give understandable, actionable advice.

**Idea.** A home energy assistant that combines price forecasts, (simulated) solar production and device consumption, schedules flexible appliances, and explains its decisions in plain language ("Run the dishwasher at 13:00 — 40% cheaper due to solar surplus"). Core scheduling runs locally so it works offline; the LLM is used for explanations and natural-language goals ("car must be 80% full by 7 am").

**Possible components.**
- Device adapters (simulated IoT / MQTT)
- Local home hub (scheduler, rules, time-series store)
- Price & weather forecast connector
- Cloud LLM service (explanations, goal parsing)
- Mobile/web app

**Style/patterns.** Edge/cloud hybrid, IoT gateway, publish/subscribe (MQTT).

**Driving quality attributes.** Availability/offline operation, privacy (consumption data reveals habits), energy-cost savings, usability.

**Interesting trade-offs.** What runs on the edge vs. cloud? How often to call the LLM (cost) vs. template explanations?

**MVP.** Simulated household with 4 devices, real or recorded price data, scheduler + explanation UI.

**Evaluation.** Cost savings vs. naive schedule in simulation; offline behavior test; user rating of explanations.

**Risks.** Hardware is not needed — keep everything simulated.

---

## 6. FairPlay GM – AI Game Master for Multiplayer Text Games

**Problem.** LLM-based text adventures are fun but break down in multiplayer: the AI forgets facts, contradicts itself, ignores game rules, and responses are slow and expensive when several players act at once.

**Idea.** A multiplayer game platform where an **authoritative game-state engine** holds the truth (inventory, positions, rules), and the LLM acts only as narrator/NPC voice constrained by that state. Player actions are validated by the rules engine before the LLM describes the outcome.

**Possible components.**
- Game client (web)
- Real-time session server (WebSockets)
- Game-state & rules engine (deterministic)
- Narrative LLM service (with state-based prompts)
- Memory/summary service (long sessions)
- Content moderation filter

**Style/patterns.** Client–server with authoritative server, event sourcing for game state, guardrail pattern around LLM.

**Driving quality attributes.** Consistency, latency, cost per session, scalability (many concurrent sessions), safety (moderation).

**Interesting trade-offs.** Creativity vs. rule consistency; streaming responses vs. validated responses; cost of long context vs. summarization.

**MVP.** 2–4 players, one small world, rules engine + LLM narrator, contradiction checks.

**Evaluation.** Contradiction rate vs. plain-LLM baseline; response latency; cost per hour of play.

**Risks.** Fun but must keep the focus on architecture, not game content.

---

## 7. TransitBuddy – Accessible Public Transport Assistant

**Problem.** Public-transport apps are hard to use for visually impaired, elderly, or non-German-speaking people, especially during disruptions ("Which replacement bus do I take now?"). Information is spread over timetables, real-time feeds and station notices.

**Idea.** A voice-first, multilingual assistant that combines open timetable data (GTFS), real-time disruption feeds, and station accessibility information (elevators working?), and answers questions in natural language with step-by-step guidance. The LLM interprets questions and explains; a deterministic routing service computes the actual connections (no hallucinated departures).

**Possible components.**
- Voice/chat frontend (speech-to-text, text-to-speech)
- Intent & language understanding (LLM)
- Routing engine (e.g. OpenTripPlanner on GTFS)
- Real-time feed adapter + cache
- Accessibility info service
- Response composer (LLM, grounded in routing results)

**Style/patterns.** Layered + microservices, adapter pattern for data sources, grounding/tool-use pattern for LLM.

**Driving quality attributes.** Correctness (never invent departures), latency, availability during disruptions (high load), accessibility, multilingual support.

**Interesting trade-offs.** Freshness of real-time data vs. caching; fallback when LLM or feed is unavailable.

**MVP.** One city (e.g. Stuttgart open GTFS data), text + voice in 2 languages, simulated disruptions.

**Evaluation.** Correctness of answers vs. ground truth routing; response time; small usability test.

**Risks.** Data availability/quality of real-time feeds — can be simulated if needed.

---

## 8. Interview2Req – From Stakeholder Interviews to Traceable Requirements

**Problem.** Requirements elicitation interviews produce hours of recordings and messy notes. Turning them into structured requirements (e.g. IEEE 830) is slow, and the link between "who said what" and each requirement is often lost — making later changes and validation hard.

**Idea.** A tool that transcribes interviews, extracts candidate requirements with an LLM, classifies them (functional/quality, priority), detects conflicts/duplicates, and keeps **traceability links** to the exact transcript passages. The requirements engineer reviews and approves everything (human-in-the-loop).

**Possible components.**
- Upload & transcription service (speech-to-text)
- Requirement extraction service (LLM)
- Classification & conflict detection
- Traceability store (requirements ↔ transcript segments ↔ stakeholders)
- Review UI for the requirements engineer
- Export (IEEE 830 / Markdown / ReqIF)

**Style/patterns.** Pipeline, repository pattern, human-in-the-loop, plugin exporters.

**Driving quality attributes.** Traceability, correctness, privacy of recordings, cost per interview hour.

**Interesting trade-offs.** Level of automation vs. reviewer effort; local vs. cloud transcription (privacy vs. quality).

**MVP.** Upload a mock interview (recorded by our own team), extract and review requirements, export IEEE 830 skeleton.

**Evaluation.** Compare extracted requirements against a manually created gold standard; time saved.

**Risks.** Bonus: we can use it on our own Deliverable 2. Must use only our own mock interviews (no real personal data).

---

## Discussion questions for our meeting

1. Which 2–3 ideas excite us most? Why?
2. Which domain do we already have knowledge or contacts in?
3. For our top idea: what are the **4–7 main components** and the **top 2–3 quality attributes**?
4. What is the **minimum** prototype we can definitely deliver by 22.01.2027?
5. What data do we need, and is it open/synthetic?
6. How will we use AI (OpenRouter budget) during the project — which tasks, which models?

## Our own ideas

_Add yours here:_

- …
- …

## Next steps

| When | What | Who |
|---|---|---|
| by 04.11 | Everyone scores ideas, adds own ideas | All |
| ~05.11 | Meeting: pick one idea, sketch components | All |
| by 09.11 | Draft PIBA sections (Problem / Idea / Benefits / Action) | split |
| 10.–11.11 | Review, fit to one page, submit in ILIAS | All |
