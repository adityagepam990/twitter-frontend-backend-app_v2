from fastapi import APIRouter, HTTPException

from backend.schemas.user_schema import UserOut
from backend.services.user_service import UserNotFoundError, get_suggested_users, toggle_follow

router = APIRouter()


@router.get("/users/suggested", response_model=list[UserOut])
def get_suggested_users_route():
    return get_suggested_users()


@router.post("/users/{user_id}/follow", response_model=UserOut)
def follow_user_route(user_id: str):
    try:
        return toggle_follow(user_id)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail=f"User not found: {user_id}")
