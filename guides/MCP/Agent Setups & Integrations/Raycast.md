# Connecting Pieces MCP to Raycast

**Tool type:** macOS productivity launcher
**Website:** [raycast.com](https://raycast.com)
**Transport support:** stdio only

> Raycast does not natively support HTTP-based MCP servers. You need a **stdio-to-HTTP bridge** (like `mcp-remote`) to connect to PiecesOS. See the [mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) for full documentation, or the [stdio-to-HTTP Bridges section](./README.md#stdio-to-http-bridges) for a quick comparison of bridge options.

---

## Config File Location

| Platform | Path |
|----------|------|
| **macOS** | In the Raycast Extension support directory — open via **Manage MCP Servers > Show Config File in Finder** |

The file is named `mcp-config.json`. To find it:

1. Open Raycast (Cmd+Space or your hotkey)
2. Search for **"Manage MCP Servers"**
3. Press **Cmd+K** → **"Show Config File in Finder"**

---

## JSON Format

Raycast uses `mcpServers` as the root key. All servers must use `type: "stdio"`.

---

## Setup with mcp-remote Bridge

> See the [mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) for full documentation, all CLI flags, OAuth setup, and alternative bridge tools. Quick reference also at [stdio-to-HTTP Bridges](./README.md#stdio-to-http-bridges).

### 1. Ensure Node.js is installed

```bash
node --version   # should print v18 or later
```

### 2. Add to `mcp-config.json` (same machine as PiecesOS — recommended)

> **Recommended when PiecesOS and Raycast are on the same Mac.**

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

### 3. Remote Setup (ngrok)

> Use this to access PiecesOS running on a **different machine**. For ngrok setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

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

## Adding via Raycast UI

1. Open Raycast and search **"Install Server"**
2. Fill in the form:
   - **Name:** pieces
   - **Type:** stdio
   - **Command:** npx
   - **Args:** `-y mcp-remote http://localhost:39300/model_context_protocol/2024-11-05/sse`

---

## Using Pieces in Raycast

After setup, use `@pieces` in Raycast AI (Quick AI, AI Chat, or Presets) to invoke Pieces tools. Raycast automatically shows AI all available servers.

---

## Updating

Edit `mcp-config.json` (found via "Show Config File in Finder"), update the URL in `args`, and restart Raycast AI.

---

## Verification

1. Open Raycast AI Chat
2. Type `@pieces` to mention the server
3. Ask: "What tools do you have from Pieces?"

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `npx: command not found` | Install Node.js; ensure it's in your PATH (`/usr/local/bin` or `/opt/homebrew/bin` on macOS) |
| Bridge not connecting | Verify PiecesOS is running and the SSE endpoint responds: `curl http://localhost:39300/.well-known/version` |
| Config file location | Use Raycast's "Manage MCP Servers > Show Config File in Finder" to locate the exact path |
| macOS only | Raycast is currently macOS-only |

---

## Related Guides

- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access
- [Bridging Local MCP Clients with mcp-remote](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) — Connect stdio-only clients to the Pieces HTTP endpoint

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Back to All Agent Setup Guides</a>&nbsp;&nbsp;</td>
</tr></table>
