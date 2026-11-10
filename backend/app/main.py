from fastapi import FastAPI

# Create the FastAPI application
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
