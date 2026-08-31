import uuid
from datetime import UTC, datetime

from backend.models.post_model import Post
from backend.repositories.provider import get_post_repository
from backend.repositories.seed.user_seed import get_seed_users

MAX_POST_LENGTH = 280
CURRENT_USER_ID = "u1"


class InvalidPostTextError(ValueError):
    pass


class PostNotFoundError(ValueError):
    pass


def _current_user():
    return {user.id: user for user in get_seed_users()}[CURRENT_USER_ID]


def _get_post_or_raise(post_id: str) -> Post:
    post = get_post_repository().get_post(post_id)
    if post is None:
        raise PostNotFoundError(post_id)
    return post


def create_post(text: str) -> Post:
    if not text.strip():
        raise InvalidPostTextError("Post text cannot be empty.")
    if len(text) > MAX_POST_LENGTH:
        raise InvalidPostTextError(f"Post text cannot exceed {MAX_POST_LENGTH} characters.")

    author = _current_user()
    post = Post(
        id=str(uuid.uuid4()),
        author_id=author.id,
        author_name=author.display_name,
        author_handle=author.handle,
        author_avatar_url=author.avatar_url,
        author_followed=author.followed,
        body=text,
        created_at=datetime.now(UTC),
        reply_count=0,
        repost_count=0,
        like_count=0,
    )
    return get_post_repository().create_post(post)


def toggle_like(post_id: str) -> Post:
    post = _get_post_or_raise(post_id)
    liked = CURRENT_USER_ID not in post.liked_by
    updated = get_post_repository().set_like(post_id, CURRENT_USER_ID, liked)
    updated.like_count += 1 if liked else -1
    return updated


def toggle_repost(post_id: str) -> Post:
    post = _get_post_or_raise(post_id)
    reposted = CURRENT_USER_ID not in post.reposted_by
    updated = get_post_repository().set_repost(post_id, CURRENT_USER_ID, reposted)
    updated.repost_count += 1 if reposted else -1
    return updated
