from fastapi import FastAPI, UploadFile, File
from app.inference_wrapper import run_inference
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "inputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/generate/")
async def generate(source_image: UploadFile = File(...), driven_audio: UploadFile = File(...)):
    # 一時保存
    source_path = os.path.join(UPLOAD_DIR, source_image.filename)
    audio_path = os.path.join(UPLOAD_DIR, driven_audio.filename)
    with open(source_path, "wb") as f:
        shutil.copyfileobj(source_image.file, f)
    with open(audio_path, "wb") as f:
        shutil.copyfileobj(driven_audio.file, f)

    # 推論呼び出し
    output_path = run_inference(source_path, audio_path)
    return {"output": output_path}
