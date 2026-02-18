# Connecting Pieces MCP to Cursor

**Tool type:** AI-first code editor (desktop)
**Website:** [cursor.com](https://cursor.com)
**Transport support:** stdio, SSE, Streamable HTTP

---

## Config File Location

| Scope | Path |
|-------|------|
| **Global (all projects)** | `~/.cursor/mcp.json` |
| **Project-specific** | `.cursor/mcp.json` in your project root |

On **Windows**, the global path is `%USERPROFILE%\.cursor\mcp.json`.

Project-level configs can be committed to version control so teammates automatically inherit them.

---

## JSON Format

The root key is `mcpServers`. For a remote HTTP/SSE server, use the `url` key:

```json
{
  "mcpServers": {
    "pieces": {
      "url": "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

For a stdio server (local process):

```json
{
  "mcpServers": {
    "pieces": {
      "command": "npx",
      "args": ["-y", "some-mcp-package"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

---

## Local Setup (localhost)

> **Recommended when PiecesOS and Cursor are on the same machine.** The `http://localhost` URL is direct and needs no extra setup.

```json
{
  "mcpServers": {
    "pieces": {
      "url": "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

> **Port note:** PiecesOS may run on any port from 39300-39333. Check yours at **PiecesOS Quick Menu > MCP Servers**, or probe `http://localhost:PORT/.well-known/version` for each port.

---

## Remote Setup (ngrok)

> Use this when Cursor is running on a **different machine** from PiecesOS, or when you need a public HTTPS URL. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```json
{
  "mcpServers": {
    "pieces": {
      "url": "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

---

## Verification

1. Open Cursor Settings (Cmd+Shift+J on macOS, Ctrl+Shift+J on Windows/Linux)
2. Navigate to the **MCP** section
3. Confirm "pieces" appears in the server list with a green status indicator
4. Open Cursor Chat and ask: "What tools do you have from Pieces?"

---

## Updating

To update the MCP URL (e.g., after your [ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) address changes):

1. Edit `~/.cursor/mcp.json` (or `.cursor/mcp.json`)
2. Update the `url` value
3. Restart Cursor

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Server shows red/disconnected | Verify PiecesOS is running and the port is correct |
| Tools not appearing in chat | Restart Cursor after editing `mcp.json`; Cursor loads MCP config on startup |
| SSE stopped working after upgrade | Some Cursor versions have SSE regressions; switch to Streamable HTTP endpoint (`/model_context_protocol/2025-03-26/mcp`) |
| Project-level config not loading | Ensure the file is at `.cursor/mcp.json` (not `.cursor/config/mcp.json`) |
| Wrong port | Probe ports 39300-39333 with `curl http://localhost:PORT/.well-known/version` |

---

## Related Guides

- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Back to All Agent Setup Guides</a>&nbsp;&nbsp;</td>
</tr></table>
