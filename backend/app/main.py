from fastapi import FastAPI

app = FastAPI(
    title="EduRAG API",
    description="AI-powered University Knowledge Assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to EduRAG!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }