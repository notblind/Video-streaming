import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from base import get_db, settings
from base.models import FileModel

router = APIRouter(tags=["files"])


@router.get("/files")
async def download_file(
    store_name: str, db: AsyncSession = Depends(get_db)
) -> Response:
    result = await db.execute(
        select(FileModel).where(FileModel.store_name == store_name)
    )
    file_obj = result.scalar_one_or_none()
    if file_obj is None:
        raise HTTPException(status_code=404, detail="File not found")

    file_path = f"{settings.FILES_DIR}/{store_name}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(
        file_path,
        filename=file_obj.name,
        media_type=file_obj.content_type,
    )
