from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.course import create_random_course


def test_create_course(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"name": "string", "language": "en", "image": "string", "is_active": True, "description": "string"}
    response = client.post(
        f"{settings.API_V1_STR}/courses/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    
    for k, v in data.items():
        assert content[k] == data[k]
        
    assert content["is_verified"] == False
    assert "id" in content


def test_create_course_negative(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"name": "string", "language": "wronglang", "image": "string", "is_active": True, "description": "string"}
    response = client.post(
        f"{settings.API_V1_STR}/courses/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 404


def test_read_course(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    course, _, _  = create_random_course(db)
    response = client.get(
        f"{settings.API_V1_STR}/courses/{course.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    
    for k, v in content.items():
        assert course.__getattribute__(k) == content[k]
    
def test_verify_course(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    course, _, _  = create_random_course(db)
    response = client.post(
        f"{settings.API_V1_STR}/courses/verify/{course.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["is_verified"] == True
    
def test_search_courses(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    course, _, user  = create_random_course(db, is_active=True)
    client.post(
        f"{settings.API_V1_STR}/courses/verify/{course.id}",
        headers=superuser_token_headers,
    )
    
    response = client.get(
        f"{settings.API_V1_STR}/courses/search/",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()[0]
    
    for k in ['name', 'language', 'image', 'description', 'owner_id']:
        assert course.__getattribute__(k) != None
        
    
