from abc import ABC, abstractmethod

from backend.models.post_model import Post


class PostRepository(ABC):
    @abstractmethod
    def list_posts(self) -> list[Post]: ...

    @abstractmethod
    def get_post(self, post_id: str) -> Post | None: ...

    @abstractmethod
    def create_post(self, post: Post) -> Post: ...

    @abstractmethod
    def set_like(self, post_id: str, user_id: str, liked: bool) -> Post: ...

    @abstractmethod
    def set_repost(self, post_id: str, user_id: str, reposted: bool) -> Post: ...
