from pydantic import BaseModel, ConfigDict


class TrendOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    category: str
    topic: str
    post_count: int
