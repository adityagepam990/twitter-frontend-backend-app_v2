from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_for_you_tab_returns_all_posts():
    response = client.get("/api/v1/feed", params={"tab": "for-you"})
    assert response.status_code == 200
    assert len(response.json()) == 12


def test_following_tab_returns_only_followed_authors():
    response = client.get("/api/v1/feed", params={"tab": "following"})
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 6
    assert all(post["author_followed"] for post in posts)


def test_feed_is_ordered_newest_first():
    response = client.get("/api/v1/feed", params={"tab": "for-you"})
    timestamps = [post["created_at"] for post in response.json()]
    assert timestamps == sorted(timestamps, reverse=True)


def test_unknown_tab_is_422():
    response = client.get("/api/v1/feed", params={"tab": "trending"})
    assert response.status_code == 422
