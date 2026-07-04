from pydantic import BaseModel
from datetime import datetime


class DocumentResponse(BaseModel):
    id: int
    filename: str
    file_size: int
    uploaded_by: int
    created_at: datetime

    class Config:
        from_attributes = True
