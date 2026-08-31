from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_suggested_users_returns_at_most_three_unfollowed():
    response = client.get("/api/v1/users/suggested")
    assert response.status_code == 200
    users = response.json()
    assert len(users) <= 3
    assert all(not user["followed"] for user in users)


def test_follow_toggles_both_directions():
    suggested = client.get("/api/v1/users/suggested").json()
    user_id = suggested[0]["id"]

    followed = client.post(f"/api/v1/users/{user_id}/follow")
    assert followed.status_code == 200
    assert followed.json()["followed"] is True

    unfollowed = client.post(f"/api/v1/users/{user_id}/follow")
    assert unfollowed.status_code == 200
    assert unfollowed.json()["followed"] is False


def test_unknown_user_id_is_404():
    response = client.post("/api/v1/users/does-not-exist/follow")
    assert response.status_code == 404
