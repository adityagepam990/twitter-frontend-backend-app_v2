import json
from datetime import datetime
from pathlib import Path

from backend.models.post_model import Post
from backend.repositories.post_repository import PostRepository

_DEFAULT_PATH = Path(__file__).parent / "data" / "posts.json"


def _post_to_dict(post: Post) -> dict:
    return {
        "id": post.id,
        "author_id": post.author_id,
        "author_name": post.author_name,
        "author_handle": post.author_handle,
        "author_avatar_url": post.author_avatar_url,
        "author_followed": post.author_followed,
        "body": post.body,
        "created_at": post.created_at.isoformat(),
        "reply_count": post.reply_count,
        "repost_count": post.repost_count,
        "like_count": post.like_count,
        "image_url": post.image_url,
        "liked_by": sorted(post.liked_by),
        "reposted_by": sorted(post.reposted_by),
    }


def _dict_to_post(data: dict) -> Post:
    return Post(
        id=data["id"],
        author_id=data["author_id"],
        author_name=data["author_name"],
        author_handle=data["author_handle"],
        author_avatar_url=data["author_avatar_url"],
        author_followed=data["author_followed"],
        body=data["body"],
        created_at=datetime.fromisoformat(data["created_at"]),
        reply_count=data["reply_count"],
        repost_count=data["repost_count"],
        like_count=data["like_count"],
        image_url=data.get("image_url"),
        liked_by=set(data.get("liked_by", [])),
        reposted_by=set(data.get("reposted_by", [])),
    )


class JsonFilePostRepository(PostRepository):
    def __init__(self, path: Path | str | None = None, seed_posts: list[Post] | None = None) -> None:
        self._path = Path(path) if path is not None else _DEFAULT_PATH
        if not self._path.exists():
            self._write(list(seed_posts or []))
        self._posts: dict[str, Post] = {post.id: post for post in self._read()}

    def _read(self) -> list[Post]:
        raw = json.loads(self._path.read_text())
        return [_dict_to_post(item) for item in raw]

    def _write(self, posts: list[Post]) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._path.write_text(json.dumps([_post_to_dict(post) for post in posts]))

    def _save(self) -> None:
        self._write(list(self._posts.values()))

    def list_posts(self) -> list[Post]:
        return list(self._posts.values())

    def get_post(self, post_id: str) -> Post | None:
        return self._posts.get(post_id)

    def create_post(self, post: Post) -> Post:
        self._posts[post.id] = post
        self._save()
        return post

    def set_like(self, post_id: str, user_id: str, liked: bool) -> Post:
        post = self._posts[post_id]
        if liked:
            post.liked_by.add(user_id)
        else:
            post.liked_by.discard(user_id)
        self._save()
        return post

    def set_repost(self, post_id: str, user_id: str, reposted: bool) -> Post:
        post = self._posts[post_id]
        if reposted:
            post.reposted_by.add(user_id)
        else:
            post.reposted_by.discard(user_id)
        self._save()
        return post
