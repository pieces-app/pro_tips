# Connecting Pieces MCP to Continue.dev

**Tool type:** Open-source coding assistant (VS Code / JetBrains extension)
**Website:** [continue.dev](https://continue.dev)
**Transport support:** stdio, SSE, Streamable HTTP

> **Agent mode required:** MCP servers in Continue.dev only work in **agent mode**. They are not available in regular chat or plan modes.

---

## Config File Location

| Scope | Path |
|-------|------|
| **Workspace** | `.continue/config.yaml` at project root (recommended — commit to version control) |
| **Alternative JSON** | `.continue/mcpServers/mcp.json` |

---

## YAML Config Format

Continue.dev uses **YAML** with an `mcpServers` array.

### Local Setup (Streamable HTTP — recommended)

> **Recommended when PiecesOS and Continue.dev are on the same machine.**

```yaml
mcpServers:
  - name: Pieces LTM
    type: streamable-http
    url: http://localhost:39300/model_context_protocol/2025-03-26/mcp
```

### Local Setup (SSE)

```yaml
mcpServers:
  - name: Pieces LTM
    type: sse
    url: http://localhost:39300/model_context_protocol/2024-11-05/sse
```

### Remote Setup (ngrok)

> Use this when Continue.dev is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```yaml
mcpServers:
  - name: Pieces LTM
    type: streamable-http
    url: https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp
```

---

## JSON Config Format (Alternative)

If you prefer JSON, create `.continue/mcpServers/mcp.json`:

```json
{
  "mcpServers": [
    {
      "name": "Pieces LTM",
      "type": "streamable-http",
      "url": "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
    }
  ]
}
```

---

## Updating

Edit your `config.yaml` (or JSON file), update the `url`, and switch to agent mode. Continue picks up the change on the next agent session.

---

## Verification

1. Switch Continue.dev to **agent mode** in the UI
2. Check the available tools — Pieces LTM tools should appear
3. Ask the agent to search your Long-Term Memory

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Tools not appearing | Ensure you are in **agent mode**, not regular chat |
| YAML parse error | Check indentation; YAML is whitespace-sensitive |
| Server not connecting | Check PiecesOS port (39300-39333) and URL |
| Type value wrong | Use `streamable-http` (with hyphen), not `streamableHttp` or `http` |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access
