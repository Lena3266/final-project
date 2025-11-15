from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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
    return {"status": "healthy"}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Navi AI Backend is running"}

# Detection endpoint (placeholder)
@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    """Detect objects in uploaded image."""
    try:
        contents = await file.read()
        # Placeholder: Process image detection
        return {
            "status": "success",
            "message": "Image processed",
            "filename": file.filename
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

