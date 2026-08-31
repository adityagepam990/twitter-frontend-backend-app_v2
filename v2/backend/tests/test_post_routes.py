from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_create_post_returns_201_and_appears_first_in_feed():
    response = client.post("/api/v1/posts", json={"text": "Hello from the test suite."})
    assert response.status_code == 201
    created = response.json()
    assert created["body"] == "Hello from the test suite."

    feed = client.get("/api/v1/feed", params={"tab": "for-you"}).json()
    assert feed[0]["id"] == created["id"]


def test_empty_text_is_422():
    response = client.post("/api/v1/posts", json={"text": "   "})
    assert response.status_code == 422


def test_text_over_280_chars_is_422():
    response = client.post("/api/v1/posts", json={"text": "a" * 281})
    assert response.status_code == 422


def test_text_at_280_chars_is_accepted():
    response = client.post("/api/v1/posts", json={"text": "a" * 280})
    assert response.status_code == 201


def test_like_toggles_both_directions():
    feed = client.get("/api/v1/feed", params={"tab": "for-you"}).json()
    oldest_post = feed[-1]
    post_id = oldest_post["id"]
    initial_count = oldest_post["like_count"]

    liked = client.post(f"/api/v1/posts/{post_id}/like")
    assert liked.status_code == 200
    assert liked.json()["like_count"] == initial_count + 1

    unliked = client.post(f"/api/v1/posts/{post_id}/like")
    assert unliked.status_code == 200
    assert unliked.json()["like_count"] == initial_count


def test_unknown_post_id_is_404():
    response = client.post("/api/v1/posts/does-not-exist/like")
    assert response.status_code == 404
