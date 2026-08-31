from datetime import UTC, datetime, timedelta

from backend.models.post_model import Post
from backend.repositories.seed.user_seed import get_seed_users


def get_seed_posts() -> list[Post]:
    authors = {user.id: user for user in get_seed_users()}
    now = datetime.now(UTC)

    def post(post_id, author_id, minutes_ago, body, replies, reposts, likes, image_url=None):
        author = authors[author_id]
        return Post(
            id=post_id,
            author_id=author.id,
            author_name=author.display_name,
            author_handle=author.handle,
            author_avatar_url=author.avatar_url,
            author_followed=author.followed,
            body=body,
            created_at=now - timedelta(minutes=minutes_ago),
            reply_count=replies,
            repost_count=reposts,
            like_count=likes,
            image_url=image_url,
        )

    return [
        post("p1", "u1", 4, "Shipping a small fix before lunch feels like a full day's work.", 3, 1, 42),
        post("p2", "u5", 9, "Does anyone else read release notes for fun? Just me? Cool.", 1, 0, 12),
        post("p3", "u2", 15, "Finally got the CI pipeline under five minutes. Small wins.", 5, 2, 88),
        post("p4", "u6", 22, "Coffee shop wifi holding strong today. Productive morning.", 0, 0, 6),
        post(
            "p5", "u3", 31, "New design tokens are in. Dark mode looks so much better now.", 7, 4, 130,
            image_url="https://picsum.photos/seed/p5/600/400",
        ),
        post("p6", "u7", 38, "Reminder: code review is a conversation, not a courtroom.", 12, 6, 210),
        post("p7", "u4", 47, "Refactored the auth middleware. Fewer lines, same guarantees.", 2, 1, 35),
        post(
            "p8", "u8", 55, "Watching the sunset instead of my terminal for once.", 4, 3, 95,
            image_url="https://picsum.photos/seed/p8/600/400",
        ),
        post("p9", "u1", 63, "PSA: turn on two-factor auth. Today. Right now.", 9, 15, 300),
        post("p10", "u5", 74, "Debugging a race condition felt like untangling headphones.", 6, 2, 58),
        post("p11", "u2", 89, "Pair programming session today reminded me why I love this job.", 3, 1, 47),
        post("p12", "u6", 101, "First cup of coffee, first commit of the day.", 1, 0, 19),
    ]
