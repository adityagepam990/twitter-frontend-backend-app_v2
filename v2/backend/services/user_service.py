from backend.models.user_model import User
from backend.repositories.provider import get_user_repository

SUGGESTED_USERS_LIMIT = 3


class UserNotFoundError(ValueError):
    pass


def get_suggested_users() -> list[User]:
    users = get_user_repository().list_users()
    not_followed = [user for user in users if not user.followed]
    return not_followed[:SUGGESTED_USERS_LIMIT]


def toggle_follow(user_id: str) -> User:
    repository = get_user_repository()
    user = repository.get_user(user_id)
    if user is None:
        raise UserNotFoundError(user_id)
    return repository.set_followed(user_id, not user.followed)
