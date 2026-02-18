# Pieces MCP and LTM Tools Guide

Complete reference for every tool exposed by the Pieces MCP server. This guide is written for both end users configuring MCP integrations and AI agents consuming the tools programmatically.

---

## Table of Contents

- [Why Use Pieces MCP Alongside Your AI Agents](#why-use-pieces-mcp-alongside-your-ai-agents)

- [Overview](#overview)
- [Core Workflow Pattern](#core-workflow-pattern)
- [Temporal Filtering](#temporal-filtering)
- [LTM and Memory Tools](#ltm-and-memory-tools)
  - [ask_pieces_ltm](#ask_pieces_ltm)
  - [create_pieces_memory](#create_pieces_memory)
- [Full-Text Search Tools](#full-text-search-tools)
  - [workstream_summaries_full_text_search](#workstream_summaries_full_text_search)
  - [conversations_full_text_search](#conversations_full_text_search)
  - [tags_full_text_search](#tags_full_text_search)
  - [annotations_full_text_search](#annotations_full_text_search)
  - [persons_full_text_search](#persons_full_text_search)
  - [anchors_full_text_search](#anchors_full_text_search)
  - [workstream_events_full_text_search](#workstream_events_full_text_search)
  - [websites_full_text_search](#websites_full_text_search)
  - [hints_full_text_search](#hints_full_text_search)
  - [models_full_text_search](#models_full_text_search)
  - [wpe_sources_full_text_search](#wpe_sources_full_text_search)
  - [wpe_source_windows_full_text_search](#wpe_source_windows_full_text_search)
  - [entities_full_text_search](#entities_full_text_search)
  - [conversation_messages_full_text_search](#conversation_messages_full_text_search)
- [Vector / Semantic Search Tools](#vector--semantic-search-tools)
  - [materials_vector_search](#materials_vector_search)
  - [workstream_summaries_vector_search](#workstream_summaries_vector_search)
  - [hints_vector_search](#hints_vector_search)
  - [tags_vector_search](#tags_vector_search)
  - [workstream_events_vector_search](#workstream_events_vector_search)
- [Filter and Enumerate Tools](#filter-and-enumerate-tools)
  - [material_identifiers](#material_identifiers)
- [ML Capabilities Tools](#ml-capabilities-tools)
  - [extract_temporal_range](#extract_temporal_range)
- [Batch Snapshot Tools](#batch-snapshot-tools)
  - [workstream_summaries_batch_snapshot](#workstream_summaries_batch_snapshot)
  - [conversations_batch_snapshot](#conversations_batch_snapshot)
  - [tags_batch_snapshot](#tags_batch_snapshot)
  - [annotations_batch_snapshot](#annotations_batch_snapshot)
  - [persons_batch_snapshot](#persons_batch_snapshot)
  - [anchors_batch_snapshot](#anchors_batch_snapshot)
  - [anchor_points_batch_snapshot](#anchor_points_batch_snapshot)
  - [workstream_events_batch_snapshot](#workstream_events_batch_snapshot)
  - [hints_batch_snapshot](#hints_batch_snapshot)
  - [models_batch_snapshot](#models_batch_snapshot)
  - [ranges_batch_snapshot](#ranges_batch_snapshot)
  - [websites_batch_snapshot](#websites_batch_snapshot)
  - [entities_batch_snapshot](#entities_batch_snapshot)
  - [conversation_messages_batch_snapshot](#conversation_messages_batch_snapshot)
  - [wpe_sources_batch_snapshot](#wpe_sources_batch_snapshot)
  - [wpe_source_windows_batch_snapshot](#wpe_source_windows_batch_snapshot)
- [Common Workflow Examples](#common-workflow-examples)
- [Visibility Reference](#visibility-reference)

---

## Why Use Pieces MCP Alongside Your AI Agents

Every AI agent you use -- Cursor, Claude Code, Goose, GitHub Copilot, or any MCP-compatible client -- is powerful in the moment but fundamentally stateless. It can see your current file, your current prompt, maybe your current project. It cannot see what you were doing yesterday, what you decided in last week's architecture meeting, what you copied from Stack Overflow three days ago, or what your colleague said about the database migration during a pair programming session.

**Pieces MCP changes that.** It gives every agent access to your Long-Term Memory (LTM) -- a continuously captured, locally processed, and semantically searchable record of your entire work life. Pieces runs in the background and passively captures:

- **What's on your screen** -- screenshots processed with OCR so text in UIs, terminals, dashboards, and documentation becomes searchable
- **What's on your clipboard** -- every copy/paste operation, the code snippets you move between files, the URLs you grab, the error messages you capture
- **What's being said** -- microphone input and system audio output from meetings, pair programming sessions, video calls, and presentations, transcribed locally
- **What you're browsing** -- URLs, page titles, and context from Chrome, Firefox, Safari, and other browsers
- **What applications you're in** -- which IDE, which file, which terminal, which Figma board, which Slack conversation

All of this is processed locally on your machine into structured, searchable, and semantically embedded materials. No raw audio is stored. No screenshots leave your device. Everything runs through on-device models that extract meaning, identify topics, tag collaborators, and generate summaries.

### What This Means for Your Agents

When your Cursor agent can call Pieces MCP tools, it stops being a stateless code assistant and starts being a colleague who was there for everything:

**Context restoration across sessions.** You close your laptop Friday evening. Monday morning, you ask your agent "What was I working on Friday afternoon?" and it retrieves the exact summaries, clipboard copies, and audio transcriptions from that session. No more staring at git log trying to reconstruct your mental state.

**Decision recall.** You're implementing a caching layer and can't remember why the team chose Redis over Memcached. Your agent searches your meeting transcriptions and Copilot conversations and finds the exact discussion where the decision was made, including the performance benchmarks someone mentioned.

**Cross-application intelligence.** Your agent can see that you copied a SQL query from DataGrip, pasted it into a Slack message to your DBA, then later opened a Chrome tab to the PostgreSQL docs on indexing. It connects the dots across applications that would otherwise be completely siloed.

**Research retrieval.** You spent two hours last Tuesday researching WebSocket libraries. Your agent finds every page you visited, every code snippet you copied, and every note you made -- even if you never saved any of it explicitly.

**Meeting context in code.** You're in Cursor writing an API endpoint. Your agent searches audio transcriptions from this morning's standup and finds that your PM mentioned the endpoint needs to support pagination with cursor-based navigation, not offset-based. Context that would otherwise be lost in the ether of a 15-minute meeting.

**Standup and reporting generation.** Your agent generates your daily standup by querying yesterday's workstream summaries. It knows which PRs you reviewed, which files you edited, which meetings you attended, and which research you did -- because Pieces captured all of it.

**Persistent memory across agents.** You use `create_pieces_memory` in Claude Code to save a detailed record of a debugging session. Later, you ask your Cursor agent about it using `ask_pieces_ltm` and it retrieves the full context. Memories persist across agents, sessions, and time.

**Collaboration awareness.** Your agent can find which colleagues are associated with specific work, what discussions happened with specific people, and what organizational teams are connected to specific projects. It understands the social graph of your work.

### The Fundamental Shift

Without Pieces MCP, your agents operate in a narrow window: the current file, the current conversation, maybe the current project. With Pieces MCP, your agents operate across your entire work history. They can look back days, weeks, or months. They can search by keyword or by meaning. They can filter by application, by time, by person, by event type. They can find things you forgot you ever saw.

This is the difference between an AI assistant that helps you write code and one that helps you think.

---

## Overview

The Pieces MCP server exposes **39 tools** across six categories. These tools give AI agents and end users access to the user's long-term memory, captured workflow activity, Copilot conversations, code bookmarks, contacts, and more.

| Category | Count | Purpose |
|----------|-------|---------|
| LTM / Memory | 2 | Query or persist long-term memories |
| Full-Text Search | 14 | Keyword search across every material type |
| Vector / Semantic Search | 5 | Meaning-based search using AI embeddings |
| Filter & Enumerate | 1 | List material UUIDs by time and config filters |
| ML Capabilities | 1 | AI-powered temporal extraction |
| Batch Snapshot | 16 | Retrieve full objects by UUID (1-100 at a time) |

> **Introduced in Pieces 5.0.3 (PiecesOS 12.3.8):** This release expanded the Pieces MCP server from the original `ask_pieces_ltm` and `create_pieces_memory` tools to the full suite documented here — adding 14 full-text search tools, 5 vector search tools, `material_identifiers`, `extract_temporal_range`, and 16 batch snapshot tools. See [What's New in Pieces 5.0.3](../../releases/Whats%20New%20in%20Pieces%205.0.3.md#expanded-mcp-server-richer-long-term-memory-access-in-cursor-claude-code--more) for details.

---

## Core Workflow Pattern

Most tasks follow a two-step pattern: **search or identify**, then **retrieve details**.

```
Step 1 — Find identifiers
    Use a search tool or material_identifiers
    to get a list of UUIDs matching your criteria.

Step 2 — Retrieve full objects
    Pass those UUIDs to the corresponding
    batch_snapshot tool to get complete data.
```

**Example flow:**

```
tags_full_text_search(query: "react")
  --> returns [{tag: {...}, similarity: 0.95}, ...]

                    OR

material_identifiers(material_type: "TAGS")
  --> returns {identifiers: ["uuid-1", "uuid-2", ...]}

                    THEN

tags_batch_snapshot(identifiers: ["uuid-1", "uuid-2"])
  --> returns full Tag objects with all fields
```

Vector search tools return identifiers and scores only (no full objects), so a batch snapshot call is always the expected follow-up.

---

## Temporal Filtering

Most search and listing tools accept optional `created` and `updated` parameters to narrow results by date range. Both use the same structure:

```json
{
  "created": {
    "from": "2025-02-01T00:00:00Z",
    "to": "2025-02-18T23:59:59Z"
  }
}
```

- `from` and `to` are ISO 8601 UTC timestamps.
- Either field can be omitted for an open-ended range.
- Use the `extract_temporal_range` tool to convert natural language like "yesterday" or "last week" into these UTC ranges before passing them to other tools.

---

## LTM and Memory Tools

These two tools are the highest-level entry points to your Long-Term Memory. They are the tools an agent should reach for first when it needs historical context or wants to save something important for later.

**`ask_pieces_ltm`** is the "just ask" tool. When a user says "What was I working on last week?" or "Find that conversation about the API redesign," the agent passes the natural language question directly to Pieces. Pieces handles the retrieval, ranking, and scoring internally, returning the most relevant summaries and raw events. This is the fastest path from a user's question to historical context -- no need to manually choose between full-text search, vector search, or temporal filtering. Pieces does it all behind the scenes.

**`create_pieces_memory`** is the "save this for later" tool. Agents should use this to persist important context that the user (or a future agent) will want to recall. Debugging breakthroughs, architectural decisions, deployment notes, meeting summaries, research findings -- anything worth remembering. These memories are embedded semantically, so they surface later through both keyword and meaning-based searches. This is how agents communicate across sessions: one agent saves a memory, another retrieves it days or weeks later.

---

### ask_pieces_ltm

Query the user's long-term memory to retrieve historical context from workstream events and summaries.

**Availability:** MCP

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `question` | string | Yes | The main question to search for in the user's history |
| `topics` | string[] | No | Topical keywords to narrow results (e.g., `["python", "react"]`) |
| `open_files` | string[] | No | Currently open file paths for additional context |
| `application_sources` | string[] | No | Filter by application names (e.g., `["chrome", "vscode"]`) |
| `chat_llm` | string | Yes | LLM model name for response generation (e.g., `"gpt-4o-mini"`) |
| `related_questions` | string[] | No | Supplementary questions to enhance search coverage |
| `connected_client` | string | No | Client identifier (e.g., `"Cursor"`, `"Claude"`) |

**Returns:** A JSON string containing `summaries` and `events` arrays, each with `created`, `score`, `combined_string`, and event-specific fields like `browser_url`, `app_title`, `window_title`.

**Agent instructions:** Use `ask_pieces_ltm` from the Pieces MCP to ask natural language questions about the user's past work. This returns ranked workstream summaries and events with relevance scores. Useful for recalling what the user worked on, finding past decisions, or retrieving context from previous sessions.

```json
{
  "name": "ask_pieces_ltm",
  "arguments": {
    "question": "What authentication changes did I make last week?",
    "topics": ["auth", "jwt", "security"],
    "application_sources": ["vscode"],
    "chat_llm": "gpt-4o-mini"
  }
}
```

---

### create_pieces_memory

Persist a detailed, structured memory into Pieces that can be retrieved later via `ask_pieces_ltm` or search tools.

**Availability:** MCP

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `summary` | string | Yes | Detailed markdown-formatted narrative of the memory |
| `summary_description` | string | Yes | Concise title or summary (1-2 sentences) |
| `project` | string | No | Absolute path to the project root directory |
| `files` | string[] | No | Absolute file or folder paths to associate |
| `externalLinks` | string[] | No | URLs and external references to associate |
| `connected_client` | string | No | Client identifier |

**Returns:** A success message confirming the memory was created, with guidance on how to query it back.

**Agent instructions:** Use `create_pieces_memory` from the Pieces MCP to save important context, decisions, or work summaries as permanent memories. This persists the data as a workstream summary with embeddings for future semantic retrieval. Useful for capturing architectural decisions, debugging sessions, deployment notes, or any context the user may want to recall later.

```json
{
  "name": "create_pieces_memory",
  "arguments": {
    "summary": "Resolved performance bottleneck in the search API by adding a Redis caching layer. Response times dropped from 800ms to 120ms. Cache TTL set to 1 hour with invalidation on product updates.",
    "summary_description": "Search API Redis caching implementation",
    "project": "/Users/dev/my-project",
    "files": ["/Users/dev/my-project/src/cache/redis.ts"],
    "externalLinks": ["https://github.com/org/repo/pull/42"]
  }
}
```

---

## Full-Text Search Tools

Full-text search tools find materials by keyword matching. They return full objects (not just identifiers) along with similarity scores and exact-match flags. All support optional temporal filtering via `created` and `updated`.

**When to use full-text search vs. `ask_pieces_ltm`:** Use `ask_pieces_ltm` when the user asks a general question and you want Pieces to handle the retrieval strategy. Use individual full-text search tools when you need precision -- searching a specific material type, filtering by application or context type, or combining multiple targeted searches in parallel for a comprehensive answer.

**When to use full-text search vs. vector search:** Full-text search matches exact keywords. Use it when you know the specific terms the user used -- function names, error messages, project names, URLs, colleague names. Vector search matches meaning. Use it when the user describes a concept that may have been captured with different words. The two approaches are complementary; agents should use both when thoroughness matters.

**Why 14 separate search tools?** Each tool searches a different material type with type-specific parameters and return shapes. This gives agents surgical precision: search only workstream events from Chrome, search only audio transcriptions, search only code bookmarks, search only conversations with the Copilot. The granularity prevents information overload and lets agents compose targeted multi-tool workflows.

The most commonly used full-text search tools for agentic workflows:

- **`workstream_summaries_full_text_search`** -- The go-to for "What did I work on?" questions. Summaries are AI-generated every ~20 minutes and capture the essence of what the user was doing, including which apps, files, and topics were involved.
- **`workstream_events_full_text_search`** -- The raw activity layer. This is where you find the actual clipboard copies, OCR'd screenshots, and audio transcriptions. Invaluable when the user needs the exact text they copied, the exact error message they saw, or the exact thing someone said in a meeting.
- **`conversations_full_text_search`** and **`conversation_messages_full_text_search`** -- Past Copilot conversations. When the user asks "Didn't I already solve this?" or "What did the AI suggest for that bug?", these tools find it.
- **`annotations_full_text_search`** -- Notes, summaries, descriptions, and comments attached to any material. This is the meta-layer that captures explanations and documentation.

---

### workstream_summaries_full_text_search

Search AI-generated work session summaries by keyword.

**Availability:** Both (MCP and OpenCode)

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-1000 chars) |
| `limit` | integer | No | 10 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `summary` object (with associated annotations), `similarity` score, and `exact` match flag.

**Agent instructions:** Use `workstream_summaries_full_text_search` from the Pieces MCP to find work session summaries matching specific keywords. This returns full summary objects with annotations and relevance scores. Useful for finding past work sessions about a topic, locating summaries that mention specific technologies or tasks, or discovering what the user accomplished during a time period.

```json
{
  "name": "workstream_summaries_full_text_search",
  "arguments": {
    "query": "database migration",
    "limit": 10
  }
}
```

---

### conversations_full_text_search

Hybrid search across Copilot conversation names, message content, and annotation summaries simultaneously.

**Availability:** MCP only

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-1000 chars) |
| `limit` | integer | No | 25 | Max conversations to return (1-50) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a `conversation` object (messages removed to avoid bloat), `matched_messages` with content and scores, `matched_annotations` with content and scores, and counts.

**Agent instructions:** Use `conversations_full_text_search` from the Pieces MCP to find Copilot conversations where a topic was discussed. This returns conversations with matched messages and annotations highlighted separately. Useful for finding past AI-assisted discussions about a feature, locating code examples shared in chat, or rediscovering solutions discussed with the Copilot.

```json
{
  "name": "conversations_full_text_search",
  "arguments": {
    "query": "React hooks performance",
    "limit": 10
  }
}
```

---

### tags_full_text_search

Search user-created labels and tags by keyword.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-500 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `tag` object, `similarity` score, and `exact` match flag.

**Agent instructions:** Use `tags_full_text_search` from the Pieces MCP to find tags matching a keyword. This returns full tag objects with relevance scores. Useful for discovering how the user has categorized their work, finding related labels, or checking if a tag already exists before creating content.

```json
{
  "name": "tags_full_text_search",
  "arguments": {
    "query": "typescript"
  }
}
```

---

### annotations_full_text_search

Search notes, summaries, comments, and other annotations by keyword, with optional type filtering.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-1000 chars) |
| `limit` | integer | No | 50 | Max results (1-200) |
| `annotation_type` | string | No | - | Filter by type: `SUMMARY`, `DESCRIPTION`, `COMMENT`, `DOCUMENTATION`, `EXPLANATION`, `CODE`, `GENERATED_CODE`, `GIT_COMMIT`, `KNOWLEDGE_GRAPH`, etc. |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `annotation` object, `similarity` score, and `exact` match flag. When a type filter is applied, it is reflected in the response metadata.

**Agent instructions:** Use `annotations_full_text_search` from the Pieces MCP to find notes, summaries, or comments matching keywords. This returns full annotation objects with relevance scores. Useful for finding documentation notes, git commit annotations, code explanations, or any textual metadata the user has attached to their materials. Use the `annotation_type` filter to narrow to specific categories.

```json
{
  "name": "annotations_full_text_search",
  "arguments": {
    "query": "API rate limiting",
    "annotation_type": "DOCUMENTATION",
    "limit": 20
  }
}
```

---

### persons_full_text_search

Search contacts and collaborators across six identity fields (email, name, username).

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-500 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `person` object, `similarity` score, and `exact` match flag.

**Agent instructions:** Use `persons_full_text_search` from the Pieces MCP to find people by name, email, or username. This returns full person objects with relevance scores. Useful for finding collaborators associated with specific work, locating contacts by partial name or email, or discovering who was involved in past projects.

```json
{
  "name": "persons_full_text_search",
  "arguments": {
    "query": "john@example.com"
  }
}
```

---

### anchors_full_text_search

Hybrid search across code bookmark names and their anchor point file paths simultaneously.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-1000 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `anchor` object (includes anchor points), `anchor_point_count`, `similarity` score, and `exact` match flag.

**Agent instructions:** Use `anchors_full_text_search` from the Pieces MCP to find code bookmarks by name or file path. This returns full anchor objects with their associated file locations. Useful for finding saved code references, locating bookmarked files by path, or discovering which code locations the user has marked as important.

```json
{
  "name": "anchors_full_text_search",
  "arguments": {
    "query": "authentication middleware"
  }
}
```

---

### workstream_events_full_text_search

Multi-field search across captured activity records (clipboard, screenshots/OCR, audio transcriptions) with application, window, URL, and context type filtering.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-1000 chars) |
| `limit` | integer | No | 50 | Max results (1-200) |
| `application` | string | No | - | Filter by application name (partial match) |
| `window_title` | string | No | - | Filter by window/tab title (partial match) |
| `url` | string | No | - | Filter by browser URL (partial match) |
| `context_type` | string | No | - | Filter by event type: `CLIPBOARD`, `VISION`, `AUDIO` |
| `audio_type` | string | No | - | Filter audio events by device: `INPUT`, `OUTPUT` |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `event` object, extracted `material_config` (application, window_title, url, type, audio_type), `similarity` score, and `exact` match flag.

**Agent instructions:** Use `workstream_events_full_text_search` from the Pieces MCP to search through captured workflow activity. This returns full event objects with application context metadata. Useful for finding clipboard content copied from a specific app, locating screenshots containing specific text (via OCR), finding audio transcriptions mentioning a topic, or filtering activity by application and window context. Searches across 11 fields including descriptions, window titles, URLs, clipboard content, OCR text, and audio transcriptions.

```json
{
  "name": "workstream_events_full_text_search",
  "arguments": {
    "query": "API endpoint design",
    "application": "Google Chrome",
    "context_type": "CLIPBOARD",
    "limit": 25
  }
}
```

---

### websites_full_text_search

Dual-field search across saved URL addresses and their display names.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-500 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `website` object, `similarity` score, and `exact` match flag.

**Agent instructions:** Use `websites_full_text_search` from the Pieces MCP to find saved URLs by address or name. This returns full website objects with relevance scores. Useful for finding documentation links, API references, GitHub repositories, or any external URLs the user has saved or that were captured from their workflow.

```json
{
  "name": "websites_full_text_search",
  "arguments": {
    "query": "github.com/pieces-app"
  }
}
```

---

### hints_full_text_search

Search AI-generated follow-up suggestions by text content.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-500 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `hint` object (embedding vectors cleared), `similarity` score, and `exact` match flag.

**Agent instructions:** Use `hints_full_text_search` from the Pieces MCP to find AI-generated follow-up suggestions matching a keyword. This returns hint objects containing suggested questions. Useful for discovering what follow-up questions Pieces suggested after conversations or work summaries, finding related exploration paths, or identifying topics the system flagged as worth revisiting.

```json
{
  "name": "hints_full_text_search",
  "arguments": {
    "query": "performance optimization"
  }
}
```

---

### models_full_text_search

Multi-field search across AI/ML model configurations (name, provider, foundation, description, and AWS Bedrock fields).

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-500 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `model` object, `similarity` score, and `exact` match flag.

**Agent instructions:** Use `models_full_text_search` from the Pieces MCP to find AI/ML models by name, provider, or description. This returns full model configuration objects. Useful for listing available models, finding models from a specific provider (e.g., "anthropic"), or discovering which models support a particular capability.

```json
{
  "name": "models_full_text_search",
  "arguments": {
    "query": "claude"
  }
}
```

---

### wpe_sources_full_text_search

Search application sources extracted from workflow activity, across readable names and raw application/window/URL fields.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-500 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `wpe_source` object, `similarity` score, and `exact` match flag.

**Agent instructions:** Use `wpe_sources_full_text_search` from the Pieces MCP to find application sources that were detected during workflow monitoring. This returns source objects including readable application names and raw identifiers. Useful for discovering which applications the user has been working in, finding sources by application bundle ID, or checking if a specific app is being tracked.

```json
{
  "name": "wpe_sources_full_text_search",
  "arguments": {
    "query": "Visual Studio Code"
  }
}
```

---

### wpe_source_windows_full_text_search

Search window title contexts captured during workflow monitoring.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-500 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `wpe_source_window` object, `similarity` score, and `exact` match flag.

**Agent instructions:** Use `wpe_source_windows_full_text_search` from the Pieces MCP to find specific window contexts by title. This returns window objects with their names and timestamps. Useful for finding which browser tabs, IDE files, or application windows the user had open, or locating activity from a specific document or webpage.

```json
{
  "name": "wpe_source_windows_full_text_search",
  "arguments": {
    "query": "Pull Request #42"
  }
}
```

---

### entities_full_text_search

Search organizations and teams by name.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-500 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `entity` object, `similarity` score, and `exact` match flag.

**Agent instructions:** Use `entities_full_text_search` from the Pieces MCP to find organizations or teams by name. This returns entity objects with type and distribution model information. Useful for looking up organizational memberships or team structures.

```json
{
  "name": "entities_full_text_search",
  "arguments": {
    "query": "engineering"
  }
}
```

---

### conversation_messages_full_text_search

Search individual Copilot chat messages by content.

**Availability:** MCP only

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Search query (1-500 chars) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing a full `message` object, `similarity` score, and `exact` match flag.

**Agent instructions:** Use `conversation_messages_full_text_search` from the Pieces MCP to find specific messages within Copilot conversations. This returns individual message objects with their content and role (USER, ASSISTANT, SYSTEM). Useful for finding a specific code snippet shared in chat, locating an answer the Copilot gave about a topic, or searching across all conversations at the message level for granular results.

```json
{
  "name": "conversation_messages_full_text_search",
  "arguments": {
    "query": "useEffect cleanup function",
    "limit": 15
  }
}
```

---

## Vector / Semantic Search Tools

Vector search tools use AI embeddings to find content by meaning rather than exact keywords. A query like "database optimization" will match materials about "SQL tuning", "query performance", and "indexing strategies" even without shared words.

These tools return **identifiers and similarity scores only** (not full objects). Always follow up with the corresponding `batch_snapshot` tool to retrieve complete data.

**Why this matters for agents:** Users rarely describe their past work with the same words they used at the time. You might ask "How did I handle authentication?" but the actual clipboard copy said "JWT token validation middleware." Full-text search would miss that connection. Vector search finds it because the embeddings understand that authentication and JWT token validation are semantically related.

**The two-step pattern is intentional.** Vector search returns lightweight identifier+score pairs to keep responses fast and token-efficient. The agent then selectively retrieves full objects only for the top results using batch snapshot tools. This prevents flooding the context window with irrelevant detail.

**Threshold tuning:** Use ~0.5 for exploratory "show me everything even loosely related" searches. Use ~0.7 for focused results. Use ~0.9 only when you need near-exact semantic matches. When in doubt, start broad and let the agent filter by relevance.

---

### materials_vector_search

Generic semantic search across multiple material types. Requires specifying which type to search.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Natural language query (1-1000000 chars) |
| `material_type` | string | Yes | - | Type to search: `WORKSTREAM_SUMMARIES`, `HINTS`, `TAGS`, `WORKSTREAM_EVENTS` |
| `threshold` | number | No | - | Minimum similarity score (0.0-1.0). Use ~0.5 for broad, ~0.8 for strict |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results, each containing an `identifier` (UUID) and `score` (similarity), plus `next_steps` guidance for follow-up.

**Agent instructions:** Use `materials_vector_search` from the Pieces MCP to perform semantic similarity search across a specified material type. This returns identifiers with similarity scores sorted by relevance. Useful when you need to search a specific material type by meaning rather than exact keywords. Follow up with the appropriate batch snapshot tool to get full details. Prefer the type-specific vector search tools (e.g., `tags_vector_search`) when you know the type ahead of time, as they simplify the call.

```json
{
  "name": "materials_vector_search",
  "arguments": {
    "query": "microservices architecture patterns",
    "material_type": "WORKSTREAM_SUMMARIES",
    "threshold": 0.6,
    "limit": 15
  }
}
```

---

### workstream_summaries_vector_search

Semantic search specifically for work session summaries.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Natural language query (1-1000000 chars) |
| `threshold` | number | No | - | Minimum similarity score (0.0-1.0) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results with `identifier` and `score`, plus `next_steps`.

**Agent instructions:** Use `workstream_summaries_vector_search` from the Pieces MCP to find semantically similar work session summaries. This returns UUIDs with similarity scores. Useful for finding conceptually related work even when different terminology was used, discovering past sessions that tackled similar problems, or exploring the user's work history by theme. Follow up with `workstream_summaries_batch_snapshot` to retrieve full summary details.

```json
{
  "name": "workstream_summaries_vector_search",
  "arguments": {
    "query": "CI/CD pipeline improvements",
    "limit": 10
  }
}
```

---

### hints_vector_search

Semantic search for AI-generated follow-up suggestions.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Natural language query (1-1000000 chars) |
| `threshold` | number | No | - | Minimum similarity score (0.0-1.0) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results with `identifier` and `score`, plus `next_steps`.

**Agent instructions:** Use `hints_vector_search` from the Pieces MCP to discover follow-up suggestions related to a concept. This returns hint UUIDs with similarity scores. Useful for finding what questions Pieces previously suggested about a topic, discovering related exploration paths across conversations, or identifying patterns in the user's learning journey. Follow up with `hints_batch_snapshot` for full hint text.

```json
{
  "name": "hints_vector_search",
  "arguments": {
    "query": "error handling best practices"
  }
}
```

---

### tags_vector_search

Semantic search for user-created labels and categories.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Natural language query (1-1000000 chars) |
| `threshold` | number | No | - | Minimum similarity score (0.0-1.0) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results with `identifier` and `score`, plus `next_steps`.

**Agent instructions:** Use `tags_vector_search` from the Pieces MCP to find semantically similar tags. This returns tag UUIDs with similarity scores. Useful for discovering related categorizations the user has created, finding tags that overlap conceptually, or suggesting existing tags that match new content. Follow up with `tags_batch_snapshot` for full tag details.

```json
{
  "name": "tags_vector_search",
  "arguments": {
    "query": "frontend testing"
  }
}
```

---

### workstream_events_vector_search

Semantic search for captured workflow activity with optional context type filtering.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Natural language query (1-1000000 chars) |
| `threshold` | number | No | - | Minimum similarity score (0.0-1.0) |
| `limit` | integer | No | 25 | Max results (1-100) |
| `context_type` | string | No | - | Filter by event type: `CLIPBOARD`, `VISION`, `AUDIO` |
| `audio_type` | string | No | - | Filter audio events: `INPUT`, `OUTPUT` |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |

**Returns:** List of results with `identifier` and `score`, plus `next_steps`.

**Agent instructions:** Use `workstream_events_vector_search` from the Pieces MCP to find activity events semantically related to a concept. This returns event UUIDs with similarity scores. Useful for finding clipboard copies, screenshots, or audio transcriptions related to a topic even when different words were used. Use `context_type` to narrow to a specific capture channel. Follow up with `workstream_events_batch_snapshot` for full event details.

```json
{
  "name": "workstream_events_vector_search",
  "arguments": {
    "query": "deployment configuration",
    "context_type": "CLIPBOARD",
    "limit": 20
  }
}
```

---

## Filter and Enumerate Tools

While search tools require a query, `material_identifiers` lets agents enumerate materials purely by type, time range, and configuration filters. This is essential for time-based workflows: "Get all workstream summaries from today," "List every clipboard event from VS Code this morning," or "Count how many tags were created this week."

**Why agents need this:** Sometimes the question isn't "find something matching X" but rather "give me everything from a time window." Standup generation, time breakdowns, daily recaps, and activity audits all start with `material_identifiers` scoped to a time range, followed by batch snapshot retrieval for the full objects.

---

### material_identifiers

List UUIDs for any of 16 material types using time-based and configuration filters. No search query required.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `material_type` | string | Yes | - | See supported types below |
| `limit` | integer | No | 100 | Max identifiers (1-1000) |
| `created` | object | No | - | Temporal filter on creation date |
| `updated` | object | No | - | Temporal filter on last update |
| `configurations` | object | No | - | Material-specific filters (WORKSTREAM_EVENTS only) |

**Supported material types (16):**

| Type | Description |
|------|-------------|
| `WORKSTREAM_SUMMARIES` | AI-generated work session summaries |
| `WORKSTREAM_EVENTS` | Captured activity records (clipboard, vision, audio) |
| `HINTS` | AI-generated follow-up suggestions |
| `TAGS` | User-created labels |
| `CONVERSATIONS` | Copilot chat history |
| `CONVERSATION_MESSAGES` | Individual chat messages |
| `ANNOTATIONS` | Notes, summaries, comments |
| `ANCHORS` | Code bookmarks |
| `ANCHOR_POINTS` | Specific file path locations |
| `RANGES` | Temporal ranges |
| `PERSONS` | Collaborators and contacts |
| `WEBSITES` | External URL references |
| `MODELS` | AI model configurations |
| `ENTITIES` | Organizations and teams |
| `WORKSTREAM_PATTERN_ENGINE_SOURCES` | Application context sources |
| `WORKSTREAM_PATTERN_ENGINE_SOURCE_WINDOWS` | Window context |

**Workstream events configuration filters:**

When `material_type` is `WORKSTREAM_EVENTS`, use the `configurations` parameter:

```json
{
  "configurations": {
    "workstream_events": {
      "context": {
        "type": "CLIPBOARD",
        "application": "Visual Studio Code",
        "window": "main.dart",
        "url": null
      }
    }
  }
}
```

Context types: `CLIPBOARD`, `VISION`, `AUDIO`

**Returns:** `material_type`, `count`, `identifiers` (array of UUIDs), `limit`, and `next_step` (guidance on which batch snapshot tool to call next).

**Agent instructions:** Use `material_identifiers` from the Pieces MCP to list or enumerate materials without a search query. This returns UUIDs that can be passed to the corresponding batch snapshot tool. Useful for listing all materials of a type, filtering by time range (e.g., "all tags created today"), or enumerating workstream events from a specific application. Always follow up with the appropriate `*_batch_snapshot` tool to get full object details.

```json
{
  "name": "material_identifiers",
  "arguments": {
    "material_type": "WORKSTREAM_SUMMARIES",
    "created": {
      "from": "2025-02-17T00:00:00Z",
      "to": "2025-02-18T23:59:59Z"
    },
    "limit": 50
  }
}
```

---

## ML Capabilities Tools

**`extract_temporal_range`** is a utility that every agent should call as a pre-processing step whenever the user mentions time in natural language. Users say "yesterday," "last week," "this morning," "the past 3 hours," or "back in August." These need to be converted into precise UTC timestamps before they can be used as `created` or `updated` filters in search and listing tools. This tool handles that conversion using AI/ML models that understand natural language time expressions and the user's timezone context. Without it, agents would have to hardcode timezone logic and calendar math -- a fragile and error-prone approach.

---

### extract_temporal_range

Convert natural language time expressions into precise UTC ISO 8601 timestamp ranges using AI/ML models.

**Availability:** Both

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | - | Natural language with time phrases (1-300 chars) |

**Returns:** `query`, `count`, and `ranges` (array of `{from, to}` objects in ISO 8601 UTC). If no temporal phrases are detected, returns an empty array. If ranges extend into the future, they are truncated to current time with a `processing_note`.

**Agent instructions:** Use `extract_temporal_range` from the Pieces MCP to convert human time expressions into UTC timestamp ranges. This returns structured `{from, to}` pairs suitable for passing to the `created` or `updated` parameters of search and listing tools. Useful as a pre-processing step when the user says things like "yesterday", "last week", or "the past 3 hours". Note that results are AI-generated and may not always be 100% accurate.

```json
{
  "name": "extract_temporal_range",
  "arguments": {
    "query": "what did I work on last Tuesday afternoon"
  }
}
```

Example output:
```json
{
  "query": "what did I work on last Tuesday afternoon",
  "count": 1,
  "ranges": [
    {
      "from": "2025-02-11T12:00:00.000Z",
      "to": "2025-02-11T17:59:59.000Z"
    }
  ]
}
```

---

## Batch Snapshot Tools

Batch snapshot tools retrieve full material objects by UUID. They all follow the same pattern:

- Accept an `identifiers` array of 1-100 UUIDs
- Return the found objects plus a `missing_ids` list for any UUIDs that were not found
- Are the standard follow-up after any search or `material_identifiers` call

**Why batch snapshots exist as separate tools:** This design separates discovery (search/filter) from retrieval (snapshot). Search tools can return many results efficiently (just IDs and scores), and the agent selectively retrieves full objects only for the results that matter. This keeps responses fast, avoids token bloat, and gives agents control over how much detail they pull. An agent generating a standup might retrieve 10 summary snapshots. An agent answering a narrow question might only need 1-2.

**How agents should use them:** After any search or `material_identifiers` call, take the top-N identifiers by relevance score and pass them to the matching `*_batch_snapshot` tool. The naming is consistent: `tags_full_text_search` pairs with `tags_batch_snapshot`, `workstream_events_vector_search` pairs with `workstream_events_batch_snapshot`, and so on. Each tool returns the complete object with all fields, associations, and metadata.

---

### workstream_summaries_batch_snapshot

Retrieve full workstream summary objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full summary objects), and `missing_ids` (if any).

**Agent instructions:** Use `workstream_summaries_batch_snapshot` from the Pieces MCP to retrieve complete workstream summary details by ID. This returns full summary objects including content, annotations, and metadata. Use this after `workstream_summaries_full_text_search`, `workstream_summaries_vector_search`, or `material_identifiers` to get the complete data for results.

```json
{
  "name": "workstream_summaries_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1", "uuid-2", "uuid-3"]
  }
}
```

---

### conversations_batch_snapshot

Retrieve full conversation objects by UUID.

**Availability:** MCP only

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full conversation objects), and `missing_ids`.

**Agent instructions:** Use `conversations_batch_snapshot` from the Pieces MCP to retrieve complete Copilot conversation details by ID. This returns full conversation objects including metadata and message references. Use this after `conversations_full_text_search` or `material_identifiers` to get the complete data for results.

```json
{
  "name": "conversations_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1"]
  }
}
```

---

### tags_batch_snapshot

Retrieve full tag objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full tag objects), and `missing_ids`.

**Agent instructions:** Use `tags_batch_snapshot` from the Pieces MCP to retrieve complete tag details by ID. This returns full tag objects with all metadata. Use this after `tags_full_text_search`, `tags_vector_search`, or `material_identifiers`.

```json
{
  "name": "tags_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1", "uuid-2"]
  }
}
```

---

### annotations_batch_snapshot

Retrieve full annotation objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full annotation objects), and `missing_ids`.

**Agent instructions:** Use `annotations_batch_snapshot` from the Pieces MCP to retrieve complete annotation details by ID. This returns full annotation objects including content, type, and associations. Use this after `annotations_full_text_search` or `material_identifiers`.

```json
{
  "name": "annotations_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1", "uuid-2"]
  }
}
```

---

### persons_batch_snapshot

Retrieve full person objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full person objects), and `missing_ids`.

**Agent instructions:** Use `persons_batch_snapshot` from the Pieces MCP to retrieve complete person/contact details by ID. This returns full person objects with name, email, username, and associations. Use this after `persons_full_text_search` or `material_identifiers`.

```json
{
  "name": "persons_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1"]
  }
}
```

---

### anchors_batch_snapshot

Retrieve full anchor (code bookmark) objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full anchor objects including name, type, watch status, timestamps), and `missing_ids`.

**Agent instructions:** Use `anchors_batch_snapshot` from the Pieces MCP to retrieve complete code bookmark details by ID. This returns anchor objects with names, types (FILE, DIRECTORY, etc.), and associated anchor points. Use this after `anchors_full_text_search` or `material_identifiers`.

```json
{
  "name": "anchors_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1", "uuid-2"]
  }
}
```

---

### anchor_points_batch_snapshot

Retrieve full anchor point (file path location) objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full anchor point objects including file path, platform info, line ranges), and `missing_ids`.

**Agent instructions:** Use `anchor_points_batch_snapshot` from the Pieces MCP to retrieve specific file path locations within code bookmarks. This returns anchor point objects with full file paths and optional line ranges. Use this after getting anchor point IDs from anchor details or related materials.

```json
{
  "name": "anchor_points_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1"]
  }
}
```

---

### workstream_events_batch_snapshot

Retrieve full workstream event (activity capture) objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full event objects including clipboard/vision/audio content, application name, window title, browser URL), and `missing_ids`.

**Agent instructions:** Use `workstream_events_batch_snapshot` from the Pieces MCP to retrieve complete activity event details by ID. This returns full event objects with the captured content (clipboard text, OCR output, audio transcription) and application context. Use this after `workstream_events_full_text_search`, `workstream_events_vector_search`, or `material_identifiers`.

```json
{
  "name": "workstream_events_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1", "uuid-2", "uuid-3"]
  }
}
```

---

### hints_batch_snapshot

Retrieve full hint (AI follow-up suggestion) objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full hint objects including suggestion text, type, generating model), and `missing_ids`.

**Agent instructions:** Use `hints_batch_snapshot` from the Pieces MCP to retrieve complete follow-up suggestion details by ID. This returns hint objects with the suggested question text, hint type, and the AI model that generated them. Use this after `hints_full_text_search`, `hints_vector_search`, or `material_identifiers`.

```json
{
  "name": "hints_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1", "uuid-2"]
  }
}
```

---

### models_batch_snapshot

Retrieve full AI/ML model configuration objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full model objects including name, provider, foundation, usage type, cloud/local status), and `missing_ids`.

**Agent instructions:** Use `models_batch_snapshot` from the Pieces MCP to retrieve complete AI model configuration details by ID. This returns model objects with provider info, capabilities, and status. Use this after `models_full_text_search` or `material_identifiers`.

```json
{
  "name": "models_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1"]
  }
}
```

---

### ranges_batch_snapshot

Retrieve full temporal range objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full range objects including `from`/`to` timestamps, type BETWEEN or CONTINUOUS), and `missing_ids`.

**Agent instructions:** Use `ranges_batch_snapshot` from the Pieces MCP to retrieve temporal range details by ID. This returns range objects defining time windows used for grounding conversations and summaries. Use this after getting range IDs from conversation or summary details.

```json
{
  "name": "ranges_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1"]
  }
}
```

---

### websites_batch_snapshot

Retrieve full website objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full website objects including URL, name, text content, timestamps), and `missing_ids`.

**Agent instructions:** Use `websites_batch_snapshot` from the Pieces MCP to retrieve complete website/URL details by ID. This returns website objects with URLs, display names, and associated content. Use this after `websites_full_text_search` or `material_identifiers`.

```json
{
  "name": "websites_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1", "uuid-2"]
  }
}
```

---

### entities_batch_snapshot

Retrieve full entity (organization/team) objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full entity objects including name, type, distribution model), and `missing_ids`.

**Agent instructions:** Use `entities_batch_snapshot` from the Pieces MCP to retrieve complete organization or team details by ID. This returns entity objects with name, type, and membership information. Use this after `entities_full_text_search` or `material_identifiers`.

```json
{
  "name": "entities_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1"]
  }
}
```

---

### conversation_messages_batch_snapshot

Retrieve full conversation message objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full message objects including content, role, sentiment, model used), and `missing_ids`.

**Agent instructions:** Use `conversation_messages_batch_snapshot` from the Pieces MCP to retrieve complete chat message details by ID. This returns message objects with content, role (USER/ASSISTANT/SYSTEM), sentiment analysis, and the AI model used. Use this after `conversation_messages_full_text_search` or `material_identifiers`.

```json
{
  "name": "conversation_messages_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1", "uuid-2"]
  }
}
```

---

### wpe_sources_batch_snapshot

Retrieve full WPE (Workstream Pattern Engine) application source objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full source objects including readable application name, raw context with bundle ID/executable, window title, URL, and filter status), and `missing_ids`.

**Agent instructions:** Use `wpe_sources_batch_snapshot` from the Pieces MCP to retrieve complete application source details by ID. This returns source objects with readable names, raw identifiers, and filter status. Use this after `wpe_sources_full_text_search` or `material_identifiers`.

```json
{
  "name": "wpe_sources_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1"]
  }
}
```

---

### wpe_source_windows_batch_snapshot

Retrieve full WPE source window (window context) objects by UUID.

**Availability:** Both

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifiers` | string[] | Yes | Array of UUIDs (1-100) |

**Returns:** `material_type`, `count`, `requested`, `items` (full window objects including window name/title and timestamps), and `missing_ids`.

**Agent instructions:** Use `wpe_source_windows_batch_snapshot` from the Pieces MCP to retrieve complete window context details by ID. This returns window objects with titles and timestamps. Use this after `wpe_source_windows_full_text_search` or `material_identifiers`.

```json
{
  "name": "wpe_source_windows_batch_snapshot",
  "arguments": {
    "identifiers": ["uuid-1"]
  }
}
```

---

## Common Workflow Examples

These examples show multi-tool chains that agents can execute to answer real user questions. Each demonstrates how the tools compose together to turn a natural language question into a precise, evidence-backed answer.

### 1. Find everything the user worked on yesterday

```
Step 1: Convert "yesterday" to a UTC range
  extract_temporal_range(query: "yesterday")
  --> { ranges: [{ from: "2025-02-17T00:00:00Z", to: "2025-02-17T23:59:59Z" }] }

Step 2: List workstream summary IDs from that range
  material_identifiers(
    material_type: "WORKSTREAM_SUMMARIES",
    created: { from: "2025-02-17T00:00:00Z", to: "2025-02-17T23:59:59Z" }
  )
  --> { identifiers: ["uuid-1", "uuid-2"] }

Step 3: Get the full summaries
  workstream_summaries_batch_snapshot(identifiers: ["uuid-1", "uuid-2"])
  --> [full summary objects with content and annotations]
```

### 2. Search Copilot chat history for a topic

```
Step 1: Search conversations
  conversations_full_text_search(query: "GraphQL schema design")
  --> returns conversations with matched messages and annotations highlighted

Step 2 (optional): Get full conversation details
  conversations_batch_snapshot(identifiers: ["conv-uuid-1"])
  --> full conversation with all metadata
```

### 3. Semantic search for related work

```
Step 1: Find conceptually similar summaries
  workstream_summaries_vector_search(query: "API rate limiting strategies")
  --> { results: [{ identifier: "uuid-1", score: 0.87 }, ...] }

Step 2: Retrieve the full summaries
  workstream_summaries_batch_snapshot(identifiers: ["uuid-1"])
  --> full summary objects with content
```

### 4. Save a memory about current work

```
  create_pieces_memory(
    summary: "Implemented Redis caching for the product search API...",
    summary_description: "Search API caching with Redis",
    project: "/Users/dev/my-project",
    files: ["/Users/dev/my-project/src/cache/redis.ts"],
    externalLinks: ["https://github.com/org/repo/pull/42"]
  )
  --> "Long term memory successfully created..."
```

### 5. Ask Pieces about past context

```
  ask_pieces_ltm(
    question: "What database changes did I make this week?",
    topics: ["database", "migrations", "schema"],
    application_sources: ["vscode", "datagrip"],
    chat_llm: "gpt-4o-mini"
  )
  --> ranked summaries and events with relevance scores
```

### 6. Find clipboard activity from a specific application

```
Step 1: Get event IDs filtered by app and type
  material_identifiers(
    material_type: "WORKSTREAM_EVENTS",
    configurations: {
      workstream_events: {
        context: {
          type: "CLIPBOARD",
          application: "Visual Studio Code"
        }
      }
    },
    created: { from: "2025-02-18T00:00:00Z" },
    limit: 50
  )
  --> { identifiers: ["evt-1", "evt-2", ...] }

Step 2: Get the full events
  workstream_events_batch_snapshot(identifiers: ["evt-1", "evt-2"])
  --> full event objects with clipboard content and context
```

### 7. Recall what was said in a meeting about a topic

```
Step 1: Search audio transcriptions for the topic
  workstream_events_full_text_search(
    query: "caching strategy",
    context_type: "AUDIO",
    limit: 20
  )
  --> returns transcriptions from meetings where caching was discussed

Step 2 (optional): Narrow to a specific day
  workstream_events_full_text_search(
    query: "caching strategy",
    context_type: "AUDIO",
    created: { from: "2025-02-17T00:00:00Z", to: "2025-02-17T23:59:59Z" },
    limit: 20
  )
  --> only transcriptions from that day
```

### 8. Generate a standup from yesterday's activity

```
Step 1: Convert "yesterday" to UTC range
  extract_temporal_range(query: "yesterday")
  --> { ranges: [{ from: "...", to: "..." }] }

Step 2: Get all summaries from that range
  material_identifiers(
    material_type: "WORKSTREAM_SUMMARIES",
    created: { from: "...", to: "..." }
  )
  --> { identifiers: ["uuid-1", "uuid-2", "uuid-3", ...] }

Step 3: Retrieve full summaries
  workstream_summaries_batch_snapshot(identifiers: ["uuid-1", "uuid-2", "uuid-3"])
  --> full summary objects with content, tags, persons, and annotations

Step 4: Use the summary content to draft the standup
  The agent now has detailed records of every ~20-minute
  work session from yesterday, including which apps were
  used, which files were touched, which people were involved,
  and what topics were covered. It synthesizes these into a
  concise standup update.
```

### 9. Find research across multiple applications

```
Step 1: Search browser activity for the topic
  workstream_events_full_text_search(
    query: "WebSocket libraries",
    application: "Google Chrome",
    limit: 20
  )
  --> browser tabs, pages visited, text captured from screens

Step 2: Search clipboard activity for related code
  workstream_events_full_text_search(
    query: "WebSocket",
    context_type: "CLIPBOARD",
    limit: 20
  )
  --> code snippets and text copied during the research

Step 3: Search saved URLs
  websites_full_text_search(query: "websocket")
  --> URLs the user visited or bookmarked

The agent now has a complete picture: what pages were
visited, what code was copied, and what URLs were saved --
reconstructing the full research session across applications.
```

### 10. Cross-agent memory persistence

```
Agent A (Claude Code) saves a debugging breakthrough:
  create_pieces_memory(
    summary: "Root cause of the OOM crash: the connection pool
    wasn't releasing idle connections. Fixed by setting
    pool.max_idle_time to 30s. Verified with 48hr soak test.",
    summary_description: "Connection pool OOM fix",
    project: "/Users/dev/api-server",
    files: ["/Users/dev/api-server/src/db/pool.rs"],
    externalLinks: ["https://github.com/org/repo/pull/187"]
  )

Days later, Agent B (Cursor) retrieves it:
  ask_pieces_ltm(
    question: "How did we fix the OOM crash in the API server?",
    topics: ["OOM", "memory", "connection pool"],
    chat_llm: "gpt-4o-mini"
  )
  --> returns the memory saved by Agent A with full context

This is how agents build on each other's work across time.
```

---

## Visibility Reference

| Tool | MCP | OpenCode | Both |
|------|-----|----------|------|
| `ask_pieces_ltm` | Yes | - | - |
| `create_pieces_memory` | Yes | - | - |
| `conversations_full_text_search` | Yes | - | - |
| `conversation_messages_full_text_search` | Yes | - | - |
| `conversations_batch_snapshot` | Yes | - | - |
| `workstream_summaries_full_text_search` | - | - | Yes |
| `tags_full_text_search` | - | - | Yes |
| `annotations_full_text_search` | - | - | Yes |
| `persons_full_text_search` | - | - | Yes |
| `anchors_full_text_search` | - | - | Yes |
| `workstream_events_full_text_search` | - | - | Yes |
| `websites_full_text_search` | - | - | Yes |
| `hints_full_text_search` | - | - | Yes |
| `models_full_text_search` | - | - | Yes |
| `wpe_sources_full_text_search` | - | - | Yes |
| `wpe_source_windows_full_text_search` | - | - | Yes |
| `entities_full_text_search` | - | - | Yes |
| `materials_vector_search` | - | - | Yes |
| `workstream_summaries_vector_search` | - | - | Yes |
| `hints_vector_search` | - | - | Yes |
| `tags_vector_search` | - | - | Yes |
| `workstream_events_vector_search` | - | - | Yes |
| `material_identifiers` | - | - | Yes |
| `extract_temporal_range` | - | - | Yes |
| `workstream_summaries_batch_snapshot` | - | - | Yes |
| `tags_batch_snapshot` | - | - | Yes |
| `annotations_batch_snapshot` | - | - | Yes |
| `persons_batch_snapshot` | - | - | Yes |
| `anchors_batch_snapshot` | - | - | Yes |
| `anchor_points_batch_snapshot` | - | - | Yes |
| `workstream_events_batch_snapshot` | - | - | Yes |
| `hints_batch_snapshot` | - | - | Yes |
| `models_batch_snapshot` | - | - | Yes |
| `ranges_batch_snapshot` | - | - | Yes |
| `websites_batch_snapshot` | - | - | Yes |
| `entities_batch_snapshot` | - | - | Yes |
| `conversation_messages_batch_snapshot` | - | - | Yes |
| `wpe_sources_batch_snapshot` | - | - | Yes |
| `wpe_source_windows_batch_snapshot` | - | - | Yes |

---

## Smoke Test Results (February 18, 2026)

All 39 Pieces MCP tools were tested with minimal valid inputs to confirm they respond without error.

| Tool | Status | Notes |
|------|--------|-------|
| `ask_pieces_ltm` | Pass | Returned recent summaries and events |
| `create_pieces_memory` | Pass | Memory persisted successfully |
| `workstream_summaries_full_text_search` | Pass | 1 result returned |
| `conversations_full_text_search` | Pass | 1 result returned |
| `tags_full_text_search` | Pass | 1 result returned |
| `annotations_full_text_search` | Pass | 1 result returned |
| `persons_full_text_search` | Pass | 1 result returned |
| `anchors_full_text_search` | Pass | 1 result returned |
| `workstream_events_full_text_search` | Pass | 1 result returned |
| `websites_full_text_search` | Pass | 1 result returned |
| `hints_full_text_search` | Pass | 1 result returned |
| `models_full_text_search` | Pass | 0 results (no model name matched "test"; valid empty response) |
| `wpe_sources_full_text_search` | Pass | 0 results (valid empty response) |
| `wpe_source_windows_full_text_search` | Pass | 1 result returned |
| `entities_full_text_search` | Pass | 0 results (valid empty response) |
| `conversation_messages_full_text_search` | Pass | 1 result returned |
| `materials_vector_search` | Pass | 1 result returned (WORKSTREAM_SUMMARIES) |
| `workstream_summaries_vector_search` | Pass | 1 result returned |
| `hints_vector_search` | Pass | 1 result returned |
| `tags_vector_search` | Pass | 1 result returned (score 1.0) |
| `workstream_events_vector_search` | Pass | 1 result returned |
| `material_identifiers` | Pass | Tested with ENTITIES and WPE_SOURCES |
| `extract_temporal_range` | Pass | "yesterday" resolved to correct UTC range |
| `workstream_summaries_batch_snapshot` | Pass | 1 item returned |
| `conversations_batch_snapshot` | Pass | 1 item returned |
| `tags_batch_snapshot` | Pass | 1 item returned |
| `annotations_batch_snapshot` | Pass | 1 item returned |
| `persons_batch_snapshot` | Pass | 1 item returned |
| `anchors_batch_snapshot` | Pass | 1 item returned |
| `anchor_points_batch_snapshot` | Pass | 1 item returned |
| `workstream_events_batch_snapshot` | Pass | 1 item returned |
| `hints_batch_snapshot` | Pass | 1 item returned |
| `models_batch_snapshot` | Pass | 0 items + missing_ids (reference UUID, not a stored model; valid response) |
| `ranges_batch_snapshot` | Pass | 1 item returned |
| `websites_batch_snapshot` | Pass | 1 item returned |
| `entities_batch_snapshot` | Pass | 1 item returned |
| `conversation_messages_batch_snapshot` | Pass | 1 item returned |
| `wpe_sources_batch_snapshot` | Pass | 1 item returned |
| `wpe_source_windows_batch_snapshot` | Pass | 1 item returned |

**Result: 39/39 tools passed.**

---

## Related Guides

- [MCP Guides Index](./README.md) — Overview of all Pieces MCP documentation
- [Agent Setups & Integrations](./Agent%20Setups%20%26%20Integrations/README.md) — Per-tool setup guides for Cursor, Claude, Goose, and 16 more
- [Connecting to PiecesOS via Ngrok](./Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md) — Expose your local PiecesOS to cloud-based agents
- [Bridging Local MCP Clients with mcp-remote](./Bridging%20Local%20MCP%20Clients%20to%20Remote%20Servers%20with%20mcp-remote.md) — Connect stdio-only clients to the HTTP endpoint

---

<table width="100%"><tr>
<td>&nbsp;&nbsp;<a href="./README.md">← Previous: MCP Guides Index</a>&nbsp;&nbsp;</td>
<td align="right">&nbsp;&nbsp;<a href="./Connecting%20to%20PiecesOS%20from%20the%20Outside%20World%20via%20Ngrok.md">Next: Connecting to PiecesOS via Ngrok →</a>&nbsp;&nbsp;</td>
</tr></table>
