from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from base import BaseModel


class ClipModel(BaseModel):
    __tablename__ = "clip_clips"

    id = Column(Integer, primary_key=True)
    name = Column(String, default="", nullable=False)
    description = Column(String, default="")
    clip_file_id = Column(Integer, ForeignKey("base_files.id"), nullable=False)

    clip_file = relationship("FileModel")
