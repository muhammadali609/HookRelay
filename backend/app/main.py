from typing import Any

from fastapi import FastAPI

app = FastAPI(
    title="HookRelay",
    description="A reliable webhook management platform",
    version="0.1.0"
)


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "HookRelay API is running"
    }


# Receive webhook events
@app.post("/webhooks/{source}")
async def receive_webhook(source: str, payload: dict[str, Any]):
    return {
        "status": "received",
        "source": source,
        "event_type": payload.get("type", "unknown"),
        "message": "Webhook received successfully"
    }
