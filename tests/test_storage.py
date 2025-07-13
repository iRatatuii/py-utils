import os
import tempfile

from src.user.models import User
from src.user.storage import load_users, save_user
from src.user.storage import find_users_by_name


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


def test_find_users_by_name(tmp_path):
    filepath = tmp_path / "users.json"

    users = [
        User(
            name="Anton",
            age=31,
            height=176,
            weight=83.0,
            is_active=True,
            has_subscription=True,
        ),
        User(
            name="Anastasia",
            age=28,
            height=165,
            weight=60.0,
            is_active=True,
            has_subscription=False,
        ),
        User(
            name="Andrei",
            age=31,
            height=176,
            weight=83.0,
            is_active=True,
            has_subscription=True,
        ),
        User(
            name="Diana",
            age=22,
            height=170,
            weight=55.0,
            is_active=False,
            has_subscription=False,
        ),
    ]

    for user in users:
        save_user(user, filepath)
    results = find_users_by_name("n", filepath)

    assert len(results) == 4
    assert any(u.name == "Andrei" for u in results)
    assert any(u.name == "Anastasia" for u in results)
    assert any(u.name == "Diana" for u in results)
    assert any(u.name == "Anton" for u in results)
