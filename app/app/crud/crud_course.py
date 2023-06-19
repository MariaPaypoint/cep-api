from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate


class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: CourseCreate, user: int
    ) -> Course:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user=user)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, user: int, skip: int = 0, limit: int = 100
    ) -> List[Course]:
        return (
            db.query(self.model)
            .filter(Course.user == user)
            .offset(skip)
            .limit(limit)
            .all()
        )


course = CRUDCourse(Course)
