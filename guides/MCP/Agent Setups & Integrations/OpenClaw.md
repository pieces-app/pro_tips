# Connecting Pieces MCP to OpenClaw

**Tool type:** Open-source self-hosted AI agent (CLI / Node.js service)
**Also known as:** ClawdBot, Moltbot
**GitHub:** [github.com/clawdbot](https://github.com/clawdbot)
**Transport support:** stdio, SSE, Streamable HTTP (via MCPorter)

---

## What is OpenClaw?

OpenClaw (formerly ClawdBot, formerly Moltbot) is an open-source **continuous AI agent runtime** that runs as a persistent Node.js service on your local machine. Unlike chatbots that respond to one-off prompts, OpenClaw:

- Runs 24/7 in the background, executing tasks proactively via cron jobs and event listeners
- Connects to messaging platforms (WhatsApp, Telegram, Discord, Slack, iMessage) as interfaces
- Executes MCP tools via **MCPorter** — its built-in MCP management layer
- Maintains persistent memory and context across sessions

With Pieces MCP connected, OpenClaw gains access to your Long-Term Memory. It can autonomously query your past work, generate standups, monitor recent activity, and surface relevant context without you asking.

---

## Prerequisites

1. Node.js 18+ installed
2. OpenClaw cloned and configured: follow the [OpenClaw setup guide](https://github.com/clawdbot)
3. PiecesOS running locally (port 39300-39333)

---

## Config File Location

```
~/.openclaw/workspace/config/mcporter.json
```

---

## Adding Pieces via MCPorter

Edit `~/.openclaw/workspace/config/mcporter.json`:

### Local Setup (SSE — recommended when PiecesOS is on the same machine)

> **Recommended when OpenClaw and PiecesOS are running on the same machine.** The localhost URL is fastest and needs no extra setup. Uses `mcp-remote` as a stdio bridge — see the [mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) or [stdio-to-HTTP Bridges guide](./README.md#stdio-to-http-bridges) for documentation.

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

### Local Setup (if OpenClaw supports native HTTP)

```json
{
  "mcpServers": {
    "pieces": {
      "type": "sse",
      "url": "http://localhost:39300/model_context_protocol/2024-11-05/sse"
    }
  }
}
```

### Remote Setup (ngrok)

> Use this when OpenClaw needs to reach PiecesOS on a **different machine** (e.g., your main dev machine while OpenClaw runs on a server). For ngrok setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

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

## Example Use Cases

Once Pieces MCP is connected to OpenClaw, you can automate workflows like:

**Autonomous daily standup:**
> Schedule OpenClaw to run every morning, query yesterday's workstream summaries via `material_identifiers` + `workstream_summaries_batch_snapshot`, and post a formatted standup to your Slack or Teams channel.

**Meeting prep:**
> Before a calendar event, OpenClaw searches audio transcriptions and workstream summaries for context related to the meeting topic and drafts a brief for you.

**Automated debugging log:**
> When OpenClaw detects a production alert, it queries recent `workstream_events_full_text_search` for error-related clipboard content, screenshots, or transcriptions, and creates a `pieces_memory` entry with the incident context.

---

## Verification

1. Start OpenClaw
2. Ask via your connected messaging platform: "What Pieces tools do you have?"
3. Pieces LTM tools should be listed
4. Try: "What did I work on yesterday?" — OpenClaw will call `ask_pieces_ltm`

---

## Security Note

OpenClaw can run with `permissionMode: 'bypassPermissions'` to execute tools autonomously. When combined with Pieces MCP write tools (like `create_pieces_memory`), this is powerful but should be used carefully. Consider:

- Running OpenClaw in Docker with limited filesystem access
- Disabling write tools in MCPorter if running fully autonomously
- Monitoring execution logs

---

## Updating

Edit `~/.openclaw/workspace/config/mcporter.json`, update the URL, and restart OpenClaw.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCPorter config not found | Create `~/.openclaw/workspace/config/` directory manually |
| Bridge process not starting | Install Node.js; verify `npx` is in PATH |
| Tools not available | Restart OpenClaw after editing MCPorter config |
| [ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) URL expired | Restart the ngrok tunnel and update the URL in MCPorter config |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

[← Back to All Agent Setup Guides](./README.md)
