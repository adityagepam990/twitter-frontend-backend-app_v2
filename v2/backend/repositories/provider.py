from backend.core.config import settings
from backend.repositories.engines.jsonfile.jsonfile_post_repository import JsonFilePostRepository
from backend.repositories.engines.jsonfile.jsonfile_trend_repository import JsonFileTrendRepository
from backend.repositories.engines.jsonfile.jsonfile_user_repository import JsonFileUserRepository
from backend.repositories.engines.memory.memory_post_repository import MemoryPostRepository
from backend.repositories.engines.memory.memory_trend_repository import MemoryTrendRepository
from backend.repositories.engines.memory.memory_user_repository import MemoryUserRepository
from backend.repositories.post_repository import PostRepository
from backend.repositories.seed.post_seed import get_seed_posts
from backend.repositories.seed.trend_seed import get_seed_trends
from backend.repositories.seed.user_seed import get_seed_users
from backend.repositories.trend_repository import TrendRepository
from backend.repositories.user_repository import UserRepository

_post_repository: PostRepository | None = None
_user_repository: UserRepository | None = None
_trend_repository: TrendRepository | None = None


def get_post_repository() -> PostRepository:
    global _post_repository
    if _post_repository is None:
        if settings.ENGINE == "memory":
            _post_repository = MemoryPostRepository(seed_posts=get_seed_posts())
        elif settings.ENGINE == "jsonfile":
            _post_repository = JsonFilePostRepository(seed_posts=get_seed_posts())
        else:
            raise ValueError(f"Unknown ENGINE: {settings.ENGINE}")
    return _post_repository


def get_user_repository() -> UserRepository:
    global _user_repository
    if _user_repository is None:
        if settings.ENGINE == "memory":
            _user_repository = MemoryUserRepository(seed_users=get_seed_users())
        elif settings.ENGINE == "jsonfile":
            _user_repository = JsonFileUserRepository(seed_users=get_seed_users())
        else:
            raise ValueError(f"Unknown ENGINE: {settings.ENGINE}")
    return _user_repository


def get_trend_repository() -> TrendRepository:
    global _trend_repository
    if _trend_repository is None:
        if settings.ENGINE == "memory":
            _trend_repository = MemoryTrendRepository(seed_trends=get_seed_trends())
        elif settings.ENGINE == "jsonfile":
            _trend_repository = JsonFileTrendRepository(seed_trends=get_seed_trends())
        else:
            raise ValueError(f"Unknown ENGINE: {settings.ENGINE}")
    return _trend_repository
