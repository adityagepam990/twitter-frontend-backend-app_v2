from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

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


class PostCreate(BaseModel):
    text: str
