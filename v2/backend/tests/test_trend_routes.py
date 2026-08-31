from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_trends_returns_at_most_five():
    response = client.get("/api/v1/trends")
    assert response.status_code == 200
    trends = response.json()
    assert len(trends) == 5
    for trend in trends:
        assert {"id", "category", "topic", "post_count"} <= trend.keys()
