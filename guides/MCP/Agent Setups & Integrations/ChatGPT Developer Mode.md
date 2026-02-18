# Connecting Pieces MCP to ChatGPT Developer Mode

**Tool type:** Web application (browser)
**Website:** [chatgpt.com](https://chatgpt.com)
**Transport support:** SSE, Streamable HTTP (remote HTTPS only)
**Plans required:** Pro, Plus, Business, Enterprise, Education
**Status:** Beta

> ChatGPT Developer Mode requires a **remote HTTPS URL**. Localhost will not work. You must expose PiecesOS via ngrok or another HTTPS proxy first — see [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) for full setup instructions.

---

## Prerequisites

1. A supported ChatGPT plan (Pro, Plus, Business, Enterprise, or Education)
2. PiecesOS running locally
3. [ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) tunnel active and providing an HTTPS URL

---

## Setup Steps

1. Open [chatgpt.com](https://chatgpt.com) in your browser
2. Click your **profile icon** → **Settings**
3. Go to **Connectors** in the sidebar
4. Scroll to the bottom and click **Advanced Settings**
5. Toggle **Developer Mode (beta)** ON
6. Return to **Connectors**
7. Click **Create** (appears after enabling Developer Mode)
8. Fill in the **New Connector** dialog:
   - **Connector name:** `Pieces LTM`
   - **MCP Server URL:** `https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp`
   - **Description:** (optional) `Search and retrieve from Pieces Long-Term Memory`
9. Click **Create**

> The URL must point to the `/mcp` endpoint path. Subdirectory paths like `/functions/v1/mcp` do not work.

---

## Authentication

ChatGPT supports:
- **No authentication** — works with Pieces (recommended)
- **OAuth** — supported but not required for Pieces

Bearer token authentication is not fully supported in Developer Mode.

---

## Updating

To update the [ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) URL after a tunnel restart:

1. Go to **Settings > Connectors**
2. Find "Pieces LTM" and click **Edit**
3. Update the MCP Server URL
4. Save

---

## Verification

1. Start a new conversation in ChatGPT
2. Look for the **tools indicator** in the chat
3. Ask: "What tools do you have from Pieces?"
4. Try: "What did I work on yesterday?"

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Cannot use localhost URL | ChatGPT requires public HTTPS — use [ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) |
| Connector not connecting | Ensure [ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) tunnel is running and URL is accessible in a browser |
| "Authentication required" | Use no-auth mode; Pieces doesn't need OAuth |
| Tools not appearing | Refresh the page after adding the connector |
| Developer Mode not visible | Ensure you are on a supported plan (Pro/Plus/Business/Enterprise/Education) |
| Write actions need confirmation | By default, writes require manual approval in ChatGPT |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Back to All Agent Setup Guides</a>&nbsp;&nbsp;</td>
</tr></table>
