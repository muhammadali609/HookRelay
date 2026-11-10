# DEVELOPMENT_PLAN.md — HookRelay Roadmap & Checklist

This plan outlines the milestones for building HookRelay incrementally. Each milestone delivers a functional, tested slice of the system.

---

## 🧭 Milestone Overview

```
Milestone 0: Foundation & Environment Setup
     ↓
Milestone 1: Database Schema & Webhook Ingestion API
     ↓
Milestone 2: Redis Queue & Asynchronous Delivery Worker
     ↓
Milestone 3: Retry Engine with Exponential Backoff
     ↓
Milestone 4: Idempotency & Deduplication Engine
     ↓
Milestone 5: Event Querying, Analytics & Inspection API
     ↓
Milestone 6: React Monitoring Dashboard
     ↓
Milestone 7: Testing, Dockerization & Portfolio Polish
```

---

## 📋 Detailed Milestone Checklist

### Milestone 0: Foundation & Environment Setup
- [ ] Initialize Git repository.
- [ ] Set up Docker Compose for local PostgreSQL and Redis.
- [ ] Create Python virtual environment and configure backend dependencies (`fastapi`, `uvicorn`, `sqlalchemy`, `pydantic`, `alembic`, `redis`).
- [ ] Verify database and Redis connectivity with a basic health check endpoint (`/health`).

### Milestone 1: Database Schema & Webhook Ingestion API
- [ ] Design relational database schema:
  - `endpoints` (id, url, secret, is_active, created_at)
  - `events` (id, endpoint_id, payload, headers, idempotency_key, status, received_at)
  - `delivery_attempts` (id, event_id, status_code, response_body, attempt_number, executed_at, duration_ms)
- [ ] Set up Alembic migrations.
- [ ] Build ingestion endpoint (`POST /api/v1/ingest/{endpoint_id}`):
  - Validate endpoint exists and is active.
  - Persist event payload to database with status `PENDING`.
  - Return `202 Accepted` immediately with an event tracking ID.

### Milestone 2: Redis Queue & Asynchronous Delivery Worker
- [ ] Set up background queue integration (publish event IDs onto a Redis queue upon ingestion).
- [ ] Implement standalone background worker:
  - Consume event IDs from Redis.
  - Fetch event and endpoint details from database.
  - Perform HTTP POST request to destination URL with payload and headers.
  - Record the result in `delivery_attempts` table.
  - Update `events` status to `DELIVERED` (on 2xx) or `FAILED` (on non-2xx / timeout).

### Milestone 3: Retry Engine with Exponential Backoff
- [ ] Define retry policy (e.g., max 5 attempts, initial delay 5s, exponential multiplier, jitter).
- [ ] Handle worker failures (network timeouts, 5xx server errors).
- [ ] Implement delayed scheduling in Redis for failed events.
- [ ] Mark event as `DEAD_LETTER` after maximum retry attempts exhausted.

### Milestone 4: Idempotency & Deduplication Engine
- [ ] Support `Idempotency-Key` header on ingestion.
- [ ] Implement payload hashing (SHA-256) as a fallback duplicate detection method.
- [ ] Return existing event status if a duplicate event is received within a deduplication window.

### Milestone 5: Event Querying, Analytics & Inspection API
- [ ] Endpoint management routes (`GET`, `POST`, `PATCH`, `DELETE` `/api/v1/endpoints`).
- [ ] Event query routes with pagination and filters (`GET /api/v1/events?status=...&endpoint_id=...`).
- [ ] Event details route with delivery attempt timeline (`GET /api/v1/events/{event_id}`).
- [ ] Manual redelivery trigger endpoint (`POST /api/v1/events/{event_id}/retry`).

### Milestone 6: React Monitoring Dashboard
- [ ] Initialize React frontend using Vite.
- [ ] Endpoints list and creation view.
- [ ] Real-time or polled event feed (status badges, timestamps, latencies).
- [ ] Event detail modal/view showing headers, payload, and retry history.
- [ ] "Retry Now" button for failed events.

### Milestone 7: Testing, Dockerization & Portfolio Polish
- [ ] Unit and integration tests for ingestion, worker, and retry logic.
- [ ] Full `docker-compose.yml` to spin up entire stack (FastAPI + Worker + Postgres + Redis + React).
- [ ] Comprehensive documentation with architecture diagrams.

