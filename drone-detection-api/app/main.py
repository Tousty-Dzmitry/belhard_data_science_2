from fastapi import FastAPI
from app.routes.video import router as video_router

app = FastAPI(title="Drone Detection API")

app.include_router(video_router, prefix="/video", tags=["Video"])
