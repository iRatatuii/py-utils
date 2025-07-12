import argparse

from src.user.storage import load_users, save_user
from src.user.utils import collect_user_profile

DATA_FILE = 'data/profiles.json'


def handle_create():
    user = collect_user_profile()
    save_user(user, DATA_FILE)


def handle_list():
    users = load_users(DATA_FILE)
    if not users:
        print("🙁 Пока нет ни одного пользователя.")
        return
    print(f"\n📋 В базе {len(users)} пользователей:")
    for user in users:
        print(f"— {user.name}, {user.age} лет, рост {user.height} см")


def main():
    parser = argparse.ArgumentParser(
        description="Управление профилями пользователей"
    )
    parser.add_argument(
        "command", choices=["create", "list"], help="Команда: create или list"
    )
    args = parser.parse_args()
    
    match args.command:
        case 'create':
            handle_create()
        case 'list':
            handle_list()
                
                
if __name__ == "__main__":
    main()