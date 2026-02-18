# Securely Expose PiecesOS Localhost, APIs, and MCP to the Outside World via HTTPS

This guide explains how to proxy your local PiecesOS server—including its APIs and Model Context Protocol (MCP) endpoint—to the public internet over HTTPS using [ngrok](https://ngrok.com). This enables remote AI clients (Cursor, Claude, Goose, etc.) to connect to your Long-Term Memory (LTM) when you're not on the same machine.

## Why Expose PiecesOS?

PiecesOS runs on your local machine. That's by design -- your memories, your data, your device. But there are compelling reasons to give remote services a secure HTTPS path into your local MCP server. Here are the real-world use cases:

### Cloud-Hosted AI Agents (Claude Web, ChatGPT, Gemini)

Claude's web interface, ChatGPT with plugins, and other cloud-hosted AI tools increasingly support MCP endpoints. But they can't reach `localhost:39300`. With an ngrok tunnel, you give them a public HTTPS URL that routes straight to your local PiecesOS. Your memories never leave your machine -- only the query and response travel over the wire. This means you can ask Claude on the web "What did I work on last week?" and it queries your local LTM in real time.

### GitHub Actions and CI/CD Pipelines

Imagine a GitHub Actions workflow that queries your LTM for context about the codebase before generating release notes, writing PR descriptions, or running an AI code review. An agent running in CI can connect to your ngrok-exposed MCP endpoint, search your workstream summaries for recent decisions, and use that context to produce better output. The same applies to GitLab CI, CircleCI, or any pipeline that can make HTTPS requests.

### Automation Platforms (Zapier, Make, n8n)

Zapier and Make can call any HTTP endpoint. With your PiecesOS exposed via ngrok, you can build automations like:
- **Daily standup to Slack**: A scheduled Zap queries yesterday's workstream summaries and posts a formatted standup to your team channel.
- **Weekly digest to Notion**: A Make scenario pulls your weekly summaries and creates a structured page in your Notion workspace.
- **Meeting follow-up**: After a calendar event ends, trigger a query for audio transcriptions from that time window and email yourself the key points.
- **Activity alerts**: Monitor for specific keywords in your workstream events and get notified when they appear.

### Cloud IDEs and Remote Machines (Codespaces, Gitpod, SSH)

You're working from GitHub Codespaces, Gitpod, or SSH'd into a remote server. Your Pieces MCP tools need to reach your local machine where PiecesOS is running. Point the remote MCP client at your ngrok URL and you have full LTM access as if you were on localhost. No VPN, no port forwarding, no firewall rules.

### Demos and Presentations

Sharing your ngrok URL during a live demo or sales call lets a remote audience interact with your Pieces instance from their own browser. They can see the MCP tools in action, query your (sanitized) LTM, and experience the product without installing anything.

### Cross-Device Access

Working from your phone, tablet, or a borrowed laptop? If you have a browser or any HTTP client, you can query your PiecesOS via the ngrok URL. Check what you worked on today, search for a code snippet you copied earlier, or recall what was discussed in a meeting -- all from a device that doesn't have Pieces installed.

### Multi-Agent Architectures

Building a system where multiple agents collaborate? A coordinator agent running in the cloud can dispatch queries to your local Pieces MCP via ngrok, gather context, and distribute it to specialized agents. Your local LTM becomes the shared memory layer for an entire agent swarm -- without ever moving your data off your machine.

## PiecesOS Default Endpoints

PiecesOS uses a well-known port range **39300–39333**. The exact port can vary; discover it by probing the version endpoint:

| Endpoint | URL Pattern | Notes |
|----------|-------------|-------|
| **Version (well-known)** | `http://localhost:PORT/.well-known/version` | Use this to find which port PiecesOS is running on |
| **Base** | `http://localhost:PORT` | Replace `PORT` with the discovered port |
| **MCP (Cursor)** | `http://localhost:PORT/model_context_protocol/2025-03-26/mcp` | For Cursor and compatible clients |
| **MCP (SSE)** | `http://localhost:PORT/model_context_protocol/2024-11-05/sse` | For Goose, GitHub Copilot |

> **Verify your port**: Open the **PiecesOS Quick Menu** → **Model Context Protocol (MCP) Servers** to see your active endpoint URL, or use the port search scripts below.

---

## Prerequisites

1. **PiecesOS running** — Ensure Pieces for Developers is running and the MCP server is active
2. **ngrok account** — Free at [ngrok.com](https://ngrok.com)
3. **ngrok installed** — See installation section below

---

## ngrok Installation & Setup

### macOS (Homebrew)

```bash
brew install ngrok
```

### Windows (Microsoft Store)

Install from the [Microsoft Store](https://apps.microsoft.com/store/detail/ngrok/9N4D1MSN0BZX) for automatic updates.

### Windows (Manual)

1. Download from [ngrok.com/download](https://ngrok.com/download)
2. Extract and add the directory to your `PATH`

### Linux (Debian/Ubuntu)

```bash
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update && sudo apt install ngrok
```

### Linux (Manual)

```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
sudo tar xvzf ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
```

### One-Time Authentication

1. Sign up at [ngrok.com](https://ngrok.com) and copy your authtoken from the dashboard
2. Run:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

---

## Basic Usage

### 1. Find PiecesOS Port

PiecesOS uses ports **39300–39333**. Discover which port is active by probing the well-known version endpoint:

**Bash (macOS/Linux):**

```bash
# Search ports 39300–39333 for PiecesOS
for p in $(seq 39300 39333); do
  if curl -s -o /dev/null -w "%{http_code}" --connect-timeout 1 "http://localhost:$p/.well-known/version" 2>/dev/null | grep -q 200; then
    echo "PiecesOS found on port $p"
    break
  fi
done
```

**PowerShell (Windows):**

```powershell
# Search ports 39300–39333 for PiecesOS
39300..39333 | ForEach-Object {
  try {
    $r = Invoke-WebRequest -Uri "http://localhost:$_/.well-known/version" -UseBasicParsing -TimeoutSec 1 -ErrorAction Stop
    if ($r.StatusCode -eq 200) { Write-Host "PiecesOS found on port $_"; $_ }
  } catch {}
} | Select-Object -First 1
```

### 2. Start ngrok Tunnel

```bash
ngrok http 39300   # Replace with your discovered port
```

ngrok will display a public HTTPS URL (e.g. `https://abc123.ngrok.app`). All traffic to that URL is forwarded to your local PiecesOS port.

### 3. MCP URL Over HTTPS

If your base ngrok URL is `https://abc123.ngrok.app`, your MCP endpoint is:

```
https://abc123.ngrok.app/model_context_protocol/2025-03-26/mcp
```

Use this URL in Cursor, Claude, or other MCP clients to connect remotely.

---

## One-Liner Scripts

### Bash: Find Port, Start Tunnel, Output URLs

```bash
MCP_PATH="/model_context_protocol/2025-03-26/mcp"

# Search ports 39300–39333 for PiecesOS (.well-known/version)
PORT=""
for p in $(seq 39300 39333); do
  if curl -s -o /dev/null -w "%{http_code}" --connect-timeout 1 "http://localhost:$p/.well-known/version" 2>/dev/null | grep -q 200; then
    PORT=$p
    break
  fi
done

if [ -z "$PORT" ]; then
  echo "PiecesOS not found on ports 39300–39333. Is PiecesOS running?"
  exit 1
fi

echo "PiecesOS found on port $PORT"
ngrok http $PORT --log=stdout > /tmp/ngrok.log 2>&1 &
NGROK_PID=$!
sleep 3

BASE_URL=$(curl -s http://localhost:4040/api/tunnels 2>/dev/null | jq -r '.tunnels[0].public_url // empty')
if [ -z "$BASE_URL" ]; then
  echo "Failed to get ngrok URL. Check /tmp/ngrok.log"
  kill $NGROK_PID 2>/dev/null
  exit 1
fi

echo "Base HTTPS URL: $BASE_URL"
echo "MCP URL:        $BASE_URL$MCP_PATH"
echo ""
echo "ngrok PID: $NGROK_PID (kill with: kill $NGROK_PID)"
```

### Bash: Minimal One-Liner (requires jq)

```bash
PORT=$(for p in $(seq 39300 39333); do curl -s -o /dev/null -w "%{http_code}" --connect-timeout 1 "http://localhost:$p/.well-known/version" 2>/dev/null | grep -q 200 && echo $p && break; done); ngrok http $PORT >/dev/null 2>&1 & sleep 3; BASE=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url'); echo "Base: $BASE"; echo "MCP:  $BASE/model_context_protocol/2025-03-26/mcp"
```

### PowerShell: Find Port, Start Tunnel, Output URLs

```powershell
$McpPath = "/model_context_protocol/2025-03-26/mcp"

# Search ports 39300–39333 for PiecesOS (.well-known/version)
$Port = 39300..39333 | ForEach-Object {
  try {
    $r = Invoke-WebRequest -Uri "http://localhost:$_/.well-known/version" -UseBasicParsing -TimeoutSec 1 -ErrorAction Stop
    if ($r.StatusCode -eq 200) { $_ }
  } catch {}
} | Select-Object -First 1

if (-not $Port) {
    Write-Error "PiecesOS not found on ports 39300–39333. Is PiecesOS running?"
    exit 1
}

Write-Host "PiecesOS found on port $Port"
$job = Start-Job -ScriptBlock { param($p) & ngrok http $p } -ArgumentList $Port
Start-Sleep -Seconds 3

try {
    $api = Invoke-RestMethod -Uri "http://localhost:4040/api/tunnels" -ErrorAction Stop
    $baseUrl = $api.tunnels[0].public_url
    Write-Host "Base HTTPS URL: $baseUrl"
    Write-Host "MCP URL:        $baseUrl$McpPath"
    Write-Host "`nngrok Job ID: $($job.Id) (stop with: Stop-Job -Id $($job.Id))"
} catch {
    Write-Error "Failed to get ngrok URL: $_"
    Stop-Job -Job $job
    exit 1
}
```

### PowerShell: Minimal One-Liner

```powershell
$p=(39300..39333|%{try{if((Invoke-WebRequest "http://localhost:$_/.well-known/version" -UseBasicParsing -TimeoutSec 1 -EA Stop).StatusCode -eq 200){$_}}catch{}}|Select -First 1); Start-Job { param($x) ngrok http $x } -Arg $p | Out-Null; Start-Sleep 3; $u=(Invoke-RestMethod http://localhost:4040/api/tunnels).tunnels[0].public_url; "Base: $u"; "MCP:  $u/model_context_protocol/2025-03-26/mcp"
```

---

## ngrok Local API

When ngrok is running, it exposes a local API at `http://localhost:4040`:

| Endpoint | Purpose |
|----------|---------|
| `http://localhost:4040` | Web UI for inspecting traffic |
| `http://localhost:4040/api/tunnels` | JSON list of active tunnels and public URLs |

Example: extract the public URL with `curl` and `jq`:

```bash
curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url'
```

---

## Security Considerations

1. **Temporary use** — Keep tunnels open only when needed; close ngrok when done
2. **Traffic visibility** — ngrok decrypts and forwards traffic; avoid exposing highly sensitive data
3. **Basic auth (paid plans)** — Use `ngrok http PORT --basic-auth="user:pass"` for simple protection (replace PORT with your discovered port)
4. **IP allowlist** — Paid plans support `--cidr-allow` to restrict access by IP
5. **Custom domains** — For production, use reserved domains and optional traffic policies

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "PiecesOS not found on ports 39300–39333" | Start Pieces for Developers and ensure MCP is enabled |
| "Failed to get ngrok URL" | Wait a few more seconds; ngrok may still be connecting |
| "jq: command not found" | Install jq (`brew install jq` on macOS) or parse JSON manually |
| Port discovery slow | Scripts probe 39300–39333; first responding port is used |

---

## References

- [ngrok Documentation](https://ngrok.com/docs)
- [ngrok Agent CLI](https://ngrok.com/docs/agent/cli)
- [ngrok Local API](https://ngrok.com/docs/agent/api)
- [Pieces MCP for Cursor](https://docs.pieces.app/products/mcp/cursor)
- [Pieces MCP for Goose](https://docs.pieces.app/products/mcp/goose)
