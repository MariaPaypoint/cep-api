import random
import string
from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings
from app import crud
from sqlalchemy.orm import Session

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def random_boolean() -> bool:
    return random.choice([True, False])


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers

def random_keyword(db: Session, alias) -> str:
    kvalues = crud.keyword.get_values(db=db, alias=alias)
    return random.choice(kvalues).code
