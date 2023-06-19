from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.course import create_random_course


def test_create_course(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"title": "Foo", "description": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/courses/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


def test_read_course(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    course = create_random_course(db)
    response = client.get(
        f"{settings.API_V1_STR}/courses/{course.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == course.title
    assert content["description"] == course.description
    assert content["id"] == course.id
    assert content["owner_id"] == course.owner_id
