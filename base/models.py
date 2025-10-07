from sqlalchemy import Column, Integer, String

from base import BaseModel


class FileModel(BaseModel):
    __tablename__ = "base_files"

    id = Column(Integer, primary_key=True)
    name = Column(String, default="")
    store_name = Column(String, nullable=False)
