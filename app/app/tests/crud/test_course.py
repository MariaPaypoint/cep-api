from sqlalchemy.orm import Session

from app import crud
from app.schemas.course import CourseCreate, CourseUpdate, Course
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string, random_boolean
import random

# ================================================================================================================

def random_keyword(db: Session, alias) -> str:

    kvalues = crud.keyword.get_values(db=db, alias=alias)
    return random.choice(kvalues).code

def create_course(db: Session, name = None, language = None, image = None, is_active = None, description = None):
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

# ================================================================================================================


def test_create_course(db: Session) -> None:
    course, data_in, user = create_course(db = db) 
    
    assert course.owner_id == user.id
    for k, v in data_in.items():
        assert course.__getattribute__(k) == data_in[k]


def test_get_course(db: Session) -> None:
    course, data_in, user = create_course(db = db)
    stored_course = crud.course.get(db=db, id=course.id)
    
    #data_in['name'] = '123'
    for k, v in data_in.items():
        assert stored_course.__getattribute__(k) == data_in[k]

def test_update_course(db: Session) -> None:
    course, data_in, user = create_course(db = db)
    
    data_in['description'] = random_lower_string()
    course_update = CourseUpdate(description=data_in['description'])
    course2 = crud.course.update(db=db, db_obj=course, obj_in=course_update)
    
    for k, v in data_in.items():
        assert course2.__getattribute__(k) == data_in[k]


def test_delete_course(db: Session) -> None:
    
    course, data_in, user = create_course(db = db)

    course_removed = crud.course.remove(db=db, id=course.id)
    course_nonexistent = crud.course.get(db=db, id=course.id)
    
    assert course_nonexistent is None
    
    assert course_removed.owner_id == user.id
    for k, v in data_in.items():
        assert course_removed.__getattribute__(k) == data_in[k]
