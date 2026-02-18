# Bridging Local MCP Clients to Remote Servers with mcp-remote

`mcp-remote` is a Node.js proxy that lets any stdio-only MCP client — Claude Desktop, Cursor, Windsurf, and others — connect to remote HTTP-based MCP servers. It is the standard solution for a problem that affects the entire MCP ecosystem: many clients were built to launch a local subprocess and talk over stdin/stdout, but the growing catalog of cloud-hosted MCP servers (GitHub, Linear, Notion, Cloudflare, Pieces) speak HTTP, not stdio. `mcp-remote` acts as the invisible bridge between the two worlds.

- **GitHub:** [github.com/geelen/mcp-remote](https://github.com/geelen/mcp-remote)
- **npm:** [npmjs.com/package/mcp-remote](https://www.npmjs.com/package/mcp-remote)
- **Current stable version (Feb 2026):** `0.1.38`
- **Security:** CVE-2025-6514 affects `0.0.5`–`0.1.15`; upgrade to `0.1.16+` immediately

---

## The Transport Gap — Why mcp-remote Exists

The Model Context Protocol defines two families of transport:

| Transport | Communication model | Direction | Typical use |
|-----------|--------------------|-----------|----|
| **stdio** | subprocess stdin/stdout | local only | Claude Desktop JSON config, Cursor `mcp.json`, any tool that spawns a process |
| **Streamable HTTP** (MCP 2025-03-26+) | HTTP POST + optional SSE upgrade on one endpoint | local or remote | modern cloud servers (GitHub, Notion, Cloudflare) |
| **HTTP + SSE** *(deprecated, MCP 2024-11-05)* | GET opens SSE stream; separate POST for client messages | local or remote | legacy servers still in production (PiecesOS SSE endpoint, Linear) |

The problem is a mismatch at the client level. Claude Desktop's `claude_desktop_config.json`, for example, **only launches stdio processes**. It has no built-in HTTP client for MCP. This means you cannot put a URL in that config file — the client does not know what to do with it.

`mcp-remote` solves this by appearing to be a stdio server to the client while internally speaking HTTP to the remote server:

```
Claude Desktop (stdio)  ─────►  mcp-remote (local process)  ─────►  remote MCP server (HTTPS)
        ▲                               |   ▲
        |                    Auth/OAuth/|   |
        └────── JSON-RPC over stdio ────┘   └── Token storage (~/.mcp-auth/)
```

From the client's perspective nothing has changed. From the remote server's perspective it is receiving standard HTTP requests.

---

## Client Compatibility Matrix

Before reaching for `mcp-remote`, confirm whether your client already speaks HTTP natively:

| Client | stdio | Streamable HTTP | SSE (legacy) | Needs mcp-remote? |
|--------|-------|----------------|--------------|-------------------|
| **Claude Desktop** (JSON config) | ✅ | ❌ | ❌ | **Yes** — JSON config only supports stdio |
| **Claude Desktop** (Connectors UI, Pro+) | — | ✅ | ✅ | No |
| **Claude Code** | ✅ | ✅ | ✅ | No — native `--transport http` |
| **Cursor** | ✅ | ✅ | ✅ | No — supports URL directly in `mcp.json` |
| **VS Code + Copilot** | ✅ | ✅ | ✅ (fallback) | No |
| **Windsurf (Cascade)** | ✅ | ✅ | ✅ | No — supports `serverUrl` field |
| **Goose** | ✅ | ✅ | ✅ | No — supports `type: streamable_http` |
| **JetBrains AI** | ✅ | ✅ | ✅ | No |
| **Raycast AI** | ✅ | ✅ | ✅ | No |
| **Zed** | ✅ | Partial | Partial | Sometimes |
| **Amazon Q Developer** | ✅ | ❌ | ❌ | **Yes** |
| **Continue.dev** | ✅ | ✅ | ✅ | No |
| **Cline** | ✅ | ✅ | ✅ | No |

> **Rule of thumb:** If your client's config takes only `"command"` and `"args"` (a subprocess invocation), you need `mcp-remote`. If it takes a `"url"` or `"serverUrl"` field, you can connect directly.

---

## When to Use mcp-remote

### Use mcp-remote when…

1. **Your client only supports stdio.** Claude Desktop's JSON config is the classic example. Any tool that spawns a subprocess but cannot issue HTTP requests directly.

2. **You need to inject custom auth headers.** The `--header` flag injects an `Authorization: Bearer …` (or any header) into every HTTP request — useful for API-key-protected servers that do not do OAuth.

3. **You want OAuth without modifying your client.** `mcp-remote` implements a complete OAuth 2.1 + PKCE flow with Dynamic Client Registration, token storage, and automatic refresh — all transparently.

4. **You are behind a corporate HTTP proxy.** The `--enable-proxy` flag makes `mcp-remote` respect `HTTP_PROXY` / `HTTPS_PROXY` / `NO_PROXY` environment variables, something many clients don't do.

5. **You want tool-level filtering.** The `--ignore-tool` flag lets you block specific tools from a remote server before they even reach your AI client.

6. **Bridging local dev + ngrok for remote clients.** Expose a local MCP server via ngrok, then use `mcp-remote` to connect other stdio clients to that ngrok URL — without the other clients needing HTTP support.

7. **Compatibility with PiecesOS.** PiecesOS exposes an SSE endpoint. For clients like Claude Desktop (JSON config), `mcp-remote` is the bridge.

### Skip mcp-remote when…

- Your client has a `"url"` or `"serverUrl"` field in its MCP config — use it directly.
- You are using Claude Desktop **Connectors** (Pro/Max/Team/Enterprise) — the Connectors UI handles HTTP natively.
- You are using Claude Code — use `claude mcp add --transport http <name> <url>`.

---

## Prerequisites

- **Node.js 18+** — `node --version` to verify
- `npx` — ships with Node.js; no separate install needed
- OR: global install via `npm install -g mcp-remote`

---

## Installation

### Option A — Use via npx (recommended for most users)

No installation required. `npx` downloads and caches the package on first use:

```bash
npx mcp-remote https://your-remote-server.com/sse
```

Force the latest version every time:

```bash
npx mcp-remote@latest https://your-remote-server.com/sse
```

Silence the "install?" prompt in scripted / CI environments:

```bash
npx -y mcp-remote https://your-remote-server.com/sse
```

### Option B — Global install

```bash
npm install -g mcp-remote
```

Then invoke directly:

```bash
mcp-remote https://your-remote-server.com/sse
```

> **npx vs global:** `npx` gives you always-current versions and no version drift across machines. Global install is slightly faster after the first run but requires manual `npm update -g mcp-remote` to stay current.

---

## Basic Usage

### Simplest case — no auth

```bash
npx mcp-remote https://example.com/mcp
```

### Bearer token auth

```bash
npx mcp-remote https://example.com/mcp \
  --header "Authorization: Bearer YOUR_TOKEN"
```

### Legacy SSE endpoint

```bash
npx mcp-remote https://example.com/sse \
  --transport sse-only
```

### Force modern Streamable HTTP only

```bash
npx mcp-remote https://example.com/mcp \
  --transport http-only
```

### Local dev with HTTP allowed

```bash
npx mcp-remote http://localhost:39300/model_context_protocol/2024-11-05/sse \
  --allow-http
```

### Debug mode

```bash
npx mcp-remote https://example.com/mcp --debug
```

Logs are written to `~/.mcp-auth/{server_hash}_debug.log`.

---

## Complete CLI Reference

```
npx mcp-remote <server-url> [port] [options]
```

| Flag | Default | Description |
|------|---------|-------------|
| `<server-url>` | *(required)* | Full HTTPS URL of the remote MCP server |
| `[port]` | `3334` | Local port for OAuth callback listener. Auto-selects a random port if unavailable. |
| `--transport <strategy>` | `http-first` | See transport strategies below |
| `--header "Key: Value"` | — | Add a custom HTTP header to every request. Repeatable. Supports `${ENV_VAR}` substitution. |
| `--host <hostname>` | `localhost` | Hostname registered as the OAuth redirect URI |
| `--auth-timeout <seconds>` | `30` | How long to wait for the user to complete OAuth browser flow |
| `--allow-http` | off | Permit plain HTTP (unencrypted) connections. Only use on trusted private networks. |
| `--enable-proxy` | off | Honor `HTTP_PROXY` / `HTTPS_PROXY` / `NO_PROXY` environment variables |
| `--debug` | off | Enable verbose logging to `~/.mcp-auth/{hash}_debug.log` |
| `--ignore-tool <pattern>` | — | Exclude tools matching a wildcard pattern from being surfaced. Repeatable. |
| `--static-oauth-client-info <json\|@file>` | — | Pre-registered OAuth client credentials (skip Dynamic Client Registration) |
| `--static-oauth-client-metadata <json\|@file>` | — | Custom OAuth client metadata (scopes, client name, etc.) |

### Transport strategies

| Strategy | Behavior |
|----------|----------|
| `http-first` | Tries Streamable HTTP (POST) first; falls back to SSE if server returns `404` |
| `sse-first` | Tries SSE (GET) first; falls back to Streamable HTTP if server returns `405` |
| `http-only` | Streamable HTTP exclusively; fails immediately if unsupported |
| `sse-only` | SSE exclusively; fails immediately if unsupported |

> Use `http-first` for new servers (default). Use `sse-only` for legacy servers like PiecesOS's `2024-11-05/sse` endpoint. Use `http-only` to enforce the modern protocol.

---

## How OAuth Authentication Works

`mcp-remote` implements the full **OAuth 2.1 + PKCE + Dynamic Client Registration** flow described in the MCP specification. Here is what happens on first connection to an OAuth-protected remote server:

1. **Initial request → 401 challenge.** `mcp-remote` connects to the remote server. The server responds with `401 Unauthorized` and a `WWW-Authenticate` header containing a `resource_metadata` pointer.

2. **Discover authorization server.** `mcp-remote` fetches the Protected Resource Metadata document (at `/.well-known/oauth-protected-resource`) to find which authorization server to use.

3. **Dynamic Client Registration.** If the server supports it, `mcp-remote` automatically registers itself with the authorization server — no manual app registration required. If registration is disabled, provide credentials via `--static-oauth-client-info`.

4. **Browser-based authorization.** `mcp-remote` opens the system browser to the authorization endpoint. The user logs in and grants permissions.

5. **Callback capture.** The authorization server redirects back to `http://localhost:3334/callback` (or your configured port). `mcp-remote` captures the authorization code.

6. **Token exchange.** `mcp-remote` exchanges the authorization code + PKCE verifier for an access token and refresh token at the token endpoint.

7. **Secure storage.** Tokens are written to `~/.mcp-auth/` (or `$MCP_REMOTE_CONFIG_DIR`), with file permissions scoped to your user. Each remote server gets its own token file.

8. **Automatic refresh.** On subsequent connections, `mcp-remote` loads the stored token. When the access token nears expiry, it refreshes using the stored refresh token — without any user action.

**One-time setup, persistent thereafter.** After the initial browser authorization, all subsequent invocations are silent.

---

## Token Storage and Reset

| Location | Purpose |
|----------|---------|
| `~/.mcp-auth/` | Default token storage directory |
| `$MCP_REMOTE_CONFIG_DIR` | Override the storage directory |
| `~/.mcp-auth/{hash}_debug.log` | Debug log (when `--debug` is active) |

To force re-authentication (clears all stored tokens):

```bash
rm -rf ~/.mcp-auth
```

---

## Client Configuration Examples

### Claude Desktop

**Config file locations:**

| Platform | Path |
|----------|------|
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

**OAuth-protected remote server (fully automatic):**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.githubcopilot.com/mcp"
      ]
    }
  }
}
```

**Bearer token authentication:**

```json
{
  "mcpServers": {
    "my-api-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.example.com/mcp",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer sk_your_token_here"
      }
    }
  }
}
```

> **Windows note:** Some versions of Claude Desktop on Windows mishandle spaces inside the `args` array during subprocess invocation. The workaround is to move the full `"Bearer <token>"` string into an `env` variable and reference it as `Authorization:${AUTH_HEADER}` (no space around the colon).

**PiecesOS local bridge:**

```json
{
  "mcpServers": {
    "pieces": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "http://localhost:39300/model_context_protocol/2024-11-05/sse",
        "--allow-http",
        "--transport",
        "sse-only"
      ]
    }
  }
}
```

**PiecesOS via ngrok (remote access on any Claude Desktop plan):**

```json
{
  "mcpServers": {
    "pieces-remote": {
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

**Corporate VPN / custom CA certificate:**

```json
{
  "mcpServers": {
    "internal-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.internal.company.com/mcp"
      ],
      "env": {
        "NODE_EXTRA_CA_CERTS": "/path/to/corporate-ca.pem"
      }
    }
  }
}
```

Restart Claude Desktop after any change to the config file — it only reads configuration at startup.

---

### Cursor

**Config file locations:**

| Scope | Path |
|-------|------|
| Global | `~/.cursor/mcp.json` |
| Project | `.cursor/mcp.json` (in repo root) |

Modern Cursor supports native HTTP — you can usually connect directly without `mcp-remote`:

```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp"
    }
  }
}
```

When you need `mcp-remote` in Cursor (e.g. header injection, tool filtering, or specific OAuth handling):

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.linear.app/sse",
        "--transport",
        "sse-only"
      ]
    }
  }
}
```

---

### Claude Code (CLI)

Claude Code supports HTTP natively — `mcp-remote` is not required. But you can still use it:

```bash
# Native HTTP (recommended)
claude mcp add --transport http github https://api.githubcopilot.com/mcp

# Via mcp-remote (if you need header injection or OAuth handling)
claude mcp add-json my-server '{
  "type": "stdio",
  "command": "npx",
  "args": [
    "mcp-remote@latest",
    "https://api.example.com/mcp",
    "--header",
    "Authorization: Bearer ${MY_TOKEN}"
  ]
}'
```

---

### Windsurf

**Config file:** `~/.codeium/windsurf/mcp_config.json`

Windsurf supports native HTTP via `serverUrl`. Use `mcp-remote` only when you need OAuth or header injection:

**Native HTTP (preferred):**

```json
{
  "mcpServers": {
    "github": {
      "serverUrl": "https://api.githubcopilot.com/mcp"
    }
  }
}
```

**Via mcp-remote with bearer token:**

```json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.example.com/mcp",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer your_token_here"
      }
    }
  }
}
```

---

### VS Code (GitHub Copilot)

VS Code MCP config goes in `.vscode/mcp.json` (workspace) or user settings:

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp"
    }
  }
}
```

Use `mcp-remote` in VS Code only if you are on an older version without native HTTP, or need specific OAuth handling:

```json
{
  "servers": {
    "my-server": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.example.com/mcp"
      ]
    }
  }
}
```

---

### Goose

Goose supports `streamable_http` natively. Use that when possible:

```yaml
extensions:
  github:
    enabled: true
    type: streamable_http
    name: github
    uri: https://api.githubcopilot.com/mcp
    headers: {}
    timeout: 300
```

Via `mcp-remote` in Goose (for OAuth or header injection):

```yaml
extensions:
  my-server:
    enabled: true
    type: stdio
    cmd: npx
    args:
      - "-y"
      - mcp-remote
      - https://api.example.com/mcp
      - "--header"
      - "Authorization:${AUTH_HEADER}"
    envs:
      AUTH_HEADER: "Bearer your_token"
    timeout: 300
```

---

### JetBrains IDEs

Use **Settings → Tools → AI Assistant → Model Context Protocol (MCP)** → **Add server**:

- **Type:** Command
- **Command:** `npx`
- **Arguments:** `-y mcp-remote https://api.example.com/mcp`

Or add to `~/.config/JetBrains/mcp.json`:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://api.example.com/mcp"]
    }
  }
}
```

---

### Amazon Q Developer

Amazon Q only supports stdio transport and requires `mcp-remote` to reach any remote server:

**In `~/.aws/amazonq/mcp.json`:**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.githubcopilot.com/mcp"
      ]
    }
  }
}
```

---

## Public Remote MCP Servers You Can Connect To

A growing catalog of cloud-hosted MCP servers is available without any self-hosting. Connect to them via `mcp-remote` (or natively in clients that support HTTP):

| Service | Remote URL | Auth |
|---------|-----------|------|
| **GitHub** | `https://api.githubcopilot.com/mcp` | OAuth |
| **Linear** | `https://mcp.linear.app/sse` | OAuth |
| **Notion** | `https://mcp.notion.com/mcp` | OAuth |
| **Sentry** | `https://mcp.sentry.dev/mcp` | OAuth |
| **PayPal** | `https://mcp.paypal.com/mcp` | OAuth |
| **Cloudflare Docs** | `https://docs.mcp.cloudflare.com/mcp` | OAuth |
| **Cloudflare Observability** | `https://observability.mcp.cloudflare.com/mcp` | OAuth |
| **Cloudflare Workers Bindings** | `https://bindings.mcp.cloudflare.com/mcp` | OAuth |
| **Cloudflare Radar** | `https://radar.mcp.cloudflare.com/mcp` | OAuth |
| **Cloudflare AI Gateway** | `https://ai-gateway.mcp.cloudflare.com/mcp` | OAuth |
| **Make.com** | `https://mcp.make.com/mcp` | OAuth |
| **Jina AI** | `https://mcp.jina.ai/sse` | API key via `--header` |
| **Semgrep** | `https://mcp.semgrep.ai/mcp` | OAuth |
| **Buildkite** | `https://mcp.buildkite.com/mcp` | OAuth |

---

## The ngrok + mcp-remote Pattern

`mcp-remote` and ngrok complement each other in two distinct scenarios.

### Scenario 1 — stdio client → remote ngrok-exposed server

You have a PiecesOS (or any local MCP server) running on one machine and want a stdio-only client on *another* machine (or a cloud agent) to reach it:

```
Cloud AI agent ──► ngrok public URL ──► your local MCP server
```

Use `mcp-remote` on the cloud side to bridge from HTTP back to whatever your local client expects. See the [Connecting to PiecesOS via Ngrok guide](./Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) for the full tunnel setup.

### Scenario 2 — local development server exposed for team testing

You are building a custom MCP server locally. You want teammates to test it without installing anything:

```bash
# Terminal 1: your MCP server on port 8080
node my-mcp-server.js

# Terminal 2: expose it
ngrok http 8080
# → https://abc123.ngrok.app

# Teammates configure mcp-remote to point at the ngrok URL
# npx mcp-remote https://abc123.ngrok.app/mcp
```

Each teammate adds this to their client config with no local installation of your server required.

### Combining both — ngrok auth + mcp-remote header injection

You can protect your ngrok-exposed server with an API key at the ngrok traffic policy level, then inject that key via `mcp-remote`'s `--header` flag on the client side:

```json
{
  "mcpServers": {
    "dev-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://abc123.ngrok.app/mcp",
        "--header",
        "X-Api-Key:${DEV_SERVER_KEY}"
      ],
      "env": {
        "DEV_SERVER_KEY": "your-ngrok-api-key"
      }
    }
  }
}
```

---

## mcp-remote with PiecesOS

PiecesOS uses the legacy SSE transport (`2024-11-05/sse`). Use `mcp-remote` as the bridge in stdio-only clients. Discover the active port first (39300–39333):

```bash
for p in $(seq 39300 39333); do
  if curl -s -o /dev/null -w "%{http_code}" --connect-timeout 1 \
    "http://localhost:$p/.well-known/version" 2>/dev/null | grep -q 200; then
    echo "PiecesOS on port $p"
    break
  fi
done
```

Then configure:

```json
{
  "mcpServers": {
    "pieces": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "http://localhost:39300/model_context_protocol/2024-11-05/sse",
        "--allow-http",
        "--transport",
        "sse-only"
      ]
    }
  }
}
```

For a **remote** PiecesOS instance (via ngrok — useful for cloud agents or non-local machines):

```json
{
  "mcpServers": {
    "pieces-remote": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://YOUR_NGROK_URL.ngrok.app/model_context_protocol/2024-11-05/sse",
        "--transport",
        "sse-only"
      ]
    }
  }
}
```

---

## Advanced Patterns

### Pre-registered OAuth client (skip Dynamic Client Registration)

For OAuth servers that require pre-registration:

```json
{
  "mcpServers": {
    "enterprise-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://sso.company.com/mcp",
        "--static-oauth-client-info",
        "@/Users/you/Library/Application Support/Claude/oauth_client.json"
      ]
    }
  }
}
```

Where `oauth_client.json` contains:

```json
{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret"
}
```

### Custom OAuth scopes

```json
{
  "mcpServers": {
    "scoped-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.example.com/mcp",
        "--static-oauth-client-metadata",
        "{\"scope\": \"read write admin\"}"
      ]
    }
  }
}
```

### Extended auth timeout for MFA / SSO

```json
{
  "mcpServers": {
    "sso-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://sso.company.com/mcp",
        "--auth-timeout",
        "120"
      ]
    }
  }
}
```

### Tool filtering — block dangerous tools from untrusted servers

```json
{
  "mcpServers": {
    "third-party-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.example.com/mcp",
        "--ignore-tool",
        "delete*",
        "--ignore-tool",
        "execute*",
        "--ignore-tool",
        "shell*"
      ]
    }
  }
}
```

Filtered tools are hidden from `tools/list` responses and cannot be invoked.

### Corporate proxy

```json
{
  "mcpServers": {
    "behind-proxy": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://remote.example.com/mcp",
        "--enable-proxy"
      ],
      "env": {
        "HTTPS_PROXY": "http://proxy.company.com:8080",
        "NO_PROXY": "localhost,127.0.0.1"
      }
    }
  }
}
```

### Multiple remote servers simultaneously

Each server entry runs a separate `mcp-remote` process with independent token storage:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://api.githubcopilot.com/mcp"]
    },
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/sse", "--transport", "sse-only"]
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.notion.com/mcp"]
    },
    "pieces": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://localhost:39300/model_context_protocol/2024-11-05/sse", "--allow-http", "--transport", "sse-only"]
    }
  }
}
```

---

## Security Considerations

### CVE-2025-6514 — Critical RCE (fixed in 0.1.16)

Versions `0.0.5` through `0.1.15` contain a critical remote code execution vulnerability (CVSS 9.6). A malicious or compromised MCP server could respond with a crafted OAuth `authorization_endpoint` URL containing shell metacharacters, causing `mcp-remote` to execute arbitrary commands on your machine when initiating the OAuth flow.

**Action required:**
- Check your version: `npx mcp-remote --version`
- If below `0.1.16`, update immediately
- Use `npx mcp-remote@latest` or `npm update -g mcp-remote`
- Only connect to remote servers you trust, over HTTPS

### General best practices

1. **Always use HTTPS.** Never use `--allow-http` over the public internet. Only use it on trusted, isolated private networks where traffic cannot be intercepted.

2. **Store credentials in `env`, not `args`.** Config files may be committed to version control or visible in process lists. Use the `"env"` block in your client config and reference with `${VAR_NAME}` in args.

3. **Rotate tokens.** Tokens stored in `~/.mcp-auth/` are long-lived. Rotate API keys and OAuth credentials on a regular schedule. If you suspect compromise, run `rm -rf ~/.mcp-auth` and re-authenticate.

4. **Audit remote server capabilities.** Use `--ignore-tool` to block tools you don't need, especially destructive ones (`delete*`, `execute*`, `shell*`).

5. **Pin your version in CI.** In automated environments, use `mcp-remote@0.1.38` (or whichever current version is patched) rather than `@latest`, to prevent unexpected behavior from version updates.

6. **Keep your Node.js updated.** `mcp-remote` requires Node.js 18+. Keep Node.js current for upstream security patches.

7. **Review token file permissions.** `~/.mcp-auth/` should be readable only by your user. Verify with `ls -la ~/.mcp-auth/`.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `npx: command not found` | Node.js not installed or not on PATH | Install Node.js 18+ from [nodejs.org](https://nodejs.org) |
| `Error: Cannot connect to remote server` | Server URL is wrong, server is down, or HTTPS cert invalid | Verify the URL with `curl`; check `--debug` logs |
| `Error: EACCES` on port 3334 | Port already in use | Specify an alternate port: `npx mcp-remote <url> 9696` |
| OAuth browser window does not open | Headless environment or browser misconfigured | Set the `BROWSER` environment variable; or use `--header` for API-key auth instead |
| OAuth times out | MFA/SSO is slow | Add `--auth-timeout 120` |
| `401 Unauthorized` after first auth | Token expired or revoked | Run `rm -rf ~/.mcp-auth` and re-authenticate |
| Tools not appearing in client | Client not restarted after config change | Fully quit and reopen Claude Desktop / Cursor |
| `404` on connection | Server uses SSE, not Streamable HTTP | Add `--transport sse-only` |
| `405` on connection | Server uses Streamable HTTP, not SSE | Use default `http-first` or `--transport http-only` |
| `Could not resolve host` | DNS issue or ngrok tunnel expired | Check tunnel is running; refresh ngrok URL |
| Config change not taking effect | Windows PATH or env issues | Specify full Node.js path; use `"env"` block for credentials |
| Spaces in `--header` args broken on Windows | Shell argument parsing bug in some clients | Move token to `env` var, use `Authorization:${HEADER}` (no space around `:`) |

### Clearing cached auth state

```bash
rm -rf ~/.mcp-auth
```

### Testing the connection manually

`mcp-remote` ships with a client mode for manual testing. This runs the full OAuth flow and lists available tools:

```bash
npx mcp-remote-client https://your-server.com/mcp
```

### Enabling debug logs

Add `--debug` to your args:

```json
"args": ["-y", "mcp-remote", "https://your-server.com/mcp", "--debug"]
```

Then inspect: `~/.mcp-auth/{hash}_debug.log`

---

## References

- [mcp-remote GitHub repository (geelen/mcp-remote)](https://github.com/geelen/mcp-remote)
- [mcp-remote on npm](https://www.npmjs.com/package/mcp-remote)
- [MCP Transport Specification (2025-03-26)](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports)
- [MCP Authorization Flow](https://modelcontextprotocol.io/docs/tutorials/security/authorization)
- [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
- [CVE-2025-6514 Analysis (JFrog)](https://jfrog.com/blog/2025-6514-critical-mcp-remote-rce-vulnerability/)
- [SSE vs Streamable HTTP — Deep Dive](https://brightdata.com/blog/ai/sse-vs-streamable-http)
- [Cloudflare Remote MCP Servers](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/)
- [GitHub Remote MCP Server](https://github.com/github/github-mcp-server)
- [Connecting to PiecesOS via Ngrok](./Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md)
- [ngrok + MCP Integration Guide (ngrok docs)](https://ngrok.com/docs/using-ngrok-with/using-mcp)
