from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Course(Base):
    code: int = Column(Integer, primary_key=True, index=True)
    # to do: json
    name_ru = Column(String, index=True)
    name_en = Column(String, index=True)
    image = Column(String)
    removed = Column(Boolean)
    verified = Column(Boolean)
    description = Column(String, index=True)
    user = Column(Integer, ForeignKey("user.id"))
    # to do: think, because Gena/internet doesn't recommend
    #user_link: "User" = relationship("User", back_populates="courses")
