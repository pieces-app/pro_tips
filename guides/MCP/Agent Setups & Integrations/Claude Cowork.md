# Connecting Pieces MCP to Claude Cowork

**Tool type:** Desktop task automation agent (macOS and Windows)
**Website:** [claude.ai](https://claude.ai)
**Plans required:** Pro, Max, Team, Enterprise
**Transport support:** Streamable HTTP, SSE (via Connectors or Claude Desktop config)
**Status:** Research preview (launched January 2026, Windows added February 2026)

---

## What is Claude Cowork?

Claude Cowork is Anthropic's **general-purpose task automation agent**, built on top of Claude Code and accessible through Claude Desktop. It extends Claude Desktop's capabilities beyond conversation to autonomous multi-step task execution:

- Reads, writes, and organizes files within a designated folder
- Executes tasks in parallel via sub-agents
- Works across your filesystem without requiring terminal commands
- Designed for non-technical users as well as developers

Cowork differs from Claude Code (developer-focused CLI) and regular Claude chat by enabling **autonomous, agentic task execution** with file access. With Pieces MCP connected, Cowork can use your Long-Term Memory as context while executing multi-step tasks.

---

## Prerequisites

- Claude Desktop installed (Cowork runs inside it)
- Pro, Max, Team, or Enterprise subscription
- macOS or Windows
- PiecesOS running

---

## Connecting Pieces MCP to Cowork

Cowork uses the same MCP configuration as Claude Desktop. You have two options:

### Option 1 — Via Connectors UI (Pro/Max/Team/Enterprise, for remote URLs)

> For this you need a public HTTPS URL. See: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

1. Open Claude Desktop
2. Go to **Settings > Connectors**
3. Click **Add custom connector**
4. Enter your ngrok URL:
   ```
   https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp
   ```
5. Save and restart Claude Desktop

### Option 2 — Via JSON Config with stdio Bridge (all plans, recommended for local use)

> **Recommended when PiecesOS and Claude Desktop are on the same machine.** Uses the localhost URL directly. See the [mcp-remote guide](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) or [stdio-to-HTTP Bridges guide](./README.md#stdio-to-http-bridges) for documentation.

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

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

See the [Claude Desktop guide](./Claude%20Desktop.md) for full details.

---

## Using Pieces Tools in Cowork

Once connected, start a Cowork session and Pieces LTM tools are available alongside file system access. Example tasks you can give Cowork:

**Generate a standup from yesterday's work:**
> "Use my Pieces Long-Term Memory to find what I worked on yesterday and write a standup to `~/Desktop/standup.md`"

**Research recall + document:**
> "Search my Pieces memory for everything I've captured about the authentication redesign and create a summary document in my project folder"

**Meeting notes enrichment:**
> "Use my Pieces audio transcriptions from today's meetings and create a meeting notes file with key decisions and action items"

---

## Key Differences from Claude Chat

| Feature | Claude Chat | Claude Cowork |
|---------|------------|---------------|
| File access | No | Yes (designated folder) |
| Task parallelism | No | Yes (sub-agents) |
| Autonomous execution | No | Yes |
| MCP tools | Yes | Yes |
| Session continuity | Per-conversation | Per-task (no cross-session memory) |

---

## Limitations (Research Preview)

- Sessions don't sync across devices
- Cannot work across multiple directories simultaneously
- No session memory persistence between Cowork sessions
- Cannot share sessions with other users
- Incompatible with Claude Projects

---

## Updating

Update the [ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) URL in either Settings > Connectors or in `claude_desktop_config.json`, then restart Claude Desktop.

---

## Verification

1. Open Claude Desktop and start a Cowork session (look for the folder/file access UI)
2. Ask: "What Pieces tools are available?"
3. Give a multi-step task that requires LTM access:
   > "Search my Pieces memory for my recent work on [project name] and write a status update to my Desktop"

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Cowork option not visible | Ensure you have Pro/Max/Team/Enterprise plan |
| Pieces tools not appearing | Restart Claude Desktop after config changes |
| MCP tools unavailable in Cowork | Confirm the Pieces server is configured in Claude Desktop (Cowork shares Desktop's config) |
| Windows not available | Windows support was added February 10, 2026 — update Claude Desktop |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

[← Back to All Agent Setup Guides](./README.md)
