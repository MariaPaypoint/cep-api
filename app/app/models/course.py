from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Course(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    # todo: json?
    name = Column(String)
    language = Column(String, index=True)
    image = Column(String)
    is_deleted = Column(Boolean)
    is_verified = Column(Boolean)
    is_active = Column(Boolean)
    description = Column(String)
    # todo: think, because Gena/internet doesn't recommend
    #user_link: "User" = relationship("User", back_populates="courses")
