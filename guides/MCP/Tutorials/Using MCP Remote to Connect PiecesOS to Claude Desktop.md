# Tutorial: Connect PiecesOS to Claude Desktop with MCP Remote

This guide is written for non-technical users and is fully step-by-step from start to finish.

`Claude Desktop (stdio config) -> mcp-remote -> PiecesOS MCP`

---

## What You Are Setting Up

Claude Desktop's local JSON config launches command-line tools. PiecesOS exposes MCP over HTTP/SSE.  
`mcp-remote` is the bridge between the two.

### Why this guide uses direct MCP integration (not Pieces CLI)

Per Pieces docs, Claude Desktop can be configured in multiple ways. This guide standardizes on **direct `mcp-remote` integration** because it is easier to verify and troubleshoot in one place (`claude_desktop_config.json`) and avoids stale `pieces.exe ... mcp start` path issues.

---

## Before You Start

- **Internet is required on first run** of `npx -y mcp-remote ...` so it can download `mcp-remote`.
- Keep **Pieces Desktop running** during setup.
- If you used a previous Pieces CLI MCP config, this guide removes it safely in Step 6.

---

## Step 1 - Install Required Apps (One Time)

Install these first:

1. **Pieces Desktop** (runs PiecesOS) - https://pieces.app
2. **Claude Desktop** - https://claude.ai/download
3. **Node.js LTS** (`npx` depends on this)

If you're unsure whether Node.js is installed, run the check first.  
If not installed, run the install one-liner right below it.

### macOS check (Terminal)

```bash
command -v node >/dev/null 2>&1 && node --version || echo "Node.js is not installed"
```

### macOS install (Terminal)

```bash
command -v node >/dev/null 2>&1 || (command -v brew >/dev/null 2>&1 || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"; brew install node)
```

### Linux check (Ubuntu/Debian Terminal)

```bash
command -v node >/dev/null 2>&1 && node --version || echo "Node.js is not installed"
```

### Linux install (Ubuntu/Debian Terminal)

```bash
command -v node >/dev/null 2>&1 || (curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt-get install -y nodejs)
```

### Windows check (PowerShell)

```powershell
if (Get-Command node -ErrorAction SilentlyContinue) { node --version } else { Write-Host "Node.js is not installed" }
```

### Windows install (PowerShell)

```powershell
if (-not (Get-Command node -ErrorAction SilentlyContinue)) { winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements }
```

Then verify Node/npm/npx:

### macOS/Linux verify

```bash
node --version && npm --version && npx --version
```

### Windows verify (PowerShell)

```powershell
node --version; npm --version; npx --version
```

Finally, verify `mcp-remote` can be resolved:

```bash
npx -y mcp-remote@latest --version
```

---

## Step 2 - Start Pieces Desktop

Run the one-liner for your OS:

### macOS

```bash
open "pieces://launch"
```

### Linux

```bash
xdg-open "pieces://launch"
```

### Windows (PowerShell)

```powershell
Start-Process "pieces://launch"
```

If nothing opens, launch Pieces Desktop manually once from your app launcher, then re-run the command.

Expected result: PiecesOS is active.

---

## Step 3 - Find Your PiecesOS Port (One-Liner)

PiecesOS uses a local port in `39300-39333`.

### macOS/Linux (stores result in `PORT`)

```bash
PORT=$(for p in $(seq 39300 39333); do curl -fsS "http://localhost:$p/.well-known/version" >/dev/null 2>&1 && echo "$p" && break; done); echo "Detected PORT=$PORT"
```

### Windows (PowerShell, stores result in `$PORT`)

```powershell
$PORT = 39300..39333 | ForEach-Object { try { $r = Invoke-WebRequest -Uri "http://localhost:$($_)/.well-known/version" -UseBasicParsing -TimeoutSec 2; if ($r.StatusCode -eq 200) { "$($_)"; break } } catch {} }; Write-Host "Detected PORT=$PORT"
```

If no port is detected, close/reopen Pieces Desktop and run again.

---

## Step 4 - Open or Create Claude Desktop Config

Config file path by OS:

| Platform | Path |
|----------|------|
| **macOS** | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Windows** | `%APPDATA%\Claude\claude_desktop_config.json` |
| **Linux** | `~/.config/Claude/claude_desktop_config.json` |

Optional directory check first:

### macOS check

```bash
[ -d "$HOME/Library/Application Support/Claude" ] && echo "Found: $HOME/Library/Application Support/Claude" || echo "Not found yet (will be created)"
```

### Linux check

```bash
[ -d "$HOME/.config/Claude" ] && echo "Found: $HOME/.config/Claude" || echo "Not found yet (will be created)"
```

### Windows check (PowerShell)

```powershell
if (Test-Path "$env:APPDATA\Claude") { Write-Host "Found: $env:APPDATA\Claude" } else { Write-Host "Not found yet (will be created)" }
```

Now run one open/create command:

### macOS open/create

```bash
CFG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"; mkdir -p "$(dirname "$CFG")"; [ -f "$CFG" ] || printf '{\n  "mcpServers": {}\n}\n' > "$CFG"; open "$CFG"
```

### Linux open/create

```bash
CFG="$HOME/.config/Claude/claude_desktop_config.json"; mkdir -p "$(dirname "$CFG")"; [ -f "$CFG" ] || printf '{\n  "mcpServers": {}\n}\n' > "$CFG"; xdg-open "$CFG"
```

### Windows open/create (PowerShell)

```powershell
New-Item -ItemType Directory -Force "$env:APPDATA\Claude" | Out-Null; if (!(Test-Path "$env:APPDATA\Claude\claude_desktop_config.json")) { '{ "mcpServers": {} }' | Set-Content "$env:APPDATA\Claude\claude_desktop_config.json" }; notepad "$env:APPDATA\Claude\claude_desktop_config.json"
```

Alternative UI path: **Claude Desktop -> Settings -> Developer -> Edit Config**.

---

## Step 5 - Back Up Your Config (Recommended)

### macOS backup

```bash
CFG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"; [ -f "$CFG" ] && cp "$CFG" "${CFG}.backup.$(date +%Y%m%d-%H%M%S)" && echo "Backup created" || echo "No existing config to back up"
```

### Linux backup

```bash
CFG="$HOME/.config/Claude/claude_desktop_config.json"; [ -f "$CFG" ] && cp "$CFG" "${CFG}.backup.$(date +%Y%m%d-%H%M%S)" && echo "Backup created" || echo "No existing config to back up"
```

### Windows backup (PowerShell)

```powershell
$cfg="$env:APPDATA\Claude\claude_desktop_config.json"; if (Test-Path $cfg) { Copy-Item $cfg "$cfg.backup.$(Get-Date -Format 'yyyyMMdd-HHmmss')"; Write-Host "Backup created" } else { Write-Host "No existing config to back up" }
```

---

## Step 6 - Remove Legacy Pieces CLI Entries (If Present)

If your config has an old block like this, remove it:

```json
"Pieces": {
  "command": "C:\\...\\pieces.exe",
  "args": ["--ignore-onboarding", "mcp", "start"]
}
```

Run one cleanup command:

### macOS cleanup

```bash
CFG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"; [ -f "$CFG" ] && node -e 'const fs=require("fs");const p=process.argv[1];const j=JSON.parse(fs.readFileSync(p,"utf8"));const servers=j.mcpServers||{};for(const [k,s] of Object.entries({...servers})){const cmd=String((s&&s.command)||"").toLowerCase();const args=(Array.isArray(s&&s.args)?s.args:[]).map(v=>String(v).toLowerCase());if(cmd.includes("pieces")&&args.includes("mcp")&&args.includes("start"))delete servers[k];}j.mcpServers=servers;fs.writeFileSync(p,JSON.stringify(j,null,2)+"\n");console.log("Legacy Pieces CLI MCP entries removed if present.");' "$CFG" || echo "Config file not found yet; continuing."
```

### Linux cleanup

```bash
CFG="$HOME/.config/Claude/claude_desktop_config.json"; [ -f "$CFG" ] && node -e 'const fs=require("fs");const p=process.argv[1];const j=JSON.parse(fs.readFileSync(p,"utf8"));const servers=j.mcpServers||{};for(const [k,s] of Object.entries({...servers})){const cmd=String((s&&s.command)||"").toLowerCase();const args=(Array.isArray(s&&s.args)?s.args:[]).map(v=>String(v).toLowerCase());if(cmd.includes("pieces")&&args.includes("mcp")&&args.includes("start"))delete servers[k];}j.mcpServers=servers;fs.writeFileSync(p,JSON.stringify(j,null,2)+"\n");console.log("Legacy Pieces CLI MCP entries removed if present.");' "$CFG" || echo "Config file not found yet; continuing."
```

### Windows cleanup (PowerShell)

```powershell
$p="$env:APPDATA\Claude\claude_desktop_config.json"; if (Test-Path $p) { $j=Get-Content $p -Raw | ConvertFrom-Json; if (-not $j.mcpServers) { $j | Add-Member -NotePropertyName mcpServers -NotePropertyValue ([ordered]@{}) -Force }; $new=[ordered]@{}; foreach ($prop in $j.mcpServers.PSObject.Properties) { $s=$prop.Value; $cmd=("$($s.command)").ToLower(); $args=@(); if ($s.args) { $args=@($s.args | ForEach-Object { "$_".ToLower() }) }; if (-not ($cmd -like "*pieces*" -and $args -contains "mcp" -and $args -contains "start")) { $new[$prop.Name]=$s } }; $j.mcpServers=$new; $j | ConvertTo-Json -Depth 50 | Set-Content $p; Write-Host "Legacy Pieces CLI MCP entries removed if present." } else { Write-Host "Config file not found yet; continuing." }
```

If you also added old Pieces entries in **Claude Desktop -> Settings -> Connectors**, remove those old entries too so you do not have duplicate/conflicting configurations.

---

## Step 7 - Add/Update `mcpServers.pieces` (Safe Merge)

This step **keeps your other MCP servers** and only updates `mcpServers.pieces`.

### macOS set/update

```bash
CFG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"; node -e 'const fs=require("fs");const p=process.argv[1];const port=process.argv[2]||"39300";let j={};try{j=JSON.parse(fs.readFileSync(p,"utf8"));}catch{};if(!j||typeof j!=="object")j={};if(!j.mcpServers||typeof j.mcpServers!=="object")j.mcpServers={};j.mcpServers.pieces={command:"npx",args:["-y","mcp-remote",`http://localhost:${port}/model_context_protocol/2024-11-05/sse`,`--allow-http`,`--transport`,`sse-only`]};fs.writeFileSync(p,JSON.stringify(j,null,2)+"\n");console.log("Updated mcpServers.pieces using PORT="+port);' "$CFG" "$PORT"
```

### Linux set/update

```bash
CFG="$HOME/.config/Claude/claude_desktop_config.json"; node -e 'const fs=require("fs");const p=process.argv[1];const port=process.argv[2]||"39300";let j={};try{j=JSON.parse(fs.readFileSync(p,"utf8"));}catch{};if(!j||typeof j!=="object")j={};if(!j.mcpServers||typeof j.mcpServers!=="object")j.mcpServers={};j.mcpServers.pieces={command:"npx",args:["-y","mcp-remote",`http://localhost:${port}/model_context_protocol/2024-11-05/sse`,`--allow-http`,`--transport`,`sse-only`]};fs.writeFileSync(p,JSON.stringify(j,null,2)+"\n");console.log("Updated mcpServers.pieces using PORT="+port);' "$CFG" "$PORT"
```

### Windows set/update (PowerShell)

```powershell
if (-not $PORT) { $PORT="39300" }; $cfg="$env:APPDATA\Claude\claude_desktop_config.json"; if (Test-Path $cfg) { $j=Get-Content $cfg -Raw | ConvertFrom-Json } else { $j=[pscustomobject]@{} }; if (-not $j.mcpServers) { $j | Add-Member -NotePropertyName mcpServers -NotePropertyValue ([ordered]@{}) -Force }; $j.mcpServers.pieces=[ordered]@{ command="npx"; args=@("-y","mcp-remote","http://localhost:$PORT/model_context_protocol/2024-11-05/sse","--allow-http","--transport","sse-only") }; $j | ConvertTo-Json -Depth 50 | Set-Content $cfg; Write-Host "Updated mcpServers.pieces using PORT=$PORT"
```

---

## Step 8 - Validate JSON and Confirm Entry Exists

### macOS validate

```bash
CFG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"; node -e 'const fs=require("fs");const j=JSON.parse(fs.readFileSync(process.argv[1],"utf8"));if(!j?.mcpServers?.pieces)throw new Error("mcpServers.pieces missing");console.log("Config valid. pieces entry found.");' "$CFG"
```

### Linux validate

```bash
CFG="$HOME/.config/Claude/claude_desktop_config.json"; node -e 'const fs=require("fs");const j=JSON.parse(fs.readFileSync(process.argv[1],"utf8"));if(!j?.mcpServers?.pieces)throw new Error("mcpServers.pieces missing");console.log("Config valid. pieces entry found.");' "$CFG"
```

### Windows validate (PowerShell)

```powershell
$cfg="$env:APPDATA\Claude\claude_desktop_config.json"; try { $j=Get-Content $cfg -Raw | ConvertFrom-Json; if ($null -eq $j.mcpServers.pieces) { throw "mcpServers.pieces missing" }; Write-Host "Config valid. pieces entry found." } catch { Write-Error $_ }
```

---

## Step 9 - Restart Claude Desktop

Recommended (safest for non-technical users):
1. Fully quit Claude Desktop.
2. Reopen Claude Desktop.

Optional command one-liners:

### macOS restart

```bash
osascript -e 'quit app "Claude"' >/dev/null 2>&1; sleep 2; open -a "Claude"
```

### Linux restart

```bash
pkill -x Claude >/dev/null 2>&1; sleep 2; (command -v claude-desktop >/dev/null 2>&1 && nohup claude-desktop >/dev/null 2>&1 &) || echo "Reopen Claude Desktop from your app launcher"
```

### Windows restart (PowerShell)

```powershell
Get-Process Claude -ErrorAction SilentlyContinue | Stop-Process -Force; Start-Sleep -Seconds 2; $paths=@("$env:LOCALAPPDATA\Programs\Claude\Claude.exe","$env:LOCALAPPDATA\AnthropicClaude\Claude.exe"); $exe=$paths | Where-Object { Test-Path $_ } | Select-Object -First 1; if ($exe) { Start-Process $exe } else { Write-Host "Reopen Claude Desktop from Start menu" }
```

---

## Step 10 - Confirm It Works

1. Open a new Claude Desktop chat.
2. Look for the **tools/hammer icon** near the chat box.
3. Click it and confirm Pieces tools are listed.
4. Ask: `"What Pieces MCP tools are available?"`

If you see Pieces tools, setup is complete.

---

## Quick Troubleshooting

| Problem | What to do |
|---------|------------|
| `npx` not found | Install Node.js LTS, then rerun `node --version && npm --version && npx --version` |
| First run fails at `npx` with network error | Confirm internet access, then rerun `npx -y mcp-remote@latest --version` |
| JSON parsing/config errors | Rerun Step 8 validate command and fix JSON syntax |
| No tools icon or no Pieces tools | Fully quit and reopen Claude Desktop |
| Could not connect to localhost | Make sure Pieces Desktop is running, then rerun Step 3 |
| `404` or transport error | Keep `--transport` set to `sse-only` for this endpoint |
| Other MCP servers disappeared | Restore from backup in Step 5 and rerun Step 7 (safe merge command) |

---

## Optional: Remote Setup (Advanced)

If PiecesOS is on another machine, first expose it using ngrok, then use the ngrok HTTPS URL:

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

## Related Guides

- [Bridging Local MCP Clients to Remote Servers with mcp-remote](../Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) - Full `mcp-remote` reference
- [Claude Desktop Setup Guide](../Agent%20Setups%20%26%20Integrations/Claude%20Desktop.md) - Full Claude Desktop options
- [Connecting to PiecesOS from the Outside World via Ngrok](../Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) - Remote tunnel setup

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="../README.md">← Back to MCP Guides</a>&nbsp;&nbsp;</td>
</tr></table>
