import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Video streaming app",
    version="0.0.2",
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
