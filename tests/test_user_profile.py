from src.user.utils import collect_user_profile


def test_collect_user_profile(monkeypatch):
    inputs = iter(['Andy', '31', '83.0', '176', 'да', 'нет'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    profile = collect_user_profile()
    
    assert profile.name == 'Andy'
    assert profile.age == 31
    assert profile.weight == 83.0
    assert profile.height == 176
    assert profile.is_active is True
    assert profile.has_subscription is False
