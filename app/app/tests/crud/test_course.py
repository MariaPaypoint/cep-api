from sqlalchemy.orm import Session

from app import crud
from app.schemas.course import CourseCreate, CourseUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_course(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    course_in = CourseCreate(title=title, description=description)
    user = create_random_user(db)
    course = crud.course.create_with_owner(db=db, obj_in=course_in, owner_id=user.id)
    assert course.title == title
    assert course.description == description
    assert course.owner_id == user.id


def test_get_course(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    course_in = CourseCreate(title=title, description=description)
    user = create_random_user(db)
    course = crud.course.create_with_owner(db=db, obj_in=course_in, owner_id=user.id)
    stored_course = crud.course.get(db=db, id=course.id)
    assert stored_course
    assert course.id == stored_course.id
    assert course.title == stored_course.title
    assert course.description == stored_course.description
    assert course.owner_id == stored_course.owner_id


def test_update_course(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    course_in = CourseCreate(title=title, description=description)
    user = create_random_user(db)
    course = crud.course.create_with_owner(db=db, obj_in=course_in, owner_id=user.id)
    description2 = random_lower_string()
    course_update = CourseUpdate(description=description2)
    course2 = crud.course.update(db=db, db_obj=course, obj_in=course_update)
    assert course.id == course2.id
    assert course.title == course2.title
    assert course2.description == description2
    assert course.owner_id == course2.owner_id


def test_delete_course(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    course_in = CourseCreate(title=title, description=description)
    user = create_random_user(db)
    course = crud.course.create_with_owner(db=db, obj_in=course_in, owner_id=user.id)
    course2 = crud.course.remove(db=db, id=course.id)
    course3 = crud.course.get(db=db, id=course.id)
    assert course3 is None
    assert course2.id == course.id
    assert course2.title == title
    assert course2.description == description
    assert course2.owner_id == user.id
