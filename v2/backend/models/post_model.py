from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Post:
    id: str
    author_id: str
    author_name: str
    author_handle: str
    author_avatar_url: str
    author_followed: bool
    body: str
    created_at: datetime
    reply_count: int
    repost_count: int
    like_count: int
    image_url: str | None = None
    liked_by: set[str] = field(default_factory=set)
    reposted_by: set[str] = field(default_factory=set)
