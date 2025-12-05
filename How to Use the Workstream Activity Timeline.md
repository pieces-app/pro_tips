# How to Use the Workstream Activity Timeline

## What is Workstream Activity?

The Workstream Activity view in the Pieces Desktop App is your visual dashboard for everything you've been working on. It integrates with the Long-Term Memory Engine (LTM-2.7) to automatically capture and summarize your recent tasks, discussions, code reviews, meetings, and more—turning what happened into clear summaries in one click.

Think of it as your personal work journal that writes itself. While you're coding, attending meetings, or collaborating with your team, Pieces is quietly building a comprehensive view of your workstream—no manual note-taking required.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/workstream_activity_overview.png)

## How It Works

Workstream Activity continuously captures **events** from your work across all applications. Every 20 minutes, Pieces automatically generates a **Workstream Summary** that analyzes and summarizes the work performed during that time window.

### What Gets Captured

Just like with LTM queries, Workstream Activity captures events from:
- **Code editors and IDEs** (VS Code, IntelliJ, PyCharm, etc.)
- **Web browsers** (Chrome, Firefox, Safari)
- **Communication tools** (Teams, Slack, Discord, Email)
- **Documentation platforms** (Notion, Confluence, GitHub)
- **Terminal and command line**
- **Meetings and video calls**

All of these events are continuously captured as you work.

### How Summaries Are Generated

Every 20 minutes, Pieces analyzes all the events captured during that time window and generates a **Workstream Summary**. Each summary provides a clear, structured overview of:
- What you accomplished
- What you're working on
- Important discussions or decisions
- Code changes or technical work
- Meetings attended
- Key activities and context

These summaries are then displayed in the Workstream Activity timeline, creating a chronological record of your work.

---

## Understanding the Timeline View

Workstream Activity presents your summaries as a **timeline**—a chronological view of all your Workstream Summaries. Each entry in the timeline represents a 20-minute window of your work, making it easy to see what happened when and quickly understand your work patterns.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/workstream_activity_timeline.png)

---

## Key Features

### Automatic Summarization
Workstream Activity generates summaries automatically every 20 minutes. You don't need to do anything—just work normally, and Pieces will create summaries of your activity.

### Timeline View
Summaries are organized chronologically in a timeline, making it easy to see what happened when. Each summary covers a specific 20-minute window, giving you granular insight into your work patterns. Scroll through the timeline to browse your work history.

### Multi-Source Intelligence
Unlike traditional activity logs that only show one type of activity, Workstream Activity combines information from all sources. A single summary might include:
- Code you wrote in VS Code
- A meeting you attended
- A conversation you had in Slack
- Documentation you reviewed

All connected and contextualized in one summary.

### Interactive Summaries
Each summary in the timeline is interactive. You can:
- **View** — Read the full summary to understand what happened
- **Search** — Use the search function to find specific summaries or topics
- **Start Chats** — Begin a conversation with Pieces Copilot about that summary
- **Share** — Share summaries with your team or export them for documentation


### Actionable Insights
Summaries aren't just passive records—they're designed to help you take action. Each summary highlights:
- What you accomplished
- What you're working on
- What needs follow-up
- Important decisions or discussions

---

## How to Use Workstream Activity

### Daily Workflow

**Morning Routine:**
1. Open the Pieces Desktop App
2. Navigate to Workstream Activity
3. Review recent summaries to see what you accomplished yesterday or earlier today
4. Use this context to plan your day

**Throughout the Day:**
- Glance at Workstream Activity periodically to see new summaries as they're generated
- Use summaries to quickly catch up if you've been away
- Reference past summaries when you need to recall what happened
- Start chats from summaries to dive deeper into specific topics

**End of Day:**
- Scroll through the day's summaries in the timeline to see what you accomplished
- Use search to find specific topics or activities
- Share summaries with your team if needed

### Context Restoration

One of the most powerful uses of Workstream Activity is restoring context after:
- **Weekend breaks** — Quickly catch up on what happened Friday
- **Meetings** — See what you were working on before the meeting
- **Context switching** — Jump between projects without losing track
- **Returning from time off** — Get back up to speed quickly

### Integration with LTM Queries

Workstream Activity complements LTM queries perfectly:
- **Workstream Activity** gives you the visual, structured view
- **LTM Queries** let you search and ask specific questions

Use Workstream Activity to browse and discover, then use LTM queries to dive deep into specific topics.

---

## Pro Tips for Getting the Most Out of Workstream Activity

### 1. Make It a Habit
Check Workstream Activity regularly—especially in the morning to catch up on recent summaries. The more you use it, the more valuable it becomes as a source of truth for your work.

### 2. Use It for Standups
Instead of trying to remember what you did yesterday, open Workstream Activity and scroll through the timeline to review summaries from the past 24 hours. Use these summaries to prepare your standup update.

### 3. Start Chats from Summaries
When you see something interesting in a summary, click to start a chat about it. This lets you dive deeper into specific topics:
- "Tell me more about the authentication module work mentioned in this summary"
- "What were the specific requirements discussed in that meeting?"
- "Show me the code changes related to this summary"

### 4. Use Search to Find Specific Topics
Don't scroll through everything—use the search function to find summaries about specific projects, topics, or time periods. This makes it easy to locate exactly what you need.

> **Pro Tip:** The best way to narrow down summaries is to tap a **tag** or **source**. Tapping a tag or source will filter to only show summaries with that tag and source. It's a great way to distill a list of summaries from thousands to 5-10 relevant entries. For example, tap the "VS Code" source tag to see only summaries that include code work, or tap a project tag to see all summaries related to that specific project.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/workstream_activity_tag_source_filter.png)

### 5. Use Summaries for Documentation
When you need to document what you did or create a status update, Workstream Activity summaries provide a great starting point. They're already structured and comprehensive. Share them directly or use them as a foundation for your own documentation.

### 6. Understand Your Work Patterns
Scroll through the timeline to identify patterns in your work:
- When are you most productive?
- What types of tasks take up most of your time?
- How do you balance coding, meetings, and collaboration?

### 7. Share Context with Your Team
Use the share feature to send summaries to your team. This provides a clear, structured way to communicate what you've been working on without having to remember every detail.

---

## What Makes Workstream Activity Different

### Unlike Manual Note-Taking
- **No effort required** — It happens automatically
- **Never forgets** — Captures everything, even things you might not think to note
- **Always accurate** — Based on actual activity, not memory

### Unlike Activity Logs
- **Intelligent summaries** — Not just raw data, but contextualized insights
- **Multi-source** — Combines information from all your tools
- **Actionable** — Designed to help you take action, not just record history

### Unlike Calendar or Task Apps
- **Automatic** — No manual entry required
- **Contextual** — Shows what you did, not just what you planned
- **Comprehensive** — Captures the full picture of your work

---

## Troubleshooting

### Summaries Not Appearing?
- Make sure PiecesOS is running and capturing activity
- Check that you have sufficient activity for the 20-minute window
- Summaries are generated every 20 minutes—wait for the next generation cycle if you just started working

### Summaries Not Accurate?
- Summaries improve over time as Pieces learns your work patterns
- If something seems off, use LTM queries to get more specific information

### Missing Information?
- Workstream Activity captures what Pieces can see—make sure you're using supported applications
- Private or encrypted content may not be captured
- Use LTM queries to search for specific information that might not appear in summaries

---

## Best Practices

**Do:**
- Check Workstream Activity regularly to stay on top of your work
- Use summaries as a starting point for deeper exploration with chats or LTM queries
- Use search to find specific summaries quickly
- Start chats from summaries to dive deeper into topics
- Share summaries with your team when appropriate
- Scroll through the timeline to understand your work patterns

**Don't:**
- Rely solely on summaries—use chats or LTM queries for specific details
- Expect summaries to capture everything immediately—they improve over time
- Try to manually maintain what Workstream Activity does automatically
- Ignore the timeline—it's your complete work history

---

## Getting Started

1. **Open Pieces Desktop App** — Navigate to the Workstream Activity view
2. **Let It Run** — Work normally and let Pieces capture events continuously
3. **Wait for Summaries** — Every 20 minutes, a new summary will appear in your timeline
4. **Explore the Timeline** — Scroll through summaries to see your work history
5. **Start Chats** — Click on summaries to start conversations with Pieces Copilot
6. **Use Search** — Search for specific topics or time periods
7. **Share** — Share summaries with your team when needed

The more you use Workstream Activity, the more valuable it becomes. As summaries accumulate, you'll have a comprehensive timeline of your work that you can search, reference, and build upon.

---

## Summary

Workstream Activity is your automatic work journal—capturing events continuously and generating summaries every 20 minutes. The timeline view makes it easy to browse, search, and interact with your work history.

**Key Takeaways:**
- **Automatic** — Events captured continuously, summaries generated every 20 minutes
- **Timeline View** — Chronological view of all your Workstream Summaries
- **Interactive** — View, search, start chats, and share summaries
- **Comprehensive** — Captures from all your tools and combines them intelligently
- **Actionable** — Designed to help you take action and dive deeper
- **Complements LTM Queries** — Use both for maximum value

Combine Workstream Activity's timeline view with chats and LTM queries, and you have a complete system for understanding and accessing your work history.

---

*Turn what happened into clear summaries in one click with Workstream Activity.*

