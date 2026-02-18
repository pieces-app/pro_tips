# Connecting Pieces MCP to Rovo Dev CLI

**Tool type:** CLI (Atlassian's AI developer tool)
**Website:** [atlassian.com/rovo](https://www.atlassian.com/software/rovo)
**Transport support:** stdio, SSE, Streamable HTTP

---

## Config File Location

| Platform | Path |
|----------|------|
| **All platforms** | `~/.rovodev/mcp.json` |

---

## Local Setup

Edit `~/.rovodev/mcp.json`:

### Streamable HTTP (recommended when PiecesOS is on the same machine)

> **Recommended when PiecesOS and Rovo Dev CLI are on the same machine.**

```json
{
  "servers": {
    "pieces": {
      "name": "Pieces LTM",
      "transport": "http",
      "url": "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

### SSE

```json
{
  "servers": {
    "pieces": {
      "name": "Pieces LTM",
      "transport": "sse",
      "url": "http://localhost:39300/model_context_protocol/2024-11-05/sse"
    }
  }
}
```

---

## Remote Setup (ngrok)

> Use this when Rovo Dev CLI is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```json
{
  "servers": {
    "pieces": {
      "name": "Pieces LTM",
      "transport": "http",
      "url": "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

---

## Opening the Config in Your Editor

```bash
acli rovodev mcp
```

This opens `~/.rovodev/mcp.json` in your default editor.

---

## Managing Servers in Interactive Mode

Within a Rovo Dev session, use the `/mcp` command:

```
/mcp
```

This opens an interactive interface showing:
- Configured servers and their status
- Available tools from each server
- Enable/disable toggles

---

## Disabling a Server

To disable without removing, add to `~/.rovodev/config.yml` (not `mcp.json`):

```yaml
mcp:
  disabled_servers:
    - pieces
```

---

## Updating

Edit `~/.rovodev/mcp.json` (via `acli rovodev mcp` or directly), update the URL, and restart the Rovo Dev session.

---

## Verification

1. Start a Rovo Dev session
2. Run `/mcp list` to see configured servers
3. Ask: "What Pieces tools do you have?"

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Config file not found | Create `~/.rovodev/mcp.json` manually; create `~/.rovodev/` directory first |
| Server not loading | Restart the Rovo Dev session after editing config |
| Transport key name | Use `transport` (not `type`) for Rovo Dev CLI |
| Atlassian OAuth prompt | Pieces doesn't require Atlassian OAuth; this is for the Atlassian Rovo MCP Server, not Pieces |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Back to All Agent Setup Guides</a>&nbsp;&nbsp;</td>
</tr></table>
