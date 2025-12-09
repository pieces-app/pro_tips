# How to Update Pieces Snap Packages

Keeping Pieces up to date ensures you have access to the latest features, bug fixes, and improvements. This guide covers how to update both the Pieces Desktop App (`pieces-for-developers`) and PiecesOS (`pieces-os`) using Snap package management.

---

## What Are Snap Packages?

Snap is a universal package management system for Linux that makes it easy to install and update applications. Pieces is distributed as Snap packages, which means updates are straightforward and automatic.

---

> **Important:** Before updating either package, make sure **both** the Pieces Desktop App and PiecesOS are completely shut down. This ensures a clean update process and prevents conflicts.

---

## Updating pieces-for-developers (Pieces Desktop App)

> **Shutdown Order:** Always quit the Pieces Desktop App **first**, then quit PiecesOS. This order is important to prevent issues during the update process.

### 1. Quit the Application

Before updating, make sure to quit the Pieces Desktop App completely. You can do this in two ways:

#### Option 1: Using the GUI (Recommended)

The easiest way is to simply close the application window:
1. Click the "X" button in the top-right corner of the Pieces Desktop App window
2. Make sure all windows are closed and the application is not running in the background

**Note:** Wait a moment after closing the window to ensure the application fully and gracefully shuts down before proceeding with the update.

#### Option 2: Using the Command Line

Alternatively, you can quit the Pieces Desktop App from the command line:

```bash
[ -n "$(pgrep -f pieces_for_x)" ] && xdg-open pieces-for-developers://quit
```

**Note:** Wait a moment after running this command to ensure the application fully and gracefully shuts down before proceeding with the update.

**Fallback:** If the application doesn't quit gracefully with either method, you can force terminate it:

```bash
pkill pieces_for_x
```

### 2. Check the Currently Installed Version

Check what version you currently have installed:

```bash
snap info pieces-for-developers
```

This will show:
- Your currently installed version
- The latest version available
- Other package information

### 3. Update the Package

To update only the pieces-for-developers package:

```bash
sudo snap refresh pieces-for-developers
```

If a new version is available, Snap will download and apply the update automatically.

### 4. Verify the Update

After the refresh completes, verify the installed version:

```bash
snap info pieces-for-developers
```

You should now see the latest version listed as installed.

### 5. Launch the Application

> **Launch Order:** After updating, always launch PiecesOS **first**, then launch the Desktop App. The Desktop App may try to auto-launch PiecesOS during bootup, which can cause issues. Launching PiecesOS manually first ensures proper initialization.

**Do not launch the Desktop App yet.** First, update and launch PiecesOS (see the next section), then come back to launch the Desktop App.

To launch the Pieces Desktop App after PiecesOS is running:

```bash
pieces-for-developers
```

---

## Updating PiecesOS

PiecesOS is the background service that powers Pieces' Long-Term Memory and activity capture. Keeping it updated is important for optimal performance.

### 1. Stop PiecesOS

Before updating, quit the PiecesOS service. You can do this in two ways:

#### Option 1: Using the GUI (Recommended)

The easiest way is to use the PiecesOS system tray icon:
1. Look for the PiecesOS icon in your system tray (usually in the top-right or bottom-right corner)
2. Right-click on the PiecesOS icon
3. Select "Quit" from the menu

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/pieces_os_quit_linux.png)

**Note:** Wait a moment after quitting to ensure PiecesOS fully and gracefully shuts down before proceeding with the update.

#### Option 2: Using the Command Line

Alternatively, you can quit PiecesOS from the command line:

```bash
[ -n "$(pgrep -f os_server)" ] && xdg-open pieces://quit
```

**Note:** Wait a moment after running this command to ensure PiecesOS fully and gracefully shuts down before proceeding with the update. This ensures a clean update process.

**Fallback:** If PiecesOS doesn't quit gracefully with either method, you can force terminate it:

```bash
pkill os_server
```

### 2. Check the Currently Installed Version

Check what version of PiecesOS you have installed:

```bash
snap info pieces-os
```

This will show your current version and the latest available version.

### 3. Update PiecesOS

To update only PiecesOS:

```bash
sudo snap refresh pieces-os
```

Snap will download and install the latest version if one is available.

### 4. Verify the Update

Confirm the update was successful:

```bash
snap info pieces-os
```

You should see the latest version now installed.

### 5. Start PiecesOS

> **Launch Order:** Always start PiecesOS **first** before launching the Desktop App. This ensures PiecesOS is properly initialized and prevents the Desktop App from encountering issues when it tries to connect.

Start the PiecesOS service with the updated version:

```bash
pieces-os
```

The service will now be running with the latest version.

**After PiecesOS is running, you can now launch the Pieces Desktop App** (see step 5 in the "Updating pieces-for-developers" section above).

---

## Updating Both Packages Together

> **Important:** When updating both packages, always ensure both are completely shut down before updating, and always launch PiecesOS first, then the Desktop App.

Before updating both packages, make sure to quit both applications in this order:
1. **Quit the Pieces Desktop App first** - Close the window using the "X" button (GUI) or use the command line method
2. **Then quit PiecesOS** - Use the GUI (right-click system tray icon and select "Quit") or command line method

Wait a moment after quitting both to ensure they're fully shut down, then you can update both Pieces packages at once using either method:

### Option 1: Update Both Specifically

```bash
sudo snap refresh pieces-for-developers pieces-os
```

### Option 2: Update All Snap Packages

If you'd like to update everything at once (including other Snap packages on your system):

```bash
sudo snap refresh
```

This will update all Snap packages that have available updates.

### After Updating Both Packages

After the update completes, launch the applications in this order:

1. **Start PiecesOS first:**
   ```bash
   pieces-os
   ```

2. **Wait a moment** for PiecesOS to fully initialize

3. **Then launch the Desktop App:**
   ```bash
   pieces-for-developers
   ```

> **Remember:** Always launch PiecesOS before the Desktop App to prevent auto-launch conflicts.

---

## Checking for Updates Regularly

### Manual Check

You can check for updates anytime without installing them:

```bash
snap refresh --list
```

This shows all packages with available updates.

### Automatic Updates

Snap packages are configured to update automatically by default. Updates typically happen in the background, but you can also manually trigger them using the commands above.

---

## Troubleshooting

### Update Not Available?

If `snap info` shows you're already on the latest version, there's nothing to update. Check back later for new releases.

### Update Fails?

If an update fails, try:

1. **Check your internet connection** - Updates require downloading files
2. **Free up disk space** - Ensure you have enough space for the update
3. **Check Snap service status**:
   ```bash
   sudo systemctl status snapd
   ```
4. **Restart the Snap service** (if needed):
   ```bash
   sudo systemctl restart snapd
   ```

---

## Best Practices

1. **Keep both packages updated** - Pieces Desktop App and PiecesOS work together, so keeping both updated ensures compatibility
2. **Check regularly** - While automatic updates are enabled, manually checking ensures you're aware of new versions
3. **Restart after updates** - Always restart the application after an update to ensure all changes take effect
4. **Read release notes** - Check Pieces documentation or release notes to learn about new features and changes

---

## Summary

Updating Pieces Snap packages is straightforward:

- **Quit/Stop first**: Always quit the Pieces Desktop App **first**, then quit PiecesOS. Ensure both are completely shut down.
- **Check versions**: `snap info pieces-for-developers` and `snap info pieces-os`
- **Update individually**: `sudo snap refresh pieces-for-developers` or `sudo snap refresh pieces-os`
- **Update both**: `sudo snap refresh pieces-for-developers pieces-os`
- **Update everything**: `sudo snap refresh`
- **Start/Launch**: Always start PiecesOS (`pieces-os`) **first**, wait for it to initialize, then launch the Desktop App (`pieces-for-developers`)

Keeping both Pieces Desktop App and PiecesOS updated ensures you have access to the latest features and improvements.

---

*Stay up to date with the latest Pieces features and improvements.*

