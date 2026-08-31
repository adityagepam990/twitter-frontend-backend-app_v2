from backend.models.trend_model import Trend
from backend.repositories.trend_repository import TrendRepository


class MemoryTrendRepository(TrendRepository):
    def __init__(self, seed_trends: list[Trend] | None = None) -> None:
        self._trends: dict[str, Trend] = {trend.id: trend for trend in (seed_trends or [])}

    def list_trends(self) -> list[Trend]:
        return list(self._trends.values())
