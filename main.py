"""
WellnessConnect - AI-Powered Health Concierge Platform
Main application entry point
"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings
from config.database import engine, Base
from src.api.whatsapp_webhook import router as whatsapp_router
from src.api.appointment_api import router as appointment_router
from src.api.health_assessment_api import router as health_assessment_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="WellnessConnect",
    description="AI-Powered Health Concierge Platform",
    version="1.0.0",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.DEBUG else ["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(whatsapp_router, prefix="/api/whatsapp", tags=["WhatsApp"])
app.include_router(appointment_router, prefix="/api/appointments", tags=["Appointments"])
app.include_router(health_assessment_router, prefix="/api/health", tags=["Health Assessment"])

@app.get("/")
async def root(request: Request):
    """Root endpoint"""
    return templates.TemplateResponse(
        "admin/dashboard.html", 
        {"request": request, "title": "WellnessConnect Dashboard"}
    )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "WellnessConnect"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="debug" if settings.DEBUG else "info"
    )