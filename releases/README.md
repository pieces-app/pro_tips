# Pieces Release Notes

Release notes for the Pieces platform, mirrored here for easy access alongside the guides and pro tips in this repository.

---

## The Arc from 5.0 to 6.1

The 5.x series built the foundation. **5.0.0** introduced a calm, unified UI, smarter personalization, and the first single-click summaries. **5.0.1** put it to work — Time Breakdown, Timeline Search, enterprise model governance. **5.0.3** expanded what Pieces can capture — LTM Audio, custom summary templates, and a 39-tool MCP server. **5.1.0** removed friction — Scheduled Summaries, Modality Focus, a rebuilt local LLM engine, and expanded BYOK support.

**6.0.0 changes the architecture.** Agentic Long-Term Memory replaces the single-shot Q&A engine with a multi-turn reasoning agent that follows threads, cross-references context, and builds toward complete answers. That foundation powers the first summary that takes action — Meeting Prep reads your calendar, assembles structured pre-reads, and can schedule prep time for you. The rest of the release sharpens control: Reflection Mode for metacognitive self-correction, inline AI editing for summaries, granular LTM data management, per-conversation token visibility, and one-click MCP setup.

**6.1.0 grounds that reasoning in better signals.** Summaries now use the files you actually had open and the sites you visited, with clickable citations back to the source. People mentioned in summaries become hoverable persona cards. Managed MCP setup covers Cursor, Claude, Codex, Gemini CLI, GitHub Copilot, and more; Claude Desktop connects without Node.js through a bundled bridge. PiecesOS 12.6.0 adds more durable account and organization synchronization, stronger formation and temporal search, and safer MCP recovery. PiecesOS also reads OpenRouter's live listing and applies compatibility and tier-selection rules for Claude, Gemini, GPT, and Grok routes.

Four themes run through the full arc:

**Your memory works harder.** Clipboard, screen, audio, and now calendar — Pieces captures across every modality, distinguishes your work from your colleagues', and retrieves the right context faster.

**The agent reasons, not just retrieves.** Multi-turn agentic loops replace one-shot answers. The agent follows threads, gathers evidence from memory and beyond, and self-corrects with Reflection Mode.

**Summaries become actions.** From Morning Brief to Meeting Prep, summaries don't just report — they take action on your behalf.

**Your tools plug in.** One-click MCP setup, smarter MCP tools, and deeper integration with Cursor, Claude Code, and the wider agent ecosystem.

---

## Release Index

| Version | Status / Date | Headline |
|---------|---------------|----------|
| [**6.1.0**](#pieces-610--tagged-july-29-2026) | Tagged July 29, 2026; awaiting re-tag | Managed MCP Setup, Grounded Summaries, PiecesOS 12.6.0 |
| [**6.0.0**](#pieces-600--may-2026) | Released May 2026 | Agentic LTM, Meeting Prep, Reflection Mode, Google Calendar |
| [**5.1.0**](#pieces-510--march-2026) | Released March 2026 | Scheduled Summaries, Modality Focus, Local LLM Overhaul, BYOK |
| [**5.0.3**](#pieces-503--february-2026) | Released February 2026 | LTM Audio, Custom Templates, Expanded MCP (39 tools) |
| [**5.0.1**](#pieces-501--january-27-2026) | Released January 27, 2026 | Time Breakdown, Timeline Search, Model Management |
| [**5.0.0**](#pieces-500--december-23-2025) | Released December 23, 2025 | New Home Base, Personalization, Single-Click Summaries |

---

## Pieces 6.1.0 — Tagged July 29, 2026

**[→ Read the Full Release Notes](./Whats%20New%20in%20Pieces%206.1.0.md)**

**Status:** Awaiting re-tag before launch | **Pieces Desktop:** 6.1.0 | **PiecesOS:** 12.6.0

The grounding and friction-removal release. 6.1.0 manages MCP setup for popular agents, removes the Node.js prerequisite from Claude Desktop, grounds summaries in real files and browsing activity, turns names into live person references, runs single-click summaries in parallel, and gives capture smarter pause and idle behavior. PiecesOS 12.6.0 adds durable account and organization streams, two-pass summary formation, temporal recall before roll-up, and restart-safe MCP recovery. Its runtime inventory uses OpenRouter's live listing to choose compatible Claude, Gemini, GPT, and Grok models for the picker tiers.

### What you can do now that you couldn't before

**Connect the agents you already use**

Pieces manages setup for Cursor, Claude Code, Claude Desktop, GitHub Copilot in VS Code, Codex, Gemini CLI, and Antigravity. Claude Desktop now uses a bundled bridge with no separate Node.js, npx, or `mcp-remote` installation.

**Open the evidence behind a summary**

Summaries use real open-file and browsing signals instead of inferring everything from what appeared on screen. File citations are clickable, so you can jump directly from a summary to the artifact it references.

**See who a person is without leaving the summary**

Hover a name to open a persona card with role, contact details, and relationship context built from your interactions over time.

**Generate several summaries together**

Start a Day Recap, Standup Update, and Meeting Prep at the same time instead of waiting for each one to finish.

**Pause capture for the exact duration you need**

Pause Long-Term Memory and LTM Audio for minutes, hours, or days. Pieces shows when capture will resume automatically.

**Use fewer resources when you step away**

Capture stops when the screen is locked and progressively backs off while the machine is idle, alongside lower-cost screen and audio processing.

**Keep account and organization state current**

PiecesOS receives reflected user, organization-membership, subscription, and migration-offer state through authenticated Firestore listeners. Reconnect snapshots and a durable outbox provide ordering, retries, deletion recovery, and reconciliation.

**Use current models with task-specific planning**

PiecesOS reads OpenRouter's live model listing, applies compatibility rules, and selects Claude, Gemini, GPT, and Grok options for Fast, Balanced, and Extra Thinking tiers. RouteAdvisor plans tool use separately under normal operation, while scenario-aware evaluation judges whether memory retrieval found enough evidence.

### Who benefits most from 6.1.0

| Feature | Who it's for |
|---------|--------------|
| Managed MCP setup | Users connecting Cursor, Claude, Codex, Gemini CLI, GitHub Copilot, and other supported agents |
| Grounded file and browsing summaries | Anyone who needs summaries tied to real, openable source material |
| Inline person intelligence | Teams, managers, sales, and anyone preparing for meetings |
| Parallel single-click summaries | Anyone generating several recurring reports at once |
| Custom LTM pause durations | Privacy-conscious users and anyone stepping into confidential work |
| Idle and lock-aware capture | Laptop users who want lower battery and resource use |
| Durable account and organization sync | Enterprise deployments that need safer state propagation and reconnect recovery |
| Live model routes and smarter planning | Anyone using Agentic Chat across different providers and task types |

---

## Pieces 6.0.0 — May 2026

**[→ Read the Full Release Notes](./Whats%20New%20in%20Pieces%206.0.0.md)**  
**Pieces Desktop:** 6.0.0

The agentic era begins. 6.0.0 replaces the single-shot Q&A engine with a multi-turn reasoning agent, ships the first summary that takes action on your behalf, and gives you deeper control over your data, your models, and your workflow.

### What you can do now that you couldn't before

**Have real conversations with your memory**  
Agentic Long-Term Memory enables multi-turn reasoning across your summaries, events, people, and beyond. The agent follows threads, cross-references context, and builds toward complete answers — instead of guessing in one shot. A full toolbox (memory search, web search, calendar, filesystem, browser history) lets the agent actively gather evidence during any chat or summary.

**Walk into every meeting prepared — automatically**  
Meeting Prep connects to your Google Calendar, looks ahead at upcoming meetings, cross-references each with your Long-Term Memories, and generates structured pre-reads. With your permission, it can schedule prep time on your calendar so the work to get ready is actually on your schedule.

**Let the agent reflect and self-correct**  
Reflection Mode gives the agent metacognition — the ability to step back, evaluate its reasoning, and adjust course in real time. The result is better answers even from leaner models, and deeper insights when you ask Pieces to reflect on weeks, months, or quarters of work.

**Edit summaries with AI, right inline**  
Select any text in a Workstream Summary, tap "Edit with AI," and review suggested changes in a clean diff view. Rework entire summaries with a single prompt — "make this shorter for Slack," "rewrite for an exec audience" — all grounded in the original memories.

**See the true cost of agentic work**  
Per-conversation token usage tracks input, output, reasoning, and cache — including tool calls. BYOK and enterprise deployments get clean visibility into provider usage.

**Surgically manage your LTM data**  
Clear data by time period, capture modality (vision, clipboard, audio), or specific application — or combine all three. Proactively block apps from capture before Pieces ever encounters them.

**Set up MCP in one click**  
Configure the Pieces MCP Server for Cursor, VS Code, Claude Desktop, and more directly from Settings — no JSON editing required.

### Who benefits most from 6.0.0

| Feature | Who it's for |
|---------|--------------|
| Agentic LTM (Agentic Chats & Summaries) | Everyone — fundamentally better answers and summaries |
| Meeting Prep | Anyone with a calendar full of meetings — PMs, managers, sales, consultants |
| Reflection Mode | Anyone who wants deeper, more self-correcting analysis of their work |
| Google Calendar Integration | Everyone — richer summaries, foundation for calendar-aware features |
| Edit Summaries with AI | Anyone who shares summaries with teammates, clients, or stakeholders |
| Token Usage Visibility | Teams managing API usage, BYOK and enterprise deployments |
| Granular LTM Data Management | Privacy-conscious users, regulated industries |
| One-Click MCP Setup | Developers using Cursor, VS Code, Claude Desktop, and other MCP clients |

---

## Pieces 5.1.0 — March 2026

**[→ Read the Full Release Notes](./Whats%20New%20in%20Pieces%205.1.0.md)**  
**Pieces Desktop:** 5.1.0 | **PiecesOS:** 12.3.9

The friction-removal release. 5.1.0 put summaries on autopilot with Scheduled Summaries, added Modality Focus for capture-aware querying, rebuilt the local LLM engine from the ground up (no more Ollama), expanded BYOK to OpenAI, Google AI Studio, and Anthropic, and shipped Claude Opus 4.6 and Gemini 3.1.

### What you can do now that you couldn't before

**Put summaries on autopilot**  
Schedule any summary to run automatically — daily, weekly, or custom cadence. Morning briefs generate before you open Pieces; weekly recaps arrive every Friday afternoon.

**Query by how you captured it**  
Modality Focus lets you filter chat prompts by clipboard, audio, or vision — narrowing results to the right capture type when you remember *how* you encountered something but not the exact content.

**Run local models without Ollama**  
A completely rebuilt local LLM engine removes the Ollama dependency, with fewer setup issues, better stability, and access to newer models.

**Bring your own API keys**  
Full BYOK support for OpenAI, Google AI Studio, and Anthropic joins existing AWS Bedrock and Azure support.

### Who benefits most from 5.1.0

| Feature | Who it's for |
|---------|--------------|
| Scheduled Summaries | Anyone with recurring reporting needs — standups, sprint reviews, client updates |
| Modality Focus | Anyone who wants precision in how they search their memory |
| Local LLM Overhaul | Privacy-focused users and teams running models on-device |
| Expanded BYOK | Enterprise teams with existing API agreements |
| Today's Headlines | Anyone who wants a work-relevant news brief in one click |

**Guides:** [Scheduled Summaries how-to in the release notes](./Whats%20New%20in%20Pieces%205.1.0.md#-scheduled-summaries-put-your-summaries-on-autopilot)

---

## Pieces 5.0.3 — February 2026

**[→ Read the Full Release Notes](./Whats%20New%20in%20Pieces%205.0.3.md)**  
**Pieces Desktop:** 5.0.3 | **PiecesOS:** 12.3.8

The biggest capture and integration release yet. 5.0.3 adds audio to Long-Term Memory, puts full template control in your hands, and gives AI agents their deepest access to your work history.

### What you can do now that you couldn't before

**Capture your meetings and calls**  
LTM Audio (preview) records microphone input and system audio simultaneously, extracts context, and folds it into your Long-Term Memory. Pair programming sessions, stand-ups, client calls, and webinars now become searchable—alongside everything else you've worked on. Pieces processes audio locally; no raw audio is stored.

**Build your own one-click summaries**  
Custom Summary Templates let you define exactly what you want: choose a time range, scope by website, project, or application, set your preferred prompt, and save it. Next time, one click generates the same structured output. No reconfiguring parameters each time.

**Give your AI agent your full work history**  
The Pieces MCP Server now exposes 39 tools—full-text search, vector search, temporal queries, batch retrieval, and annotation access. Cursor agents, Claude Code sessions, and Goose workflows can now query your Long-Term Memory as naturally as you can.

**Reconstruct billable hours for any window**  
Time Breakdown now accepts configurable time ranges—last 24 hours, last week, or any custom date range—so reconstructions match your actual billing cycle, not just the previous day.

**Read math the way it was meant to be read**  
LaTeX expressions now render natively in Pieces Chat and summaries. ML engineers, researchers, and anyone working with formulas no longer see raw LaTeX syntax cluttering their conversations.

### Who benefits most from 5.0.3

| Feature | Who it's for |
|---------|--------------|
| LTM Audio (Preview) | Anyone in meetings, pair programming sessions, or video calls |
| Custom Summary Templates | Teams with recurring reporting formats; professionals who bill clients |
| Expanded MCP Server (39 tools) | Developers using Cursor, Claude Code, Goose, or any MCP-compatible agent |
| Time Breakdown time ranges | Attorneys, consultants, government contractors, CPAs, researchers |
| LaTeX rendering | ML engineers, data scientists, researchers, academics |

**Guides:** [Enable LTM Audio](../guides/How%20to%20Enable%20LTM%20Audio%20Capture.md) · [macOS Permissions for LTM Audio](../guides/How%20to%20Set%20Up%20macOS%20Permissions%20for%20LTM%20Audio.md) · [Custom Summary Templates](../guides/How%20to%20Create%20and%20Save%20Custom%20Summary%20Templates.md) · [Time Breakdown with Custom Ranges](../guides/How%20to%20Generate%20a%20Time%20Breakdown%20with%20a%20Custom%20Time%20Range.md)

---

## Pieces 5.0.1 — January 27, 2026

**[→ Read the Full Release Notes](./Whats%20New%20in%20Pieces%205.0.1.md)**  
**Pieces Desktop:** 5.0.1 | **PiecesOS:** 12.3.6

The professional productivity release. 5.0.1 introduced Time Breakdown—the first tool to reconstruct your billable hours from captured context—alongside a searchable Timeline, a richer model picker, enterprise model governance, and one-tap entry from any summary into a deeper conversation.

### What you can do now that you couldn't before

**Stop losing billable hours to poor recall**  
Time Breakdown analyzes your captured workstream and reconstructs your day into approximate time blocks grouped by project and client. Studies show professionals lose 10–20% of billable time to poor recall. Time Breakdown gives you a structured starting point to review, refine, and submit—instead of starting from a blank page.

**Find anything in your work history**  
The Timeline is now searchable by keyword and filterable by time range, source application, and summary type. Combine filters to scope to "last Thursday afternoon" or "everything related to the authentication module from VS Code this week." No more endless scrolling.

**Pick the right model without the friction**  
A redesigned model picker shows inline descriptions and a quick-search field at the top. Switching from Claude to Gemini mid-conversation takes two clicks. Full model management—85+ models organized by provider—moved to a dedicated Settings section accessible directly from the picker.

**Control model access across your organization**  
AWS Bedrock Inference Profiles let enterprise teams assign specific models to specific groups (developer team gets Claude Haiku 4.5, marketing gets Claude Haiku 3.5) while inference stays on your own AWS infrastructure.

**Go deeper from any summary**  
Every summary now has a "Start Related Chat" button. One tap loads the summary and all its associated context into a new Pieces Chat session, ready for follow-up questions. Summaries aren't just reports—they're entry points.

### Who benefits most from 5.0.1

| Feature | Who it's for |
|---------|--------------|
| Time Breakdown | Attorneys, CPAs, consultants, government contractors, researchers |
| Timeline Search & Filters | Anyone looking back at recent or historical work |
| Enhanced Model Picker | Anyone who switches models frequently across different tasks |
| AWS Bedrock Inference Profiles | Enterprise teams with BYOK deployments |
| Summary to Chat | Anyone who generates summaries and wants to explore the details |

**PiecesOS 12.3.6 highlights:** ~21x faster full-text search (under 10ms), Linux X11 full support, offline mode fix, enterprise local model support, migration progress indicator.

---

## Pieces 5.0.0 — December 23, 2025

**[→ Read the Full Release Notes](./Whats%20New%20in%20Pieces%205.0.0.md)**  
**Pieces Desktop:** 5.0.0 | **PiecesOS:** 12.3.4

The foundation release. 5.0.0 consolidated Pieces into a single, calm entry point, made filtering and browsing fluid and in-place, taught Pieces to understand who you are versus who you collaborate with, and introduced single-click summaries for Morning Brief, Day Recap, Standup, and Week Recap.

### What you can do now that you couldn't before

**Start from one place, every time**  
Home Base replaced the multi-entry-point design that left users hunting for features. Now you arrive somewhere consistent: start a new chat, pick up a recent conversation, or generate a summary—without navigating to a different screen first.

**Filter, browse, and act without losing context**  
In-place filtering lets you narrow your view by date, chat type, summary type, source, or material category—and immediately ask a question or generate something new, all in the same view. As your library grows into the thousands, this replaces the "find the right screen" problem with a simpler loop: browse, filter, act.

**Get summaries that are actually about you**  
The Personification and Disambiguation engines distinguish your work from others', recognize your projects and priorities, and ensure summaries focus on what matters to you specifically. When you ask "what did I work on this week?" in a shared team environment, you get your work—not a blend of everything in shared channels.

**Start and end your day with a single click**  
Morning Brief, Day Recap, Standup Update, and Week Recap generate from your captured context with one click. No prompt required. They're consistent enough to become daily habits and structured enough to share directly with your team.

### Who benefits most from 5.0.0

| Feature | Who it's for |
|---------|--------------|
| Home Base | Everyone — cleaner, more predictable daily starting point |
| In-place filtering | Anyone with a growing library of chats, summaries, or saved materials |
| Personification & Disambiguation | Anyone working in team environments or shared channels |
| Single-Click Summaries | Professionals who need consistent daily and weekly reporting |

**PiecesOS 12.3.4 highlights:** New LLM integrations, faster vision pipeline, smarter memory formation and event clustering, enhanced enterprise deployment options.

---

## What's Coming Next

The agentic foundation in 6.0.0 and better grounding in 6.1.0 unlock the next wave of capabilities:

- **Cross-Device Real-Time Sync** — Seamless sync across all your devices so your memories, conversations, and settings are always up to date — no matter where you're working
- **Shared Artificial Memories** — Share your Long-Term Memories with teammates so the context you capture benefits your entire team — collaborative memory for collaborative work
- **Outlook Calendar Integration** — Bringing the same calendar-aware intelligence to Microsoft Outlook users — Meeting Prep, richer summaries, and schedule-aware context for everyone

---

## Related Resources

- **[All Guides](../guides/README.md)** — LTM queries, Workstream Activity, Time Breakdown, Audio, custom templates, and more
- **[MCP Agent Setup Guides](../guides/MCP/Agent%20Setups%20%26%20Integrations/README.md)** — Connect Cursor, Claude Code, Goose, and 16+ other agents to your Long-Term Memory
- **[Pieces MCP Tools Reference](../guides/MCP/Pieces%20MCP%20and%20LTM%20Tools%20Reference.md)** — Complete reference for all 39 MCP tools
- **[How to Query LTM in Pieces Copilot](../guides/How%20to%20Query%20LTM%20in%20Pieces%20Copilot.md)** — Master natural language queries against your memories
- **[How to Use the Workstream Activity Timeline](../guides/How%20to%20Use%20the%20Workstream%20Activity%20Timeline.md)** — Browse, search, and act on your automatic work journal
