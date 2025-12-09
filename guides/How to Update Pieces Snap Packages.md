# How to Update Pieces Snap Packages

Keeping Pieces up to date ensures you have access to the latest features, bug fixes, and improvements. This guide covers how to update both the Pieces Desktop App (`pieces-for-developers`) and PiecesOS (`pieces-os`) using Snap package management.

---

## What Are Snap Packages?

Snap is a universal package management system for Linux that makes it easy to install and update applications. Pieces is distributed as Snap packages, which means updates are straightforward and automatic.

---

## Updating pieces-for-developers (Pieces Desktop App)

### 1. Quit the Application

Before updating, make sure to quit the Pieces Desktop App completely. Close all windows and ensure the application is not running in the background.

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

Open the Pieces Desktop App to start using the updated version.

---

## Updating PiecesOS

PiecesOS is the background service that powers Pieces' Long-Term Memory and activity capture. Keeping it updated is important for optimal performance.

### 1. Stop PiecesOS

Before updating, stop the PiecesOS service:

```bash
sudo snap stop pieces-os
```

This ensures a clean update process.

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

Start the PiecesOS service with the updated version:

```bash
sudo snap start pieces-os
```

The service will now be running with the latest version.

---

## Updating Both Packages Together

Before updating both packages, make sure to:
1. **Quit the Pieces Desktop App** - Close all windows and ensure it's not running
2. **Stop PiecesOS** - Run `sudo snap stop pieces-os`

Then you can update both Pieces packages at once using either method:

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

### Application Not Working After Update?

1. **Restart the application** - Close and reopen Pieces Desktop App
2. **Restart PiecesOS**:
   ```bash
   sudo snap restart pieces-os
   ```
3. **Check service status**:
   ```bash
   snap services pieces-os
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

- **Quit/Stop first**: Quit the Pieces Desktop App and stop PiecesOS (`sudo snap stop pieces-os`) before updating
- **Check versions**: `snap info pieces-for-developers` and `snap info pieces-os`
- **Update individually**: `sudo snap refresh pieces-for-developers` or `sudo snap refresh pieces-os`
- **Update both**: `sudo snap refresh pieces-for-developers pieces-os`
- **Update everything**: `sudo snap refresh`
- **Start/Launch**: Start PiecesOS (`sudo snap start pieces-os`) and launch the Desktop App after updates

Keeping both Pieces Desktop App and PiecesOS updated ensures you have access to the latest features and improvements.

---

*Stay up to date with the latest Pieces features and improvements.*

