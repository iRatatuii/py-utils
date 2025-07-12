from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    weight: float
    height: int
    is_active: bool
    has_subscription: bool

