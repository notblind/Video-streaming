import asyncio

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from base import get_db, settings
from base.models import FileModel
from clip.models import ClipModel
from clip.schemas import ClipSchema

router = APIRouter(tags=["clip"])


@router.post("/clips")
async def upload_clip(
    name: str, description: str, data: UploadFile, db: AsyncSession = Depends(get_db)
) -> ClipSchema:
    pass
