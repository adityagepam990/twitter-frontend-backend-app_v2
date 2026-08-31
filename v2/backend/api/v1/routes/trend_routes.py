from fastapi import APIRouter

from backend.schemas.trend_schema import TrendOut
from backend.services.trend_service import get_trends

router = APIRouter()


@router.get("/trends", response_model=list[TrendOut])
def get_trends_route():
    return get_trends()
