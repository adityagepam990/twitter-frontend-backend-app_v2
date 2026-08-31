from abc import ABC, abstractmethod

from backend.models.trend_model import Trend


class TrendRepository(ABC):
    @abstractmethod
    def list_trends(self) -> list[Trend]: ...
