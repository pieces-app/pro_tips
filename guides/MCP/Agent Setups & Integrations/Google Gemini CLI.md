# Connecting Pieces MCP to Google Gemini CLI

**Tool type:** CLI agent
**Website:** [geminicli.com](https://geminicli.com)
**Transport support:** stdio, SSE, Streamable HTTP

---

## Config File Location

| Scope | Path |
|-------|------|
| **User (global)** | `~/.gemini/settings.json` |
| **Workspace** | `YOUR_PROJECT/.gemini/settings.json` |

Workspace settings override user settings.

---

## JSON Format

Gemini CLI uses `mcpServers` as the root key. For HTTP servers, use `httpUrl`; for SSE servers, use `url`.

### Local Setup (Streamable HTTP — recommended)

> **Recommended when PiecesOS and Gemini CLI are on the same machine.**

```json
{
  "mcpServers": {
    "pieces": {
      "httpUrl": "http://localhost:39300/model_context_protocol/2025-03-26/mcp",
      "timeout": 30000
    }
  }
}
```

### Local Setup (SSE)

```json
{
  "mcpServers": {
    "pieces": {
      "url": "http://localhost:39300/model_context_protocol/2024-11-05/sse",
      "timeout": 30000
    }
  }
}
```

---

## Remote Setup (ngrok)

> Use this when Gemini CLI is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```json
{
  "mcpServers": {
    "pieces": {
      "httpUrl": "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp",
      "timeout": 30000
    }
  }
}
```

---

## Advanced Config Options

```json
{
  "mcpServers": {
    "pieces": {
      "httpUrl": "http://localhost:39300/model_context_protocol/2025-03-26/mcp",
      "timeout": 30000,
      "enabled_tools": ["ask_pieces_ltm", "workstream_summaries_full_text_search"],
      "disabled_tools": []
    }
  }
}
```

- `timeout` — in milliseconds
- `enabled_tools` — allowlist of specific tools
- `disabled_tools` — denylist (applied after `enabled_tools`)
- `bearer_token_env_var` — env var containing a bearer token for auth
- `env_http_headers` — map of env vars to HTTP headers

---

## Updating

Edit `~/.gemini/settings.json`, update the URL, and start a new Gemini CLI session.

---

## Verification

1. Start a Gemini CLI session: `gemini`
2. Gemini discovers and registers tools from MCP servers on startup
3. Ask: "What Pieces tools are available?"

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Settings file not found | Create `~/.gemini/settings.json` manually |
| HTTP key vs SSE key | Use `httpUrl` for HTTP/Streamable HTTP, `url` for SSE — they are different fields |
| Tools not discovered | Restart Gemini CLI after editing settings |
| OAuth prompt | Pieces doesn't require OAuth; dismiss if prompted |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

[← Back to All Agent Setup Guides](./README.md)
