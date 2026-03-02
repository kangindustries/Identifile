from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from identifile_core import analyse

app = FastAPI(title="Identifile")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    return Path("static/index.html").read_text(encoding="utf-8")

@app.post("/identify")
async def identify(file: UploadFile = File(...), total_size: int = Form(default=0)):
    data = await file.read(256 * 1024) 
    if not data:
        raise HTTPException(status_code=400, detail="Empty file")
    result = analyse(data, filename=file.filename)
    if total_size > 0:
        result["size"] = total_size
    return JSONResponse(content=result)