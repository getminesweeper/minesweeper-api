import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Minesweeper"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("minesweeper_api.api:app", host="0.0.0.0", port=8000, reload=True)