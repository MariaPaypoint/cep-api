from typing import Optional, List, Dict

from pydantic import BaseModel


# Shared properties
class KeywordBase(BaseModel):
    alias: str = None


# Properties to receive on Course creation
class KeywordCreate(KeywordBase):
    #id: int
    pass


# Properties to receive on Course update
class KeywordUpdate(KeywordBase):
    pass


# Properties shared by models stored in DB
class KeywordInDBBase(KeywordBase):
    id: Optional[int] = None
    
    class Config:
        orm_mode = True


class KeywordValue(BaseModel):
    code: str
    value: str
    language: str

# Properties to return to client
class Keyword(KeywordInDBBase):
    items: List[KeywordValue] = None


# Properties properties stored in DB
class KeywordInDB(KeywordInDBBase):
    pass
