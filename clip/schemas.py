from typing import Optional

from pydantic import BaseModel, ConfigDict

from base.schemas import FileSchema


class ClipSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    clip_file: FileSchema

    model_config = ConfigDict(from_attributes=True)
