from pydantic import BaseModel, ConfigDict
from datetime import datetime

class FileCreate(BaseModel):
    name: str
    path: str
    extension: str
    size: int
    modified_at: datetime


class FileResponse(BaseModel):
    id: int
    name: str
    path: str
    extension: str
    size: int
    modified_at: datetime
    
    model_config = ConfigDict(from_attributes=True)