from abc import ABC, abstractmethod

from backend.models.user_model import User


class UserRepository(ABC):
    @abstractmethod
    def list_users(self) -> list[User]: ...

    @abstractmethod
    def get_user(self, user_id: str) -> User | None: ...

    @abstractmethod
    def set_followed(self, user_id: str, followed: bool) -> User: ...
