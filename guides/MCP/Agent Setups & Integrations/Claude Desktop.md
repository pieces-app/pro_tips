# Connecting Pieces MCP to Claude Desktop

**Tool type:** Desktop application
**Website:** [claude.ai/download](https://claude.ai/download)
**Transport support:** stdio (JSON config), Streamable HTTP + SSE (via Connectors UI, Pro/Max/Team/Enterprise only)

---

## Config File Location

| Platform | Path |
|----------|------|
| **macOS** | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Windows** | `%APPDATA%\Claude\claude_desktop_config.json` |
| **Linux** | `~/.config/Claude/claude_desktop_config.json` |

> **macOS tip:** The Library folder is hidden by default. Press **Cmd+Shift+.** in Finder to reveal it, or run `open ~/Library/Application\ Support/Claude/` in Terminal.
>
> **Windows tip:** Press **Win+R**, type `%APPDATA%\Claude`, press Enter.

---

## Option 1 — Local Setup via stdio Bridge (all plans)

> **Recommended when Claude Desktop and PiecesOS are on the same machine.** The `localhost` URL is direct and fastest.

Claude Desktop's JSON config **only supports stdio transport**. Since PiecesOS is an HTTP server, you need a bridge process. Use `mcp-remote` — see the [mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) or the [stdio-to-HTTP Bridges section](./README.md#stdio-to-http-bridges) for full documentation.

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

This spawns a local Node.js process that proxies stdio calls to the Pieces SSE endpoint.

> **Prerequisite:** Node.js must be installed and `npx` must be on your PATH.

Port note: If PiecesOS is not on 39300, probe `http://localhost:PORT/.well-known/version` for ports 39300-39333.

---

## Option 2 — Remote Setup via Connectors UI (Pro/Max/Team/Enterprise)

> Use this when Claude Desktop needs to reach PiecesOS on a **different machine** over the internet.
>
> To get your ngrok HTTPS URL, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

For HTTPS remote servers (e.g., ngrok), Claude Desktop uses **Settings > Connectors**:

1. Open Claude Desktop
2. Go to **Settings** (gear icon)
3. Click **Connectors**
4. Click **Add custom connector**
5. Enter your ngrok URL:
   ```
   https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp
   ```
6. Save and restart Claude Desktop

> Remote MCP connectors are available on **Pro, Max, Team, and Enterprise** plans only.
>
> Anthropic has noted that SSE transport may be deprecated in favour of Streamable HTTP in future updates.

---

## Option 3 — Remote via stdio Bridge (all plans, no Connectors UI required)

> Also uses ngrok. See: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) to get your HTTPS URL. See the [mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) or [stdio-to-HTTP Bridges section](./README.md#stdio-to-http-bridges) for mcp-remote documentation.

If you want remote access without needing a Pro/higher plan, use the bridge with your ngrok URL:

```json
{
  "mcpServers": {
    "pieces": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2024-11-05/sse"
      ]
    }
  }
}
```

---

## Verification

1. **Restart** Claude Desktop after editing config (it only reads config on startup)
2. Look for the **hammer icon** in the chat input area — this indicates MCP tools are available
3. Click it to see the Pieces tools listed
4. Ask Claude: "What Pieces tools are available?"

---

## Updating

- **To change the URL:** Edit the JSON config or update the Connectors entry in Settings, then restart Claude Desktop
- **After a [ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) tunnel restart:** Your ngrok URL changes each session; update the URL and restart

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Tools not appearing | Restart Claude Desktop; it only reads config on startup |
| `npx: command not found` | Install Node.js and ensure `npx` is in your PATH |
| Config file not found | Create the file (and parent directories) manually if they don't exist |
| Remote connector fails | Verify [ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) tunnel is running and URL is accessible in a browser |
| "Remote MCP requires Pro" | You need Pro/Max/Team/Enterprise for the Connectors UI; use Option 3 instead |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access
- [Bridging Local MCP Clients with mcp-remote](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) — Connect stdio-only clients to the Pieces HTTP endpoint

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Back to All Agent Setup Guides</a>&nbsp;&nbsp;</td>
</tr></table>
