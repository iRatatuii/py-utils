import argparse

from src.user.storage import delete_user_by_name, find_users_by_name, load_users, save_user
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
        "command", choices=["create", "list", 'filter', 'delete'], help="Команда: create или list"
    )
    parser.add_argument("--query", help="Поисковый запрос (для filter)")
    parser.add_argument("--name", help="Имя пользователя (для удаления)")
    
    args = parser.parse_args()
    
    match args.command:
        case 'create':
            handle_create()
        case 'list':
            handle_list()
        case 'filter':
            if not args.query:
                print("❗ Укажи поисковый запрос через --query")
                return
            results = find_users_by_name(args.query, DATA_FILE)
            if not results:
                print("🙁 Никого не найдено")
                return
            print(f"🔍 Найдено {len(results)}:")
            for user in results:
                print(f"— {user.name}, {user.age} лет")
        case 'delete':
            if not args.name:
                print("❗ Укажи имя через --name")
                return
            deleted = delete_user_by_name(args.name, DATA_FILE)
            if deleted:
                print(f"🗑️ Пользователь '{args.name}' удалён.")
            else:
                print(f"🙁 Пользователь '{args.name}' не найден.")
                
                
if __name__ == "__main__":
    main()