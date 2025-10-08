from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from base.schemas import FileSchema


class ClipSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    clip_file: FileSchema
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
