from abc import ABC, abstractmethod
from typing import Any


class PostRepository(ABC):
    @abstractmethod
    def list_posts(self) -> list[dict[str, Any]]: ...

    @abstractmethod
    def get_post(self, post_id: str) -> dict[str, Any] | None: ...

    @abstractmethod
    def create_post(self, post: dict[str, Any]) -> dict[str, Any]: ...

    @abstractmethod
    def set_like(self, post_id: str, user_id: str, liked: bool) -> dict[str, Any]: ...

    @abstractmethod
    def set_repost(self, post_id: str, user_id: str, reposted: bool) -> dict[str, Any]: ...
