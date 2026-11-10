# HookRelay 🚀

**HookRelay** is a reliable webhook management and delivery proxy platform. It receives webhook events from third-party services (e.g., Stripe, GitHub, Shopify), safely persists them, forwards them to target endpoints, automatically retries failed deliveries with exponential backoff, prevents duplicate processing, and provides full event visibility.

---

## 🎯 The Problem HookRelay Solves

Webhooks are critical for modern event-driven architectures, but standard webhook delivery is fragile:
1. **Downtime & Network Failures:** If your destination service is temporarily down, incoming webhooks are often lost forever.
2. **Duplication Risk:** Network timeouts often trigger retries from senders, causing destination services to process the same payment or action twice.
3. **Lack of Visibility:** Debugging dropped or malformed webhook payloads without centralized logs is difficult.

**HookRelay acts as a resilient buffer between event senders and receivers.**

---

## ✨ Planned Features

- **Ingestion Buffer:** Accepts webhook payloads quickly (HTTP 202 Accepted) and safely writes them to PostgreSQL before acknowledging.
- **Asynchronous Queueing:** Offloads webhook forwarding to background workers via Redis.
- **Intelligent Retries:** Retries delivery on `5xx` responses and network timeouts using configurable exponential backoff with jitter.
- **Idempotency Protection:** Detects duplicate events using unique event IDs/payload hashes to prevent duplicate processing.
- **Audit & History:** Full log of incoming events, payload data, attempt counts, response codes, and round-trip latencies.
- **Management Dashboard:** Simple React UI to inspect endpoints, monitor delivery statuses in real-time, and manually trigger redeliveries.

---

## 🛠️ Proposed Tech Stack

| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Backend API** | Python 3 + FastAPI | High performance, native async support, and auto-generated OpenAPI documentation. |
| **Database** | PostgreSQL | Robust relational storage with ACID compliance for event logs and endpoint configurations. |
| **Queue / Background Jobs** | Redis + Background Worker | Fast in-memory message broker to decouple ingestion from delivery tasks. |
| **Frontend** | React (Vite) | Fast, responsive UI for monitoring deliveries and inspecting payloads. |
| **Containerization** | Docker & Docker Compose | Uniform local environment across Windows and WSL Ubuntu. |
| **Version Control** | Git + GitHub | Clean, commit-driven portfolio history. |

---

## 📁 Repository Structure (Planned)

```text
HookRelay/
├── backend/            # FastAPI application & background workers
│   ├── app/
│   │   ├── api/        # Route handlers (ingestion, management, stats)
│   │   ├── core/       # Configurations, logging, security
│   │   ├── models/     # Database models (SQLAlchemy)
│   │   ├── schemas/    # Pydantic validation schemas
│   │   ├── services/   # Business logic (delivery, retry, hashing)
│   │   └── workers/    # Background worker processes
│   └── tests/          # Unit and integration tests
├── frontend/           # React dashboard
├── docker/             # Dockerfiles & compose files
├── AGENTS.md           # Permanent rules for AI pair programmers
├── DEVELOPMENT_PLAN.md # Roadmap and milestone checklist
└── README.md           # Project overview
```

---

## 📌 Development Philosophy
HookRelay is built incrementally with a strong emphasis on readable code, clean architecture, and real-world backend best practices.

