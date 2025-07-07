# import os
# from fastapi import APIRouter, UploadFile, File
# from fastapi.responses import FileResponse
# from app.services.detector import process_video

# UPLOAD_FOLDER = "uploads"
# OUTPUT_FOLDER = "processed_videos"

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# router = APIRouter()

# @router.post("/detect")
# async def detect_video(file: UploadFile = File(...)):
#     input_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     output_path = os.path.join(OUTPUT_FOLDER, f"processed_{file.filename}")

#     with open(input_path, "wb") as f:
#         f.write(await file.read())

#     final_video = process_video(input_path, output_path)

#     return FileResponse(final_video, media_type="video/mp4", filename=os.path.basename(final_video))

import os
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from app.services.detector import process_video

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "processed_videos"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

router = APIRouter()

@router.post("/detect")
async def detect_video(file: UploadFile = File(...)):
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FOLDER, f"processed_{file.filename}")
    with open(input_path, "wb") as f:
        f.write(await file.read())
    final_video = process_video(input_path, output_path)
    return FileResponse(final_video, media_type="video/mp4", filename=os.path.basename(final_video))
