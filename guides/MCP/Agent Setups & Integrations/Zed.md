# Connecting Pieces MCP to Zed

**Tool type:** Code editor (desktop)
**Website:** [zed.dev](https://zed.dev)
**Transport support:** stdio only

> **HTTP not yet supported natively.** Zed uses a custom `context_servers` key and currently does not support remote HTTP/SSE MCP servers. A stdio-to-HTTP bridge is required to connect to PiecesOS. See the [mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) for full documentation.

---

## Config File Location

| Scope | Path |
|-------|------|
| **User settings** | `~/.config/zed/settings.json` (Linux/macOS) or `$XDG_CONFIG_HOME/zed/settings.json` |
| **Project settings** | `.zed/settings.json` in your project root |

> **Key name:** Zed uses `context_servers` (not `mcpServers` or `servers`).

---

## Setup with mcp-remote Bridge

> A stdio-to-HTTP bridge is required because Zed does not support HTTP MCP servers natively. See the [mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) for full documentation, or the [stdio-to-HTTP Bridges section](./README.md#stdio-to-http-bridges) for a quick comparison of bridge options.

### 1. Install the bridge

See the [mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) for full installation options, CLI flags, and OAuth documentation.

```bash
npm install -g mcp-remote
# or use directly via npx (no global install needed)
```

### 2. Edit your Zed settings (same machine as PiecesOS — recommended)

> **Recommended when PiecesOS and Zed are on the same machine.** Use the localhost SSE URL.

Add to `~/.config/zed/settings.json`:

```json
{
  "context_servers": {
    "pieces": {
      "command": {
        "path": "npx",
        "args": [
          "-y",
          "mcp-remote",
          "http://localhost:39300/model_context_protocol/2024-11-05/sse"
        ],
        "env": {}
      },
      "settings": {}
    }
  }
}
```

### 3. Remote Setup (ngrok)

> Use this when Zed is running on a **different machine** from PiecesOS. For ngrok setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```json
{
  "context_servers": {
    "pieces": {
      "command": {
        "path": "npx",
        "args": [
          "-y",
          "mcp-remote",
          "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2024-11-05/sse"
        ],
        "env": {}
      },
      "settings": {}
    }
  }
}
```

---

## Alternative: supergateway Bridge

```json
{
  "context_servers": {
    "pieces": {
      "command": {
        "path": "npx",
        "args": [
          "-y",
          "supergateway",
          "--sse",
          "http://localhost:39300/model_context_protocol/2024-11-05/sse"
        ],
        "env": {}
      },
      "settings": {}
    }
  }
}
```

---

## Updating

Edit your `settings.json`, update the URL in the `args` array, and save. Zed reloads context servers on config change.

---

## Verification

1. Open Zed's AI assistant panel
2. Ask: "What context tools do you have?"
3. Pieces LTM tools should be available

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `npx: command not found` | Install Node.js; ensure `npx` is in your PATH |
| Wrong config key | Use `context_servers` (not `mcpServers` or `servers`) |
| Bridge process crashes | Check that PiecesOS is running and the SSE endpoint responds |
| No tools visible | Restart Zed; working directory must allow finding `npx` |
| HTTP support | Track progress at [github.com/zed-industries/zed/discussions/29370](https://github.com/zed-industries/zed/discussions/29370) |

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
