# Connecting AI Agents to Pieces MCP

Step-by-step setup guides for connecting 19 popular MCP-compatible tools to your Pieces Long-Term Memory server. These integrations connect to the expanded Pieces MCP server introduced in [Pieces 5.0.3](../../../releases/Whats%20New%20in%20Pieces%205.0.3.md#expanded-mcp-server-richer-long-term-memory-access-in-cursor-claude-code--more), which brought the full suite of 39 LTM tools to every MCP-compatible client. For the complete list of tools available to your agents, see the [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md). Each guide covers local (localhost) and remote (ngrok HTTPS) configuration with verified, fact-checked config formats.

---

## Pieces MCP Endpoint URLs

PiecesOS listens on a port in the range **39300–39333**. Discover yours by checking **PiecesOS Quick Menu > MCP Servers**, or probe `http://localhost:PORT/.well-known/version` for each port. See the [ngrok guide](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) for auto-discovery scripts.

| Mode | Streamable HTTP Endpoint | SSE Endpoint (legacy) |
|------|--------------------------|-----------------------|
| **Local** | `http://localhost:PORT/model_context_protocol/2025-03-26/mcp` | `http://localhost:PORT/model_context_protocol/2024-11-05/sse` |
| **Remote (ngrok)** | `https://YOUR_NGROK.ngrok.app/model_context_protocol/2025-03-26/mcp` | `https://YOUR_NGROK.ngrok.app/model_context_protocol/2024-11-05/sse` |

**Use Streamable HTTP by default.** Use SSE only for tools that explicitly require it (noted per guide).

---

## Transport Protocols

**stdio** — Tool spawns a local process; communicates via stdin/stdout. Works on the same machine only. Cannot connect to a remote URL without a bridge.

**SSE (Server-Sent Events)** — Legacy HTTP transport. Two endpoints (GET for server→client stream, POST for client→server). Still widely supported but being phased out in favour of Streamable HTTP.

**Streamable HTTP** — Modern standard (March 2025+). Single HTTP endpoint (`/mcp`) for all communication. Works over HTTPS for remote access. What Pieces exposes at `/model_context_protocol/2025-03-26/mcp`.

---

## Transport Support Matrix

| Tool | Type | stdio | SSE | Streamable HTTP | Direct Remote URL | Config Key | Guide |
|------|------|-------|-----|-----------------|-------------------|------------|-------|
| [Cursor](./Cursor.md) | IDE | Yes | Yes | Yes | Yes | `mcpServers` + `url` | [→](./Cursor.md) |
| [Claude Desktop](./Claude%20Desktop.md) | Desktop | Bridge only | Via Connectors UI | Via Connectors UI | Pro/Max/Team/Ent only | `mcpServers` + `command` | [→](./Claude%20Desktop.md) |
| [Claude Code](./Claude%20Code.md) | CLI | Yes | Yes | Yes | Yes | CLI command | [→](./Claude%20Code.md) |
| [Claude Cowork](./Claude%20Cowork.md) | Desktop agent | Bridge only | Via Connectors UI | Via Connectors UI | Pro/Max/Team/Ent only | Shared with Desktop | [→](./Claude%20Cowork.md) |
| [VS Code](./VS%20Code.md) | IDE | Yes | Yes (`type: "sse"`) | Yes (`type: "http"`) | Yes | `servers` + `type` | [→](./VS%20Code.md) |
| [Windsurf](./Windsurf.md) | IDE | Yes | Yes | Yes | Yes | `mcpServers` + `serverUrl` | [→](./Windsurf.md) |
| [Goose](./Goose.md) | CLI / Desktop | Yes | Yes (`type: sse`) | Yes (`type: streamable_http`) | Yes | YAML `extensions` | [→](./Goose.md) |
| [Cline](./Cline.md) | VS Code Ext | Yes | Yes | Buggy — use SSE | Yes | `mcpServers` + `url` | [→](./Cline.md) |
| [Continue.dev](./Continue.dev.md) | VS Code/JetBrains Ext | Yes | Yes (`type: sse`) | Yes (`type: streamable-http`) | Yes | YAML `mcpServers` array | [→](./Continue.dev.md) |
| [JetBrains IDEs](./JetBrains%20IDEs.md) | IDE | Yes | Limited | Yes | Yes | Settings UI | [→](./JetBrains%20IDEs.md) |
| [Zed](./Zed.md) | IDE | Yes | Bridge only | Bridge only | Needs bridge | `context_servers` | [→](./Zed.md) |
| [GitHub Copilot](./GitHub%20Copilot.md) | VS Code Ext | Yes | Yes | Yes | Yes | `servers` + `type` (same as VS Code) | [→](./GitHub%20Copilot.md) |
| [OpenAI Codex CLI](./OpenAI%20Codex%20CLI.md) | CLI | Yes | -- | Yes | Yes | TOML `mcp_servers` + `url` | [→](./OpenAI%20Codex%20CLI.md) |
| [Google Gemini CLI](./Google%20Gemini%20CLI.md) | CLI | Yes | Yes (`url`) | Yes (`httpUrl`) | Yes | `mcpServers` | [→](./Google%20Gemini%20CLI.md) |
| [Amazon Q Developer](./Amazon%20Q%20Developer.md) | CLI / IDE | Yes | -- | Yes | Yes | `servers` + `type` | [→](./Amazon%20Q%20Developer.md) |
| [ChatGPT Developer Mode](./ChatGPT%20Developer%20Mode.md) | Web | -- | Yes | Yes | Yes (HTTPS only) | Connectors UI | [→](./ChatGPT%20Developer%20Mode.md) |
| [Raycast](./Raycast.md) | macOS launcher | Yes | Bridge only | Bridge only | Needs bridge | `mcpServers` (JSON file) | [→](./Raycast.md) |
| [Rovo Dev CLI](./Rovo%20Dev%20CLI.md) | CLI | Yes | Yes | Yes | Yes | `servers` + `transport` | [→](./Rovo%20Dev%20CLI.md) |
| [OpenClaw](./OpenClaw.md) | Self-hosted agent | Yes | Yes | Yes | Yes | MCPorter `mcpServers` | [→](./OpenClaw.md) |

**"Needs bridge"** = tool supports stdio only; use [`mcp-remote`](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) or `supergateway` to proxy HTTP.
**"Bridge only"** = HTTP is not natively supported but works via a stdio bridge in the config.

---

## stdio-to-HTTP Bridges

For tools that only support stdio (Zed, Raycast, Claude Desktop via JSON config), use a bridge process that proxies stdio calls to the Pieces HTTP endpoint.

### mcp-remote (Recommended)

> **Full guide:** [Bridging Local MCP Clients to Remote Servers with mcp-remote](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) — covers all CLI flags, OAuth 2.1 flow, transport strategies, bearer token injection, security, and per-client config examples.

The npm package is `mcp-remote` (not `@modelcontextprotocol/mcp-remote`).

```bash
# No global install needed — use npx
npx -y mcp-remote http://localhost:39300/model_context_protocol/2024-11-05/sse
```

In any stdio-only tool's config:

```json
{
  "mcpServers": {
    "pieces": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "http://localhost:39300/model_context_protocol/2024-11-05/sse"
      ]
    }
  }
}
```

For remote ([ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md)):

```json
{
  "mcpServers": {
    "pieces": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://YOUR_NGROK.ngrok.app/model_context_protocol/2024-11-05/sse"
      ]
    }
  }
}
```

Flags: `--transport sse-only`, `--header "Authorization: Bearer token"`, `--host 127.0.0.1` — see the [full mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) for complete CLI reference.

### supergateway

Bidirectional bridge: expose a stdio server as SSE, or connect to a remote SSE server via stdio.

```bash
# Connect to remote SSE, expose as stdio:
npx -y supergateway --sse "http://localhost:39300/model_context_protocol/2024-11-05/sse"

# Connect to remote Streamable HTTP, expose as stdio:
npx -y supergateway --streamableHttp "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
```

### mcp-proxy (Python)

```bash
pip install mcp-proxy
mcp-proxy http://localhost:39300/model_context_protocol/2024-11-05/sse
```

---

## Setup Guides

| Guide | Description |
|-------|-------------|
| [Cursor](./Cursor.md) | AI-first IDE with native HTTP support via `url` key in `mcp.json` |
| [Claude Desktop](./Claude%20Desktop.md) | stdio in JSON config; remote via Connectors UI (Pro/Max/Team/Enterprise) |
| [Claude Code](./Claude%20Code.md) | CLI with `claude mcp add --transport http\|sse` |
| [Claude Cowork](./Claude%20Cowork.md) | Autonomous task agent; shares Claude Desktop MCP config |
| [VS Code](./VS%20Code.md) | `servers` key with `type: "http"\|"sse"\|"stdio"` in `.vscode/mcp.json` |
| [Windsurf](./Windsurf.md) | Use `serverUrl` (not `url`) in `~/.codeium/windsurf/mcp_config.json` |
| [Goose](./Goose.md) | YAML config at `~/.config/goose/config.yaml` with `extensions` key |
| [Cline](./Cline.md) | Separate config at `~/.cline/data/settings/cline_mcp_settings.json`; use SSE |
| [Continue.dev](./Continue.dev.md) | YAML in `.continue/config.yaml`; agent mode only; use `streamable-http` type |
| [JetBrains IDEs](./JetBrains%20IDEs.md) | Settings UI > AI Assistant > MCP; 2025.2+ required |
| [Zed](./Zed.md) | `context_servers` key in `settings.json`; stdio only; bridge required |
| [GitHub Copilot](./GitHub%20Copilot.md) | Uses VS Code's `.vscode/mcp.json` with `servers` + `type` key |
| [OpenAI Codex CLI](./OpenAI%20Codex%20CLI.md) | TOML format at `~/.codex/config.toml` with `[mcp_servers.pieces]` |
| [Google Gemini CLI](./Google%20Gemini%20CLI.md) | `~/.gemini/settings.json` with `mcpServers`; use `httpUrl` for HTTP, `url` for SSE |
| [Amazon Q Developer](./Amazon%20Q%20Developer.md) | `~/.aws/amazonq/default.json` with `servers` + `type` |
| [ChatGPT Developer Mode](./ChatGPT%20Developer%20Mode.md) | Connectors UI only; HTTPS required; Pro/Plus/Business/Enterprise/Education plans |
| [Raycast](./Raycast.md) | `mcp-config.json` file; stdio only; bridge required; macOS only |
| [Rovo Dev CLI](./Rovo%20Dev%20CLI.md) | `~/.rovodev/mcp.json` with `servers` + `transport` key |
| [OpenClaw](./OpenClaw.md) | MCPorter config at `~/.openclaw/workspace/config/mcporter.json` |

---

## Related Guides

- [MCP Guides Index](../README.md) — Overview of all Pieces MCP documentation
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access
- [Bridging Local MCP Clients with mcp-remote](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) — Connect stdio-only clients to the Pieces HTTP endpoint

---

| | |
|:---|---:|
| [← Previous: Bridging Local MCP Clients with mcp-remote](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) | |
