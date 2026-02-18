# Pieces Release Notes

Release notes for the Pieces 5.x series, mirrored here for easy access alongside the guides and pro tips in this repository.

> **Note:** This is a recently established archive, currently covering the last three releases. New release notes will be added here as the 5.x series continues. For the full historical archive, see the [Pieces documentation site](https://docs.pieces.app).

---

## The Arc of Pieces 5.x

Three releases into the 5.x series, a clear story is emerging:

**5.0.0** rebuilt the foundation — a calmer, more unified UI, smarter personalization engines, and the first single-click summaries.

**5.0.1** put that foundation to work for professional workflows — Time Breakdown for reconstructing billable hours, a searchable Timeline, and enterprise model governance.

**5.0.3** expanded what Pieces can capture and where it integrates — audio from meetings and calls, fully customizable summary templates, and a dramatically expanded MCP server giving AI agents like Cursor and Claude Code their deepest access to your Long-Term Memory yet.

Three themes run through all of it:

**Your memory works harder.** Pieces now captures clipboard, screen, and audio context simultaneously. It distinguishes your work from your colleagues', understands which projects are yours, and retrieves the right context faster—often before you know you need it.

**Summaries become your workflow.** From a single Morning Brief to a custom billable-hours reconstruction, Pieces generates structured, actionable output from captured context. These aren't static reports—they're starting points for deeper conversations with Pieces Chat.

**Your tools plug in.** The Pieces MCP Server now exposes 39 tools to agents running in Cursor, Claude Code, Goose, and beyond—giving them the same access to your Long-Term Memory that you have from inside Pieces.

---

## Release Index

| Version | Released | Headline |
|---------|----------|----------|
| [**5.0.3**](#pieces-503--february-2026) | February 2026 | LTM Audio, Custom Templates, Expanded MCP (39 tools) |
| [**5.0.1**](#pieces-501--january-27-2026) | January 27, 2026 | Time Breakdown, Timeline Search, Model Management |
| [**5.0.0**](#pieces-500--december-23-2025) | December 23, 2025 | New Home Base, Personalization, Single-Click Summaries |

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

Each release's "What's Next" section previews capabilities in active development. Across 5.0.1 and 5.0.3, the following are on the roadmap:

- **Next-Generation Agentic Engine** — Replacing the Q&A architecture with a fully agentic runtime that reasons, plans, uses tools, and maintains state across multi-turn conversations. The foundation is already shipping in PiecesOS 12.3.8.
- **Shared Memory (LTM-3)** — Memory slices accessible to teammates; query what colleagues worked on; organizational memory spanning individual users.
- **Native Browser History Ingestion** — Firefox, Chrome, Chromium, and Brave history extracted and indexed alongside your workstream.
- **Native Filesystem Ingestion** — OS-level file path tracking and proactive file surfacing based on current activity.
- **Scheduled Summary Templates** — Cron-based templates that run automatically and deliver results to your inbox.
- **Enhanced Audio Processing** — Ambient noise filtering, better transcription via Voxtral and Moonshine ASR models, speaker identification and voice profiles.

---

## Related Resources

- **[All Guides](../guides/README.md)** — LTM queries, Workstream Activity, Time Breakdown, Audio, custom templates, and more
- **[MCP Agent Setup Guides](../guides/MCP/Agent%20Setups%20%26%20Integrations/README.md)** — Connect Cursor, Claude Code, Goose, and 16+ other agents to your Long-Term Memory
- **[Pieces MCP Tools Reference](../guides/MCP/Pieces%20MCP%20and%20LTM%20Tools%20Reference.md)** — Complete reference for all 39 MCP tools
- **[How to Query LTM in Pieces Copilot](../guides/How%20to%20Query%20LTM%20in%20Pieces%20Copilot.md)** — Master natural language queries against your memories
- **[How to Use the Workstream Activity Timeline](../guides/How%20to%20Use%20the%20Workstream%20Activity%20Timeline.md)** — Browse, search, and act on your automatic work journal
