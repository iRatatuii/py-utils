from user.utils import collect_user_profile
from user.storage import save_user


if __name__ == "__main__":
    
    profile = collect_user_profile()

    subscription_text = "есть" if profile.has_subscription else "нет"
    activity_text = "активный" if profile.is_active else "сидячий"

    save_user(profile, 'data/profiles.json')
    
    print("\n--- ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ ---")
    print(f"Имя: {profile.name}")
    print(f"Возраст: {profile.age}")
    print(f"Рост: {profile.height}")
    print(f"Вес: {profile.weight}")
    print(f"Подписка: {subscription_text}")
    print(f"Образ жизни: {activity_text}")  