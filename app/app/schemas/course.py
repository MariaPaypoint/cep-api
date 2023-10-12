from typing import Optional

from pydantic import BaseModel


# Shared properties
class CourseBase(BaseModel):
    name: str = None
    language: str = None
    image: Optional[str] = None
    is_active: Optional[bool] = True
    description: Optional[str] = None


# Properties to receive on Course creation
class CourseCreate(CourseBase):
    #id: int
    pass


# Properties to receive on Course update
class CourseUpdate(CourseBase):
    name: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None


# Properties shared by models stored in DB
class CourseInDBBase(CourseBase):
    id: Optional[int] = None
    
    class Config:
        orm_mode = True


# Properties to return to client
class Course(CourseInDBBase):
    is_verified: bool

class CourseInfo(BaseModel):
    id: int = None
    name: str = None
    language: str = None
    image: Optional[str] = None
    description: Optional[str] = None
    owner_id: int = None


# Properties properties stored in DB
class CourseInDB(CourseInDBBase):
    pass
