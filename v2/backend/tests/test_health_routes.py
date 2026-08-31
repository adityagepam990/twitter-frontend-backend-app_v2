from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "v1"}


def test_unversioned_health_is_404():
    response = client.get("/health")
    assert response.status_code == 404


def test_unversioned_feed_is_404():
    response = client.get("/api/feed")
    assert response.status_code == 404
