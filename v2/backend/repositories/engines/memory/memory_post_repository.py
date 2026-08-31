from backend.models.post_model import Post
from backend.repositories.post_repository import PostRepository


class MemoryPostRepository(PostRepository):
    def __init__(self, seed_posts: list[Post] | None = None) -> None:
        self._posts: dict[str, Post] = {post.id: post for post in (seed_posts or [])}

    def list_posts(self) -> list[Post]:
        return list(self._posts.values())

    def get_post(self, post_id: str) -> Post | None:
        return self._posts.get(post_id)

    def create_post(self, post: Post) -> Post:
        self._posts[post.id] = post
        return post

    def set_like(self, post_id: str, user_id: str, liked: bool) -> Post:
        post = self._posts[post_id]
        if liked:
            post.liked_by.add(user_id)
        else:
            post.liked_by.discard(user_id)
        return post

    def set_repost(self, post_id: str, user_id: str, reposted: bool) -> Post:
        post = self._posts[post_id]
        if reposted:
            post.reposted_by.add(user_id)
        else:
            post.reposted_by.discard(user_id)
        return post
