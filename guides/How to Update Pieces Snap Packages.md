# Quick Update Guide: Pieces for Developers (Linux/Snap)

This guide provides a simple 4-step process to update Pieces for Developers on Linux using Snap packages.

## Prerequisites

- Pieces for Developers installed via Snap
- PiecesOS installed via Snap
- `sudo` access for package updates

## Update Process

### Step 1 - Shutdown

Gracefully quits the Desktop App and the OS Server.

```bash
[ -n "$(pgrep -f pieces_for_x)" ] && xdg-open pieces-for-developers://quit; sleep 2; [ -n "$(pgrep -f os_server)" ] && xdg-open pieces://quit; sleep 3
```

---

### Step 2 - Check Versions (Optional)

Compares your installed Snap versions against the latest stable release.

```bash
snap info pieces-for-developers pieces-os
```

---

### Step 3 - Update

Refreshes the snap packages (requires sudo).

```bash
sudo snap refresh pieces-for-developers pieces-os
```

---

### Step 4 - Launch

Restarts PiecesOS followed by the Desktop App.

```bash
pieces-os & sleep 5; pieces-for-developers &
```

---

## Troubleshooting

### Applications Won't Quit Gracefully?

If the applications don't quit with the commands above, you can force terminate them:

```bash
# Force quit Desktop App
pkill pieces_for_x

# Force quit PiecesOS
pkill os_server
```

### Update Fails?

1. Check your internet connection
2. Ensure you have enough disk space
3. Check Snap service status: `sudo systemctl status snapd`
4. Restart Snap service: `sudo systemctl restart snapd`

## Notes

- Always shutdown applications before updating
- Always launch PiecesOS before the Desktop App
- Updates require `sudo` privileges
- Wait times between steps ensure proper shutdown/startup

