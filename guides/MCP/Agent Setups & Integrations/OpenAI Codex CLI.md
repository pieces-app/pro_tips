# Connecting Pieces MCP to OpenAI Codex CLI

**Tool type:** CLI agent
**Website:** [openai.com/codex](https://openai.com/codex)
**Transport support:** stdio, Streamable HTTP
**Minimum version:** 0.2.0+

---

## Config File Location

| Platform | Path |
|----------|------|
| **User (global)** | `~/.codex/config.toml` |
| **Project** | `.codex/config.toml` at project root (must be a trusted project) |

> **File format:** TOML (not JSON). This is a common source of confusion.

---

## Local Setup (Streamable HTTP)

> **Recommended when PiecesOS and Codex CLI are on the same machine.**

Edit `~/.codex/config.toml`:

```toml
[mcp_servers.pieces]
url = "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
startup_timeout_sec = 10
tool_timeout_sec = 60
```

---

## Remote Setup (ngrok)

> Use this when Codex CLI is running on a **different machine** or in a cloud environment. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```toml
[mcp_servers.pieces]
url = "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp"
startup_timeout_sec = 10
tool_timeout_sec = 60
```

---

## With HTTP Headers (if authentication needed)

```toml
[mcp_servers.pieces]
url = "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp"
bearer_token_env_var = "PIECES_TOKEN"
startup_timeout_sec = 10
tool_timeout_sec = 60
```

Set the environment variable before running Codex:
```bash
export PIECES_TOKEN=your-token
```

---

## Filtering Tools (Optional)

To only expose specific Pieces tools:

```toml
[mcp_servers.pieces]
url = "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
enabled_tools = ["ask_pieces_ltm", "workstream_summaries_full_text_search"]
```

---

## Updating

Edit `~/.codex/config.toml`, update the `url`, and run a new Codex session.

---

## Verification

1. Start a Codex session: `codex`
2. Codex announces available MCP tools on startup
3. Ask: "What Pieces tools are available?"

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP not recognized | Update Codex CLI to 0.2.0 or later |
| Config file not found | Create `~/.codex/config.toml` manually (TOML, not JSON) |
| Server not connecting | Verify PiecesOS is running and URL responds |
| Timeout errors | Increase `startup_timeout_sec` or `tool_timeout_sec` |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

[← Back to All Agent Setup Guides](./README.md)
