# Pieces MCP Guides

Your AI agents are powerful in the moment, but they forget everything between sessions. Pieces gives them a Long-Term Memory (LTM) -- a continuously captured, locally processed, semantically searchable record of your work across every application, meeting, and coding session. These guides cover how to connect AI agents to that memory via the Model Context Protocol (MCP), and how to extend that connection beyond your local machine.

---

## Available Guides

### [Pieces MCP and LTM Tools Reference](./Pieces%20MCP%20and%20LTM%20Tools%20Reference.md)

The complete reference for all 39 tools exposed by the Pieces MCP server. This is the guide to read when you want to understand what your agents can do with your Long-Term Memory.

**Use this guide when you need to:**

- **Understand what agents can access** -- Pieces passively captures clipboard operations, screenshots (with OCR), audio transcriptions, browser activity, and application focus. This guide explains every tool that searches, filters, and retrieves that data.
- **Build agentic workflows** -- Learn the two-step search-then-retrieve pattern, temporal filtering, and multi-tool chains that let agents answer questions like "What did I work on last week?" or "What did we decide in that meeting about the API?"
- **Choose the right search strategy** -- Full-text search for exact keywords (function names, error messages, URLs). Vector search for meaning-based retrieval (concepts described with different words). `ask_pieces_ltm` for general questions where Pieces handles the strategy internally.
- **Enable cross-agent memory** -- Use `create_pieces_memory` to save context from one agent (e.g., a debugging breakthrough in Claude Code) that another agent (e.g., Cursor) can retrieve days or weeks later.
- **Generate standups, recaps, and reports** -- Combine `extract_temporal_range`, `material_identifiers`, and `workstream_summaries_batch_snapshot` to reconstruct exactly what happened during any time period.

> **Pieces 5.0.3 (PiecesOS 12.3.8)** expanded the MCP server from the original `ask_pieces_ltm` and `create_pieces_memory` tools to this full suite of 39 tools. See [What's New in Pieces 5.0.3](../../releases/Whats%20New%20in%20Pieces%205.0.3.md#expanded-mcp-server-richer-long-term-memory-access-in-cursor-claude-code--more) for the full announcement.

Covers: `ask_pieces_ltm`, `create_pieces_memory`, 14 full-text search tools, 5 vector search tools, `material_identifiers`, `extract_temporal_range`, and 16 batch snapshot tools -- with parameters, examples, agent instructions, and smoke test results for every tool.

---

### [Connecting to PiecesOS from the Outside World via Ngrok](./Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md)

PiecesOS runs on localhost. Ngrok gives it a public HTTPS URL. This guide walks you through the full setup -- installation, port discovery, tunnel creation, and ready-to-copy scripts for Bash and PowerShell.

**Use this guide when you need to:**

- **Connect cloud-hosted AI to your local memory** -- Claude's web interface, ChatGPT, or any cloud-based AI tool that supports MCP can reach your local PiecesOS via an ngrok HTTPS URL. Your memories stay local; only the queries and responses travel over the wire.
- **Run Pieces MCP from GitHub Actions or CI/CD** -- An agent running in a GitHub Actions workflow can query your LTM for context about the codebase, recent decisions, or past debugging sessions by connecting to your ngrok-exposed MCP endpoint.
- **Integrate with automation platforms** -- Zapier, Make, n8n, or any HTTP-capable automation tool can hit your PiecesOS APIs over the ngrok tunnel. Trigger workflows based on your work activity, pull summaries into Notion, or send standup digests to Slack.
- **Access your LTM from another machine** -- Working from a different laptop, a cloud IDE (Codespaces, Gitpod), or a colleague's machine? Point their MCP client at your ngrok URL and they connect to your memory as if they were on localhost.
- **Demo Pieces to a remote audience** -- Share your ngrok URL during a presentation or sales call and let others see your LTM in action from their own browser.
- **Test MCP integrations without deploying** -- Building an MCP client or integration? Point it at your ngrok URL during development instead of setting up a cloud deployment.

Covers: ngrok installation (macOS, Windows, Linux), one-time auth setup, PiecesOS port discovery (39300-39333), Bash and PowerShell one-liner scripts that auto-detect the port, start the tunnel, and output your base HTTPS + MCP URLs.

---

### [Bridging Local MCP Clients to Remote Servers with mcp-remote](./Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md)

Many MCP clients — Claude Desktop's JSON config, Amazon Q Developer, and others — only launch local stdio processes. They cannot put a URL in their config. `mcp-remote` is the bridge: a local Node.js process that looks like a stdio server to your client while internally speaking HTTPS to any remote MCP server.

**Use this guide when you need to:**

- **Connect Claude Desktop (JSON config) to any remote server** -- Claude Desktop's `claude_desktop_config.json` only supports stdio. `mcp-remote` is the standard solution for reaching GitHub, Linear, Notion, Cloudflare, PiecesOS, or any HTTP-based MCP server from the JSON config.
- **Inject auth headers automatically** -- The `--header` flag injects `Authorization: Bearer …` (or any custom header) into every request, handling API-key-protected servers without OAuth complexity.
- **Handle OAuth transparently** -- `mcp-remote` implements the full OAuth 2.1 + PKCE + Dynamic Client Registration flow. Run it once, authorize in your browser, and tokens are stored and refreshed automatically — no manual credential management.
- **Connect to public cloud MCP servers** -- GitHub, Linear, Notion, Sentry, PayPal, Cloudflare, Make.com, Buildkite, and dozens more all host remote MCP servers. `mcp-remote` is how stdio clients reach them.
- **Combine with ngrok** -- Expose a local server via ngrok, then use `mcp-remote` to bridge other stdio clients to that tunnel URL. One person runs the server; the whole team connects.
- **Filter tools from untrusted servers** -- The `--ignore-tool` flag blocks specific tools by wildcard pattern before they ever reach your AI client.

Covers: transport strategy selection (`http-first`, `sse-only`, `http-only`), complete CLI flag reference, OAuth 2.1 flow deep-dive, token storage and reset, configuration examples for Claude Desktop, Cursor, Windsurf, VS Code, Goose, JetBrains, and Amazon Q Developer, a public remote MCP server catalog, the ngrok + `mcp-remote` combination pattern, CVE-2025-6514 security advisory, and a full troubleshooting table.

---

### [Tutorial: Connect PiecesOS to Claude Desktop with mcp-remote](./Tutorials/Using%20MCP%20Remote%20to%20Connect%20PiecesOS%20to%20Claude%20Desktop.md)

A focused, copy-paste-first tutorial for the most common bridge setup: Claude Desktop JSON config -> `mcp-remote` -> PiecesOS SSE endpoint.

**Use this guide when you need to:**

- **Set up Claude Desktop quickly** -- Follow a single end-to-end path without the full multi-client transport deep-dive.
- **Validate your local PiecesOS bridge** -- Includes port discovery, config placement, and tool verification steps.
- **Configure remote access with the same pattern** -- Includes an optional ngrok + `mcp-remote` configuration block for remote PiecesOS.

Covers: prerequisites, PiecesOS port discovery, Claude Desktop config file paths, working `mcp-remote` JSON examples for local and remote setups, verification checks, and troubleshooting.

---

### [Agent Setups & Integrations](./Agent%20Setups%20%26%20Integrations/)

Step-by-step setup guides for connecting **19 MCP-compatible tools** to your Pieces Long-Term Memory. Each guide covers local (localhost) and remote (ngrok HTTPS) configuration with exact JSON configs, file paths, and troubleshooting.

**Use this guide when you need to:**

- **Set up Pieces MCP in your tool** -- Individual guides for Cursor, Claude Desktop, Claude Code, Claude Cowork, VS Code, Windsurf, Goose, Cline, Continue.dev, JetBrains IDEs, Zed, GitHub Copilot, OpenAI Codex CLI, Google Gemini CLI, Amazon Q Developer, ChatGPT Developer Mode, Raycast, Rovo Dev CLI, and OpenClaw.
- **Know which transport your tool supports** -- A single matrix table shows stdio, SSE, and Streamable HTTP support for every tool, plus whether it can connect to remote URLs directly.
- **Bridge stdio-only tools to Pieces** -- Tools like Zed, Raycast, and Claude Desktop (JSON config) only support stdio. The bridge section covers `mcp-remote`, `supergateway`, and `mcp-proxy` with ready-to-copy configs.

Covers: 19 tool-specific guides, transport support matrix, stdio-to-HTTP bridge setup, local and remote (ngrok) configuration patterns.

---

## Placeholder Guides

- **Security best practices for exposing MCP endpoints** -- Authentication, IP allowlists, traffic policies, and when to keep tunnels open vs. closed (planned).

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="../How%20to%20Update%20Pieces%20Snap%20Packages.md">← Previous: How to Update Pieces Snap Packages</a>&nbsp;&nbsp;</td>
<td align="right">&nbsp;&nbsp;<a href="./Pieces%20MCP%20and%20LTM%20Tools%20Reference.md">Next: Pieces MCP and LTM Tools Reference →</a>&nbsp;&nbsp;</td>
</tr></table>
