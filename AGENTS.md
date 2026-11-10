# AGENTS.md — Agent Guidelines & Instructions for HookRelay

This document defines the permanent rules, context, and development guidelines for any AI assistant working on the **HookRelay** codebase.

---

## 1. Project Context & User Profile
- **Project:** HookRelay (Webhook Management and Reliability Platform).
- **User:** BSCS student learning backend development.
- **Skill Level:** Understands core backend and computer science concepts (HTTP, REST, databases, queues, concurrency), but is building practical implementation skills.
- **Primary Goal:** Learn how production-grade, reliable distributed systems work by building one step-by-step.

---

## 2. Core Working Principles

### A. Code Style & Simplicity
- **Beginner-Friendly & Readable:** Write clean, idiomatic Python and JavaScript/TypeScript. Prefer clarity over cleverness.
- **No Overengineering:** Avoid premature abstractions, overly complex design patterns, or unnecessary third-party libraries.
- **Maintainable & Documented:** Add concise comments explaining *why* certain decisions are made (e.g., why transactions are committed at specific points, how race conditions are avoided).
- **Type Hints:** Use standard Python type hints (`pydantic`, `typing`) to aid learning and code safety.

### B. Task Discipline & Pacing
- **One Feature Per Task:** Only implement the specific task requested. Never combine multiple milestones or features into one task.
- **Do Not Generate Everything at Once:** Incremental development allows the user to review, understand, test, and learn each piece.
- **Inspect Before Modifying:** Always inspect existing code and file structures before suggesting or writing modifications.
- **Preserve Working Code:** Do not refactor or rewrite functional code unless there is a clear, explained bug or requirement.

### C. Transparency & Permissions
- **Explain Important Decisions:** Briefly explain architecture choices, database schema decisions, queue mechanics, and trade-offs.
- **Explain Operations Before Execution:** Before installing dependencies, running migrations, or executing resource-heavy commands, explain what the command does and why it is needed.

### D. Token & Communication Efficiency
- Keep responses concise, structured, and direct.
- Avoid unnecessary exploratory tool calls.
- Stick strictly to the user's explicit scope.

---

## 3. Technology Stack Reference
- **Backend:** Python 3.11+, FastAPI, Pydantic, SQLAlchemy / Alembic
- **Database:** PostgreSQL
- **Background Processing / Queue:** Redis + Worker (e.g., RQ / Celery / custom asyncio worker)
- **Frontend:** React (Vite)
- **Dev Environment:** Windows + WSL Ubuntu
- **Version Control:** Git & GitHub
- **Containerization:** Docker & Docker Compose

