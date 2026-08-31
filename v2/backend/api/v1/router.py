from fastapi import APIRouter

from backend.api.v1.routes import health_routes

router = APIRouter(prefix="/api/v1")
router.include_router(health_routes.router)
