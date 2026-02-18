# Connecting Pieces MCP to Cline

**Tool type:** VS Code extension (AI coding agent)
**Website:** [cline.bot](https://cline.bot)
**Transport support:** stdio, SSE

> **Note on Streamable HTTP:** Cline has known compatibility issues with Streamable HTTP transport (it sends GET instead of POST to initiate the session). Use the **SSE endpoint** for the most reliable connection.

---

## Config File Location

| Platform | Path |
|----------|------|
| **All platforms** | `~/.cline/data/settings/cline_mcp_settings.json` |

Cline maintains its own config file and does **not** read from `.vscode/mcp.json`.

---

## Setup via Extension UI

1. Open VS Code
2. Click the **Cline** icon in the activity bar
3. Click the **gear icon** or navigate to **MCP Servers** in the Cline panel
4. Click **"Add Server"**
5. Select **SSE** as the transport type
6. Enter the Pieces URL: `http://localhost:39300/model_context_protocol/2024-11-05/sse`
7. Name it "pieces"

---

## Manual JSON Config

Edit `~/.cline/data/settings/cline_mcp_settings.json`:

### Local Setup (SSE — recommended)

> **Recommended when PiecesOS and Cline are on the same machine.**

```json
{
  "mcpServers": {
    "pieces": {
      "url": "http://localhost:39300/model_context_protocol/2024-11-05/sse",
      "type": "sse",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

---

## Remote Setup (ngrok)

> Use this when Cline/VS Code is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```json
{
  "mcpServers": {
    "pieces": {
      "url": "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2024-11-05/sse",
      "type": "sse",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

---

## Auto-Approve Specific Tools

To skip confirmation prompts for specific Pieces tools:

```json
{
  "mcpServers": {
    "pieces": {
      "url": "http://localhost:39300/model_context_protocol/2024-11-05/sse",
      "type": "sse",
      "autoApprove": ["ask_pieces_ltm", "workstream_summaries_full_text_search"]
    }
  }
}
```

---

## Updating

Edit the config JSON and save. Cline reloads the server list from disk without requiring a VS Code restart.

---

## Verification

1. Open the Cline panel in VS Code
2. Check the **MCP** section for "pieces" with a connected status
3. Ask Cline to search your LTM

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Cline not seeing config | Cline reads from its own file, not `.vscode/mcp.json` |
| Streamable HTTP fails | Use the SSE endpoint (`/model_context_protocol/2024-11-05/sse`) — Cline has HTTP compatibility issues |
| Server shows disconnected | Restart VS Code |
| Tools not available in agent mode | Ensure Cline is in agent mode, not regular chat mode |
