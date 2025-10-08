import shutil
import uuid

from base import settings


def generate_store_name() -> str:
    file_id = uuid.uuid4().hex
    return f"{file_id[:2]}/{file_id}"


def write_file(store_name, content) -> None:
    file_path = settings.files_dir / store_name

    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(content, buffer)
