# Changelog

All notable changes to the `pro_tips` repository are documented here, organized by pull request in reverse chronological order.

---

## [Unreleased] — `feat/pieces-mcp-documentation`

**Comprehensive Pieces MCP documentation suite** — the largest single addition to the repository since launch.

### Added

- **`guides/MCP/README.md`** — Index and entry point for all MCP documentation. Describes each guide with "use this when" sections, cross-links, and Pieces 5.0.3 release attribution.
- **`guides/MCP/Pieces MCP and LTM Tools Reference.md`** — Complete reference (~1,690 lines) for all 39 tools exposed by the Pieces MCP server: `ask_pieces_ltm`, `create_pieces_memory`, 14 full-text search tools, 5 vector search tools, `material_identifiers`, `extract_temporal_range`, and 16 batch snapshot tools. Includes parameters, examples, agent instructions, and smoke test results for every tool.
- **`guides/MCP/Connecting to PiecesOS from the Outside World via Ngrok.md`** — Full ngrok setup guide: installation (macOS/Windows/Linux), one-time auth, PiecesOS port discovery (39300–39333), and auto-discovery scripts for both Bash and PowerShell. Enables cloud-based agents (Claude web, ChatGPT, GitHub Actions, Zapier) to reach a local PiecesOS instance.
- **`guides/MCP/Bridging Local MCP Clients to Remote Servers with mcp-remote.md`** — Deep-dive on `mcp-remote` (~960 lines): transport strategies (`http-first`, `sse-only`, `http-only`), complete CLI flag reference, OAuth 2.1 + PKCE flow, token storage and reset, bearer token injection, security advisory (CVE-2025-6514), per-client config examples, public remote MCP server catalog, and full troubleshooting table.
- **`guides/MCP/Configuring MCP Clients for Cursor, Claude, Goose, and More.md`** — Redirect stub pointing to Agent Setups & Integrations.
- **`guides/MCP/Agent Setups & Integrations/README.md`** — Master index for 19 per-tool setup guides. Includes transport support matrix (stdio / SSE / Streamable HTTP) for every tool, Pieces MCP endpoint URL table (local + remote/ngrok), and stdio-to-HTTP bridge section covering `mcp-remote`, `supergateway`, and `mcp-proxy`.
- **19 per-tool setup guides** in `guides/MCP/Agent Setups & Integrations/`:
  - `Cursor.md` — Native HTTP via `url` key in `mcp.json`
  - `Claude Desktop.md` — stdio bridge for JSON config; Connectors UI for Pro/Max/Team/Enterprise
  - `Claude Code.md` — CLI with `claude mcp add --transport http|sse`
  - `Claude Cowork.md` — Autonomous task agent; shares Claude Desktop MCP config
  - `VS Code.md` — `servers` key with `type: "http"|"sse"|"stdio"` in `.vscode/mcp.json`
  - `Windsurf.md` — Use `serverUrl` (not `url`) in `~/.codeium/windsurf/mcp_config.json`
  - `Goose.md` — YAML config at `~/.config/goose/config.yaml` with `extensions` key
  - `Cline.md` — Separate config at `~/.cline/data/settings/cline_mcp_settings.json`; use SSE (Streamable HTTP buggy)
  - `Continue.dev.md` — YAML in `.continue/config.yaml`; agent mode only; use `streamable-http` type
  - `JetBrains IDEs.md` — Settings UI > AI Assistant > MCP; requires 2025.2+
  - `Zed.md` — `context_servers` key in `settings.json`; stdio only; bridge required
  - `GitHub Copilot.md` — Uses VS Code `.vscode/mcp.json` with `servers` + `type` key
  - `OpenAI Codex CLI.md` — TOML format at `~/.codex/config.toml` with `[mcp_servers.pieces]`
  - `Google Gemini CLI.md` — `~/.gemini/settings.json`; use `httpUrl` for HTTP, `url` for SSE
  - `Amazon Q Developer.md` — `~/.aws/amazonq/default.json` with `servers` + `type`
  - `ChatGPT Developer Mode.md` — Connectors UI; HTTPS required; Pro/Plus/Business/Enterprise/Education plans
  - `Raycast.md` — `mcp-config.json` file; stdio only; bridge required; macOS only
  - `Rovo Dev CLI.md` — `~/.rovodev/mcp.json` with `servers` + `transport` key
  - `OpenClaw.md` — MCPorter config at `~/.openclaw/workspace/config/mcporter.json`

### Changed

- **`README.md`** — Replaced plain 3-item MCP bullet list with a structured table covering all 4 core MCP guides; added link to MCP index; correct tool count (19); added Quick Start entry for MCP; updated "What LTM Captures" to include audio (5.0.3).
- **`releases/Whats New in Pieces 5.0.3.md`** — Replaced vague "check the documentation" prose in the Expanded MCP Server "How to Use" section with direct links to LTM Tools Reference, Agent Setups & Integrations, Ngrok guide, and mcp-remote guide. Removed redundant static image below Custom Summary Templates video. Merged main's LaTeX video URL (`d4ac0813`).
- **`guides/MCP/README.md`** — Corrected tool count 17 → 19 in three places; added Claude Cowork and OpenClaw to the tool list; added Pieces 5.0.3 release attribution blockquote.
- **`guides/MCP/Configuring MCP Clients for Cursor, Claude, Goose, and More.md`** — Corrected tool count 17 → 19; added back-link to MCP index.
- **`guides/MCP/Agent Setups & Integrations/README.md`** — Added LTM Tools Reference link in intro; added Pieces 5.0.3 mention; added back-link to MCP index.
- All 19 individual agent setup guides — Added **Related Guides** footers (3 links for HTTP-capable tools; 4 links including mcp-remote for stdio-only tools).
- All 4 core MCP guides — Added **Related Guides** sections linking to sibling docs.

### Fixed

- **`guides/MCP/Connecting to PiecesOS from the Outside World via Ngrok.md`** — Fixed PowerShell `Start-Job` parameter: `-Arg` → `-ArgumentList` (invalid parameter alias; causes immediate failure on Windows).

---

## February 18, 2026 — PR #9: Fix LaTeX video URL

**Merged:** 2026-02-18

### Fixed

- **`releases/Whats New in Pieces 5.0.3.md`** — Corrected the embedded video URL in the LaTeX Rendering section. The branch had replaced the video asset (`d4ac0813`) with an incorrect URL; this restores the correct one from main.

---

## February 18, 2026 — PR #8: New Guides Suite (Time Breakdown, LTM Audio, macOS Permissions, Discount Codes)

**Merged:** 2026-02-18

### Added

- **`guides/How to Enable LTM Audio Capture.md`** — Video-guided walkthrough for enabling LTM Audio via Desktop App (User Profile) and PiecesOS Toolbar. Covers macOS, Windows, and Linux; includes role-specific query examples for developers, managers, PMs, lawyers, accountants, consultants, and executives; links to the macOS permissions guide.
- **`guides/How to Set Up macOS Permissions for LTM Audio.md`** — Step-by-step guide for granting PiecesOS microphone access and Screen & System Audio Recording on macOS. Covers both enable paths, permission dialogs, verification, and troubleshooting.
- **`guides/How to Generate a Time Breakdown with a Custom Time Range.md`** — Video-guided walkthrough for reconstructing billable hours with configurable time ranges (last 24h, last 2 days, last week, custom). Covers daily timesheets, weekly billing, sprint reviews, and export workflows.
- **`guides/How to Create and Save Custom Summary Templates.md`** — Video-guided walkthrough for building single-click summary templates with custom scoping (time range, websites, projects, apps). Includes 11 copyable use-case prompts.
- **`guides/How to Apply a Discount Code at Checkout for Pieces Pro or Enterprise.md`** — Video-guided walkthrough for the full checkout flow and applying discount codes, including finding the "Add discount" field and troubleshooting invalid codes.

### Changed

- **`releases/Whats New in Pieces 5.0.3.md`** — Added embedded video walkthroughs for LTM Audio, Custom Summary Templates, Time Breakdown, and LaTeX Rendering sections. Fixed broken links. Added "Summarize Recent Meetings" coming-soon callout in the LTM Audio section. Replaced "Copilot" terminology with "Pieces Chat" throughout. Added "Under the Hood — PiecesOS 12.3.8" section and expanded "What's Next" section.
- **`README.md`** — Added entries for all five new guides.

---

## February 17, 2026 — PR #7: Pieces 5.0.3 Release Notes

**Merged:** 2026-02-17

### Added

- **`releases/Whats New in Pieces 5.0.3.md`** — Comprehensive release notes for Pieces Desktop 5.0.3 and PiecesOS 12.3.8, covering:
  - 🎤 **LTM Audio (Preview)** — Dual-stream microphone + system audio capture for meeting context
  - 📋 **Custom Summary Templates** — Save scoped templates for one-click generation
  - 🔌 **Expanded MCP Server** — 39-tool suite replacing the original 2-tool server (`ask_pieces_ltm` + `create_pieces_memory`)
  - ⏱️ **Time Breakdown Time Ranges** — Configurable windows (24h, 2 days, week, custom)
  - 📐 **LaTeX Rendering** — Mathematical expressions in summaries and Pieces Chat
  - ⚙️ **PiecesOS 12.3.8** — Audio ingestion engine, next-gen agentic runtime, reliability fixes

### Changed

- **`README.md`** — Added 5.0.3 to the Latest Release section.

---

## January 27, 2026 — PR #6: Improve Query Code Blocks and Fix README Version

**Merged:** 2026-01-27

### Changed

- **`guides/10 Queries To Ask Pieces LTM after 24-48 Hours of Background Memory Formation.md`** — Added `text` language identifier to all query code blocks (enables GitHub copy button); wrapped long queries to avoid horizontal scrolling.
- **`guides/5 Queries To Ask Pieces LTM after 2+ Months of Background Memory Formation.md`** — Same code block improvements.
- **`README.md`** — Fixed stale version reference.

---

## January 27, 2026 — PR #5: Pieces 5.0.1 Release Notes

**Merged:** 2026-01-27

### Added

- **`releases/Whats New in Pieces 5.0.1.md`** — Release notes for Pieces Desktop 5.0.1 and PiecesOS 12.3.6, covering:
  - ⏱️ **Time Breakdown** — Reconstruct billable hours from captured workstream context
  - 🔍 **Timeline Search** — Find summaries and conversations by keyword
  - 🕒 **Time-Based Filters** — Filter Timeline by specific time ranges
  - 🎛️ **Enhanced Model Selection** — Inline model descriptions for faster switching
  - 🔐 **AWS Bedrock Inference Profiles** — Enterprise-grade model management
  - 💬 **Summary to Chat** — Go deeper with one tap from any summary
  - 🎬 **Single-Click Summary Previews** — Video tutorials before generation

### Changed

- **`README.md`** — Added 5.0.1 to the Latest Release section; added YouTube playlist link for Single-Click Summary tutorials.

---

## January 12, 2026 — PR #4: 5 Queries To Ask Pieces LTM after 2+ Months

**Merged:** 2026-01-12

### Added

- **`guides/5 Queries To Ask Pieces LTM after 2+ Months of Background Memory Formation.md`** — Strategic query guide for senior professionals with accumulated work history. Covers 2 practical search queries, 2 collaboration & efficiency queries, and 1 strategic planning query; includes transition guidance from short-term to long-term query strategies.

### Changed

- **`README.md`** — Added entry for the new guide; updated Quick Start to distinguish between 24-48 hour and 2+ month query strategies.

---

## January 5, 2026 — PR #3: What's New in Pieces 5.0.0

**Merged:** 2026-01-05

### Added

- **`releases/Whats New in Pieces 5.0.0.md`** — Comprehensive release notes for Pieces Desktop 5.0.0 and PiecesOS 12.3.4, covering:
  - 🏡 **New Home Base** — Unified navigation and consistent UI experience
  - 🔍 **Browse, Converse, Generate** — Powerful in-place filtering
  - 👤 **Personalization & Disambiguation** — Smarter understanding of work and team dynamics
  - ☀️ **Single-Click Summaries** — Morning Brief, Day Recap, Standup, and more
  - ⚙️ **Core engine improvements** — Performance and accuracy upgrades

### Changed

- **`README.md`** — Added 5.0.0 to the Latest Release section.

---

## December 9, 2025 — PR #1: Snap Packages Update Guide

**Merged:** 2025-12-09

### Added

- **`guides/How to Update Pieces Snap Packages.md`** — Step-by-step process for updating Pieces Desktop and PiecesOS on Linux via Snap: shutdown, version check, update, and relaunch sequence with troubleshooting tips.

### Changed

- **`README.md`** — Added entry for the new guide.
