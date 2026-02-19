from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo.errors import ConfigurationError, ConnectionFailure
from fastapi.concurrency import run_in_threadpool   

from backend.main import data_ingestion_pipeline, answer_question

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

templates = Jinja2Templates(directory="frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_file(request: Request):
    try:
        file = await request.form()
        file_path = file["filepath"]
        data_ingestion_pipeline(file_path)
        return JSONResponse({"message": "File uploaded successfully"})
    except ConnectionFailure or ConfigurationError as e:
        return JSONResponse({"message": "check your internet connection"}, status_code=500)
    
@app.post("/query")
async def ask_question(request: Request):
    try:
        data = await request.json()
        question = data.get("query")
        print(question)
        answer = await run_in_threadpool(answer_question, question)
        print(answer)
        return JSONResponse({"answer": answer})
    except ConnectionFailure or ConfigurationError as e:
        return JSONResponse({"answer": "check your internet connection"})
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)