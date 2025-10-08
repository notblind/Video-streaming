from sqlalchemy import Column, DateTime, Integer, String, func

from base import BaseModel


class DateModelMixin:
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )


class FileModel(BaseModel, DateModelMixin):
    __tablename__ = "base_files"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    store_name = Column(String, nullable=False, unique=True)
