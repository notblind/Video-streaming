from typing import Optional

from pydantic import BaseModel, ConfigDict


class ClipSchema(BaseModel):
    name: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
