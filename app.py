import subprocess
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import tempfile
import os

app = FastAPI()

@app.post("/ocr")
async def ocr_pdf(file: UploadFile = File(...)):
    with tempfile.TemporaryDirectory() as tmpdir:
        src_pdf = os.path.join(tmpdir, "input.pdf")
        dst_pdf = os.path.join(tmpdir, "output.pdf")
        with open(src_pdf, "wb") as f:
            shutil.copyfileobj(file.file, f)
        result = subprocess.run(["ocrmypdf", src_pdf, dst_pdf], capture_output=True)
        if result.returncode != 0:
            return {"error": result.stderr.decode()}
        return FileResponse(dst_pdf, media_type="application/pdf", filename="output.pdf")
