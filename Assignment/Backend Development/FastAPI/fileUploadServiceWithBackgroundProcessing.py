from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import time
from typing import Dict
from PIL import Image

app = FastAPI()

UPLOAD_DIRECTORY = Path("static")
UPLOAD_DIRECTORY.mkdir(exist_ok=True)

processing_status: Dict[str, str] = {}

def generate_thumbnail(file_path: Path, thumbnail_path: Path):
    try:
        time.sleep(5)  # simulate long-running task
        with Image.open(file_path) as img:
            img.thumbnail((100, 100))
            img.save(thumbnail_path)
        processing_status[file_path.name] = "completed"
    except Exception:
        processing_status[file_path.name] = "failed"

@app.post("/upload/image/")
async def upload_image(
    background_tasks: BackgroundTasks,
    image_file: UploadFile = File(...)
):
    if image_file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid image type")
    contents = await image_file.read()
    if len(contents) > 2 * 1024 * 1024:  # 2 MB limit
        raise HTTPException(status_code=400, detail="File too large")

    file_path = UPLOAD_DIRECTORY / image_file.filename
    with open(file_path, "wb") as file_object:
        file_object.write(contents)

    processing_status[image_file.filename] = "processing"
    thumbnail_path = UPLOAD_DIRECTORY / f"thumbnail_{image_file.filename}"
    background_tasks.add_task(generate_thumbnail, file_path, thumbnail_path)

    return JSONResponse({"message": "File received", "filename": image_file.filename})

@app.get("/upload/status/{filename}")
async def check_status(filename: str):
    status = processing_status.get(filename)
    if not status:
        raise HTTPException(status_code=404, detail="File not found")
    return {"filename": filename, "status": status}