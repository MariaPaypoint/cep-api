from typing import Optional

from pydantic import BaseModel


# Shared properties
class LessonBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class LessonCreate(LessonBase):
    title: str


# Properties to receive on item update
class LessonUpdate(LessonBase):
    pass


# Properties shared by models stored in DB
class LessonInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Lesson(LessonInDBBase):
    pass


# Properties properties stored in DB
class LessonInDB(ItemInDBBase):
    pass
