from fastapi import APIRouter, HTTPException

from backend.schemas.post_schema import PostOut
from backend.services.feed_service import InvalidTabError, get_feed

router = APIRouter()


@router.get("/feed", response_model=list[PostOut])
def get_feed_route(tab: str = "for-you"):
    try:
        return get_feed(tab)
    except InvalidTabError:
        raise HTTPException(status_code=422, detail=f"Unknown tab: {tab}")
