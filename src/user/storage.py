import json
import os
from dataclasses import asdict

from src.user.models import User


def save_user(user: User, filepath: str) -> None:
    users = []
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
        users.append(asdict(user))
                    
    with open(filepath, 'w') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)
    

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
    new_users = [user for user in users if user.name.lower() != name.lower()]
    
    if len(new_users) == len(users):
        return False
    
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump([asdict(user) for user in new_users], file, indent=4, ensure_ascii=False)
        return True