from pydantic import BaseModel
from typing import Optional
#pydantic models
class add_book(BaseModel):
    name:str
    author:str
    rating:str
class update_book(BaseModel):
    name:Optional[str]=None
    author:Optional[str]=None
    rating:Optional[str]=None