# How to Set Up macOS Permissions for LTM Audio

## What is LTM Audio?

LTM Audio is a preview feature in Pieces 5.0.3 that lets you capture **microphone input and system audio output** as part of your Long-Term Memory formation. This means context from meetings, pair programming sessions, video calls, and other audio-rich moments flows directly into your memory—making your summaries, Copilot chats, and Workstream Activity richer and more complete.

Before LTM Audio can capture anything on macOS, you need to grant two system permissions: **Microphone Access** and **Screen & System Audio Recording**. macOS requires these permissions for any application that wants to listen to audio, and PiecesOS is no exception.

This guide walks you through enabling both permissions step by step so you can start capturing audio context right away.

---

## Before You Begin

Make sure you have:
- **macOS Ventura (13.0) or later** — required for the Screen & System Audio Recording permission
- **Pieces Desktop App 5.0.3** or later installed
- **PiecesOS 12.3.8** or later installed and running

> **Note:** If you haven't updated yet, update both the Pieces Desktop App and PiecesOS before proceeding. LTM Audio is not available in earlier versions.

---

## Video Walkthrough

<!-- VIDEO PLACEHOLDER: Insert video walkthrough of the macOS permissions setup process here -->

---

## Step 1: Enable LTM Audio in Pieces

Before macOS prompts you for permissions, you need to activate LTM Audio inside Pieces. You can do this in two ways:

**Option A — Via User Profile Menu**
1. Open the Pieces Desktop App
2. Click your **User Profile** menu (top-right corner)
3. Select **"Enable LTM Audio"**

**Option B — Via PiecesOS Toolbar**
1. Open the **PiecesOS Toolbar** application in your macOS menu bar
2. Look for the **"Enable LTM Audio"** button
3. Click to enable

Once you toggle LTM Audio on, macOS will prompt you to grant the necessary permissions. If it doesn't prompt you automatically, follow the manual steps below.

---

## Step 2: Grant Microphone Access

Microphone access lets PiecesOS capture your voice and ambient audio — perfect for recording your side of meetings, pair programming discussions, and verbal problem-solving.

### If macOS Prompts You Automatically

1. When you enable LTM Audio, macOS may display a dialog: **"PiecesOS would like to access the microphone"**
2. Click **"OK"** or **"Allow"** to grant access
3. You're done — move on to Step 3

### If You Need to Grant Access Manually

1. Open **System Settings** (click the Apple menu  → System Settings)
2. Navigate to **Privacy & Security** in the left sidebar
3. Click **Microphone**
4. Find **PiecesOS** in the list of applications
5. Toggle the switch **on** to grant microphone access
6. If prompted, enter your macOS password or use Touch ID to confirm

> **Tip:** If PiecesOS doesn't appear in the Microphone list, try restarting PiecesOS and enabling LTM Audio again. The app needs to request access at least once before it shows up in System Settings.

---

## Step 3: Grant Screen & System Audio Recording Permission

Screen & System Audio Recording permission lets PiecesOS capture audio output from your system — this is how it hears the other participants in your video calls, webinars, and presentations.

### If macOS Prompts You Automatically

1. macOS may display a dialog: **"PiecesOS would like to record the contents of your screen and capture audio from your system"**
2. Click **"Allow"** to grant access
3. If macOS asks you to **quit and reopen** PiecesOS, click **"Quit & Reopen"** to apply the permission

### If You Need to Grant Access Manually

1. Open **System Settings** (click the Apple menu  → System Settings)
2. Navigate to **Privacy & Security** in the left sidebar
3. Click **Screen & System Audio Recording**
   - On older macOS versions (Ventura/Sonoma), this may appear as **Screen Recording**
4. Find **PiecesOS** in the list of applications
5. Toggle the switch **on** to grant recording access
6. If prompted, enter your macOS password or use Touch ID to confirm
7. macOS will likely ask you to **quit and reopen PiecesOS** for the change to take effect — click **"Quit & Reopen"**

> **Important:** macOS requires a restart of PiecesOS after granting Screen & System Audio Recording permission. If you skip this step, system audio capture won't work until PiecesOS is relaunched.

---

## Step 4: Verify Everything is Working

After granting both permissions, confirm that LTM Audio is active and capturing:

1. **Check the LTM Audio indicator** — In the Pieces Desktop App or PiecesOS Toolbar, confirm that LTM Audio shows as **enabled**
2. **Generate some audio activity** — Join a quick call, play a video, or simply talk near your microphone for a minute
3. **Check your Workstream Activity** — After the next summary cycle (summaries generate every 20 minutes), look for audio-enriched context in your timeline
4. **Ask Copilot** — Try a query like *"What was discussed in my most recent meeting?"* to verify audio context is flowing into your Long-Term Memory

> **Tip:** It may take one full 20-minute summary cycle before audio context begins appearing in your Workstream Activity and Copilot responses. Give it a little time after enabling.

---

## Troubleshooting

### PiecesOS Doesn't Appear in the Permissions Lists

- **Restart PiecesOS** and try enabling LTM Audio again — the app must request access before macOS adds it to the list
- Make sure you're running **PiecesOS 12.3.8** or later

### Permission Was Granted but Audio Isn't Being Captured

- **Restart PiecesOS** — especially after granting Screen & System Audio Recording, macOS requires a relaunch
- **Check that LTM Audio is still enabled** — verify in the User Profile menu or PiecesOS Toolbar
- **Check both permissions** — microphone and Screen & System Audio Recording must both be enabled for full capture

### macOS Says "PiecesOS is Not Permitted"

- Open **System Settings → Privacy & Security** and manually toggle the relevant permission on for PiecesOS
- If the toggle is grayed out, click the **lock icon** at the bottom of the settings window and authenticate to make changes

### Only Microphone or Only System Audio is Working

- Each audio source requires its own permission:
  - **Microphone** — captures your voice and ambient audio
  - **Screen & System Audio Recording** — captures what comes through your speakers/headphones (other meeting participants, videos, etc.)
- Verify that **both** permissions are toggled on in System Settings

### Permission Prompts Aren't Appearing

- macOS only shows permission prompts once per app. If you dismissed a prompt previously, you'll need to grant access manually through **System Settings → Privacy & Security**
- Try toggling the permission off and back on in System Settings, then restart PiecesOS

---

## Quick Reference

| Permission | What It Captures | Where to Find It |
|---|---|---|
| **Microphone** | Your voice, ambient audio, your side of conversations | System Settings → Privacy & Security → Microphone |
| **Screen & System Audio Recording** | System audio output, other participants in calls, video/webinar audio | System Settings → Privacy & Security → Screen & System Audio Recording |

### Permission Checklist

- [ ] Pieces Desktop App updated to 5.0.3+
- [ ] PiecesOS updated to 12.3.8+
- [ ] LTM Audio enabled in Pieces (User Profile menu or PiecesOS Toolbar)
- [ ] Microphone access granted to PiecesOS
- [ ] Screen & System Audio Recording granted to PiecesOS
- [ ] PiecesOS restarted after granting Screen & System Audio Recording
- [ ] Audio context appearing in Workstream Activity / Copilot

---

## Privacy & Control

LTM Audio gives you full control over when audio is captured:

- **Toggle on/off anytime** — Enable or disable LTM Audio from the User Profile menu or PiecesOS Toolbar whenever you want
- **Local processing** — Pieces processes audio locally on your device to extract meaningful context
- **No raw audio storage** — Pieces extracts context from audio and discards the raw recordings
- **Revoke permissions anytime** — You can turn off Microphone or Screen & System Audio Recording in System Settings at any time

> **Pro Tip:** If you're about to have a sensitive conversation you don't want captured, simply toggle LTM Audio off beforehand and re-enable it when you're ready.

---

## What's Next

Once LTM Audio is enabled and permissions are set, audio context will automatically flow into your Long-Term Memory. Here's how to make the most of it:

- **Ask Copilot about meetings** — *"What was discussed in my standup this morning?"*
- **Check Workstream Activity** — Look for richer summaries that include discussion points and decisions from calls
- **Combine with LTM queries** — Reference audio context alongside your code, browser, and communication activity for a complete picture of your work

For more on querying your Long-Term Memory, check out the [How to Query LTM in Pieces Copilot](./How%20to%20Query%20LTM%20in%20Pieces%20Copilot.md) guide.

---

*Capture every conversation, decision, and insight — set up LTM Audio on macOS and let Pieces remember what you heard.*
