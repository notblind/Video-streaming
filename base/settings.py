from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    # DB Settings
    ECHO: bool = False
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Clip Settings
    CLIPS_DIR: str

    @property
    def clips_dir(self):
        # CLIPS_DIR = Path("/Users/db.lee/video_stream")
        return Path(self.CLIPS_DIR)


settings = Settings()
