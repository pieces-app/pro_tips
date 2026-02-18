# Connecting Pieces MCP to JetBrains IDEs

**Tool type:** IDE family (IntelliJ IDEA, PyCharm, WebStorm, GoLand, etc.)
**Website:** [jetbrains.com](https://www.jetbrains.com)
**Transport support:** stdio, Streamable HTTP (SSE is limited/deprecated)
**Minimum version:** 2025.2+

---

## Setup via Settings UI

1. Open your JetBrains IDE
2. Go to **Settings** (Cmd+, on macOS, Ctrl+Alt+S on Windows/Linux)
3. Navigate to **Tools > AI Assistant > Model Context Protocol (MCP)**
4. Click **"+"** (Add) to create a new server
5. In the **New MCP Server** dialog, enter:

### For Streamable HTTP (recommended)

> **Recommended when PiecesOS and your JetBrains IDE are on the same machine.**

```json
{
  "mcpServers": {
    "pieces": {
      "url": "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

### For a stdio server

```json
{
  "mcpServers": {
    "pieces": {
      "command": "npx",
      "args": ["-y", "some-package"]
    }
  }
}
```

6. Optionally set a **working directory**
7. Click **OK** and apply

---

## Remote Setup (ngrok)

> Use this when your JetBrains IDE is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

In the same dialog, enter:

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

## Updating

Go back to **Settings > Tools > AI Assistant > MCP**, select the "pieces" server, click **Edit**, update the URL, and apply.

---

## Brave Mode (Auto-Execute Tools)

By default, JetBrains prompts for confirmation before executing tools. To enable auto-execution:

**Settings > Tools > AI Assistant > MCP > Brave Mode = enabled**

Use with caution in production environments.

---

## Verification

1. Open the **AI Assistant** panel
2. Check that Pieces tools appear in the available tools list
3. Ask the AI Assistant to query your Pieces Long-Term Memory

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP option not visible in Settings | Update to JetBrains 2025.2 or later |
| Only STDIO working, not HTTP | JetBrains AI Assistant currently supports local servers best; verify 2025.2+ installed |
| SSE not connecting | JetBrains has limited/deprecated SSE; use Streamable HTTP endpoint |
| AI not using tools automatically | Enable "Brave Mode" in MCP settings |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Back to All Agent Setup Guides</a>&nbsp;&nbsp;</td>
<td>&nbsp;&nbsp;</td>
</tr></table>
