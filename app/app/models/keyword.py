from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

# if TYPE_CHECKING:
    # from .user import User  # noqa: F401


class Keyword_Group(Base):

    __tablename__ = 'keyword_group'
    
    id: int = Column(Integer, primary_key=True, index=True)
    alias = Column(String, unique=True)
    
    values =  relationship("Keyword_Value", back_populates="group")

class Keyword_Value(Base):
    
    __tablename__ = 'keyword_value'
    
    id: int = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("keyword_group.id"), index=True) # 
    code = Column(String)
    value = Column(String)

    group = relationship("Keyword_Group", back_populates="values")
