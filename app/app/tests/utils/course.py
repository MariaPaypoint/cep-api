from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.course import CourseCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string, random_boolean, random_keyword


# def create_random_course(db: Session, *, owner_id: Optional[int] = None) -> models.Course:
    # if owner_id is None:
        # user = create_random_user(db)
        # owner_id = user.id
        
    # name        = random_lower_string()
    # language    = random_keyword(db=db, alias='language')
    # image       = random_lower_string()
    # is_active   = random_boolean()
    # description = random_lower_string()
    
    # course_in = CourseCreate(title=title, description=description, id=id)
    # return crud.course.create_with_owner(db=db, obj_in=course_in, owner_id=owner_id)


def create_random_course(db: Session, name = None, language = None, image = None, is_active = None, description = None):
    user = create_random_user(db)
    data_in = dict(
        name        = name        or random_lower_string(),
        language    = language    or random_keyword(db=db, alias='language'),
        image       = image       or '', # todo: correct / incorrect url
        is_active   = is_active   or random_boolean(),
        description = description or random_lower_string(),
    )
    course_in = CourseCreate(**data_in)
    course = crud.course.create_with_owner(db=db, obj_in=course_in, owner_id=user.id)
    return course, data_in, user
