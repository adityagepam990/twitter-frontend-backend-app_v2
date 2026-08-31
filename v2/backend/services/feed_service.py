from backend.models.post_model import Post
from backend.repositories.provider import get_post_repository

VALID_TABS = {"for-you", "following"}


class InvalidTabError(ValueError):
    pass


def get_feed(tab: str) -> list[Post]:
    if tab not in VALID_TABS:
        raise InvalidTabError(tab)

    posts = get_post_repository().list_posts()

    if tab == "following":
        posts = [post for post in posts if post.author_followed]

    return sorted(posts, key=lambda post: post.created_minutes_ago)
