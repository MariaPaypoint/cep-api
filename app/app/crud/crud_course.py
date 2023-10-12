from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.crud.base import CRUDBase
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate, CourseInfo


class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):

    def create_with_owner(
        self, db: Session, *, obj_in: CourseCreate, owner_id: int
    ) -> Course:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id, is_verified=False)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100, language: str = None
    ) -> List[Course]:
        queries = [Course.owner_id == owner_id]
        if language:
            queries.append(Course.language == language)
        return (
            db.query(self.model)
            .filter(*queries)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def search_multi(
        self, db: Session, skip: int = 0, limit: int = 100, language: str = None
    ) -> List[CourseInfo]:
        # queries = []
        # if language:
            # queries.append(Course.language == language)
        # return (
            # db.query(self.model)
            # .filter(*queries)
            # .offset(skip)
            # .limit(limit)
            # .all()
        # )
        
        sql = '''
            SELECT id, name, language, image, description, owner_id
            FROM %(course)s
            WHERE 1=1
              AND is_verified = true
              AND is_active   = true
            ORDER BY name
        ''' % {
            'course': Course.__tablename__,
        }
        result = db.execute(text(sql).params({
            # 'alias': alias,
        })).all()
        
        return result


course = CRUDCourse(Course)
