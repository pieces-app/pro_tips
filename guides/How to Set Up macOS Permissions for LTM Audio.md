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

<video src="https://github.com/user-attachments/assets/971a1c28-7e44-46bf-bad2-5a5d2be00cb7" controls="controls" autoplay muted style="max-width: 730px">
</video>

---

## Step 1: Open the Permissions Modal

1. Open the **Pieces Desktop App**
2. Click your **Profile button** in the top center of the screen
3. If your permissions aren't fully configured yet, you'll notice a small **warning icon** on or near your profile button
4. Click the **warning icon** to open the dedicated **Permissions modal**

The Permissions modal shows you exactly which permissions are currently enabled and which still need to be granted. For LTM Audio, you need two:

- **Microphone** — for audio input (your voice, ambient audio)
- **Screen & System Audio Recording** — for audio output (other meeting participants, system sounds)

---

## Step 2: Grant Microphone Access

Microphone access lets PiecesOS capture your voice and ambient audio — perfect for recording your side of meetings, pair programming discussions, and verbal problem-solving.

1. In the Permissions modal, click **Allow** next to the **Microphone** permission
2. Pieces will present a **macOS system dialog** that directs you straight to **System Settings → Privacy & Security → Microphone**
3. PiecesOS should **already be listed** as a line item in the Microphone section — simply **toggle it on**
4. If prompted, enter your **macOS password** or use **Touch ID** to confirm
5. macOS will ask you to **quit and reopen PiecesOS** — click **"Quit & Reopen"**

PiecesOS will restart in the background, and the Pieces Desktop App will automatically reconnect. The Permissions modal should now reflect the enabled microphone permission.

---

## Step 3: Grant Screen & System Audio Recording Permission

Screen & System Audio Recording permission lets PiecesOS capture audio output from your system — this is how it hears the other participants in your video calls, webinars, and presentations.

1. In the Permissions modal, click **Allow** next to the **Screen & System Audio Recording** permission
2. Pieces will present a **macOS system dialog** that directs you straight to **System Settings → Privacy & Security → Screen & System Audio Recording**
   - On older macOS versions (Ventura/Sonoma), this may appear as **Screen Recording**
3. Unlike the Microphone permission, PiecesOS will **not** be pre-listed here — you need to click the **"+" button** and **manually add PiecesOS** to the list of enabled applications
4. If prompted, enter your **macOS password** or use **Touch ID** to confirm
5. macOS will ask you to **quit and reopen PiecesOS** — click **"Quit & Reopen"**

PiecesOS will restart in the background, and the Pieces Desktop App will automatically reconnect. The Permissions modal should now show both permissions as enabled.

> **Important:** You must click **"Quit & Reopen"** when prompted. If you skip this step, the permission won't take effect until PiecesOS is manually relaunched.

---

## Step 4: Activate LTM Audio

Once both permissions are enabled and reflected in the Permissions modal, you're ready to turn on LTM Audio:

1. **Confirm both permissions show as enabled** in the Permissions modal
2. **Enable LTM Audio** — you can now activate it from the User Profile menu or PiecesOS Toolbar
3. LTM Audio will begin capturing audio context from your meetings and conversations immediately

> **Good news:** This is a **one-time setup**. Once you've granted both permissions, you won't need to go through this process again — the permissions persist across app updates and restarts.

---

## Step 5: Verify Everything is Working

After activating LTM Audio, confirm that audio context is flowing:

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

### Before You Enable

- **Pieces Desktop App** is updated to **5.0.3** or later
- **PiecesOS** is updated to **12.3.8** or later
- PiecesOS is **running** in the background
- You have your **macOS password** or **Touch ID** ready — you'll need it to confirm permission changes

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

Once LTM Audio is enabled and permissions are set, audio context will automatically flow into your Long-Term Memory. Try some of these queries in Pieces Copilot to see it in action:

### Recall What Was Said

```
What was discussed in my standup this morning?
```

```
What did the team decide about the release timeline in yesterday's planning call?
```

### Track Decisions & Action Items

```
What action items came out of my 1:1 with my manager this afternoon?
```

```
What did the client agree to during the kickoff call last Monday?
```

### Connect Audio with Screen Activity

```
What was discussed about the authentication module in yesterday's Teams call, and what code did I write afterward?
```

```
Summarize what was said in this morning's design review and what mockups I looked at in Figma afterward.
```

For more on querying your Long-Term Memory, check out the [How to Query LTM in Pieces Copilot](./How%20to%20Query%20LTM%20in%20Pieces%20Copilot.md) guide.

---

## Need Help?

If you run into any issues or have questions, we're here to help:

- **Support Portal** — Visit [pieces.app/support](https://pieces.app/support) to browse FAQs and submit a request
- **GitHub Issues** — Report bugs or request features directly on our [GitHub Issues page](https://github.com/pieces-app/support/issues)
- **Book a Call** — Schedule time with our team directly: [Book a Call](https://calendar.app.google/bUwL7DGvsJsAohoW7)

---

*Capture every conversation, decision, and insight — set up LTM Audio on macOS and let Pieces remember what you heard.*

---

| | |
|:---|---:|
| [← Previous: How to Enable LTM Audio Capture](./How%20to%20Enable%20LTM%20Audio%20Capture.md) | [Next: How to Generate a Time Breakdown →](./How%20to%20Generate%20a%20Time%20Breakdown%20with%20a%20Custom%20Time%20Range.md) |
