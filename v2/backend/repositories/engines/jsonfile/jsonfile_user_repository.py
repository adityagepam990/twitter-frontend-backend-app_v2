import json
from pathlib import Path

from backend.models.user_model import User
from backend.repositories.user_repository import UserRepository

_DEFAULT_PATH = Path(__file__).parent / "data" / "users.json"


def _user_to_dict(user: User) -> dict:
    return {
        "id": user.id,
        "display_name": user.display_name,
        "handle": user.handle,
        "avatar_url": user.avatar_url,
        "followed": user.followed,
    }


def _dict_to_user(data: dict) -> User:
    return User(**data)


class JsonFileUserRepository(UserRepository):
    def __init__(self, path: Path | str | None = None, seed_users: list[User] | None = None) -> None:
        self._path = Path(path) if path is not None else _DEFAULT_PATH
        if not self._path.exists():
            self._write(list(seed_users or []))
        self._users: dict[str, User] = {user.id: user for user in self._read()}

    def _read(self) -> list[User]:
        raw = json.loads(self._path.read_text())
        return [_dict_to_user(item) for item in raw]

    def _write(self, users: list[User]) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._path.write_text(json.dumps([_user_to_dict(user) for user in users]))

    def _save(self) -> None:
        self._write(list(self._users.values()))

    def list_users(self) -> list[User]:
        return list(self._users.values())

    def get_user(self, user_id: str) -> User | None:
        return self._users.get(user_id)

    def set_followed(self, user_id: str, followed: bool) -> User:
        user = self._users[user_id]
        user.followed = followed
        self._save()
        return user
