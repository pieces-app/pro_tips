# Connecting Pieces MCP to Amazon Q Developer

**Tool type:** AI assistant (CLI and IDE plugin)
**Website:** [aws.amazon.com/q/developer](https://aws.amazon.com/q/developer)
**Transport support:** stdio, Streamable HTTP

---

## Config File Location

| Interface | Current path | Legacy path (still supported) |
|-----------|-------------|-------------------------------|
| **IDE (global)** | `~/.aws/amazonq/default.json` | `~/.aws/amazonq/mcp.json` |
| **IDE (workspace)** | `.amazonq/default.json` at project root | `.amazonq/mcp.json` |
| **CLI** | `~/.aws/amazonq/cli-agents/` (directory) | — |

> Workspace settings take precedence over global settings.

---

## IDE Plugin Setup (Local)

> **Recommended when PiecesOS and Amazon Q are on the same machine.**

Edit `~/.aws/amazonq/default.json`:

```json
{
  "servers": {
    "pieces": {
      "type": "http",
      "url": "http://localhost:39300/model_context_protocol/2025-03-26/mcp",
      "timeout": 60
    }
  }
}
```

---

## IDE Plugin Setup (Remote / ngrok)

> Use this when Amazon Q is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```json
{
  "servers": {
    "pieces": {
      "type": "http",
      "url": "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp",
      "timeout": 60
    }
  }
}
```

---

## CLI Setup

Configure a remote MCP server in the CLI using:

```bash
q mcp add --name pieces --type http --url http://localhost:39300/model_context_protocol/2025-03-26/mcp
```

---

## Tool Permissions

Amazon Q allows per-tool permission levels. You can configure these in the IDE settings UI after adding the server:

- **Ask** — prompts before each use
- **Always allow** — runs without prompting
- **Deny** — blocked entirely

---

## Updating

Edit `~/.aws/amazonq/default.json`, update the `url`, and restart Amazon Q or start a new session.

---

## Verification

1. Start Amazon Q (CLI or IDE)
2. MCP servers load in the background; tools become available progressively
3. Ask Q: "What Pieces tools are available?"

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Config directory doesn't exist | Create `~/.aws/amazonq/` manually |
| Legacy vs current config | Both `default.json` and `mcp.json` are supported; `default.json` takes precedence |
| MCP not loading | Ensure you have a recent version of Amazon Q Developer |
| OAuth prompt | Pieces doesn't require OAuth; use no-auth configuration |

---

## Related Guides

- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Back to All Agent Setup Guides</a>&nbsp;&nbsp;</td>
</tr></table>
