import asyncio

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from base import get_db_atomic, settings
from base.models import FileModel
from clip.models import ClipModel
from clip.schemas import ClipSchema
from clip.utils import generate_store_name, write_file

router = APIRouter(tags=["clip"])


@router.post("/clips")
async def upload_clip(
    name: str,
    description: str,
    data: UploadFile,
    db: AsyncSession = Depends(get_db_atomic),
) -> ClipSchema:
    store_name = generate_store_name()
    file_path = settings.clips_dir / store_name

    clip_file = FileModel(
        name=data.filename,
        store_name=store_name,
    )
    db.add(clip_file)
    await db.flush()

    new_clip = ClipModel(
        name=name,
        description=description,
        clip_file=clip_file.id,
    )
    db.add(new_clip)
    await db.flush()

    # If there is an error during commit, we will delete broken files
    # that do not have an entry in the 'base_files' table in the cron task.
    await asyncio.to_thread(write_file, file_path, data.file)
    return ClipSchema.model_validate(new_clip)
