from backend.models.trend_model import Trend
from backend.repositories.provider import get_trend_repository

TRENDS_LIMIT = 5


def get_trends() -> list[Trend]:
    trends = get_trend_repository().list_trends()
    return trends[:TRENDS_LIMIT]
