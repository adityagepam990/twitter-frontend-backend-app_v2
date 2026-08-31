from dataclasses import dataclass


@dataclass
class Trend:
    id: str
    category: str
    topic: str
    post_count: int
