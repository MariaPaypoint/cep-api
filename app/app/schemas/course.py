from typing import Optional

from pydantic import BaseModel


# Shared properties
class CourseBase(BaseModel):
    pass
    # name_ru: Optional[str] = None
    # name_en: Optional[str] = None
    # description: Optional[str] = None


# Properties to receive on Course creation
class CourseCreate(CourseBase):
    pass
    # name_ru: str
    # name_en: str


# Properties to receive on Course update
class CourseUpdate(CourseBase):
    pass


# Properties shared by models stored in DB
class CourseInDBBase(CourseBase):
    # code: int
    # name_en: str
    # name_ru: str
    # user: int

    class Config:
        orm_mode = True


# Properties to return to client
class Course(CourseInDBBase):
    pass


# Properties properties stored in DB
class CourseInDB(CourseInDBBase):
    pass
