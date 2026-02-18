# Connecting Pieces MCP to Goose

**Tool type:** Open-source AI agent framework (CLI and desktop)
**Website:** [block.github.io/goose](https://block.github.io/goose)
**Transport support:** stdio, SSE, Streamable HTTP

---

## Config File Location

| Platform | Path |
|----------|------|
| **macOS / Linux** | `~/.config/goose/config.yaml` |
| **Windows** | `%APPDATA%\Block\goose\config\config.yaml` |

---

## YAML Config Format

Goose uses **YAML** (not JSON) with an `extensions` top-level key. Environment variables use `${VAR_NAME}` syntax (no `env:` prefix).

### Local Setup (SSE)

> **Recommended when PiecesOS and Goose are on the same machine.**

```yaml
extensions:
  pieces:
    name: Pieces LTM
    type: sse
    url: http://localhost:39300/model_context_protocol/2024-11-05/sse
    enabled: true
    timeout: 30
```

### Local Setup (Streamable HTTP — recommended)

```yaml
extensions:
  pieces:
    name: Pieces LTM
    type: streamable_http
    url: http://localhost:39300/model_context_protocol/2025-03-26/mcp
    enabled: true
    timeout: 30
```

### Remote Setup (ngrok)

> Use this when Goose is running on a **different machine** from PiecesOS. For setup, see: [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md).

```yaml
extensions:
  pieces:
    name: Pieces LTM
    type: streamable_http
    url: https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2025-03-26/mcp
    enabled: true
    timeout: 30
```

---

## Adding via Interactive Wizard

```bash
goose configure
```

1. Select **"Add Extension"**
2. Choose **SSE** or **Streamable HTTP** as the provider type
3. Enter your Pieces URL
4. Name it "Pieces LTM"

---

## Adding via Deep Link (One-Click)

Open this in a browser to install directly in Goose (update the URL first):

```
goose://extension/add?name=pieces&type=sse&url=http%3A%2F%2Flocalhost%3A39300%2Fmodel_context_protocol%2F2024-11-05%2Fsse
```

---

## Temporary Session Extension

To add Pieces for just one session without saving to config:

```bash
goose session --with-remote-extension "http://localhost:39300/model_context_protocol/2024-11-05/sse"
```

---

## Updating

Edit `~/.config/goose/config.yaml`, update the `url`, and start a new Goose session.

---

## Verification

1. Run `goose session` to start a new session
2. Ask: "What tools do you have from Pieces?"
3. Pieces LTM tools should be listed

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Extension not loading | Run `goose configure` and verify the URL |
| YAML parse error | Ensure consistent indentation; YAML is whitespace-sensitive |
| Connection timeout | Ensure PiecesOS is running; check port 39300-39333 |
| Tools not available | Restart the Goose session after editing config |

---

## Related Guides

- [All Agent Setup Guides](./README.md) — Transport matrix and setup guides for 19 MCP-compatible tools
- [Pieces MCP and LTM Tools Reference](../Pieces%20MCP%20and%20LTM%20Tools%20Reference.md) — Complete reference for all 39 tools available to your agents
- [Connecting to PiecesOS via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local Pieces server for remote access
