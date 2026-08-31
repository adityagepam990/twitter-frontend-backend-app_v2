from backend.models.user_model import User
from backend.repositories.user_repository import UserRepository


class MemoryUserRepository(UserRepository):
    def __init__(self, seed_users: list[User] | None = None) -> None:
        self._users: dict[str, User] = {user.id: user for user in (seed_users or [])}

    def list_users(self) -> list[User]:
        return list(self._users.values())

    def get_user(self, user_id: str) -> User | None:
        return self._users.get(user_id)

    def set_followed(self, user_id: str, followed: bool) -> User:
        user = self._users[user_id]
        user.followed = followed
        return user
