import ast
import copy
from datetime import UTC, datetime
from pathlib import Path

from backend.models.post_model import Post
from backend.models.trend_model import Trend
from backend.models.user_model import User
from backend.repositories.engines.jsonfile.jsonfile_post_repository import JsonFilePostRepository
from backend.repositories.engines.jsonfile.jsonfile_trend_repository import JsonFileTrendRepository
from backend.repositories.engines.jsonfile.jsonfile_user_repository import JsonFileUserRepository
from backend.repositories.engines.memory.memory_post_repository import MemoryPostRepository
from backend.repositories.engines.memory.memory_trend_repository import MemoryTrendRepository
from backend.repositories.engines.memory.memory_user_repository import MemoryUserRepository
from backend.repositories.seed.post_seed import get_seed_posts
from backend.repositories.seed.trend_seed import get_seed_trends
from backend.repositories.seed.user_seed import get_seed_users

BACKEND_ROOT = Path(__file__).resolve().parents[1]


def _run_post_contract(repository) -> list[Post]:
    repository.set_like("p1", "u9", True)
    repository.set_repost("p1", "u9", True)
    repository.set_like("p2", "u1", True)
    repository.set_like("p2", "u1", False)
    new_post = Post(
        id="p_new",
        author_id="u1",
        author_name="Maya Chen",
        author_handle="@mayachen",
        author_avatar_url="https://i.pravatar.cc/150?img=1",
        author_followed=True,
        body="contract test post",
        created_at=datetime(2026, 1, 1, tzinfo=UTC),
        reply_count=0,
        repost_count=0,
        like_count=0,
    )
    repository.create_post(new_post)
    return sorted(repository.list_posts(), key=lambda post: post.id)


def test_post_repository_contract_matches_across_engines(tmp_path: Path):
    seed_posts = get_seed_posts()
    memory_repo = MemoryPostRepository(seed_posts=copy.deepcopy(seed_posts))
    jsonfile_repo = JsonFilePostRepository(path=tmp_path / "posts.json", seed_posts=copy.deepcopy(seed_posts))

    assert _run_post_contract(memory_repo) == _run_post_contract(jsonfile_repo)


def _run_user_contract(repository) -> list[User]:
    repository.set_followed("u5", True)
    repository.set_followed("u1", False)
    return sorted(repository.list_users(), key=lambda user: user.id)


def test_user_repository_contract_matches_across_engines(tmp_path: Path):
    memory_repo = MemoryUserRepository(seed_users=get_seed_users())
    jsonfile_repo = JsonFileUserRepository(path=tmp_path / "users.json", seed_users=get_seed_users())

    assert _run_user_contract(memory_repo) == _run_user_contract(jsonfile_repo)


def test_trend_repository_contract_matches_across_engines(tmp_path: Path):
    memory_repo = MemoryTrendRepository(seed_trends=get_seed_trends())
    jsonfile_repo = JsonFileTrendRepository(path=tmp_path / "trends.json", seed_trends=get_seed_trends())

    memory_result = sorted(memory_repo.list_trends(), key=lambda trend: trend.id)
    jsonfile_result = sorted(jsonfile_repo.list_trends(), key=lambda trend: trend.id)
    assert memory_result == jsonfile_result


def test_jsonfile_engine_persists_across_instances(tmp_path: Path):
    path = tmp_path / "persisted_posts.json"
    first = JsonFilePostRepository(path=path, seed_posts=get_seed_posts())
    first.set_like("p1", "u9", True)

    second = JsonFilePostRepository(path=path)
    assert "u9" in second.get_post("p1").liked_by


def _imports_repository_engines(path: Path) -> bool:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any("repositories.engines" in alias.name for alias in node.names):
                return True
        elif isinstance(node, ast.ImportFrom):
            if node.module and "repositories.engines" in node.module:
                return True
    return False


def test_only_provider_imports_storage_engines():
    offenders = [
        str(path.relative_to(BACKEND_ROOT))
        for path in BACKEND_ROOT.rglob("*.py")
        if path.name != "provider.py"
        and "engines" not in path.parts
        and "tests" not in path.parts
        and _imports_repository_engines(path)
    ]
    assert offenders == []
