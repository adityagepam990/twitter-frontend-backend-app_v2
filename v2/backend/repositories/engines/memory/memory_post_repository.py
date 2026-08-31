from typing import Any

from backend.repositories.post_repository import PostRepository


class MemoryPostRepository(PostRepository):
    def __init__(self) -> None:
        self._posts: dict[str, dict[str, Any]] = {}

    def list_posts(self) -> list[dict[str, Any]]:
        return list(self._posts.values())

    def get_post(self, post_id: str) -> dict[str, Any] | None:
        return self._posts.get(post_id)

    def create_post(self, post: dict[str, Any]) -> dict[str, Any]:
        self._posts[post["id"]] = post
        return post

    def set_like(self, post_id: str, user_id: str, liked: bool) -> dict[str, Any]:
        post = self._posts[post_id]
        liked_by = post.setdefault("liked_by", set())
        liked_by.add(user_id) if liked else liked_by.discard(user_id)
        return post

    def set_repost(self, post_id: str, user_id: str, reposted: bool) -> dict[str, Any]:
        post = self._posts[post_id]
        reposted_by = post.setdefault("reposted_by", set())
        reposted_by.add(user_id) if reposted else reposted_by.discard(user_id)
        return post
