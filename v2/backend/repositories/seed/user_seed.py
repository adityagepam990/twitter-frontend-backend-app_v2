from backend.models.user_model import User


def get_seed_users() -> list[User]:
    return [
        User(id="u1", display_name="Maya Chen", handle="@mayachen", avatar_url="https://i.pravatar.cc/150?img=1", followed=True),
        User(id="u2", display_name="Jordan Blake", handle="@jblake", avatar_url="https://i.pravatar.cc/150?img=2", followed=True),
        User(id="u3", display_name="Priya Nair", handle="@priyanair", avatar_url="https://i.pravatar.cc/150?img=3", followed=True),
        User(id="u4", display_name="Sam Okafor", handle="@samokafor", avatar_url="https://i.pravatar.cc/150?img=4", followed=True),
        User(id="u5", display_name="Elena Ruiz", handle="@elenaruiz", avatar_url="https://i.pravatar.cc/150?img=5", followed=False),
        User(id="u6", display_name="Tobias Klein", handle="@tklein", avatar_url="https://i.pravatar.cc/150?img=6", followed=False),
        User(id="u7", display_name="Aisha Rahman", handle="@aisharahman", avatar_url="https://i.pravatar.cc/150?img=7", followed=False),
        User(id="u8", display_name="Leo Fontaine", handle="@leofontaine", avatar_url="https://i.pravatar.cc/150?img=8", followed=False),
    ]
