import json
from pathlib import Path

from backend.models.trend_model import Trend
from backend.repositories.trend_repository import TrendRepository

_DEFAULT_PATH = Path(__file__).parent / "data" / "trends.json"


def _trend_to_dict(trend: Trend) -> dict:
    return {
        "id": trend.id,
        "category": trend.category,
        "topic": trend.topic,
        "post_count": trend.post_count,
    }


def _dict_to_trend(data: dict) -> Trend:
    return Trend(**data)


class JsonFileTrendRepository(TrendRepository):
    def __init__(self, path: Path | str | None = None, seed_trends: list[Trend] | None = None) -> None:
        self._path = Path(path) if path is not None else _DEFAULT_PATH
        if not self._path.exists():
            self._write(list(seed_trends or []))
        self._trends: dict[str, Trend] = {trend.id: trend for trend in self._read()}

    def _read(self) -> list[Trend]:
        raw = json.loads(self._path.read_text())
        return [_dict_to_trend(item) for item in raw]

    def _write(self, trends: list[Trend]) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._path.write_text(json.dumps([_trend_to_dict(trend) for trend in trends]))

    def list_trends(self) -> list[Trend]:
        return list(self._trends.values())
