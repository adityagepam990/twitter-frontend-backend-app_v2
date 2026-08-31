from backend.core.config import settings
from backend.repositories.engines.memory.memory_post_repository import MemoryPostRepository
from backend.repositories.post_repository import PostRepository

_post_repository: PostRepository | None = None


def get_post_repository() -> PostRepository:
    global _post_repository
    if _post_repository is None:
        if settings.ENGINE == "memory":
            _post_repository = MemoryPostRepository()
        else:
            raise ValueError(f"Unknown ENGINE: {settings.ENGINE}")
    return _post_repository
