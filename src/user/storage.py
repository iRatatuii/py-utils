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
    
    