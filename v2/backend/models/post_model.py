from dataclasses import dataclass, field


@dataclass
class Post:
    id: str
    author_id: str
    author_name: str
    author_handle: str
    author_avatar_url: str
    author_followed: bool
    body: str
    created_minutes_ago: int
    reply_count: int
    repost_count: int
    like_count: int
    image_url: str | None = None
    liked_by: set[str] = field(default_factory=set)
    reposted_by: set[str] = field(default_factory=set)
