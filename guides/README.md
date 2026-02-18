# Guides

Practical guides for getting the most out of Pieces—organized by what you're trying to accomplish.

---

## Getting Started with Long-Term Memory Queries

Pieces Long-Term Memory (LTM) captures context from your work throughout the day—code editors, browsers, communication tools, terminals, and audio—and makes it queryable in natural language. These guides help you go from first query to fluent.

| Guide | What you'll learn |
|-------|------------------|
| **[How to Query LTM in Pieces Copilot](./How%20to%20Query%20LTM%20in%20Pieces%20Copilot.md)** | The 5 keys to great LTM queries (Time, Source, Gestures, Topic, People), how to combine them, troubleshooting tips, and a quick-reference cheat sheet. Start here. |
| **[10 Queries To Ask Pieces LTM after 24-48 Hours](./10%20Queries%20To%20Ask%20Pieces%20LTM%20after%2024-48%20Hours%20of%20Background%20Memory%20Formation.md)** | Tested, practical examples organized by use case: daily work queries, reflective queries, and analytical queries—ready to copy and try yourself. |
| **[5 Essential Queries for 2+ Months of LTM](./5%20Queries%20To%20Ask%20Pieces%20LTM%20after%202%2B%20Months%20of%20Background%20Memory%20Formation.md)** | Strategic queries for when you've built up a meaningful history: collaboration analysis, workflow optimization, and quarterly performance reflection. |

---

## Daily Workflows & Summaries

Pieces generates structured summaries from your captured workstream—automatically, or on your terms. These guides cover the tools that turn your work history into actionable output.

| Guide | What you'll learn |
|-------|------------------|
| **[How to Use the Workstream Activity Timeline](./How%20to%20Use%20the%20Workstream%20Activity%20Timeline.md)** | How the Timeline captures events and generates 20-minute summaries, how to browse and search your work history, and how to start chats and share directly from the Timeline. |
| **[How to Create and Save Custom Summary Templates](./How%20to%20Create%20and%20Save%20Custom%20Summary%20Templates.md)** | Build summary templates scoped to specific time ranges, websites, projects, or applications—then generate them with one click every time. Includes 11 copyable use case prompts. |
| **[How to Generate a Time Breakdown with a Custom Time Range](./How%20to%20Generate%20a%20Time%20Breakdown%20with%20a%20Custom%20Time%20Range.md)** | Reconstruct your billable hours from captured context for any time window—last 24 hours, last week, or a custom range. Covers use cases for daily timesheets, mid-week client updates, and weekly billing summaries. |
| **[Navigating the Desktop App UI with the Power Menu](./Navigating%20the%20Desktop%20App%20UI%20with%20the%20Power%20Menu.md)** | Use the Power Menu to jump between Workstream Activity and Pieces Copilot without losing context. Keyboard shortcuts, search tips, and common workflows. |

---

## Audio & Context Capture

LTM Audio brings meetings, pair programming sessions, and video calls into your Long-Term Memory. These guides walk through enabling audio capture and satisfying the macOS permissions it requires.

| Guide | What you'll learn |
|-------|------------------|
| **[How to Enable LTM Audio Capture](./How%20to%20Enable%20LTM%20Audio%20Capture.md)** | Two methods to enable LTM Audio (Desktop App and PiecesOS Toolbar), role-specific query examples for developers, managers, lawyers, accountants, and executives, and privacy controls. |
| **[How to Set Up macOS Permissions for LTM Audio](./How%20to%20Set%20Up%20macOS%20Permissions%20for%20LTM%20Audio.md)** | Step-by-step macOS permission setup: microphone access for PiecesOS, Screen & System Audio Recording access, verification that audio context is flowing, and troubleshooting for common permission issues. |

---

## MCP & AI Agent Integration

The Pieces MCP Server gives AI agents like Cursor, Claude Code, and Goose direct access to your Long-Term Memory through 39 tools covering full-text search, vector search, temporal queries, batch retrieval, and more.

**[→ MCP Guides Index](./MCP/README.md)** — Start here for the full overview.

| Guide | What you'll learn |
|-------|------------------|
| **[Pieces MCP and LTM Tools Reference](./MCP/Pieces%20MCP%20and%20LTM%20Tools%20Reference.md)** | Complete reference for all 39 MCP tools: `ask_pieces_ltm`, `create_pieces_memory`, 14 full-text search tools, 5 vector search tools, `material_identifiers`, `extract_temporal_range`, and 16 batch snapshot tools—with parameters, examples, and agent instructions. |
| **[Agent Setups & Integrations](./MCP/Agent%20Setups%20%26%20Integrations/README.md)** | Step-by-step setup for 19 MCP-compatible tools: Cursor, Claude Desktop, Claude Code, VS Code, Windsurf, Goose, Cline, Continue.dev, JetBrains, Zed, GitHub Copilot, OpenAI Codex CLI, Gemini CLI, Amazon Q, ChatGPT Developer Mode, Raycast, and more. |
| **[Connecting to PiecesOS via Ngrok](./MCP/Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md)** | Expose your local PiecesOS over HTTPS so cloud-based agents (Claude web, ChatGPT, GitHub Actions, Zapier) can reach your Long-Term Memory. Includes auto-discovery scripts for Bash and PowerShell. |
| **[Bridging Local MCP Clients with mcp-remote](./MCP/Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md)** | Connect stdio-only clients (Claude Desktop JSON config, Zed, Raycast) to any remote MCP server. Covers transport strategy, OAuth 2.1, bearer token injection, and a catalog of public remote MCP servers. |

---

## Setup & Administration

| Guide | What you'll learn |
|-------|------------------|
| **[How to Apply a Discount Code at Checkout](./How%20to%20Apply%20a%20Discount%20Code%20at%20Checkout%20for%20Pieces%20Pro%20or%20Enterprise.md)** | The full checkout flow from the Upgrade button to purchase completion, where to find the discount field, and troubleshooting for invalid codes or existing subscriptions. |
| **[How to Update Pieces Snap Packages (Linux)](./How%20to%20Update%20Pieces%20Snap%20Packages.md)** | A 4-step process to update Pieces on Linux/Snap: shutdown both Desktop App and PiecesOS, check installed versions, update via Snap, and relaunch in the correct order. |

---

## What LTM Captures

Long-Term Memory passively captures context from:

- **Code editors & IDEs** — VS Code, IntelliJ, Xcode, and others
- **Web browsers** — Chrome, Firefox, Safari
- **Communication tools** — Teams, Slack, Discord
- **Documentation platforms** — Notion, Confluence, GitHub
- **Terminal & command line**
- **Microphone & system audio** — meetings, pair programming sessions, video calls, and presentations (via [LTM Audio](./How%20to%20Enable%20LTM%20Audio%20Capture.md), introduced in [Pieces 5.0.3](../releases/Whats%20New%20in%20Pieces%205.0.3.md))

Everything becomes queryable through natural language—no need to remember exact file names, commands, or when something happened.

---

## Quick Start by Goal

| I want to... | Start here |
|-------------|-----------|
| Write my first LTM query | [How to Query LTM in Pieces Copilot](./How%20to%20Query%20LTM%20in%20Pieces%20Copilot.md) |
| Try practical query examples | [10 Queries after 24-48 Hours](./10%20Queries%20To%20Ask%20Pieces%20LTM%20after%2024-48%20Hours%20of%20Background%20Memory%20Formation.md) |
| Reconstruct my billable hours | [Time Breakdown with Custom Ranges](./How%20to%20Generate%20a%20Time%20Breakdown%20with%20a%20Custom%20Time%20Range.md) |
| Capture my meetings in memory | [How to Enable LTM Audio Capture](./How%20to%20Enable%20LTM%20Audio%20Capture.md) |
| Build a recurring summary template | [Custom Summary Templates](./How%20to%20Create%20and%20Save%20Custom%20Summary%20Templates.md) |
| Connect Cursor or Claude Code to my memory | [Agent Setups & Integrations](./MCP/Agent%20Setups%20%26%20Integrations/README.md) |
| Access Pieces from a remote machine or cloud agent | [Connecting to PiecesOS via Ngrok](./MCP/Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) |
| Browse my work history visually | [Workstream Activity Timeline](./How%20to%20Use%20the%20Workstream%20Activity%20Timeline.md) |

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="../README.md">← Back to Pro Tips</a>&nbsp;&nbsp;</td>
</tr></table>
