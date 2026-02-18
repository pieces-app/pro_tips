# Connecting Pieces MCP to VS Code

**Tool type:** Code editor (desktop)
**Website:** [code.visualstudio.com](https://code.visualstudio.com)
**Transport support:** stdio, SSE (legacy), Streamable HTTP

---

## Config File Location

| Scope | Path |
|-------|------|
| **Workspace** | `.vscode/mcp.json` in your project root |
| **User (global)** | Via Settings > search "MCP Servers" |

---

## JSON Format

VS Code uses a **`servers`** root key (not `mcpServers`). The transport type is set with a **`type`** field.

### Local Setup (Streamable HTTP — recommended)

> **Recommended when PiecesOS and VS Code are on the same machine.**

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

### Local Setup (SSE — legacy)

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

### Local Setup (stdio)

```json
{
  "servers": {
    "pieces": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "some-mcp-package"],
      "env": {}
    }
  }
}
```

---

## Remote Setup (ngrok)

> Use this when VS Code is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

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

## Adding via Command Palette

1. Open Command Palette (**Cmd+Shift+P** / **Ctrl+Shift+P**)
2. Search for **"MCP: Add Server"**
3. Select **HTTP** or **SSE** as the transport type
4. Enter the Pieces MCP URL
5. Name it "pieces"

---

## Updating

To update the URL: edit `.vscode/mcp.json` and save. VS Code picks up changes without a restart.

To update via Command Palette: **"MCP: Edit Server"** > select "pieces" > update the URL.

---

## Verification

1. Open Command Palette and run **"MCP: List Servers"**
2. Confirm "pieces" shows as connected
3. Open GitHub Copilot Chat and ask about available MCP tools

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Server not connecting | Check that PiecesOS is running and the port is correct |
| `type` field not recognized | Update VS Code to latest; MCP support requires recent versions |
| Tools not visible in Copilot | Ensure the GitHub Copilot Chat extension is installed and active |
| Config at wrong location | The file must be `.vscode/mcp.json` (not `.cursor/mcp.json` or `mcp.json` at root) |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access
