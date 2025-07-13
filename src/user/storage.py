import csv
import json
import os
from dataclasses import asdict

from src.user.models import User


def save_user(user: User, filepath: str) -> None:
    users = []
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                users = [User(**u) for u in data]
            except json.JSONDecodeError:
                users = []
    users.append(user)
                    
    with open(filepath, 'w') as file:
        json.dump(
            [asdict(user) for user in users], file, indent=4, ensure_ascii=False
        )
    

def load_users(filepath: str) -> list[User]:
    if not os.path.exists(filepath):
        return []
    
    with open(filepath, 'r') as file:
        try:
            raw_data = json.load(file)
        except json.JSONDecodeError:
            return []
    return [User(**data) for data in raw_data]


def find_users_by_name(query: str, filepath: str) -> list[User]:
    users = load_users(filepath)
    return [user for user in users if query.lower() in user.name.lower()]


def delete_user_by_name(name: str, filepath: str) -> bool:
    users = load_users(filepath)
    new_users = [u for u in users if u.name.lower() != name.lower()]
    
    if len(new_users) == len(users):
        return False
    
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(
            [asdict(user) for user in new_users],
            file,
            indent=4,
            ensure_ascii=False)
        return True
    
    
def export_users_to_csv(filepath: str, csv_path: str) -> None:
    users = load_users(filepath)
    with open(csv_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Имя", "Возраст", "Рост", "Вес", "Активен", "Подписка"]
        )
        for user in users:
            writer.writerow(
                [
                    user.name,
                    user.age,
                    user.height,
                    user.weight,
                    user.is_active,
                    user.has_subscription,
                ]
            )
