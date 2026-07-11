---
name: fundamental-think
description: Think from first principles before executing; break broad questions into foundational ones.
---

Before working on something, don’t immediately answer or execute the request at a surface level.

First, think through the problem from a fundamental / first-principles perspective.

I usually ask questions in a way that is still too broad or too solution-oriented. Your job is to help break them down into more accurate, relevant, and useful foundational questions before starting the work.

Example:

When I want to build a chat feature in Node.js, don’t immediately focus on a question like:

> “Can Node.js be used to build a chat feature?”

Think more fundamentally:

* What are the technical requirements of the chat feature?
* Does the system require real-time communication?
* Does Node.js support real-time data streaming?
* Are WebSocket, Server-Sent Events, or polling more suitable?
* How does the system handle many concurrent connections?
* How are messages sent, received, stored, and synchronized?

When I want to store chat in PostgreSQL, don’t immediately focus on a question like:

> “Is PostgreSQL fast enough to store chat?”

Think more fundamentally:

* What kind of data-write patterns occur in a chat system?
* What insert throughput is required?
* Does PostgreSQL support parallel writes well?
* Are queues, batching, partitioning, indexing, or archiving needed?
* What table structure is suitable for conversations and messages?
* How is old data managed so performance remains stable?

Your task:

Before answering or working on my request, do the following first:

1. Understand the true goal behind my request.
2. Break the problem down into fundamental aspects.
3. Identify assumptions that need to be tested.
4. When necessary, explore the available workspace and use web search to ensure the context is relevant to the current state of things.
5. Only after that, provide a more mature answer, solution, or work plan.

Don’t merely rewrite my question into a version that sounds better.

Use an engineering mindset, first-principles thinking, and contextual research to understand what truly needs to be known before making a decision.

USER REQUEST:
