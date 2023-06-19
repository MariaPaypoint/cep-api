from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.course import CourseCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_course(db: Session, *, owner_id: Optional[int] = None) -> models.Course:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    course_in = CourseCreate(title=title, description=description, id=id)
    return crud.course.create_with_owner(db=db, obj_in=course_in, owner_id=owner_id)
