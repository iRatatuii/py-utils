import argparse

from src.user.storage import (
    delete_user_by_name,
    export_users_to_csv,
    find_users_by_name,
    load_users,
    save_user,
)
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


def handle_filter(query: str):
    if not query:
        print("❗ Укажи поисковый запрос через --query")
        return
    results = find_users_by_name(query, DATA_FILE)
    if not results:
        print("🙁 Никого не найдено")
        return
    print(f"🔍 Найдено {len(results)}:")
    for user in results:
        print(f"— {user.name}, {user.age} лет")


def handle_delete(name: str) -> None:
    if not name:
        print("❗ Укажи имя через --name")
        return
    deleted = delete_user_by_name(name, DATA_FILE)
    if deleted:
        print(f"🗑️ Пользователь '{name}' удалён.")
    else:
        print(f"🙁 Пользователь '{name}' не найден.")
    

def handle_export(out: str) -> None:
    if not out:
        print("❗ Укажи путь к CSV через --out")
        return
    export_users_to_csv(DATA_FILE, out)
    print(f"📤 Экспорт завершён: {out}")


def parse_args(args):
    match args.command:
        case "create":
            handle_create()
        case "list":
            handle_list()
        case "filter":
            handle_filter(args.query)
        case "delete":
            handle_delete(args.name)
        case "export":
            handle_export(args.out)
    
    
def main():
    parser = argparse.ArgumentParser(
        description="Управление профилями пользователей"
    )
    parser.add_argument(
        "command", 
        choices=["create", "list", 'filter', 'delete', 'export'],
        help="Команда: create или list"
    )
    parser.add_argument("--query", help="Поисковый запрос (для filter)")
    parser.add_argument("--name", help="Имя пользователя (для удаления)")
    parser.add_argument("--out", help="Путь к CSV-файлу (для export)")
    
    args = parser.parse_args()
    
    parse_args(args)
    

if __name__ == "__main__":
    main()