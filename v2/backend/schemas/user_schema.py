from pydantic import BaseModel, ConfigDict


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    display_name: str
    handle: str
    avatar_url: str
    followed: bool
