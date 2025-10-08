from pydantic import BaseModel, ConfigDict


class FileSchema(BaseModel):
    id: int
    name: str
    store_name: str

    model_config = ConfigDict(from_attributes=True)
