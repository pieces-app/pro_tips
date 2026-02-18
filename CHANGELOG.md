# Changelog

All notable changes to the `pro_tips` repository are documented here, organized by pull request in reverse chronological order. PR numbers link to GitHub.

---

## [PR #11](https://github.com/pieces-app/pro_tips/pull/11) — MCP Documentation Suite (February 18, 2026 — open)

**Comprehensive Pieces MCP documentation suite** — the largest single addition to the repository since launch. Introduces 25 new files covering every aspect of connecting AI agents to Pieces Long-Term Memory via the Model Context Protocol, plus cross-linking and release attribution across all existing docs.

### Added

- **[`guides/MCP/README.md`](./guides/MCP/README.md)** — Index and entry point for all MCP documentation. Describes each guide with "use this when" sections, cross-links, and Pieces 5.0.3 release attribution.
- **[`guides/MCP/Pieces MCP and LTM Tools Reference.md`](./guides/MCP/Pieces%20MCP%20and%20LTM%20Tools%20Reference.md)** — Complete reference (~1,690 lines) for all 39 tools exposed by the Pieces MCP server: `ask_pieces_ltm`, `create_pieces_memory`, 14 full-text search tools, 5 vector search tools, `material_identifiers`, `extract_temporal_range`, and 16 batch snapshot tools. Includes parameters, examples, agent instructions, and smoke test results for every tool.
- **[`guides/MCP/Connecting to PiecesOS from the Outside World via Ngrok.md`](./guides/MCP/Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md)** — Full ngrok setup guide: installation (macOS/Windows/Linux), one-time auth, PiecesOS port discovery (39300–39333), and auto-discovery scripts for both Bash and PowerShell. Enables cloud-based agents (Claude web, ChatGPT, GitHub Actions, Zapier) to reach a local PiecesOS instance.
- **[`guides/MCP/Bridging Local MCP Clients to Remote Servers with mcp-remote.md`](./guides/MCP/Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md)** — Deep-dive on `mcp-remote` (~960 lines): transport strategies (`http-first`, `sse-only`, `http-only`), complete CLI flag reference, OAuth 2.1 + PKCE flow, token storage and reset, bearer token injection, security advisory (CVE-2025-6514), per-client config examples, public remote MCP server catalog, and full troubleshooting table.
- **[`guides/MCP/Configuring MCP Clients for Cursor, Claude, Goose, and More.md`](./guides/MCP/Configuring%20MCP%20Clients%20for%20Cursor%2C%20Claude%2C%20Goose%2C%20and%20More.md)** — Redirect stub pointing to Agent Setups & Integrations.
- **[`guides/MCP/Agent Setups & Integrations/README.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/README.md)** — Master index for 19 per-tool setup guides. Includes transport support matrix (stdio / SSE / Streamable HTTP) for every tool, Pieces MCP endpoint URL table (local + remote/ngrok), and stdio-to-HTTP bridge section covering `mcp-remote`, `supergateway`, and `mcp-proxy`.
- **19 per-tool setup guides** in [`guides/MCP/Agent Setups & Integrations/`](./guides/MCP/Agent%20Setups%20%26%20Integrations/):
  - [`Cursor.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Cursor.md) — Native HTTP via `url` key in `mcp.json`
  - [`Claude Desktop.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Claude%20Desktop.md) — stdio bridge for JSON config; Connectors UI for Pro/Max/Team/Enterprise
  - [`Claude Code.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Claude%20Code.md) — CLI with `claude mcp add --transport http|sse`
  - [`Claude Cowork.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Claude%20Cowork.md) — Autonomous task agent; shares Claude Desktop MCP config
  - [`VS Code.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/VS%20Code.md) — `servers` key with `type: "http"|"sse"|"stdio"` in `.vscode/mcp.json`
  - [`Windsurf.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Windsurf.md) — Use `serverUrl` (not `url`) in `~/.codeium/windsurf/mcp_config.json`
  - [`Goose.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Goose.md) — YAML config at `~/.config/goose/config.yaml` with `extensions` key
  - [`Cline.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Cline.md) — Separate config at `~/.cline/data/settings/cline_mcp_settings.json`; use SSE (Streamable HTTP buggy)
  - [`Continue.dev.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Continue.dev.md) — YAML in `.continue/config.yaml`; agent mode only; use `streamable-http` type
  - [`JetBrains IDEs.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/JetBrains%20IDEs.md) — Settings UI > AI Assistant > MCP; requires 2025.2+
  - [`Zed.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Zed.md) — `context_servers` key in `settings.json`; stdio only; bridge required
  - [`GitHub Copilot.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/GitHub%20Copilot.md) — Uses VS Code `.vscode/mcp.json` with `servers` + `type` key
  - [`OpenAI Codex CLI.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/OpenAI%20Codex%20CLI.md) — TOML format at `~/.codex/config.toml` with `[mcp_servers.pieces]`
  - [`Google Gemini CLI.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Google%20Gemini%20CLI.md) — `~/.gemini/settings.json`; use `httpUrl` for HTTP, `url` for SSE
  - [`Amazon Q Developer.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Amazon%20Q%20Developer.md) — `~/.aws/amazonq/default.json` with `servers` + `type`
  - [`ChatGPT Developer Mode.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/ChatGPT%20Developer%20Mode.md) — Connectors UI; HTTPS required; Pro/Plus/Business/Enterprise/Education plans
  - [`Raycast.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Raycast.md) — `mcp-config.json` file; stdio only; bridge required; macOS only
  - [`Rovo Dev CLI.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/Rovo%20Dev%20CLI.md) — `~/.rovodev/mcp.json` with `servers` + `transport` key
  - [`OpenClaw.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/OpenClaw.md) — MCPorter config at `~/.openclaw/workspace/config/mcporter.json`
- **[`CHANGELOG.md`](./CHANGELOG.md)** — This file. Full PR history from December 2025 to present.

### Changed

- **[`README.md`](./README.md)** — Replaced plain 3-item MCP bullet list with a structured table covering all 4 core MCP guides; added MCP Guides Index link; corrected tool count to 19; added Quick Start entry for MCP; updated "What LTM Captures" to include audio.
- **[`releases/Whats New in Pieces 5.0.3.md`](./releases/Whats%20New%20in%20Pieces%205.0.3.md)** — Replaced vague "check the documentation" prose in the Expanded MCP Server "How to Use" section with direct links to [LTM Tools Reference](./guides/MCP/Pieces%20MCP%20and%20LTM%20Tools%20Reference.md), [Agent Setups & Integrations](./guides/MCP/Agent%20Setups%20%26%20Integrations/README.md), [Ngrok guide](./guides/MCP/Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md), and [mcp-remote guide](./guides/MCP/Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md). Removed redundant static image below Custom Summary Templates video. Merged main's LaTeX video URL.
- **[`guides/MCP/README.md`](./guides/MCP/README.md)** — Corrected tool count 17 → 19 in three places; added Claude Cowork and OpenClaw to the tool list; added Pieces 5.0.3 release attribution blockquote.
- **[`guides/MCP/Configuring MCP Clients for Cursor, Claude, Goose, and More.md`](./guides/MCP/Configuring%20MCP%20Clients%20for%20Cursor%2C%20Claude%2C%20Goose%2C%20and%20More.md)** — Corrected tool count 17 → 19; added back-link to MCP index.
- **[`guides/MCP/Agent Setups & Integrations/README.md`](./guides/MCP/Agent%20Setups%20%26%20Integrations/README.md)** — Added [LTM Tools Reference](./guides/MCP/Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) link in intro; added Pieces 5.0.3 mention; added back-link to MCP index.
- All 19 individual agent setup guides — Added **Related Guides** footers (3 links for HTTP-capable tools; 4 links including mcp-remote for stdio-only tools).
- All 4 core MCP guides — Added **Related Guides** sections linking to sibling docs.

### Fixed

- **[`guides/MCP/Connecting to PiecesOS from the Outside World via Ngrok.md`](./guides/MCP/Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md)** — Fixed PowerShell `Start-Job` parameter: `-Arg` → `-ArgumentList` (invalid parameter alias; causes immediate failure on Windows).

---

## [PR #9](https://github.com/pieces-app/pro_tips/pull/9) — Fix LaTeX Video URL (February 18, 2026)

### Fixed

- **[`releases/Whats New in Pieces 5.0.3.md`](./releases/Whats%20New%20in%20Pieces%205.0.3.md)** — Corrected the embedded video URL in the LaTeX Rendering section. A prior commit on the branch had replaced the correct video asset with an incorrect URL; this restores the original from main.

---

## [PR #8](https://github.com/pieces-app/pro_tips/pull/8) — New Guides: Time Breakdown, LTM Audio, macOS Permissions, Discount Codes (February 18, 2026)

### Added

- **[`guides/How to Enable LTM Audio Capture.md`](./guides/How%20to%20Enable%20LTM%20Audio%20Capture.md)** — Video-guided walkthrough for enabling LTM Audio (introduced in [Pieces 5.0.3](./releases/Whats%20New%20in%20Pieces%205.0.3.md)) via Desktop App (User Profile) and PiecesOS Toolbar. Covers macOS, Windows, and Linux; includes role-specific query examples; links to the [macOS permissions guide](./guides/How%20to%20Set%20Up%20macOS%20Permissions%20for%20LTM%20Audio.md).
- **[`guides/How to Set Up macOS Permissions for LTM Audio.md`](./guides/How%20to%20Set%20Up%20macOS%20Permissions%20for%20LTM%20Audio.md)** — Step-by-step guide for granting PiecesOS microphone access and Screen & System Audio Recording on macOS. Covers both enable paths, permission dialogs, verification, and troubleshooting.
- **[`guides/How to Generate a Time Breakdown with a Custom Time Range.md`](./guides/How%20to%20Generate%20a%20Time%20Breakdown%20with%20a%20Custom%20Time%20Range.md)** — Video-guided walkthrough for reconstructing billable hours using the configurable time ranges introduced in [Pieces 5.0.3](./releases/Whats%20New%20in%20Pieces%205.0.3.md) (last 24h, last 2 days, last week, custom). The Time Breakdown feature itself shipped in [Pieces 5.0.1](./releases/Whats%20New%20in%20Pieces%205.0.1.md).
- **[`guides/How to Create and Save Custom Summary Templates.md`](./guides/How%20to%20Create%20and%20Save%20Custom%20Summary%20Templates.md)** — Video-guided walkthrough for building single-click summary templates (introduced in [Pieces 5.0.3](./releases/Whats%20New%20in%20Pieces%205.0.3.md)) with custom scoping (time range, websites, projects, apps). Includes 11 copyable use-case prompts.
- **[`guides/How to Apply a Discount Code at Checkout for Pieces Pro or Enterprise.md`](./guides/How%20to%20Apply%20a%20Discount%20Code%20at%20Checkout%20for%20Pieces%20Pro%20or%20Enterprise.md)** — Video-guided walkthrough for the full checkout flow and applying discount codes, including finding the "Add discount" field and troubleshooting invalid codes.

### Changed

- **[`releases/Whats New in Pieces 5.0.3.md`](./releases/Whats%20New%20in%20Pieces%205.0.3.md)** — Added embedded video walkthroughs for LTM Audio, Custom Summary Templates, Time Breakdown, and LaTeX Rendering sections. Fixed broken links. Added "Summarize Recent Meetings" coming-soon callout. Replaced "Copilot" terminology with "Pieces Chat" throughout. Added "Under the Hood — PiecesOS 12.3.8" section and expanded "What's Next" section.
- **[`README.md`](./README.md)** — Added entries for all five new guides.

---

## [PR #7](https://github.com/pieces-app/pro_tips/pull/7) — Pieces 5.0.3 Release Notes (February 17, 2026)

### Added

- **[`releases/Whats New in Pieces 5.0.3.md`](./releases/Whats%20New%20in%20Pieces%205.0.3.md)** — Comprehensive release notes for Pieces Desktop 5.0.3 and PiecesOS 12.3.8, covering:
  - 🎤 **LTM Audio (Preview)** — Dual-stream microphone + system audio capture for meeting context. *(How-to guide added in [PR #8](https://github.com/pieces-app/pro_tips/pull/8): [How to Enable LTM Audio Capture](./guides/How%20to%20Enable%20LTM%20Audio%20Capture.md))*
  - 📋 **Custom Summary Templates** — Save scoped templates for one-click generation. *(How-to guide added in [PR #8](https://github.com/pieces-app/pro_tips/pull/8): [How to Create and Save Custom Summary Templates](./guides/How%20to%20Create%20and%20Save%20Custom%20Summary%20Templates.md))*
  - 🔌 **Expanded MCP Server** — 39-tool suite replacing the original 2-tool server (`ask_pieces_ltm` + `create_pieces_memory`). *(Full documentation added in [PR #11](https://github.com/pieces-app/pro_tips/pull/11): [Pieces MCP and LTM Tools Reference](./guides/MCP/Pieces%20MCP%20and%20LTM%20Tools%20Reference.md))*
  - ⏱️ **Time Breakdown Time Ranges** — Configurable windows (24h, 2 days, week, custom). *(How-to guide added in [PR #8](https://github.com/pieces-app/pro_tips/pull/8): [How to Generate a Time Breakdown with a Custom Time Range](./guides/How%20to%20Generate%20a%20Time%20Breakdown%20with%20a%20Custom%20Time%20Range.md))*
  - 📐 **LaTeX Rendering** — Mathematical expressions in summaries and Pieces Chat.
  - ⚙️ **PiecesOS 12.3.8** — Audio ingestion engine, next-gen agentic runtime, reliability fixes.

### Changed

- **[`README.md`](./README.md)** — Added 5.0.3 to the Latest Release section.

---

## [PR #6](https://github.com/pieces-app/pro_tips/pull/6) — Improve Query Code Blocks and Fix README Version (January 27, 2026)

### Changed

- **[`guides/10 Queries To Ask Pieces LTM after 24-48 Hours of Background Memory Formation.md`](./guides/10%20Queries%20To%20Ask%20Pieces%20LTM%20after%2024-48%20Hours%20of%20Background%20Memory%20Formation.md)** — Added `text` language identifier to all query code blocks (enables GitHub copy button); wrapped long queries to avoid horizontal scrolling.
- **[`guides/5 Queries To Ask Pieces LTM after 2+ Months of Background Memory Formation.md`](./guides/5%20Queries%20To%20Ask%20Pieces%20LTM%20after%202%2B%20Months%20of%20Background%20Memory%20Formation.md)** — Same code block improvements applied.
- **[`README.md`](./README.md)** — Fixed stale version reference.

---

## [PR #5](https://github.com/pieces-app/pro_tips/pull/5) — Pieces 5.0.1 Release Notes (January 27, 2026)

### Added

- **[`releases/Whats New in Pieces 5.0.1.md`](./releases/Whats%20New%20in%20Pieces%205.0.1.md)** — Release notes for Pieces Desktop 5.0.1 and PiecesOS 12.3.6, covering:
  - ⏱️ **Time Breakdown** — Reconstruct billable hours from captured workstream context. *(How-to guide with custom time range support added in [PR #8](https://github.com/pieces-app/pro_tips/pull/8): [How to Generate a Time Breakdown with a Custom Time Range](./guides/How%20to%20Generate%20a%20Time%20Breakdown%20with%20a%20Custom%20Time%20Range.md))*
  - 🔍 **Timeline Search** — Find summaries and conversations by keyword.
  - 🕒 **Time-Based Filters** — Filter Timeline by specific time ranges.
  - 🎛️ **Enhanced Model Selection** — Inline model descriptions for faster switching.
  - 🔐 **AWS Bedrock Inference Profiles** — Enterprise-grade model management.
  - 💬 **Summary to Chat** — Go deeper with one tap from any summary.
  - 🎬 **Single-Click Summary Previews** — Video tutorials before generation. *(Custom Summary Templates, which extend Single-Click Summaries, documented in [PR #8](https://github.com/pieces-app/pro_tips/pull/8): [How to Create and Save Custom Summary Templates](./guides/How%20to%20Create%20and%20Save%20Custom%20Summary%20Templates.md))*

### Changed

- **[`README.md`](./README.md)** — Added 5.0.1 to the Latest Release section; added YouTube playlist link for Single-Click Summary tutorials.

---

## [PR #4](https://github.com/pieces-app/pro_tips/pull/4) — 5 Queries To Ask Pieces LTM after 2+ Months (January 12, 2026)

### Added

- **[`guides/5 Queries To Ask Pieces LTM after 2+ Months of Background Memory Formation.md`](./guides/5%20Queries%20To%20Ask%20Pieces%20LTM%20after%202%2B%20Months%20of%20Background%20Memory%20Formation.md)** — Strategic query guide for senior professionals with accumulated work history. Covers 2 practical search queries, 2 collaboration & efficiency queries, and 1 strategic planning query. Pairs with the earlier [10 Queries guide](./guides/10%20Queries%20To%20Ask%20Pieces%20LTM%20after%2024-48%20Hours%20of%20Background%20Memory%20Formation.md) for a complete query progression path.

### Changed

- **[`README.md`](./README.md)** — Added entry for the new guide; updated Quick Start to distinguish between 24-48 hour and 2+ month query strategies.

---

## [PR #3](https://github.com/pieces-app/pro_tips/pull/3) — What's New in Pieces 5.0.0 (January 5, 2026)

### Added

- **[`releases/Whats New in Pieces 5.0.0.md`](./releases/Whats%20New%20in%20Pieces%205.0.0.md)** — Comprehensive release notes for Pieces Desktop 5.0.0 and PiecesOS 12.3.4, covering:
  - 🏡 **New Home Base** — Unified navigation and consistent UI experience.
  - 🔍 **Browse, Converse, Generate** — Powerful in-place filtering.
  - 👤 **Personalization & Disambiguation** — Smarter understanding of work and team dynamics.
  - ☀️ **Single-Click Summaries** — Morning Brief, Day Recap, Standup, and more. *(Extended with video tutorial previews in [Pieces 5.0.1](./releases/Whats%20New%20in%20Pieces%205.0.1.md); extended with Custom Summary Templates in [Pieces 5.0.3](./releases/Whats%20New%20in%20Pieces%205.0.3.md) — how-to guide: [How to Create and Save Custom Summary Templates](./guides/How%20to%20Create%20and%20Save%20Custom%20Summary%20Templates.md))*
  - ⚙️ **Core engine improvements** — Performance and accuracy upgrades.

### Changed

- **[`README.md`](./README.md)** — Added 5.0.0 to the Latest Release section.

---

## [PR #1](https://github.com/pieces-app/pro_tips/pull/1) — Snap Packages Update Guide (December 9, 2025)

### Added

- **[`guides/How to Update Pieces Snap Packages.md`](./guides/How%20to%20Update%20Pieces%20Snap%20Packages.md)** — Step-by-step process for updating Pieces Desktop and PiecesOS on Linux via Snap: shutdown, version check, update, and relaunch sequence with troubleshooting tips.

### Changed

- **[`README.md`](./README.md)** — Added entry for the new guide.
