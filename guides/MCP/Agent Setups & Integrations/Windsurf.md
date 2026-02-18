# Connecting Pieces MCP to Windsurf

**Tool type:** AI-first IDE (desktop)
**Website:** [windsurf.com](https://windsurf.com)
**Transport support:** stdio, SSE (legacy), Streamable HTTP

---

## Config File Location

| Platform | Path |
|----------|------|
| **All platforms** | `~/.codeium/windsurf/mcp_config.json` |

---

## JSON Format

Windsurf uses `mcpServers` as the root key. For **HTTP/remote servers**, the key is **`serverUrl`** (not `url`).

### Local Setup (Streamable HTTP — recommended)

> **Recommended when PiecesOS and Windsurf are on the same machine.**

```json
{
  "mcpServers": {
    "pieces": {
      "serverUrl": "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

### Local Setup (SSE — legacy)

```json
{
  "mcpServers": {
    "pieces": {
      "serverUrl": "http://localhost:39300/model_context_protocol/2024-11-05/sse"
    }
  }
}
```

---

## Remote Setup (ngrok)

> Use this when Windsurf is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```json
{
  "mcpServers": {
    "pieces": {
      "serverUrl": "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

---

## Authentication Headers

To add auth headers (not required for Pieces):

```json
{
  "mcpServers": {
    "pieces": {
      "serverUrl": "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp",
      "headers": {
        "Authorization": "Bearer ${env:PIECES_TOKEN}"
      }
    }
  }
}
```

Environment variables use the `${env:VAR_NAME}` syntax.

---

## Adding via MCP Marketplace

1. Open the Cascade panel in Windsurf
2. Click the **MCP icon** to open the MCP Marketplace
3. Search for Pieces, or click **"Add custom"** and point to your URL

---

## Updating

Edit `~/.codeium/windsurf/mcp_config.json`, update the `serverUrl`, then restart Windsurf.

---

## Verification

1. Open Cascade panel
2. Check the MCP tools section — Pieces LTM tools should appear
3. Ask Cascade: "What Pieces tools are available?"

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Config not loading | Restart Windsurf after editing `mcp_config.json` |
| Server not connecting | Use `serverUrl` (not `url`) — this is a Windsurf-specific key name |
| Environment variable not resolving | Use `${env:VAR_NAME}` syntax (with `env:` prefix) |
| Need to disable a server | Add `"disabled": true` to the server config object |

---

## Related Guides

- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Back to All Agent Setup Guides</a>&nbsp;&nbsp;</td>
</tr></table>
