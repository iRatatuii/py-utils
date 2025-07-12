from src.user.models import User


# Сбор пользовательских данных
def collect_user_profile() -> User:
    name: str = ""

    while not name:
        name = input("Имя пользователя: ").strip()

    while True:
        try:
            age = int(input("Возраст: "))
            break
        except ValueError:
            print("Пожалуйста, введите число.")

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

    is_active = input("Активен да/нет: ").lower() == "да"
    has_subscription = input("Имеет подписку да/нет: ").lower() == "да"

    user = User(name=name, 
                age=age, 
                height=height, 
                weight=weight, 
                is_active=is_active, 
                has_subscription=has_subscription)
    return user