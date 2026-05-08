# What's New in Pieces 5.1.0

**Release Date:** March 5, 2026
**Pieces Desktop:** 5.1.0
**PiecesOS:** 12.3.9

You've got a summary you run every morning. A conversation where one line buried in a long response is the thing you actually want to dig into. A local model you've been meaning to try but the setup was never quite right.

Pieces 5.1.0 is about removing friction from the workflows you already have. This release brings **Scheduled Summaries** so your briefings generate themselves, **Modality Focus** so you can query by *how* you captured something, **inline follow-ups** so you can drill into any line of a chat response, and a **completely rebuilt local LLM engine** that no longer depends on Ollama. Plus new cloud models, expanded BYOK support, and a smarter understanding of the people in your world.

---

## ⏰ Scheduled Summaries: Put Your Summaries on Autopilot

You shouldn't have to remember to check in with your work — Pieces can do it for you now. **Schedule any summary to run automatically** on a daily, weekly, or custom cadence, at whatever time works best for your day.

Start every Friday with a weekly recap already waiting, or kick off each morning with a fresh brief before you've had your coffee.

> **Note:** Scheduled summaries currently require the Desktop App to be running at the scheduled time. We're working on removing that limitation — stay tuned.

### What's New

**Automatic Scheduling**
- Set any summary to run on a daily, weekly, or custom schedule
- Choose the exact time that fits your routine
- Summaries generate in the background and are ready when you are

**Flexible Cadence Options**
- Daily — Morning briefs, end-of-day recaps, standup prep
- Weekly — Sprint reviews, client updates, week-in-review
- Custom — Match any reporting cycle or billing period

**Zero Effort, Always Current**
- No manual triggering required once configured
- Results are waiting for you when you open Pieces
- Combine with Custom Summary Templates for fully automated workflows

<video src="https://github.com/user-attachments/assets/df8fc701-ab7e-40bf-9a5a-501f551bd142" controls="controls" autoplay muted style="max-width: 730px">
</video>

*Set it and forget it. Your summaries generate on schedule and are ready when you are.*

### Use Cases

**Morning Brief on Autopilot**
- Schedule your Morning Brief to generate at 7:30 AM every weekday
- Open Pieces and your day's context is already waiting
- No clicks, no waiting — just start reading

**Weekly Client Updates**
- Schedule project-scoped summaries every Friday at 4 PM
- Copy the output directly into client emails or Slack updates
- Consistent format, zero manual effort

**Sprint Retrospective Prep**
- Schedule a two-week summary to generate at the end of each sprint
- Walk into retro with a full accounting of what happened
- Never scramble to remember what you worked on

**End-of-Day Journaling**
- Schedule a Day Recap at 5 PM to capture everything before you sign off
- Build a running log of your work without lifting a finger
- Review trends over weeks and months

### How to Use

1. **Open any summary** — from Home Base or the Summaries section
2. **Tap the schedule icon** — configure your cadence and time
3. **Save** — the summary will generate automatically on your schedule
4. **Check back anytime** — your scheduled summaries are always ready

---

## 🤖 New Cloud LLMs: Claude Opus 4.6 & Gemini 3.1

Two major models just landed in Pieces.

**Claude Opus 4.6** — Anthropic's strongest model yet. Excellent for complex, multi-step work where you need the model to actually think things through. Deep reasoning, nuanced responses, and strong performance on technical tasks.

**Gemini 3.1** — Google's latest. Fast, big context window, handles a wide range of tasks well. Great for breadth-heavy queries and large-context work.

### What's New

- Both models available immediately in Pieces Chat
- Enable them in Settings under Model Management
- Use them for summaries, chats, and any chat interaction
- Compare performance across models for your specific use cases

<video src="https://github.com/user-attachments/assets/29ce5dd2-a4b3-41aa-a19b-a769967478cf" controls="controls" autoplay muted style="max-width: 730px">
</video>

*The latest from Anthropic and Google — available now in Pieces Chat.*

### How to Enable

1. **Open Settings** — navigate to Model Management
2. **Enable the models** — toggle on Claude Opus 4.6 and/or Gemini 3.1
3. **Select in chat** — choose your preferred model from the model picker
4. **Start using** — all chat features work with the new models

---

## 🔑 Full BYOK Support: OpenAI, Google AI Studio & Anthropic

**Bring Your Own Key (BYOK)** now works with three additional providers, joining existing support for AWS Bedrock and Microsoft Azure OpenAI.

### What's New

**Newly Supported Providers**
- **OpenAI** — use your organization's key for the latest GPT & o-series models
- **Google AI Studio** — bring your AI Studio key and use Gemini through your own account
- **Anthropic** — connect your key for the full Claude lineup

**Centralized Key Management**
- Manage all API keys from the Organization Portal
- Clear status indicators for each connected provider
- Easy setup and rotation of keys

<video src="https://github.com/user-attachments/assets/d16ad82b-c420-42d6-beb3-c05dc55678a3" controls="controls" autoplay muted style="max-width: 730px">
</video>

*Connect your org's API keys for OpenAI, Google AI Studio, and Anthropic — all managed from the Portal.*

### How to Configure

1. **Open the Organization Portal** — navigate to Models → API Keys
2. **Add your provider key** — paste your API key for OpenAI, Google AI Studio, or Anthropic
3. **Select models** — choose which models your organization can access
4. **Save** — keys are encrypted and stored securely

### Why It Matters

If your organization already has API agreements in place, BYOK keeps usage and costs where they belong — on your own account. This is especially valuable for enterprises with negotiated pricing, compliance requirements, or usage tracking needs.

---

## 🔧 Local LLMs, Rebuilt from the Ground Up

We've **completely rebuilt how Pieces runs local LLMs** — and it no longer depends on Ollama.

The new engine is significantly more stable, with fewer of the setup and runtime issues that Ollama occasionally introduced. It also opens the door to newer models that weren't available before, so there's more to choose from than ever.

### What's New

**New Local Runtime Engine**
- Purpose-built engine replacing the previous Ollama dependency
- More stable startup, fewer configuration issues
- Better resource management and performance

**Expanded Model Library**
- Access to newer models that weren't previously available
- Broader architecture support across platforms
- Faster model downloads and initialization

**Improved Reliability**
- Fewer crashes and timeout issues during inference
- Better error handling and recovery
- Consistent performance across extended sessions

<video src="https://github.com/user-attachments/assets/9aceab2e-0367-4eca-bac5-b9f00cd96530" controls="controls" autoplay muted style="max-width: 730px">
</video>

*Local LLMs that just work — no external dependencies, fewer setup headaches, more models to choose from.*

### How to Use

1. **Open Settings** — navigate to Model Management
2. **Browse local models** — explore the expanded library
3. **Download and enable** — select a model and it downloads automatically
4. **Use in chat** — select your local model from the model picker

### Why It Matters

If you've ever struggled to get a local model working — or had one crash mid-conversation — this should feel like a big improvement. Running models locally means your data never leaves your machine, and the new engine makes that experience dramatically more reliable.

---

## 🧠 Better Person Disambiguation in Memories

Pieces is getting much better at **distinguishing the people in your world**.

Whether it's teammates, managers, collaborators, or external contacts — Pieces can now tell them apart more reliably across your workstream. That means summaries and chat responses reference the right people in the right context, instead of blurring them together.

The more Pieces understands who's who, the more useful everything built on top of that becomes — from summaries that mention the right person to chat responses that accurately attribute decisions and discussions.

---

## 🗞️ Today's Headlines: Your World, Relevant to Your Work

Today's Headlines is a new **single-click summary** that pulls in real-time news — filtered around what's actually relevant to you and your work.

One tap and you've got a quick brief on topics tied to your projects, stack, and industry. No scrolling through feeds or hunting for context.

### What's New

**Personalized News Brief**
- One-click generation from the home dashboard
- News filtered by your projects, tech stack, and areas of focus
- Relevant industry developments surfaced automatically

**Work-Aware Filtering**
- Headlines are scoped to your actual work context
- Not a generic news feed — it knows what matters to you
- Surfaces developments in tools, languages, and platforms you use

<video src="https://github.com/user-attachments/assets/8231ef2a-3403-42d8-8a0c-f0d59b74e5e3" controls="controls" autoplay muted style="max-width: 730px">
</video>

*One tap for a news brief that actually matters to your work. No noise, no irrelevant headlines.*

### Use Cases

**Morning Context**
- Start your day knowing what happened overnight in your areas of focus
- Catch breaking changes in frameworks or libraries you depend on
- Stay informed without context-switching to news sites

**Client Conversations**
- Walk into meetings aware of industry developments relevant to the discussion
- Reference recent news in proposals and strategy conversations
- Demonstrate industry awareness effortlessly

**Technology Radar**
- Track developments in tools and platforms you're evaluating
- Stay ahead of deprecations, vulnerabilities, and major releases
- Build awareness over time with daily headlines

### How to Use

1. **Find it on the home dashboard** — Today's Headlines appears alongside your other single-click summaries
2. **Tap to generate** — one click and your personalized brief is ready
3. **Read and follow up** — use chat to dig deeper on any headline

### Early Access Note

This is our first pass at Today's Headlines. We'll keep making it sharper — better relevance, more sources, tighter signal. We're excited to hear what it pulls up for you.

---

## 🔭 Chat Modality Focus: Query by How You Captured It

Your workflow happens in a few different ways — what you copy, what you say, and what you see. Now you can **filter a chat prompt by how that information was captured**: clipboard, audio, or vision.

This is a small filter that makes a big difference when you know roughly *how* you encountered something.

### What's New

**Capture-Aware Filtering**
- Filter by **clipboard** — things you copied, pasted, or highlighted
- Filter by **audio** — things said in meetings, calls, or pair programming
- Filter by **vision** — things you viewed on screen, documentation, web pages

**Precision Queries**
- Narrow down results when you remember the modality but not the exact content
- Combine with time ranges and topic filters for surgical precision
- Reduce noise by excluding irrelevant capture types

<video src="https://github.com/user-attachments/assets/026b31e1-e13e-490f-a11f-757c93b48e34" controls="controls" autoplay muted style="max-width: 730px">
</video>

*Filter your queries by clipboard, audio, or vision to find exactly what you're looking for.*

### Example Queries

- "What have I been copying and pasting today related to this bug?"
- "What did someone say in this morning's meeting about the roadmap?"
- "What was that docs page I was reading while researching authentication?"
- "Show me everything I copied from Stack Overflow this week"
- "What did the team discuss about the migration plan in yesterday's call?"

### Use Cases

**Post-Meeting Recall**
- Filter by audio to surface what was discussed in a specific meeting
- Find decisions, action items, and commitments without scrubbing recordings
- Combine with time filters to isolate a single meeting

**Research Recovery**
- Filter by vision to find that documentation page you read but didn't bookmark
- Recover research context from browsing sessions
- Retrace your steps through a debugging session

**Code Pattern Search**
- Filter by clipboard to find code snippets you copied earlier
- Recover that terminal command you pasted three hours ago
- Track what you've been pulling from different sources

### How to Use

1. **Open a chat** — start a new chat or continue an existing one
2. **Select a modality filter** — choose clipboard, audio, or vision
3. **Ask your question** — Pieces scopes the search to that capture type
4. **Refine as needed** — combine with time and topic filters

---

## ↩️ Chat Response Follow-Up: Drill Into Any Line

Sometimes a chat response covers a lot of ground and you only want to go deeper on one part of it. Now you can **highlight any phrase or sentence in a response, tap follow-up, and a new prompt opens already tied to that exact text**.

No more copying things into a new message or over-explaining what you meant. Pieces knows exactly what you're pointing at.

### What's New

**Inline Follow-Up**
- Highlight any text in a chat response
- Tap follow-up to open a new prompt pre-loaded with that context
- Continue the conversation from exactly where you want to dig in

**Context Preservation**
- The follow-up retains the full context of the original conversation
- No need to re-explain what you were discussing
- Pieces understands the relationship between the original response and your follow-up

<video src="https://github.com/user-attachments/assets/92395c84-8341-4118-9cc0-a1b68719430d" controls="controls" autoplay muted style="max-width: 730px">
</video>

*Highlight a line, tap follow-up, and go deeper — no copy-pasting or re-explaining required.*

### Use Cases

**Deep Dive on a Recommendation**
- Pieces suggests five optimization strategies — follow up on the one that interests you most
- Get implementation details without wading through the rest

**Clarify a Specific Point**
- A long summary mentions a decision you don't remember — follow up for more context
- Ask "when did we decide this?" directly tied to that line

**Expand on a Code Suggestion**
- Pieces provides a solution with multiple approaches — follow up on one for full implementation
- Get test cases, edge case handling, or alternative implementations for just that approach

### How to Use

1. **Read a chat response** — find the line you want to explore
2. **Highlight the text** — select the phrase or sentence
3. **Tap follow-up** — a new prompt opens with that text as context
4. **Ask your question** — go deeper on exactly what you selected

---

## 🏢 A More Intuitive Organization Portal

The Organization Portal received significant attention this release with a focus on making administration easier and more intuitive.

### What's Improved

- **Cleaner navigation** — easier to move around and find what you need
- **Simpler API key management** — clearer status indicators, less clicking
- **Streamlined team management** — adding and removing members is faster
- **Better model selection** — easier access to org-level model configuration
- **Tidier layout** — the overall interface is cleaner and more organized

<video src="https://github.com/user-attachments/assets/79c8852c-9013-4330-8ac3-65e56e173198" controls="controls" autoplay muted style="max-width: 730px">
</video>

*A cleaner, more intuitive Organization Portal for managing your team and configuration.*

If you manage a Pieces organization, head to the Portal and have a look.

---

## ⭐ Favorite Summaries for Quick Access

Some summaries you run once. Others you keep coming back to. Now you can **star the ones you use most** for quick access right from the View More dialog.

Favorites pin to the top so you're not scrolling through the whole list every time. Tap the star on any summary to get started.

<video src="https://github.com/user-attachments/assets/f9c99874-98ad-4ad6-ba05-f15800ee1e51" controls="controls" autoplay muted style="max-width: 730px">
</video>

*Star your most-used summaries and find them instantly at the top of the list.*

---

## Getting Started with 5.1.0

If you're upgrading to 5.1.0, here's how to make the most of these new features:

1. **Schedule Your First Summary** — Pick your most-used summary and set it to run automatically every morning
2. **Try Modality Focus** — Ask in chat what you copied, heard, or saw — filter by how you captured it
3. **Follow Up on a Response** — Next time chat gives a long answer, highlight one line and tap follow-up
4. **Check Out Today's Headlines** — Tap the new summary on your home dashboard and see what's relevant to your work
5. **Try the New Cloud Models** — Enable Claude Opus 4.6 or Gemini 3.1 in Settings and compare them to your current model
6. **Explore Local LLMs** — If you've been hesitant about local models, the rebuilt engine makes setup dramatically easier

---

## What's Next

We're continuing to build on the workflows that matter most to you. Upcoming releases will bring:

- **Scheduled Summary Improvements**
  - Remove the requirement for the Desktop App to be running
  - Email and Slack delivery for scheduled summaries
  - More granular scheduling options

- **Enhanced Modality Intelligence**
  - Better audio transcription and attribution
  - Richer vision context extraction
  - Cross-modality correlation for deeper insights

- **Expanded BYOK & Enterprise Features**
  - Additional provider support
  - Usage analytics and cost tracking
  - Role-based access controls for model selection

Thank you for being part of the Pieces community. We're excited to keep building features that make your work more efficient and your memories more powerful!

---

## Learn More

- **[What's New in Pieces 5.0.3](./Whats%20New%20in%20Pieces%205.0.3.md)** — LTM Audio, Custom Summary Templates, MCP Server expansion
- **[What's New in Pieces 5.0.1](./Whats%20New%20in%20Pieces%205.0.1.md)** — Time Breakdown and Timeline enhancements
- **[What's New in Pieces 5.0.0](./Whats%20New%20in%20Pieces%205.0.0.md)** — The foundation that powers these features
- **[How to Query LTM in Pieces Copilot](../guides/How%20to%20Query%20LTM%20in%20Pieces%20Copilot.md)** — Master the art of querying your Long-Term Memory
- **[How to Use the Workstream Activity Timeline](../guides/How%20to%20Use%20the%20Workstream%20Activity%20Timeline.md)** — Understand your work patterns and history
- **[10 Queries To Ask Pieces LTM after 24-48 Hours](../guides/10%20Queries%20To%20Ask%20Pieces%20LTM%20after%2024-48%20Hours%20of%20Background%20Memory%20Formation.md)** — Get started with powerful LTM queries

---

**Questions or Feedback?**

We'd love to hear what you think about 5.1.0! Join our community or reach out to our support team.

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./Whats%20New%20in%20Pieces%205.0.3.md">← Previous: What's New in Pieces 5.0.3</a>&nbsp;&nbsp;</td>
<td align="right">&nbsp;&nbsp;<a href="./Whats%20New%20in%20Pieces%206.0.0.md">Next: What's New in Pieces 6.0.0 →</a>&nbsp;&nbsp;</td>
</tr></table>
