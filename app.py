import subprocess
import tempfile
import shutil
import os
import uuid
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/ocr")
async def ocr_pdf(file: UploadFile = File(...)):
    with tempfile.TemporaryDirectory() as tmpdir:
        src_path = os.path.join(tmpdir, file.filename)
        pdf_ocr_path = os.path.join(tmpdir, "output.pdf")
        text_path = os.path.join(tmpdir, "output.txt")
        with open(src_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        # Run OCRmyPDF to extract text, using German and English ('-l deu+eng') if needed
        subprocess.run([
            "ocrmypdf",
            "-l", "deu+eng",
            "--force-ocr",
            "--sidecar", text_path,
            src_path, pdf_ocr_path
        ], check=True)
        # Parse text and return structure (very simplified!)
        with open(text_path, encoding="utf-8") as f:
            text = f.read()
        # You would parse/structure this as your sample JSON output; here we just return as simple text
        return JSONResponse(content={"text": text})
