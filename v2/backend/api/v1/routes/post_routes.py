from fastapi import APIRouter, HTTPException, status

from backend.schemas.post_schema import PostCreate, PostOut
from backend.services.post_service import (
    InvalidPostTextError,
    PostNotFoundError,
    create_post,
    toggle_like,
    toggle_repost,
)

router = APIRouter()


@router.post("/posts", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post_route(payload: PostCreate):
    try:
        return create_post(payload.text)
    except InvalidPostTextError as error:
        raise HTTPException(status_code=422, detail=str(error))


@router.post("/posts/{post_id}/like", response_model=PostOut)
def like_post_route(post_id: str):
    try:
        return toggle_like(post_id)
    except PostNotFoundError:
        raise HTTPException(status_code=404, detail=f"Post not found: {post_id}")


@router.post("/posts/{post_id}/repost", response_model=PostOut)
def repost_post_route(post_id: str):
    try:
        return toggle_repost(post_id)
    except PostNotFoundError:
        raise HTTPException(status_code=404, detail=f"Post not found: {post_id}")
