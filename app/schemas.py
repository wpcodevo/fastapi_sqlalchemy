from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class NoteBaseSchema(BaseModel):
    id: Optional[str] = None  
    title: str
    content: str
    category: Optional[str] = None  
    published: bool = False
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    class Config:
        orm_mode = True  
        arbitrary_types_allowed = True  

# Schema for partial updates (PATCH request)
class NotePatchSchema(NoteBaseSchema):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    published: Optional[bool] = None

class ListNoteResponse(BaseModel):
    status: str
    results: int
    notes: List[NoteBaseSchema]
