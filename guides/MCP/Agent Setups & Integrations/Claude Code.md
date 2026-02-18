# Connecting Pieces MCP to Claude Code

**Tool type:** CLI tool and VS Code extension
**Website:** [code.claude.com](https://code.claude.com)
**Transport support:** stdio, SSE, Streamable HTTP

---

## Config Storage

| Scope | Location |
|-------|----------|
| **User (default)** | `~/.claude.json` |
| **Project** | `.mcp.json` at project root (commit to version control for team sharing) |

---

## Adding via CLI

### Local (Streamable HTTP)

> **Recommended when PiecesOS and Claude Code are on the same machine.**

```bash
claude mcp add --transport http pieces http://localhost:39300/model_context_protocol/2025-03-26/mcp
```

### Local (SSE)

```bash
claude mcp add --transport sse pieces http://localhost:39300/model_context_protocol/2024-11-05/sse
```

### Remote (ngrok)

> Use this when Claude Code is running on a **different machine** or cloud environment. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```bash
claude mcp add --transport http pieces https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp
```

### With authentication header (if needed)

```bash
claude mcp add --transport http pieces https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp \
  --header "Authorization: Bearer your-token"
```

---

## Managing Servers

```bash
# List all configured servers
claude mcp list

# Remove a server
claude mcp remove pieces

# Show server details
claude mcp get pieces
```

---

## Scope Options

By default, servers are added with **user scope** (available across all projects). To scope to a project:

```bash
claude mcp add --transport http --scope project pieces http://localhost:39300/model_context_protocol/2025-03-26/mcp
```

Project-scoped servers are stored in `.mcp.json` at the project root and can be committed to version control.

---

## VS Code Extension

The Claude Code VS Code extension shares MCP configuration with the CLI. Servers added via `claude mcp add` are automatically available in the extension — no additional setup needed.

---

## Verification

1. Run `claude mcp list` and confirm "pieces" appears
2. Start a Claude Code session: `claude`
3. Ask: "What MCP tools do you have from Pieces?"
4. Pieces LTM tools should be listed

---

## Updating

```bash
# Remove and re-add with new URL
claude mcp remove pieces
claude mcp add --transport http pieces https://NEW_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Server not in list after `add` | Check the URL is reachable: `curl http://localhost:39300/.well-known/version` |
| Transport error | Try switching between `--transport http` and `--transport sse` |
| Config stored in wrong location | User scope: `~/.claude.json`; project scope: `.mcp.json` (not `~/.claude/settings.json`) |
| VS Code extension not seeing tools | Restart VS Code after adding via CLI |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Back to All Agent Setup Guides</a>&nbsp;&nbsp;</td>
</tr></table>
