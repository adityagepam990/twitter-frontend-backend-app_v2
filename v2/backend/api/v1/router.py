from fastapi import APIRouter

from backend.api.v1.routes import feed_routes, health_routes, post_routes, trend_routes, user_routes

router = APIRouter(prefix="/api/v1")
router.include_router(health_routes.router)
router.include_router(feed_routes.router)
router.include_router(post_routes.router)
router.include_router(user_routes.router)
router.include_router(trend_routes.router)
