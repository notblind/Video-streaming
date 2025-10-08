from fastapi import FastAPI

from base.router import router as router_base
from clip.router import router as router_clips

app = FastAPI(
    title="Video streaming app",
    version="0.0.2",
)
app.include_router(router_base)
app.include_router(router_clips)
