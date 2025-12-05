# 10 Queries to Ask Pieces LTM after 24-48 Hours of Background Memory Formation

These queries have been tested with real LTM data to demonstrate practical usage patterns after 24 hours of memory formation.

---

## 5 Practical Queries for Daily Work

### 1\. **Daily Standup Generator**

**Query:**

```
Generate my standup update for today: what I accomplished in the past 24 hours, what I'm currently working on, and any blockers or questions I have for the team.
```

**What This Query Does:**

- **Time:** Past 24 hours (implicit "today" timeframe)  
- **Modality:** ALL sources (meetings, code, terminal, emails, chats)  
- **Topic:** General work summary focused on team communication  
- **Why It Works:** Natural language, clear structure (accomplished/working/blockers), suitable for morning standups

**Example Results:** Aggregates pipeline work, client onboarding activities, feature launches, and troubleshooting into a standup format.  
![](https://storage.googleapis.com/pieces_static_resources/pro_tips/daily_standup_generator.png)

---

### 2\. **Command Line Power User**

**Query:**

```
What are my top 5 most frequently used terminal commands or bash scripts from the past week?
```

**What This Query Does:**

- **Time:** Past week (explicit time range)  
- **Modality:** SPECIFIC \- Terminal only  
- **Topic:** Specific technical patterns (commands/scripts)  
- **Why It Works:** Focused modality filter, quantifiable request (top 5), identifies workflow patterns

**Example Results:** Returns frequently used commands like `ngrok`, `melos`, `dart run`, showing development workflow patterns.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/command_line_power_user.png)

---

### 3\. **Monday Morning Context Restoration**

**Query:**

```
It's Monday morning - based on what I was working on Thursday and Friday, where should I jump back in to continue my work? What was my momentum and what are the logical next steps?
```

**What This Query Does:**

- **Time:** Multi-day (Thursday \+ Friday), contextual (Monday morning)  
- **Modality:** ALL sources weighted toward code and tasks  
- **Topic:** General but focused on continuation and momentum  
- **Why It Works:** Scenario-based (Monday morning), asks for actionable next steps, references specific past timeframe

**Example Results:** Identifies unfinished work, pending tasks, and logical next steps for context restoration.

---

### 4\. **Follow-ups & Action Items Scanner**

**Query:**

```
What follow-ups, action items, or reminders came up in my emails, chats, and meetings over the past 48 hours that I shouldn't forget about?
```

**What This Query Does:**

- **Time:** Past 48 hours (explicit)  
- **Modality:** SPECIFIC \- Communications only (email, chat, meetings)  
- **Topic:** Specific (action items, commitments, follow-ups)  
- **Why It Works:** Explicit modality filtering, urgency framing ("shouldn't forget"), practical timeframe (2 days)

**Example Results:** Retrieves API key refresh reminders, meeting recording commitments, email drafts, and calendar scheduling items.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/follow_ups_action_items.png)

---

### 5\. **Clipboard History Search**

**Query:**

```
Resurface something interesting or valuable that I copied, pasted, or captured in the last 48 hours that I might want to reference or remember.
```

**What This Query Does:**

- **Time:** Past 48 hours (explicit)  
- **Modality:** SPECIFIC \- Clipboard/saved items  
- **Topic:** Specific (interesting/valuable content)  
- **Why It Works:** Targets ephemeral data (clipboard), asks for "interesting" (quality filter), retrieves previously copied content

**Example Results:** Returns email templates, configuration snippets, debugging notes, and code from clipboard history.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/clipboard_history.png)

---

## 3 Reflective Queries

### 6\. **Week in Review**

**Query:**

```
What did I accomplish this week and what's the vibe/theme of the work I've been doing? And how did my Friday turn out?
```

**What This Query Does:**

- **Time:** Full week with Friday focus  
- **Modality:** ALL sources for holistic view  
- **Topic:** Reflective and thematic (vibe, patterns, themes)  
- **Why It Works:** Narrative-focused language ("vibe/theme"), reflective tone, weekly retrospective framing

**Example Results:** Summarizes weekly themes like client onboarding, infrastructure work, and pipeline shipping.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/week_in_review.png)

---

### 7\. **Work Pattern Analysis**

**Query:**

```
Tell me a fun fact about my work style based on this week. What types of projects am I naturally drawn to, and what does my day-to-day rhythm look like?
```

**What This Query Does:**

- **Time:** This week (general timeframe)  
- **Modality:** ALL sources for pattern detection  
- **Topic:** Meta-analysis (work style, preferences, patterns)  
- **Why It Works:** Asks for "fun fact" (engaging format), personality-focused, identifies natural patterns

**Example Results:** Identifies patterns like morning meetings and afternoon focused work, plus preferences for developer tools and automation.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/work_pattern_analysis.png)

---

### 8\. **Weekly Highlights**

**Query:**

```
Give me a creative recap of my week - what was the vibe, what were the highlights, and any fun or unexpected moments in my work?
```

**What This Query Does:**

- **Time:** Week retrospective  
- **Modality:** ALL sources  
- **Topic:** Emotional/qualitative (vibe, highlights, surprises)  
- **Why It Works:** "Creative recap" invites storytelling, asks for highlights AND surprises, focuses on memorable moments

**Example Results:** Identifies key moments like feature launches, debugging sessions, and problem-solving opportunities.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/weekly_highlights.png)

---

## 2 Analytical Queries

### 9\. **Time & Efficiency Audit**

**Query:**

```
Based on how I spent my time yesterday, what did I focus on most? Where could I have been more efficient, and what was the coolest or most interesting thing I worked on?
```

**What This Query Does:**

- **Time:** Yesterday (specific day)  
- **Modality:** ALL sources for complete time analysis  
- **Topic:** Multi-part analysis (focus areas, efficiency, highlights)  
- **Why It Works:** Combines quantitative (time spent) with qualitative (efficiency, interesting), actionable insights

**Example Results:** Shows time distribution across meetings, coding, and communications with efficiency analysis.

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/time_and_efficiency_1.png)![](https://storage.googleapis.com/pieces_static_resources/pro_tips/time_and_efficiency_2.png)

---

### 10\. **Repeated Patterns & Code Abstractions**

**Query:**

```
I'm looking for repeatable code patterns that I can abstract or isolate into helper functions. What are sequences of code I've been copying and pasting repeatedly over the last 48 hours?
```

**What This Query Does:**

- **Time:** Past 48 hours (explicit)  
- **Modality:** SPECIFIC \- Clipboard/capture events  
- **Topic:** Coding patterns and frequently used code  
- **Why It Works:** Targets ephemeral actions (copy/paste), "repeatable" implies something that’s been used multiple times, and a practical timeframe

**Example Results:** Returns reused code snippets or concepts, and suggests coding improvements

![](https://storage.googleapis.com/pieces_static_resources/pro_tips/clipboard_gems.png)![](https://storage.googleapis.com/pieces_static_resources/pro_tips/clipboard_gems_2.png)

---

## Query Construction Patterns

### **Time Specification Strategies:**

- **Relative:** "today," "yesterday," "this week," "past 24 hours," "last 48 hours"  
- **Contextual:** "Thursday and Friday," "end of week," "Monday morning"  
- **Implicit:** "recent," "lately" (use sparingly—less precise)  
- **Best Practice:** Be specific when possible ("past 48 hours" \> "recently")

### **Modality Filtering:**

| ALL SOURCES | COMMUNICATION | CODE/TECHNICAL | CAPTURE |
| :---- | :---- | :---- | :---- |
| General summaries, themes | Emails, chats, meetings | Terminal, IDE, code | Clipboard, screenshots |
| "everything I did" | "in my conversations" | "commands I ran" | "things I copied" |
| "my work today" | "in meetings" | "in VS Code" | "snippets I saved" |

### **Topic Specificity:**

- **General:** "What did I work on?" (cast wide net)  
- **Focused:** "What follow-ups do I have?" (specific goal)  
- **Meta:** "What patterns emerged?" (analytical)  
- **Best Practice:** Match specificity to your need (broad for discovery, narrow for action)

---

## Query Best Practices

### Recommended Approaches:

- Use natural language (like talking to a colleague)  
- Be specific about time when it matters  
- Combine multiple dimensions (time \+ modality \+ topic)  
- Ask for actionable outcomes ("where should I jump back in?")  
- Request structured formats when helpful (standup format, top 5 list)

### Common Pitfalls:

- Don't use overly technical syntax ("SELECT \* FROM memories WHERE...")  
- Don't be vague about timeframes without context ("show me stuff")  
- Don't ask multiple unrelated questions in one query  
- Don't forget to specify modality when it matters

---

## What 24 Hours of Memory Formation Enables

After 24 hours of memory formation, you can:

1. Generate standup updates from yesterday's work  
2. Identify frequently used development commands and patterns  
3. Restore context when resuming work after breaks  
4. Track follow-ups and action items from conversations  
5. Search clipboard history for previously copied content  
6. Analyze work patterns and time allocation  
7. Create weekly retrospectives and summaries  
8. Identify efficiency opportunities in daily workflow  
9. Retrieve forgotten content from recent work  
10. Review weekly activities with full context

Pieces remembers context from meetings, code editors, terminal, communications, and clipboard activity, making all of it searchable through natural language queries.

---

## Usage Recommendations

1. **Morning Ritual:** Start your day with "What did I leave unfinished yesterday?"  
2. **Weekly Review:** On Friday afternoon, run "How did my week go?"  
3. **Context Switching:** Before meetings, ask "What was I working on before this?"  
4. **Learning Capture:** "What interesting technical solutions did I discover this week?"  
5. **Team Communication:** Use the standup query every morning for consistent updates  
6. **Experiment:** Try variations of these queries to find what works best for you  
7. **Be Specific:** The more specific your query, the more targeted your results  
8. **Iterate:** If results aren't quite right, refine your query with more context

---

## Summary

After 24 hours of memory formation, Pieces LTM contains:

- Meeting attendance and discussion content  
- Terminal commands and their context  
- Email communications and commitments  
- Code snippets and problem-solving approaches  
- Browser activity and conversations

These queries demonstrate how to access this information through natural language. Start with these examples and modify them based on your specific workflow needs.

---

*Want more query patterns? Ask Pieces: "Based on my work patterns, what other queries might be useful for me?"*  
