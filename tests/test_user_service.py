import pytest
from services.user_service import UserService
from models.user import User
from datetime import datetime

class FakeRepo:
    def __init__(self):
        self.users = []

    def get_user_by_email(self, email):
        return next((u for u in self.users if u.email == email), None)

    def create_user(self, name, email):
        u = User(id=len(self.users)+1, name=name, email=email, created_at=datetime.now())
        self.users.append(u)
        return u

    def get_all_users(self):
        return self.users

@pytest.fixture
def service():
    return UserService(FakeRepo())

def test_register_user_success(service):
    user = service.register_user("Иван", "ivan@example.com")
    assert user.id == 1
    assert user.email == "ivan@example.com"

def test_register_user_duplicate(service):
    service.register_user("Иван", "ivan@example.com")
    with pytest.raises(ValueError, match="уже существует"):
        service.register_user("Иван", "ivan@example.com")

def test_register_user_invalid_email(service):
    with pytest.raises(ValueError, match="Некорректный email"):
        service.register_user("Иван", "wrongemail")

def test_register_user_short_name(service):
    with pytest.raises(ValueError, match="Имя должно содержать"):
        service.register_user("A", "a@example.com")
