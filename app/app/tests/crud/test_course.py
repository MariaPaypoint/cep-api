from sqlalchemy.orm import Session

from app import crud
from app.schemas.course import CourseCreate, CourseUpdate, Course
from app.tests.utils.user import create_random_user
from app.tests.utils.course import create_random_course
from app.tests.utils.utils import random_lower_string, random_boolean
import random

# я не совсем поняла, зачем мне 2 типа тестов на каждую операцию
# тесты ниже работают, но смысла я в них не вижу (и не дополняю)

# def test_create_course(db: Session) -> None:
    # course, data_in, user = create_random_course(db = db) 
    
    # assert course.owner_id == user.id
    # for k, v in data_in.items():
        # assert course.__getattribute__(k) == data_in[k]


# def test_get_course(db: Session) -> None:
    # course, data_in, user = create_random_course(db = db)
    # stored_course = crud.course.get(db=db, id=course.id)
    
    ##data_in['name'] = '123'
    # for k, v in data_in.items():
        # assert stored_course.__getattribute__(k) == data_in[k]

# def test_update_course(db: Session) -> None:
    # course, data_in, user = create_random_course(db = db)
    
    # data_in['description'] = random_lower_string()
    # course_update = CourseUpdate(description=data_in['description'])
    # course2 = crud.course.update(db=db, db_obj=course, obj_in=course_update)
    
    # for k, v in data_in.items():
        # assert course2.__getattribute__(k) == data_in[k]

# def test_delete_course(db: Session) -> None:
    
    # course, data_in, user = create_random_course(db = db)

    # course_removed = crud.course.remove(db=db, id=course.id)
    # course_nonexistent = crud.course.get(db=db, id=course.id)
    
    # assert course_nonexistent is None
    
    # assert course_removed.owner_id == user.id
    # for k, v in data_in.items():
        # assert course_removed.__getattribute__(k) == data_in[k]
