from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from app.api.health import router as health_router
from app.api.database import router as database_router
from app.api.test_hash import router as hash_router
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.documents import router as documents_router
from app.api.test_pdf import router as pdf_router
from app.api.chat import router as chat_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# ======================================
# CORS
# ======================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================================
# Routers
# ======================================

app.include_router(database_router)
app.include_router(health_router)
app.include_router(hash_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(documents_router)
app.include_router(pdf_router)
app.include_router(chat_router)

# ======================================
# Home
# ======================================

@app.get("/")
def home():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "Running Successfully"
    }