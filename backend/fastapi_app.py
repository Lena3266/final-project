"""
Navi AI FastAPI Backend
Version: 1.0.2 (Updated: 2025-11-15)

This backend provides API endpoints for the Navi AI navigation assistance system.
Basic endpoints (/health, /) work without python-multipart.
File upload endpoints will be added once python-multipart is installed on the deployment environment.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Navi AI Backend",
    description="Backend API for Navi AI navigation assistance system",
    version="1.0.2"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.2"}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Navi AI Backend is running", "version": "1.0.2"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
