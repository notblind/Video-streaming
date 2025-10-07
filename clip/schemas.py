from typing import Optional

from pydantic import BaseModel


class ClipSchema(BaseModel):
    name: str
    description: Optional[str] = None
