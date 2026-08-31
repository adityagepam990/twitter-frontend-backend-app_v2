from dataclasses import dataclass


@dataclass
class User:
    id: str
    display_name: str
    handle: str
    avatar_url: str
    followed: bool
