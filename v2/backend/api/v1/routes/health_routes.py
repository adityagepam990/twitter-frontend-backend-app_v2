from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/health")
def get_health():
    return {"status": "ok", "version": "v1"}
