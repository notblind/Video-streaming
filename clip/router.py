import asyncio

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import select

from base import get_db, get_db_atomic, settings
from base.models import FileModel
from base.utils import generate_store_name, write_file
from clip.constants import ACCEPTABLE_CONTENT_TYPES, ACCEPTABLE_VIDEO_FORMATS
from clip.models import ClipModel
from clip.schemas import ClipSchema

router = APIRouter(tags=["clips"])


@router.get("/clips")
async def get_clip(clip_id: int, db: AsyncSession = Depends(get_db)) -> ClipSchema:
    result = await db.execute(
        select(ClipModel)
        .options(joinedload(ClipModel.clip_file))
        .where(ClipModel.id == clip_id)
    )
    clip = result.scalar_one_or_none()
    if clip is None:
        raise HTTPException(status_code=404, detail="Clip not found")
    return ClipSchema.model_validate(clip)


@router.post("/clips")
async def upload_clip(
    name: str,
    description: str,
    data: UploadFile,
    db: AsyncSession = Depends(get_db_atomic),
) -> ClipSchema:
    content_type = data.content_type
    if content_type not in ACCEPTABLE_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Only videos in the following format can be uploaded: {', '.join(ACCEPTABLE_VIDEO_FORMATS)}",
        )

    store_name = generate_store_name()
    clip_file = FileModel(
        name=data.filename,
        store_name=store_name,
        content_type=content_type,
    )
    db.add(clip_file)
    await db.flush()

    new_clip = ClipModel(
        name=name,
        description=description,
        clip_file_id=clip_file.id,
    )
    db.add(new_clip)
    await db.flush()

    # If there is an error during commit, we will delete broken files
    # that do not have an entry in the 'base_files' table in the cron task.
    await asyncio.to_thread(write_file, store_name, data.file)
    return ClipSchema.model_validate(new_clip)


@router.delete("/clips")
async def delete_clip(clip_id: int, db: AsyncSession = Depends(get_db_atomic)) -> dict:
    clip = await db.get(ClipModel, clip_id)
    if clip is None:
        raise HTTPException(status_code=404, detail="Clip not found")
    await db.delete(clip)
    return {"result": "Ok"}
