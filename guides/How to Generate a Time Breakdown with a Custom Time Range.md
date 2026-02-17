# How to Generate a Time Breakdown with a Custom Time Range

## What is Time Breakdown?

Time Breakdown is a single-click summary in the Pieces Desktop App that reconstructs your billable hours from your captured workstream context. Instead of scrambling at the end of the day to recall what you worked on, Time Breakdown analyzes your activity and generates structured time blocks—organized by project and activity—so you never start from a blank page.

Think of it as your memory assistant for time tracking. Pieces captures context from your code editors, browsers, meetings, and communication tools throughout the day, then Time Breakdown turns all of that into an audit-ready starting point you can review, refine, and submit.

**In this guide**, we'll walk through how to generate a Time Breakdown and configure a specific time range so you get exactly the reporting window you need.

<video src="https://github.com/user-attachments/assets/346c2d1e-7190-45a7-93a5-ed258bc04cfe" controls="controls" autoplay muted style="max-width: 730px">
</video>

---

## Why Time Ranges Matter

By default, Time Breakdown analyzes your recent activity. But not every professional reports on the same schedule:

- **Attorneys** may need to log billable hours at the end of each day
- **Consultants** might bill on a weekly or bi-weekly cycle
- **Government contractors** often need time & materials documentation for specific periods
- **Freelancers** may submit timesheets for custom windows that match client invoicing

Configurable time ranges let you scope your Time Breakdown to the exact period you need—whether that's the last 24 hours, the past week, or anything in between.

---

## Step-by-Step: Generating a Time Breakdown with a Preset Time Range

### Step 1 — Open Discover More

From your **Home Dashboard** in the Pieces Desktop App, tap **Discover More** to view all of the available single-click summary options.

<!-- ![](https://storage.googleapis.com/pieces_static_resources/pro_tips/time_breakdown_guide_discover_more.png) -->

### Step 2 — Select Time Breakdown

In the list of single-click summaries, find and tap **Time Breakdown**. This will open a new modal with a set of preset time range options to choose from.

<!-- ![](https://storage.googleapis.com/pieces_static_resources/pro_tips/time_breakdown_guide_select.png) -->

### Step 3 — Choose a Preset Time Range

Select the preset that matches your reporting needs:

- **Last 24 Hours** — Perfect for daily timesheet submissions
- **Last 2 Days** — Great for catching up on a missed day
- **Last Week** — Ideal for weekly billing cycles or sprint reviews
- **Last 2 Weeks** — Useful for bi-weekly invoicing or longer reporting periods
- **Last 30 Days** — For monthly reviews or end-of-month billing

<!-- ![Time Breakdown now supports configurable time ranges for flexible reporting](https://storage.googleapis.com/pieces_static_resources/pro_tips/5_0_3_time_breakdown_time_range_configuration.png) -->

### Step 4 — Generate Time Breakdown

Once you've selected a time range, tap **Generate Time Breakdown**. Pieces will analyze all the workstream context captured during that period and produce a structured breakdown.

This includes:
- **Approximate time blocks** showing when you worked on what
- **Project and client groupings** to organize your billing
- **Activity descriptions** that jog your memory on the details

### Step 5 — View, Edit, and Use Your Time Breakdown

Once the Time Breakdown is generated, you have several options:

- **View** the full breakdown to review your time blocks and activity summaries
- **Edit** any entries directly—adjust time blocks, add notes, merge or split activities, and fill in any gaps
- **Copy** the breakdown to paste into your billing system or timesheet
- **Export** for use in spreadsheets, legal billing tools, or PSA platforms
- **Use as context for a conversation** — start a chat from your Time Breakdown to ask Pieces Copilot follow-up questions or get more detail on specific time blocks

---

## What Gets Captured in a Time Breakdown

Time Breakdown draws from the same sources that power all of Pieces Long-Term Memory:

| Source | Examples |
|--------|----------|
| **Code Editors & IDEs** | VS Code, IntelliJ, PyCharm, Cursor |
| **Web Browsers** | Chrome, Firefox, Safari |
| **Communication Tools** | Teams, Slack, Discord, Email |
| **Documentation** | Notion, Confluence, GitHub |
| **Meetings & Calls** | Video calls, pair programming sessions |
| **Terminal** | Command line activity |

The more sources Pieces captures from, the more complete your Time Breakdown will be.

---

## Use Cases

### Daily Timesheets
Generate a Time Breakdown scoped to the **last 24 hours** at the end of each workday. Review, refine, and submit—no more guessing what happened at 2 PM.

### Weekly Client Billing
At the end of the week, generate a Time Breakdown for the **last 7 days**. Use the project groupings to separate billable hours by client, then export for invoicing.

### Sprint Reviews
Scope to your sprint duration to see how time was distributed across tasks. Use this as a data point for retrospectives and capacity planning.

### Invoice Preparation
Pull Time Breakdowns as a foundation for billing cycles. Refine the narratives, add client-specific context, then finalize.

### Memory Jogger
Can't remember what you were working on Tuesday afternoon? Generate a Time Breakdown for the **last 2 days** and let the activity descriptions bring you back up to speed.

---

## Pro Tips

### 1. Match Your Time Range to Your Billing Cycle
Don't just default to the last 24 hours. If you bill weekly, generate a weekly breakdown. If you bill bi-weekly, use the 2-week range. Matching your time range to your billing cycle reduces the number of breakdowns you need to generate and gives you a more complete picture.

### 2. Generate Before You Forget
The best time to generate a Time Breakdown is at the end of the day or the end of your billing period—while the work is still fresh. This makes it easier to review and fill in any gaps.

### 3. Use It Alongside Workstream Activity
Time Breakdown gives you the structured billing view. [Workstream Activity](./How%20to%20Use%20the%20Workstream%20Activity%20Timeline.md) gives you the narrative timeline. Use both together—browse the timeline to recall context, then use Time Breakdown to format it for billing.

### 4. Refine the Output
Time Breakdown is a starting point, not a finished product. Always review the output and add your professional judgment. Adjust time blocks, add client codes, and refine descriptions before submitting.

### 5. Start a Chat for More Detail
If a time block seems incomplete or you want more context, start a chat from the summary. Ask Pieces Copilot to elaborate on what happened during a specific window—this is a great way to fill gaps.

---

## Troubleshooting

### Time Breakdown Seems Incomplete?
- **Check your time range** — Make sure the selected range covers the period you need
- **Verify PiecesOS is running** — PiecesOS needs to be actively capturing context for Time Breakdown to have data to work with
- **Give it time** — If you just started using Pieces, it needs time to build up enough context for comprehensive breakdowns

### Time Blocks Don't Match Your Memory?
- Time Breakdown provides **approximate** time blocks based on captured activity. Use them as a starting point and adjust based on your recollection
- Edit entries directly to correct any inaccuracies
- Use [LTM queries](./How%20to%20Query%20LTM%20in%20Pieces%20Copilot.md) to investigate specific time periods in more detail

### Missing a Project or Client?
- Time Breakdown groups by detected projects and activities. If a project isn't showing up, the context for that work may not have been captured
- Make sure you're using Pieces-supported applications for that work
- Manually add entries for any work done in unsupported environments

---

## Summary

Time Breakdown turns your captured workstream context into structured, billable time entries—and configurable time ranges let you scope that breakdown to exactly the period you need.

**Key Takeaways:**
- **Discover More** — Tap Discover More from your Home Dashboard to find Time Breakdown
- **Preset time ranges** — Choose from last 24 hours, 2 days, 1 week, 2 weeks, or 30 days
- **One tap to generate** — Select your range and tap Generate Time Breakdown
- **Structured output** — Time blocks organized by project with activity descriptions
- **Fully editable** — View, edit, copy, export, or use as context for a conversation
- **Works with your cycle** — Match the time range to your billing schedule

Stop starting from a blank page. Let Time Breakdown give you the foundation, then apply your judgment to finalize.

---

## Need Help?

If you run into any issues or have questions, we're here to help:

- **Support Portal** — Visit [pieces.app/support](https://pieces.app/support) to browse FAQs and submit a request
- **GitHub Issues** — Report bugs or request features directly on our [GitHub Issues page](https://github.com/pieces-app/support/issues)
- **Book a Call** — Schedule time with our team directly: [Book a Call](https://calendar.app.google/bUwL7DGvsJsAohoW7)

---

*Reconstruct your billable hours with confidence—generate a Time Breakdown scoped to exactly the time range you need.*
