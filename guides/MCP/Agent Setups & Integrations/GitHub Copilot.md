# Connecting Pieces MCP to GitHub Copilot

**Tool type:** AI coding assistant (VS Code extension)
**Website:** [github.com/features/copilot](https://github.com/features/copilot)
**Transport support:** stdio, SSE, Streamable HTTP (via VS Code's MCP support)

---

## Setup

GitHub Copilot uses VS Code's built-in MCP server configuration. Create or edit `.vscode/mcp.json` in your project:

### Local Setup (recommended when PiecesOS is on the same machine)

```json
{
  "servers": {
    "pieces": {
      "type": "http",
      "url": "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

Or using SSE:

```json
{
  "servers": {
    "pieces": {
      "type": "sse",
      "url": "http://localhost:39300/model_context_protocol/2024-11-05/sse"
    }
  }
}
```

---

## Remote Setup (ngrok)

> Use this when VS Code / Copilot is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```json
{
  "servers": {
    "pieces": {
      "type": "http",
      "url": "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

---

## Verification

1. Open VS Code with the GitHub Copilot Chat extension active
2. Run **"MCP: List Servers"** from the Command Palette
3. Confirm "pieces" is connected
4. In Copilot Chat, ask about your work history

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP tools not available | Ensure GitHub Copilot Chat extension is up to date |
| Server not connecting | Check PiecesOS port; try both `http` and `sse` types |
| Agent mode needed | MCP tools may only be available in Copilot's agent mode, not inline suggestions |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access
