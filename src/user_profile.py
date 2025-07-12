
# Сбор пользовательских данных
def collect_user_profile() -> dict:
    name: str = ''
    
    while not name:
        name = input('Имя пользователя: ').strip()

    while True:
        try:
            age = int(input("Возраст: "))
            break
        except ValueError:
            print('Пожалуйста, введите число.')
            
    while True:
        try:
            weight = float(input("Вес: "))
            break
        except ValueError:
            print("Пожалуйста, введите число.")

    while True:       
        try:
            height = int(input("Рост: "))
            break
        except ValueError:
            print("Пожалуйста, введите число.")
            
    is_active = input("Активен да/нет: ").lower() == 'да'
    has_subscription = input("Имеет подписку да/нет: ").lower() == "да"
    
    user_dict = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "is_active": is_active,
        "has_subscription": has_subscription
    }
    return user_dict


if __name__ == '__main__':
    profile = collect_user_profile()
    
    subscription_text = "есть" if profile['has_subscription'] else "нет"
    activity_text = "активный" if profile['is_active'] else "сидячий"
    
    print("\n--- ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ ---")
    print(f"Имя: {profile['name']}")
    print(f"Возраст: {profile['age']}")
    print(f"Рост: {profile['height']}")
    print(f"Вес: {profile['weight']}")
    print(f"Подписка: {subscription_text}")
    print(f"Образ жизни: {activity_text}")
    
    