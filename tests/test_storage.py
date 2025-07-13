import os
import tempfile

from src.user.models import User
from src.user.storage import load_users, save_user


def test_save_and_load_user():
    user = User(
        name="Andy",
        age=30,
        height=176,
        weight=83.0,
        is_active=True,
        has_subscription=True,
    )

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
        filepath = temp.name

    try:
        save_user(user, filepath)
        users = load_users(filepath)

        assert len(users) == 1
        assert users[0].name == "Andy"
        assert users[0].age == 30
    finally:
        os.remove(filepath)
