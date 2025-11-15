from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Check if multipart is available
try:
    import multipart
    HAS_MULTIPART = True
except ImportError:
    HAS_MULTIPART = False

try:
    from backend.modules import backend_utils as bu
    from backend.modules import db as dbmod
except ImportError:
    # For development: use relative imports if backend.modules is not available
    import backend_utils as bu
    import db as dbmod

# Initialize FastAPI app
app = FastAPI(
    title="Navi AI Backend",
    description="Backend API for Navi AI navigation assistance system",
    version="1.0.0"
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
    return {"status": "healthy", "multipart_available": HAS_MULTIPART}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Navi AI Backend is running", "multipart_available": HAS_MULTIPART}

# Detection endpoint - will be added once python-multipart is installed
# TODO: Add @app.post("/detect") endpoint after python-multipart is installed

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

