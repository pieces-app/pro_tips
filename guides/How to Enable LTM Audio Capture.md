# How to Enable LTM Audio Capture

## What is LTM Audio?

LTM Audio extends the Long-Term Memory Engine by capturing context from your spoken conversations—meetings, pair programming sessions, huddles, and more. When enabled, Pieces passively listens to your audio interactions and weaves them into your Long-Term Memory alongside everything else you're already capturing from your screen.

Think of it as giving Pieces ears in addition to eyes. Instead of only remembering what you typed, browsed, and coded, Pieces can also remember what was said—turning verbal discussions into searchable, queryable context you can reference anytime.

> **Introduced in [Pieces 5.0.3](../releases/Whats%20New%20in%20Pieces%205.0.3.md) (PiecesOS 12.3.8).** LTM Audio is currently available as a preview feature. Requires Pieces Desktop 5.0.3 or later.

## Why Enable LTM Audio?

Without audio capture, Pieces can only build context from what happens on your screen. But a huge amount of your work happens verbally:

- **Standup meetings** where tasks and blockers are discussed
- **Code reviews** where decisions are explained out loud
- **Pair programming sessions** where you talk through approaches
- **Slack huddles and Teams calls** where quick decisions get made
- **Design discussions** where architecture choices are debated

With LTM Audio enabled, all of that verbal context becomes part of your Long-Term Memory—searchable, summarized, and ready to query just like everything else.

---

## macOS Users: Set Up Permissions First

> **If you're on macOS**, you must grant microphone and system audio permissions before enabling LTM Audio. Without these permissions, audio capture won't work even if the toggle is turned on.
>
> Follow our dedicated guide to get your permissions configured: **[How to Set Up macOS Permissions for LTM Audio](./How%20to%20Set%20Up%20macOS%20Permissions%20for%20LTM%20Audio.md)**
>
> **Windows and Linux users** — no additional permissions setup is needed. You can jump straight to enabling LTM Audio below.

---

## How to Enable LTM Audio from the Pieces Desktop App

The Pieces Desktop App provides a straightforward way to toggle audio capture on or off from within the app settings.

<video src="https://github.com/user-attachments/assets/4322c770-fe15-4e00-9810-7ea9b77b3dcc" controls="controls" autoplay muted style="max-width: 730px">
</video>

### Steps

1. **Open the Pieces Desktop App**
2. **Tap your User Profile button** in the top center of the screen
3. **Find and tap "Enable LTM Audio"**
4. **Accept the Terms & Conditions** — If this is your first time enabling LTM Audio, you'll be prompted to review and accept a few terms and conditions before proceeding
5. **You're all set** — Once accepted, Pieces will begin forming memories from audio

Once enabled, Pieces will begin passively capturing audio from your meetings and conversations, adding that context to your Long-Term Memory.

---

## How to Enable LTM Audio from the PiecesOS Toolbar

You can also enable LTM Audio directly from the PiecesOS toolbar icon—useful when you want to quickly toggle audio capture without opening the full Desktop App.

<video src="https://github.com/user-attachments/assets/04f58d33-507a-486a-b14f-d03e3509a9b2" controls="controls" autoplay muted style="max-width: 730px">
</video>

### Steps

1. **Tap the PiecesOS toolbar icon**
   - **macOS** — Located in your top menu bar
   - **Windows** — Located in your lower-right system tray
   - **Linux** — Located in the top-right of your toolbar
2. **Find and tap "Enable LTM Audio"** in the dropdown menu
3. **Accept the Terms & Conditions** — If this is your first time enabling LTM Audio, you'll be prompted to review and accept a few terms and conditions before proceeding
4. **You're all set** — Once accepted, Pieces will begin forming memories from audio

The toolbar method is especially handy when you're about to jump into a meeting and want to make sure audio capture is active without leaving your current workflow.

---

## Querying Your Audio Context

Once LTM Audio is enabled and you've had some meetings or conversations, you can query that audio context just like any other LTM data. Here are some example queries you can copy and paste directly into Pieces Copilot:

### For Developers

```
What was discussed in yesterday's standup about the blockers on the API migration?
```

```
What did the team decide on the database schema changes during this morning's code review call?
```

```
Summarize the architecture decisions from the engineering sync last Thursday.
```

### For Engineering Managers

```
What action items came out of yesterday's sprint planning meeting?
```

```
What did each team member report as their progress in this morning's standup?
```

```
What concerns were raised in the 1:1 with my direct report this afternoon?
```

### For Product Managers

```
What feature requirements were discussed in the stakeholder call this morning?
```

```
What did the design team say about the new onboarding flow in yesterday's review?
```

### For Executives & VCs

```
Summarize the key takeaways from today's board meeting.
```

```
What metrics were discussed in the quarterly business review last week?
```

### For Lawyers & Compliance

```
What were the key points discussed in the client consultation call this morning?
```

```
What did opposing counsel propose during the settlement discussion yesterday?
```

### For Accountants & Finance

```
What was agreed on regarding the Q4 budget allocations in the finance meeting today?
```

```
What did the auditor flag during the review call last Wednesday?
```

### For Consultants & Freelancers

```
What deliverables did the client request during our kickoff call this morning?
```

```
What feedback did the client give on the proposal during yesterday's walkthrough?
```

> **Tip:** Combine audio context with other LTM signals for even better results. For example:
>
> ```
> What was discussed about the authentication module in yesterday's Teams call, and what code did I write afterward in VS Code?
> ```
>
> This lets Pieces connect what was said with what you actually did.

---

## Things to Know

### Privacy and Control

- **You're always in control** — LTM Audio can be toggled on or off at any time from either the Desktop App or the PiecesOS toolbar
- **Local processing** — Audio is processed locally on your machine by PiecesOS
- **No always-on recording** — Audio context is captured and processed into memory, not stored as raw audio files

### Microphone Permissions

- On **macOS**, you may need to grant microphone access in **System Settings > Privacy & Security > Microphone**
- On **Windows**, check **Settings > Privacy > Microphone** to ensure PiecesOS has access
- On **Linux**, ensure your audio permissions are configured for the PiecesOS process

### Best Results

- **Enable audio before your meeting starts** — Make sure the toggle is on before joining a call
- **Use a clear microphone** — Better audio input means better context capture
- **Let it run** — The more audio context Pieces captures over time, the richer your Long-Term Memory becomes

---

## Troubleshooting

### Audio Not Being Captured?
- Verify that LTM Audio is enabled in either the Desktop App settings or the PiecesOS toolbar
- Check that PiecesOS has microphone permissions at the system level
- Make sure PiecesOS is running—audio capture requires an active PiecesOS process

### Audio Context Not Appearing in Queries?
- Give it some time—audio context needs to be processed and integrated into your Long-Term Memory
- Try being specific in your queries by referencing the meeting or conversation (e.g., "What was said in my 2pm meeting?")
- Make sure the "LTM Context" button is enabled in your Copilot chat—without it, Pieces won't search your Long-Term Memory

### Microphone Permission Issues?
- Restart PiecesOS after granting permissions—some systems require a restart for new permissions to take effect
- Check that no other application is exclusively locking your microphone
- On macOS, you may need to re-enable the permission after a system update

---

## Summary

LTM Audio brings your spoken conversations into the same Long-Term Memory that already captures your screen activity. Enable it from the **Pieces Desktop App** settings or the **PiecesOS toolbar**—whichever is more convenient—and start building richer, more complete context from every part of your workday.

**Key Takeaways:**
- **Two ways to enable** — Desktop App settings or PiecesOS toolbar
- **Captures verbal context** — Meetings, calls, pair programming, huddles
- **Fully queryable** — Ask about what was said just like you ask about what you coded or browsed
- **You're in control** — Toggle on or off anytime, processed locally
- **Better together** — Combine audio context with screen context for the richest Long-Term Memory

Turn on LTM Audio, and never lose track of what was said again.

---

## Need Help?

If you run into any issues or have questions, we're here to help:

- **Support Portal** — Visit [pieces.app/support](https://pieces.app/support) to browse FAQs and submit a request
- **GitHub Issues** — Report bugs or request features directly on our [GitHub Issues page](https://github.com/pieces-app/support/issues)
- **Book a Call** — Schedule time with our team directly: [Book a Call](https://calendar.app.google/bUwL7DGvsJsAohoW7)

---

*Give Pieces ears—enable LTM Audio and make every conversation part of your Long-Term Memory.*

---

**See also:** [How to Query LTM in Pieces Copilot](./How%20to%20Query%20LTM%20in%20Pieces%20Copilot.md) — Ask questions about what was said in your meetings using natural language

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./Navigating%20the%20Desktop%20App%20UI%20with%20the%20Power%20Menu.md">← Previous: Navigating the Desktop App UI with the Power Menu</a>&nbsp;&nbsp;</td>
<td align="right">&nbsp;&nbsp;<a href="./How%20to%20Set%20Up%20macOS%20Permissions%20for%20LTM%20Audio.md">Next: How to Set Up macOS Permissions for LTM Audio →</a>&nbsp;&nbsp;</td>
</tr></table>
